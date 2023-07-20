from tkinter import*
from tkinter.messagebox import *
from math import *
import webbrowser
import os
import random
import time

##################################################################################################################
def LOL():
    global degat_perso0,degat_perso1
    global NbVie1,NbVie2,PerteVie
    global NbSaut0 , NbSaut
    global sautP1, sautP1
    global DovahJ1,DovahJ2,WitcherJ1,WitcherJ2
    global u,v,w,k
    global firstgame

    canvas.forget()
    canvas1.pack()

    canvas1.itemconfig(AQW1, state="normal")

    canvas1.itemconfig(personnage, state="normal")
    canvas1.itemconfig(personnage1, state="normal")
    canvas1.itemconfig(zone_hitbox, state="normal")
    canvas1.coords(zone_hitbox, -100 , -100)
    canvas1.itemconfig(zone_hitbox1, state="normal")
    canvas1.coords(zone_hitbox1, -100 , -100)
    canvas1.itemconfig(VP11, state="normal")
    canvas1.itemconfig(VP12, state="normal")
    canvas1.itemconfig(VP13, state="normal")
    canvas1.itemconfig(VP21, state="normal")
    canvas1.itemconfig(VP22, state="normal")
    canvas1.itemconfig(VP23, state="normal")

    canvas1.itemconfig(txt,text="200 PV", state="normal")
    canvas1.itemconfig(txt1,text="200 PV", state="normal")
    canvas1.itemconfig(BannierB, state="normal")

    if DovahJ1 == True and DovahJ2 == True:
        canvas1.itemconfig(PourcentPersoDovahRouge, state="normal")
        canvas1.itemconfig(PourcentPersoDovahBleu, state="normal")

    if DovahJ1 == True and WitcherJ2 == True:
        canvas1.itemconfig(PourcentPersoDovahRouge, state="normal")
        canvas1.itemconfig(PourcentPersoWitcherBleu, state="normal")

    if WitcherJ1 == True and WitcherJ2 == True:
        canvas1.itemconfig(PourcentPersoWitcherRouge, state="normal")
        canvas1.itemconfig(PourcentPersoWitcherBleu, state="normal")

    if WitcherJ1 == True and DovahJ2 == True:
        canvas1.itemconfig(PourcentPersoWitcherRouge, state="normal")
        canvas1.itemconfig(PourcentPersoDovahBleu, state="normal")

    canvas1.bind('<Motion>',BJM)
    canvas1.bind('<Button-1>',BJB)

    canvas1.coords(personnage,100,45)
    canvas1.coords(personnage1,960,45)

    degat_perso0 = 200
    degat_perso1 = 200

    NbVie1 = 3
    NbVie2 = 3

    NbSaut0 = 2
    NbSaut = 2

    sautP1 = True
    sautP2 = True

    PerteVie = False

    u=0
    v=0

    w=0
    k=0

    terrain1()
    if firstgame == True:
        mouvement()
        firstgame = False

    canvas1.bind_all('<d>',droiteOn)
    canvas1.bind_all('<KeyRelease-d>',droiteOff)
    canvas1.bind_all('<q>',gaucheOn)
    canvas1.bind_all('<KeyRelease-q>',droiteOff)
    canvas1.bind_all('<z>',saut)
    canvas1.bind_all('<e>',frapper)
    canvas1.bind_all('<KeyRelease-e>',frapperOff)

    canvas1.bind_all('<Right>',droiteOn1)
    canvas1.bind_all('<KeyRelease-Right>',droiteOff1)
    canvas1.bind_all('<Left>',gaucheOn1)
    canvas1.bind_all('<KeyRelease-Left>',droiteOff1)
    canvas1.bind_all('<Up>',saut1)
    canvas1.bind_all('<m>',frapper1)
    canvas1.bind_all('<KeyRelease-m>',frapperOff1)

def verifCollision(m,p):
    global personnage,listeBloc,saut
    collision = False
    coord = canvas1.coords(personnage)
    superposition = canvas1.find_overlapping(coord[0]+m,coord[1]+p,coord[0]+30+m,coord[1]+40+p)
    for L in superposition:
        for I in listeBloc :
            if L==I:
                collision = True
    return(collision)

def verifCollision1(m,p):
    global personnage1,listeBloc,saut1
    collision = False
    coord = canvas1.coords(personnage1)
    superposition = canvas1.find_overlapping(coord[0]+m,coord[1]+p,coord[0]+30+m,coord[1]+40+p)
    for L in superposition:
        for I in listeBloc :
            if L==I:
                collision = True
    return(collision)

def droiteOn(event):
    global u,sens
    sens="droite"
    u=7

def droiteOff(event):
    global u
    u=0

def gaucheOn(event):
    global u,sens
    sens="gauche"
    u=-7

def gaucheOff(event):
    global u
    u=0

def saut(event):
    global v,sens,NbSaut0

    if sautP2 == True:
        v = -15
        NbSaut0 = NbSaut0 - 1
        sautMax0()

def frapper(event):
    global sens

    coord = canvas1.coords(personnage)

    if sens=="normal":
        canvas1.coords(zone_hitbox, coord[0]+20, coord[1]-10)
        canvas1.itemconfig(zone_hitbox, state="normal")

    if sens=="droite":
        canvas1.coords(zone_hitbox, coord[0]+30, coord[1]-10)
        canvas1.itemconfig(zone_hitbox, state="normal")

    if sens=="gauche":
        canvas1.coords(zone_hitbox, coord[0]-50, coord[1]-10)
        canvas1.itemconfig(zone_hitbox, state="normal")

    degat()

def frapperOff(event):
    canvas1.itemconfig(zone_hitbox, state="hidden")
    canvas1.coords(zone_hitbox1, -50, -50)

def droiteOn1(event):
    global w,sens1
    sens1="droite"
    w=7

def droiteOff1(event):
    global w
    w=0

def gaucheOn1(event):
    global w,sens1
    sens1="gauche"
    w=-7

def gaucheOff1(event):
    global w
    w=0

