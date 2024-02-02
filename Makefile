
install:
	pip install -r requirements.txt
	pip install -e src

test_it:
	pytest

run:
	python main.py