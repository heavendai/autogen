#-*- coding:utf-8 -*-
"""
####################################
# author: daimingyang@baidu.com
# date: 2024-02-28 15:51
# last modified: 2024-02-28 15:51
# filename: tools.py
# description: 
####################################
"""

from serpapi import GoogleSearch
import http.client
import json
import os
from typing import Type
import env_info

from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, Tool, tool


@tool("search_google_news", return_direct=True)
def search_google_news(keyword):
    """‘
    在GoogleNews上搜索keyword，得到相关信息链接列表。
    The keyword that's used to search google news.
    """
    print(f"Keyword: {keyword}")
    search = GoogleSearch({
      "q": keyword,
      "tbm": "nws",
      "api_key": SERPAPI_KEY
    })
    result = search.get_dict()
    return [item['link'] for item in result['news_results']]

class GoogleSearchInfo(BaseModel):
    query: str = Field(description="用于输入Google搜索引擎，查询相关信息。")

class GoogleSearchTool(BaseTool):
    name = "google_search"
    description = "在网络上查询、搜索query，用于调研相关信息。可以得到链接列表。"
    args_schema: Type[BaseModel] = GoogleSearchInfo

    def _run(self, query: str):
        urls = google_search_func(query)
        docs = extract_content_from_url(urls)
        return docs

google_search = GoogleSearchTool()

#@tool("google_search", args_schema=GoogleSearchInfo, return_direct=True)
def google_search_func(query: str) -> str:
    """
    在网络上查询、搜索query，用于调研相关信息。可以得到链接列表。
    The query that's used to search google engine.
    get links.
    """
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
      "q": query
    })
    headers = {
      'X-API-KEY': '79e580c027a4c4393f2d6268619ea887f8d0d4ff',
      'Content-Type': 'application/json'
    }
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = eval(data)
    if 'organic' not in data:
        print("NOT FOUND `organic` in data:", data)
    #return [[x['title'], x['snippet'], x['link']] for x in data['organic']]
    return [x['link'] for x in data['organic']]

def extract_content_from_url(urls):
    """
    从url中提取内容。
    """
    from langchain_community.document_loaders import AsyncHtmlLoader
    from langchain_community.document_transformers import Html2TextTransformer
    loader = AsyncHtmlLoader(urls)
    docs = loader.load()
    html2text = Html2TextTransformer()
    docs_transformed = html2text.transform_documents(docs)
    return docs_transformed

@tool("summary", return_direct=True)
def summary(content):
    """
    对`content`中的文本进行总结
    """
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        #openai_api_base=GPTGOD_INFERENCE_SERVER_URL,
        openai_api_key=OPENAI_API_KEY,
        temperature=0)
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n"], chunk_size=10000, chunk_overlap=500)
    
    if type(content) == list:
        docs = splitter.split_documents(docs_transformed)
    else:
        docs = text_splitter.create_documents([content])
    
    map_prompt = """
    请对下面的文本进行以研究为目的的总结:
    "{text}"
    总结:
    """
    map_prompt_template = PromptTemplate(
        template=map_prompt, input_variables=["text"])

    summary_chain = load_summarize_chain(
        llm=llm,
        chain_type='map_reduce',
        map_prompt=map_prompt_template,
        combine_prompt=map_prompt_template,
        verbose=True
    )
    output = summary_chain.run(input_documents=docs,)
    return output

def generate_llm_config(tool):
    # Define the function schema based on the tool's args_schema
    function_schema = {
        "name": tool.name.lower().replace(" ", "_"),
        "description": tool.description,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }

    if tool.args is not None:
        function_schema["parameters"]["properties"] = tool.args
        #function_schema["parameters"]["required"] = [x for x in tool.args]

    return function_schema
