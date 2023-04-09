import tomli
from .content import *

# Read config file
with open("config.toml", "rb") as config_file:
    config = tomli.load(config_file)

tm_config = config["TeachableMachine"]

# Read default value from the config
CONFIG_MODEL_FILE = tm_config["path"] + '/' + tm_config["model_file"]
CONFIG_LABEL_FILE =  tm_config["path"] + '/' + tm_config["label_file"]
CONFIG_SHOW_CAM_FEED = True if tm_config["show_cam_feed"] == "True" else False

CURRENT_MODEL, CURRENT_LABEL = \
    load_model_and_label(CONFIG_MODEL_FILE, CONFIG_LABEL_FILE)
