from .EventHandler import EventHandler


class SingletonManager(EventHandler):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def set_bot(self, bot):
        self.bot = bot
