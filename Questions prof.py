n=1
from random import randint



#Fonction sur la question
def question_n() :
    global confirmation
    global n
    print ("Quelle est votre question n°",n,"?")
    Question = input()
    print ("Votre Question est :",Question,"\n")

#Confirmation question
def confirmation_():
    global confirmation
    confirmation = input("Voulez vous confirmer ? (oui ou non)\n")
    if confirmation != "oui" and confirmation != "non":
        return confirmation_()
    if confirmation == "oui":
        print ("\nQuestion validée et enregistée, veulliez rentrer les réponses de la question",n,":")
    if confirmation == "non":
        print ("\nVous avez choisi de modifier la question.")
        sol()



#Lancement fonction question
def sol():
    global question_n
    global confirmation_
    question_n()
    confirmation_()
 
sol()

#Global
global confirmation

#Lancement fonction réponses
def sol_2():
    global reponses_n
    global confirmation_2
    reponses_n()
    confirmation_2()

#Fonction réponses
def reponses_n():
    global n
    global a
    global b
    global c
    global d
    global confirmation_2
    a = input("A:")
    b = input("B:")
    c = input("C:")
    d = input("D:")
    print ("\nLes réponses de la question",n,"sont",": \n A:",a,"\n B:",b,"\n C:",c,"\n D:",d)
    
global a
global b
global c
global d

#Confirmation réponses
def confirmation_2():
    global sol_2
    confirmation_2 = input("Voulez vous confirmer ? (oui ou non)\n")
    if confirmation_2 != "oui" and confirmation_2 != "non":
        return confirmation_()
    if confirmation_2 == "oui":
        print ("\nQuestion validée et enregistée")
    if confirmation_2 == "non":
        print ("\nVous avez choisi de modifier la question.")
        sol_2()

sol_2()

#Global
global confirmation_2

#Bonnes réponses
def bonnes_rep_n():
    global i
    global a
    global b
    global c
    global d
    bonnes_rep_n = input("Veulliez selectionner les bonnes réponses pour la question (exemple: ""A,B"") :")
    reponse = [a,b,c,d]
    y=randint(0,3)
    o=randint(0,2)
    p=randint(0,1)
    m=0
    z = reponse[y]
    del reponse[y]
    g = reponse[o]
    del reponse[o]
    l = reponse[p]
    del reponse[p]
    v = reponse[m]
    del reponse[m]
    reponse= [z, g, l, v]
    for i in range(0,4) :
        print(i,": ",reponse[i])

bonnes_rep_n()






