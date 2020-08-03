#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import re


# In[3]:


#criação de uma função para a criação do dataframe basico
def criador_df(files):
    

    # obtendo o nome das colunas a partir dos nomes de arquivos (necessário uma lista para cada mês para manter a ordenação):

    colunas_mar= []
    for i in files:
        if "mar" in i:
            colunas_mar.append(i.rpartition('\\')[2].replace(".xlsx", ""))
    
    colunas_abr= []
    for i in files:
        if "abr" in i:
            colunas_abr.append(i.rpartition('\\')[2].replace(".xlsx", ""))
        
    colunas_mai=[]
    for i in files:
        if "mai" in i:
            colunas_mai.append(i.rpartition('\\')[2].replace(".xlsx", ""))
        
    
    colunas_jun=[]
    for i in files:
        if "jun" in i:
            colunas_jun.append(i.rpartition('\\')[2].replace(".xlsx", ""))
            
    colunas_jul=[]
    for i in files:
        if "jul" in i:
            colunas_jul.append(i.rpartition('\\')[2].replace(".xlsx", ""))
    

    colunas_ago=[]
    for i in files:
        if "ago" in i:
            colunas_ago.append(i.rpartition('\\')[2].replace(".xlsx", ""))
    
    colunas = colunas_mar+colunas_abr+colunas_mai+colunas_jun+colunas_jul+colunas_ago




    #obtendo todos os nomes de cidades a partir da lista padronizada
    df = pd.read_excel(r"D:\Dropbox\Pessoal\Python\COVID\COVID19-SP-BR\tabelas_espelho\pop_mun_padronizado.xlsx")
    indice=[]
    [indice.append(i) for i in df["nome"]]

    df = pd.DataFrame(columns = colunas, index= indice)
    df.to_excel(r"D:\Dropbox\Pessoal\Python\COVID\COVID19-SP-BR\tabelas_analise\tabela_base.xlsx")

