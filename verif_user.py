
import sqlite3

def senha_ver(c) -> str:
    conn =sqlite3.connect('bdados1.db')
    cursor = conn.cursor()
    cursor.execute(f'select senha from users where email="{c}"')
    rows = cursor.fetchall()
    for row in rows:
        senha = row[0]
        return senha
    # conn.commit()
    conn.close()


def email_ver(c) -> bool:
    conn = sqlite3.connect('bdados1.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT email FROM users WHERE email="{c}"')
    rows = cursor.fetchall()
    conf = False
    for row in rows:
        # print(row[0])
        if row[0] == c:
            conf = True    
    return conf


