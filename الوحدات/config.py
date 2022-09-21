import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "13171866"))
API_HASH = getenv("API_HASH", "a44683ee14433e825fe61ea45f040f3f")
BOT_TOKEN = getenv("BOT_TOKEN", "5776606218:AAGs_2oxoK7NcWKCVxidbSQZu-irzISa20Y")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AgB2oS3E9TJ-cStM_kNz0rR0MHUQhE_DetJ9y8VQHvsTbtkzQpiXQw5aRjPfztysed9RwCUjBhx-NEzoxfnpyiMvE262acPMASj8KPRrn83zLt1wSGXjkOm4jarroXnKz2HJkvqha2BEqNwl8VTZodRJOpwcF2x2nGJn_csdFGOtweooDKTybQ-qrLUy-zXnGuTZXRwX3Za-mgieVhusOKKMZ5x2EZ0CEaKx4fb1S_-mO1ztGj__CQrGjrS0YwPbpQIg29YmqLIV_qAJlq0OIP4DVaJJWLkPk3o7qpvrCjlIapbths-WGNRHF5QvIp-sdp_wosUKJg4Qbvlp7wlalcXDbNP-cwA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