def saut1(event):
    global k,sens1,NbSaut

    if sautP1 == True:
        k=-15
        NbSaut = NbSaut - 1
        sautMax()

def frapper1(event):
    global sens1

    coord1 = canvas1.coords(personnage1)

    if sens1=="normal":
        canvas1.coords(zone_hitbox1, coord1[0]-50, coord1[1]-10)
        canvas1.itemconfig(zone_hitbox1, state="normal")

    if sens1=="droite":
        canvas1.coords(zone_hitbox1, coord1[0]+30, coord1[1]-10)
        canvas1.itemconfig(zone_hitbox1, state="normal")

    if sens1=="gauche":
        canvas1.coords(zone_hitbox1, coord1[0]-50, coord1[1]-10)
        canvas1.itemconfig(zone_hitbox1, state="normal")

    degat()

def frapperOff1(event):
    canvas1.itemconfig(zone_hitbox1, state="hidden")
    canvas1.coords(zone_hitbox1, -50, -50)

def sautMax0():
    global NbSaut0,sautP2

    if NbSaut0 == 0:
        sautP2 = False

def sautMax():
    global NbSaut,sautP1

    if NbSaut == 0:
        sautP1 = False

def perteVie1():
    global NbVie1

    if NbVie1 == 2:
        canvas1.itemconfig(VP13, state="hidden" )

    if NbVie1 == 1:
        canvas1.itemconfig(VP12, state="hidden" )

    if NbVie1 == 0:
        canvas1.itemconfig(VP11, state="hidden" )
        retourjouer()

def perteVie2():
    global NbVie2

    if NbVie2 == 2:
        canvas1.itemconfig(VP23, state="hidden" )

    if NbVie2 == 1:
        canvas1.itemconfig(VP22, state="hidden" )

    if NbVie2 == 0:
        canvas1.itemconfig(VP21, state="hidden" )
        retourjouer()

def affichage():
    global degat_perso0,degat_perso1

    canvas1.itemconfig(txt1, text=(degat_perso1,"PV") )
    canvas1.itemconfig(txt, text=(degat_perso0,"PV") )

def degat():
    global degat_perso0,degat_perso1
    global NbVie1,NbVie2

    coord = canvas1.coords(personnage)
    coord1 = canvas1.coords(personnage1)

    coord3 = canvas1.coords(zone_hitbox)
    coord4 = canvas1.coords(zone_hitbox1)

    if coord3[0] < coord1[0] < coord3[0] + 50 and coord3[1] < coord1[1] < coord3[1] + 50:
        random0 = random.randint(28, 38)
        degat_perso1 = degat_perso1 - random0
        if degat_perso1 < 0:
            canvas1.coords(personnage1,960,45)
            NbVie2 = NbVie2 - 1
            degat_perso1 = 200
            perteVie2()
        affichage()

    if coord4[0] < coord[0] < coord4[0] + 50 and coord4[1] < coord[1] < coord4[1] + 50:
        random1 = random.randint(28, 38)
        degat_perso0 = degat_perso0 - random1
        if degat_perso0 < 0:
            canvas1.coords(personnage,100,45)
            NbVie1 = NbVie1 - 1
            degat_perso0 = 200
            perteVie1()
        affichage()

def mouvement():
    global u,v,sens
    global w,k,sens1
    global NbVie1,NbVie2
    global sautP1,NbSaut
    global sautP2,NbSaut0
    global PerteVie

    coord = canvas1.coords(personnage)
    coord1 = canvas1.coords(personnage1)

    v+=1
    k+=1

    if -200 < coord[0] < -100 and -40 < coord[1] < 760:
        canvas1.coords(personnage,100,45)
        NbVie1 = NbVie1 - 1
        perteVie1()
    if 0 < coord[0] < 720 and -200 < coord[1] < -100:
        canvas1.coords(personnage,100,45)
        NbVie1 = NbVie1 - 1
        perteVie1()
    if -300 < coord[0] < 1380 and 760 < coord[1] < 860:
        canvas1.coords(personnage,100,45)
        NbVie1 = NbVie1 - 1
        perteVie1()
    if 1240 < coord[0] < 1260 and -100 < coord[1] < 860:
        canvas1.coords(personnage,100,45)
        NbVie1 = NbVie1 - 1
        perteVie1()

    if -200 < coord1[0] < -100 and -40 < coord1[1] < 760:
        canvas1.coords(personnage1,960,45)
        NbVie2 = NbVie2 - 1
        perteVie2()
    if 0 < coord1[0] < 720 and -200 < coord1[1] < -100:
        canvas1.coords(personnage1,980,45)
        NbVie2 = NbVie2 - 1
        perteVie2()
    if -300 < coord1[0] < 1380 and 760 < coord1[1] < 860:
        canvas1.coords(personnage1,960,45)
        NbVie2 = NbVie2 - 1
        perteVie2()
    if 1240 < coord1[0] < 1260 and -100 < coord1[1] < 860:
        canvas1.coords(personnage1,960,45)
        NbVie2 = NbVie2 - 1
        perteVie2()

    collisionVertical = verifCollision(0,v)
    collisionHorizontal = verifCollision(u,0)
    if collisionVertical==True :
        v=0
        sautP2 = True
        NbSaut0 = 2
    if collisionHorizontal==True:
        u=0
    canvas1.move(personnage,u,v)

    collisionVertical1 = verifCollision1(0,k)
    collisionHorizontal1 = verifCollision1(w,0)
    if collisionVertical1==True :
        k=0
        sautP1 = True
        NbSaut = 2
    if collisionHorizontal1==True:
        w=0
    canvas1.move(personnage1,w,k)

    F.after(20,mouvement)

def terrain1():
    global listeBloc
    fichier = open("niveau1.txt", "r+")
    x=0
    y=0
    for rang in fichier:
        for caractere in rang:
            if caractere=="G":
                bloc = canvas1.create_image(x,y,image=platGauche,anchor="nw")
                listeBloc.append(bloc)
            if caractere=="M":
                bloc  = canvas1.create_image(x,y,image=platMilieu,anchor="nw")
                listeBloc.append(bloc)
            if caractere=="D":
                bloc = canvas1.create_image(x,y,image=platDroite,anchor="nw")
                listeBloc.append(bloc)
            x = x+21
        x = 0
        y = y+21
    fichier.close()

