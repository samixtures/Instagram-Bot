from instabot import Bot
bot = Bot()
f = open("C:\\Users\Bajwa\\Downloads\\instabot_credentials.txt")
usern = f.readline()
passw = f.readline()
bot.login(username=usern, password=passw)
bot.login(ask_for_code=True)
bot.upload_photo("yoda.jpg", caption="Cute biscuit eating yoda")