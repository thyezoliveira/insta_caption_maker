# Plano do Projeto

Este arquivo contém o planejamento para o InstaCaptionMaker.

## Funcionalidade 1: Leitor de CSV

Desenvolver um módulo robusto para leitura de arquivos CSV, que será integrado ao `main.py`.

### Requisitos:
- **Arquivo Alvo:** `arquivo.csv`.
- **Estrutura do CSV:** Deve conter obrigatoriamente as colunas `legenda` e `hashtags`.
- **Processamento de Hashtags:**
    - As hashtags no CSV estão separadas por espaços (ex: `#h1 #h2`).
    - O leitor deve converter essa string em uma lista.
    - Selecionar aleatoriamente 5 hashtags (ou todas, caso existam menos de 5).
    - Retornar as hashtags selecionadas como uma string única separada por espaços.
- **Objetivo:** O módulo deve processar o arquivo e retornar uma lista de dicionários contendo `legenda` e a string de `hashtags` processada.
- **Tratamento de Erros:** Validar se o arquivo existe e se as colunas necessárias estão presentes.

## Funcionalidade 2: Gerador de Arquivos de Legenda

Criar uma funcionalidade que utiliza a lista de dicionários processada para gerar arquivos de texto individuais.

### Requisitos:
- **Estrutura de Pastas:** Verificar a existência da pasta `captions/` e criá-la caso não exista.
- **Processamento:** Iterar sobre a lista de dicionários recebida como parâmetro.
- **Saída de Arquivos:**
    - Criar um arquivo `.txt` para cada item da lista.
    - Padrão de nomenclatura: `caption_1.txt`, `caption_2.txt`, etc.
- **Conteúdo do Arquivo:** Cada arquivo deve conter a `legenda` seguida pelas `hashtags` selecionadas.
- **Objetivo:** Automatizar a criação de arquivos prontos para uso em postagens, organizados em uma pasta dedicada.