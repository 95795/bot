import requests
import random
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from requests_html import HTMLSession

def get_news():
    url='https://api.ixiaowai.cn/tgrj/index.php'
    res = requests.get(url)
    b = res.text
    c = b.replace('*','')
    print('情感语录1:',c)
    return c
exlpain = on_command("舔狗" ,priority=2,block=True)
@exlpain.handle()
async def slove(bot: Bot, event: Event):
    if int(event.get_user_id())!= event.self_id:
        try:
        
            
            str1 = get_news()
            await bot.send(
                event=event,
                message=str1,
                at_sender=True
            )
        except Exception as e:
            await exlpain.send("舔狗插件出现故障")

