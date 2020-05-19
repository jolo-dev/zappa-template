# Zappa Template

## Pre-Requisite

- [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/)
- [Venv](https://docs.python.org/3/library/venv.html)
- [AWS CLI](https://aws.amazon.com/cli/) + configure

```bash
# Best to install it globally
python3 -m pip install cookiecutter

cookiecutter gh:https://github.com/jolo-dev/zappa-template
```

## Choose your Engine

- Flask
- Django

# Development

```bash
cd *project_slug*
python3 -m venv .env
source .env/bin/activate
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
