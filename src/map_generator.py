import folium

def create_cg_map(cg_data, map_location=[-23.5505, -46.6333], map_zoom=8):
    """
    Cria um mapa tático interativo.
    Correção: Garante que os marcadores clicáveis fiquem sempre na camada superior.
    """
    mapa = folium.Map(location=map_location, zoom_start=map_zoom, tiles=None)

    folium.TileLayer(
        'CartoDB dark_matter',
        name='Visão Tática'
    ).add_to(mapa)

    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Satélite (IMINT)',
        overlay=False,
        control=True
    ).add_to(mapa)
    
    # --- MUDANÇA ESTRATÉGICA: ORDEM DE RENDERIZAÇÃO ---
    # Para garantir a clicabilidade, vamos desenhar os elementos em duas passadas.

    # 1. Primeiro, desenhar todas as áreas de influência (camada inferior)
    for cg in cg_data:
        folium.Circle(
            location=cg["coord"],
            radius=cg["raio_influencia"],
            color=cg["cor"],
            fill=True,
            fill_opacity=0.1,
            weight=1,
        ).add_to(mapa)

    # 2. Em seguida, desenhar todos os marcadores de alvo (camada superior)
    for cg in cg_data:
        popup_html = f"""
        <b>Nome:</b> {cg['nome']}<br>
        <b>Tipo:</b> {cg['tipo']}<br>
        <hr style='margin: 3px;'>
        <b>Vulnerabilidade:</b> {cg['vulnerabilidade']}%<br>
        <b>Impacto:</b> {cg['impacto']}
        """
        folium.CircleMarker(
            location=cg["coord"],
            radius=10,
            color=cg["cor"],
            fill=True,
            fill_color=cg["cor"],
            fill_opacity=0.8,
            popup=folium.Popup(popup_html, max_width=300)
        ).add_to(mapa)

    # -----------------------------------------------------------

    # Adiciona as linhas de dependência
    if len(cg_data) >= 4:
        folium.PolyLine(
            locations=[cg_data[0]["coord"], cg_data[2]["coord"]],
            color="yellow", weight=2.5, opacity=0.8, dash_array="5, 10",
            tooltip="Dependência Energética Crítica"
        ).add_to(mapa)
        
        folium.PolyLine(
            locations=[cg_data[1]["coord"], cg_data[3]["coord"]],
            color="cyan", weight=2, opacity=0.7, dash_array="5, 5",
            tooltip="Dependência de Comunicação"
        ).add_to(mapa)

    folium.LayerControl().add_to(mapa)

    return mapa