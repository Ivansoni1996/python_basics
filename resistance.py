import tkinter
class Application(object):
    def __init__(self):
        """Constructeur de la fenêtre principale"""
        self.root = tkinter.Tk()
        self.root.title('Code des couleurs')
        self.dessineResistance()
        label1=tkinter.Label(self.root, text ="Entrez la valeur de la résistance, en ohms :")
        label1.grid(row =2, column =1, columnspan =3)
        self.root.focus_set()
        self.root.bind('<Return>',lambda event:self.changeCouleurs())
        #button1=tkinter.Button(self.root, text ='Montrer', command =self.changeCouleurs)
        #button1.grid(row =3, column =1)
        button2=tkinter.Button(self.root, text ='Quitter', command =self.root.quit)
        button2.grid(row =3, column =3)
        self.entree = tkinter.Entry(self.root, width =14)
        self.entree.grid(row =3, column =2)
        # Code des couleurs pour les valeurs de zéro à neuf :
        self.color_code= ['black','brown','red','orange','yellow', 'green','blue','purple','grey','white']
        self.root.mainloop()

    #designe ressistance
    def dessineResistance(self):
        """Canevas avec un modèle de résistance à trois lignes colorées"""
        self.can = tkinter.Canvas(self.root, width=250, height =100, bg ='light blue')
        self.can.grid(row =1, column =2, columnspan =3, pady =5, padx =20)
        self.can.create_line(10, 55, 260, 55, width =0)         # fils
        self.can.create_rectangle(45, 30, 220, 100, fill ='beige', width =0)
        # Dessin des trois lignes colorées (noires au départ) :
        self.ligne =[]          # on mémorisera les trois lignes dans 1 liste
        for x in range(85,150,24):
            self.ligne.append(self.can.create_rectangle(x,30,x+18,100,fill='black',width=0))
    #changer de couleur
    def changeCouleurs(self):
        """Affichage des couleurs correspondant à la valeur entrée"""
        self.vlch = self.entree.get()     # cette méthode renvoie une chaîne
        try:
            v = float(self.vlch)         # conversion en valeur numérique
        except:
            err =1                     # erreur : entrée non numérique
        else:
            err =0
        if v==1 or  v > 1e11 :
            self.signaleErreur()         # entrée incorrecte ou hors limites
            for n in range(3):
               print("the color is changing")
               self.can.itemconfigure(self.ligne[n], fill ='black')
            
        else:
            li =[0]*3                   # liste des 3 codes à afficher
            from math import log10
            logv = int(log10(v))         # partie entière du logarithme
            ordgr = 10**logv             # ordre de grandeur
            li[0] = 0        # partie entière
            #decim = v/ordgr - li[0]      # partie décimale
            # extraction du premier chiffre significatif :
            li[1] = int(v/ordgr)  
            # nombre de zéros à accoler aux 2 chiffres significatifs :
            li[2] = logv -1    # +.5 pour arrondir correctement
            # Coloration des 3 lignes :
            for n in range(3):
                self.can.itemconfigure(self.ligne[n], fill =self.color_code[li[n]])
    def signaleErreur(self):
        self.entree.configure(bg ='red')         # colorer le fond du champ
        self.root.after(1000, self.videEntree)    # après 1 seconde, effacer

    def videEntree(self):
        self.entree.configure(bg ='white')         # rétablir le fond blanc
        self.entree.delete(0, len(self.vlch))     # enlever les car. présents

    # Programme principal
if __name__ == '__main__':
    # logarithmes en base 10

    from tkinter import *
    from math import log10
    f = Application()   