# InstaCaptionMaker 📸

Um utilitário simples em Python para automatizar a criação de legendas do Instagram a partir de arquivos CSV. O sistema processa legendas, seleciona hashtags aleatoriamente e gera arquivos de texto individuais prontos para uso.

## ✨ Funcionalidades

- **Leitura de CSV:** Processa arquivos com colunas de `legenda` e `hashtags`.
- **Hashtag Mixer:** Seleciona aleatoriamente 5 hashtags de uma lista maior para evitar repetição e Shadowban.
- **Gerador de Arquivos:** Cria automaticamente arquivos `.txt` organizados em uma pasta `captions/`.

## 🚀 Como Usar

1.  **Prepare seu CSV:** Crie um arquivo chamado `arquivo.csv` na raiz do projeto com o seguinte cabeçalho:
    ```csv
    legenda,hashtags
    "Sua legenda aqui","#tag1 #tag2 #tag3..."
    ```
2.  **Execute o Script:**
    ```bash
    python main.py
    ```
3.  **Confira o Resultado:** Os arquivos serão gerados na pasta `/captions` seguindo o padrão `caption_1.txt`, `caption_2.txt`, etc.

## 🛠️ Estrutura do Projeto

- `src/instacaptionmaker.py`: Módulo principal com a classe `instaCM`.
- `main.py`: Ponto de entrada e testes do sistema.
- `docs/`: Documentação e planejamento.

## ✒️ Créditos

Desenvolvido como um protótipo de automação para criadores de conteúdo.
Criado com o auxílio do Gemini CLI.
