import asyncpg


class Database:
    def __init__(self, config):
        self.config = config

        self.conn: asyncpg.connection.Connection = None

    def __str__(self):
        return f"<{self.__class__.__name__}>"

    async def connect(self):
        self.conn = await asyncpg.connect(dsn=self.config.get('dsn'))

    async def close(self):
        await self.conn.close()

    async def execute(self, query):
        await self.conn.execute(query)

    async def create_table(self, table_name, columns=None, ifnotexists=False):
        if columns is None:
            columns = []
        if ifnotexists:
            await self.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})")
        else:
            await self.execute(f"CREATE TABLE {table_name} ({', '.join(columns)})")

    async def drop_table(self, table_name, ifexists=False):
        if ifexists:
            await self.execute(f"DROP TABLE IF EXISTS {table_name}")
        else:
            await self.execute(f"DROP TABLE {table_name}")

    async def insert(self, table_name, data):
        values = "(" + ", ".join(f"'{value}'" for value in data.values()) + ")"
        await self.execute(f"INSERT INTO {table_name} ({', '.join(data.keys())}) VALUES {values}")

    async def update(self, table_name, data):
        data = ", ".join(f"{key} = '{value}'" for key, value in data.items())
        await self.execute(f"UPDATE {table_name} SET {data}")

    async def select(self, table_name, columns=None, where=None):
        if columns is None:
            columns = ["*"]
        columns = ", ".join(columns)

        query = f"SELECT {columns} FROM {table_name}"

        if where:
            query += f" WHERE {' AND '.join(where)}"

        return await self.fetch(query)

    async def fetch(self, query):
        return [dict(record) for record in await self.conn.fetch(query)]

    async def fetchrow(self, query):
        return [dict(record) for record in await self.conn.fetchrow(query)]


async def main():
    db = Database({})
    await db.connect()
    await db.create_table("test", ["id serial PRIMARY KEY", "name varchar(255)"], ifnotexists=True)
    await db.insert("test", {"name": "test"})
    await db.update("test", {"name": "test2"})
    print(await db.select("test"))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
