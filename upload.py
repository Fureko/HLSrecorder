import os
import time
import asyncio
from telethon import TelegramClient

api_id = os.environ['TG_API_ID']
api_hash = os.environ['TG_API_HASH']
bot_token = os.environ['TG_BOT_TOKEN']
chat_id = int(os.environ['TG_CHAT_ID'])

async def upload_file(client, file_path):
    print(f"Envoi de {file_path}...")
    await client.send_file(
        chat_id, 
        file_path, 
        caption=f"Partie terminée : {file_path}",
        supports_streaming=True
    )
    os.remove(file_path) # Supprime pour libérer de l'espace sur GitHub
    print(f"Terminé et supprimé : {file_path}")

async def main():
    client = TelegramClient('bot_session', api_id, api_hash)
    await client.start(bot_token=bot_token)
    
    async with client:
        print("Surveillance des fichiers vidéos lancée...")
        while True:
            # On cherche les fichiers qui ne finissent pas par .part (enregistrement en cours)
            files = [f for f in os.listdir('.') if f.endswith('.mp4') and not f.endswith('.part')]
            for file in files:
                await upload_file(client, file)
            
            await asyncio.sleep(10) # Attendre 10 secondes avant de revérifier

if __name__ == "__main__":
    asyncio.run(main())
