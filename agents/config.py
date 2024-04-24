#-*- coding:utf-8 -*-
"""
####################################
# author: daimingyang@baidu.com
# date: 2024-02-28 15:36
# last modified: 2024-02-28 15:36
# filename: config.py
# description: 
####################################
"""
import os
from autogen import config_list_from_json
from tools import generate_llm_config
from tools import search_google_news, google_search, summary

os.environ['OPENAI_API_KEY'] = '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'

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

config_list_gpt4 = config_list_from_json(env_or_file="OAI_CONFIG_LIST", filter_dict={
        "model": ["gpt-4-0125-preview"],
    })
config_list_oa_gpt4 = config_list_from_json(env_or_file="OAI_CONFIG_LIST", filter_dict={
        #"model": ["gpt-4-1106-preview"],
        "model": ["gpt-4-0125-preview"],
    })

config_list_qwen = config_list_from_json(env_or_file="OAI_CONFIG_LIST", filter_dict={
        "model": ["qwen_72b_chat"],
    })
config_list_mixtral= config_list_from_json(env_or_file="OAI_CONFIG_LIST", filter_dict={
        "model": ["mixtral"],
    })

llm_func_config_gpt = {
    "timeout": 1000,
    "seed": 42,
    "config_list": config_list_gpt4,
    "temperature": 0.7,
    "max_tokens": 1024
}

llm_func_config_oa_gpt4 = {
    "timeout": 1000,
    "seed": 42,
    "config_list": config_list_oa_gpt4,
    "temperature": 0.1,
    "max_tokens": 1024
}

llm_func_config_qwen = {
   "timeout": 1000,
    "seed": 42,
    "config_list": config_list_qwen,
    "temperature": 0.0000001,
    "max_tokens": 2048
}

llm_func_config = {
   "timeout": 1000,
    "seed": 42,
    "config_list": config_list_qwen,
    "temperature": 0.0000001,
    "functions": [
        generate_llm_config(google_search)
    ]
}
#generate_llm_config(search_google_news),
#generate_llm_config(summary)
    
llm_func_config_bak = {
    "timeout": 1000,
    "seed": 42,
    "config_list": config_list_qwen,
    "temperature": 0.0000001,
    "functions": [
        {
            "name": "search_google_news",
            "description": "Google新闻搜索。Search google news by keyword",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "keyword被用于Google新闻搜索。The keyword that's used to search google news"
                    }
                },
                "required": ["keyword"]
            }
        },
        {
            "name": "google_search",
            "description": "Google搜索引擎搜索关键词。Search google engine by query",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "query用于输入搜索引擎。The query that's used to search google engine"
                    }
                },
                "required": ["query"]
            }
        },
        {
            "name": "ask_planner",
            "description": "任务规划器。遇到任务先询问 ·norm_planner·: 1. 为完成一项任务先得到一个规划；2. 验证这个规划的执行结果并尽可能提供新的更合适的规划。",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "把问题给到 ask_planner. 确认当前问题包含了足够的背景，例如代码和执行结果。norm_planner不知道你和user的对话内容，除非你共享对话内容给norm_planner。"
                    }
                },
                "required": ["message"]
            }
        },
        {
            "name": "summary",
            "description": "对文本内容进行总结",
            "parameters": {
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": "文本内容，需要进行总结"
                    }
                },
                "required": ["content"]
            }
        }
    ]
}
