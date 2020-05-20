# Zappa Template

## Pre-Requisite

- [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/)
- [Venv](https://docs.python.org/3/library/venv.html)
- [AWS CLI](https://aws.amazon.com/cli/) + configure

```bash
# Best to install it globally
python3 -m pip install cookiecutter

cookiecutter gh:jolo-dev/zappa-template
```

## Choose your Engine

- Flask
- Django

# Development

```bash
cd *project_slug*
python3 -m venv .env
source .env/bin/activate
pip install --upgrade pip # In case you need to
pip install -r requirements.txt
```

# Deployment

```bash
zappa deploy dev
```

```bash
# For Changes and Updating
zappa update dev
```

```bash
# Tear down the deployment
zappa undeploy dev
```

# Working with Django

Django is a fully fleshed application which requires a database.
In this template, the default database is deactivated.
[Here is a very good instruction, how to setup a database on AWS and Zappa](https://romandc.com/zappa-django-guide/walk_database/#init-the-database)

```bash
zappa deploy dev # The function needs to be up and running
zappa update dev # If neccessary
zappa manage dev "collectstatic --noinput"
```
