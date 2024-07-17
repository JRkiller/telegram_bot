from telegram.ext import  *
import answer_bot as answer
from telegram import *

from dotenv import load_dotenv

load_dotenv()

print("Bot started ...")

TOKEN = ""

async def help_cmd(update: Update, context: CallbackContext):
    keybords = [
        [KeyboardButton("Apropos"), KeyboardButton("Guide")],#erreur de fonctionnement du bouton apropos .
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard=keybords,resize_keyboard=True,one_time_keyboard=True
    )
    await update.message.reply_text("📌Avez vous Bésoin d'aide ?",reply_markup=reply_markup)

async def start_cmd(update: Update, context: CallbackContext):
    await update.message.reply_text(answer.handle_msgs(update.message.text,update.message.from_user.first_name))

async def handle_msg(update: Update, context: CallbackContext):
    await update.message.reply_text(answer.handle_msgs(update.message.text,update.message.from_user.first_name))

async def access_learn_cmd(update:Update , context: CallbackContext):
    keyboards = [
        [
            KeyboardButton("/Cours_de_Programmation"),
            KeyboardButton("/Hacking_Éthique"),
        ],
        [
            KeyboardButton("/Téléchargement_YouTube"),
            KeyboardButton("/Internet_Illimité"),
        ],
        [KeyboardButton("/Conseils_Informatique_Débutants")],
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard=keyboards,
        one_time_keyboard=True,
        resize_keyboard=True,
        input_field_placeholder=f"fait un choix {update.message.from_user.first_name}",
    )
    await update.message.reply_text(
        f"veuillez faire votre choix {update.message.from_user.first_name}",
        reply_markup=reply_markup,
    )
async def Téléchargement_YouTube(update:Update, context:CallbackContext):
    await update.message.reply_text(
        answer.youtube_download_single_video(update.message.text),
        answer.youtube_download_single_video(update.message.text),
    )
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("help",help_cmd))
app.add_handler(CommandHandler("start",start_cmd))
app.add_handler(CommandHandler("access_learn", access_learn_cmd))
app.add_handler(MessageHandler(filters.TEXT,handle_msg))

app.run_polling(poll_interval=5)
