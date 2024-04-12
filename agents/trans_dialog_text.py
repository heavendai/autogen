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
from tqdm import tqdm
import logging

logging.basicConfig(filename='trans.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#logger = loggin.getLogger(__name__)

UNIT_LINE_COUNT = 60

model = QianfanLLMEndpoint(
        streaming=True,
        model="ERNIE-3.5-8K",
        temperature=0.1,
        #max_tokens=50
    )


def chunk_split(lst, M):
    # 使用列表推导和range()按M切片列表
    return [lst[i:i + M] for i in range(0, len(lst), M)]

def main(src_file, dst_file):
    lines = open(src_file, 'r').readlines()

    chunk_lst = chunk_split(lines, UNIT_LINE_COUNT)
    fp_log = open("trans_dialog_g3.log", 'w')
    fp_dst = open(dst_file, 'w')
    fp_last = open("last.log", 'a')
    logging.warning(len(chunk_lst))
    #for term in chunk_lst:
    for i in tqdm(range(len(chunk_lst))):
        term = chunk_lst[i]
        logging.warning(f"i:{i}, {len(chunk_lst)}\n")
        content = "".join(term)
        human_input = f"""请把下面的对话，转成更合理的语言对话，请一定保证句子标点符号的正确性。并用很口语化的生活用语表述来改写对话内容。
对话如下：```{content}```"""
        fp_log.write(human_input + '\n')
        try:
            ret = model.invoke(human_input)
        except Exception as ex:
            fp_last.write(content + '\n')
            continue

        fp_dst.write(ret + '\n')
        fp_log.write("========\n")

    fp_last.close()
    fp_dst.close()
    fp_log.close()
    return 

if __name__ == "__main__":
    src_file = r'/data1/mingyang/data/dl/concate_info.op.scp.g3'
    dst_file = r'/data1/mingyang/data/dl/concate_info.out.scp.g3'

    main(src_file, dst_file)

