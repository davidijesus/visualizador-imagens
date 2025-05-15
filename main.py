import PySimpleGUI as sg
import cv2
from processador import *
from utils import load_image, save_image, convert_cv2_to_bytes

sg.theme('DarkGreen') 

layout = [
    [sg.Text('Visualizador de Imagens', font='Any 20')],
    
    # Botões principais (do utils.py)
    [sg.Button('Carregar Imagem'), sg.Button('Limpar'), sg.Button('Salvar Imagem'), sg.Button('Sair')],

    # Botões de filtros (do processador.py)
    [
        sg.Button('Escala de Cinza'), sg.Button('Inverter Cores'),
        sg.Button('Contraste'), sg.Button('Desfoque'),
        sg.Button('Nitidez'), sg.Button('Bordas'),
         
        sg.Button('Resetar') # botão para reset de filtros
    ],

    # Imagens lado a lado (primeiro a original e depois a processada)
    [sg.Image(key='-ORIGINAL-', size=(300, 300)), sg.Image(key='-PROCESSADA-', size=(300, 300))]
]

# Criar janela
window = sg.Window('Visualizador de Imagens', layout, resizable=True)

original = None
processada = None

# Loop da interface
while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, 'Sair'):
        break

    if event == 'Carregar Imagem':
        filepath = sg.popup_get_file('Escolha uma imagem', file_types=(("Imagens", "*.png;*.jpg;*.jpeg"),))
        if filepath:
            original = load_image(filepath)
            processada = original.copy()
            window['-ORIGINAL-'].update(data=convert_cv2_to_bytes(original))
            window['-PROCESSADA-'].update(data=convert_cv2_to_bytes(processada))

    elif event == 'Salvar Imagem' and processada is not None:
        save_path = sg.popup_get_file('Salvar imagem como', save_as=True, file_types=(("PNG", "*.png"),))
        if save_path:
            save_image(processada, save_path)

    elif processada is not None:
        if event == 'Escala de Cinza':
            if len(processada.shape) == 2 or (len(processada.shape) == 3 and processada.shape[2] == 1):
                sg.popup('⚠️ Filtro já aplicado!', 'A imagem já está em escala de cinza.')
            else:
                processada = to_grayscale(processada)
        elif event == 'Inverter Cores':
            processada = invert_colors(processada)
        elif event == 'Contraste':
            # Verifica se imagem está em escala de cinza
            if len(processada.shape) == 2 or (len(processada.shape) == 3 and processada.shape[2] == 1):
              sg.popup('⚠️ Filtro indisponível!', 'O filtro de contraste só pode ser aplicado em imagens coloridas (RGB).')
            else:
              processada = increase_contrast(processada)
        elif event == 'Desfoque':
            processada = blur_image(processada)
        elif event == 'Nitidez':
            processada = sharpen_image(processada)
        elif event == 'Bordas':
            # Verifica se a imagem já parece ser uma borda binarizada
            if len(processada.shape) == 2:
                unique_vals = set(processada.flatten())
                if unique_vals.issubset({0, 255}):
                    sg.popup('⚠️ Filtro já aplicado!', 'A imagem já parece ser uma borda ou binarizada. O filtro não será aplicado novamente.')
                else:
                    processada = detect_edges(processada)
            else:
                processada = detect_edges(processada)
        elif event == 'Resetar' and original is not None:
            processada = original.copy()
        elif event == 'Limpar':
            original = None
            processada = None
            window['-ORIGINAL-'].update(data=None)
            window['-PROCESSADA-'].update(data=None)
    

        window['-PROCESSADA-'].update(data=convert_cv2_to_bytes(processada))

window.close()
