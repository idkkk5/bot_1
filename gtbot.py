import discord
from discord.ext import commands
import asyncio
import random
from random import randint
import os
import platform
import time
 
g=commands.Bot(command_prefix='/')
dabs='440281410197258280'
mrnxd='526187749439438868'
blue='429851945352560650'
 
async def playing():
 while True:
  for x in range(999999):
    await g.change_presence(game=discord.Game(name='Type Ghelp for more info!'))
    await asyncio.sleep(18)
    await g.change_presence(game=discord.Game(name='Made by Dabs Yt#5590'))
    await asyncio.sleep(18)
   
@g.event
async def on_ready():
    print('Gt Pro Bot is up!')
    print('-------------------------')
    g.loop.create_task(playing())
   
@g.command(pass_context=True)
async def farm(ctx,typeId):
    c=ctx.message.channel
    if typeId==None:
        return
    elif typeId=='help':
        await g.say('**How to use /farm?**\n**/farm dirt**\n**/farm sugarcane**\n**/farm ftank**\n**/farm pinball**\n**/farm pepper**\n**/farm chand**\n***Updated 29/01/2018 by Dabs Yt#5590.***')
    elif typeId=='dirt':
        res=randint(0,3)
        if res==0:
            await g.say("No gems!")
        elif res==1:
            res=str(res)
            await g.say('You got '+res+' gem!')
        elif res>1:
            res=str(res)
            await g.say('You got '+res+' gems!')
        return
    elif typeId=='sugarcane':
        res=randint(0,5)
        if res==0:
            await g.say("No gems!")
        elif res==1:
            res=str(res)
            await g.say('You got '+res+' gem!')
        elif res>1:
            res=str(res)
            await g.say('You got '+res+' gems!')
        return
    elif typeId=='ftank':
        res=randint(0,15)
        if res==0:
            await g.say("No gems!")
        elif res==1:
            res=str(res)
            await g.say('You got '+res+' gem!')
        elif res>1:
            res=str(res)
            await g.say('You got '+res+' gems!')
        return
    elif typeId=='pinball':
        res=randint(0,20)
        if res==0:
            await g.say("No gems!")
        elif res==1:
            res=str(res)
            await g.say('You got '+res+' gem!')
        elif res>1:
            res=str(res)
            await g.say('You got '+res+' gems!')
        return
    elif typeId=='pepper':
        res=randint(0,18)
        if res==0:
            await g.say("No gems!")
        elif res==1:
            res=str(res)
            await g.say('You got '+res+' gem!')
        elif res>1:
            res=str(res)
            await g.say('You got '+res+' gems!')
        return
    elif typeId=='chand':
        res=randint(0,25)
        if res==0:
            await g.say("No gems!")
        elif res==1:
            res=str(res)
            await g.say('You got '+res+' gem!')
        elif res>1:
            res=str(res)
            await g.say('You got '+res+' gems!')
        return
   
@g.command(pass_context=True)
async def giveaway(ctx,c:discord.Channel,m:str,num:int):
    if ctx.message.author.id==(dabs) or (mrnxd) or (blue):
        for x in range(num):
           await g.send_message(c,m)
           await g.say('√ Success!')
    else:
      await g.say('No permission!')
   
@g.command(pass_context=True)
async def clear(ctx,num:int):
    if ctx.message.author.id==(dabs) or (mrnxd) or (blue):
        c=ctx.message.channel
        if num=='all':
            await g.purge_from(c,limit=1000)
        else:
            await g.purge_from(c,limit=num)
    else:
         await g.say('No permission!')
         
@g.command(pass_context=True)
async def id(ctx,tag:discord.Member=None):
    if tag:
       id=str(tag.id)
       msg='His id is:'+id+'.'
       await g.say(msg)
    else:
        id=str(ctx.message.author.id)
        msg='Your id is:'+id+'.'
        await g.say(msg)
     
