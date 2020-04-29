#1194714850:AAGsCicfXKJrK4Z_QICDYxF6_G9jNYalMu8
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


STATE1 = 1
STATE2 = 2

def welcome(update, content):
    message = 'Olá usuário, ' + update.message.from_user.first_name + '!'
    print(message)
    content.bot.send_message(chat_id = update.effective_chat.id, text = message)

#método para , e serão chamados no método inputFeedback
def feedback(update, context):
    message ='Por favor, digite um feedback para o nosso tutorial:\n'
            #1 - OPÇÃO1
            #2 - OPÇÃO2 '''
            
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
    return STATE1

def inputFeedback(update, context):
    feedback = lower(update.message.text)
    print(feedback)
    if len(feedback) < 10:
        #resposta do bot referente ao feedback
        message = """Seu feedback foi muito curtinho... 
                        \nInforma mais pra gente, por favor?"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    else:
        message = "Muito obrigada pelo seu feedback!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def inputFeedback2(update, context):
    feedback = update.message.text
    message = "Muito obrigada pelo seu feedback!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def cancel(update, context):
    return ConversationHandler.END

def main():
    token = '1194714850:AAGsCicfXKJrK4Z_QICDYxF6_G9jNYalMu8'
    updater = Updater(token = token, use_context = True)
    
    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        
        #conversa
        entry_points=[CommandHandler('feedback', feedback)],


        states={
            STATE1: [MessageHandler(Filters.text, inputFeedback)],
            STATE2: [MessageHandler(Filters.text, inputFeedback2)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)


    updater.start_polling()
    print('Updater' + str(updater))
    updater.idle()



if __name__ == "__main__":
    main()
    
