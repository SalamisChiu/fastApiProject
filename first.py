#! /usr/bin/env python3
from fastapi import FastAPI

app = FastAPI()

def index():
    return 'hey'