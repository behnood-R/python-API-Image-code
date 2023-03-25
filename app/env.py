import os
from dotenv import load_dotenv
load_dotenv()

def get_env_variable(var_name, default_value=None):
    try:
        value = os.environ[var_name]
        if value.lower() in ['true', 'yes', '1']:
            return True
        elif value.lower() in ['false', 'no', '0']:
            return False
        return value
    except KeyError:
        return default_value


APP_NAME = get_env_variable("APP_NAME", "app")
APP_VERSION = get_env_variable("APP_VERSION", "0.0.1")
PRODUCTION = get_env_variable("PRODUCTION", True)
DEBUG = get_env_variable("DEBUG", False)
PRIVATE_PORT = get_env_variable("PRIVATE_PORT", 8888)
PUBLIC_PORT = get_env_variable("PUBLIC_PORT", 8000)
