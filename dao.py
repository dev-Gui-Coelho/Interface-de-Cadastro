import sqlite3



def inserir(c):
    conn = sqlite3.connect('bdados1.db')
    cursor = conn.cursor()
    sql = f'INSERT INTO users VALUES("{c.nome}", "{c.email}", "{c.senha}", "{c.num}", "{c.gen}", "{c.pais}")'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()

def excluir(c):
    conn =sqlite3.connect('bdados1.db')
    cursor = conn.cursor()
    sql = f'DELETE FROM users WHERE email="{c}"'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()

def atualizar(c):
    conn = sqlite3.connect('bdados1.db')
    cursor = conn.cursor()
    sql = f'UPDATE users SET nome="{c.nome}",contato="{c.num}",genero="{c.gen}",pais="{c.pais}" WHERE email="{c.email}"'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
def listar_bd(c):
    conn = sqlite3.connect('bdados1.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM users WHERE email="{c}"')
    rows = cursor.fetchone()
    if rows:
        return rows
    conn.close()






