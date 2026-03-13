# Termo de Abertura de Projeto (TAP) - InstaCaptionMaker

## 1. Identificação do Projeto
- **Nome:** InstaCaptionMaker
- **Versão Inicial:** 1.0.0

## 2. Justificativa
Automatizar a gestão e formatação de legendas e hashtags para o Instagram, reduzindo o trabalho manual de criar arquivos de texto individuais para cada postagem a partir de uma planilha CSV.

## 3. Objetivos
- Desenvolver um leitor de CSV robusto para extração de legendas.
- Criar lógica de seleção aleatória de 5 hashtags para aumentar o alcance orgânico sem repetições excessivas.
- Gerar arquivos `.txt` organizados por numeração automática.

## 4. Requisitos de Alto Nível
- Linguagem: Python 3.12+
- Dependências: Apenas bibliotecas padrão (`os`, `csv`, `random`, `sys`).
- Saída: Pasta `captions/` contendo arquivos numerados.

## 5. Partes Interessadas
- Criadores de conteúdo.
- Gestores de redes sociais.

## 6. Riscos Iniciais
- Formatação incorreta do CSV.
- Falta de hashtags suficientes para a seleção aleatória.
