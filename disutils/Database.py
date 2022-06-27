import asyncpg


class Database:
    def __init__(self, config):
        self.config = config
        self.pool = None

    async def connect(self):
        self.conn = await asyncpg.connect('postgresql://postgres@localhost/test')

    async def close(self):
        await self.conn.close()
