build:
{%- if cookiecutter.use_black_formatting == 'y' %}	python3 -m black .{% endif %}
	python3 tests
	rm -rf dist/
	python3 -m build
	twine upload -r pypi dist/*
install:
	pip3 install -U {{ cookiecutter.project_slug }}
