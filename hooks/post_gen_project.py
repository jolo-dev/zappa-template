import os

engine = "{{ cookiecutter.engine }}"
project = "{{ cookiecutter.project_slug }}"
os.chdir(project)
if engine == "Flask":
    os.remove("manage.py")
    os.rmdir(project)

if engine == "Django":
    os.remove("app.py")
