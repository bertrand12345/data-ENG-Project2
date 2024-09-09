install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora

test:
	python -m pytest -vvv --cov=hello --cov=greeting\
	 --cov=smath --cov=web --cov=nlplogic tests 
	python -m pytest --nbval notebook.ipynb # tests our jupyter notebook
	#python -m pytest -v tests/test_web.py # if you want to test web

debug:
	python -m pytest -vv --pdb #Debugger is invoked

one-test:
	python -m pytest -vv tests/test_greeting.py::test_sally


debugthree:
	#not working the way Iexpect
	python -m pytest -vv --pdb --maxfail=4 # drop to PDB for first three failures

format:	
	black *.py  nlplogic

lint:
	pylint --disable=R,C *.py nlplogic/*.py



		
all: install lint test format