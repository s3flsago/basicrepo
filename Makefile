install:
	python3 -m venv venv
	bash venv/bin/activate
	pip install --upgrade pip
	pip install .

run:
	python3 main.py

run_tests:
	python3 -m unittest
