# Import FastAPI, status
from fastapi import FastAPI, HTTPException, status
# To turn classes into JSONs
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
# Schema
from pydantic import BaseModel
from typing import Optional
# import os
# import requests
# from dotenv import load_dotenv

# Inherit from BaseModel class
class Customer(BaseModel):
    # Attributes
    customer_id: str
    country: str
    city: Optional[str] = None

class URLLink(BaseModel):
    # Attributes
    url: Optional[str] = None
    
class Invoice(BaseModel):
    # Attributes
    invoice_no: int
    invoice_date: str
    customer: Optional[URLLink] = None

# Simulate DB
fakeInvoiceTable = dict()

# Run Instance
app = FastAPI()

# Methods

# 1️⃣ Check API
@app.get("/")
async def read_root():
    return {"message": "Api Connected!!"}

# 2️⃣ Add new Customer
@app.post("/customer")
# We require a Customer item
async def create_customer(item: Customer):
    # Encode the created customer item if successful into a JSON and return it to the client with 201
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data, status_code=201)

# 3️⃣ Get a customer by customer id
# {customer_id} --> path parameter
@app.get("/customer/{customer_id}")
async def read_customer(customer_id: str):
    
    # Business Logic
    if customer_id == "12345" :
        
        # Create a fake customer ( usually you would get this from a database)
        item = Customer(customer_id = "12345", country= "Germany")  
        
        # Encode the customer into JSON and send it back
        json_compatible_item_data = jsonable_encoder(item)
        return JSONResponse(content=json_compatible_item_data)
    else:
        # Raise a 404 exception
        raise HTTPException(status_code=404, detail="Item not found")
    
# 4️⃣ Create a new invoice for a customer
@app.post("/customer/{customer_id}/invoice")
async def create_invoice(customer_id: str, invoice: Invoice):
    
    # Add the customer link to the invoice
    invoice.customer.url = "/customer/" + customer_id
    
    # Turn the invoice instance into a JSON string and store it
    jsonInvoice = jsonable_encoder(invoice)
    fakeInvoiceTable[invoice.invoice_no] = jsonInvoice

    # Read it from the store and return the stored item
    created_invoice = fakeInvoiceTable[invoice.invoice_no]
    
    return JSONResponse(content=created_invoice)

# 5️⃣ Return all invoices for a customer
@app.get("/customer/{customer_id}/invoice")
async def get_invoices(customer_id: str):
    
    # Create Links to the actual invoice (get from DB)
    ex_json = { "id_123456" : "/invoice/123456",
                "id_789101" : "/invoice/789101" 
    }
    return JSONResponse(content=ex_json)

# 6️⃣ Return a specific invoice
@app.get("/invoice/{invoice_no}")
async def read_invoice(invoice_no: int):
    # Option to manually create an invoice
        #ex_inv = Invoice(invoice_no = invnoice_no, invoice_date= "2021-01-05", customer= URLLink(url = "/customer/12345"))
        #json_compatible_item_data = jsonable_encoder(ex_inv)
    
    # Read invoice from the dictionary
    ex_invoice = fakeInvoiceTable[invoice_no]

    # Return the JSON that we stored
    return JSONResponse(content=ex_invoice)