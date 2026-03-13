# InstaCaptionMaker 📸

Um utilitário simples em Python para automatizar a criação de legendas do Instagram a partir de arquivos CSV. O sistema processa legendas, seleciona hashtags aleatoriamente e gera arquivos de texto individuais prontos para uso.

## ✨ Funcionalidades

- **Leitura de CSV:** Processa arquivos com colunas de `legenda` e `hashtags`.
- **Hashtag Mixer:** Seleciona aleatoriamente 5 hashtags de uma lista maior para evitar repetição e Shadowban.
- **Gerador de Arquivos:** Cria automaticamente arquivos `.txt` organizados em uma pasta `captions/`.

> [!TIP]
> **Dica:** Você pode criar sua planilha com as colunas `legenda` e `hashtags` no **Google Sheets** e depois exportar como **CSV (Valores separados por vírgula)**. O arquivo estará pronto para ser usado pelo sistema!

## 📋 Pré-requisitos

Antes de começar, você precisará ter o **Python (3.12+)** e o **uv** instalados em sua máquina. O `uv` é o gerenciador de pacotes e ambientes utilizado neste projeto.

Para instalar o `uv`, execute o seguinte comando:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Após instalar o `uv`, sincronize o ambiente do projeto:
```bash
uv sync
```

## 🚀 Como Usar

1.  **Prepare seu CSV:** Crie um arquivo chamado `arquivo.csv` na raiz do projeto com o seguinte cabeçalho:
    ```csv
    legenda,hashtags
    "Sua legenda aqui","#tag1 #tag2 #tag3..."
    ```
2.  **Execute o Script:**
    ```bash
    uv run main.py
    ```
3.  **Confira o Resultado:** Os arquivos serão gerados na pasta `/captions` seguindo o padrão `caption_1.txt`, `caption_2.txt`, etc.

## 🛠️ Estrutura do Projeto

- `src/instacaptionmaker.py`: Módulo principal com a classe `instaCM`.
- `main.py`: Ponto de entrada e testes do sistema.
- `docs/`: Documentação e planejamento.

## ✒️ Créditos

Desenvolvido por **Thyéz de Oliveira Monteiro**.

- **Empresa:** [Forjatech](https://forjatech-oficial.netlify.app)
- **Atuação:** Desenvolvedor na **SMECICT** (Secretaria Municipal de Educação, Cultura, Inclusão, Ciência e Tecnologia) em Saquarema.

Este projeto foi realizado com o apoio de ferramentas de IA generativa, aliado a conhecimento técnico especializado, revisão humana e um trabalho criterioso e metódico.
