import httpx

from .config import Config
from nonebot import get_plugin_config
from nonebot.rule import to_me
from nonebot.params import EventMessage
from nonebot.plugin import on_message,PluginMetadata
from nonebot.adapters import Message
# 本地存储
from nonebot import require
import nonebot_plugin_localstore as store
require("nonebot_plugin_localstore")


## plugin meta data
__plugin_meta__= PluginMetadata(
    name= "ai_topia",
    description= "接入ai乌托邦pro对话",
    usage= "暂无",
    type= "application",
    homepage= "https://github.com/KanzakiD/nonebot-plugin-ai-topia",
)


## config
plugin_config= get_plugin_config(Config)

api_key= plugin_config.ai_topia_api_key
api_secret= plugin_config.ai_topia_api_secret
role_id= plugin_config.ai_topia_role_id


## 响应
mes= on_message(rule=to_me(),priority=plugin_config.ai_topia_priority)

# 临时token，后期挪到config
temp_token= "eyJhbGciOiJIUzUxMiJ9.eyJhdXRoX3R5cGUiOiIyIiwidXNlcl9pZCI6Njg1NjgsInVzZXJfa2V5IjoiZGM4Mjc3MGNmN2M1NGI2Y2IwMDI4OTk1NGQzNzY0MmYiLCJ1c2VybmFtZSI6IjE4Njk3NDQzOTAwIn0.btmchfObGh9rDlYP6QsbIiTTg8BUDOykSeLAZjfeyDnvfIBefhJhqK3iBfwduC-AAZWZpq0ulhePz3VDgRFA_g"
headers= {'Content-Type': 'application/json; charset=utf-8','Authorization': f'Bearer {temp_token}'}
sc_url= 'https://pro.ai-topia.com/apis/chat/sendChat'

@mes.handle()
async def handle_function(args: Message = EventMessage()):
    # 检测非空消息
    if user_content := args.extract_plain_text():
        # body
        body= {'appUserId': '2', 'content': user_content, "roleId": role_id}

        async with httpx.AsyncClient() as client:
            res= await client.post(
                sc_url,
                headers= headers,
                json= body
            )
            # 检查是否请求成功
            if res.status_code == 200:
                data= res.json()
                # 检查json合法并处理
                if "content" in data["data"]:
                    await mes.finish(data["data"]["content"])
                else:
                    await mes.send("数据结构不符合预期，请重试喵")
                    await mes.finish(f"数据为：{data}")
            else:
                await mes.finish("请求失败，请重试喵")