# wsBackend-Fabrica26.1

🐍 Projeto Django - API de Pokémon
📌 Descrição
Este projeto é uma aplicação desenvolvida com Django que consome a API pública de Pokémon (PokeAPI), permitindo buscar, salvar e listar Pokémons.
🚀 Funcionalidades
🔍 Buscar Pokémon pelo nome
💾 Salvar Pokémon no banco de dados
📋 Listar Pokémons cadastrados
✏️ Atualizar informações (PUT)
❌ Deletar Pokémon
🛠️ Tecnologias utilizadas
Python
Django
Django REST Framework
SQLite
Requests

📁 Estrutura do Projeto
api_rest/
 ├── models.py
 ├── views.py
 ├── serializers.py
 ├── services.py
 ├── urls.py
 ├── templates/
 
⚙️ Como rodar o projeto
1. Clonar o repositório
git clone https://github.com/seu-usuario/seu-repo.git
2. Acessar a pasta
cd seu-repo
3. Criar ambiente virtual
python3 -m venv venv
4. Ativar a venv
source venv/bin/activate
5. Instalar dependências
pip install -r requirements.txt
6. Rodar migrações
python manage.py makemigrations
python manage.py migrate
7. Rodar o servidor
python manage.py runserver
