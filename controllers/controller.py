# ./controllers/controller.py
from typing import Any
from datetime import datetime
from random import randint # for development testing purpose only
from jinja2 import Environment, FileSystemLoader

view: Environment = Environment(loader= FileSystemLoader("views"))

class Controller:
    def __init__(self) -> None:
        # Application's constant parameters
        self.webpage: str = "w86md" 
        self.version: str = "1.0.0"
        self.curYear: int = int(datetime.now().strftime("%Y"))
        self.cuMonth: int = int(datetime.now().strftime("%m"))
        self.strYear: int = 2027
        self.stMonth: int = 7
        self.devYear: int = 2025
        
        # Application's variable parameters
        self.display: str = ""
        self.section: str = ""
        self.keyword: str = ""
        self.scripts: str = ""
        self.headers: str = ""
        self.tabname: str = ""
        self.pgchart: str = ""
        self.pgsdata: list[dict[str, Any]]
        self.pgdatum: dict[str, Any]
        
        # user Authentication &  Authority parameters
        self.islogin: bool = bool(randint(0, 1))
        self.userLvl: int = 0

    @property
    def context(self) -> dict[str, Any]:
        return vars(self)

    @property
    def template(self) -> str:
        return view.get_template(f"{self.display}.html").render(ctx = self.context)