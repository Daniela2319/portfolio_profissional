# Passo a Passo para Configurar Ambiente Virtual, Django, e Tailwind CSS

| Etapa                           | Comando/Descrição                                                                                   |
|---------------------------------|-----------------------------------------------------------------------------------------------------|
| **1. Instalar Ambiente Virtual** |                                                                                                     |
| Atualizar pacotes do sistema    | `sudo apt update && sudo apt upgrade` (Linux) ou usar um gerenciador no Windows/Mac.                |
| Instalar virtualenv (caso não tenha) | `pip install virtualenv`                                                                         |
| **2. Criar o Ambiente Virtual** |                                                                                                     |
| Criar ambiente virtual          | `python -m venv nome_do_ambiente`                                                                  |
| Ativar o ambiente virtual       | `source nome_do_ambiente/bin/activate` (Linux/Mac) ou `nome_do_ambiente\Scripts\activate` (Windows) |
| Entrar no ambiente virtual      | Após ativar, o prompt exibirá o nome do ambiente antes da linha de comando.                        |
| **3. Instalar Django**          |                                                                                                     |
| Instalar Django                 | `pip install django`                                                                               |
| **4. Criar o Projeto Django**   |                                                                                                     |
| Criar projeto                   | `django-admin startproject nome_do_projeto .`                                                      |
| Criar aplicativo (app)          | `python manage.py startapp nome_do_app`                                                            |
| **5. Instalar e Configurar Tailwind** |                                                                                                  |
| Instalar dependências do Tailwind | `pip install django-tailwind`                                                                      |
| Criar app do Tailwind           | `python manage.py tailwind init nome_do_app_tailwind`                                              |
| Configurar settings.py          | Adicionar o app criado no `INSTALLED_APPS`                                                         |
| Instalar Node.js e npm (caso não tenha) | Baixe do [site oficial](https://nodejs.org) ou instale pelo gerenciador de pacotes.            |
| Instalar dependências do Tailwind | `npm install` (dentro da pasta do app Tailwind criado)                                             |
| Configurar input.css            | Crie um arquivo `input.css` com o seguinte conteúdo:                                               |
|                                 | ```css
@tailwind base;
@tailwind components;
@tailwind utilities;                                                                                                 |
| Configurar output.css           | Atualize o arquivo `tailwind.config.js` para apontar o caminho de entrada e saída.                 |
| Executar Tailwind               | Use o comando `npm run dev` para compilar os arquivos CSS.                                         |
| **6. Criar requirements.txt**   |                                                                                                     |
| Exportar dependências            | `pip freeze > requirements.txt`                                                                   |
| Instalar dependências de um projeto | `pip install -r requirements.txt`                                                              |


