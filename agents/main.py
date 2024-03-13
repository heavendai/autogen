#-*- coding:utf-8 -*-
"""
####################################
# author: daimingyang@baidu.com
# date: 2024-02-28 15:36
# last modified: 2024-02-28 15:36
# filename: main.py
# description: 
####################################
"""
import config
from agents import assistant, user_proxy, user_proxy_terminate

user_proxy.initiate_chat(
        assistant,
        message="最近半年有哪些MultiAgent的开源框架比较著名，这些框架各自的特点是什么？",
        )
