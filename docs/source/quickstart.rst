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
