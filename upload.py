import os
import asyncio
from telethon import TelegramClient

# Récupération des secrets
api_id = os.environ['TG_API_ID']
api_hash = os.environ['TG_API_HASH']
bot_token = os.environ['TG_BOT_TOKEN']
chat_id = int(os.environ['TG_CHAT_ID'])

async def main():
    # On crée le client
    client = TelegramClient('bot_session', api_id, api_hash)
    
    # On se connecte et on s'identifie
    await client.start(bot_token=bot_token)
    
    async with client:
        print("Connexion réussie. Envoi en cours vers Telegram...")
        await client.send_file(
            chat_id, 
            "video.mp4", 
            caption="Enregistrement terminé !",
            supports_streaming=True
        )
        print("Fichier envoyé avec succès.")

if __name__ == "__main__":
    asyncio.run(main())
