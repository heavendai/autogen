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

from config import serpapi_key
from serpapi import GoogleSearch

def search_google_news(keyword):
    """
    The keyword that's used to search google news.

    """
    print(f"Keyword: {keyword}")
    search = GoogleSearch({
      "q": keyword,
      "tbm": "nws",
      "api_key": serpapi_key
    })
    result = search.get_dict()
    return [item['link'] for item in result['news_results']]

def search_google(keyword):
    """
    The keyword that's used to search google engine.

    """
    print(f"Keyword: {keyword}")
    search = GoogleSearch({
      "q": keyword,
      "api_key": serpapi_key
    })
    result = search.get_dict()
    return [item['link'] for item in result['news_results']]


