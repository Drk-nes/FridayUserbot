# sed lyf
# Made A Litte UnderStoodAble By Blue_Devil and also removed some unnecessary imports
# This Code Is Also Reduced To 106 Lines From Over 150 Lines
# The Logo Was Created By Akash
# Imports
from os import system as cmd
from time import sleep
from random import choice as r
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from userbot import CHROME_DRIVER
from userbot.utils import admin_cmd
from userbot import GOOGLE_CHROME_BIN
CARBONLANG = "auto"
LANG = "en"
Blue_Facts = ['**Did U Know**\n\nThe Most Wonderful Plugin That Is Javify Was created By [Blue_Devil](https://t.me/AKASH_AM1) On His Phone Abd Not On A Computer!!',
              '**Did U Know**\n\n[IndianBhai](https://t.me/pureindialover) Is The Actual Owner Of Indian Bot!!',
              '**Did U Know**\n\n[Python](https://docs.python.org/) Is The Future Of Programming',
              '**Did U Know**\n\nCarryMinati Is Always Against tikTok',
              '**Did U Know**\n\nIt Took Over 1 Month For Blue_Devil To Create The Javify Plugin',
              '**Did U Know**\n\nCC-Checker Plugin Is Coming soon',
              '**Did U Know**\n\nFree-Fire Is Lit/Love',
              '**Did U Know**\n\nThe Song Yalgaar Of CarryMinati Is Due To His Video Got Down Due To That ""Graduated 4th Fail""',
              '**Did U Know**\n\nIts Very Easy To Make Plugins'
              ]
bf = r(Blue_Facts)
def carbon_lago():
    logo = ('█▒█▒▒▒█▒▒█▒      ████      █▒▒▒▒▒▒▒▒█ ████████████ ▒█▒█▒█▒█▒ █▒      █\n'
            '█               █    █     █        █  █         █ █       ▒ ▒ ▒     █\n'
            '█              █      █    █        █  █         █ ▒       █ █  ▒    █\n'
            '█             █▒▒▒█▒▒▒▒█   ██████████  █▒▒▒██▒▒▒▒█ █       ▒ ▒   █   ▒\n'
            '█            █          █  ███         █         █ ▒       █ █    ▒  █\n'
            '█           █            █ █  ██       █         █ █       ▒ ▒     ▒ ▒\n'
            '████████████              ██    ██    ████████████ █████████ █      ██\n'
            '██████████████████████████████████████████████████████████████████████\n')
    print(f'{logo}')
@borg.on(admin_cmd("nbon")) # This Is The Command Recogniser , This Has Been Changed To Borg.on From Register
async def carbon_api(mytext):
    carbon_lago()
    if not mytext.text[0].isalpha() and mytext.text[0] not in ("/", "#", "@", "!"): # Checking For Alpha Or Not
        await mytext.edit('**One Minito**')
        CARBON = "https://carbon.now.sh/?l={lang}&code={code}"
        global CARBONLANG
        textx = await mytext.get_reply_message()
        pcode = mytext.text
        if pcode[8:]:
            pcode = str(pcode[8:])
        elif textx:
            pcode = str(textx.message)  # Importing message to module
        code = quote_plus(pcode)  # Converting to urlencoded
        await mytext.edit('Meking Carbon...')
        url = CARBON.format(code=code, lang=CARBONLANG)
        chrome_options = Options() # No Need to See All This
        chrome_options.add_argument('--headless')
        chrome_options.binary_location = GOOGLE_CHROME_BIN
        chrome_options.add_argument('--window-size=1920x1080')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        prefs = {'download.default_directory': './'}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)
        driver.get(url) # Url Is Given Avobe
        await mytext.edit('0 Bhau\nAb Tak Sirf 50% Hua He')
        download_path = "./" # Download Path Is Very Important
        driver.command_executor._commands["send_command"] = (
            "POST",
            "/session/$sessionId/chromium/send_command",
        )
        params = {
            "cmd": "Page.setDownloadBehavior",
            "params": {
                "behavior": "allow",
                "downloadPath": download_path
            },
        }
        driver.execute("send_command", params)
        # Now It Will Download The File
        driver.find_element_by_xpath(
            "//button[contains(text(),'Export')]").click()
        await mytext.edit('Are Bhai **Sabr** Karo')
        sleep(2.5)
        await mytext.edit("Chalo Hogaya")
        driver.quit()
        file = "./carbon.png"
        await mytext.edit("Ab Upload Karta Hu")
        # Uploading The File
        await mytext.client.send_file(
            mytext.chat_id,
            file,
            caption=
            "<< Here's Your Carbon Boi,\n  Carbonised By [Darknes](https://t.me/drk_nes)>>",
            force_document=True,
            reply_to=mytext.message.reply_to_msg_id,
        )
        cmd("rm ./carbon.png") # A Better Way A Deleting
        # Removing carbon.png after uploading
        await mytext.edit('Chalo Ab Bye')
        sleep(2)
        await mytext.delete()
        # Deleting msg
        # This part is new
        #Credits Blue Devil And INDIANBOT
        await borg.send_message(mytext.chat_id, bf)
