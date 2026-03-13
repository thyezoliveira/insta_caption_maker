import csv
import random
from pathlib import Path
from typing import List, Dict, Optional

class instaCM:
    """
    Classe para carregar e processar legendas e hashtags de um arquivo CSV.
    """
    def __init__(self, file_path: str = "arquivo.csv"):
        self.file_path = Path(file_path)

    def _process_hashtags(self, hashtags_raw: str, count: int) -> str:
        """
        Método interno para limpar e selecionar hashtags aleatórias.
        """
        if not hashtags_raw:
            return ""
            
        # Converte em lista e remove espaços extras
        hashtags_list = [h.strip() for h in hashtags_raw.split(' ') if h.strip()]
        
        # Seleciona o número solicitado ou o máximo disponível
        num_to_select = min(count, len(hashtags_list))
        selected = random.sample(hashtags_list, num_to_select)
        
        return " ".join(selected)

    def read_csv(self, num_hashtags: int = 5) -> List[Dict[str, str]]:
        """
        Lê o CSV, valida colunas e processa hashtags.
        :param num_hashtags: Quantidade de hashtags aleatórias a selecionar.
        :return: Lista de dicionários com 'legenda' e 'hashtags'.
        """
        if not self.file_path.exists():
            print(f"Erro: O arquivo '{self.file_path}' não foi encontrado.")
            return []

        processed_data = []

        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                # Validação de cabeçalho
                if not reader.fieldnames or 'legenda' not in reader.fieldnames or 'hashtags' not in reader.fieldnames:
                    print("Erro: O CSV deve conter as colunas 'legenda' e 'hashtags'.")
                    return []

                for row in reader:
                    processed_data.append({
                        "legenda": row['legenda'],
                        "hashtags": self._process_hashtags(row['hashtags'], num_hashtags)
                    })

            return processed_data

        except Exception as e:
            print(f"Erro ao processar CSV: {e}")
            return []

    def generate_caption_files(self, data_list: List[Dict[str, str]], output_dir: str = "captions") -> int:
        """
        Gera arquivos .txt a partir da lista de dados processada.
        :param data_list: Lista de dicionários (legenda e hashtags).
        :param output_dir: Pasta de destino.
        :return: Total de arquivos gerados.
        """
        dest_path = Path(output_dir)
        
        try:
            dest_path.mkdir(parents=True, exist_ok=True)
            
            count = 0
            for i, item in enumerate(data_list, start=1):
                file_path = dest_path / f"caption_{i}.txt"
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"{item['legenda']}\n\n{item['hashtags']}")
                count += 1
                
            print(f"Sucesso: {count} arquivos gerados em '{output_dir}/'.")
            return count

        except Exception as e:
            print(f"Erro ao gerar arquivos: {e}")
            return 0
