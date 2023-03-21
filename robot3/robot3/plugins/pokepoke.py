from nonebot import on_notice
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11 import Event, PokeNotifyEvent
import random
from nonebot.adapters.onebot.v11 import MessageSegment

a = ['那...那里...那里不能戳...绝对...','嘤嘤嘤,好疼','如果是欧尼酱的话，可以的哦~',
   '啊...恩...那里不行','嗯嗯...啊啊啊...不要...啊啊啊...去了','不...不可以...那里不行']


pre = 0
poke=on_notice()
@poke.handle()
async def _(bot:Bot,event:Event):
    try:
        if isinstance(event,PokeNotifyEvent):
            if event.is_tome() and event.user_id !=event.self_id:
                l = len(a)
                k = random.randint(0,l-1)
                while pre == k:
                    k = random.randint(0,l-1)
                last = k
                await bot.send(
                    event=event,
                    message=a[k],
                    at_sender=True
                )
    except Exception as e:
        await poke.send("戳一戳插件出现故障")