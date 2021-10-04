from typing import Optional
from fastapi import FastAPI

import os
from pathlib import Path
from dotenv import load_dotenv

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')
mailchimp = MailchimpMarketing.Client()
mailchimp.set_config({"api_key": os.getenv('API_KEY'), "server": os.getenv('SERVER')})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/getalllists")
def get_all_lists():
    ## ALL LIST
    response = mailchimp.lists.get_all_lists()
    print(response)
    return {"done": 'true', 'response': response}


@app.get("/addmember/{email}")
def add_member(email: str):
    response = mailchimp.lists.add_list_member(
        os.getenv('LIST_ID'), {"email_address": email, "status": "subscribed"}
    )
    return {"done": 'true', 'response': response}


@app.get("/getallmember")
def get_all_members():
    # GET MEMBER INFO
    response = mailchimp.lists.get_list_members_info(os.getenv('LIST_ID'))
    return {"done": 'true', 'response': response.get('members')}