@g.command(pass_context=True)
async def presence(ctx,t1:str,t2:int):
  c=ctx.message.channel
  p=ctx.message.author
  if ctx.message.author.id==(dabs):
      if t1.length()>40:
          await g.say('Max letters for text are 40!')
      elif (t2<0) or (t2>3):
           await g.say('Presence type number limit is 0-3!')
      else:
        await g.change_presence(game=discord.Game(name=t1,type=t2))
        await g.say('**Success!**')
  else:
     await g.say('No permission!')
     
@g.command(pass_context=True)
async def pinfo(ctx,name:discord.Member=None):
  if ctx.message.author.id==(dabs) or (mrnxd) or (blue):
      if name:
        person = ctx.message.author
        channel = ctx.message.channel
        pname = f'{name.name}'
        pid = f'{name.id}'
        ptag = f'{name.mention}'
        pcreated = f'{name.created_at}'
        pdisplay= f'{name.display_name}'
   
        pmsg = '**\nName:' + pname + '\nId:' + pid + '\nTag:' + ptag + '\nAccount created at:' + pcreated + '\nServer name:' + pdisplay + '**'
        await g.say(pmsg)
      elif not tag:
        person = ctx.message.author
        channel = ctx.message.channel
        pname = f'{name.name}'
        pid = f'{name.id}'
        ptag = f'{name.mention}'
        pcreated = f'{name.created_at}'
        pdisplay= f'{name.display_name}'
   
        pmsg = '**\nName:' + pname + '\nId:' + pid + '\nTag:' + ptag + '\nAccount created at:' + pcreated + '\nServer name:' + pdisplay + '**'
        await g.say(pmsg)
  else:
    await g.say('No permission!')
     
@g.command(pass_context=True)
async def render(ctx,w:str=None):
    if w:
        await g.say("http://growtopiagame.com/worlds/" + w.lower() + ".png")
     
@g.command(pass_context=True)
async def avatar(ctx,p:discord.Member=None):
    p1=ctx.message.author
    if p:
        await g.say(f'{p.avatar_url}')
    elif not tag:
        await g.say(f'{p1.avatar_url}')
     
@g.command(pass_context=True)
async def hack(ctx,t:discord.Member=None):
     if t:
        tn=t.name
        t=str(t)
        msg1=await g.say('```Preparing to hack '+t+' .```')
        await asyncio.sleep(2)
        await g.edit_message(msg1,'```Preparing to hack '+t+' ..```')
        await asyncio.sleep(1)
        await g.delete_message(msg1)
        msg2=await g.say('```Searching for '+t+' username in https://growtopiagame.com sql database.```')
        await asyncio.sleep(1.5)
        await g.edit_message(msg2,'```Searching for'+t+'username in https://growtopiagame.com sql database.```')
        await asyncio.sleep(0.5)
        await g.delete_message(msg2)
        msg3=await g.say('```Username found!Reversing base64 hash.```')
        await asyncio.sleep(2)
        await g.edit_message(msg3,'```Username found!Reversing base64 hash..```')
        await asyncio.sleep(0.5)
        await g.delete_message(msg3)
        msg4=await g.say('```Hash reversed!Fetching data from main server with encrypted ip.```')
        await asyncio.sleep(2.5)
        await g.edit_message(msg4,'```Hash reversed!Fetching data from main server with encrypted ip..```')
        await asyncio.sleep(1)
        await g.delete_message(msg4)
        msg5=await g.say('```Success!Sending you the data right now!Check your dms!```')
        await asyncio.sleep(2)
        await g.delete_message(msg5)
        email=tn+'@gmail.com'
        password=tn+'549//'
        await g.send_message(ctx.message.author,'```Username: '+t+'\nEmail: '+email+'\nPassword: '+password+'\nAll data has been sent!```')
     if not t:
         msg1=await g.say('```For security reasons you cant hack yourself! Protocol:Dont_Hack_Dummies.```')
         await asyncio.sleep(3)
         await g.delete_message(msg1)
         
g.run(os.getenv('token'))
