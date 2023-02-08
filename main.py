from fastapi import FastAPI, Body
from db_temp import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API Response OK!"}

@app.get("/api/v1/notes/")
async def read_notes():
    return data_notes

@app.get("/api/v1/errors/")
async def read_errors():
    return data_errors

@app.get("/api/v1/customers/")
async def read_customers():
    return data_customer

@app.get("/api/v1/cases/")
async def read_customers():
    return data_cases

@app.get("/api/v1/tickets/list/")
async def read_tickets():
    return data_tickets

@app.post("/api/v1/add/tickets/list")
async def get_body(data: dict = {}):
    print(data)
    data_tickets.append(data)
    return data