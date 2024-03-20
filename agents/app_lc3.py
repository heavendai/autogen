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

import chainlit as cl
import logging
import os

log_file = os.path.abspath(__file__)
print("log_file:", os.path.basename(log_file) + ".log")

logging.basicConfig(level = logging.WARNING, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', \
        filename=log_file, filemode="a")


#inference_server_url = "https://gptgod.online/api/v1"
#"gpt-4-0125-preview",
#llm_name = 'qwen_72b_chat'

@cl.password_auth_callback
def auth_callback(username: str, password: str):
    # Fetch the user matching username from your database
    # and compare the hashed password with the value stored in the database
    if (username, password) == ("admin", "autism"):
        return cl.User(
            identifier="admin", metadata={"role": "admin", "provider": "credentials"}
        )
    else:
        return None


@cl.on_chat_start
async def on_chat_start():
    """
    model = ChatOpenAI(streaming=False,
                    model=llm_name,
                    #openai_api_key="sk-2CKHg2AXZdFqchl18m8zEUFlVBT9lVVZIOwTBIRZQjnZgWZR",
                    openai_api_key="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", # openai
                    openai_api_base=inference_server_url,
                    temperature=0.01,
                    max_tokens=25
                )
    """
    model = QianfanLLMEndpoint(
            streaming=True,
            model="ERNIE-Bot-4",
            temperature=0.01,
            max_tokens=25
        )

    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content="""你是一个超级AI助理，在自闭症教育、治疗领域是专家。我会告诉你关于自闭症儿童的一些分类，以及每个类型下的患者的特点，需要你切换到对应的自闭症指导老师的身份，针对这个分类下的患者做陪聊工作，从而帮助患者成长、生活。你说话应该足够简洁，不要长篇大论，患者不喜欢太复杂的内容，一次理解不了太多的内容。请直接输出说要说的句子，不要输出心理过程，不要输出任务前缘词，直接输出你要说的内容。

类型1：高功能自闭症儿童（亚斯伯格综合症）
针对有特定兴趣和较好语言沟通能力的儿童设计对话，通过讨论他们感兴趣的主题来鼓励交流和学习。
例如：“让我们谈谈你最喜欢的事情。是恐龙、宇宙还是编程？你可以告诉我你喜欢它的原因，或者我们可以一起解决一个关于它的谜题。”
类型2：非言语或低功能自闭症儿童
为这类儿童设计使用图片和简单词语作为交流的媒介，减少语言交流的压力。
例如：“我是一个喜欢安静的朋友，可以用图片或简单的词语和你聊天。你今天想看什么图片？动物、汽车还是星星？”
类型3：社交交往困难的儿童
针对社交交往能力较弱的儿童，通过设定社交场景和问题，帮助他们练习和思考社交互动的方式。你说话应该足够简洁，不要长篇大论，患者不喜欢太复杂的内容。
例如：“如果你今天在学校（或在公园、生日派对）和别的孩子玩，你会选择什么游戏？如果有人不明白游戏规则，可以请你教他们吗？”

在正式开始后，会告诉你对方是哪种类型的患者，你再切换到对应的身份开始正式的陪聊工作。这是一项很有意义，很需要耐心的工作，你要认真对待，全力发挥自己的能力。
                """,
            ),
            MessagesPlaceholder(
                    variable_name="chat_history"
                ),
            HumanMessagePromptTemplate.from_template(
                    "{human_input}"
                ),
        ]
    )
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    chain = LLMChain(llm=model, prompt=prompt, output_parser=StrOutputParser(), memory=memory)

    cl.user_session.set("chain", chain)
    #await cl.Message(content="请选择自闭症类型：高功能类型，非语言低功能类型，社交交往困难型\n\n\t【】为说话内容\n\t（）为心理过程", author="Huiting").send()
    await cl.Message(content="请选择自闭症类型：高功能类型，非语言低功能类型，社交交往困难型", author="Huiting").send()

answer_prefix_tokens=["FINAL", "ANSWER"]

class MyCustomHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        print(f"My custom handler, token: {token}")


@cl.on_message
async def on_message(message: cl.Message):

    logging.info("\n\n")
    logging.info("query:%s\n\n" % message.content)

    chain = cl.user_session.get("chain")  # type: LLMChain

    async with cl.Step(name="Processing") as parent_step:
        parent_step.input = "Bot input"
        parent_step.output = "Processing......"

    res = await chain.arun(
        human_input=message.content, 
        #callbacks=[cl.LangchainCallbackHandler(stream_final_answer=True,answer_prefix_tokens=answer_prefix_tokens,)]
        callbacks=[]
    )

    #await cl.Message(content=res, author="Teacher").send()
    msg = cl.Message(content="", author="Teacher")
    for token in res:
        logging.info(token)
        await msg.stream_token(token)
    await msg.send()

