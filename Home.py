# Importa os pacotes necessários
import streamlit as st
import datetime
import locale
from datetime import datetime

def app():
    # Adiciona o banner de imagem usando st.image
    st.image("Banner_Home.png", use_column_width=True)

    # Referenciando o arquivo styles.css bo streamlit
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

    st.caption(''':blue[Criado por Victor Ramos França]''')

    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    texto1 = '''Dashboard criado para a pratica dos estudos feitos em Pyhton 3.11.5 e algumas de suas bibliotecas na analisa e exibição de dados em um aplicativo web.'''
    st.markdown(texto1)

    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    st.markdown(''':red[**Extração dos Dados:**]''')
    texto2 = '''Feita com uso de técnicas de Web Scrapping diretamente no site de CBF (https://www.cbf.com.br/futebol-brasileiro/competicoes/).  
    Foram levantados dados de partidas, equipes de arbitragem e clubes participantes dos campeonatos de futebol masculino no período de 2012 à 2024 (ainda em andamento).  
    O código foi construido para buscar por todas as temporadas disponiveis no site e, dentro destas, os jogos e seus respectivos quadros de arbitragem bem como as equipes participantes.  
    Após leitura, identificação e arrumação dos dados do site, estes foram gravados em arquivos .XLSX separadops por grupos (arbitragem, jogos e equipes) para serem, posteriormente, utilizados.  
    **Bibliotecas utilizadas:**  
    - OS:  
    Fornece funções para interagir com o sistema operacional, como manipulação de arquivos e diretórios, variáveis de ambiente e execução de comandos do sistema.  
    - TIME:  
    Permite trabalhar com tempo, incluindo a obtenção da hora atual, pausas na execução do programa (sleep) e medições de tempo.  
    - BeautifulSoup:  
    Biblioteca para extração de dados de arquivos HTML e XML. É amplamente usada para web scraping, permitindo navegar e buscar facilmente em documentos HTML.  
    - Pandas:  
    Biblioteca poderosa para análise e manipulação de dados, oferecendo estruturas de dados como DataFrames e ferramentas para leitura e escrita de dados, limpeza, filtragem e operações estatísticas.
    '''
    st.markdown(texto2)
    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    st.markdown(''':red[**Analise e Exibição dos Dados:**]''')
    texto3 = '''Analise e exibição feita 100% em Python, tendo como base a biblioteca STREAMLIT para facilitar e agilizar o processo de construção das páginas web.  
    Criadas funções para remoção de acentos dos caracteres dentro dos dataset e para a construção e persistência das seleções do menu lateral (Serie e Temporada).  
    Para uma melhor customização das páginas fizemos uso de um arquivo CSS **(styles.css)**, referenciado no streamlit, que permitia a alteração de itens não habilitados no streamlit.  
    Este painel foi dividido em 04 páginas:  
    - **Home:** Apresentação do painel.  
    - **Arbitros:** Exibição de Informações sobre a arbitragem.  
    - **Clubes:** Exibição de Informações sobre os clubes.  
    - **Jogos:** Exibição de Informações sobre as partidas.  
    - **Analise:** Analise das informações levantadas.  
    **Bibliotecas utilizadas:**  
    - Streamlit:  
    Biblioteca para criar aplicações web interativas e personalizadas de forma rápida e fácil, especialmente para visualização de dados e aprendizado de máquina.  
    - Datetime:  
    Fornece classes para manipulação de datas e horas, incluindo operações como aritmética de datas, formatação e parsing.  
    - Pandas:  
    Biblioteca poderosa para análise e manipulação de dados, oferecendo estruturas de dados como DataFrames e ferramentas para leitura e escrita de dados, limpeza, filtragem e operações estatísticas.  
    - Plotly:  
    Biblioteca de visualização de dados que permite criar gráficos interativos e visualmente atraentes, incluindo gráficos 2D e 3D, mapas e dashboards.  
    - NumPy:  
    Biblioteca fundamental para computação científica em Python, fornecendo suporte para arrays multidimensionais e uma variedade de funções matemáticas e estatísticas.  
    - JSON:  
    Biblioteca padrão para trabalhar com dados no formato JSON (JavaScript Object Notation), permitindo serialização (conversão para string) e desserialização (conversão para objeto Python) de dados JSON.  
    - Unidecode:  
    Biblioteca para transliteração de texto Unicode em ASCII, útil para converter caracteres especiais ou acentuados em equivalentes simples.  
    '''
    st.markdown(texto3)
    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    # Define o locale para português (Brasil)
    locale.setlocale(locale.LC_TIME, "pt_BR.utf8")  # Para sistemas Linux/Unix
    # locale.setlocale(locale.LC_TIME, "Portuguese_Brazil.1252")  # Para sistemas Windows

    # Obtém a data e hora atual
    data_atual = datetime.now()

    # Lista com os nomes dos dias da semana em português
    dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

    # Obtém o índice do dia da semana (0 a 6)
    indice_dia_semana = data_atual.weekday()

    # Formata a data no padrão desejado
    data_formatada = data_atual.strftime("%d de %B de %Y %H:%M")
    data_hora = f"{dias_semana[indice_dia_semana]}, {data_formatada}"

    # Exibe a data e hora formatada no Streamlit
    st.caption(data_hora)

    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)