# NIM: 18220109
# Nama: Adwa Sofia
# Program ini menggunakan file NIMnamaMahasiswa.json yang terdapat pada folder yang sama dengan program ini.

import json
from fastapi import FastAPI
from pydantic import BaseModel


with open("NIMnamaMahasiswa.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()


class NIMnama(BaseModel): # the data model
    NIM: int
    Nama: str

@app.post("/NIMNamas")
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
        data["NIMnamaMahasiswa"].append(new_data)
        return data