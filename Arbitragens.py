# Importa os pacotes necessários
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Importa as variáveis globais
from carga_dados import _global_df_capitais
from carga_dados import _global_df_arbitros
from carga_dados import _global_df_geojson

def app():
    # Adiciona o banner de imagem usando st.image
    st.image("Banner_Arbitragem.png", use_column_width=True)

    # Referenciando o arquivo styles.css bo streamlit
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

    # Acesse os dados armazenados na variável global
    df_capitais = _global_df_capitais
    df_geojson = _global_df_geojson
    df_arbitros = _global_df_arbitros

    # Carrega os dados de serie e temporada selecionados no menu
    series_selecionadas = st.session_state.selected_series
    temporadas_selecionadas = st.session_state.selected_temporadas

    # Obtém as séries selecionadas (com valor True)
    series = [serie for serie, valor in series_selecionadas.items() if valor]

    # Obtém as temporadas selecionadas (com valor True)
    temporadas = [temporada for temporada, valor in temporadas_selecionadas.items() if valor]

    # Determina a temporada incial e final selecionada
    t_inicial = min(temporadas)
    t_final = max(temporadas)

    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    # Divide a area de página em 03 colunas
    col1, col2, col3 = st.columns(3)

    # Cria os menus de pagina e coleta os valores selecionados nas respectivas variaveis
    df = df_arbitros.sort_values(by = ["funcao"])
    funcao = col1.multiselect("Selecione a Função:", ["Todas"] + list(df["funcao"].unique()), default = ["Todas"])
    df = df_arbitros.sort_values(by = ["quadro"])
    quadro = col2.selectbox("Selecio o Quadro:", ["Todos"] + list(df["quadro"].unique()), placeholder = "Selecione o Quadro"
                                , index = 0)
    df = df_arbitros.sort_values(by = ["federacao"])
    federacao = col3.selectbox("Selecione a Federação:", ["Todas"] + list(df["federacao"].unique()), placeholder = "Selecione a Federação"
                                    , index = 0)

    # Aplica os filtros do menu no dataset
    df_filtro1 = df_arbitros[df_arbitros["serie"].isin(series)]
    df_filtro2 = df_filtro1[(df_filtro1["temporada"] >= t_inicial) & (df_filtro1["temporada"] <= t_final)]
    if "Todas" in funcao:
        df_filtro3 = df_filtro2
    else:
        df_filtro3 = df_filtro2[df_filtro2["funcao"].isin(funcao)]
    if quadro == "Todos":
        df_filtro4 = df_filtro3
    else:
        df_filtro4 = df_filtro3[df_filtro3["quadro"] == quadro]
    if federacao == "Todas":
        df_filtro5 = df_filtro4
    else:
        df_filtro5 = df_filtro4[df_filtro4["federacao"] == federacao]
    df_arbitros = df_filtro5
    df_arbitros['temporada'] = df_arbitros['temporada'].apply(str)

    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    st.markdown(''':blue[***TOP 10 Profisisonais Mais Escalados***]''')

    # Exibição dos dados

    # Definir um plano de cores específico
    color_sequence = ['#F0F0F0', '#FFD700', '#009B3A', '#002776']

    ## Exibindo a tabela com os dados selecionados
    # Excluido colunas especificas do dataset para criar uma lista de arbitros
    lista = df_arbitros.drop(["serie", "temporada", "jogo"], axis = 1)
    # Calcula a contagem de ocorrências de cada nome
    contagem = lista['nome'].value_counts().reset_index()
    contagem.columns = ['nome', 'escalações']
    # Agrupa e agrega os valores únicos de arbitros em listas
    lista = lista.groupby("nome").agg({
        'quadro': lambda x: list(set(x)),
        'federacao': lambda x: list(set(x)),
        'funcao': lambda x: list(set(x)),
    }).reset_index()
    # Junta a contagem de ocorrências com o DataFrame agregado
    lista = pd.merge(lista, contagem, on = 'nome')
    # Reordena as colunas para que "escalações" seja a primeira coluna
    cols = ['escalações'] + [col for col in lista.columns if col != 'escalações']
    lista = lista[cols]
    # Seleciona os 10 nomes com maior quantidade de escalações
    lista = lista.nlargest(10, 'escalações')
    # Ordena a lista em ordem descrescente pela quantidade de escalações
    lista = lista.sort_values("escalações", ascending = False)
    # Exibi a lista com os top 10 arbitros com mais escalações
    st.write("""
        <div style='height: 400px; overflow-y: scroll;'>
            """ + lista.to_html(index=False) + """
        </div>
        """, unsafe_allow_html=True)

    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    st.markdown(''':blue[***Qtde de Profisisonais por Temporada***]''')
    ## Cria e exibe os gráficos da página
    ### Quantidade de Arbitros utilizados em cada temporada
    arb_ano = df_arbitros.groupby("temporada")["nome"].nunique().reset_index()
    arb_ano.rename(columns = {"nome": "Qtde.", "temporada": "Temporada"}, inplace = True)
    fig1 = px.bar(arb_ano, 
                x = "Temporada", 
                y = "Qtde." 
    )
    fig1.update_traces(texttemplate='%{y}', textposition='outside')
    fig1.update_yaxes(showticklabels=False)
    # Atualizando o eixo X para mostrar apenas valores existentes
    fig1.update_xaxes(type='category')
    st.plotly_chart(fig1)

    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    st.markdown(''':blue[***Qtde de Profisisonais por Função***]''')
    ### Quantidade de Arbitros por função
    arb_func = df_arbitros.groupby("funcao")["nome"].nunique().reset_index()
    arb_func.rename(columns = {"nome": "Qtde.", "funcao": "Função"}, inplace = True)
    arb_func_sorted = arb_func.sort_values("Função", ascending = False)
    fig2 = px.bar(arb_func_sorted, 
                x = "Qtde.", 
                y = "Função", 
                title = "Arbitros por Função"
    )
    fig2.update_traces(texttemplate='%{x}', textposition='outside')
    fig2.update_xaxes(showticklabels=False)
    st.plotly_chart(fig2)

    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    # Divide a area de página em 02 colunas
    col1, col2 = st.columns(2)

    col1.markdown(''':blue[***Qtde de Profisisonais por Federação***]''')
    ### Quantidade de Arbitros por federação
    arb_fed = df_arbitros.groupby("federacao")["nome"].nunique().reset_index()
    arb_fed = arb_fed.rename(columns = {"nome": "Qtde", "federacao": "Sigla"})
    arb_fed = pd.merge(arb_fed, df_capitais, on = "Sigla", how = "left")
    arb_fed = arb_fed.rename(columns = {"Sigla": "Info"})
    #### Define uma posição na Ilha de Trindade para os arbitros sem estado definido no dataset
    arb_fed["latitude"] = arb_fed["latitude"].fillna(-20.5000)
    arb_fed["longitude"] = arb_fed["longitude"].fillna(-29.3167)
    arb_fed = arb_fed.rename(columns = {"Info": "Sigla"})
    fig3 = px.choropleth(arb_fed, 
                        geojson = df_geojson,
                        locations = 'Sigla',
                        color = 'Qtde',
                        color_continuous_scale = color_sequence,  # Escolha a escala de cores
                        range_color = (12, 124),  # Defina o intervalo de cores
                        hover_data = ['Estado', 'Sigla', 'Capital'],
                        scope = 'south america',
                        center = {'lat': -15, 'lon': -55},  # Coordenadas do centro do mapa
                        width = 700, 
                        height = 700
    )
    fig3.update_geos(projection_scale = 2) # Nível de zoom inicial
    fig3.update_coloraxes(showscale = False) # oculta a barra de medida lateral
    ## Ajustar o layout para aumentar o mapa e reduzir o tamanho da barra de cores
    fig3.update_layout(
        margin={"r":0,"t":50,"l":0,"b":0},
        coloraxis_colorbar={
            'len': 0.5,  # Ajuste a altura da barra de cores
            'y': 0.5,  # Posicione a barra de cores mais centralizada verticalmente
            'thickness': 15,  # Ajuste a espessura da barra de cores
            'x': 0.9,  # Posicione a barra de cores mais para a direita
            'xanchor': 'center'
        }
    )
    col1.plotly_chart(fig3)

    ### Quantidade de Arbitros por Serie
    col2.markdown(''':blue[***Qtde de Profissionais por Serie***]''')

    arb_serie = df_arbitros.groupby("serie")["nome"].nunique().reset_index()
    arb_serie.rename(columns={"nome": "Qtde.", "serie": "Serie"}, inplace=True)

    arb_serie = arb_serie.sort_values(by='Qtde.', ascending=True)

    # Calcular a quantidade total de profissionais
    total_profissionais = arb_serie['Qtde.'].sum()

    # Criação do gráfico de pizza com Plotly
    fig4 = go.Figure()

    fig4.add_trace(go.Pie(
        labels=['Série ' + serie for serie in arb_serie['Serie']],
        values=arb_serie['Qtde.'],
        hole=0.3,  # Para criar um gráfico de rosca
        pull=[0, 0, 0, 0.1],  # Puxa o primeiro pedaço para dar uma sensação de 3D
        marker=dict(colors=color_sequence),
        hoverinfo='label+value+percent',
        textinfo='label+value+percent',
        textposition='inside',
        showlegend=False,
    ))

    # Atualizar o hovertemplate para adicionar o prefixo
    fig4.update_traces(hovertemplate='Serie %{label}: %{value} árbitros')

    # Ajustar layout para adicionar título e aumentar o tamanho da legenda
    fig4.update_layout(
        #title_text=f'Total: {total_profissionais}',
        #legend={
        #   'title_text': 'Séries',
        #    'font': {'size': 15}
        #},
        height=600,  # Ajusta a altura do gráfico para melhorar a visualização
        #annotations=[dict(
        #    text=f'Total: {total_profissionais}',
        #    x=0.5, y=0.5,
        #    font_size=20,
        #    showarrow=False
        #)]
    )

    col2.plotly_chart(fig4)