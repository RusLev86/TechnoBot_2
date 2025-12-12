import telebot

# Вставьте свой токен
TOKEN = 'f9LHodD0cOKL_H-R_qDhhjRvFlEohd8CFd37GA1_9Z_0e1oY5DT1sbd5IMUFPTO-LQ4rzxP50anS1eaeZBiG'
bot = telebot.TeleBot(TOKEN)

# Удаляем вебхук
bot.remove_webhook()

# Запускаем опрос
bot.polling(none_stop=True)
