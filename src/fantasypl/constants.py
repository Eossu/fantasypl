#
#
#
from pydantic import BaseSettings


class Urls(BaseSettings):
    """Base URLs this SDK needs"""

    BASE_URL: str = "https://fantasy.premierleague.com/api/"
    ME: str = f"{BASE_URL}me/"
    STATIC: str = f"{BASE_URL}bootstrap-static/"
    MY_TEAM: str = f"{BASE_URL}my-team/{{}}"
    ENTRY: str = f"{BASE_URL}entry/{{}}/"
    CUP: str = f"{ENTRY}{{}}/"
    PLAYER_SUMMARY: str = f"{BASE_URL}element-summary/{{}}"
