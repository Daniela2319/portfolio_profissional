#!/bin/bash

# Instalar dependências do Python
python3 -m pip install -r requirements.txt

# Instalar dependências do Node.js
npm install

# Rodar o build do Tailwind CSS
npm run build:css

# Coletar os arquivos estáticos do Django
python3 manage.py collectstatic --no-input




