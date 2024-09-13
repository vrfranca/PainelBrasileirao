# Importa os pacotes necessários
import streamlit as st
import pandas as pd
import numpy as np
import json
from unidecode import unidecode

#Função para remover acentos
def remover_acentos(texto):
    return unidecode(texto)

# ---------------  INICIO DA CARGA DOS DADOS ------------------------

# INICIO DOS DADOS DAS CAPITAIS
_global_df_capitais = pd.read_excel("Capitais_Brasileiras.xlsx")
# FIM DOS DADOS DAS CAPITAIS

# INICIO DOS DADOS DE ARBITRAGEM
# Lê os arquivos XLSX de Arbitragem
arbitros_a = pd.read_excel("Arbitragem_Brasileirao_Serie_A.xlsx")
arbitros_b = pd.read_excel("Arbitragem_Brasileirao_Serie_B.xlsx")
arbitros_c = pd.read_excel("Arbitragem_Brasileirao_Serie_C.xlsx")
arbitros_d = pd.read_excel("Arbitragem_Brasileirao_Serie_D.xlsx")
# Unifica os arquivos de arbitragem em um único dataset
df_arbitros = pd.concat([arbitros_a, arbitros_b, arbitros_c, arbitros_d])
# Aplicar a função de remoção de acentos na coluna específica (02 modos diferentes)
df_arbitros["nome"] = df_arbitros["nome"].apply(remover_acentos)
df_arbitros["funcao"] = df_arbitros["funcao"].str.replace("Á", "A")
# Definindo como nulo valores de federacao genericos
df_arbitros["federacao"] = df_arbitros["federacao"].replace("BRA", np.nan)
df_arbitros["federacao"] = df_arbitros["federacao"].replace("BR", np.nan)
# Preenchendo valores nulos na coluna 'federacao' conforme existentes em outras linhas
df_arbitros["federacao"] = df_arbitros.groupby('nome')["federacao"].transform(lambda x: x.ffill().bfill())
df_arbitros["quadro"] = df_arbitros["quadro"].replace("VAR-FIFA", "FIFA")
# Definindo um valor para campos nulos nas colunas especificadas
df_arbitros["federacao"] = df_arbitros["federacao"].fillna("Não Especificada")
df_arbitros["funcao"] = df_arbitros["funcao"].fillna("Não Especificada")
_global_df_arbitros = df_arbitros
# FIM DOS DADOS DE ARBITRAGEM

# INICIO DOS DADOS DE GEOLOCALIZAÇÃO DOS ESTADOS BRASILEIROS
_global_df_geojson = json.load(open('brasil_estados.json'))
# FIM DOS DADOS DE GEOLOCALIZAÇÃO DOS ESTADOS BRASILEIROS