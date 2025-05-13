from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Request

def hello_word():
    return {'Olá':'Mundo'}