# Python_APIs
## Introdução
Projeto em python para construção de ETL acessando informações via API, com a biblioteca requests.
### Proposta
Sou contratado como engenheiro de dados em uma startup. Como primeiro trabalho, preciso desenvolver um projeto onde será obtido dados das linguagens de programação 
utilizadas por algumas grandes empresas, como Amazon, Spotify, Netflix e Apple.
Para realizar esse projeto, iremos implementar uma ETL, fazendo uso da biblioteca Requests do Python e também da API do GitHub. Através da API, ferei acesso aos dados 
sobre as linguagens de programação utilizadas pelas empresas mencionadas em seus projetos.

## Desenvolvimento
Para ter a informação das linguagens utilizadas pelas empresas foi utilizado a API do GitHub, acessando as informações dos repositórios e extraindo as linguagens utilizadas em cada. Foi feita a exploração inicial com Jupyter Notebook para consolidar os modos de acesso a API, extração da informação com paginação. Tratamento necessário para separar a informação requerida. E criação de um repositório para disponibilizar o arquivo consolidado com as informações.
Depois dessa exploração foi feito um script para consolidar toda esse processo de ETL, onde foi importado classes de outros scripts feitos que tinham os métodos necessário para realizar a tarefa.

## Resultado
Como resultado tem-se os seguintes arquivos:
* **linguagens_rapos.ipynb**: Notebook com toda a exploração incial de desenvolvimento. E como resultado tem-se o arquivo *'Linguagens_AMZ.csv'* com os dados das linguagens do repositório da Amazon;
* **dados_repo.py**: classe para fazer a conexão com a API fo GitHub, acessar as informações dos repositórios e tratamento dela para extrair as informações necessárias, criando um Data Frame as consolidando;
* **manipula_repos.py**: classe que cria repositórios no GitHub do user passado e faz upload de arquivos via API;
* **ETL_repos.py**: Script que consolida todos os passo de ETL para realizar a tarefa de acesso a informações dos repositório das empresas, tratamento dela para extrair e consolidar as informações necessárioas e disponibilização dela para a equipe que solicitou;
* **Dados/Linguagens_Repositorios.csv**: Arquivo resultante após executar a ETL. Trazendo as informações por empresa e repositório da linguagem utilizada.

O resultado final é o seguinte repositório com as informações das linguagens utilizadas pelas empresas:
https://github.com/GeGusta/Linguagens-repositorios-empresas

Para executar os scripts é necessário adicionar o Token de Autenticação do Git Hub, gerado na conta pessoal. Adicionar no Notebook e na parte de inicialização de cada classe.
