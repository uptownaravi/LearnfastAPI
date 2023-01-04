from fastapi import FastAPI
from encoder import encode
from pydantic import BaseModel

class TemplateData(BaseModel):
  data: str
  template: dict

app = FastAPI()
enc = encode.Encode()

@app.get("/health")
def read_root():
    return {"health": "okay"}

@app.get("/encode/{data}")
def encodedata(data: str):
    encodedata = enc.encoded(data)
    return f"encoded value of {data} is {encodedata}"

@app.post("/encodeWithTemplate/")
def encodewithtemplate(dataTemplate: TemplateData):
    templateDict = dataTemplate.dict()
    encodedata = enc.encodewithtemplate(templateDict['template'], templateDict['data'])
    return f"encoded value of {templateDict['data']} with {templateDict['template']} is {encodedata}"