def BJM(event):
    if (0 < event.x < 40) and (0 < event.y < 40):
        canvas1.itemconfig(Back12, state="normal")
    else:
        canvas1.itemconfig(Back12, state="hidden")

def BJB(event):
    if (0 < event.x < 40) and (0 < event.y < 40):
        retourjouer()

def retourjouer():
    global PlayerOne,PlayerTwo
    global BoutonB1,BoutonR1,BoutonB2,BoutonR2,BoutonB3,BoutonR3
    global PassageGauche, PassageDroite
    global Fin
    global DovahJ1,DovahJ2,WitcherJ1,WitcherJ2

    canvas1.itemconfig(PourcentPersoDovahRouge, state="hidden")
    canvas1.itemconfig(PourcentPersoDovahBleu, state="hidden")
    canvas1.itemconfig(PourcentPersoWitcherRouge, state="hidden")
    canvas1.itemconfig(PourcentPersoWitcherBleu, state="hidden")

    canvas1.forget()
    canvas.pack()

    PlayerOne = True
    PlayerTwo = False

    PassageGauche = False
    PassageDroite = False

    BoutonB1 = False
    BoutonR1 = False
    BoutonB2 = False
    BoutonR2 = False
    BoutonB3 = False
    BoutonR3 = False

    Fin = False

    DovahJ1 = False
    DovahJ2 = False
    WitcherJ1 = False
    WitcherJ2 = False

    Jouer()
##################################################################################################################

def DLC():
    if askyesno('DLC', "Pour pouvoir accÃƒÂ©der ÃƒÂ  ce continu, il faut possÃƒÂ©der l'ÃƒÂ©dition Game Of The Year. Voulez-vous la possÃƒÂ©der?"):
        webbrowser.open('https://store.steampowered.com/app/813630/Supraland/')

def Retour_Menu_Principal():
    global PlayerOne,PlayerTwo
    global BoutonB1,BoutonR1,BoutonB2,BoutonR2,BoutonB3,BoutonR3
    global PassageGauche, PassageDroite
    global Fin

    canvas.itemconfig(Back1, state="hidden")
    canvas.itemconfig(Banniere_Back_1, state="hidden")
    canvas.itemconfig(Fond_MN, state="normal")
    canvas.itemconfig(Fond_J, state="hidden")
    canvas.itemconfig(Fond_O, state="hidden")

    F.geometry("1080x720")

    canvas.bind('<Motion>',Bouton_Passage_MN)
    canvas.bind('<Button-1>',Bouton_Pression_MN)

    PlayerOne = True
    PlayerTwo = False

    PassageGauche = False
    PassageDroite = False

    BoutonB1 = False
    BoutonR1 = False
    BoutonB2 = False
    BoutonR2 = False
    BoutonB3 = False
    BoutonR3 = False

    Fin = False

def Jouer():
    canvas.itemconfig(Fond_MN, state="hidden")
    canvas.itemconfig(Fond_J, state="normal")

    canvas.bind('<Motion>',B)
    canvas.bind('<Button-1>',Bouton_Pression_J)

    retirer()

def Option():
    canvas.itemconfig(Fond_MN, state="hidden")
    canvas.itemconfig(Fond_O, state="normal")

    canvas.bind('<Motion>',Bouton_Passage_Option)
    canvas.bind('<Button-1>',Bouton_Pression_Option)

    retirer()

def Editeur_De_Niveau():
    canvas.itemconfig(Fond_MN, state="hidden")

    F.geometry("1110x720")
    canvas.forget()
    fond.pack()

    fond.itemconfig(AQW, state= "normal")
    fond.itemconfig(QSD, state= "normal")
    fond.itemconfig(Banniere_Back_0, state= "normal")

    fond.bind('<Motion>',Bouton_Passage_Editeur_De_Niveau)
    fond.bind("<Button 1>",cordsouris)
    terrain()

    retirer()

def Quitter():
    if askyesno("Quitter", 'r de vouloir faire  ?'):
        F.destroy()

def retirer():
    canvas.itemconfig(Bouton_Passage_J, state="hidden")
    canvas.itemconfig(Bouton_Passage_O, state="hidden")
    canvas.itemconfig(Bouton_Passage_Q, state="hidden")

