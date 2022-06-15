from discord.ext import commands
import discordSuperUtils
from disutils import LevellingManager, CogEventHandler


class Levelling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.manager = LevellingManager(bot, xp_per_message=50)
        print("added")

    @commands.command()
    async def level(self, ctx):
        print("lol")
        await ctx.send(f"{ctx.author.mention} is level {self.manager.get_level(ctx.guild.id, ctx.author.id)}")


async def setup(bot):
    await bot.add_cog(Levelling(bot))
