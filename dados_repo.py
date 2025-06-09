import requests
import pandas as pd
from math import ceil

# Define uma classe que interage com a API do GitHub para coletar informações sobre os repositórios de um usuário específico.
# A classe permite:
# - Listar todos os repositórios públicos de um "owner" (proprietário de conta GitHub).
# - Extrair os nomes dos repositórios.
# - Extrair as linguagens de programação utilizadas em cada repositório.
# - Criar um DataFrame do Pandas que organiza essas informações, associando o nome do repositório à sua linguagem principal.

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = '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'
        self.header = {'Authorization': 'Bearer ' + self.access_token,
                       "X-GitHub-Api-Version": "2022-11-28"}

    def lista_repositorios(self):
        repos_list = []

        # calculando a quantidade de paginas
        response = requests.get(f'https://api.github.com/users/{self.owner}')
        num_pages = ceil(response.json()['public_repos']/30)

        for page_num in range(1, num_pages + 1):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.header)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        
        return repos_list

    def nomes_repos(self, repos_list):
        lista_name = []

        for pages in repos_list:
            for repo in pages:
                lista_name.append(repo["name"])

        return lista_name

    def nomes_linguagens(self, repos_list):
        lista_language = []

        for pages in repos_list:
            for repo in pages:
                lista_language.append(repo["language"])

        return lista_language
    
    def cria_df_linguagens(self):

        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)
        
        Linguagens_Amz = pd.DataFrame()

        Linguagens_Amz["Repositorio_Nome"] = nomes
        Linguagens_Amz["Language"] = linguagens

        return Linguagens_Amz
    