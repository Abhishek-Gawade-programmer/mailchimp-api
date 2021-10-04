from typing import Optional
from fastapi import FastAPI

import os
from pathlib import Path
from dotenv import load_dotenv

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/getalllists")
async def get_all_lists():
    ## ALL LIST
    response = mailchimp.lists.get_all_lists()
    print(response)
    return {"done": 'true', 'response': response}


@app.get("/addmember/{email}")
async def add_member(email: str):
    response = mailchimp.lists.add_list_member(
        os.getenv('LIST_ID'), {"email_address": email, "status": "subscribed"}
    )
    return {"done": 'true', 'response': response}


@app.get("/getallmember")
async def get_all_members():
    # GET MEMBER INFO
    response = mailchimp.lists.get_list_members_info(os.getenv('LIST_ID'))
    return {"done": 'true', 'response': response.get('members')}
