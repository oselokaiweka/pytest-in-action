install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest -vv --cov=src tests
	python -m pytest --nbval notebook.ipynb # Tests project jupyter notebook

debug:
	python -m pytest -vv --pdb # Invoke debugger on test fail

debug-maxfail:
	python -m pytest -vv --pdb --maxfail=3 # Drop to pdb for first three failures

one-test:
	python -m pytest -vv tests/test_greeting.py::test_my_name4

format:
	black src

lint:
	pylint --disable=R,C src

all: install lint test format