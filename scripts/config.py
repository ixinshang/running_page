import os
import yaml

GET_DIR = "activities"
OUTPUT_DIR = "activities"
GPX_FOLDER = os.path.join(os.getcwd(), "GPX_OUT")
SQL_FILE = "scripts/data.db"
JSON_FILE = "src/static/activities.json"

# TODO: Move into nike_sync
BASE_URL = "https://api.nike.com/sport/v3/me"
TOKEN_REFRESH_URL = "https://unite.nike.com/tokenRefresh"
NIKE_CLIENT_ID = "HlHa2Cje3ctlaOqnxvgZXNaAs7T9nAuH"

TYPE_DICT = {
    "running": "Run",
    "RUN": "Run",
    "Run": "Run",

    "cycling": "Ride",
    "CYCLING": "Ride",
    "Ride": "Ride",

    "indoor_cycling": "Indoor Ride",

    "walking": "Hike",
    "Walk": "Hike",
    "Hike": "Hike",

    "Swim": "Swim",

    "rowing": "Rowing",
}

MAPPING_TYPE = ["Hike", "Ride", "Rowing", "Run", "Swim"]


try:
    with open("config.yaml") as f:
        _config = yaml.safe_load(f)
except:
    _config = {}


def config(*keys):
    def safeget(dct, *keys):
        for key in keys:
            try:
                dct = dct[key]
            except KeyError:
                return None
        return dct

    return safeget(_config, *keys)
