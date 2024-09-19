import sqlite3


#Ele faz a conecção com o bd, se ele não existir o py cria um com esse nome
conn = sqlite3.connect('bdados1.db')
# sql =  'create table users(nome text not null,email text not null PRIMARY KEY, senha text not null,contato text ,genero text, pais text)'
# conn.execute(sql)


