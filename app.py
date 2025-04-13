replay_text("مرحبًا! أنا بوت لرسائل التنبيه على العملات الحلال.")

# دالة إعداد البوت
def main():
    # توكن البوت (استبدله بالتوكن الخاص بك)
    updater = Updater("7948997743:AAH77y46rqNrJEJE1uk_sZJlk1f95fV7SKk", use_context=True)
    dp = updater.dispatcher
    
    # إضافة معالجات الأوامر
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("add_coin", add_coin))
    dp.add_handler(CommandHandler("remove_coin", remove_coin))
    
    # بدء البوت
    updater.start_polling()
    updater.idle()

# تشغيل Flask في وضع متوازي مع البوت
if name == '__main__':
    from threading import Thread
    t = Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000})
    t.start()
    main()
