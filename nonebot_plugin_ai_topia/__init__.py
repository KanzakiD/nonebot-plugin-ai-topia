import nonebot
from nonebot.plugin import on_command,on_keyword,on_message
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me

__plugin_meta__ = PluginMetadata(
    name="ai_topia",
    description="接入ai乌托邦pro对话",
    usage="暂无",
    type="application",
    homepage="https://github.com/KanzakiD/nonebot-plugin-ai-topia",
)

bot= on_message(rule=to_me(),priority=20)



@bot.handle()
async def handle_function():

    await bot.finish(str("success"))