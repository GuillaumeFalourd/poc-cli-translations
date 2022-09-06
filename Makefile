## Setup
install:
	poetry config virtualenvs.create false
	cd src; poetry install

# Test
test:
	cd src; pytest -v tests/

# Execute
run:
	python src/poc_cli_translations/__init__.py 

# create env
create-env:
	python3 -m venv env