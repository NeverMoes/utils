import pymysql

config={'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'passwd': ''}


def db_rename(old_db, new_db, config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    cur.execute('use {old_dbname}'.format(old_dbname=old_db))
    cur.execute('show tables')
    tables = [tb_name[0] for tb_name in cur.fetchall()]
    for table in tables:
        cur.execute('rename table {old_dbname}.{table_name} to {new_dbname}.{table_name}'.format(
            old_dbname=old_db, new_dbname=new_db, table_name=table))
    cur.execute('drop database {old_dbname}'.format(old_dbname=old_db))
    conn.close()
