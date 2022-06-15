import os
import sys
import discord
from discord.ext import commands

if True:
    sys.path.insert(0, os.path.abspath('..'))
    from disutils import LevellingManager

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

levelling = LevellingManager(bot, xp_per_message=50)


@bot.listen()
async def on_ready():
    await bot.load_extension("cogs.levelling")
    print(bot.user)

'''
@levelling.event()
async def on_level_up(msg, level):
    await msg.channel.send(f"{msg.author.mention} has leveled up to level {level}!")


@bot.command("level")
async def lvl(ctx):
    print("lol")
    await ctx.send(f"{ctx.author.mention} is level {levelling.get_level(ctx.guild.id, ctx.author.id)}")
'''
with open("token.txt", "r") as f:
    token = f.read()

bot.run(token)
