# Projeto Tratamento Variavéis Texto

O arquivo CSV possui colunas com texto e isso dificulta a leitura dos algoritmos de aprendizado de máquina


## Objetivo

Tratar as colunas de texto para que elas possam ser lidas por aprendizado de máquina

## Processo de aprendizagem

- [x] Bibliotecas usadas: Pandas e OneHotEncoder
- [x] Elimando a coluna 'Voo'
- [x] Utilizando apply e lambda function para tratar os dados da colunas 'classe'
- [x] Criação de uma função para tratar os dados da coluna 'paradas'
- [x] Utilizando OneHotEnconder para usar os nomes das empresas áreas para criar uma nova coluna com cada nome
   
    ![Utilizando OneHotEnconder](https://user-images.githubusercontent.com/107354811/224610939-feb309f1-7384-4c49-9945-f0d430a74db1.png)

- [x] Para cada linha atribuí valor 1 correspondente ao nome da empresa e valor 0 não correspondendo
     
     ![colunas e linhas](https://user-images.githubusercontent.com/107354811/224611514-926d4db6-b983-4a95-b66b-711d9e26235c.png)

- [x] No final juntei dataframe novo criado com os nomes das empresas junto com o original

## Agradecimento

Agradeço ao Henrique de Andrade pelo desafio da realização do projeto.
