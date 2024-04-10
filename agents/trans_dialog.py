#-*- coding:utf-8 -*-
"""
####################################
# author: daimingyang@huitingtech.com
# date: 2024-04-10 20:29
# last modified: 2024-04-10 20:29
# filename: trans_dialog.py
# description: 
####################################
"""
import os, sys

from langchain.chat_models import ChatAnthropic, ChatOpenAI

from langserve import add_routes

from langchain_openai import ChatOpenAI
from langchain.schema import StrOutputParser
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import SystemMessage
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.callbacks import BaseCallbackHandler
from langchain_community.llms import QianfanLLMEndpoint

from typing import Any, Dict, List, Union

"""
model = QianfanLLMEndpoint(
        streaming=True,
        model="ERNIE-Bot-4",
        temperature=0.7,
        max_tokens=20
    )

"""
#ret1 = model.invoke("""请把下面的对话，转成更合理的语言对话，请一定保证句子标点符号的正确性。并用很口语化的生活用语表述来改写对话内容。
#对话如下：{input}""")

def chunk_split(lst, M):
    # 使用列表推导和range()按M切片列表
    return [lst[i:i + M] for i in range(0, len(lst), M)]

def main(src_file, dst_file):
    lines = open(src_file, 'r').readlines()

    chunk_lst = chunk_split(lines, 40)
    print(chunk_lst)
    #fp_dst = open(dst_file, 'w')
    #fp_dst.close()
    return 

if __name__ == "__main__":
    src_file = r''
    dst_file = r''
    main(src_file, dst_file)

