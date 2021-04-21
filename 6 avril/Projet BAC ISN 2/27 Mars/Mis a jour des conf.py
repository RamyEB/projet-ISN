
from random import randint
n=0

#Fonction sur la question
def question_n() :
    global confirmation
    global n
    n+=1
    print ("Quelle est votre question n°",n,"?")
    Question = input()
    print ("Votre Question est :",Question,"\n")
    confirmation_()

def confirmation_():#Definition qui confirmation la question
    global confirmation
    confirmation = input("Voulez vous confirmer ? (oui ou non)\n")
    if confirmation != "oui" and confirmation != "non":
        confirmation_()
    if confirmation == "oui":
        print ("\nQuestion validée et enregistée, veulliez rentrer les réponses de la question",n,":")
        reponses_n()
    if confirmation == "non":
        print ("\nVous avez choisi de modifier la question.")
        sol()

#Lancement fonction question
def sol():
    global question_n
    global confirmation_
    question_n()
    confirmation_()
 


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
    modif_1()

#Global
global confirmation
global a
global b
global c
global d

#Lancement fonction réponses
def sol_2():
    global reponses_n
    global confirmation_2
    reponses_n()
    confirmation_2()

def solconf():
    global confirmation_3
    global modif_1
    confirmation_3()
    
    
def confirmation_3() :
    global modif_1
    global str
    global e
    global a
    global b
    global c
    global d
    global solconf
    global confirmation_3
    confirmation_3 = input("Voulez vous confirmer la modification : oui ou non\n")
    if confirmation_3 != "oui" and confirmation_3 != "non":
        return confirmation_3()
    if confirmation_3 == "oui":
        print ("Vos réponses sont :")
        print (" A:",a,"\n B:",b,"\n C:",c,"\n D:",d)
        e = input("\nRéponses validées et enregistées: oui ou non\n")
        if e == "oui":
            bonnes_rep_n()
        else :
            modif_1()
    if confirmation_3 == "non":
        print ("\nVous avez choisi de modifier une ou plusieurs réponses.\n")
        modif_1()
        
    
    
def modif_1() :
    global confirmation_3
    global solconf
    global str
    global s
    global a
    global b
    global c
    global d
    global modif_1
    s = input("qu'elle(s) réponse(s) voulez vous modifier: (A, B, C ou D, toutes, aucunes)\n")
    if s == "A" or s == "a" :
        a = input("A:")
        confirmation_3()
    if s == "B" or s == "b" :
        b = input("B:")
        confirmation_3()
    if s == "C" or s == "c" :
        c = input("C:")
        confirmation_3()
    if s == "D" or s == "d" :
        d = input("D:")
        confirmation_3()
    if s =="toutes" :
        a = input("A:")
        b = input("B:")
        c = input("C:")
        d = input("D:")
        confirmation_3()
    if s =="aucunes" :
        confirmation_2()
    if s !="A" and s !="a" and s !="B" and s !="b" and s !="c" and s !="C" and s !="D" and s !="d" and s !="toutes" and s !="aucunes" :
        modif_1()
    
    

#Confirmation réponses
def confirmation_2():
    global confirmation_3
    global modif_1
    confirmation_2 = input("Voulez vous confirmer ? (oui ou non)\n")
    if confirmation_2 != "oui" and confirmation_2 != "non":
        confirmation_()
    if confirmation_2 == "oui":
        print ("\nRéponses validées et enregistées.")
        bonnes_rep_n()
    if confirmation_2 == "non":
        print ("\nVous avez choisi de modifier une ou plusieurs réponses.")
        modif_1()
        



#Global
global confirmation_2

#Bonnes réponses
def bonnes_rep_n():
    global i
    global a
    global b
    global c
    global d
    # bonnes_rep_n = input("Veulliez selectionner la bonne réponse pour la question (exemple: A) :")
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
    relance()
        # if relance == oui
        #     main()
        #     n=+1
        
def relance():
    relance = input("Voulez vous ajouter une question ?")
    if relance != "oui" and relance != "non":
        relance()
    if relance == "oui":
        main()
    if confirmation_2 == "non":
        print ("\nFin")

def main():
    global n
    question_n()
main()


    








