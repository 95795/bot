from tkinter import N
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot,Event

help = on_command("help",priority=2)
@help.handle()
async def help_(bot:Bot,event:Event,state:T_State):
    await bot.send(
        event=event,
        message=("@机器人/添加op语录 顾名思义\n\
        @机器人 /echo+一句话   复读那一句话\n\
        翻看答案 + 问题  获取某一问题的答案\n\
        /一言 /鸡汤  发鸡汤\n\
        /每日一图 正常图片\n\
        @机器人😎+😁  将两个emoji合成为一张图片\n\
        @机器人/舔狗  让机器人成为舔狗\n[开启/关闭小助手] 开启/关闭吃饭小助手\n[添加/删除问候 时段 问候语] 添加/删除吃饭小助手问候语\n")
    )