def B (event):
    global PlayerOne,PlayerTwo
    global BoutonB1,BoutonR1,BoutonB2,BoutonR2,BoutonB3,BoutonR3
    global PassageGauche, PassageDroite
    global Fin

    if (331 < event.x < 445) and (350 < event.y < 393):
        if PlayerOne == True:
            canvas.itemconfig(Bouton_Haut_Bleu_Gauche, state="normal")
            canvas.itemconfig(Perso_Gauche_0, state="normal")
        if PlayerTwo == True:
            if Fin == False:
                if BoutonB1 == True:
                     canvas.itemconfig(B__D__R__G, state="normal")
                else:
                    canvas.itemconfig(Bouton_Haut_Rouge_Gauche, state="normal")
                canvas.itemconfig(Perso_Droite_0, state="normal")
    elif (485 < event.x < 596) and (350 < event.y < 393):
        if PlayerOne == True:
            canvas.itemconfig(Bouton_Haut_Millieu_Bleu, state="normal")
            canvas.itemconfig(Perso_Gauche_1, state="normal")
        if PlayerTwo == True:
            if Fin == False:
                if BoutonB2 == True:
                     canvas.itemconfig(B__D__R__C, state="normal")
                else:
                    canvas.itemconfig(Bouton_Haut_Millieu_Rouge, state="normal")
                canvas.itemconfig(Perso_Droite_1, state="normal")
    elif (627 < event.x < 769) and (350 < event.y < 393):
        if PlayerOne == True:
            canvas.itemconfig(Bouton_Haut_Droite_Bleu, state="normal")
            canvas.itemconfig(Perso_Gauche_2, state="normal")
        if PlayerTwo == True:
            if Fin == False:
                canvas.itemconfig(Bouton_Haut_Droite_Rouge, state="normal")
                canvas.itemconfig(Perso_Droite_2, state="normal")

    elif (342 < event.x < 446) and (427 < event.y < 473):
        if PlayerOne == True:
            canvas.itemconfig(Bouton_Centre_Bleu_Gauche, state="normal")
            canvas.itemconfig(Perso_Gauche_2, state="normal")
        if PlayerTwo == True:
            if Fin == False:
                canvas.itemconfig(Bouton_Centre_Rouge_Gauche, state="normal")
                canvas.itemconfig(Perso_Droite_2, state="normal")
    elif (485 < event.x < 596) and (427 < event.y < 473):
        if PlayerOne == True:
            canvas.itemconfig(Bouton_Centre_Millieu_Bleu, state="normal")
            canvas.itemconfig(Perso_Gauche_2, state="normal")
        if PlayerTwo == True:
            if Fin == False:
                canvas.itemconfig(Bouton_Centre_Millieu_Rouge, state="normal")
                canvas.itemconfig(Perso_Droite_2, state="normal")
    elif (636 < event.x < 744) and (427 < event.y < 473):
        if PlayerOne == True:
            canvas.itemconfig(Bouton_Centre_Droite_Bleu, state="normal")
            canvas.itemconfig(Perso_Gauche_2, state="normal")
        if PlayerTwo == True:
            if Fin == False:
                canvas.itemconfig(Bouton_Centre_Droite_Rouge, state="normal")
                canvas.itemconfig(Perso_Droite_2, state="normal")

    elif (349 < event.x < 445) and (507 < event.y < 551):
        if PlayerOne == True:
            canvas.itemconfig(Bouton_Bas_Gauche_Bleu, state="normal")
            canvas.itemconfig(Perso_Gauche_2, state="normal")
        if PlayerTwo == True:
            if Fin == False:
                canvas.itemconfig(Bouton_Bas_Gauche_Rouge, state="normal")
                canvas.itemconfig(Perso_Droite_2, state="normal")
    elif (485 < event.x < 596) and (506 < event.y < 551):
        if PlayerOne == True:
            canvas.itemconfig(Bouton_Bas_Millieu_Bleu, state="normal")
            canvas.itemconfig(Perso_Gauche_2, state="normal")
        if PlayerTwo == True:
            if Fin == False:
                canvas.itemconfig(Bouton_Bas_Millieu_Rouge, state="normal")
                canvas.itemconfig(Perso_Droite_2, state="normal")
    elif (636 < event.x < 734) and (505 < event.y < 550):
        if PlayerOne == True:
            canvas.itemconfig(Bouton_Bas_Droite_Bleu, state="normal")
            canvas.itemconfig(Perso_Gauche_2, state="normal")
        if PlayerTwo == True:
            if Fin == False:
                canvas.itemconfig(Bouton_Bas_Droite_Rouge, state="normal")
                canvas.itemconfig(Perso_Droite_2, state="normal")

    elif (358 < event.x < 722) and (602 < event.y < 689):
        if Fin == True:
            canvas.itemconfig(Bouton__Jouez, state="normal")
    elif (20 < event.x < 52) and (2 < event.y < 38):
        canvas.itemconfig(Back1, state="normal")

    else:
        if BoutonB1 == False:
            canvas.itemconfig(Bouton_Haut_Bleu_Gauche, state="hidden")
            canvas.itemconfig(Perso_Gauche_0, state="hidden")
        if BoutonR1 == False:
            canvas.itemconfig(Bouton_Haut_Rouge_Gauche, state="hidden")
            canvas.itemconfig(B__D__R__G, state="hidden")
            canvas.itemconfig(Perso_Droite_0, state="hidden")
        if BoutonB2 == False:
            canvas.itemconfig(Bouton_Haut_Millieu_Bleu, state="hidden")
            canvas.itemconfig(Perso_Gauche_1, state="hidden")
        if BoutonR2 == False:
            canvas.itemconfig(Bouton_Haut_Millieu_Rouge, state="hidden")
            canvas.itemconfig(B__D__R__C, state="hidden")
            canvas.itemconfig(Perso_Droite_1, state="hidden")
        if BoutonB3 == False:
            canvas.itemconfig(Bouton_Haut_Droite_Bleu, state="hidden")
            canvas.itemconfig(Perso_Gauche_2, state="hidden")
        if BoutonR3 == False:
            canvas.itemconfig(Bouton_Haut_Droite_Rouge, state="hidden")
            canvas.itemconfig(B__D__R__D, state="hidden")
            canvas.itemconfig(Perso_Droite_2, state="hidden")

        canvas.itemconfig(Bouton_Centre_Bleu_Gauche, state="hidden")
        canvas.itemconfig(Bouton_Centre_Rouge_Gauche, state="hidden")
        canvas.itemconfig(Bouton_Centre_Millieu_Bleu, state="hidden")
        canvas.itemconfig(Bouton_Centre_Millieu_Rouge, state="hidden")
        canvas.itemconfig(Bouton_Centre_Droite_Bleu, state="hidden")
        canvas.itemconfig(Bouton_Centre_Droite_Rouge, state="hidden")

        canvas.itemconfig(Bouton_Bas_Gauche_Bleu, state="hidden")
        canvas.itemconfig(Bouton_Bas_Gauche_Rouge, state="hidden")
        canvas.itemconfig(Bouton_Bas_Millieu_Bleu, state="hidden")
        canvas.itemconfig(Bouton_Bas_Millieu_Rouge, state="hidden")
        canvas.itemconfig(Bouton_Bas_Droite_Bleu, state="hidden")
        canvas.itemconfig(Bouton_Bas_Droite_Rouge, state="hidden")

        canvas.itemconfig(Bouton__Jouez, state="hidden")
        canvas.itemconfig(Back1, state="hidden")

    if PlayerOne == True:
        canvas.coords(J_1, event.x + 10, event.y + 10)
        canvas.itemconfig(J_1, state="normal")
    if PlayerTwo == True:
        if Fin == False:
            canvas.coords(J_2, event.x + 10, event.y + 10)
            canvas.itemconfig(J_2, state="normal")

