from fastapi import FastAPI
from pydantic import BaseModel

NIMnamaMahasiswa = {
    0: {
        "NIM":0,
        "Nama":"Kosong"
    }
}

class NIMnama(BaseModel): # the data model
    NIM: int
    Nama: str
app = FastAPI()
@app.post("/NIMNama")
async def add_NIM_nama(new_NIM_nama: NIMnama):
    if new_NIM_nama.NIM in NIMnamaMahasiswa:
        return {"NIM tersebut telah tersimpan."}
    else:
        NIMnamaMahasiswa[new_NIM_nama.NIM] = {
            "NIM": new_NIM_nama.NIM,
            "Nama": new_NIM_nama.Nama
            }
        return NIMnamaMahasiswa
