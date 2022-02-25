
from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
import os
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import time
from time import sleep
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
app = Client('dedinside-session', api_id=1016382, api_hash='c27834e5683d50a9bacf835a95ec4763')

app.start()

app.stop()
print('''
      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      ┃       Made by Criblle                       ┃
      ┃  Telegram: muhammadamin ┃
      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


''')
print("После ввода задержки напишите в любой телеграм чат команду /help для просмотра команд!\n --Команды-- \n.dead 5 \n.night 5 \n.ghoul \n.love 5 \n.jopa 5")
print("\n МЫ НЕ НЕСЕМ ОТВЕТСВЕННОСТИ ЗА ВАШИ ДЕЙСТВИЯ!")
print()
cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool == 0:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool > 10:
    print("Слишком медленно!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool < 5:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость(Норма 8):  "))


@app.on_message(filters.command("dead", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded.split("\n")
    e = True
    etime = int(msg.text.split('.dead ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'❤️{i} ❤️')
                sleep(time/cool)
                msg.edit(f'🧡 {i} 🧡')
                sleep(time/cool)
                msg.edit(f'💛 {i} 💛')
                sleep(time/cool)
                msg.edit(f'💚 {i} 💚')
                sleep(time/cool)
                msg.edit(f'💙 {i} 💙')
                sleep(time/cool)
                msg.edit(f'💜 {i} 💜')
                sleep(time/cool)
                msg.edit(f'🖤 {i} 🖤')
                sleep(time/cool)
                msg.edit(f'🤍 {i} 🤍')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐ 😩🥲</b>')

textded = '''
<b> Я дед инсайд </b>
<b> Мне 9 лет </b>
<b> И я хочу в Психокидс </b>
'''

textded1 = '''
<b>спокойной ночи зайка 💚</b>
<b>спокойной ночи солнышко 💛</b>
<b>спокойной ночи котёнок ❤</b>️
<b>спокойной ночи цветочек 💙</b>
<b>спокойной ночи ангелочек 💜</b>
<b>спокойной ночи принцесса 💓</b>
<b>спокойной ночи красотка 💕</b>
<b>спокойной ночи милашка 💖</b>
<b>спокойной ночи симпатяжка 💗</b>
<b>спокойной ночи бусинка 💘</b>
<b>❤я❤</b>️
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
'''

@app.on_message(filters.command("night", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded1.split("\n")
    e = True
    etime = int(msg.text.split('.night ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐  </b>')

@app.on_message(filters.command("ghoul", prefixes=".") & filters.me)
def valentine(app, message):
    app.send_message(message.chat.id,f'<b>Ты гуль?</b>')
    sleep(2)
    app.send_message(message.chat.id,f'<i>Я тоже</i>')
    sleep(5)
    i = 1000
    while i > 0:
        try:
            app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
        except FloodWait as e:
            sleep(e.x)

        i -= 7
        sleep(0)

    if(end_message != ''):
        app.send_message(message.chat.id, end_message)

@app.on_message(filters.command("help", prefixes="/") & filters.me)
def valentine(app, message):
    app.send_message(message.chat.id,f'''

<b>—Команды—

Скрипт спама 1000-7
</b><i>+ Введите: </i><code>.ghoul

</code><b>Скрипт анимации «Я дед инсайд💚»
</b><i>+ Введите</i> <code>.dead 5     

</code><b>Скрипт анимации для</b><code> </code><b>влюблённых: «Спокойной ночи❤️»
</b><i>+ Введите </i><code>.night 5

</code><b>Скрипт анимации «Я люблю тебя❤️‍🔥»
</b><i>+ Введите</i> <code>.love 5   

</code><b>Скрипт анимации «ВЗЛОМ ЖОПЫ»
</b><i>+ Введите</i><code> .jopa 5   


</code>Все команды нужно писать в любой чат<code> </code><i>телеграмм после выполнения кода! (Ввода зависим. числа)</i>
<i></i>

''')

@app.on_message(filters.command("jopa", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = jopa.split("\n")
    e = True
    etime = int(msg.text.split('.jopa ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐  </b>')

@app.on_message(filters.command("love", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = love.split("\n")
    e = True
    etime = int(msg.text.split('.love', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐  </b>')

jopa = '''
           <b>ВЗЛОМ ЖОПЫ</b> 
           <b><i>Loading...</i></b> 
    10%  █▒▒▒▒▒▒▒▒▒▒▒▒
    30%  ███▒▒▒▒▒▒▒▒▒▒    
    50%  █████▒▒▒▒▒▒▒▒
    66%  ██████▒▒▒▒▒▒▒
    79%  ████████▒▒▒▒▒
    84%  █████████▒▒▒▒
    89%  ██████████▒▒▒
    95%  ████████████▒
    99%  █████████████
    100% █████████████
    <b> ВАША ЖОПА ВЗЛОМАНА </b>
    <b><i>Создатель: "Прощайте"</i></b>
    <b><i>Создатель: "Прощайте"</i></b>
    <b><i>Создатель: "Прощайте"</i></b>
'''

love = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
<b>Загрузка любви...</b>
❤️🤍🤍🤍🤍🤍🤍🤍🤍🤍
❤️❤️🤍🤍🤍🤍🤍🤍🤍🤍
❤️❤️❤️🤍🤍🤍🤍🤍🤍🤍
❤️❤️❤️❤️🤍🤍🤍🤍🤍🤍
❤️❤️❤️❤️❤️🤍🤍🤍🤍🤍
❤️❤️❤️❤️❤️❤️🤍🤍🤍🤍
❤️❤️❤️❤️❤️❤️❤️🤍🤍🤍
❤️❤️❤️❤️❤️❤️❤️❤️🤍🤍
❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>

'''
end_message = '<b> ⭐  </b>'
app.run()
