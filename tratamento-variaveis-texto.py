#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando o Pandas

import pandas as pd


# In[2]:


# Importando base de dados

tabela = pd.read_csv(r'C:\Users\Lucy Minene\Desktop\tratamento-variaveis-texto\Clean_Dataset.csv', index_col=[0])

tabela.head(3)


# In[3]:


# Traduzindo os nomes das colunas

tabela.columns = ['empresa_area', 'voo', 'origem', 'hr_embarque', 
                  'paradas', 'hr_chegada', 'destino', 'classe', 'duracao', 'dias_antes', 'preco']


# In[4]:


# Verificando as informações do DF
# Colunas 0 a 7 estão todas no formato de texto

tabela.info()


# ## Eliminando coluna desnecessária

# In[5]:


#Verificando a cardinalidade do Data Frame

tabela.nunique()


# In[6]:


# Eliminando a coluna 'voo'

tabela = tabela.drop('voo', axis=1)


# ##  Utilizando apply e lambda function

# In[7]:


# Visualizando os valores da coluna 'class'

tabela.classe.value_counts()


# #### Como exitem apenas 2 tipos de classe, economica e executiva, irei criar uma coluna com o valor 1 para classe economica e valor 0 para classe executiva.

# In[8]:


# Criando a nova coluna

tabela['economica'] = tabela.classe.apply(lambda x:1 if x == 'Economy' else 0)


# In[9]:


# Visualizando valores

tabela[['classe', 'economica']].value_counts()


# ### Criando uma função para tratamento dos dados

# In[10]:


# Visualizando os valores da coluna "paradas"

tabela.paradas.value_counts()


# In[11]:


# Criando uma função para tratar os valores da coluna "paradas"

def num_paradas(valor):
    if valor == 'zero':
        return 0
    elif valor == 'one':
        return 1
    elif valor == 'two_or_more':
        return 2
    else:
        return -1


# In[12]:


# Aplicando a função

tabela['num_paradas'] = tabela.paradas.apply(num_paradas)


# In[13]:


# Visualizando valores

tabela[['paradas', 'num_paradas']].value_counts()


# ### Utilizando OneHotEncoder

# In[14]:


# Verificando a coluna "empresa_área"

tabela.empresa_area.value_counts()


# In[15]:


# Criando o codificador

from sklearn.preprocessing import OneHotEncoder

ohe_empresa_area = OneHotEncoder(handle_unknown='ignore')

# Fazendo fit com os dados

ohe_empresa_area = ohe_empresa_area.fit(tabela[['empresa_area']])

# Fazendo a transformação dos dados

ohe_empresa_area.transform(tabela[['empresa_area']])


# In[16]:


# Visualizando no formato de array

ohe_empresa_area.transform(tabela[['empresa_area']]).toarray()


# In[17]:


# Transformando o array em DataFrame

ohe_df = pd.DataFrame(ohe_empresa_area.transform(tabela[['empresa_area']]).toarray())

ohe_df.head(5)


# In[18]:


# Selencionando o nome das colunas

colunas = ohe_empresa_area.get_feature_names_out()

colunas


# In[19]:


# Utilizando get_feature_names_out para nomear as colunas

ohe_df = pd.DataFrame(ohe_empresa_area.transform(tabela[['empresa_area']]).toarray(),
                     columns = colunas,
                      dtype = 'int32'
                     )

ohe_df.head(5)


# In[20]:


# Unir o df acima com o original

tabela = pd.concat([tabela, ohe_df], axis=1)

tabela.head(5)


# In[21]:


# Resultado

tabela.groupby('empresa_area')[colunas].sum()

