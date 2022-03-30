import discord
from discord.ext import commands
import DiscordUtils

intents = discord.intents.default()
intents.members = True
bot = commands.AutoShardedBot(command_prefix=">", intents=intents)
tracker = DiscordUtils.InviteTracker(bot)

@bot.event
async def on_member_join(member):
    inviter = await tracker.fetch_inviter(member) # inviter is the member who invited
    # do something with inviter 
