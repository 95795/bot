import ast
import nonebot
import requests  # 需要用到GET的方式获取图片，否则一直是一张图片
from nonebot.rule import *
from nonebot import on_command
from nonebot import *
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event, GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message
import sqlite3
import random
import urllib3
import json
from datetime import date

setu = on_keyword({'色图', '涩涩','涩图'}, priority=5)  # 饥渴的涩涩人是不会先打出命令符的，那么只需要对关键词记录就好了
url = (
       "https://api.r10086.com/img-api.php?type=动漫综合6",
       "https://api.vvhan.com/api/acgimg",
    #    "https://api.lolicon.app/setu/v2"
       "https://iw233.cn/API/Random.php",
    #    "https://acg-img.dustella.net/"
       "https://dev.iw233.cn/api.php?sort=random",
       "http://ap1.iw233.cn/api.php?sort=random"
       )  # 一些图片api，举了几个自己用的


@setu.handle()
async def setu_handle(bot: Bot, event: Event):
    with open(r'C:\Users\Administrator\Desktop\robot3\robot3\plugins\群名单.txt', encoding='utf-8') as file:  # 提取白名单群文件中的群号
        white_block = []
        for line in file:
            line = line.strip()
            line = re.split("[ |#]", line)  # 可能会有'#'注释或者空格分割
            white_block.append(line[0])  # 新建一个表给它扔进去
    try:
        whatever, group_id, user_id = event.get_session_id().split('_')  # 获取当前群聊id，发起人id，返回的格式为group_groupid_userid
    except:  # 如果上面报错了，意味着发起的是私聊，返回格式为userid
        group_id = None
        user_id = event.get_session_id()
    if group_id in white_block or group_id == None:  # 判断是否为群聊白名单或者是私聊（也可以设置白名单不过没必要）
        randomrul = random.randint(0, 4)  # 可能一个图片网站会不小心重复，那么多个就不会重复了吧！ 
        reciece_message = str(event.get_message())
        if len(reciece_message) > 4:
            '''
            有时候句中也可能包含了'ldst'，比如'这个某某某天天喜欢ldst'。
            由于N2的on_keyword()针对的是句中关键词，为了避免这种情况下也会不合时宜地发送一张图片
            我们可以手动判断输入的数据长度，或者判断是否和给定的关键词相同即可
            实际上这部分内容可以使用N2自带的rule来提前判断，十分强大
            具体接着参考大佬的博客吧
            "http://blog.well404.top/2022/05/09/nonebot/%E3%80%90NoneBot2%E3%80%91%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E5%9F%BA%E7%A1%80%E6%8F%92%E4%BB%B6%E7%BC%96%E5%86%99%E6%8C%87%E5%8D%97%E7%AC%AC%E5%9B%9B%E8%8A%82%E2%80%94%E2%80%94%E2%80%94%E4%BA%BA%E5%AE%B6%E6%89%8D%E6%87%92%E5%BE%97%E7%90%86%E4%BD%A0%E5%91%A2/"
            '''
            await setu.finish()  # 出现这种情况就直接结束
        await setu.send(Message(f"一天到晚只想着涩涩是吧打你哦ヽ(#`Д´)ﾉ"))  # 自行发挥，还可以建个表拉取下每个qq涩了多少次来返回不同的“谴责”
        result = requests.get(url[randomrul])  # 使用GET方法获取图片，返回的是JSON格式，发送时调用url即可
        await setu.finish(Message(f"[CQ:image,file={result.url},id=400000]"))  # 由于并未涉及群聊私聊的区分，直接发送即可