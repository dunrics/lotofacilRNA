#FUNCIONAL#
#Pega o arquivo 'outputRNA.csv' com os resultados previstos e realiza upload no github
#https://github.com/dunrics/lotofacilRNA/tree/main
from github import Github
import os

# Informações de autenticação
token = 'CHAVE TOKEN'

# Caminho local do arquivo CSV
csv_file_path = 'CAMINHO DO ARQUIVO\outputRNA.csv'

# Nome do arquivo no repositório
repo_file_name = 'outputRNA.csv'

# Nome do repositório e nome de usuário
repository_name = 'lotofacilRNA'
username = 'dunrics'

# Inicializar o objeto Github
g = Github(token)

# Obter uma referência para o repositório
repo = g.get_user(username).get_repo(repository_name)

# Leitura do conteúdo do arquivo CSV
with open(csv_file_path, 'r') as file:
    csv_content = file.read()

# Criar ou atualizar o arquivo no repositório
try:
    # Tentar obter uma referência para o arquivo no repositório
    file = repo.get_contents(repo_file_name)
    # Atualizar o conteúdo do arquivo
    repo.update_file(file.path, "Atualizando arquivo CSV", csv_content, file.sha)
    print(f"Arquivo '{repo_file_name}' atualizado no repositório '{repository_name}'.")
except Exception:
    # Se o arquivo não existir, criar um novo arquivo
    repo.create_file(repo_file_name, "Criando arquivo CSV", csv_content)
    print(f"Arquivo '{repo_file_name}' criado no repositório '{repository_name}'.")

# Excluir o arquivo localmente
os.remove(csv_file_path)
print(f"Arquivo '{csv_file_path}' excluído.")