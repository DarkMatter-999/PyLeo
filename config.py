import os
import platform
import json

def get_config_file_path():
    current_os = platform.system().lower()

    if current_os == "windows":
        config_dir = os.getenv("APPDATA", os.path.expanduser("~\\AppData\\Roaming"))
        config_file = os.path.join(config_dir, "pyleo", "config.json")
    elif current_os == "linux":
        config_dir = os.path.expanduser("~/.config/pyleo")
        config_file = os.path.join(config_dir, "config.json")
    elif current_os == "darwin":  # macOS
        config_dir = os.path.expanduser("~/.config/pyleo")
        config_file = os.path.join(config_dir, "config.json")
    else:
        raise Exception("Unsupported OS")

    os.makedirs(config_dir, exist_ok=True)

    return config_file

def load_config():
    config_file = get_config_file_path()

    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        with open(config_file, 'w') as file:
            default_config = {
                "SHORT_BREAK":15,
                "SHORT_BREAK_DURATION": 0.5,
                "LONG_BREAK": 50,
                "LONG_BREAK_DURATION": 5,
                "COLOR": "34,14,59,200",
            }

            json.dump(default_config, file)
            print(f"Config file not found at '{config_file}' creating a new one.")

            return default_config

        # raise Exception(f"Config file '{config_file}' not found.")
    except json.JSONDecodeError:
        raise Exception(f"Error parsing the config file '{config_file}'.")

class Config:
    config = None

    def __init__(self):
        Config.config = load_config()

    def get(key):
        return Config.config[key]

SHORT_BREAK = 15
SHORT_BREAK_DURATION = 0.5

LONG_BREAK = 50
LONG_BREAK_DURATION = 5