def Bouton_Pression_J(event):
    global PlayerOne,PlayerTwo
    global BoutonB1,BoutonR1,BoutonB2,BoutonR2,BoutonB3,BoutonR3
    global PassageGauche, PassageDroite
    global Fin
    global DovahJ1,DovahJ2,WitcherJ1,WitcherJ2

    if (331 < event.x < 445) and (350 < event.y < 393):
        if PlayerOne == True:
            BoutonB1 = True
            canvas.itemconfig(B__D__R__G, state="normal")
            canvas.itemconfig(Perso_Droite_0, state="normal")
            canvas.itemconfig(J_1 , state="hidden")
            canvas.itemconfig(J_2 , state="normal")
            canvas.coords(J_2, event.x + 10, event.y + 10)
            DovahJ1 = True
        if PlayerTwo == True:
            BoutonR1 = True
            Fin = True
            canvas.itemconfig(J_1 , state="hidden")
            canvas.itemconfig(J_2 , state="hidden")
            DovahJ2 = True
        PlayerOne = False
        PlayerTwo = True
    if (485 < event.x < 596) and (350 < event.y < 393):
        if PlayerOne == True:
            BoutonB2 = True
            canvas.itemconfig(B__D__R__C, state="normal")
            canvas.itemconfig(Perso_Droite_1, state="normal")
            canvas.itemconfig(J_1 , state="hidden")
            canvas.itemconfig(J_2 , state="normal")
            canvas.coords(J_2, event.x + 10, event.y + 10)
            WitcherJ1 = True
        if PlayerTwo == True:
            BoutonR2 = True
            Fin = True
            canvas.itemconfig(J_1 , state="hidden")
            canvas.itemconfig(J_2 , state="hidden")
            WitcherJ2 = True
        PlayerOne = False
        PlayerTwo = True
    if (627 < event.x < 769) and (350 < event.y < 393):
        if Fin == False:
            DLC()
    if (342 < event.x < 446) and (427 < event.y < 473):
        if Fin == False:
            DLC()
    if (485 < event.x < 596) and (427 < event.y < 473):
        if Fin == False:
            DLC()
    if (636 < event.x < 744) and (427 < event.y < 773):
        if Fin == False:
            DLC()
    if (349 < event.x < 445) and (507 < event.y < 551):
        if Fin == False:
            DLC()
    if (485 < event.x < 596) and (506 < event.y < 551):
        if Fin == False:
            DLC()
    if (636 < event.x < 734) and (505 < event.y < 550):
        if Fin == False:
            DLC()
    if (20 < event.x < 52) and (2 < event.y < 38):
        canvas.itemconfig(Bouton_Haut_Bleu_Gauche, state="hidden")
        canvas.itemconfig(Perso_Gauche_0, state="hidden")

        canvas.itemconfig(Bouton_Haut_Rouge_Gauche, state="hidden")
        canvas.itemconfig(B__D__R__G, state="hidden")
        canvas.itemconfig(Perso_Droite_0, state="hidden")

        canvas.itemconfig(Bouton_Haut_Millieu_Bleu, state="hidden")
        canvas.itemconfig(Perso_Gauche_1, state="hidden")

        canvas.itemconfig(Bouton_Haut_Millieu_Rouge, state="hidden")
        canvas.itemconfig(B__D__R__C, state="hidden")
        canvas.itemconfig(Perso_Droite_1, state="hidden")

        canvas.itemconfig(Bouton_Haut_Droite_Bleu, state="hidden")
        canvas.itemconfig(Perso_Gauche_2, state="hidden")

        canvas.itemconfig(Bouton_Haut_Droite_Rouge, state="hidden")
        canvas.itemconfig(B__D__R__D, state="hidden")
        canvas.itemconfig(Perso_Droite_2, state="hidden")

        canvas.itemconfig(Bouton_Centre_Bleu_Gauche, state="hidden")
        canvas.itemconfig(Bouton_Centre_Rouge_Gauche, state="hidden")
        canvas.itemconfig(Bouton_Centre_Millieu_Bleu, state="hidden")
        canvas.itemconfig(Bouton_Centre_Millieu_Rouge, state="hidden")
        canvas.itemconfig(Bouton_Centre_Droite_Bleu, state="hidden")
        canvas.itemconfig(Bouton_Centre_Droite_Rouge, state="hidden")

        canvas.itemconfig(Bouton_Bas_Gauche_Bleu, state="hidden")
        canvas.itemconfig(Bouton_Bas_Gauche_Rouge, state="hidden")
        canvas.itemconfig(Bouton_Bas_Millieu_Bleu, state="hidden")
        canvas.itemconfig(Bouton_Bas_Millieu_Rouge, state="hidden")
        canvas.itemconfig(Bouton_Bas_Droite_Bleu, state="hidden")
        canvas.itemconfig(Bouton_Bas_Droite_Rouge, state="hidden")

        canvas.itemconfig(Bouton__Jouez, state="hidden")
        canvas.itemconfig(Back1, state="hidden")

        canvas.itemconfig(J_1, state="hidden")
        canvas.itemconfig(J_2, state="hidden")

        Retour_Menu_Principal()

    if (358 < event.x < 722) and (602 < event.y < 689):
        if Fin == True:
            LOL()

def Bouton_Pression_Option(event):
    if (0 < event.x < 40) and (0 < event.y < 40):
        canvas.itemconfig(Back1, state="normal")
        Retour_Menu_Principal()

def Bouton_Passage_Option(event):
    if (0 < event.x < 40) and (0 < event.y < 40):
        canvas.itemconfig(Back1, state="normal")
    else:
        canvas.itemconfig(Back1, state="hidden")

