#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import glob


# In[2]:



def criador_df_analise(files):
    

    #Importação do dataframe padrao
    df = pd.read_excel(r"D:\Dropbox\Pessoal\Python\COVID\COVID19-SP-BR\tabelas_analise\tabela_base.xlsx", index_col=0)


    #Para cada coluna do DF padrão procura a correnpondência no arquivo de dados e adiciona onde houver correspondência entre
    # o nome do arquivo e a coluna padrão assim como onde o nome da cidade for semelhante entre os dois

    # iterando entre as colunas
    for col in list(df.columns):

        #iterando entre os arquivos
        for file in files:
            f = pd.read_excel(file, index_col=0)

            #criação de um dicionário para armazenar o valor e a chave
            d = dict(f.iloc[:,0])

            #verificando se o nome do arquivo tem correspondência com alguma coluna
            if file.rpartition('\\')[2].replace(".xlsx", "") == col:

                # se houver itera entre as chaves do dicionário e adiciona o valor dele na coluna do DF padrão
                for i in d:
                    try:
                        df.loc[i, col] = d.get(i)
                    except:
                        continue

    df.fillna(0, inplace = True)
    df.to_csv(r"D:\Dropbox\Pessoal\Python\COVID\COVID19-SP-BR\tabelas_analise\infectados_municipio.csv")


# In[17]:


path = r'D:\Dropbox\Pessoal\Python\COVID\COVID19-SP-BR\Dados'
files = glob.glob(path + "/*.xlsx")


# In[19]:





# In[22]:





# In[ ]:




