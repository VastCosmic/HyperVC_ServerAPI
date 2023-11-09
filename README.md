# HyperVC_ServerAPI
A Server API for Hyperspectral Image Classification Application

# Intro
This is the server api project of HyperVC.
With FastAPI, you can use it to Classify Hyperspectral Images with our model by sending a HTTP request.
By the way, you may use the HyperVCApplication for Windows as a client to send requests to this server to gain a better experience.

# Supported Model
IndianPines、Salinas、PaviaU

# Run
1. Install the requirements
`pip install -r requirements.txt`
2. Run the server
`python app.py`

# API
Tostart Classify Hyperspectral Images send a HTTP request to the server with the following format:
`http://127.0.0.1:7777/start/indian`
`http://127.0.0.1:7777/start/paviau`
`http://127.0.0.1:7777/start/salinas`
