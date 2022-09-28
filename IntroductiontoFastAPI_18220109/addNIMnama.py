# NIM: 18220109
# Nama: Adwa Sofia

import json
from fastapi import FastAPI
from pydantic import BaseModel


with open("NIMnamaMahasiswa.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()
#@app.get('/menu/{item_id}')
#async def read_menu(item_id: int):
    #for menu_item in data['menu']:
        #if menu_item['id'] == item_id:
            #return menu_item
    #raise HTTPException(
        #status_code=404, detail=f'Item not found'
#)

class NIMnama(BaseModel): # the data model
    NIM: int
    Nama: str
#app = FastAPI()
@app.post("/NIMNama")
async def add_NIM_nama(new_NIM_nama: NIMnama):
    if new_NIM_nama.NIM in data:
        return {"NIM tersebut telah tersimpan."}
    else:
        data[new_NIM_nama.NIM] = {
            "NIM": new_NIM_nama.NIM,
            "Nama": new_NIM_nama.Nama
            }
        return data
