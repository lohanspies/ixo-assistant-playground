## Green Yoma - ESRI Custom Action for IXO Assistant
Make sure you have `conda` installed in a virtual environment with Python 3.7.

Then install the ESRI and ArcGIS Python packages via conda.

Open a terminal application, navigate to the directory you want to work in and activate the conda environment you want to use with the ArcGIS API for Python. 

Install the API with the following command:

`conda install -c esri arcgis`

Install Jupyter.

`conday install jupyter`

Start Jupyter

`jupyter-notebook`

Install packages

`pip3 install -U --user pip && pip3 install rasa rasa-sdk`

Follow this link to install [rasa-server](https://rasa.com/docs/rasa/installation/).

Init Rasa Server
`rasa init`

Another method to setup Rasa

`https://github.com/rsykoss/rasa-chatbot-webchat-deployment`

This PyPi package provide a Rasa Docker setup in the [Project Description](https://pypi.org/project/rasa-sdk/).