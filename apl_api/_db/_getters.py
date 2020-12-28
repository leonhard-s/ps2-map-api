from typing import List

import asyncpg

from ..interfaces import ContinentInfo, ServerInfo


async def get_continents(pool: asyncpg.pool.Pool) -> List[ContinentInfo]:
    conn: asyncpg.Connection
    async with pool.acquire() as conn:  # type: ignore
        rows = await conn.fetch(  # type: ignore
            '''--sql
            SELECT
                ("id", "name")
            FROM
                "autopl"."Continent"
            ;''')
    return [ContinentInfo(*r) for r in rows]  # type: ignore


async def get_servers(pool: asyncpg.pool.Pool) -> List[ServerInfo]:
    conn: asyncpg.Connection
    async with pool.acquire() as conn:  # type: ignore
        rows = await conn.fetch(  # type: ignore
            '''--sql
            SELECT
                ("id", "name", "region")
            FROM
                "autopl"."Server"
            ;''')
    return [ServerInfo(*r) for r in rows]  # type: ignore
