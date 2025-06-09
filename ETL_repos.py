import pandas as pd
from dados_repo import DadosRepositorios
from manipula_repos import ManipulaRepositorios

#Lista com as empresas para pesquisar as linguagens dos repositórios
empresas_repos = ['amzn', 'spotify', 'netflix', 'apple']

linguagens_empresas = pd.DataFrame(columns=["Empresa", "Repositorio_Nome", "Language"])

print("....................................................................................................................")
print("Fazendo o acesso ao GitHub da Amazon, Spotify, Netflix e Apple via API. Buscando em seus repositórios as linguagens utilizadas.")

#Pesquisa por empresa no repositórios e as linguagens que usa. Consolidando em uma Data Frame
for empresa in empresas_repos:

    repo = DadosRepositorios(empresa)

    repo_df = repo.cria_df_linguagens()

    repo_df["Empresa"] = empresa

    linguagens_empresas = pd.concat([linguagens_empresas, repo_df], ignore_index = True)

#Salvando o dataframe final
linguagens_empresas.to_csv('Dados/Linguagens_Repositorios.csv', index=False)
print("....................................................................................................................")
print("Busca feita e armazenando os dados na pasta Dados")
#Criando um repositório para disponibilizar o arquivo, além de fazer o upload dele via API
#Instanciando um objeto
novo_repo = ManipulaRepositorios('GeGusta')

print("\n....................................................................................................................")
print("Criando repositório no GitHub do GeGusta para acessar os dados. Acompanhe os Status")
#Criando Repositório
nome_repo = 'Linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo)

#Adicionando Arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, 'Linguagens_Repositorios.csv', 'Dados/Linguagens_Repositorios.csv')