def Bouton_Passage_MN(event):
    if (35 < event.x < 200) and (300 < event.y < 360):
        canvas.itemconfig(Bouton_Passage_J, state= "normal")
    else:
        canvas.itemconfig(Bouton_Passage_J, state= "hidden")

    if (37 < event.x < 230) and (383 < event.y < 445):
        canvas.itemconfig(Bouton_Passage_O, state= "normal")
    else:
        canvas.itemconfig(Bouton_Passage_O, state= "hidden")

    if (33 < event.x < 495) and (470 < event.y < 528):
        canvas.itemconfig(Bouton_Passage_EN, state= "normal")
    else:
        canvas.itemconfig(Bouton_Passage_EN, state= "hidden")

    if (34 < event.x < 278) and (553 < event.y < 612):
        canvas.itemconfig(Bouton_Passage_Q, state= "normal")
    else:
        canvas.itemconfig(Bouton_Passage_Q, state= "hidden")

def Bouton_Pression_MN(event):
    if (35 < event.x < 200) and (300 < event.y < 360):
        Jouer()

    if (37 < event.x < 230) and (383 < event.y < 445):
        Option()

    if (33 < event.x < 495) and (470 < event.y < 528):
        Editeur_De_Niveau()

    if (34 < event.x < 278) and (553 < event.y < 612):
        canvas.itemconfig(Bouton_Passage_Q, state="hidden")
        Quitter()

###########################################################################################################################################################################################################################################
def Bouton_Pression_Editeur_De_Niveau():
    fond.forget()
    canvas.pack()
    Retour_Menu_Principal()

def Bouton_Passage_Editeur_De_Niveau(event):
    global POS

    if (0 < event.x < 40) and (0 < event.y < 40):
        fond.itemconfig(Back2, state="normal")
    elif (0 < event.x < 1080) and (0 < event.y < 66):
        POS = False
    else:
        fond.itemconfig(Back2, state="hidden")
        POS = True

def changeBloc(bloc):
    global typeBloc
    typeBloc = bloc

def boutonEnfonce(bouton) :
    bloc1.config(bg=couleurB)
    bloc2.config(bg=couleurB)
    bloc3.config(bg=couleurB)
    bloc4.config(bg="red")
    bouton.config(bg="white")

def cordsouris(cord):
    global POS

    x0 = cord.x
    y0 = cord.y
    x1 = 0
    x2 = 22
    y1 = 0
    y2 = 22
    testx = False
    testy = False
    colonne = 0
    ligne = 0
    if POS == True:
        while testx == False:
            if x1 < x0 < x2:
                testx = True
                colonne = colonne + 1
            else:
                colonne = colonne + 1
                x1 = x1+21
                x2 = x2+21

        while testy == False:
            if y1 < y0 < y2:
                testy = True
                ligne = ligne + 1
            else:
                ligne = ligne + 1
                y1 = y1+21
                y2 = y2+21
        modif_fichiertexte(ligne,colonne)

    if (0 < x0 < 40) and (0 < y0 < 40):
        Bouton_Pression_Editeur_De_Niveau()

def modif_fichiertexte(ligne,colonne):
    global fichier
    nb = 0
    fichier = open("niveau1.txt","r")
    with open("temp.txt","w") as temp:
        for rang in fichier:
            nb = nb+1
            if (ligne==nb): text = '%s%s%s'%(rang[:colonne-1],typeBloc,rang[colonne:])
            else : text = rang
            temp.write(text)
    fichier.close()
    os.remove("niveau1.txt")
    os.rename("temp.txt","niveau1.txt")
    terrain()

def terrain():
    fichier = open("niveau1.txt", "r+")
    x=0
    y=0
    for rang in fichier:
        for caractere in rang:
            if caractere=="S":
                fond.delete(fond.find_closest(x,y))
                changeBloc("V")
                caractere = "V"
                fichier.close()
                modif_fichiertexte(ligne,colonne)
            if caractere=="G":
                fond.create_image(x,y,image=platGauche,anchor="nw")
            if caractere=="M":
                fond.create_image(x,y,image=platMilieu,anchor="nw")
            if caractere=="D":
                fond.create_image(x,y,image=platDroite,anchor="nw")
            x = x+21
        x = 0
        y = y+21
    fichier.close()

F = Tk()
F.geometry("1080x720")

Menu_Principal = PhotoImage( file="Menu_Principal2.png" )
Editeur_Fond = PhotoImage( file="AH.png" )
Az = PhotoImage( file="FondCredits.png" )
Bouton = PhotoImage( file="back.png" )
Bouton1 = PhotoImage( file="Bouton_Jouer.png" )
Bouton2 = PhotoImage( file="Bouton_Option.png" )
Bouton3 = PhotoImage( file="Bouton_Editeur_De_Niveau.png" )
Bouton4 = PhotoImage( file="Bouton_Quitter.png" )
Baniere_Back = PhotoImage( file="cc.png" )
Baniere_Back0 = PhotoImage( file="cc1.png" )
Back = PhotoImage( file="back.png" )

Jouer_Fond = PhotoImage( file="AH.png")
Joueur_1 = PhotoImage( file="P_1.png")
Joueur_2 = PhotoImage( file="P_2.png")

BoutonMillieuBleu = PhotoImage( file="B_C_B.png")
BoutonMillieuRouge = PhotoImage( file="B_C_R.png")

BoutonHautBleuGauche = PhotoImage( file="B_H_B_G.png")
BoutonHautRougeGauche = PhotoImage( file="B_H_R_G.png")
BoutonHautBleuDroite = PhotoImage( file="B_H_B_D.png")
BoutonHautRougeDroite = PhotoImage( file="B_H_R_D.png")

BoutonCentreBleuGauche = PhotoImage( file="B_C_D_G.png")
BoutonCentreRougeGauche = PhotoImage( file="B_C_R_G.png")
BoutonCentreBleuDroite = PhotoImage( file="B_C_D_B.png")
BoutonCentreRougeDroite = PhotoImage( file="B_C_R_D.png")

BoutonBasBleuGauche = PhotoImage( file="B_B_G_B.png")
BoutonBasRougeGauche = PhotoImage( file="B_B_G_R.png")
BoutonBasBleuDroite = PhotoImage( file="B_B_D_B.png")
BoutonBasRougeDroite = PhotoImage( file="B_B_D_R.png")

