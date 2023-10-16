import sqlite3

banco = sqlite3.connect('frist_bank.db')

cursor = banco.cursor()


#cursor.execute("CREATE TABLE alunos (nome text, idade integer, email text)")

cursor.execute("INSERT INTO alunos VALUES('Thaise', 21, 'thaiseed@gmail.com')")

banco.commit()
