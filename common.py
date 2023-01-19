async def get_sql_connection():
    async def conn_attributes(conn):
        conn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
        conn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        conn.setdecoding(pyodbc.SQL_WMETADATA, encoding='utf_16_le')
        conn.setencoding(encoding='utf-8')

    dsn = 'DSN=tibero6'
    return await aioodbc.connect(dsn=dsn, loop=asyncio.get_event_loop(), after_created=conn_attributes)


async def sql_query(sql, *args):
    conn = await get_sql_connection()
    cur = await conn.cursor()
    try:
        await cur.execute(sql, args)
    except Exception as e:
        await cur.close()
        await conn.close()
        _log.error(e)
        raise e
    rows = None
    if cur.description != None:
        rows = await cur.fetchall()
        cols = [column[0] for column in cur.description]
        r = []
        for row in rows:
            d = dict()
            for i, col in enumerate(row):
                # db의 응답은 uppercase로 오지만 json 결과는 lowercase로 전달하기 위해 여기에서 lowercase로 변경하는 로직을 추가
                d[cols[i].lower()] = col
            r.append(d)
        rows = r
    await cur.close()
    await conn.close()
    return rows
