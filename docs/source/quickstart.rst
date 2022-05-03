Quickstart
==========

Installation
------------
.. code-block:: bash

    pip install disutils

.. warning:: 

    discord.py is not listed on the library's requirements, due to installing discord.py on top of py-cord can cause wierd bugs. You need to install one of them yourself! 


Music
-----

.. warning:: 

    You need ffmpeg or avconv installed and added to the PATH to use this.
    To try it out, run the following command in a terminal or command prompt:

    .. code-block:: bash

        ffmpeg -version

To be able to use music with your bot, you have to create a :class:`Music` object. I recommend storing this in an instance variable of a Cog. For eg.

    .. code-block:: python

        # main.py
        bot = discord.Bot(...)

        # somewhere else in a cog (recommended)
        class Music(commands.Cog):
            def __init__(self, bot):
                self.bot = bot
                self.music = disutils.Music()
            
            @commands.command()
            async def play(self, ctx, url_or_search):
                player = self.music.get_player(ctx)

                await player.queue(url_or_search)
                if not player.is_playing():
                    player.play()


InviteTracker
-------------

As of now, the discord API does not provide the inviter of a member. This is a workaround for that, and sometimes may be glitchy. 

    .. code-block:: python

        class InviteTracker(commands.Cog):
            def __init__(self, bot):
                self.bot = bot
                self.invite_tracker = disutils.InviteTracker()
            
            @commands.Cog.listener()
            async def on_member_join(self, member):
                inviter = await self.invite_tracker.fetch_inviter(member)
                print(f"{member} joined, and was invited by {inviter}")


Pagination
----------

Paginates a list of ``discord.Embed`` objects.
Pagination works a bit differently from the others. 

    .. code-block:: python

        @commands.command()
        async def paginate(self, ctx):
            pages = [
                discord.Embed(title=f"Page {i}", description=f"This is page {i}") for i in range(1,10)
            ]
            paginator = disutils.Paginator(ctx, pages, timeout=30)
            await paginator.run()