B_D_R_G = PhotoImage( file="BDRG.png")
B_D_R_C = PhotoImage( file="BDRC.png")
B_D_R_D = PhotoImage( file="BDRD.png")

Perso_Gauche = PhotoImage( file="PersoGauche.png")
Perso_Gauche1 = PhotoImage( file="PersoGauche1.png")
Perso_Gauche2 = PhotoImage( file="PersoGauche2.png")
Perso_Droite = PhotoImage( file="PersoDroite.png")
Perso_Droite1 = PhotoImage( file="PersoDroite1.png")
Perso_Droite2 = PhotoImage( file="PersoDroite2.png")

Bouton_Jouez = PhotoImage( file="BoutonJouez.png")

bgImage = PhotoImage(file="Greenbg.png")

largeur = 1080
hauteur = 720
canvas = Canvas(F, width = largeur , height = hauteur)
canvas1 = Canvas(F, width = largeur , height = hauteur)
fond = Canvas(F ,width=1110,height=720)

#############################################################################################################
AQW = fond.create_image(0,0,image=bgImage,anchor="nw" , state = "hidden")
AQW1 = canvas1.create_image(0,0,image=bgImage,anchor="nw" , state = "hidden")
QSD = fond.create_rectangle(1080,0,1111,720,fill="black", state = "hidden")

platGauche = PhotoImage(file="platGauche.png")
platMilieu = PhotoImage(file="platMilieu.png")
platDroite = PhotoImage(file="platDroite.png")

couleurB = "black"
global typeBloc

bloc1 = Button(F,image=platGauche,height=21,width=21,relief=FLAT,bg=couleurB,command=lambda : [changeBloc("G"),boutonEnfonce(bloc1)])
bloc1.forget()
bloc2 = Button(F,image=platMilieu,height=21,width=21,relief=FLAT,bg=couleurB,command=lambda : [changeBloc("M"),boutonEnfonce(bloc2)])
bloc2.forget()
bloc3 = Button(F,image=platDroite,height=21,width=21,relief=FLAT,bg=couleurB,command=lambda : [changeBloc("D"),boutonEnfonce(bloc3)])
bloc3.forget()
bloc4 = Button(F,height=1,width=21,relief=FLAT,bg="red",command=lambda : [changeBloc("S"),boutonEnfonce(bloc4)])
bloc4.forget()

bloc1.place(x=1082,y=10+50)
bloc2.place(x=1082,y=41+50)
bloc3.place(x=1082,y=72+50)
bloc4.place(x=1082,y=103+50)

ligne = 0
colonne = 0
POS = False
#############################################################################################################

global listeBloc
global u,v,personnage,sens
global x,y,personnage1,sens1

position = 0
sens = "normal"
sens1 = "normal"
listeBloc = []

perso = PhotoImage(file="personnage.png")
perso1 = PhotoImage(file="personnage1.png")
hitbox = PhotoImage(file="La_Hitbox.png")
hitbox1 = PhotoImage(file="La_Hitbox.png")
PourcentP1 = PhotoImage(file="DegatPerso1.png")
PourcentP2 = PhotoImage(file="DegatPerso2.png")
PourcentP3 = PhotoImage(file="DegatPP1.png")
PourcentP4 = PhotoImage(file="DegatPP2.png")
VieP1 = PhotoImage(file="VieP1.1.png")
VieP2 = PhotoImage(file="VieP2.1.png")
Banniere = PhotoImage(file="cc.png")

personnage = canvas1.create_image(100,45,image=perso,anchor="nw",state="hidden")
personnage1 = canvas1.create_image(980,45,image=perso1,anchor="nw",state="hidden")

PourcentPersoDovahRouge = canvas1.create_image(161-175+40,520,image=PourcentP1,anchor="nw",state="hidden")
PourcentPersoDovahBleu = canvas1.create_image(580+40,498,image=PourcentP2,anchor="nw",state="hidden")
PourcentPersoWitcherRouge = canvas1.create_image(-110,351,image=PourcentP4,anchor="nw",state="hidden")
PourcentPersoWitcherBleu = canvas1.create_image(456+40,352,image=PourcentP3,anchor="nw",state="hidden")

zone_hitbox = canvas1.create_image(-250,-250,image=hitbox,anchor="nw",state="hidden")
zone_hitbox1 = canvas1.create_image(-250,-250,image=hitbox1,anchor="nw",state="hidden")

coord = canvas1.coords(personnage)
coord1 = canvas1.coords(personnage1)

txt = canvas1.create_text(375-135+40, 590, text="", font="Arial 60", fill="red",state="hidden")
txt1 = canvas1.create_text(845+40, 590, text="", font="Arial 60", fill="blue",state="hidden")

VP11 = canvas1.create_image(186-75-60,647,image=VieP1,anchor="nw",state="hidden")
VP12 = canvas1.create_image(201-75-60,647,image=VieP1,anchor="nw",state="hidden")
VP13 = canvas1.create_image(216-75-60,647,image=VieP1,anchor="nw",state="hidden")

VP21 = canvas1.create_image(720-60,647,image=VieP2,anchor="nw",state="hidden")
VP22 = canvas1.create_image(735-60,647,image=VieP2,anchor="nw",state="hidden")
VP23 = canvas1.create_image(750-60,647,image=VieP2,anchor="nw",state="hidden")

BannierB = canvas1.create_image(2,0,image=Banniere,anchor="nw",state="hidden")
Back12 = canvas1.create_image( 37,20 , image=Back , state = "hidden")


u=0
v=0

w=0
k=0

degat_perso0 = 0
degat_perso1 = 0

NbVie1 = 3
NbVie2 = 3

NbSaut0 = 2
NbSaut = 2

sautP1 = True
sautP2 = True

PerteVie = False
Invincibilite = False

g = 9.8
delta = float(70)
Vo = float(3)

#############################################################################################################

Fond_MN = canvas.create_image( 0 , 0 , image=Menu_Principal , anchor="nw")
Fond_J = canvas.create_image( 0 , 0 , image=Jouer_Fond , anchor="nw" , state = "hidden"  )
Fond_O = canvas.create_image( 0 , 0 , image=Az , anchor="nw" , state = "hidden"  )

