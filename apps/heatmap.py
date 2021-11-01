import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title('Heatmaps')

    filepath ="https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    m = leafmap.Map(tiles="stamentoner")
    m.add_heatmap(
        filepath,
        latitude="lat",
        longitude="lon",
        value="cases",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(width=700, height=500)
