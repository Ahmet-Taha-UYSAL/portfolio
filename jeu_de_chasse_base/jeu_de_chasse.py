'''######################################################################################
######################### jeu_de_chasse.py ##############################################
######################################################################################'''

############ import des modules #########################################################

import random 
import pygame 
import time 
import os
import math

########### initialisation de Pygame ####################################################

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Jeu de chasse")
clock = pygame.time.Clock()
pygame.joystick.init()
manette = None
if pygame.joystick.get_count() > 0:
    manette = pygame.joystick.Joystick(0)
    manette.init()
    print("Manette connectée :", manette.get_name())

########### chargement des images #######################################################

avion_niveau_1_1 = pygame.image.load("_internal/images/avions/avion_niveau_1_1.png").convert_alpha()
avion_niveau_1_2 = pygame.image.load("_internal/images/avions/avion_niveau_1_2.png").convert_alpha()
avion_niveau_1_3 = pygame.image.load("_internal/images/avions/avion_niveau_1_3.png").convert_alpha()
avion_niveau_2_1 = pygame.image.load("_internal/images/avions/avion_niveau_2_1.png").convert_alpha()
avion_niveau_2_2 = pygame.image.load("_internal/images/avions/avion_niveau_2_2.png").convert_alpha()
avion_niveau_2_3 = pygame.image.load("_internal/images/avions/avion_niveau_2_3.png").convert_alpha()
avion_final_boss = pygame.image.load("_internal/images/avions/final_boss.png").convert_alpha()
avion_mini_boss = pygame.image.load("_internal/images/avions/mini_boss.png").convert_alpha()
avion_bleu_base = pygame.image.load("_internal/images/avions/bleu.png").convert_alpha()
avion_rouge = pygame.image.load("_internal/images/avions/rouge.png").convert_alpha()
avion_rouge_base = pygame.image.load("_internal/images/avions/rouge.png").convert_alpha()

avion_niveau_2_1 = pygame.transform.scale(avion_niveau_2_1, (130, 130))
avion_niveau_2_2 = pygame.transform.scale(avion_niveau_2_2, (130, 130))
avion_niveau_2_3 = pygame.transform.scale(avion_niveau_2_3, (130, 130))
avion_mini_boss = pygame.transform.scale(avion_mini_boss, (200, 130))
avion_niveau_2_1 = pygame.transform.rotate(avion_niveau_2_1, 180)
avion_niveau_2_2 = pygame.transform.rotate(avion_niveau_2_2, 180)
avion_niveau_2_3 = pygame.transform.rotate(avion_niveau_2_3, 180)
avion_mini_boss = pygame.transform.rotate(avion_mini_boss, 180)
avion_final_boss = pygame.transform.scale(avion_final_boss, (500, 500))
avion_bleu = pygame.transform.scale(avion_bleu_base, (100, 100))
avion_bleu_classique = pygame.transform.scale(avion_bleu_base, (30, 30))
avion_rouge_classique = pygame.transform.scale(avion_rouge, (30, 30))
avion_rouge_base = pygame.transform.rotate(avion_rouge_base, 180)

barre_de_vie_120 = pygame.image.load("_internal/images/barre_de_vie/barre_de_vie_120.png").convert_alpha()
barre_de_vie_100 = pygame.image.load("_internal/images/barre_de_vie/barre_de_vie_100.png").convert_alpha()
barre_de_vie_80 = pygame.image.load("_internal/images/barre_de_vie/barre_de_vie_80.png").convert_alpha()
barre_de_vie_60 = pygame.image.load("_internal/images/barre_de_vie/barre_de_vie_60.png").convert_alpha()
barre_de_vie_40 = pygame.image.load("_internal/images/barre_de_vie/barre_de_vie_40.png").convert_alpha()
barre_de_vie_20 = pygame.image.load("_internal/images/barre_de_vie/barre_de_vie_20.png").convert_alpha()
barre_de_vie_0 = pygame.image.load("_internal/images/barre_de_vie/barre_de_vie_0.png").convert_alpha()
vie_ennemi_1 = pygame.image.load("_internal/images/barre_de_vie/vie_ennemi__1.png").convert_alpha()
vie_ennemi_2 = pygame.image.load("_internal/images/barre_de_vie/vie_ennemi__2.png").convert_alpha()
vie_ennemi_3 = pygame.image.load("_internal/images/barre_de_vie/vie_ennemi__3.png").convert_alpha()
vie_ennemi_4 = pygame.image.load("_internal/images/barre_de_vie/vie_ennemi_4.png").convert_alpha()
vie_boss_1 = pygame.image.load("_internal/images/barre_de_vie/vie_boss_1.png").convert_alpha()
vie_boss_2 = pygame.image.load("_internal/images/barre_de_vie/vie_boss_2.png").convert_alpha()
vie_boss_3 = pygame.image.load("_internal/images/barre_de_vie/vie_boss_3.png").convert_alpha()
vie_boss_4 = pygame.image.load("_internal/images/barre_de_vie/vie_boss_4.png").convert_alpha()
vie_boss_5 = pygame.image.load("_internal/images/barre_de_vie/vie_boss_5.png").convert_alpha()
vie_boss_6 = pygame.image.load("_internal/images/barre_de_vie/vie_boss_6.png").convert_alpha()
vie_boss_7 = pygame.image.load("_internal/images/barre_de_vie/vie_boss_7.png").convert_alpha()
vie_ennemi_1 = pygame.transform.scale(vie_ennemi_1, (40, 5))
vie_ennemi_2 = pygame.transform.scale(vie_ennemi_2, (40, 5))
vie_ennemi_3 = pygame.transform.scale(vie_ennemi_3, (40, 5))
vie_ennemi_4 = pygame.transform.scale(vie_ennemi_4, (40, 5))
vie_boss_1 = pygame.transform.scale(vie_boss_1, (300, 30))
vie_boss_2 = pygame.transform.scale(vie_boss_2, (300, 30))
vie_boss_3 = pygame.transform.scale(vie_boss_3, (300, 30))
vie_boss_4 = pygame.transform.scale(vie_boss_4, (300, 30))
vie_boss_5 = pygame.transform.scale(vie_boss_5, (300, 30))
vie_boss_6 = pygame.transform.scale(vie_boss_6, (300, 30))
vie_boss_7 = pygame.transform.scale(vie_boss_7, (300, 30))

