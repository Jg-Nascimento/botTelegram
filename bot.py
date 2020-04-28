
from telegram.ext import Updater, CommandHandler

def welcome(update, content):
    message = 'Olá usuário, ' + update.message.from_user.first_name + '!'
    print(message)
    content.bot.send_message(chat_id = update.effective_chat.id, text = message)

def main():
    token = '#1194714850:AAGsCicfXKJrK4Z_QICDYxF6_G9jNYalMu8'
    updater = Updater(token = token, use_context = True)
    updater.start_polling()
    print('Updater' + str(updater))
    updater.dispatcher.add_handler(CommandHandler('start', welcome))
    updater.idle()

if __name__ == "__main__":
    main()

