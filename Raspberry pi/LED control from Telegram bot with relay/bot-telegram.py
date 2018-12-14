#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.

This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep


import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

update_id = None


def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot("510013616:AAFlR38KSTLevI0iikdeAWPHzOLvS6rxGUo")

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            #update.message.reply_text(update.message.text)
            a=update.message.text
            try:
                myindex=a.index('+')
            except:
                myindex=-1
        
            if myindex!=-1:
                splited=a.split('+')
                sum=int(splited[0])+int(splited[1])
                update.message.reply_text(sum)
            else:
                update.message.reply_text(a)
            
            fname=update.message.from_user.first_name
            lname=update.message.from_user.last_name
            print("The first name is %s and the last name is %s"%(fname,lname))
            
            try:
                myindex=a.index("led")
            except:
                myindex=-1
            if myindex!=-1:
                splited_2=a.split(",")
                if splited_2[1]=="0":
                    GPIO.output(14,GPIO.LOW)
                    print("LED is set to 0")
                else:
                    GPIO.output(14,GPIO.HIGH)
                    print("LED is set to 1")
                    
                    
    # Request updates after the last update_id
    for name in bot.get_updates(offset=update_id, timeout=10):
        update_id = name.update_id + 1
        if name.message: 

            b=name.message.text
            try:
                myindex2=b.index('+')
            except:
                myindex2=-1
        
            if myindex2!=-1:
                splitedx=b.split('+')
                sum=int(splitedx[0])+int(splitedx[1])
                name.message.reply_text(sum)
            else:
                name.message.reply_text(b)
            
            fname=name.message.from_user.first_name
            lname=name.message.from_user.last_name
            print("The first name is %s and the last name is %s"%(fname,lname))

            
            try:
                myindex2=b.index("led2")
            except:
                myindex2=-1
            if myindex2!=-1:
                splitedx_2=b.split(",")
                if splitedx_2[1]=="0":
                    GPIO.output(12,GPIO.LOW)
                    print("LED is set to 0")
                else:
                    GPIO.output(12,GPIO.HIGH)
                    print("LED is set to 1")      
            
            

if __name__ == '__main__':
    main()
