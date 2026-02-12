import telebot

# توکن رباتت را اینجا بگذار
bot = telebot.TeleBot('8344100450:AAFiooMCbFEl6lXvfyaKrsdjERBr2PCcSFk')

# آیدی‌های رابط که قبلاً دادی
INTERFACE_1 = 8457219431
INTERFACE_2 = 6936902567

# شمارنده برای مدیریت توزیع 4 به 2
msg_counter = 0

@bot.message_handler(func=lambda message: True)
def distribute_text(message)
    global msg_counter
    
    # فقط متن را بدون هیچ تغییر یا واترمارکی ارسال می‌کند
    text_to_send = message.text 
    
    if msg_counter  4
        # ارسال به رابط 1
        bot.send_message(INTERFACE_1, text_to_send)
    else
        # ارسال به رابط 2
        bot.send_message(INTERFACE_2, text_to_send)
    
    msg_counter += 1
    
    # بعد از 6 پیام (4+2)، شمارنده صفر می‌شود
    if msg_counter = 6
        msg_counter = 0


bot.infinity_polling()

