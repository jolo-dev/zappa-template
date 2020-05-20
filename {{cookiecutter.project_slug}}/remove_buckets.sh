aws s3 rb s3://{{ cookiecutter.aws_bucket_name }} --force
# From Django static page
{% if cookiecutter.engine == "Django" %}
aws s3 rb s3://{{ cookiecutter.project_slug.replace('_', '-') }}-{{ cookiecutter.engine.lower() }} --force
{% endif %}