game_over_image = pygame.image.load("_internal/images/pages/game_over.png").convert_alpha()
main_menu_image = pygame.image.load("_internal/images/pages/main_menu.png").convert_alpha()
victoire_image = pygame.image.load("_internal/images/pages/victoire.png").convert_alpha()
game_over_infinie_image = pygame.image.load("_internal/images/pages/game_over_infinie.png").convert_alpha()
choix_mode_image = pygame.image.load("_internal/images/pages/choix_mode.png").convert_alpha()
image_R = pygame.image.load("_internal/images/pages/R.png").convert_alpha()
image_fond = pygame.image.load("_internal/images/pages/fond.png").convert_alpha()
image_fond = pygame.transform.scale(image_fond, (1400, 1000))
page_help_manette = pygame.image.load("_internal/images/pages/help_manette.png").convert_alpha()
page_help_manette = pygame.transform.scale(page_help_manette, (580, 325))
bonus_vie = pygame.image.load("_internal/images/barre_de_vie/bonus.png").convert_alpha()
########### initialisation de la police #################################################

font = pygame.font.Font(None, 24)
font_score = pygame.font.Font("_internal/polices/pixel/PressStart2P-Regular.ttf", 30)
font_best_score = pygame.font.Font("_internal/polices/pixel/PressStart2P-Regular.ttf", 45)

########### variables globales ##########################################################

game_over_infini = False
mini_boss_tire = False
mode_infinie = False
mode_classic = False
debut_manche = True
choix_mode = False
game_over = False
victoire = False
main_menu = True
running = True
debut = True
game = False

delai_entre_tirs_rouge = 1000
temps_animation_danger = 0      
temps_entre_bonus = 15000   
vitesse_pulsation = 0.05
bouton_selectionne = 0
delai_entre_tirs = 600
nb_ennemis_en_vie = 0
dernier_tir_rouge = 0
mini_boss_tire_x = 0
dernier_bonus = 0
dernier_tir = 0
time_actuel = 0
Hauteur_min = 0
best_score = 0
nb_tirreur = 3
LARGEUR = 800
compteur = 0
largeur = 0
manche = 1
degat = 0  
score = 0
vie = 1
x = 400
y = 0

positions_ennemis = []
position_bonus = []
tab_ennemis = []
tirs_rouge = []
tirs = []

COULEUR_DANGER_1 = (100, 0, 0)    
COULEUR_DANGER_2 = (200, 100, 0)  

'''#######################################################################################
######################### fonctions ######################################################
#######################################################################################'''

############ Fonction pour mélanger deux couleurs ########################################

def calculer_couleur_pulsation(couleur_a, couleur_b, temps, vitesse):
    """
    Mélange deux couleurs (RGB) de façon fluide en suivant une onde sinusoïdale.
    """
    facteur = (math.sin(temps * vitesse) + 1) / 2
    r = couleur_a[0] + (couleur_b[0] - couleur_a[0]) * facteur
    g = couleur_a[1] + (couleur_b[1] - couleur_a[1]) * facteur
    b = couleur_a[2] + (couleur_b[2] - couleur_a[2]) * facteur

    return (int(r), int(g), int(b))

############ animations ##################################################################

def animation_debut():
    for i in range(250):
        screen.fill((0, 0, 0))
        screen.blit(avion_bleu, (x, 850 - i))
        pygame.display.flip()
        time.sleep(0.001)

def animation_ennemi(ennemi, x_ennemi):
    for i in range(100):
        screen.blit(ennemi, (x_ennemi, -50 + i))
        pygame.display.flip()
        time.sleep(0.001)

def animation_mort_avion(x_avion):
    global screen
    global avion_bleu
    global avion_rouge
    global avion_bleu_classique
    global avion_rouge_classique
    global mode_classic

    if mode_classic:
        avion_bleu_affiche = avion_bleu_classique
        avion_rouge_affiche = avion_rouge_classique
    else:
        avion_bleu_affiche = avion_bleu
        avion_rouge_affiche = avion_rouge
    
    
    for frame in range(60):  
        screen.fill((0, 0, 0))
        vibration = random.randint(-5, 5)
        x_vibration = x_avion + vibration
        
        if frame % 2 == 0:
            screen.blit(avion_bleu_affiche, (x_vibration, 600))
        else:
            screen.blit(avion_rouge_affiche, (x_vibration, 600))

        pygame.display.flip()
        clock.tick(60)

def dessiner_jeu(ecran_actuel, largeur_actuelle, px, py, offset_x, offset_y, boss_actif, k):
    global screen
    global temps_animation_danger
    global avion_bleu_classique
    global avion_final_boss
    global vitesse_pulsation
    global x
    global LARGEUR
    global HAUTEUR
    global largeur

    ecran_actuel.fill((0, 0, 0)) 
    temps_animation_danger += 1
    couleur_fond_actuelle = calculer_couleur_pulsation(COULEUR_DANGER_1, COULEUR_DANGER_2, temps_animation_danger, vitesse_pulsation)
    
    screen.blit(image_fond, (-400 + LARGEUR - 800, 0))

    pygame.draw.rect(ecran_actuel, couleur_fond_actuelle, (0, 0, LARGEUR, largeur))
    pygame.draw.rect(ecran_actuel, couleur_fond_actuelle, (0, 0, largeur, HAUTEUR))
    pygame.draw.rect(ecran_actuel, couleur_fond_actuelle, (0, HAUTEUR - largeur, LARGEUR, largeur))
    pygame.draw.rect(ecran_actuel, couleur_fond_actuelle, (LARGEUR - largeur, 0, largeur, HAUTEUR))


    if boss_actif or largeur_actuelle > 800:
        pos_boss_x = largeur_actuelle /2 - 250
        screen.blit(avion_final_boss, (pos_boss_x, -400+k))

    screen.blit(avion_bleu_classique, (x, 600))
    
def animation_finale_boss():
    global screen
    global avion_final_boss
    global temps_animation_danger
    global vitesse_pulsation
    global LARGEUR
    global HAUTEUR
    global x
    global largeur
    global animation

    offset_x = 0
    offset_y = 0
    shake_timer = 60
    mode_boss_actif = False
    LARGEUR = 800
    HAUTEUR = 800
    k = 0

    while animation:
        if shake_timer > 0:
            offset_x = random.randint(-8, 8)
            offset_y = random.randint(-8, 8)
            shake_timer -= 1
            
            if shake_timer == 0:
                mode_boss_actif = True
                os.environ['SDL_VIDEO_CENTERED'] = '1'

                while LARGEUR < 1200:
                    LARGEUR += 2
                    if LARGEUR > 1200: LARGEUR = 1200
                    
                    screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
                    
                    if largeur <= 50 and LARGEUR < 950:
                        largeur += 2
                    if LARGEUR >= 1150 and largeur >= 0:
                        largeur -= 2
                    x += 1
                    k += 1.5
                    dessiner_jeu(screen, LARGEUR, x, 600, 0, 0, True, k)
                    
                    if LARGEUR == 1200:
                        animation = False

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            animation = False

                    pygame.display.flip()
                    pygame.time.delay(10)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                animation = False
                
        dessiner_jeu(screen, LARGEUR, x, 600, offset_x, offset_y, mode_boss_actif, k)

        pygame.display.flip()
        clock.tick(60)

