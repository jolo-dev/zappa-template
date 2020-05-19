import os
import shutil

engine = "{{ cookiecutter.engine }}"
project = "{{ cookiecutter.project_slug }}"

if engine == "Flask":
    os.remove("manage.py")
    shutil.rmtree(project, ignore_errors=True)
    
elif engine == "Django":
    os.remove("app.py")
