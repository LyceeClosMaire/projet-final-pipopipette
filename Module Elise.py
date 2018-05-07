point=1
case_vide=0

point_par_cote = 4
taille_tableau1 = point_par_cote*2-1
aire_jeu=[]
for ligne in range(0,taille_tableau1):
        aire_jeu.append([])
        for colonne in range(0,taille_tableau1):
            if ligne%2==1: ##Si la ligne est impaire
                aire_jeu[ligne].append(0)
            else:
                if colonne%2==1: ##Si la colonne est impaire
                    aire_jeu[ligne].append(0)
                if colonne%2==0: ##Si la colonne est paire
                    aire_jeu[ligne].append(1)


point_par_cote2 = 6
taille_tableau2 = point_par_cote2*2-1
aire_jeu2=[]
for ligne in range(0,taille_tableau2):
        aire_jeu2.append([])
        for colonne in range(0,taille_tableau2):
            if ligne%2==1: ##Si la ligne est impaire
                aire_jeu2[ligne].append(0)
            else:
                if colonne%2==1: ##Si la colonne est impaire
                    aire_jeu2[ligne].append(0)
                if colonne%2==0: ##Si la colonne est paire
                    aire_jeu2[ligne].append(1)


point_par_cote3 = 9
taille_tableau3 = point_par_cote3*2-1
aire_jeu3=[]
for ligne in range(0,taille_tableau3):
        aire_jeu3.append([])
        for colonne in range(0,taille_tableau3):
            if ligne%2==1: ##Si la ligne est impaire
                aire_jeu3[ligne].append(0)
            else:
                if colonne%2==1: ##Si la colonne est impaire
                    aire_jeu3[ligne].append(0)
                if colonne%2==0: ##Si la colonne est paire
                    aire_jeu3[ligne].append(1)


joueur_1=2
joueur_2=3
score1=0
score2=0

for colonne in aire_jeu:
    for ligne%2==1:


        score1+=1






