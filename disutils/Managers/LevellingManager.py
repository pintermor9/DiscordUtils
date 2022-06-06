import asyncio
import random
import discord
from discord.ext import commands
from typing import Callable, List, Literal, Union

from .Managers import SingletonManager


class LevellingManager(SingletonManager):
    def __init__(self,
                 bot: commands.Bot,  # TODO possibly make discord.Client support
                 xp_per_message: Union[int, Callable] = 1,
                 level_formula: Callable = lambda x: x * 100 + 100,
                 custom_level_getter: Callable = None,
                 ignored_guilds: List[int] = [],
                 enable_global: bool = True):
        """This manager is used to manage the xp of users. It is a singleton manager, meaning that only one instance can exist.
        :param bot: The bot instance. (``commands.Bot``)
        :param xp_per_message: The amount of xp to give per message. Can be an ``int`` or a ``Callable``. If a ``Callable``, it must return an ``int``.
        :param level_formula: The formula used to calculate the level of a user. It must take an ``int`` as an argument and return a tuple containing the level, the xp in that level and the xp required to level up. For eg. ``tuple(3, 43, 300)`` where ``tuple(level, xp_in_level, xp_required_to_level_up)``.
        :param custom_level_getter: A custom function to get the level of a user. Must take an ``int`` as an argument and return the same as ``level_formula``. It's basically a more customizable version of ``level_formula``.
        :param ignored_guilds: A list of guilds to ignore. (``List[int]``)
        :param enable_global: Whether or not to enable the global xp system. (``bool``)
        """
        # FIXME docs not working cause of the SingletonManager inheritance
        self.bot = bot

        self.data = {}
        self.xp_per_message = xp_per_message
        self.level_formula = level_formula
        self.custom_level_getter = custom_level_getter
        self.ignored_guilds = ignored_guilds
        self.enable_global = enable_global

        # Add listeners
        bot.add_listener(self._on_connect, "on_connect")
        bot.add_listener(self._on_message, "on_message")

    def _get_step(self):
        if isinstance(self.xp_per_message, int):
            return self.xp_per_message
        else:
            return self.xp_per_message()

    def _get_level(self, xp: int):
        if self.custom_level_getter:
            return self.custom_level_getter(xp)

        level = 0
        remaining_xp = xp
        while True:
            required = self.level_formula(level)
            if required > remaining_xp:
                break
            else:
                level += 1
                remaining_xp -= required
        return level, remaining_xp, required

    async def _on_connect(self):
        # TODO load a databas or idk
        self.data = {
            "int(GUILD_ID_HERE)": {
                "user_id_here": 0,
                "another_user_id_here": 10,
            },
            "GLOBAL": {
                "user_id_here": 0,
                "another_user_id_here": 10,
            },
        }

    async def _on_message(self, message):
        if message.author.bot:
            return

        if message.guild is None:
            return

        if not message.guild.id in self.ingored_guilds:
            if message.guild.id not in self.data:
                self.data[message.guild.id] = {}

            if message.author.id not in self.data[message.guild.id]:
                self.data[message.guild.id][message.author.id] = 0

            step = self._get_step()
            old = self.data[message.guild.id][message.author.id]

            new = old + step

            new_level = self._get_level(new)[0]
            if new_level > self._get_level(old)[0]:
                self.bot.dispatch("disutils_level_up", message, new_level)

            self.data[message.guild.id][message.author.id] = new

        if self.enable_global:
            if message.author.id not in self.data["GLOBAL"]:
                self.data["GLOBAL"][message.author.id] = 0

            step = self._get_step()
            old = self.data["GLOBAL"][message.author.id]

            new = old + step

            new_level = self._get_level(new)[0]
            if new_level > self._get_level(old)[0]:
                self.bot.dispatch("disutils_global_level_up",
                                  message, new_level)

            self.data["GLOBAL"][message.author.id] = new

    def set_xp(self, guild_id: Union[int, Literal["GLOBAL"]], user_id: int, xp: int):
        """Sets the xp of a user to a specific value."""
        self.data[guild_id][user_id] = xp

    def get_xp(self, guild_id: Union[int, Literal["GLOBAL"]], user_id: int):
        """Returns the xp of a user."""
        return self.data[guild_id][user_id]

    def add_xp(self, guild_id: Union[int, Literal["GLOBAL"]], user_id: int, xp: int):
        """Adds xp to a user."""
        self.data[guild_id][user_id] += xp

    def remove_xp(self, guild_id: Union[int, Literal["GLOBAL"]], user_id: int, xp: int):
        """Removes xp from a user."""
        self.data[guild_id][user_id] -= xp

    def get_level(self, guild_id: Union[int, Literal["GLOBAL"]], user_id: int):
        """Returns the level of a user."""
        return self._get_level(self.data[guild_id][user_id])[0]

    def get_total_xp_to_level_up(self, guild_id: Union[int, Literal["GLOBAL"]], user_id: int):
        """Returns the total xp required to level up."""
        return self._get_level(self.data[guild_id][user_id])[2]

    def get_remaining_xp_to_level_up(self, guild_id: Union[int, Literal["GLOBAL"]], user_id: int):
        """Returns the remaining xp required to level up."""
        foo = self._get_level(self.data[guild_id][user_id])
        return foo[2] - foo[1]


if __name__ == "__main__":
    l1 = LevellingManager(commands.Bot(
        command_prefix=".", intents=discord.Intents.all()))
    l2 = LevellingManager(commands.Bot(
        command_prefix=".", intents=discord.Intents.all()), xp_per_message=lambda: random.randint(1, 100))
    print(l1 == l2)
    print(l1 is l2)
    print(l1)
    print(l2)

    async def main():
        class foo:
            def __init__(self, **kwargs):
                self.__dict__.update(kwargs)

        print(l1.data)
        while True:
            input()
            await l1._on_message(foo(author=foo(bot=False, id=0), guild=foo(id=0)))
            print(l1.data)
            print(l1._get_level(l1.get_xp(0, 0)))

    asyncio.run(main())
