# ./main.py
from fasthtml import common as FH # type: ignore
import controllers as Pages

# Apps parameters
DEBUG: bool = True # False on production
LIVE: bool = True # False on production
HOST: str = "0.0.0.0" # Change on production 
PORT: int = 5001  # Change on production

app, rt = FH.fast_app(pico=False, htmx=False, debug=DEBUG, live=LIVE, static_path="dist")

if __name__ == "__main__":
    FH.serve(host=HOST, port=PORT)