def animation_choix_mode():
    if manette:
        global bouton_selectionne
            
        axe_y_droit = manette.get_axis(3) 

        if axe_y_droit > 0.5:      
            bouton_selectionne = 2
        elif axe_y_droit < -0.5:   
            bouton_selectionne = 1
        
        if main_menu or game_over or victoire:
            if bouton_selectionne == 2:
                pygame.draw.rect(screen, (255, 255, 0), (215 + (LARGEUR - 800)/2, 605, 385, 75), 5)
        
            elif bouton_selectionne == 1:
                pygame.draw.rect(screen, (255, 255, 0), (215 + (LARGEUR - 800)/2, 525, 385, 80), 5)
        elif choix_mode:
            if bouton_selectionne == 1:
                pygame.draw.rect(screen, (255, 255, 0), (185, 185, 450, 220), 5)
                
            elif bouton_selectionne == 2:
                pygame.draw.rect(screen, (255, 255, 0), (185, 445, 450, 220), 5)
############ creation ennemis ############################################################

def ennemi():
    global tab_ennemis
    global positions_ennemis

    random_nb_ennemi = random.randint(4, 8)

    x_ennemi = random.randint(0, 7)
    x_ennemi = x_ennemi * 100
    tab_ennemis.append(avion_rouge_base)
    positions_ennemis.append(x_ennemi)

    for i in range(random_nb_ennemi-1):
        while x_ennemi in positions_ennemis:
            x_ennemi = random.randint(0, 7)
            x_ennemi = x_ennemi * 100
        tab_ennemis.append(avion_rouge_base)
        positions_ennemis.append(x_ennemi)
    
    return random_nb_ennemi

############ gestion du temps entre les tirs #############################################

def temps_entre_tirs():
    global dernier_tir
    global delai_entre_tirs
    global time_actuel
    
    if time_actuel - dernier_tir > delai_entre_tirs:
        return True
    else:
        return False

def temps_entre_tirs_rouge():
    global dernier_tir_rouge
    global delai_entre_tirs_rouge
    global time_actuel
    
    if time_actuel - dernier_tir_rouge > delai_entre_tirs_rouge:
        return True
    else:
        return False

############# affichage de la barre de vie  ##############################################

def affichage_barre_de_vie(vie):
    global screen
    global barre_de_vie_120
    global barre_de_vie_100
    global barre_de_vie_80
    global barre_de_vie_60
    global barre_de_vie_40
    global barre_de_vie_20
    global barre_de_vie_0
    global font

    if vie >= 120:
        screen.blit(barre_de_vie_120, (10, 700))
    elif vie >= 100:
        screen.blit(barre_de_vie_100, (10, 700))
    elif vie >= 80:
        screen.blit(barre_de_vie_80, (10, 700))
    elif vie >= 60:
        screen.blit(barre_de_vie_60, (10, 700))
    elif vie >= 30:
        screen.blit(barre_de_vie_40, (10, 700))
    elif vie >= 10:
        screen.blit(barre_de_vie_20, (10, 700))
    else:
        screen.blit(barre_de_vie_0, (10, 700))
    
    image_vie = font.render(f"{vie}", True, (255, 255, 255))
    screen.blit(image_vie, (70, 742))

def affichage_barre_de_vie_ennemi():
    global screen
    global vie_ennemi_1
    global vie_ennemi_2
    global vie_ennemi_3
    global vie_ennemi_4
    global tab_ennemis
    vie_de_base = 0
    vie_ennemi = 0
    position_x = 0
    position_y = 0

    for ennemi in tab_ennemis:
        type_ennemi = ennemi[0]
        x_ennemi = ennemi[1]
        y_ennemi = ennemi[2]
        vie_ennemi = ennemi[3]

        if type_ennemi == avion_niveau_1_1:
            vie_de_base = 2
            position_x = 17
            position_y = 0
        elif type_ennemi == avion_niveau_1_2:
            vie_de_base = 4
            position_x = 17
            position_y = 0
        elif type_ennemi == avion_niveau_1_3:
            vie_de_base = 6
            position_x = 17
            position_y = 0
        elif type_ennemi == avion_niveau_2_1:
            vie_de_base = 3
            position_x = -14
            position_y = -20
        elif type_ennemi == avion_niveau_2_2:
            vie_de_base = 6
            position_x = -14
            position_y = -20
        elif type_ennemi == avion_niveau_2_3:
            vie_de_base = 8   
            position_x = -14
            position_y = -20
        elif type_ennemi == avion_mini_boss:
            vie_de_base = 10
            position_x = -48
            position_y = -7
        elif type_ennemi == avion_final_boss:
            vie_de_base = 14
            position_x = -73
            position_y = -105

        if ennemi[0] != avion_final_boss:
            if vie_ennemi >= vie_de_base * 0.8:
                screen.blit(vie_ennemi_1, (x_ennemi + 30 - position_x, y_ennemi - 5 - position_y))
            elif vie_ennemi >= vie_de_base * 0.5:
                screen.blit(vie_ennemi_2, (x_ennemi + 30 - position_x, y_ennemi - 5 - position_y))
            elif vie_ennemi >= vie_de_base * 0.2:
                screen.blit(vie_ennemi_3, (x_ennemi + 30 - position_x, y_ennemi - 5 - position_y))
            elif vie_ennemi > 0:
                screen.blit(vie_ennemi_4, (x_ennemi + 30 - position_x, y_ennemi - 5 - position_y))
        else:
            if vie_ennemi > vie_de_base - 2:
                screen.blit(vie_boss_1, (x_ennemi + 30 - position_x, y_ennemi - 5 - position_y))
            elif vie_ennemi > vie_de_base - 4:
                screen.blit(vie_boss_2, (x_ennemi + 30 - position_x, y_ennemi - 5 - position_y))
            elif vie_ennemi > vie_de_base - 6:
                screen.blit(vie_boss_3, (x_ennemi + 30 - position_x, y_ennemi - 5 - position_y))
            elif vie_ennemi > vie_de_base - 8:
                screen.blit(vie_boss_4, (x_ennemi + 30 - position_x, y_ennemi - 5 - position_y))
            elif vie_ennemi > vie_de_base - 10:
                screen.blit(vie_boss_5, (x_ennemi + 30 - position_x, y_ennemi - 5 - position_y))
            elif vie_ennemi > vie_de_base - 12:
                screen.blit(vie_boss_6, (x_ennemi + 30 - position_x, y_ennemi - 5 - position_y))
            elif vie_ennemi > vie_de_base - 14:
                screen.blit(vie_boss_7, (x_ennemi + 30 - position_x, y_ennemi - 5 - position_y))
            
