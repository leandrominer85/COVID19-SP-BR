#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import re
import unidecode


# In[21]:


# função que, a partir de uma lista vazia lê o arquivo, retira todas as linhas sem dados da primeira coluna e salva arquivo
# com a coluna padronizada com minusculas e sem acentuação
def renomear(arquivo):
    lista_palavras= ["total geral", "ignorado", "total","nao informado","none","outro estado" ,"outro pais",
                     "na?o informado","Unnamed: 0","cidade","outros estados","outros paises","municipio",
                     "municipio deresidencia","municipio ","(vazio)","municipios","cidades","Municípios",
                     "MUNICIPIO","Município","MUNICÍPIO","ignorado ou exterior","MUNCIPIO","NOME","MUNICÍPIOS",
                     "nafo informado","escada","salvador","2020-06-21;"]
    lista = []
    df = pd.read_excel(arquivo,encoding="latin")
    df = df[df.iloc[:,1].notna()]
    df = df[df.iloc[:,0].notna()]
    for i in df.iloc[:,0]:
        i = re.sub("_", ' ', i)
        i =  re.sub("-", ' ', i)
        i = re.sub("moji mirim", "mogi mirim", i)
        i = re.sub("mog guacu", "mogi guacu", i)
        i = re.sub("bom jesus dos perda es", "bom jesus dos perdoes", i)
        i = re.sub("monca es", "moncoes", i)
        i = re.sub("sao paulo das missa es", "sao paulo das missoes", i)
        

        lista.append(unidecode.unidecode(i).lower())
    df.iloc[:,0] = lista
    
    #limpeza das colunas com nomes não interessantes para a análise:
    df = df[~df.iloc[:,0].isin(lista_palavras)]
    df.to_excel(f'{arquivo}', index= None)


# In[ ]:





# In[ ]:




