import threading
import uuid
import subprocess
from fastapi import FastAPI

import HybridSN_Indian as HybridSN_Indian

app = FastAPI()

@app.get("/start/indian")
def start_script_and_return_response():
    task_uuid = str(uuid.uuid4())
    print(task_uuid)
    threading.Thread(target=run_HybridSN_Indian, args=(task_uuid,)).start()
    return {"task_uuid": task_uuid, "status": "success"}

@app.get("/start/paviau")
def start_script_and_return_response():
    task_uuid = str(uuid.uuid4())
    print(task_uuid)
    threading.Thread(target=run_HybridSN_PaviaU, args=(task_uuid,)).start()
    return {"task_uuid": task_uuid, "status": "success"}

@app.get("/start/salinas")
def start_script_and_return_response():
    task_uuid = str(uuid.uuid4())
    print(task_uuid)
    threading.Thread(target=run_HybridSN_Salinas, args=(task_uuid,)).start()
    return {"task_uuid": task_uuid, "status": "success"}

def run_HybridSN_Indian(task_uuid):
    HybridSN_Indian.process_HybridSN_Indian(task_uuid)

def run_HybridSN_PaviaU(task_uuid):
    subprocess.run(["python", "Server\HybridSN_PaviaU.py", task_uuid])

def run_HybridSN_Salinas(task_uuid):
    subprocess.run(["python", "Server\HybridSN_Salinas.py", task_uuid])

if __name__ == "__main__":
    import uvicorn
    import yaml
    yamlPath = "Config\HyperVC_Setting.yaml"
    f = open(yamlPath,'r',encoding='utf-8')
    cont = f.read()
    cfg = yaml.safe_load(cont)
    uvicorn.run(app, host="0.0.0.0", port=cfg['port'])