############# gestion des tirs de l'avion bleu ###########################################

def gestion_tirs_bleu():
    global tirs
    global x
    global time_actuel
    global dernier_tir
    y = 0

    tirs_suivants = []
    for k in range(len(tirs)):
        y=tirs[k][1]-10
        if y>=50:
            tirs_suivants.append([tirs[k][0], y])

    tirs = tirs_suivants

    for k in range(len(tirs)):
        pygame.draw.rect(screen, (144, 213, 255), (tirs[k][0], tirs[k][1], 10, 30))

    if temps_entre_tirs():
        tirs.append([x+13, 620])
        tirs.append([x+73, 620])
        dernier_tir = time_actuel

def gestion_tirs_bleu_classique():
    global tirs
    global x
    global time_actuel
    global dernier_tir
    y = 0

    tirs_suivants = []
    for k in range(len(tirs)):
        y=tirs[k][1]-10
        if y>=50:
            tirs_suivants.append([tirs[k][0], y])

    tirs = tirs_suivants

    for k in range(len(tirs)):
        pygame.draw.rect(screen, (144, 213, 255), (tirs[k][0], tirs[k][1], 5, 15))

    if temps_entre_tirs():
        tirs.append([x+4, 620])
        tirs.append([x+22, 620])
        dernier_tir = time_actuel

############# gestion des tirs de l'avion rouge ##########################################

def gestion_tirs_rouge():
    global tirs_rouge
    global positions_ennemis
    global nb_ennemis_en_vie
    global time_actuel
    global dernier_tir_rouge
    global nb_tirreur
    global debut
    global screen

    tirs_suivants_rouge = []
    for k in range(len(tirs_rouge)):
        y=tirs_rouge[k][1]+10
        if y<=700:
            tirs_suivants_rouge.append([tirs_rouge[k][0], y, 1])

    tirs_rouge = tirs_suivants_rouge
    for k in range(len(tirs_rouge)):
        pygame.draw.rect(screen, (255, 213, 144), (tirs_rouge[k][0], tirs_rouge[k][1], 10, 30))

    deja_choisi = [-1]
    if temps_entre_tirs_rouge():
        nombre_qui_tirent = min(3, nb_ennemis_en_vie)
        for k in range(nombre_qui_tirent):
            y=random.randint(0,nb_ennemis_en_vie-1)
            while y in deja_choisi:
                y=random.randint(0,nb_ennemis_en_vie-1)
            tirs_rouge.append([positions_ennemis[y]+13, 100, 1])
            tirs_rouge.append([positions_ennemis[y]+72, 100, 1])
            deja_choisi.append(y)
        dernier_tir_rouge = time_actuel

def gestion_tirs_rouge_classique():
    global tirs_rouge
    global time_actuel
    global dernier_tir_rouge
    global nb_tirreur
    global debut
    global screen
    global manche
    global tab_ennemis
    global mini_boss_tire
    global compteur
    global mini_boss_tire_x

    nb_ennemis_en_vie = len(tab_ennemis)
    tirs_suivants_rouge = []
    for k in range(len(tirs_rouge)):
        y=tirs_rouge[k][1]+10
        if tirs_rouge[k][2] == 3:
            if x < tirs_rouge[k][0]:
                tirs_rouge[k][3] = -1
            elif x > tirs_rouge[k][0]:
                tirs_rouge[k][3] = 1
        if y<=700:
            if tirs_rouge[k][2] == 3:
                tirs_suivants_rouge.append([tirs_rouge[k][0]+tirs_rouge[k][3]*5, y-4, tirs_rouge[k][2], tirs_rouge[k][3]])
            else:
                tirs_suivants_rouge.append([tirs_rouge[k][0], y, tirs_rouge[k][2]])
    tirs_rouge = tirs_suivants_rouge

    for k in range(len(tirs_rouge)):
        if tirs_rouge[k][2] == 1:
            pygame.draw.rect(screen, (255, 213, 144), (tirs_rouge[k][0], tirs_rouge[k][1], 5, 20))
        elif tirs_rouge[k][2] == 2:
            pygame.draw.rect(screen, (255, 50, 50), (tirs_rouge[k][0], tirs_rouge[k][1], 30, 30))
        elif tirs_rouge[k][2] == 3:
            pygame.draw.rect(screen, (255, 213, 144), (tirs_rouge[k][0], tirs_rouge[k][1], 30, 40))

    if mini_boss_tire == True and compteur > 0:
        if compteur > 150 and compteur <= 300:
            compteur = compteur - 1
            pygame.draw.circle(screen, (255, 50, 50), (tab_ennemis[mini_boss_tire_x][1]+100, tab_ennemis[mini_boss_tire_x][2]+125), 20)
        if compteur <= 150:
            compteur = compteur - 1
            pygame.draw.circle(screen, (255, 50, 50), (tab_ennemis[mini_boss_tire_x][1]+100, tab_ennemis[mini_boss_tire_x][2]+125), 20)
            tirs_rouge.append([tab_ennemis[mini_boss_tire_x][1]+85, tab_ennemis[mini_boss_tire_x][2]+105, 2])
            if compteur == 0:
                mini_boss_tire = False

    deja_choisi = [-1]
    if temps_entre_tirs_rouge():
        nb_ennemis_en_vie = len(tab_ennemis)
        if nb_ennemis_en_vie > 0:
            nombre_qui_tirent = min(5, nb_ennemis_en_vie)
            if nombre_qui_tirent == nb_ennemis_en_vie and nb_ennemis_en_vie > 2:
                nombre_qui_tirent = nombre_qui_tirent - 2
            for k in range(nombre_qui_tirent):
                y=random.randint(0,nb_ennemis_en_vie-1)
                tentatives = 0
                while (y in deja_choisi or (mini_boss_tire and tab_ennemis[y][0] == avion_mini_boss)) and tentatives < 20:
                    y=random.randint(0,nb_ennemis_en_vie-1)
                    tentatives = tentatives + 1
                if tentatives >= 20:
                    break
                if tab_ennemis[y][0] == avion_niveau_1_1 or tab_ennemis[y][0] == avion_niveau_1_2 or tab_ennemis[y][0] == avion_niveau_1_3:
                    tirs_rouge.append([tab_ennemis[y][1]+20, tab_ennemis[y][2]+25, 1])
                    tirs_rouge.append([tab_ennemis[y][1]+40, tab_ennemis[y][2]+25, 1])
                elif tab_ennemis[y][0] == avion_niveau_2_1 or tab_ennemis[y][0] == avion_niveau_2_2 or tab_ennemis[y][0] == avion_niveau_2_3:
                    tirs_rouge.append([tab_ennemis[y][1]+40, tab_ennemis[y][2]+50, 1])
                    tirs_rouge.append([tab_ennemis[y][1]+84, tab_ennemis[y][2]+50, 1])
                elif tab_ennemis[y][0] == avion_mini_boss:
                    mini_boss_tire = True
                    mini_boss_tire_x = y
                    compteur = 300
                elif tab_ennemis[y][0] == avion_final_boss:
                    tirs_rouge.append([tab_ennemis[y][1]+194, tab_ennemis[y][2]+225, 3, 0])
                    tirs_rouge.append([tab_ennemis[y][1]+278, tab_ennemis[y][2]+225, 3, 0])
                deja_choisi.append(y)

        dernier_tir_rouge = time_actuel

