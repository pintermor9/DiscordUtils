import discord
from discord.ext import commands
import disutils

bot = commands.Bot(command_prefix=">")


@bot.command()
async def paginate(ctx):
    embed1 = discord.Embed(color=ctx.author.color).add_field(
        name="Example", value="Page 1")
    embed2 = discord.Embed(color=ctx.author.color).add_field(
        name="Example", value="Page 2")
    embed3 = discord.Embed(color=ctx.author.color).add_field(
        name="Example", value="Page 3")
    paginator = disutils.Pagination.AutoEmbedPaginator(ctx)
    embeds = [embed1, embed2, embed3]
    await paginator.run(embeds)

bot.run("token")
