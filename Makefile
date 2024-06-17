install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest -vv --cov=src tests
	python -m pytest --nbval notebook.ipynb # Tests project jupyter notebook

format:
	black src

lint:
	pylint --disable=R,C src

all: install lint test format