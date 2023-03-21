from nonebot.adapters.onebot.v11 import Message, MessageSegment

from pathlib import Path
from typing import Any
from enum import Enum


class Meals(Enum):
    BREAKFAST = ["breakfast", "早餐", "早饭"]
    LUNCH = ["lunch", "午餐", "午饭", "中餐"]
    SNACK = ["snack", "摸鱼", "下午茶", "饮茶"]
    DINNER = ["dinner", "晚餐", "晚饭"]
    MIDNIGHT = ["midnight", "夜宵", "宵夜"]
try:
    import ujson as json
except ModuleNotFoundError:
    import json


class FoodLoc(Enum):
    IN_BASIC = "In basic"
    IN_GROUP = "In group"
    NOT_EXISTS = "Not exists"


class SearchLoc(Enum):
    IN_BASIC = "In basic"
    IN_GROUP = "In group"
    IN_GLOBAL = "In global"


def save_json(_file: Path, _data: Any) -> None:
    with open(_file, 'w', encoding='utf-8') as f:
        json.dump(_data, f, ensure_ascii=False, indent=4)


def load_json(_file: Path) -> Any:
    with open(_file, 'r', encoding='utf-8') as f:
        return json.load(f)
