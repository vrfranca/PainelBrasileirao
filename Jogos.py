import streamlit as st

def app():
    # Adiciona o banner de imagem usando st.image
    st.image("Banner_Jogos.png", use_column_width=True)
    
    # Referenciando o arquivo styles.css bo streamlit
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

    st.header('''Página em Construção :construction:''')