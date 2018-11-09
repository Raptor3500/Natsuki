import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import youtube_dl

startup_extensions = [
  'cogs.message',
]

bot = commands.Bot(command_prefix='natsuki ')
bot.remove_command('help')
ownerID = "274298631517896704"
Error = 0xFF0000
messages = ['rock', 'paper', 'scissors']

# To remove the help command and make your own help command
#bot.remove_command('help')

@bot.event
async def on_ready():
  print ("------")
  print ("My name is " + bot.user.name)
  print ("With the ID: " + bot.user.id)
  print ("Using discord.py v" + discord.__version__)
  print ("------")
  
  # Make me say stuff
@bot.command(pass_context=True)
async def say(ctx, *args):
    """Make me say your message"""
    if ctx.message.author.id in ownerID:
        channel = ctx.message.channel
        mesg = ' '.join(args)
        await bot.delete_message(ctx.message)
        await bot.send_typing(channel)
        await asyncio.sleep(1)
        await bot.say(mesg)
        print (ctx.message.author.id + " or " + ctx.message.author.name + " made me say '{}'".format(mesg))
        
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
            
@bot.command(pass_context=True)
async def playing(ctx, *args):
  if ctx.message.author.id in ownerID:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= (mesg)))
    await bot.say("I am now playing " + mesg)
    
@bot.command(pass_context=True)
async def watching(ctx, *args):
  if ctx.message.author.id in ownerID:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= mesg, type=3))
    
@bot.command(pass_context=True)
async def listening(ctx, *args):
  if ctx.message.author.id in ownerID:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= mesg, type=2))
    
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
  if ctx.message.author.id in ownerID:
  
    embed = discord.Embed(title="{}'s info".format(user.name), description='Here is what I could find:', color=ctx.message.author.color)
    embed.add_field(name='Name', value='{}'.format(user.name))
    embed.add_field(name='ID', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Highest Role', value='<@&{}>'.format(user.top_role.id), inline=True)
    embed.add_field(name='Joined at', value='{:%d/%h/%y at %H:%M}'.format(user.joined_at), inline=True)
    embed.add_field(name='Created at', value='{:%d/%h/%y at %H:%M}'.format(user.created_at), inline=True)
    embed.add_field(name='Discriminator', value='{}'.format(user.discriminator), inline=True)
    embed.add_field(name='Playing', value='{}'.format(user.game))
    embed.set_footer(text="{}'s Info".format(user.name), icon_url='{}'.format(user.avatar_url))
    embed.set_thumbnail(url=user.avatar_url)
  
    await bot.say(embed=embed)
  
@bot.command()
async def rate(str : str):
    str = str.strip()
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    if 'Xenzai' in str:
        await bot.say('Are you kidding me, Xenzai is a freaking 10/10!')
    if 'Xenzai' not in str:
        await bot.say('I rate {} a {}/10'.format(str, random.choice(number)))
        
@bot.command(pass_context=True)
async def prune(ctx, number, *args):
  if ctx.message.author.id in ownerID:
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)
    
@bot.command()
async def choose(str : str, *args):
  mesg = ' '.join(args)
  choices = [str, mesg]
  await bot.say('I choose {}'.format(random.choice(choices)))
  
@bot.command()
async def doki(str : str):
  str = str.strip
  if 'natsuki' or 'Natsuki' in str:
    await bot.say('You wanna hear about me?')
    await bot.say('Ok then')
    await bot.say('Im the youngest in the literarture club people call me cute even though Im not. My friends in the literature club are Giovanni, Sayori, Yuri, And ~~Monika~~ we have lots of fun in the literature club maybe you can join us!')
    await bot.say('Do natsuki dokidokiinfo <Doki Doki character mentioned in my message> if you wanna hear about anyone else') 
  elif 'sayori' or 'Sayori' in str:
    await bot.say('So you wanna hear about sayori huh? ok then')

        
    

  




bot.run(os.environ.get('Token'))
