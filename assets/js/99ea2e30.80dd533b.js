"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[4344],{26568:(e,s,n)=>{n.r(s),n.d(s,{assets:()=>c,contentTitle:()=>i,default:()=>m,frontMatter:()=>a,metadata:()=>o,toc:()=>l});var t=n(85893),r=n(11151);const a={sidebar_label:"transform_messages",title:"agentchat.contrib.capabilities.transform_messages"},i=void 0,o={id:"reference/agentchat/contrib/capabilities/transform_messages",title:"agentchat.contrib.capabilities.transform_messages",description:"TransformMessages",source:"@site/docs/reference/agentchat/contrib/capabilities/transform_messages.md",sourceDirName:"reference/agentchat/contrib/capabilities",slug:"/reference/agentchat/contrib/capabilities/transform_messages",permalink:"/autogen/docs/reference/agentchat/contrib/capabilities/transform_messages",draft:!1,unlisted:!1,editUrl:"https://github.com/microsoft/autogen/edit/main/website/docs/reference/agentchat/contrib/capabilities/transform_messages.md",tags:[],version:"current",frontMatter:{sidebar_label:"transform_messages",title:"agentchat.contrib.capabilities.transform_messages"},sidebar:"referenceSideBar",previous:{title:"text_compressors",permalink:"/autogen/docs/reference/agentchat/contrib/capabilities/text_compressors"},next:{title:"transforms",permalink:"/autogen/docs/reference/agentchat/contrib/capabilities/transforms"}},c={},l=[{value:"TransformMessages",id:"transformmessages",level:2},{value:"__init__",id:"__init__",level:3},{value:"add_to_agent",id:"add_to_agent",level:3}];function d(e){const s={code:"code",h2:"h2",h3:"h3",li:"li",ol:"ol",p:"p",pre:"pre",strong:"strong",ul:"ul",...(0,r.a)(),...e.components};return(0,t.jsxs)(t.Fragment,{children:[(0,t.jsx)(s.h2,{id:"transformmessages",children:"TransformMessages"}),"\n",(0,t.jsx)(s.pre,{children:(0,t.jsx)(s.code,{className:"language-python",children:"class TransformMessages()\n"})}),"\n",(0,t.jsx)(s.p,{children:"Agent capability for transforming messages before reply generation."}),"\n",(0,t.jsx)(s.p,{children:"This capability allows you to apply a series of message transformations to\na ConversableAgent's incoming messages before they are processed for response\ngeneration. This is useful for tasks such as:"}),"\n",(0,t.jsxs)(s.ul,{children:["\n",(0,t.jsx)(s.li,{children:"Limiting the number of messages considered for context."}),"\n",(0,t.jsx)(s.li,{children:"Truncating messages to meet token limits."}),"\n",(0,t.jsx)(s.li,{children:"Filtering sensitive information."}),"\n",(0,t.jsx)(s.li,{children:"Customizing message formatting."}),"\n"]}),"\n",(0,t.jsxs)(s.p,{children:["To use ",(0,t.jsx)(s.code,{children:"TransformMessages"}),":"]}),"\n",(0,t.jsxs)(s.ol,{children:["\n",(0,t.jsxs)(s.li,{children:["Create message transformations (e.g., ",(0,t.jsx)(s.code,{children:"MessageHistoryLimiter"}),", ",(0,t.jsx)(s.code,{children:"MessageTokenLimiter"}),")."]}),"\n",(0,t.jsxs)(s.li,{children:["Instantiate ",(0,t.jsx)(s.code,{children:"TransformMessages"})," with a list of these transformations."]}),"\n",(0,t.jsxs)(s.li,{children:["Add the ",(0,t.jsx)(s.code,{children:"TransformMessages"})," instance to your ",(0,t.jsx)(s.code,{children:"ConversableAgent"})," using ",(0,t.jsx)(s.code,{children:"add_to_agent"}),"."]}),"\n"]}),"\n",(0,t.jsx)(s.p,{children:"NOTE: Order of message transformations is important. You could get different results based on\nthe order of transformations."}),"\n",(0,t.jsxs)(s.p,{children:[(0,t.jsx)(s.strong,{children:"Example"}),":"]}),"\n",(0,t.jsx)(s.pre,{children:(0,t.jsx)(s.code,{children:"```python\nfrom agentchat import ConversableAgent\nfrom agentchat.contrib.capabilities import TransformMessages, MessageHistoryLimiter, MessageTokenLimiter\n\nmax_messages = MessageHistoryLimiter(max_messages=2)\ntruncate_messages = MessageTokenLimiter(max_tokens=500)\ntransform_messages = TransformMessages(transforms=[max_messages, truncate_messages])\n\nagent = ConversableAgent(...)\ntransform_messages.add_to_agent(agent)\n```\n"})}),"\n",(0,t.jsx)(s.h3,{id:"__init__",children:"__init__"}),"\n",(0,t.jsx)(s.pre,{children:(0,t.jsx)(s.code,{className:"language-python",children:"def __init__(*, transforms: List[MessageTransform] = [], verbose: bool = True)\n"})}),"\n",(0,t.jsxs)(s.p,{children:[(0,t.jsx)(s.strong,{children:"Arguments"}),":"]}),"\n",(0,t.jsxs)(s.ul,{children:["\n",(0,t.jsxs)(s.li,{children:[(0,t.jsx)(s.code,{children:"transforms"})," - A list of message transformations to apply."]}),"\n",(0,t.jsxs)(s.li,{children:[(0,t.jsx)(s.code,{children:"verbose"})," - Whether to print logs of each transformation or not."]}),"\n"]}),"\n",(0,t.jsx)(s.h3,{id:"add_to_agent",children:"add_to_agent"}),"\n",(0,t.jsx)(s.pre,{children:(0,t.jsx)(s.code,{className:"language-python",children:"def add_to_agent(agent: ConversableAgent)\n"})}),"\n",(0,t.jsx)(s.p,{children:"Adds the message transformations capability to the specified ConversableAgent."}),"\n",(0,t.jsx)(s.p,{children:"This function performs the following modifications to the agent:"}),"\n",(0,t.jsxs)(s.ol,{children:["\n",(0,t.jsx)(s.li,{children:"Registers a hook that automatically transforms all messages before they are processed for\nresponse generation."}),"\n"]})]})}function m(e={}){const{wrapper:s}={...(0,r.a)(),...e.components};return s?(0,t.jsx)(s,{...e,children:(0,t.jsx)(d,{...e})}):d(e)}},11151:(e,s,n)=>{n.d(s,{Z:()=>o,a:()=>i});var t=n(67294);const r={},a=t.createContext(r);function i(e){const s=t.useContext(a);return t.useMemo((function(){return"function"==typeof e?e(s):{...s,...e}}),[s,e])}function o(e){let s;return s=e.disableParentContext?"function"==typeof e.components?e.components(r):e.components||r:i(e.components),t.createElement(a.Provider,{value:s},e.children)}}}]);