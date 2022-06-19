
class Salle :
    def __init__(self,name,movie,time) :
        self.name = name 
        self.movie = movie 
        self.time = time
    def get_name (self) :
        return self.name 
    def get_movie (self) :
        return self.movie 
    def get_time (self) :
        return self.time 

Salle_1 = Salle (1, "Tchoupie a l'école magique",2.5)
Salle_2 = Salle (2, "Titanic the amazing return",4)
Salle_3 = Salle (3,"Sur le flux des résaux sociaux", 1.3)
Salle_4 = Salle (4, "L'Avare", 2)

All = [Salle_1,Salle_2,Salle_3,Salle_4]
print ("Bienvenu au cinéma,")
for Film in All :
    print ("il y a la salle "+ str(Film.get_name()) + " qui diffuse le film "+ str(Film.get_movie())+" qui dure a peut pres "+ str(Film.get_time())+" Heure")
# Faire une boucle while tant que on a pas trouver la salle que on veut

Room_correct = False 
while Room_correct == False :
    Salle_Player =  int(input ("Quelle Salle Voullez vous "))
    Tentative = 0
    for Salle_CP in All :
        if Salle_Player == Salle_CP.get_name () :
            print ("OK")
            Adulte = input ("Combien d'adulte va voir le film ? ")
            Enfant = input ("Combien d'enfant ? ")
            prix = float(Adulte) * 25 * Salle_CP.get_time() + float(Enfant) * 15 * Salle_CP.get_time()
            Popcorn = input ("Voullez vous du pocorne o/n ")
            if Popcorn == "o" :
                Type_popcorne = int(input ("Quelle taille : 1 Petit (10$) , 2 Moyen(25$) , 3 Grand(30$)"))
                if Type_popcorne == 1 :
                    prix += 10
                elif Type_popcorne == 2 :
                    prix += 25
                elif Type_popcorne == 3 :
                    prix += 30
                else :
                    print ("Ok , j'annule le popcorn ") 
            print ("Tres bien , cela fera un total de ", prix , "$")
            Room_correct = True


        elif Tentative >= len(All) :
            print ("Vous vous etes tromper, je recommence")
            break
    
        else : 
            Tentative += 1    
            continue 
    