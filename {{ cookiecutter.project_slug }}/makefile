build:
	python tests
	rm -rf dist/
	python3 -m build
	twine upload -r pypi dist/*
install:
	pip3 install -U {{ cookiecutter.project_slug }}