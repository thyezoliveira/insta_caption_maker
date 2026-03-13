import os
from instacaptionmaker import instaCM


def test_generate_caption_files_success(tmp_path):
    """Testa a geração de arquivos .txt a partir de uma lista."""
    output_dir = tmp_path / "captions_teste"
    data = [
        {"legenda": "L1", "hashtags": "#t1 #t2"},
        {"legenda": "L2", "hashtags": "#t3 #t4"}
    ]
    
    icm = instaCM()
    total = icm.generate_caption_files(data, output_dir=str(output_dir))
    
    assert total == 2
    assert os.path.exists(output_dir)
    assert os.path.exists(output_dir / "caption_1.txt")
    assert os.path.exists(output_dir / "caption_2.txt")
    
    # Verifica o conteúdo do primeiro arquivo
    content = (output_dir / "caption_1.txt").read_text(encoding="utf-8")
    assert "L1" in content
    assert "#t1 #t2" in content

def test_generate_caption_files_empty_list(tmp_path):
    """Testa quando a lista de entrada está vazia."""
    output_dir = tmp_path / "captions_vazio"
    icm = instaCM()
    total = icm.generate_caption_files([], output_dir=str(output_dir))
    
    assert total == 0
    # A pasta deve ser criada mesmo que a lista esteja vazia
    assert os.path.exists(output_dir)
    assert len(os.listdir(output_dir)) == 0
