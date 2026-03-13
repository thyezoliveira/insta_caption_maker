import csv
import random
import os

class instaCM:
    """
    Classe para carregar e processar legendas e hashtags de um arquivo CSV.
    """
    def __init__(self, file_path="arquivo.csv"):
        self.file_path = file_path

    def read_csv(self):
        """
        Lê o CSV, valida as colunas e processa as hashtags (escolhendo 5 aleatórias).
        Retorna uma lista de dicionários.
        """
        if not os.path.exists(self.file_path):
            print(f"Erro: O arquivo '{self.file_path}' não foi encontrado.")
            return []

        processed_data = []

        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                # Validação básica de colunas
                if 'legenda' not in reader.fieldnames or 'hashtags' not in reader.fieldnames:
                    print("Erro: O CSV deve conter as colunas 'legenda' e 'hashtags'.")
                    return []

                for row in reader:
                    legenda = row['legenda']
                    hashtags_raw = row['hashtags'].strip()
                    
                    # Converte a string de hashtags em uma lista (separando por espaços)
                    # Filtra strings vazias caso haja múltiplos espaços
                    hashtags_list = [h for h in hashtags_raw.split(' ') if h]
                    
                    # Seleciona 5 aleatórias (ou todas se tiver menos de 5)
                    num_to_select = min(5, len(hashtags_list))
                    selected_hashtags = random.sample(hashtags_list, num_to_select)
                    
                    # Junta de volta em uma string separada por espaços
                    hashtags_string = " ".join(selected_hashtags)

                    processed_data.append({
                        "legenda": legenda,
                        "hashtags": hashtags_string
                    })

            return processed_data

        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
            return []

    def generate_caption_files(self, data_list, output_dir="captions"):
        """
        Cria a pasta de destino e gera um arquivo .txt para cada item na lista de dados.
        """
        # Verifica se a pasta existe, caso contrário, cria
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Pasta '{output_dir}' criada com sucesso.")

        count = 0
        for i, item in enumerate(data_list, start=1):
            file_name = f"caption_{i}.txt"
            file_path = os.path.join(output_dir, file_name)
            
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"{item['legenda']}\n\n")
                    f.write(f"{item['hashtags']}")
                count += 1
            except Exception as e:
                print(f"Erro ao criar o arquivo {file_name}: {e}")

        print(f"Processo concluído: {count} arquivos de legenda gerados em '{output_dir}/'.")
        return count
