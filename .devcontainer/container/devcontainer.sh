{
	"name": "Python 3 NER Copyright texts detection Pipeline",
	"image": "mcr.microsoft.com/devcontainers/python:1-3.10-bookworm",
	"postCreateCommand": "/bin/bash -c 'bash .devcontainer/setup.sh && pip install --upgrade pip setuptools wheel && pip cache purge && pip install -r requirements.txt || pip cache purge && pip install -r requirements.txt'",
	# "postStartCommand": "pip install --upgrade pip setuptools wheel && pip cache purge && pip install -r requirements.txt || pip cache purge && pip install -r requirements.txt"
}
