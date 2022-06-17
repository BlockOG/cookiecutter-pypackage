{%- if cookiecutter.use_black_formatting == 'y' %}format:
	python3 -m black .{% endif %}
test:
	python3 -m unittest tests/test_{{ cookiecutter.project_slug }}.py
build:
{%- if cookiecutter.use_black_formatting == 'y' %}	make format{% endif %}
	make test
	rm -rf dist/
	python3 -m build
	twine upload -r pypi dist/*
install:
	pip3 install -U {{ cookiecutter.project_slug }}
