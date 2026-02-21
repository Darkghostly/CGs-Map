import folium

def create_cg_map(cg_data, map_zoom=8):
    """
    Cria um mapa tático interativo de forma 100% dinâmica.
    """
    if cg_data and "coord" in cg_data[0]:
        map_location = cg_data[0]["coord"]
    else:
        map_location = [-23.5505, -46.6333]

    mapa = folium.Map(location=map_location, zoom_start=map_zoom, tiles=None)

    folium.TileLayer('CartoDB dark_matter', name='Visão Tática').add_to(mapa)
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri', name='Satélite (IMINT)', overlay=False, control=True
    ).add_to(mapa)
    
    for cg in cg_data:
        folium.Circle(
            location=cg["coord"], radius=cg["raio_influencia"], color=cg["cor"],
            fill=True, fill_opacity=0.1, weight=1,
        ).add_to(mapa)

    coords_por_id = {cg.get("id"): cg["coord"] for cg in cg_data if "id" in cg}

    for cg in cg_data:
        if "conexoes" in cg:
            origem = cg["coord"]
            for conexao in cg["conexoes"]:
                destino_id = conexao.get("destino")
                if destino_id in coords_por_id:
                    destino = coords_por_id[destino_id]
                    folium.PolyLine(
                        locations=[origem, destino],
                        color=conexao.get("cor", "white"),
                        weight=2.5,
                        opacity=0.8,
                        dash_array="5, 8",
                        tooltip=conexao.get("tipo", "Conexão")
                    ).add_to(mapa)

    for cg in cg_data:
        popup_html = f"""
        <b>Nome:</b> {cg['nome']}<br>
        <b>Tipo:</b> {cg['tipo']}<br>
        <hr style='margin: 3px;'>
        <b>Vulnerabilidade:</b> {cg['vulnerabilidade']}%<br>
        <b>Impacto:</b> {cg['impacto']}
        """
        folium.CircleMarker(
            location=cg["coord"], radius=10, color=cg["cor"],
            fill=True, fill_color=cg["cor"], fill_opacity=0.8,
            popup=folium.Popup(popup_html, max_width=300)
        ).add_to(mapa)

    folium.LayerControl().add_to(mapa)
    return mapa