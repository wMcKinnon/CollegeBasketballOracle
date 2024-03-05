#!/usr/bin/env python3
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from db import CollegeRatings

def get_net():
    response = requests.get("https://www.ncaa.com/rankings/basketball-men/d1/ncaa-mens-basketball-net-rankings")
    return response.json()["Rank"]["School"]

def get_kenpom():
    response = requests.get("https://kenpom.com/")
    return response.json()["Team"]["AdjEM"]

def get_barttorvik():
    response = requests.get("https://www.barttorvik.com/trank.php#")
    return response.json()["Team"]["AdjEM"]