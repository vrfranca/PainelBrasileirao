import streamlit as st
import pandas as pd
import os

# Importa as variáveis globais
from carga_dados import _global_df_arbitros

# Função para criar os itens de seleção do menu lateral
def menu_lateral():
    # Cria um dicionário para armazenar os estados dos checkboxes de série
    if 'selected_series' not in st.session_state:
        st.session_state.selected_series = {'A': True, 'B': True, 'C': True, 'D': True}
    states_series = st.session_state.selected_series

    # Cria um dicionário para armazenar os estados dos checkboxes de temporada
    if 'selected_temporadas' not in st.session_state:
        st.session_state.selected_temporadas = {2024: True, 2023: True, 2022: True, 2021: True}
    states_temporadas = st.session_state.selected_temporadas

    st.sidebar.markdown(
        "<p style='text-align: center;'><strong>Selecione a Série do Brasileirão</strong></p>", 
        unsafe_allow_html=True
    )

    # Divide a barra lateral em duas colunas
    col1, col2 = st.sidebar.columns(2)

    # Cria a lista das séries
    serie = ['A', 'B', 'C', 'D']

    # Exibe checkboxes personalizados em cada série
    for i, valor in enumerate(serie):
        if i % 2 == 0:
            states_series[valor] = col1.checkbox(f"Série {valor}", value=states_series.get(valor, False))
        else:
            states_series[valor] = col2.checkbox(f"Série {valor}", value=states_series.get(valor, False))

    # Usa o estilo personalizado para criar a linha separadora
    st.sidebar.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    st.sidebar.markdown(
        "<p style='text-align: center;'><strong>Selecione a Temporada do Brasileirão</strong></p>", 
        unsafe_allow_html=True
    )

    # Divide a barra lateral em duas colunas
    col1, col2 = st.sidebar.columns(2)

    # Cria a lista das temporadas
    df = _global_df_arbitros
    temporada = df['temporada'].drop_duplicates()
    temporada = sorted(temporada, reverse = True)

    # Exibe checkboxes personalizados em cada temporada
    for i, valor in enumerate(temporada):
        if i % 2 == 0:
            states_temporadas[valor] = col1.checkbox(f"{valor}", value=states_temporadas.get(valor, False))
        else:
            states_temporadas[valor] = col2.checkbox(f"{valor}", value=states_temporadas.get(valor, False))
    
    # Usa o estilo personalizado para criar a linha separadora
    st.sidebar.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)