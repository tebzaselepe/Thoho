import os
import pprint
import datetime
from datetime import date
import pandas as pd
import streamlit as st
import datetime
from typing import Dict, List, Literal, Optional, Set
import pymongo
from pymongo import MongoClient

# server connection/creation
# connection_str = f"mongodb+srv://cluster0.sfcysmi.mongodb.net/test?tls=true&tlsCertificateKeyFile=C%3A%5CUsers%5CPfunzo%5CDesktop%5Cstreamlit_mongo%5CX509-cert-3952646099818541177.pem&tlsAllowInvalidCertificates=true&tlsAllowInvalidHostnames=true&authMechanism=MONGODB-X509&authSource=%24external"
connection_str = "mongodb://localhost:27017"
client = MongoClient(connection_str)


# getting DB from server
db = client.tfs_db
# getting collections from DB
clients = db.new_client_data
employees = db.emps

def insert_client_doc(first_name,last_name,email,phone_no,gender,race,id_no,dob,id_photo,payment_method,beneficiary_names,beneficiary_phone,policy_type,policy_cover,policy_premium,start_date,dependents):

    client_document = {
        "first_name" : first_name,
        "last_name" : last_name,
        "email" : email,
        "phone_no" : phone_no,
        "gender" : gender,
        "race" : race,
        "id_no" : id_no,
        "date_of_birth" : dob.isoformat(),
        "age" : calculate_age(dob),
        "photo_id" : id_photo,
        "payment_method" : payment_method,
        "beneficiary" : {
            "full_names" : beneficiary_names,
            "contact_phone" : beneficiary_phone
        },
        "policy" : {
            "type" : policy_type,
            "cover" : policy_cover,
            "premium" : policy_premium,
            "start_date" : start_date,
            "status" : determine_policy_status()
        },
        "dependents" : dependents
    }
    clients.insert_one(client_document)
    
def show_client_data():
    items = clients.find()
    items = list(items)
    return items

def determine_policy_status():
    status = 'new'
    return status

def insert_emp_doc(first_name,last_name,email,password,role,status):
    today = datetime.date.today()
    emp_doc = {
        "first_name" : first_name,
        "last_name" : last_name,
        "email" : email,
        "password" : password,
        "role" : role,
        "hire_date" : today,
        "status" : status
    }
    inserted_id =  employees.insert_one(emp_doc).inserted_id

def calculate_age(dob):
    today = datetime.date.today()
    age = today.year - dob.year
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        age -= 1
    return age

def calculate_policy_premium(policy_type, num_dependants):
    if policy_type == "silver":
        if num_dependants == 0:
            return 100.00
        else:
            return 150.00
    elif policy_type == "gold":
        if num_dependants == 0:
            return 200.00
    else:
        return 300.00        
    if num_dependants == 0:
        return 300.00
    else:
        return 450.00        