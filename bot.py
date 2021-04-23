import os
import discord
import requests
import json
import random

from discord.ext import commands
from config import settings

print("Thiccy v1.0 by Lunarelly\nGitHub: https://github.com/Lunarelly")

bot = commands.Bot(command_prefix = settings["prefix"])

@bot.event

async def on_ready():
    print("Logged in as {0}".format(bot.user))
    await bot.change_presence(status = discord.Status.idle, activity = discord.Game("Thiccy"))

@bot.command()

async def hello(ctx):
    author = ctx.message.author
    await ctx.channel.send(f"Привет, {author.mention}!")

@bot.command()

async def cat(ctx):
    response = requests.get("https://some-random-api.ml/img/cat")
    json_data = json.loads(response.text)

    embed = discord.Embed()
    embed.set_image(url = json_data["link"])
    await ctx.channel.send(embed = embed)

@bot.command()

async def billy(ctx):
    embed = discord.Embed(title = f"Billy... R.I.P 02.03.2018")
    embed.set_image(url = "https://i.ytimg.com/vi/Dycy5tW3970/hqdefault.jpg")
    await ctx.channel.send(embed = embed)

@commands.has_permissions(kick_members = True)
@bot.command()

async def kick(ctx, user: discord.Member, *, reason = "без причины"):
    if user == ctx.message.author:
        await ctx.channel.send(f"Вы не можете кикнуть самого себя!")
        return
    await user.kick(reason = reason)
    kick = discord.Embed(title = f"Кикнут: {user.name}", description = f"Причина: {reason}\nКикнул: {ctx.author.mention}")
    await ctx.channel.send(embed = kick)
    await user.send(embed = kick)

@commands.has_permissions(ban_members = True)
@bot.command()

async def ban(ctx, user: discord.Member, *, reason = "без причины"):
    if user == ctx.message.author:
        await ctx.channel.send(f"Вы не можете забанить самого себя!")
        return
    await user.ban(reason = reason)
    ban = discord.Embed(title = f"Забанен: {user.name}", description = f"Причина: {reason}\nЗабанил: {ctx.author.mention}")
    await ctx.channel.send(embed = ban)
    await user.send(embed = ban)

@bot.command()

async def chance(ctx):
    chance = random.randint(1, 100)
    author = ctx.message.author
    await ctx.channel.send(f"{author.mention}, шанс этого - {chance}%")

bot.run(settings['token'])