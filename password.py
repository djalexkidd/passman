#Alexandre Poyer
#Vendredi 15 Octobre 2021
#Gestionnaire de mots de passe en Python
import random
import csv

def reader(): #Affiche tout les mots de passe depuis un fichier csv
    with open('passwords.csv','r') as f: #Ouvre le fichier passwords.csv en lecture (read)
        reader = csv.reader(f)
        for row in reader: #Affiche toutes les lignes du document
            print(', '.join(row))

def writer(password, passname): #Stocke un mot de passe dans un fichier csv
    with open('passwords.csv', 'a', newline='', encoding='utf-8') as f: #Ouvre le fichier passwords.csv en écriture (append)
        writer = csv.writer(f) #Crée l'instance d'écriture
        writer.writerow([passname] + [] + [password]) #Écrit le mot de passe et son nom dans une ligne séparée

def creator(): #Génère aléatoirement un mot de passe
    lower = "abcdefghijklmnopqrstuvwxyz" #Liste des charactères minuscules
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Liste des charactères majuscules
    numbers = "0123456789" #Liste des chiffres
    symbols = "[]{}()\*/_-" #Liste des symboles

    all = lower + upper + numbers + symbols #Combine les quatre listes en un tout

    length = int(input("Entrez la longueur du mot de passe: ")) #Demande à l'utilisateur d'entrer une longueur
    password = "".join(random.sample(all, length)) #Génère le MdP depuis la liste des charactères, de la longueur et de la librairie random et le stocke dans une variable
    print(password) #Affiche le mot de passe depuis la variable
    passname = input("Entrez un nom pour ce mot de passe: ") #Demande à l'utilisateur d'entrer un nom
    writer(password, passname) #Écrit le mot de passe et son nom en utilisant la fonction writer

def main(): #Menu principal
    while True: #Boucle jusqu'à l'arrêt du programme
        s = input("Créer, voir les mots de passe ou quitter? [C/v/q] ") #Demande à l'utilisateur de choisir une fonction
        if s.lower() in "c": #Si l'utilisateur veut créer un mot de passe
            creator()
            print("Mot de passe enregistré.")
        elif s.lower() in "v": #Si l'utilisateur veut voir ses mots de passe
            reader()
        elif s.lower() in "q": #Si l'utilisateur veut quitter
            break
        else:
            pass

main()
