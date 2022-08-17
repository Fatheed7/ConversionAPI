# main.py

from fastapi import FastAPI
import json

app = FastAPI()

json_file = json.load(open('conversion.json'))

@app.get("/convert/")
def hello(type: str, from_type: str, to_type: str, value: float):
  x = json_file[type][0]
  if from_type in x.__str__():
    return {
      'valid': True,
      'from_type': from_type,
      'to_type': to_type,
      'value': value,
      'result': value * x[from_type][to_type]
    }
  else:
    return {
      'valid': False,
    }