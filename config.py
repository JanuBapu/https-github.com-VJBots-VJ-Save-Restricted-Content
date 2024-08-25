import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25436183"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "03fbfb7036edd6f6786e422795eb861b")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://janubapu:5uadFAdA1WQcHdtV3@cluster0.ld2ya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
