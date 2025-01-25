#!/bin/bash

echo "Instalando dependências do Python..."
python3 -m pip install -r requirements.txt

if [ $? -ne 0 ]; then
  echo "Erro ao instalar dependências. Verifique o arquivo requirements.txt."
  exit 1
fi

echo "Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput

if [ $? -ne 0 ]; then
  echo "Erro ao coletar arquivos estáticos. Verifique sua configuração STATIC_ROOT."
  exit 1
fi

echo "Build concluído com sucesso!"


