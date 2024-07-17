from datetime import*
from pytube import YouTube , Playlist
from telegram import *
from telegram_bot_config import TOKEN

bot = Bot(token=TOKEN)

def handle_msgs(text:str,user_name:str):
    input_msg = text.lower()
    if input_msg == '/start':
        return f"""
        🎉Bienvenue Mon ami {user_name}🤞, mon nom est Tools Bot et je suis ici pour vous aidez,
        Si vous desiré savoir comment m'utilisé Tapez la commande /help .
        """
    elif input_msg == "guide":
        return f"""
🧾Bienvenue dans le guide {user_name}\n
Mon but est de vous fournir un maximum de\nresources pour vous aidez dans votre apprentissage,\n
Découvrez notre bot Telegram révolutionnaire ! 🚀

Notre bot est conçu pour aider les utilisateurs en leur offrant une gamme de services essentiels :

-Cours de programmation (applications & web) 😏\n
-Hacking éthique 😌\n
-Connexion internet illimitée 🙃\n
-Conseils pour débutants en informatique 💻\n
-Téléchargement de ressources YouTube (vidéos & playlists) \n
-Et bien plus à venir !\n
PS : Et tout cela est a vous gratuitement 🎁,\n Tout se qui vous avez a faire c'est de tapé la commande /access_learn
"""
    elif input_msg == "apropos":
        """ 
Présentation de Tools Bot 🎉
Tools bot est conçu pour aider un grand nombre de personnes en offrant des services variés et utiles.
Vous pouvez apprendre la programmation d’applications et de sites web, explorer le hacking éthique,
et profiter d’une connexion internet illimitée.
De plus, nous fournissons des conseils pratiques pour les débutants 
en atique informet permettons le téléchargement de vidéos et playlists YouTube.
Notre objectif est de rendre l’informatique accessible à tous et de vous 
accompagner dans votre apprentissage.
        """
    else:
        return "Requête non prise en Charge 😞"

def youtube_download_single_video(url:str):
    get_url = YouTube(url)
    def on_download_progress(stream, chunk, bytes_remaining):
        bytes_downloaded = stream.filesize - bytes_remaining
        percent = bytes_downloaded * 100 / stream.filesize
        bot.send_message(
            chat_id=Update.message.chat_id, text=f"Progression : {int(percent)}%"
        )
    get_url.register_on_progress_callback(on_download_progress)
    get_url.streams.get_by_itag(133).download()

# Remplace par le token de ton bot et l'ID du chat
