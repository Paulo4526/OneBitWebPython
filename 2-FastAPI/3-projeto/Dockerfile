# Etapa de build
FROM python:3.13-slim AS build
# Instalar dependências básicas
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*
# Instalar Poetry globalmente
RUN curl -sSL https://install.python-poetry.org | python3 -
# Adicionar Poetry ao PATH
ENV PATH="/root/.local/bin:$PATH"
# Criar diretório da aplicação
RUN mkdir -p /apk/app
WORKDIR /apk/app
# Copiar projeto
COPY . /apk/app
# Instalar dependências via Poetry (criando o venv)
RUN poetry config virtualenvs.create true \
    && poetry install --no-root

# Etapa final
FROM python:3.13-slim
# Dependências básicas
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*
# Instalar Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
# Criar diretório da aplicação
RUN mkdir -p /apk/app
WORKDIR /apk/app
# Copiar projeto do build
COPY --from=build /apk/app /apk/app
# Instalar dependências via Poetry
RUN poetry install --no-root
# Expõe porta
EXPOSE 8000
# Rodar uvicorn via Poetry
ENTRYPOINT ["poetry", "run", "uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
