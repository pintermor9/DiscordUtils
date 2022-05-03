.. currentmodule:: disutils

Event reference
====================

As you propably know, discord.py has an event system.
But you might not have known that you can actually create your own events.

.. code-block:: python3

    # you can listen to events with the
    @bot.event # decorator
    async def on_message(message):
        # do stuff
        pass
    
    # but you can also register your own event linstener
    @bot.event
    async def on_my_event(event_arg1, event_arg2):
        # do stuff
        pass
    
    # and even *dispatch* them
    bot.dispatch('my_event', 'arg1', 'arg2')

disutils has a few of these custom events.

disutils' custom events
-----------------------

.. function:: on_disutils_music_queue(ctx: discord.Context, song: disutils.Song)
    :noindex:

    This event is called when a song is queued.

.. function:: on_disutils_music_play(ctx: discord.Context, song: disutils.Song)

    This event is called when a song starts playing.

    .. warning:: 

        This event is called when the player starts playing. NOT when you queue a song! 
        See :func:`on_disutils_music_queue` for that.

.. function:: on_disutils_music_pause(ctx: discord.Context, song: disutils.Song)

    This event is called when the player is paused.


.. function:: on_disutils_music_resume(ctx: discord.Context, song: disutils.Song)

    This event is called when the player is resumed.

.. function:: on_disutils_music_stop(ctx: discord.Context)

    This event is called when the player is stopped.

.. function:: on_disutils_music_skip(ctx: discord.Context, old: disutils.Song, new: Optional[disutils.Song])

    This event is called when the player skips a song.

.. function:: on_disutils_music_volume_change(ctx: discord.Context, song: disutils.Song, volume: float)

    This event is called when the player's volume is changed.

    ``volume`` is the new volume and its a ``float`` between ``0.00`` and ``1.00``.

.. function:: on_disutils_music_toggle_loop(ctx: discord.Context, song: disutils.Song)

    This event is called when the player's looping status is changed.

    .. tip::

        If you want to know if the player is looping, use :attr:`Song.is_looping`.

.. function:: on_disutils_music_queue_remove(ctx: discord.Context, song: disutils.Song)

    This event is called when a song is removed from the queue.

.. function:: on_disutils_music_queue_shuffle(ctx: discord.Context)

    This event is called when the queue is shuffled.
