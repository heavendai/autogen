#-*- coding:utf-8 -*-
"""
####################################
# author: daimingyang
# date: 2024-05-09 13:48
# last modified: 2024-05-09 13:53
# filename: env_info.py
# description: 
####################################
"""
import os

ABS_PATH = os.path.dirname(os.path.abspath(__file__))

def _load_env() -> None:
    """
    # Loading the .env file if it exists
    """
    dotenv_path = os.path.join(ABS_PATH, ".env")
    if os.path.exists(dotenv_path):
        from dotenv import load_dotenv
        load_dotenv(dotenv_path)
_load_env()
