import mysql.connector
from mysql.connector import Error

#Fonction qui retourne True si une adresse mail est absente dans la base de donnée 
def VerifierMail(liste) -> list:
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='Projet',
                                            user='root',
                                            password='root')

        sql_select_Query = f"select * from user where Mail = '{liste[2]}'"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        return cursor.rowcount == 0

    except mysql.connector.Error as e:
        return False

#Fonction qui retourne True si l'inscription s'est déroulée avec succès
def Inscription(list) -> list:
    if VerifierMail(list) == False:
        return False

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='Projet',
                                            user='root',
                                            password='root')

        mySql_insert_query = f"""INSERT INTO user(Nom, Prenom, Mail, Password) 
                            VALUES 
                            ('{list[0]}', '{list[1]}', '{list[2]}', '{list[3]}') """

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
        return True

    except mysql.connector.Error as error:
        return False

#Fonction qui retourne True si les identifiants (nom,mot de passe) sont présents dans la base de donnée
def Connexion(liste)-> list:
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='Projet',
                                            user='root',
                                            password='root')

        sql_select_Query = f"select * from user where Mail = '{liste[0]}' AND Password = '{liste[1]}'"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        return cursor.rowcount == 1

    except mysql.connector.Error as e:
        return False