############# reset ######################################################################

def reset_infinie():
    global nb_ennemis_en_vie
    global tab_ennemis
    global positions_ennemis
    global nb_tirreur
    global tirs_rouge
    global tirs
    global vie
    global score
    global debut
    global avion_bleu
    global avion_bleu_base

    avion_bleu = pygame.transform.scale(avion_bleu_base, (100, 100))
    nb_tirreur = 3
    nb_ennemis_en_vie = 0
    tab_ennemis = []
    positions_ennemis = []
    tirs_rouge = []
    tirs = []
    vie = 120
    score = 0
    debut = True

def reset():
    global nb_ennemis_en_vie
    global tab_ennemis
    global positions_ennemis
    global nb_tirreur
    global tirs_rouge
    global tirs
    global vie
    global score
    global manche
    global debut_manche
    global debut
    global x
    global degat
    global mode_classic
    global mode_infinie
    global mini_boss_tire
    global compteur
    global mini_boss_tire_x
    global tab_ennemis
    global positions_ennemis
    global tirs_rouge
    global tirs
    global vie
    global score
    global manche
    global debut_manche
    global debut
    global x
    global avion_bleu
    global avion_bleu_base

    avion_bleu = pygame.transform.scale(avion_bleu_base, (100, 100))
    x = 400
    degat = 0
    mini_boss_tire = False
    compteur = 0
    mini_boss_tire_x = 0
    nb_tirreur = 3
    nb_ennemis_en_vie = 0
    tab_ennemis = []
    positions_ennemis = []
    tirs_rouge = []
    tirs = []
    vie = 120
    score = 0
    manche = 1
    debut_manche = True
    debut = True

############# affichage des règles ######################################################

def afficher_regles():
    global screen
    global font
    global running
    global game
    global main_menu
    global choix_mode
    global game_over
    global game_over_infini
    global victoire
    global mode_infinie
    global mode_classic
    r=0

    flou = pygame.Surface((1200, 800))
    flou.set_alpha(200) 
    flou.fill((0, 0, 0))
    screen.blit(flou, (0, 0))

    font_titre = pygame.font.Font("polices/pixel/PressStart2P-Regular.ttf", 35)
    font_texte = pygame.font.Font("polices/pixel/PressStart2P-Regular.ttf", 15)

    lignes_texte = [
        "--- PAUSE / INFOS ---",
        "",
        "COMMENT JOUER :",
        "- Utilisez les flèches GAUCHE et DROITE",
        "  pour déplacer l'avion.",
        "- Le tir est automatique.",
        "- Évitez les tirs ennemis et détruisez",
        "  les vagues d'avions.",
        "Appuyez sur 'R' pour reprendre la partie."
    ]

    if LARGEUR == 1200:
        r = 200
    else:
        r = 0 
    bouton_rect = pygame.Rect(250 + r, 350, 300, 60)
    couleur_bouton = (112, 128, 144)

    retour_menu = False
    en_pause = True
    while en_pause and running:
        
        y_pos = 50
        for ligne in lignes_texte:
            texte_surface = font_texte.render(ligne, True, (255, 255, 255))
            if "---" in ligne: 
                texte_surface = font_titre.render(ligne, True, (200, 50, 50))
                y_pos += 30
            
            rect_texte = texte_surface.get_rect(center=(400+r, y_pos))
            screen.blit(texte_surface, rect_texte)
            y_pos += 30

        rect_img = page_help_manette.get_rect(center=(400 + r, 590))
        screen.blit(page_help_manette, rect_img)
        pygame.draw.rect(screen, couleur_bouton, bouton_rect)
        texte_bouton = font.render("RETOUR AU MENU PRINCIPAL", True, (255, 255, 255))
        rect_bouton_texte = texte_bouton.get_rect(center=bouton_rect.center)
        screen.blit(texte_bouton, rect_bouton_texte)

        if manette:
            pygame.draw.rect(screen, (255, 255, 0), bouton_rect, 5)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                en_pause = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    en_pause = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_rect.collidepoint(event.pos):
                    en_pause = False
                    retour_menu = True
                    game = False       
                    main_menu = True   
                    mode_infinie = False
                    mode_classic = False
                    game_over_infini = False
                    choix_mode = False 
                    game_over = False
                    victoire = False
                    if mode_infinie:
                        reset_infinie()
                    else:
                        reset()
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 6: 
                    en_pause = False
                elif event.button == 1:
                    en_pause = False
                    retour_menu = True
                    game = False       
                    main_menu = True   
                    mode_infinie = False
                    mode_classic = False
                    game_over_infini = False
                    choix_mode = False 
                    game_over = False
                    victoire = False
                    if mode_infinie:
                        reset_infinie()
                    else:
                        reset()
    
    return retour_menu

############# point de vie suplementaire ################################################

def vie_bonus():
    global x
    global position_bonus
    global bonus_vie
    global time_actuel
    global dernier_bonus
    global temps_entre_bonus
    global vie

    a_supprimer = []
    provisoire = []
    chance = random.randint(0, 1000)

    if (time_actuel-dernier_bonus > temps_entre_bonus) and (chance > 550 and chance < 600):
        position_bonus.append([x, 0])
        dernier_bonus = time_actuel
    
    for i in range(len(position_bonus)):
        screen.blit(bonus_vie, (position_bonus[i][0], position_bonus[i][1]))
        position_bonus[i][1] = position_bonus[i][1] + 5
        if (position_bonus[i][1] < 640 and position_bonus[i][1] > 600) and (position_bonus[i][0] < x + 50 and position_bonus[i][0] > x-5):
            a_supprimer.append(i)
            vie += 15
        if position_bonus[i][1] > 700:
            a_supprimer.append(i)
    
    for i in range(len(position_bonus)):
        if i not in a_supprimer:
            provisoire.append(position_bonus[i])
    position_bonus = provisoire

'''#######################################################################################
######################### programme principale ###########################################
#######################################################################################'''

