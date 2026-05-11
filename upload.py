import os
import asyncio
from telethon import TelegramClient

# Récupération des secrets depuis GitHub
api_id = os.environ['TG_API_ID']
api_hash = os.environ['TG_API_HASH']
bot_token = os.environ['TG_BOT_TOKEN']
chat_id = int(os.environ['TG_CHAT_ID'])

async def main():
    # 1. On initialise le client
    client = TelegramClient('bot_session', api_id, api_hash)
    
    # 2. On démarre explicitement le client avec le token (CORRECTION ICI)
    await client.start(bot_token=bot_token)
    
    # 3. On utilise "async with" uniquement pour la session ouverte
    async with client:
        print("Connexion réussie. Envoi de la vidéo vers Telegram...")
        await client.send_file(
            chat_id, 
            "video.mp4", 
            caption="Enregistrement terminé ! ✅",
            supports_streaming=True
        )
        print("Fichier envoyé avec succès !")

if __name__ == "__main__":
    asyncio.run(main())
