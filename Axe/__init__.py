from pyrogram import Client

## -----------------------------------------------------------------------------[CLIENT]------------------------------------------------------------------------------------------------------- ##

API_ID = 
API_HASH = 
TOKEN = 
LOG = 


AxeDL = Client(
  "AxeDL",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=TOKEN
)

print("[STARTING BOT] < code : >")
AxeDL.start()

x = AxeDL.get_me()
BOT_NAME = x.first_name
BOT_USERNAME = x.username
BOT_ID = x.id

print("{BOT_NAME} has started!")


## -----------------------------------------------------------------------------[LOGGER]------------------------------------------------------------------------------------------------------- ##