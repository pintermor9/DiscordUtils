import discord
from discord.ext import commands
import disutils

intents = discord.intents.default()
intents.members = True
bot = commands.AutoShardedBot(command_prefix=">", intents=intents)
tracker = disutils.InviteTracker(bot)


@bot.event
async def on_member_join(member):
    # inviter is the member who invited
    inviter = await tracker.fetch_inviter(member)
    # do something with inviter
