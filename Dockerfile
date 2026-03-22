# Imagem base
FROM python:3.10

# Evita criação de arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Não bufferiza logs (melhor para debug)
ENV PYTHONUNBUFFERED=1

# Define diretório dentro do container
WORKDIR /app

# Copia requirements primeiro (melhor cache)
COPY requirements.txt /app/

# Instala dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia todo o projeto
COPY . /app/

# Expõe porta do Django
EXPOSE 8000

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]