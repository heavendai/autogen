"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[6117],{85:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>c,contentTitle:()=>l,default:()=>h,frontMatter:()=>i,metadata:()=>r,toc:()=>a});var o=n(5893),s=n(1151);const i={title:"AutoGen with Custom Models: Empowering Users to Use Their Own Inference Mechanism",authors:["olgavrou"],tags:["AutoGen"]},l=void 0,r={permalink:"/autogen/blog/2024/01/26/Custom-Models",source:"@site/blog/2024-01-26-Custom-Models/index.mdx",title:"AutoGen with Custom Models: Empowering Users to Use Their Own Inference Mechanism",description:"TL;DR",date:"2024-01-26T00:00:00.000Z",formattedDate:"January 26, 2024",tags:[{label:"AutoGen",permalink:"/autogen/blog/tags/auto-gen"}],readingTime:5.455,hasTruncateMarker:!1,authors:[{name:"Olga Vrousgou",title:"Senior Software Engineer at Microsoft Research",url:"https://github.com/olgavrou/",imageURL:"https://github.com/olgavrou.png",key:"olgavrou"}],frontMatter:{title:"AutoGen with Custom Models: Empowering Users to Use Their Own Inference Mechanism",authors:["olgavrou"],tags:["AutoGen"]},unlisted:!1,prevItem:{title:"Anny: Assisting AutoGen Devs Via AutoGen",permalink:"/autogen/blog/2024/02/02/AutoAnny"},nextItem:{title:"AutoGenBench -- A Tool for Measuring and Evaluating AutoGen Agents",permalink:"/autogen/blog/2024/01/25/AutoGenBench"}},c={authorsImageUrls:[void 0]},a=[{value:"TL;DR",id:"tldr",level:2},{value:"Quickstart",id:"quickstart",level:2},{value:"Step 1: Create the custom model client class",id:"step-1-create-the-custom-model-client-class",level:3},{value:"Step 2: Add the configuration to the OAI_CONFIG_LIST",id:"step-2-add-the-configuration-to-the-oai_config_list",level:3},{value:"Step 3: Register the new custom model to the agent that will use it",id:"step-3-register-the-new-custom-model-to-the-agent-that-will-use-it",level:3},{value:"Protocol details",id:"protocol-details",level:2},{value:"Troubleshooting steps",id:"troubleshooting-steps",level:2},{value:"Conclusion",id:"conclusion",level:2}];function d(e){const t={a:"a",code:"code",h2:"h2",h3:"h3",li:"li",p:"p",pre:"pre",strong:"strong",ul:"ul",...(0,s.a)(),...e.components};return(0,o.jsxs)(o.Fragment,{children:[(0,o.jsx)(t.h2,{id:"tldr",children:"TL;DR"}),"\n",(0,o.jsx)(t.p,{children:"AutoGen now supports custom models! This feature empowers users to define and load their own models, allowing for a more flexible and personalized inference mechanism. By adhering to a specific protocol, you can integrate your custom model for use with AutoGen and respond to prompts any way needed by using any model/API call/hardcoded response you want."}),"\n",(0,o.jsx)(t.p,{children:(0,o.jsx)(t.strong,{children:"NOTE: Depending on what model you use, you may need to play with the default prompts of the Agent's"})}),"\n",(0,o.jsx)(t.h2,{id:"quickstart",children:"Quickstart"}),"\n",(0,o.jsxs)(t.p,{children:["An interactive and easy way to get started is by following the notebook ",(0,o.jsx)(t.a,{href:"https://github.com/microsoft/autogen/blob/main/notebook/agentchat_custom_model.ipynb",children:"here"})," which loads a local model from HuggingFace into AutoGen and uses it for inference, and making changes to the class provided."]}),"\n",(0,o.jsx)(t.h3,{id:"step-1-create-the-custom-model-client-class",children:"Step 1: Create the custom model client class"}),"\n",(0,o.jsxs)(t.p,{children:["To get started with using custom models in AutoGen, you need to create a model client class that adheres to the ",(0,o.jsx)(t.code,{children:"ModelClient"})," protocol defined in ",(0,o.jsx)(t.code,{children:"client.py"}),". The new model client class should implement these methods:"]}),"\n",(0,o.jsxs)(t.ul,{children:["\n",(0,o.jsxs)(t.li,{children:[(0,o.jsx)(t.code,{children:"create()"}),": Returns a response object that implements the ",(0,o.jsx)(t.code,{children:"ModelClientResponseProtocol"})," (more details in the Protocol section)."]}),"\n",(0,o.jsxs)(t.li,{children:[(0,o.jsx)(t.code,{children:"message_retrieval()"}),": Processes the response object and returns a list of strings or a list of message objects (more details in the Protocol section)."]}),"\n",(0,o.jsxs)(t.li,{children:[(0,o.jsx)(t.code,{children:"cost()"}),": Returns the cost of the response."]}),"\n",(0,o.jsxs)(t.li,{children:[(0,o.jsx)(t.code,{children:"get_usage()"}),": Returns a dictionary with keys from ",(0,o.jsx)(t.code,{children:'RESPONSE_USAGE_KEYS = ["prompt_tokens", "completion_tokens", "total_tokens", "cost", "model"]'}),"."]}),"\n"]}),"\n",(0,o.jsx)(t.p,{children:"E.g. of a bare bones dummy custom class:"}),"\n",(0,o.jsx)(t.pre,{children:(0,o.jsx)(t.code,{className:"language-python",children:'class CustomModelClient:\n    def __init__(self, config, **kwargs):\n        print(f"CustomModelClient config: {config}")\n\n    def create(self, params):\n        num_of_responses = params.get("n", 1)\n\n        # can create my own data response class\n        # here using SimpleNamespace for simplicity\n        # as long as it adheres to the ModelClientResponseProtocol\n\n        response = SimpleNamespace()\n        response.choices = []\n        response.model = "model_name" # should match the OAI_CONFIG_LIST registration\n\n        for _ in range(num_of_responses):\n            text = "this is a dummy text response"\n            choice = SimpleNamespace()\n            choice.message = SimpleNamespace()\n            choice.message.content = text\n            choice.message.function_call = None\n            response.choices.append(choice)\n        return response\n\n    def message_retrieval(self, response):\n        choices = response.choices\n        return [choice.message.content for choice in choices]\n\n    def cost(self, response) -> float:\n        response.cost = 0\n        return 0\n\n    @staticmethod\n    def get_usage(response):\n        return {}\n'})}),"\n",(0,o.jsx)(t.h3,{id:"step-2-add-the-configuration-to-the-oai_config_list",children:"Step 2: Add the configuration to the OAI_CONFIG_LIST"}),"\n",(0,o.jsxs)(t.p,{children:["The field that is necessary is setting ",(0,o.jsx)(t.code,{children:"model_client_cls"})," to the name of the new class (as a string) ",(0,o.jsx)(t.code,{children:'"model_client_cls":"CustomModelClient"'}),". Any other fields will be forwarded to the class constructor, so you have full control over what parameters to specify and how to use them. E.g.:"]}),"\n",(0,o.jsx)(t.pre,{children:(0,o.jsx)(t.code,{className:"language-json",children:'{\n    "model": "Open-Orca/Mistral-7B-OpenOrca",\n    "model_client_cls": "CustomModelClient",\n    "device": "cuda",\n    "n": 1,\n    "params": {\n        "max_length": 1000,\n    }\n}\n'})}),"\n",(0,o.jsx)(t.h3,{id:"step-3-register-the-new-custom-model-to-the-agent-that-will-use-it",children:"Step 3: Register the new custom model to the agent that will use it"}),"\n",(0,o.jsxs)(t.p,{children:["If a configuration with the field ",(0,o.jsx)(t.code,{children:'"model_client_cls":"<class name>"'})," has been added to an Agent's config list, then the corresponding model with the desired class must be registered after the agent is created and before the conversation is initialized:"]}),"\n",(0,o.jsx)(t.pre,{children:(0,o.jsx)(t.code,{className:"language-python",children:"my_agent.register_model_client(model_client_cls=CustomModelClient, [other args that will be forwarded to CustomModelClient constructor])\n"})}),"\n",(0,o.jsxs)(t.p,{children:[(0,o.jsx)(t.code,{children:"model_client_cls=CustomModelClient"})," arg matches the one specified in the ",(0,o.jsx)(t.code,{children:"OAI_CONFIG_LIST"})," and ",(0,o.jsx)(t.code,{children:"CustomModelClient"})," is the class that adheres to the ",(0,o.jsx)(t.code,{children:"ModelClient"})," protocol (more details on the protocol below)."]}),"\n",(0,o.jsx)(t.p,{children:"If the new model client is in the config list but not registered by the time the chat is initialized, then an error will be raised."}),"\n",(0,o.jsx)(t.h2,{id:"protocol-details",children:"Protocol details"}),"\n",(0,o.jsxs)(t.p,{children:["A custom model class can be created in many ways, but needs to adhere to the ",(0,o.jsx)(t.code,{children:"ModelClient"})," protocol and response structure which is defined in ",(0,o.jsx)(t.code,{children:"client.py"})," and shown below."]}),"\n",(0,o.jsx)(t.p,{children:"The response protocol is currently using the minimum required fields from the autogen codebase that match the OpenAI response structure. Any response protocol that matches the OpenAI response structure will probably be more resilient to future changes, but we are starting off with minimum requirements to make adpotion of this feature easier."}),"\n",(0,o.jsx)(t.pre,{children:(0,o.jsx)(t.code,{className:"language-python",children:'\nclass ModelClient(Protocol):\n    """\n    A client class must implement the following methods:\n    - create must return a response object that implements the ModelClientResponseProtocol\n    - cost must return the cost of the response\n    - get_usage must return a dict with the following keys:\n        - prompt_tokens\n        - completion_tokens\n        - total_tokens\n        - cost\n        - model\n\n    This class is used to create a client that can be used by OpenAIWrapper.\n    The response returned from create must adhere to the ModelClientResponseProtocol but can be extended however needed.\n    The message_retrieval method must be implemented to return a list of str or a list of messages from the response.\n    """\n\n    RESPONSE_USAGE_KEYS = ["prompt_tokens", "completion_tokens", "total_tokens", "cost", "model"]\n\n    class ModelClientResponseProtocol(Protocol):\n        class Choice(Protocol):\n            class Message(Protocol):\n                content: Optional[str]\n\n            message: Message\n\n        choices: List[Choice]\n        model: str\n\n    def create(self, params) -> ModelClientResponseProtocol:\n        ...\n\n    def message_retrieval(\n        self, response: ModelClientResponseProtocol\n    ) -> Union[List[str], List[ModelClient.ModelClientResponseProtocol.Choice.Message]]:\n        """\n        Retrieve and return a list of strings or a list of Choice.Message from the response.\n\n        NOTE: if a list of Choice.Message is returned, it currently needs to contain the fields of OpenAI\'s ChatCompletion Message object,\n        since that is expected for function or tool calling in the rest of the codebase at the moment, unless a custom agent is being used.\n        """\n        ...\n\n    def cost(self, response: ModelClientResponseProtocol) -> float:\n        ...\n\n    @staticmethod\n    def get_usage(response: ModelClientResponseProtocol) -> Dict:\n        """Return usage summary of the response using RESPONSE_USAGE_KEYS."""\n        ...\n\n'})}),"\n",(0,o.jsx)(t.h2,{id:"troubleshooting-steps",children:"Troubleshooting steps"}),"\n",(0,o.jsx)(t.p,{children:"If something doesn't work then run through the checklist:"}),"\n",(0,o.jsxs)(t.ul,{children:["\n",(0,o.jsxs)(t.li,{children:["Make sure you have followed the client protocol and client response protocol when creating the custom model class","\n",(0,o.jsxs)(t.ul,{children:["\n",(0,o.jsxs)(t.li,{children:[(0,o.jsx)(t.code,{children:"create()"})," method: ",(0,o.jsx)(t.code,{children:"ModelClientResponseProtocol"})," must be followed when returning an inference response during ",(0,o.jsx)(t.code,{children:"create"})," call."]}),"\n",(0,o.jsxs)(t.li,{children:[(0,o.jsx)(t.code,{children:"message_retrieval()"})," method: returns a list of strings or a list of message objects. If a list of message objects is returned, they currently must contain the fields of OpenAI's ChatCompletion Message object, since that is expected for function or tool calling in the rest of the codebase at the moment, unless a custom agent is being used."]}),"\n",(0,o.jsxs)(t.li,{children:[(0,o.jsx)(t.code,{children:"cost()"}),"method: returns an integer, and if you don't care about cost tracking you can just return ",(0,o.jsx)(t.code,{children:"0"}),"."]}),"\n",(0,o.jsxs)(t.li,{children:[(0,o.jsx)(t.code,{children:"get_usage()"}),": returns a dictionary, and if you don't care about usage tracking you can just return an empty dictionary ",(0,o.jsx)(t.code,{children:"{}"}),"."]}),"\n"]}),"\n"]}),"\n",(0,o.jsxs)(t.li,{children:["Make sure you have a corresponding entry in the ",(0,o.jsx)(t.code,{children:"OAI_CONFIG_LIST"})," and that that entry has the ",(0,o.jsx)(t.code,{children:'"model_client_cls":"<custom-model-class-name>"'})," field."]}),"\n",(0,o.jsxs)(t.li,{children:["Make sure you have registered the client using the corresponding config entry and your new class ",(0,o.jsx)(t.code,{children:"agent.register_model_client(model_client_cls=<class-of-custom-model>, [other optional args])"})]}),"\n",(0,o.jsxs)(t.li,{children:["Make sure that all of the custom models defined in the ",(0,o.jsx)(t.code,{children:"OAI_CONFIG_LIST"})," have been registered."]}),"\n",(0,o.jsx)(t.li,{children:"Any other troubleshooting might need to be done in the custom code itself."}),"\n"]}),"\n",(0,o.jsx)(t.h2,{id:"conclusion",children:"Conclusion"}),"\n",(0,o.jsx)(t.p,{children:"With the ability to use custom models, AutoGen now offers even more flexibility and power for your AI applications. Whether you've trained your own model or want to use a specific pre-trained model, AutoGen can accommodate your needs. Happy coding!"})]})}function h(e={}){const{wrapper:t}={...(0,s.a)(),...e.components};return t?(0,o.jsx)(t,{...e,children:(0,o.jsx)(d,{...e})}):d(e)}},1151:(e,t,n)=>{n.d(t,{Z:()=>r,a:()=>l});var o=n(7294);const s={},i=o.createContext(s);function l(e){const t=o.useContext(i);return o.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function r(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(s):e.components||s:l(e.components),o.createElement(i.Provider,{value:t},e.children)}}}]);