#-*- coding:utf-8 -*-
"""
####################################
# author: daimingyang@ht.com
# date: 2024-04-16 14:02
# last modified: 2024-04-16 14:02
# filename: client.py
# description: 
####################################
"""
import requests


# 第一轮
chat_history = []
content = '高功能型自闭症'
print(content)
chat_history = [{'role': 'human', 'content': content}]

response = requests.post(
    'http://localhost:7874/v1/chat/completions/stream',
    json={'input': {'human_input': '高功能型自闭症', 'chat_history': []}}, stream=True,
)

tmp = ''
#streaming output
for chunk in response.iter_content(decode_unicode=True):
    tmp += chunk
    print(chunk, end="", flush=True)
    
vec = tmp.split('event: data\r\n')
terms = [x[x.find("\"")+1:x.rfind("\"")] for x in vec[1:-1]]
content = {'role': 'AI', 'content':'%s' % ''.join(terms)}
chat_history.append(content)

# 第二轮
content = '我喜欢科学'
print(content)
chat_history.append({'role': 'human', 'content': '%s' % (content)})
response = requests.post(
    'http://localhost:7874/v1/chat/completions/stream',
    json={'input': {'human_input': content, 'chat_history': chat_history}}, stream=True,
    headers={"Content-Type": "application/json"}
)
tmp = ''
for chunk in response.iter_content(decode_unicode=True):
    tmp += chunk
    print(chunk, end="", flush=True)
vec = tmp.split('event: data\r\n')
terms = [x[x.find("\"")+1:x.rfind("\"")] for x in vec[1:-1]]
content = {'role': 'AI', 'content': '%s' % ''.join(terms)}
chat_history.append(content)
