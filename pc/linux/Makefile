PYTHON_V := 3.8
VENV ?= Pandapp_venv
INSTALL_FILE = "Anaconda3-2021.11-Linux-x86_64.sh"
.DEFAULT_GOAL = help

help :
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To run the project type make run"
	@echo "To clean the project type make clean"
	@echo "------------------------------------"


setup :
	sudo apt install wget
	sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
	wget https://repo.anaconda.com/archive/
	bash Anaconda3-2021.11-Linux-x86_64.sh
	conda create -n $(VENV) python=$(PYTHON_V) anaconda
	conda install -n $(VENV) requests
	conda install -n $(VENV) tk
	conda install -n $(VENV) pillow
	conda install -n $(VENV) python-socketio
	conda install -n $(VENV) pycryptodome
	conda install -n $(VENV) websocket-client
	sudo apt install xdotool
	sudo apt install playerctl
	rm $(INSTALL_FILE)


run :
	./runner.sh

clean :
	conda env remove -n $(VENV)
