# main.py
import sys
import os

# Adiciona o diretório src/ ao path do sistema para importar o módulo
sys.path.append(os.path.abspath("src"))

# Importa o módulo instacaptionmaker as icm
import instacaptionmaker as icm

def test_full_process():
    """
    Função de teste para validar o fluxo completo:
    1. Ler o CSV e processar hashtags.
    2. Gerar arquivos .txt na pasta captions/.
    """
    print("--- Iniciando Teste do InstaCaptionMaker ---")
    
    # Instancia a classe
    instancia = icm.instaCM("arquivo.csv")
    
    # FUNCIONALIDADE 1: Leitura do CSV
    print("\n[Etapa 1] Lendo e processando CSV...")
    dados_processados = instancia.read_csv()
    
    if dados_processados:
        print(f"Sucesso! {len(dados_processados)} legendas processadas.")
        
        # FUNCIONALIDADE 2: Geração de Arquivos
        print("\n[Etapa 2] Gerando arquivos de texto...")
        total_gerado = instancia.generate_caption_files(dados_processados)
        
        if total_gerado > 0:
            print("\nTeste concluído com sucesso!")
            print(f"Verifique a pasta 'captions/' para ver os {total_gerado} arquivos.")
    else:
        print("Erro: Não foi possível processar os dados do CSV.")

def main():
    # Executa o fluxo completo de teste
    test_full_process()

if __name__ == "__main__":
    main()
