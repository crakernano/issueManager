from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/issues/status/{issue_id}")
def issue_status(issue_id: int):
    return {"issue": issue_id, "status": "open"}

'''
    ToDo:
     - Endpoint de creación de incidente
     - Una vez se crea se carga en github/gitlab y se almacena el ID devuelto por git en la base de datos. La estructura de la tabla podría ser esta:
        | issue | Tinicio | Tfin | Severity | Status |

     -  Si la serveridad es critica se notifica por Slack
        -> Crear un bot de Slack

     -  Si afecta al servicio se muestra en la pagina de status
        -> Crear una pagina de status

     -  Si afecta al servicio se publica en twitter
        -> Crear un bot de twitter

     - Una vez se da por cerrado el issue se actualiza la pagina de status
     - Una vez se da por cerrado el issue se publica en twitter

     - El sistema espera que se genere un RCA del incidendente.
     - Mostrar estadisticas de resolución, tiempos de respuesta, afectación... etc

'''
