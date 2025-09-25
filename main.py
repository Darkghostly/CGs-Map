import json
from src.map_generator import create_cg_map

# --- CONFIGURAÇÃO DA MISSÃO ---
INTEL_DATA_PATH = "data/centros_gravidade.json"
OUTPUT_MAP_PATH = "output/mapa_tatico_cg.html"


def run_mission():
    """
    Função principal que executa a geração do mapa.
    """
    # 1. Carregar inteligência do arquivo JSON
    print("1/3 - Carregando dados de inteligência...")
    with open(INTEL_DATA_PATH, 'r', encoding='utf-8') as f:
        centros_de_gravidade = json.load(f)
    print("-> Dados carregados.")

    # 2. Gerar o objeto do mapa tático
    print("2/3 - Gerando visualização tática do mapa...")
    mapa_tatico = create_cg_map(centros_de_gravidade)
    print("-> Mapa gerado em memória.")

    # 3. Salvar o mapa como um arquivo HTML
    print(f"3/3 - Salvando artefato em '{OUTPUT_MAP_PATH}'...")
    mapa_tatico.save(OUTPUT_MAP_PATH)
    print("-> Missão concluída com sucesso!")


if __name__ == "__main__":
    run_mission()