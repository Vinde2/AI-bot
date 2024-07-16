import discord
from discord.ext import commands
import os, random
import requests
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if attachment.filename[-1] == "g" and attachment.filename[-2] == "p" and attachment.filename[-3] == "j" :
                name = attachment.filename
                url = attachment.url
                await attachment.save(name)
                await ctx.send("....Saved:)")
                await ctx.send(get_class(model="keras_model.h5", labels="labels.txt", image = name))
    else :
        await ctx.send("Nothing here")




bot.run("MTE5Mjg3MTc2ODU5NjE2MDU1Mg.GJB7jL.d6VWeiv5OceBqBlxbNhfLRrPmsM1Ard1WnOsEY")

