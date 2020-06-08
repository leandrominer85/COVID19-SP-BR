# COVID19-SP-BR
Repositório com análises dobre o Covid-19 no Estado de São Paulo

O repositório é composto dos dados sobre a COVID-19 no Estado de São  Paulo disponibilizados pela Fundação SEADE no seguinte repositório:
https://github.com/seade-R

Pela falta de uniformidade dos dados foi necessário um processo de padronização dos dados. Para tanto o código "Padronizador da coluna de municipios" serve como ferramenta para que todas as planilhas compartilhem a mesma formatação de nomes.

A partir dessa padronização foi criado o código "Criador DF padrão" que permite criar um DataFrame sem os dados com as colunas e índices advindos dos arquivos de dados.

Populamos o Dataframe em branco com os dados dos arquivos na pasta utiizando o codigo disponivel em "Criador do DF para a análise"

Só a partir de então criamos o gráfico com o código "Grafico interativo". Este gráfico é salvo como HTML na pasta.
