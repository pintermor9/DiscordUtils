class SingletonManager:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        raise Exception(
            "This class MUST NOT be instantiated! can only be inherited, tho thats not intended use  either.")
