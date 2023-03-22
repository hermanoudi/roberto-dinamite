import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='root'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `dinamite`;")

cursor.execute("CREATE DATABASE `dinamite`;")

cursor.execute("USE `dinamite`;")

# criando tabelas
TABLES = {}
TABLES['Services'] = ('''
      CREATE TABLE `services` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(200) NOT NULL,
      `price` decimal(10,2) NOT NULL,
      `unit` varchar(30) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Users'] = ('''
      CREATE TABLE `users` (
      `name` varchar(200) NOT NULL,
      `nickname` varchar(30) NOT NULL,
      `password` varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# inserindo usuarios
usuario_sql = 'INSERT INTO users (name, nickname, password) VALUES (%s, %s, %s)'
usuarios = [
      ("Hermano Flavio", "Hermanitto", generate_password_hash("edmundo").decode('utf-8')),
      ("Hugo Flavio", "Huguinho", generate_password_hash("romario").decode('utf-8')),
      ("Jose Abilio", "Ze", generate_password_hash("roberto").decode('utf-8'))
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from dinamite.users')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo services
services_sql = 'INSERT INTO services (name, price, unit) VALUES (%s, %s, %s)'
services = [
      ('Perfurações de 30cm diâmetro', 10, 'profundidade'),
      ('Perfurações de 35cm diâmetro', 10, 'profundidade'),
      ('Perfurações de 40cm diâmetro', 10, 'profundidade'),
      ('Perfurações de 45cm diâmetro', 10, 'profundidade'),
]
print(' -------------  Servicos:  -------------')

print(services_sql)

cursor.executemany(services_sql, services)
cursor.execute('select * from dinamite.services')
print(' -------------  Servicos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()