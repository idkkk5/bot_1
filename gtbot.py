import discord
from discord.ext import commands
import asyncio
import random
import os
import platform
import time

g=commands.Bot(command_prefix='/')

@g.event
async def on_ready():
    print('Gt Pro Bot is up!')
    print('-------------------------')
    
@g.event
async def on_command_error(er,ctx):
  c=ctx.message.channel
  p=ctx.message.author
  if isinstance(er,commands.errors.MissingRequiredArgument):
    await g.send_message(c,'Error:MissingRequiredArgument.')
    return
  elif isinstance(er,commands.errors.BadArgument):
    await g.send_message(c,'Error:BadArgument.')
    return
  elif isinstance(er,commands.errors.CommandNotFound):
    return
  elif isinstance(er,commands.errors.TooManyArguments):
    await g.send_message(c,'Error:TooManyArguments.')
    return
  elif isinstance(er,commands.errors.CommandError):
    await g.send_message(c,'Error on command execution! Please report the bug at Dabs Yt#5590!Error:CommandError.')
    return 
  elif isinstance(er,commands.errors.UserInputError):
    await g.send_message(c,'Error:UserInputError.')
    return
  elif isinstance(er,commands.errors.DiscordException):
    await g.say('Error:DiscordException.')
    return 
    
@g.command(pass_context=True)
async def farm(ctx,typeId):
    if typeId==None:
        return
    elif typeId=='help':
        await g.say('**How to use /farm?**\n1.**/farm dirt**\n2.**/farm sugarcane**\n3.**/farm ftank**\n4.**/farm pinball**\n5.**/farm pepper**\n6.**/farm chand**\n***Updated 27/01/2018 by Dabs Yt#5590.')
    elif typeId=='dirt':
        await g.say('You farmed dirt!')
        return
    elif typeId=='sugarcane':
        await g.say('You farmed sugarcane!')
        return
    elif typeId=='ftank':
        await g.say('You farmed fishtank!')
        return
    elif typeId=='pinball':
        await g.say('You farmed pinball!')
        return
    elif typeId=='pepper':
        await g.say('You farmed pepper!')
        return
    elif typeId=='chand':
        await g.say('You farmed chandelier!')
        return
    
g.run(os.getenv('token'))