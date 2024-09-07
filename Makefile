install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=greeting tests
	python -m pytest --nbval notebook.ipynb # tests our jupyter notebook

debug:
	python -m pytest -vv --pdb #Debugger is invoked

one-test:
	python -m pytest -vv tests/test_greeting.py::test_my_name4


debugthree:
	#not working the way Iexpect
	python -m pytest -vv --pdb --maxfail=4 # drop to PDB for first three failures

format:	
	black *.py 

lint:
	pylint --disable=R,C hello.py



		
all: install lint test format