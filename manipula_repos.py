import requests
import base64

#Classe criada para manipular repositórios. Para instanciar é necessário passar como parametro o user.Possui dois metodos: 
#cria_repo: cria repositório no user passado ao instanciar a classe, com o nome do repositorio passado como parametro
#add_arquivo: adiciona arquivo a um repositorio. Passar como parametro o nome do repositorio existente, nome do arquivo e caminho dele

class ManipulaRepositorios:

    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = 'Seu Token de Acesso'
        self.header = {'Authorization': 'Bearer ' + self.access_token,
                       "X-GitHub-Api-Version": "2022-11-28"}
        
    def cria_repo(self, nome_repo):
        data = {
            'name': nome_repo,
            'description': 'Linguagens utilizados nos repositórios da Amazon.',
            'private': False
        }
        url = f'{self.api_base_url}/user/repos'
        reponse = requests.post(url, headers=self.header, json=data)

        print(f'status_code criação do repositório: {reponse.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        
        with open(caminho_arquivo, 'rb') as file:
            conteudo = file.read()

        conteudo_codificado = base64.b64encode(conteudo)

        url_put = f'{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}'
        data_put = {
            'message': "Adicionar um novo arquivo",
            'content': conteudo_codificado.decode('utf-8')
        }

        response_put = requests.put(url_put, json = data_put, headers = self.header)

        print(f'status_code upload do arquivo: {response_put.status_code}')