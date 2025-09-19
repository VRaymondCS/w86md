# ./controllers/home.py
from controllers import Controller, Any, app

class Home(Controller):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    @app.get("/")
    def index():
        page = Home()
        page.section = "home"
        page.keyword = "Homepage"
        page.tabname = "Homepage"
        page.headers = f"Welcome to homepage {page.webpage}"
        page.webpage = "PATH"
        page.display = "pages/home/index"
        
        return page.template