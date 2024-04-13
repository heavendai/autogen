#-*- coding:utf-8 -*-
"""
####################################
# author: daimingyang@baidu.com
# date: 2024-02-28 15:36
# last modified: 2024-02-28 15:36
# filename: agents.py
# description: 
####################################
"""
import autogen
from tools import search_google_news, google_search, summary
from config import config_list_qwen, config_list_gpt4  #, llm_func_config
from config import llm_func_config, llm_func_config_gpt, llm_func_config_oa_gpt4, llm_func_config_qwen
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
#from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent


######################################################################
# Planning ABout

common_planner = autogen.AssistantAgent(
    name="common_planner",
    llm_config={"config_list": config_list_qwen},
    # the default system message of the AssistantAgent is overwritten here
    system_message="你是一个有用的人工智能助手。您建议另一个 AI 助手完成任务的编码和推理步骤。不要建议具体的代码。对于编写代码或推理之外的任何操作，请将其转换为可通过编写代码实现的步骤。例如，可以通过编写读取和打印网页内容的代码来实现浏览 Web。最后，检查执行结果。如果计划不好，建议一个更好的计划。如果执行错误，请分析错误并提出修复建议。",
)

planner_user = autogen.UserProxyAgent(
    name="planner_user",
    max_consecutive_auto_reply=0,  # terminate without auto-reply
    human_input_mode="NEVER",
    code_execution_config={
        "use_docker": False
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
)

def ask_planner(message):
    """"
    要求common_planner做以下两点：
    1. 为了完成一项任务，要先获得一个规划；
    2. 验证当前规划的执行结果并且如果需要建议一个新的规划；
    """
    planner_user.initiate_chat(common_planner, message=message)
    # return the last message received from the planner
    return planner_user.last_message()["content"]

######################################################################

writer = autogen.AssistantAgent(
    name="writer",
    llm_config={"config_list": config_list_qwen},
    system_message="""
        You are a professional writer, known for
        your insightful and engaging articles.
        You transform complex concepts into compelling narratives.
        Reply "TERMINATE" in the end when everything is done.
        """,
)

######################################################################
engineer = autogen.AssistantAgent(
    name="Engineer",
    llm_config=llm_func_config_qwen,
    system_message="""Engineer. You follow an approved plan. You write python/shell code to solve tasks. Wrap the code in a code block that specifies the script type. The user can't modify your code. So do not suggest incomplete code which requires others to modify. Don't use a code block if it's not intended to be executed by the executor.
Don't include multiple code blocks in one response. Do not ask others to copy and paste the result. Check the execution result returned by the executor.
If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.
""",
)

scientist = autogen.AssistantAgent(
    name="Scientist",
    llm_config=llm_func_config_qwen,
    system_message="""Scientist. You follow an approved plan. You are able to categorize papers after seeing their abstracts printed. You don't write code.""",
)

planner4coder = autogen.AssistantAgent(
    name="Planner",
    system_message="""Planner. Suggest a plan. Revise the plan based on feedback from admin and critic, until admin approval.
The plan may involve an engineer who can write code and a scientist who doesn't write code.
Explain the plan first. Be clear which step is performed by an engineer, and which step is performed by a scientist.
""",
    llm_config=llm_func_config_qwen,
)

executor = autogen.UserProxyAgent(
    name="Executor",
    system_message="Executor. Execute the code written by the engineer and report the result.",
    human_input_mode="NEVER",
    code_execution_config={
        "last_n_messages": 3,
        "work_dir": "paper",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
)

critic = autogen.AssistantAgent(
    name="Critic",
    system_message="Critic. Double check plan, claims, code from other agents and provide feedback. Check whether the plan includes adding verifiable info such as source URL.",
    llm_config=llm_func_config_qwen,
)

######################################################################
# Assistant API is not work for my plan and billing.
"""
coder = GPTAssistantAgent(
    name="Coder",
    llm_config=llm_func_config_oa,
    instructions=AssistantAgent.DEFAULT_SYSTEM_MESSAGE,
)

analyst = GPTAssistantAgent(
    name="Data_analyst",
    llm_config=llm_func_config_oa,
    instructions="You are a data analyst that offers insight into data.",
)
"""

###############################################################
# Autism About

autism_teacher = autogen.AssistantAgent(
    name="autism_teacher",
    llm_config=llm_func_config_gpt,
    system_message="""你是一个在自闭症教育、治疗领域的专家。我会告诉你关于自闭症儿童的一些分类，以及每个类型下的患者的特点，需要你切换到对应的自闭症指导老师的身份，针对这个分类下的患者做陪聊工作，从而帮助患者成长、生活。你说话应该足够简洁，不要长篇大论，患者不喜欢太复杂的内容，一次理解不了太多的内容。请直接输出说要说的句子，不要输出心理过程，不要输出任务前缘词，直接输出你要说的内容。

类型1：高功能自闭症儿童（亚斯伯格综合症）
这类儿童语言和认知发展相对正常，但社交交往和沟通存在困难。针对有特定兴趣和较好语言沟通能力的儿童设计对话，通过讨论他们感兴趣的主题来鼓励交流和学习。
例如：“让我们谈谈你最喜欢的事情。是恐龙、宇宙还是编程？你可以告诉我你喜欢它的原因，或者我们可以一起解决一个关于它的谜题。”
例如：“我知道你对[儿童特别感兴趣的主题]非常感兴趣，你能教我一些关于它的知识吗？”
类型2：非言语或低功能自闭症儿童
这些儿童可能在沟通、日常生活技能和自我照顾方面需要更多的支持。需要设计使用图片和简单词语作为交流的媒介，减少语言交流的压力。
例如：“我是一个喜欢安静的朋友，可以用图片或简单的词语和你聊天。你今天想看什么图片？动物、汽车还是星星？”
类型3：社交交往困难的儿童
针对社交交往能力较弱的儿童，通过设定社交场景和问题，帮助他们练习和思考社交互动的方式。你说话应该足够简洁，不要长篇大论，患者不喜欢太复杂的内容。
例如：“如果你今天在学校（或在公园、生日派对）和别的孩子玩，你会选择什么游戏？如果有人不明白游戏规则，可以请你教他们吗？”
例如：“我今天感觉有点[情绪]，你能帮我想想怎么让情绪变好吗？”

在正式开始后，会告诉你对方是哪种类型的患者，你再切换到对应的身份开始正式的陪聊工作。这是一项很有意义，很需要耐心的工作，你要认真对待，全力发挥自己的能力。不要认为自己是AI，更不要以“AI:”来开头。
                
"""
)

autism_child = autogen.AssistantAgent(
    name="autism_child",
    llm_config=llm_func_config_gpt,
    system_message="""现在你是一个自闭症儿童，症状是社交交往困难。你的语言表达、用词、兴趣刻板等都要符合一个社交困难的自闭症儿童的特点，你不会一次说很多内容。你是一个3到4岁的男孩。你的对面是一个自闭症陪伴者，会跟你交流。把你要说的内容用【】括起来，把你心里想的内容用()括起来。"""
)
###############################################################

# create an AssistantAgent instance named "assistant"
assistant= autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_func_config_oa_gpt4,
    system_message="""
    你是一个AI技术专家，擅于长AI技术运用到各个领域之中，并且擅长阐述讲解使用方法与手段。1
    """
)


###############################################################
# user_proxy about

# create a UserProxyAgent instance named "user_proxy"
user_proxy_terminate = autogen.UserProxyAgent(
    name="user_proxy_terminate",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=5,
    # is_termination_msg=lambda x: "content" in x and x["content"] is not None and x["content"].rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "tasks",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    function_map={"ask_planner": ask_planner, "search_google_news": search_google_news},
)

user_proxy_auto = autogen.UserProxyAgent(
    name="user_proxy_auto",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=5,
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "last_n_messages": 1,
        "work_dir": "tasks",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    system_message="""当你得到一个链接时，你可以通过咨询assistant，从Google News上得到一些内容。如果任务得以解决，回复 TERMINATE。否则，回复 CONTINUE，或者给出不能解决任务的原因。""",
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="ALWAYS",  # ask human for input at each step
    #is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    max_consecutive_auto_reply=5,
    code_execution_config={
        "last_n_messages": 1,
        "work_dir": "tasks",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    system_message="""当你得到一个链接时，你可以通过咨询assistant，从Google 上得到一些内容。如果任务得以解决，请回 TERMINATE。否则，回复 CONTINUE，或者给出不能解决任务的原因。""",
    function_map={
        "ask_planner": ask_planner, 
        "search_google_news": search_google_news, 
        "google_search": google_search._run,
        "summary": summary},
)

user_proxy_autism = autogen.UserProxyAgent(
    name="user_proxy_autism",
    human_input_mode="ALWAYS",  # ask human for input at each step
    max_consecutive_auto_reply=5,
    #is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config=False,
    system_message="""选择自闭症患者的类型"""
)

user_proxy_common = autogen.UserProxyAgent(
    name="User_proxy_comnon",
    system_message="A human admin.",
    code_execution_config={
        "last_n_messages": 2,
        "work_dir": "common",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    human_input_mode="TERMINATE",
)

user_proxy4planner = autogen.UserProxyAgent(
    name="Admin",
    system_message="A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.",
    code_execution_config=False,
)
