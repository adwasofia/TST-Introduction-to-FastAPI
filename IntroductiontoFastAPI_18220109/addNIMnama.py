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

#jsonString = json.dumps(aList)
#jsonFile = open("data.json", "w")
#jsonFile.write(jsonString)
#jsonFile.close()

class NIMnama(BaseModel): # the data model
    NIM: int
    Nama: str
#app = FastAPI()
@app.post("/NIMNama")
async def add_NIM_nama(new_NIM_nama: NIMnama):
    if new_NIM_nama.NIM in data:
        return {"NIM tersebut telah tersimpan."}
    else:
        new_data = [
            {
            "NIM": new_NIM_nama.NIM,
            "Nama": new_NIM_nama.Nama
            }
            ]
        new_jsonString = jsonString = json.dumps(new_data)
        jsonWrite = open("NIMnamaMahasiswa.json", "w")
        jsonWrite.write(new_jsonString)
        jsonWrite.close()
        return data
    
