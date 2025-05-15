# 🖼️ Visualizador de Imagens 

Atividade ponderada desenvolvida por Davi Nascimento de Jesus.

**Vídeo-demo da solução:** encontre-o [aqui](https://drive.google.com/file/d/1-olajy-yTA4I_h1cOiMG7t7pUFNk7of0/view?usp=sharing).

## 📌 Descrição do Projeto

Este projeto consiste em um **visualizador de imagens interativo**, que permite ao usuário:
- Carregar imagens do computador
- Aplicar múltiplos filtros e transformações
- Visualizar o resultado lado a lado com a imagem original
- Salvar a imagem modificada
- Remover a imagem ou resetar os filtros aplicados

A interface gráfica foi construída com **PySimpleGUI**, e o processamento de imagem com **OpenCV**. O projeto foi estruturado de forma **modular**, com foco em legibilidade, organização e reutilização de código.

---

## 🧱 Organização do Código

O projeto está dividido em três módulos principais:

```
📁 visualizador_imagens/
├── app.py # Interface gráfica e controle dos eventos
├── image_processor.py # Implementação dos filtros (OpenCV)
├── utils.py # Funções auxiliares (carregamento, salvamento, conversão)
└── requirements.txt # Dependências do projeto
```

Essa estrutura modular permite **separar responsabilidades**, facilita a manutenção e torna o sistema extensível (caso em alguma outra ponderada, fosse pedido para adicionar novos filtros, por exemplo).

---

## 🛠️ Funcionalidades Implementadas

- [x] Carregamento de imagem com diálogo de arquivos
- [x] Exibição da imagem original e processada lado a lado
- [x] Aplicação sequencial (acumulativa) dos filtros:
  - Escala de cinza
  - Inversão de cores
  - Aumento de contraste
  - Desfoque
  - Nitidez
  - Detecção de bordas
- [x] Reset dos filtros com restauração da imagem original
- [x] Salvamento da imagem processada
- [x] Remoção da imagem da interface
- [x] **Tratamento de erros e interações com o usuário via popups**:
  - Avisos ao tentar aplicar filtros duplicados que sejam incompatíveis
  - Validação para não aplicar filtros em imagens `None`

---

## ▶️ Como Executar o Projeto

### 1. Clone o repositório

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```
O PySimpleGUI precisa ser instalado via servidor privado:
```bash
python -m pip install --force-reinstall --extra-index-url https://PySimpleGUI.net/install PySimpleGUI
```

### 3. Execute o app
```bash
python main.py
```

### 4. Aplique os filtros e have fun!

Clicando nos botões dos filtros, é possível se divertir com as possibilidades acumulativas que a imagem vai adquirindo. É possível ver um exemplo no vídeo demo da atividade que pode ser encontrado [aqui](https://drive.google.com/file/d/1-olajy-yTA4I_h1cOiMG7t7pUFNk7of0/view?usp=sharing).

## 💬 Considerações Finais

A atividade ponderada proporcionou a revisão de conteúdos vistos em sala, relacionados à aplicação de filtros com a biblioteca da opencv, mas também a obtenção de mais ferramentas para a bagagem como o PySimpleGUI.