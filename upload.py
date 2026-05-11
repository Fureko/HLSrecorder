import os
import asyncio
from telethon import TelegramClient
# Récupération des secrets GitHub
api_id = os.environ['TG_API_ID']
api_hash = os.environ['TG_API_HASH']
bot_token = os.environ['TG_BOT_TOKEN']
chat_id = int(os.environ['TG_CHAT_ID'])
file_path = "video.mp4"
async def main():
# Utilise le bot token pour s'authentifier via Telethon
async with TelegramClient('bot_session', api_id,
api_hash).start(bot_token=bot_token) as client:
print(f"Début de l'envoi de {file_path}...")
await client.send_file(
1.
2.
3.

chat_id,
file_path,
caption="Enregistrement terminé",
supports_streaming=True # Permet de lire la vidéo avant la fin
du téléchargement
)
print("Envoi réussi !")
if __name__ == "__main__":
asyncio.run(main())
