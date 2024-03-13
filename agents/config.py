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

os.environ['OPENAI_API_KEY'] = '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'
serpapi_key = '2a9fcda3acf4429dc82fe3b6c7e23c65fbf28b24d54fed9b283e6f2d430439fc'

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

config_list_gpt4 = config_list_from_json(env_or_file="OAI_CONFIG_LIST", filter_dict={
        "model": ["gpt-4-0125-preview"],
    })
config_list_qwen = config_list_from_json(env_or_file="OAI_CONFIG_LIST", filter_dict={
        "model": ["qwen_72b_chat"],
    })
config_list_mixtral= config_list_from_json(env_or_file="OAI_CONFIG_LIST", filter_dict={
        "model": ["mixtral"],
    })

llm_func_config_a = {
    "timeout": 1000,
    "seed": 42,
    "config_list": config_list_gpt4,
    "temperature": 0.7,
    "max_tokens": 2048
}

llm_func_config = {
    "timeout": 1000,
    "seed": 42,
    "config_list": config_list_qwen,
    "temperature": 0.001,
    "functions": [
        {
            "name": "search_google_news",
            "description": "Google新闻搜索。Search google news by keyword",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "keyword被用于Google新闻搜索。The keyword that's used to search google news",
                    }
                },
                "required": ["keyword"],
            },
        },
        {
            "name": "search_google",
            "description": "Google搜索引擎搜索关键词。Search google engine by keyword",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "keyword被用于搜索引擎。The keyword that's used to search google engine",
                    }
                },
                "required": ["keyword"],
            },
        },

        {
            "name": "ask_planner",
            "description": "寻问 norm_planner: 1. 为完成一项任务先得到一个规划；2. 验证这个规划的执行结果并进可能提供新的规划。",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "把问题给到 ask_planner. 确认当前问题包含了足够的背景，例如代码和执行结果。norm_planner不知道你可user的对话内容，除非你共享对话内容给norm_planner。",
                    },
                },
                "required": ["message"],
            },
        },

    ],
}
