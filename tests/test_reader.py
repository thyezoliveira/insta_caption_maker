import os
import pytest
from instacaptionmaker import instaCM

def test_read_csv_success(tmp_path):
    """Testa a leitura bem-sucedida de um CSV válido."""
    csv_file = tmp_path / "teste_sucesso.csv"
    # Removendo aspas simples literais do conteúdo do CSV para evitar erro na comparação
    csv_file.write_text("legenda,hashtags\nLegenda 1,#h1 #h2 #h3 #h4 #h5 #h6", encoding="utf-8")
    
    icm = instaCM(str(csv_file))
    result = icm.read_csv()
    
    assert len(result) == 1
    assert result[0]["legenda"] == "Legenda 1"
    # Verifica se selecionou exatamente 5 hashtags
    hashtags = result[0]["hashtags"].split(" ")
    assert len(hashtags) == 5
    # Verifica se as hashtags são subconjunto das originais
    original_tags = ["#h1", "#h2", "#h3", "#h4", "#h5", "#h6"]
    for tag in hashtags:
        assert tag in original_tags

def test_read_csv_fewer_than_5_hashtags(tmp_path):
    """Testa quando há menos de 5 hashtags no CSV."""
    csv_file = tmp_path / "teste_poucas.csv"
    csv_file.write_text("legenda,hashtags\nLegenda 2,#tag1 #tag2", encoding="utf-8")
    
    icm = instaCM(str(csv_file))
    result = icm.read_csv()
    
    assert len(result) == 1
    hashtags = result[0]["hashtags"].split(" ")
    assert len(hashtags) == 2
    assert "#tag1" in hashtags
    assert "#tag2" in hashtags

def test_read_csv_missing_file():
    """Testa o comportamento quando o arquivo não existe."""
    icm = instaCM("arquivo_fantasma.csv")
    result = icm.read_csv()
    assert result == []

def test_read_csv_wrong_columns(tmp_path):
    """Testa quando as colunas obrigatórias estão ausentes."""
    csv_file = tmp_path / "teste_colunas.csv"
    csv_file.write_text("coluna1,coluna2\nvalor1,valor2", encoding="utf-8")
    
    icm = instaCM(str(csv_file))
    result = icm.read_csv()
    assert result == []
