# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20172532"))
API_HASH = getenv("API_HASH", "6814101098c5b74fbd07ee76b14129e3")
BOT_TOKEN = getenv("BOT_TOKEN", "6968487291:AAF78gZ50ZIHGwVmst8t95f7aXFioA7rw_0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5142272541").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://chotuyt:chotuyt@cluster0.eo5tm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002324408535")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002447050882"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "50"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "200"))
