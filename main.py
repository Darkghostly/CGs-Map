import json
import os
from src.map_generator import create_cg_map


INTEL_DATA_PATH = "data/centros_gravidade.json"
OUTPUT_MAP_PATH = "output/mapa_tatico_cg.html"


def run_mission():
    print("1/3 - Carregando dados de inteligência...")
    with open(INTEL_DATA_PATH, 'r', encoding='utf-8') as f:
        centros_de_gravidade = json.load(f)
    print("-> Dados carregados.")

    print("2/3 - Gerando visualização tática do mapa...")
    mapa_tatico = create_cg_map(centros_de_gravidade)
    print("-> Mapa gerado em memória.")

    print(f"3/3 - Salvando artefato em '{OUTPUT_MAP_PATH}'...")

    os.makedirs(os.path.dirname(OUTPUT_MAP_PATH), exist_ok=True)
    
    mapa_tatico.save(OUTPUT_MAP_PATH)
    print("-> Missão concluída com sucesso!")


if __name__ == "__main__":
    run_mission()