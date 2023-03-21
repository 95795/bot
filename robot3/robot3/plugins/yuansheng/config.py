from pathlib import Path
from pydantic import BaseModel, Extra
from typing import List, Dict, Set, Union, Any, Optional
from nonebot import get_driver, logger
from .utils import save_json
import httpx
try:
    import ujson as json
except ModuleNotFoundError:
    import json

class PluginConfig(BaseModel, extra=Extra.ignore):
    what2eat_path: Path = Path(__file__).parent / "chushi"
    use_preset_menu: bool = False
    use_preset_greetings: bool = False
    eating_limit: int = 3
    greeting_groups_id: Set[str] = set()
    superusers: Set[str] = set()


driver = get_driver()
what2eat_config: PluginConfig = PluginConfig.parse_obj(driver.config.dict())


@driver.on_startup
async def what2eat_check() -> None:
    if not what2eat_config.what2eat_path.exists():
        what2eat_config.what2eat_path.mkdir(parents=True, exist_ok=True)
    
    if not (what2eat_config.what2eat_path / "img").exists():
        (what2eat_config.what2eat_path / "img").mkdir(parents=True, exist_ok=True)
    
    '''
        If eating.json doesn't exist or eating.json exists but f.get["basic_food"] doesn't exist and USE_PRESET_MENU is True, download
        If USE_PRESET_MENU is False, break
    '''
    eating_json: Path = what2eat_config.what2eat_path / "eating.json"
    if what2eat_config.use_preset_menu:
            # check the keys
            with eating_json.open("r", encoding="utf-8") as f:
                _f: Dict[str, Union[List[str], Dict[str, Union[Dict[str, List[int]], List[str]]]]] = json.load(f)
                if not _f.get("basic_food", False):
                    _f.update({"basic_food": []})
                
                if not _f.get("group_food", False):
                    _f.update({"group_food": {}})
                    
                if not _f.get("count", False):
                    _f.update({"count": {}})
                
            save_json(eating_json, _f)
            
            
            
__all__ = [
    what2eat_config
]