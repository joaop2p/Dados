from typing import Any
import requests

def getCluster(data: dict) -> Any | dict[str, str]:
    try:
        result = requests.post("http://localhost:8000/prever_cluster", json=data)
        return result.json()
    except Exception as e:
        return {"erro": str(e)}
