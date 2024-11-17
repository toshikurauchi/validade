# Controle de Datas de Validade

## Configuração

### Django

Instale as dependências com:

```
pip install -r requirements.txt
```

### Render

Utilizei o seguinte tutorial para configurar o deploy no Render: https://docs.render.com/deploy-django

### TailwindCSS

Instale o Tailwind localmente:

```
npm install -g tailwindcss@latest
```

Execute o script `tailwind/watch.sh` para atualizar o CSS.

## Executando o servidor

Utilize os comandos do Django para executar o servidor localmente:

```
python manage.py migrate
python manage.py runserver
```

### Testando com gunicorn

Utilize o seguinte comando:

```
python -m gunicorn validade.asgi:application -k uvicorn.workers.UvicornWorker
```
