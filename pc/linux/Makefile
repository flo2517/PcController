PYTHON_V := 3.8
VENV ?= Pandapp_venv
.DEFAULT_GOAL = help

help :
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To run the project type make run"
	@echo "To clean the project type make clean"
	@echo "------------------------------------"


setup :
	conda create -n $(VENV) python=$(PYTHON_V) anaconda
	conda install -n $(VENV) requests
	conda install -n $(VENV) tk
	conda install -n $(VENV) pillow
	conda install -n $(VENV) python-socketio
	conda install -n $(VENV) pycryptodome
	conda install -n $(VENV) websocket-client

run :
	./runner.sh

clean :
	conda env remove -n $(VENV)