Bouton_Passage_J = canvas.create_image( 117.5 , 330 , image=Bouton1 , state = "hidden")
Bouton_Passage_O = canvas.create_image( 88 , 373 , image=Bouton2 , state = "hidden")
Bouton_Passage_EN = canvas.create_image( 264 , 499 , image=Bouton3 , state = "hidden")
Bouton_Passage_Q = canvas.create_image( 156 , 582.5 , image=Bouton4 , state = "hidden")
Bouton_Passage_B = canvas.create_image( -40 , 0 , image=Bouton , state = "hidden")
Bouton_Passage_B1 = fond.create_image( -40 , 0 , image=Bouton , state = "hidden")
Banniere_Back_1 = canvas.create_image( 540,362 , image=Baniere_Back , state = "hidden")
Banniere_Back_0 = fond.create_image( 555,362 , image=Baniere_Back0 , state = "hidden")
Back1 = canvas.create_image( 37,20 , image=Back , state = "hidden")
Back2 = fond.create_image( 37,20 , image=Back , state = "hidden")

Bouton_Haut_Millieu_Bleu = canvas.create_image( 542.5 , 353.5 , image=BoutonMillieuBleu , state="hidden")
Bouton_Haut_Millieu_Rouge = canvas.create_image( 542.5 , 353.5 , image=BoutonMillieuRouge , state="hidden")
Bouton_Centre_Millieu_Bleu = canvas.create_image( 542.5 , 432.5 , image=BoutonMillieuBleu , state="hidden")
Bouton_Centre_Millieu_Rouge = canvas.create_image( 542.5 , 432.5 , image=BoutonMillieuRouge , state="hidden")
Bouton_Bas_Millieu_Bleu = canvas.create_image( 542.5 , 511.5 , image=BoutonMillieuBleu , state="hidden")
Bouton_Bas_Millieu_Rouge = canvas.create_image( 542.5 , 511.5 , image=BoutonMillieuRouge , state="hidden")

Bouton_Haut_Bleu_Gauche = canvas.create_image( 388 , 366.5 , image=BoutonHautBleuGauche , state="hidden")
Bouton_Haut_Rouge_Gauche = canvas.create_image( 388 , 366.5 , image=BoutonHautRougeGauche , state="hidden")
Bouton_Haut_Droite_Bleu = canvas.create_image( 699 , 366.5 , image=BoutonHautBleuDroite , state="hidden")
Bouton_Haut_Droite_Rouge = canvas.create_image( 699 , 366.5 , image=BoutonHautRougeDroite , state="hidden")

Bouton_Centre_Bleu_Gauche = canvas.create_image( 388 , 434.5 , image=BoutonCentreBleuGauche , state="hidden")
Bouton_Centre_Rouge_Gauche = canvas.create_image( 388 , 434.5 , image=BoutonCentreRougeGauche , state="hidden")
Bouton_Centre_Droite_Bleu = canvas.create_image( 695 , 435 , image=BoutonCentreBleuDroite , state="hidden")
Bouton_Centre_Droite_Rouge = canvas.create_image( 696 , 435 , image=BoutonCentreRougeDroite , state="hidden")

Bouton_Bas_Gauche_Bleu = canvas.create_image( 398 , 513.5 , image=BoutonBasBleuGauche , state="hidden")
Bouton_Bas_Gauche_Rouge = canvas.create_image( 398 , 513.5 , image=BoutonBasRougeGauche , state="hidden")
Bouton_Bas_Droite_Bleu = canvas.create_image( 685 , 513.5 , image=BoutonBasBleuDroite , state="hidden")
Bouton_Bas_Droite_Rouge = canvas.create_image( 685 , 513.5 , image=BoutonBasRougeDroite , state="hidden")

B__D__R__G = canvas.create_image( 388 , 366.5 , image=B_D_R_G , state="hidden")
B__D__R__C = canvas.create_image( 542.5 , 353.5 , image=B_D_R_C , state="hidden")
B__D__R__D = canvas.create_image( 699 , 366.5 , image=B_D_R_D , state="hidden")

Perso_Gauche_0 = canvas.create_image( -340 , 0 , image=Perso_Gauche , state="hidden", anchor="nw")
Perso_Gauche_1 = canvas.create_image( -340 , 0 , image=Perso_Gauche1 , state="hidden", anchor="nw")
Perso_Gauche_2 = canvas.create_image( -340 , 0 , image=Perso_Gauche2 , state="hidden", anchor="nw")
Perso_Droite_0 = canvas.create_image( 1080+340 , 0 , image=Perso_Droite , state="hidden", anchor="ne")
Perso_Droite_1 = canvas.create_image( 1080+340 , 0 , image=Perso_Droite1 , state="hidden", anchor="ne")
Perso_Droite_2 = canvas.create_image( 1080+340 , 0 , image=Perso_Droite2 , state="hidden", anchor="ne")

Bouton__Jouez = canvas.create_image( 533.5 , 633.5 , image=Bouton_Jouez , state="hidden")
Back1 = canvas.create_image( 37,20 , image=Back , state = "hidden")

J_1 = canvas.create_image( -50 , -50 , image=Joueur_1 , anchor="nw" , state="hidden")
J_2 = canvas.create_image( 0 , 0 , image=Joueur_2 , anchor="nw" , state="hidden")

PlayerOne = True
PlayerTwo = False

PassageGauche = False
PassageDroite = False

BoutonB1 = False
BoutonR1 = False
BoutonB2 = False
BoutonR2 = False
BoutonB3 = False
BoutonR3 = False

Fin = False

DovahJ1 = False
DovahJ2 = False
WitcherJ1 = False
WitcherJ2 = False

firstgame = True

NbMap = 3
NbPassageMap = 1

canvas.bind('<Motion>',Bouton_Passage_MN)
canvas.bind('<Button-1>',Bouton_Pression_MN)

canvas.pack()
canvas1.forget()
fond.forget()

F.mainloop()