while running:

    ############# menu principal #####################################################

    while main_menu and running:
        screen.fill((0, 0, 0))
        screen.blit(image_fond, (-400 + LARGEUR - 800, 0))
        if LARGEUR == 1200:
            screen.blit(main_menu_image, (290, 100))
            screen.blit(image_R, (1050, 150))
        else:
            screen.blit(main_menu_image, (90, 100))
            screen.blit(image_R, (650, 150))
        
        animation_choix_mode()

        ############# gestion des événements #############################################

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu = False
                    choix_mode = True
                if event.key == pygame.K_r:
                    afficher_regles() 
                    if not game: 
                        break 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(220, 520, 380, 80).collidepoint(event.pos):
                    main_menu = False
                    choix_mode = True
                if pygame.Rect(220, 630, 380, 80).collidepoint(event.pos):
                    running = False
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0: 
                    if bouton_selectionne == 1: 
                        reset()
                        main_menu = False
                        choix_mode = True
                    elif bouton_selectionne == 2: 
                        reset()
                        running = False
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 6: 
                        retour_menu = afficher_regles()
                        if not game:
                            break

        pygame.display.flip()
        clock.tick(60)

    ############# choix de mode ######################################################

    while choix_mode and running:
        screen.fill((0, 0, 0))
        screen.blit(image_fond, (-400 + LARGEUR - 800, 0))
        if LARGEUR == 1200:
            screen.blit(choix_mode_image, (290, 100))
            screen.blit(image_R, (1050, 150))
        else:
            screen.blit(choix_mode_image, (90, 100))
            screen.blit(image_R, (650, 150))
        
        animation_choix_mode()

        ############# gestion des événements #############################################

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    afficher_regles()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(195, 195, 440, 210).collidepoint(event.pos):
                    reset()
                    choix_mode = False
                    mode_classic = True
                    mode_infinie = False
                    game = True
                if pygame.Rect(190, 450, 440, 210).collidepoint(event.pos):
                    reset_infinie()
                    choix_mode = False
                    mode_infinie = True
                    mode_classic = False
                    game = True
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0: 
                    if bouton_selectionne == 1: 
                        reset()
                        choix_mode = False
                        mode_classic = True
                        mode_infinie = False
                        game = True
                    elif bouton_selectionne == 2: 
                        reset_infinie()
                        choix_mode = False
                        mode_infinie = True
                        mode_classic = False
                        game = True
                if event.button == 6: 
                    retour_menu = afficher_regles()
                    if not game:
                        break

        pygame.display.flip()
        clock.tick(60)

    ############# mode infini ########################################################

    while game and running and mode_infinie:
        screen.fill((0, 0, 0))
        screen.blit(image_fond, (-400 + LARGEUR - 800, 0))
        screen.blit(image_R, (760, 10))
        
        ############# temps à l'instant  #################################################
        time_actuel = pygame.time.get_ticks()
        
        if debut:
            dernier_tir_rouge = time_actuel
            debut = False

        ############# mouvement de l'avion bleu  #########################################

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if x > 0:
                x = x - 10
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            if x < 700:
                x = x + 10

        valeur_stick_droit = 0
        if manette:
            valeur_stick_droit = manette.get_axis(0) 

        # GAUCHE
        if pygame.key.get_pressed()[pygame.K_LEFT] or valeur_stick_droit < -0.2:
            if x > 0:
                x = x - 10
        
        # DROITE
        elif pygame.key.get_pressed()[pygame.K_RIGHT] or valeur_stick_droit > 0.2:
            
            if LARGEUR > 800: 
                limite_x = 1100 
            else:
                limite_x = 700
            
            if x < limite_x:
                x = x + 10
        
        ############# affichage des avions  ##############################################
        if degat > 0:
            screen.blit(avion_rouge, (x, 600))
            degat -= 1
        else:
            screen.blit(avion_bleu, (x, 600))

        while nb_ennemis_en_vie == 0:
            nb_ennemis_en_vie = ennemi()
            if debut:
                animation_debut()

            for i in range(len(tab_ennemis)):
                animation_ennemi(tab_ennemis[i], positions_ennemis[i])
        
        print(tab_ennemis)
        print(positions_ennemis)

        for i in range(len(tab_ennemis)):
            screen.blit(tab_ennemis[i], (positions_ennemis[i], 50))

        ############# affichage de la barre de vie  ######################################

        affichage_barre_de_vie(vie)

        ############# affichage du score #################################################

        image_score = font.render(f"Score : {score}", True, (255, 255, 255))
        screen.blit(image_score, (650, 742))

        ############# gestion des tirs de l'avion bleu ###################################

        gestion_tirs_bleu()

        ############# gestion des tirs de l'avion rouge ##################################

        gestion_tirs_rouge()

        ############# gestion des vies ###################################################
        
        balles_a_supprimer = []
        if len(tirs_rouge) > 0:
            for k in range(len(tirs_rouge)):
                tir_x = tirs_rouge[k][0]
                tir_y = tirs_rouge[k][1]
                tir_type = tirs_rouge[k][2]
                
                if tir_type == 1:
                    tir_largeur = 5
                    tir_hauteur = 20
                elif tir_type == 2:
                    tir_largeur = 30
                    tir_hauteur = 30
                else: 
                    tir_largeur = 30
                    tir_hauteur = 40
                
                if (tir_y + tir_hauteur >= 600 and tir_y <= 630):
                    if (tir_x + tir_largeur >= x + 6 and tir_x <= x + 89):
                        
                        vie = vie - 15
                        degat = 15  
                        balles_a_supprimer.append(k)

        tirs_rouge_suivants = []
        for k in range(len(tirs_rouge)):
            if k not in balles_a_supprimer:
                tirs_rouge_suivants.append(tirs_rouge[k])

        tirs_rouge = tirs_rouge_suivants

        ############# gestion des collisions ##############################################

        balles_a_supprimer = []
        ennemis_a_supprimer = []
        if len(tirs) > 0:
            for k in range(len(tirs)):
                if tirs[k][1] >= 100 and tirs[k][1] <= 130:
                    for i in range(nb_ennemis_en_vie):
                        if tirs[k][0] >= positions_ennemis[i] + 6 and tirs[k][0] <= positions_ennemis[i] + 94:
                            balles_a_supprimer.append(k)
                            ennemis_a_supprimer.append(i)
        
        ennemis_suivants = []
        positions_ennemis_suivantes = []
        for k in range(nb_ennemis_en_vie):
            if k not in ennemis_a_supprimer:
                ennemis_suivants.append(tab_ennemis[k])
                positions_ennemis_suivantes.append(positions_ennemis[k])
            else:
                score = score + 10

        tab_ennemis = ennemis_suivants
        positions_ennemis = positions_ennemis_suivantes
        nb_ennemis_en_vie = len(tab_ennemis)

        tirs_suivants = []
        for k in range(len(tirs)):
            if k not in balles_a_supprimer:
                tirs_suivants.append(tirs[k])

        tirs = tirs_suivants

        ############# gestion des événements #############################################

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    retour_menu = afficher_regles() 
                    if retour_menu: 
                        break 
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 6: 
                    retour_menu = afficher_regles()
                    if not game:
                        break

        if vie <= 0:
            animation_mort_avion(x)
            game_over_infini = True
            game = False

        pygame.display.flip()
        clock.tick(60)
    
    ############# mode classique #####################################################

    while game and running and mode_classic:
        screen.fill((0, 0, 0))
        screen.blit(image_fond, (-400 + LARGEUR - 800 , 0))
        if LARGEUR == 1200:
            screen.blit(image_R, (1150, 10))
        else:
            screen.blit(image_R, (760, 10))
        
        ############# temps à l'instant  #################################################

        time_actuel = pygame.time.get_ticks()
        
        ############# mouvement de l'avion bleu  #########################################

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if x > 0:
                x = x - 10
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            if manche == 3:
                if x < 1170:
                    x = x+10
            if x < 770:
                x = x + 10
            
        valeur_stick_droit = 0
        if manette:
            valeur_stick_droit = manette.get_axis(0) 

        # GAUCHE
        if valeur_stick_droit < -0.2:
            if x > 0:
                x = x - 10
        
        # DROITE
        elif valeur_stick_droit > 0.2:
            
            if LARGEUR > 800: 
                limite_x = 1170 
            else:
                limite_x = 770
            
            if x < limite_x:
                x = x + 10
        
        ############# affichage des avions  ##############################################
        
        if degat > 0:
            screen.blit(avion_rouge_classique, (x, 600))
            degat -= 1
        else:
            screen.blit(avion_bleu_classique, (x, 600))
        if manche == 1 and debut_manche:
            nb_ennemis_en_vie = 17
            tab_ennemis = []
            for i in range(7):
                tab_ennemis.append([avion_niveau_2_1, +i*110, 10, 3])
            for i in range(10):
                tab_ennemis.append([avion_niveau_1_1, i*80, 150, 2])
            debut_manche = False
        elif manche == 2 and debut_manche:
            nb_ennemis_en_vie = 19
            tab_ennemis = []
            for i in range(3):
                tab_ennemis.append([avion_mini_boss, +i*300, 10, 10])
            for i in range(6):
                tab_ennemis.append([avion_niveau_2_2, +i*130, 130, 6])
            for i in range(10):
                tab_ennemis.append([avion_niveau_1_2, i*80, 230, 4])
            debut_manche = False
        elif manche == 3 and debut_manche:
            tab_ennemis = []
            animation = True

            animation_finale_boss()
            debut_manche = False

            tab_ennemis.append([avion_mini_boss, 0, 10, 10])
            tab_ennemis.append([avion_mini_boss, 3*300, 10, 10])
            for i in range(3):
                tab_ennemis.append([avion_niveau_2_3, i*110, 130, 8])
                tab_ennemis.append([avion_niveau_2_3, 1070-i*110, 130, 8])
            for i in range(4):
                tab_ennemis.append([avion_niveau_1_3, i*80, 230, 6])
                tab_ennemis.append([avion_niveau_1_3, 1120-i*80, 230, 6])
            for i in range(3):
                tab_ennemis.append([avion_niveau_2_3, i*110, 290, 8])
                tab_ennemis.append([avion_niveau_2_3, 1070-i*110, 290, 8])
            for i in range(15):
                tab_ennemis.append([avion_niveau_1_3, i*80, 400, 6])
            tab_ennemis.append([avion_final_boss, 350, -100, 14])
            nb_ennemis_en_vie = 38

        for i in range(len(tab_ennemis)):
            screen.blit(tab_ennemis[i][0], (tab_ennemis[i][1], tab_ennemis[i][2]))
        
        ############# affichage de la barre de vie  ######################################

        affichage_barre_de_vie(vie)
        affichage_barre_de_vie_ennemi()

        ############# affichage de la barre de vie  ######################################

        vie_bonus()

        ############# affichage du score #################################################

        image_score = font.render(f"Score : {score}", True, (255, 255, 255))
        screen.blit(image_score, (650 + LARGEUR-800, 742))
        
        ############# gestion des tirs de l'avion bleu ###################################
        
        gestion_tirs_bleu_classique()
        
        ############# gestion des tirs de l'avion rouge ##################################

        gestion_tirs_rouge_classique()
        
        ############# gestion des vies ###################################################
        
        balles_a_supprimer = []
        if len(tirs_rouge) > 0:
            for k in range(len(tirs_rouge)):
                tir_x = tirs_rouge[k][0]
                tir_y = tirs_rouge[k][1]
                tir_type = tirs_rouge[k][2]
                
                if tir_type == 1:
                    tir_largeur = 5
                    tir_hauteur = 20
                elif tir_type == 2:
                    tir_largeur = 30
                    tir_hauteur = 30
                else: 
                    tir_largeur = 30
                    tir_hauteur = 40
                
                if (tir_y + tir_hauteur >= 600 and tir_y <= 630):
                    if (tir_x + tir_largeur >= x and tir_x <= x + 30):
                      
                        if tir_type == 1:
                            vie = vie - 5
                        elif tir_type == 2:
                            vie = vie - 10
                        else:  
                            vie = vie - 30
                        degat = 15
                        balles_a_supprimer.append(k)

        tirs_rouge_suivants = []
        for k in range(len(tirs_rouge)):
            if k not in balles_a_supprimer:
                tirs_rouge_suivants.append(tirs_rouge[k])

        tirs_rouge = tirs_rouge_suivants

        ############# gestion des collisions ##############################################

        balles_a_supprimer = []
        ennemis_a_supprimer = []
        if len(tirs) > 0:
            for k in range(len(tirs)):
                if tirs[k][1] <= 400:
                    for i in range(len(tab_ennemis)):

                        if tab_ennemis[i][0] == avion_mini_boss:
                            position_min = tab_ennemis[i][1] + 60
                            position_max = tab_ennemis[i][1] + 150
                            Hauteur_min = 0
                        elif tab_ennemis[i][0] == avion_final_boss:
                            position_min = tab_ennemis[i][1] + 100
                            position_max = tab_ennemis[i][1] + 400
                            Hauteur_min = tab_ennemis[i][2] + 220
                        elif tab_ennemis[i][0] == avion_niveau_2_1 or tab_ennemis[i][0] == avion_niveau_2_2 or tab_ennemis[i][0] == avion_niveau_2_3:
                            position_min = tab_ennemis[i][1] + 40
                            position_max = tab_ennemis[i][1] + 84
                            Hauteur_min = 0
                        else:
                            position_min = tab_ennemis[i][1] + 6
                            position_max = tab_ennemis[i][1] + 56
                            Hauteur_min = 0
                            
                        if tirs[k][1] >= tab_ennemis[i][2]-20 and tirs[k][1] <= tab_ennemis[i][2]+40 + Hauteur_min:
                            if tirs[k][0] >= position_min and tirs[k][0] <= position_max:
                                
                                balles_a_supprimer.append(k)
                                tab_ennemis[i][3] = tab_ennemis[i][3] - 1

                                if tab_ennemis[i][3] <= 0:

                                    ennemis_a_supprimer.append(i)

                                    if mini_boss_tire:
                                        if i == mini_boss_tire_x:
                                            mini_boss_tire = False
                                            compteur = 0
                                        elif i < mini_boss_tire_x:
                                            mini_boss_tire_x = mini_boss_tire_x - 1
                                        
        score = time_actuel // 1000

        ennemis_suivants = []
        positions_ennemis_suivantes = []
        for k in range(nb_ennemis_en_vie):
            if k not in ennemis_a_supprimer:
                ennemis_suivants.append(tab_ennemis[k])

        tab_ennemis = ennemis_suivants
        nb_ennemis_en_vie = len(tab_ennemis)

        tirs_suivants = []
        for k in range(len(tirs)):
            if k not in balles_a_supprimer:
                tirs_suivants.append(tirs[k])

        tirs = tirs_suivants

        ############# gestion des événements #############################################

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    afficher_regles()
                    if not game:
                        if LARGEUR == 1200:
                            os.environ['SDL_VIDEO_CENTERED'] = '1'
                            LARGEUR = 800
                            HAUTEUR = 800   
                            screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
                        break
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 6: 
                    retour_menu = afficher_regles()
                    if not game:
                        if LARGEUR == 1200:
                            os.environ['SDL_VIDEO_CENTERED'] = '1'
                            LARGEUR = 800
                            HAUTEUR = 800   
                            screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
                        break

        if vie <= 0:
            animation_mort_avion(x)
            game_over = True
            game = False
            debut_manche = True
            manche = 1
        
        if nb_ennemis_en_vie == 0:
            if manche < 3:
                manche = manche + 1
                debut_manche = True
            elif manche == 3:
                victoire = True
                if LARGEUR == 1200:
                    os.environ['SDL_VIDEO_CENTERED'] = '1'
                    LARGEUR = 800
                    HAUTEUR = 800   
                    screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
                game = False
                debut_manche = True
                manche = 1
        
        pygame.display.flip()
        clock.tick(60)

    ############# écran de game over #################################################

    while game_over_infini and running:
        screen.fill((0, 0, 0))
        screen.blit(image_fond, (-400 + LARGEUR - 800, 0))
        screen.blit(game_over_infinie_image, (90, 100))
        screen.blit(image_R, (650, 150))
        
        best_score = max(best_score, score)

        score_image = font_score.render(f"Score : {score}", True, (255, 247, 153))
        best_score_image = font_best_score.render(f"{best_score}", True, (255, 255, 255))
        

        screen.blit(score_image, (240, 486))

        if best_score < 10:
            screen.blit(best_score_image, (380, 385))
        elif best_score < 100 and best_score >= 10:
            screen.blit(best_score_image, (360, 385))
        elif best_score < 1000 and best_score >= 100:
            screen.blit(best_score_image, (340, 385))
        elif best_score < 10000 and best_score >= 1000:
            screen.blit(best_score_image, (320, 385))

        animation_choix_mode()

        ############# gestion des événements #############################################

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_over_infini = False
                game = True
                reset_infinie()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0: 
                    game_over_infini = False
                    game = True
                    reset_infinie()
                if event.button == 6: 
                    retour_menu = afficher_regles()
                    if not game:
                        break

        pygame.display.flip()
        clock.tick(60)

    while game_over and running:
        
        screen.fill((0, 0, 0))
        screen.blit(image_fond, (-400 + LARGEUR - 800, 0))
        if LARGEUR == 1200:
            screen.blit(game_over_image, (290, 100))
            screen.blit(image_R, (650+400, 150))
        else:
            screen.blit(game_over_image, (90, 100))
            screen.blit(image_R, (650, 150))
        
        animation_choix_mode()

        ############# gestion des événements #############################################

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(220, 520, 380, 80).collidepoint(event.pos):
                    if LARGEUR == 1200:
                        os.environ['SDL_VIDEO_CENTERED'] = '1'
                        LARGEUR = 800
                        HAUTEUR = 800   
                        screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
                    main_menu = True
                    game_over = False
                if pygame.Rect(220, 610, 380, 80).collidepoint(event.pos):
                    game = True
                    game_over = False 
                    reset()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    retour_menu = afficher_regles()
                    if retour_menu:
                        if LARGEUR == 1200:
                            os.environ['SDL_VIDEO_CENTERED'] = '1'
                            LARGEUR = 800
                            HAUTEUR = 800   
                            screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
                            break
                        break
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0: 
                    if bouton_selectionne == 1: 
                        if LARGEUR == 1200:
                            os.environ['SDL_VIDEO_CENTERED'] = '1'
                            LARGEUR = 800
                            HAUTEUR = 800   
                            screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
                        main_menu = True
                        game_over = False
                    elif bouton_selectionne == 2: 
                        game = True
                        reset()
                        game_over = False 
                if event.button == 6: 
                    retour_menu = afficher_regles()
                    if not game:
                        break

        pygame.display.flip()
        clock.tick(60)
    
    ############# écran de victoire ##################################################

    while victoire and running:
        screen.fill((0, 0, 0))
        screen.blit(image_fond, (-400 + LARGEUR - 800, 0))
        screen.blit(victoire_image, (90, 100))
        screen.blit(image_R, (650, 150))
        
        animation_choix_mode()

        ############# gestion des événements #########################################

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(220, 520, 380, 80).collidepoint(event.pos):
                    main_menu = True
                    reset()
                    victoire = False
                if pygame.Rect(220, 610, 380, 80).collidepoint(event.pos):
                    game = True
                    reset()
                    victoire = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    afficher_regles()
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0: 
                    if bouton_selectionne == 1: 
                        main_menu = True
                        reset()
                        victoire = False
                    elif bouton_selectionne == 2: 
                        game = True
                        reset()
                        victoire = False 
                if event.button == 6: 
                    retour_menu = afficher_regles()
                    if not game:
                        break

        pygame.display.flip()
        clock.tick(60)
    
pygame.quit()