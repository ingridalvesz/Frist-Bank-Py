import sqlite3

try:
    banco = sqlite3.connect('frist_bank.db')

    cursor = banco.cursor()

    cursor.execute("DELETE from alunos WHERE nome = 'Fernanda'")

    banco.commit()
    banco.close()
    print("Aluno deletado")


except sqlite3.Error as erro:
    print("Erro ao excluir",erro)
