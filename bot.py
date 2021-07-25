#!/usr/bin/python
# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-
# links:
# https://discord.com/developers/applications
# ===========================================================
'''

                    " ჯიმა ბოტი "                
                
                
>> სიტყვების განმარტება 
>> კომუნიკაცია
>> თარგმნა  ინგლისური - ქართული, ქართული- ინგლისური
>> მესიჯების წაშლა
>> გუგლში ძიება


'''
# ===========================================================
'''
my functions
'''
import functions
# ===========================================================
import random
import discord
import time
from discord.ext import commands
import unidecode
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


driver=webdriver.Chrome(r'C:\Users\gio\Desktop\chatbot.py\chromedriver.exe')
# driver.set_window_position(-20000, 0)
# driver.minimize_window()
# -------------------------------------
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
# -------------------------------------
client = commands.Bot(command_prefix = ".")
@client.event
async def on_ready():
    channel = client.get_channel(808057422773092365)
    await channel.send('მოგესალმები დავით')
    
    
# # -------------------------------------
# start
@client.command(aliases=['მევედი','მოვედი','გაუშვი','დავიწყოთ'])
async def start(ctx):
    channel = client.get_channel(808057422773092365)
    await channel.send('სიამოვნებით   ☺️😊☺️😊☺️😊☺️😊')
# გამოსვლა
@client.command(aliases=['წავედი', 'აბა_ჰე','გავე','წავე'])
async def gonne(txt):
    channel = client.get_channel(808057422773092365)
    await channel.send('კარგად იყავი ბოს, დროებით')
    await txt.channel.purge(limit=9999999999999**99)
    return
    
# -------------------------------------
# პასუხები
@client.command(aliases=["როგორ_ხარ?"])
async def hello(ctx):
    await ctx.send('კარგად შენ?')



@client.command(aliases=['შენ?'])
async def ok(ctx):
    responses =['არამიშავს',
                'ნიჩიო',
                'კარგად']
    await ctx.send(random.choice(responses))

# -------------------------------------
# წაშლის ფუნქცია
@client.command(aliases=['წაშალე'])
async def clear(ctx,number=500000000): # მესიჯების ოდენობა
    channel = client.get_channel(808057422773092365)
    await channel.send('წაშლა..')
    time.sleep(1)
    await ctx.channel.purge(limit=number)
    return
    
    
# -------------------------------------
# დასერჩვა
@client.command(aliases=['ეძებე:','გუგლშიძებნა:'])
async def search(t,name='',text='',a='',b='',c=''):
    driver.get('https://www.google.com/')
    search=driver.find_element_by_name('q')
    search.send_keys(name+' '+text+' '+a+' '+b+' '+c)
    search.send_keys(Keys.ENTER)
    
# -------------------------------------
# სიტყვის განმარტება
@client.command(aliases=['რას_ნიშნავს:','რა_არის:','განმიმარტე:'])
async def define(t,a='',b='',c=''):
    # კონვერტაცია
    text=a+' '+b+' '+c
    texti=str(text)
    # შესვლა
    driver.get('https://bidzer.ge/')
    time.sleep(1)
    # შეყვანა
    search=driver.find_element_by_name('searchterm')
    search.send_keys(texti)
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    # აღება
    words=driver.find_elements_by_xpath('/html/body/div/main/article[5]/h1/a')
    if list(words) ==[]:
        await t.send('არმაქვს შესაბამისი განმარტება')
        return
    for word in words:
        a1=unidecode.unidecode(texti)
        b1=unidecode.unidecode(word.text)
        # შემოწმება
        if str(a1) == str(b1) or a==b1:
            print('if')
            word.get_attribute('href')
            word.click()
            time.sleep(2)
            defin=driver.find_element_by_css_selector('p.post-definition')
            defin=defin.text
            text=word.text+'_ს განმარტება: '+defin
            print(1)
            await t.send(text)
            return
        else:
            await t.send('არმაქვს შესაბამისი განმარტება')
            return
            
            
# -------------------------------------
# english სიტყვის განმარტება
@client.command(aliases=['მითარგმნე:','თარგმნე:'])
async def translate(t,a='',b='',c=''):
    # კონვერტაცია
    text=a+' '+b+' '+c
    texti=str(text)
    # შეყვანა ტექსტის და ძოება
    driver.get('https://www.translate.ge/word/'+texti+'?')
    time.sleep(1)
    # სიტყვების აღება
    words=driver.find_elements_by_class_name('word')
    if list(words) ==[]:
        await t.send('არმაქვს შესაბამისი განმარტება')
        return
    for word in words:
        a1=unidecode.unidecode(texti)
        b1=unidecode.unidecode(word.text)
        print(a1,b1)
        # შემოწმება დამთხვევის
        if str(a1) == str(b1) or a == str(b) or b == str(b) :
            defin=driver.find_element_by_class_name('translation')
            text=word.text+'_ს განმარტება: '+defin.text
            await t.send(text)
            return
        else:
            await t.send('არმაქვს შესაბამისი განმარტება')
            return
            
            
#()()()()()()()()()()()()()()()()()()()()()()
# მოდულური ფუნქციები
# functions.hello()
# შენახვა
client.run('ODA4MDU4NTQ1NDI0Njk1MzY2.YCBBKg.mEvw4wvak1A_qx1hwQEDcakEENs')
