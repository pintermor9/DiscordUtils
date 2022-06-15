from .Managers import SingletonManager


class AutoModManager(SingletonManager):
    def __init__(self,
                 banned_words: dict = None,):
        self.bot = None
        self.banned_words = banned_words

    def set_bot(self, bot):
        super().set_bot(bot)
        bot.add_listener(self._on_message, "on_message")
        bot.add_listener(self._on_message, "on_message_edit")
        bot.add_listener(self._on_connect, "on_connect")

    async def _on_connect(self):
        self.banned_words = {
            920662357372444672: ["fuck", "shit"]
        }

    async def _on_message(self, message):
        if message.author.bot:
            return

        if message.guild is None:
            return

        banned_words = self.banned_words.get(message.guild.id, [])

        for word in banned_words:
            if word in message.content.lower():
                return self.dispatch("banned_word", message, word)
