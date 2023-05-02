#import sys, Ice
#import Demo
 #
#with Ice.initialize(sys.argv) as communicator:
#    base = communicator.stringToProxy("SimplePrinter:default -p 10000")
#    printer = Demo.PrinterPrx.checkedCast(base)
#    if not printer:
#        raise RuntimeError("Invalid proxy")
 
#    printer.printString("Hello World!")

import sys, Ice, os
import Demo
import IceGrid

Ice.loadSlice('Printer.ice')

import sqlite3

connectionDatabase = sqlite3.connect('DataBase.db', check_same_thread=False)
cursorDatabase = connectionDatabase.cursor()




def run(communicator):
    hello = None
    try:
        hello = Demo.PrinterPrx.checkedCast(communicator.stringToProxy("printer"))
    except Ice.NotRegisteredException:
        query = IceGrid.QueryPrx.checkedCast(communicator.stringToProxy("DemoIceGrid/Query"))
        hello = Demo.PrinterPrx.checkedCast(query.findObjectByType("::Demo::Printer"))

    if not hello:
        print("couldn't find a `::Demo::Printer' object.")
        sys.exit(1)

    menu()

    c = None
    while c != 'x':
        sys.stdout.write("==> ")
        sys.stdout.flush()
        c = sys.stdin.readline().strip()
        if c == 't':
            hello.sayHello()
        elif c == 's':
            hello.shutdown()
        elif c == 'x':
            pass  # Nothing to do
        elif c == '?':
            menu()
        else:
            print("unknown command `" + c + "'")
            menu()


def menu():
    print("""
        usage:
        t: send greeting as twoway
        s: shutdown server
        x: exit
        ?: help
        """)





def MusiquesClient():
    # listeMusiques= os.listdir('/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/ice/Musiques/')
    listeMusiques= os.listdir('/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/middlware/ice/clientmusique')

    
    for name in listeMusiques:
        print(name.replace(".mp3",''))



with Ice.initialize(sys.argv, "config.client") as communicator:
    try:
        #
        # The communicator initialization removes all Ice-related arguments from argv
        #
        # if len(sys.argv) > 1:
        #     print(sys.argv[0] + ": too many arguments")
        #     sys.exit(1)

        # run(communicator)

        # base = communicator.stringToProxy("SimplePrinter:default -p 10000")
        base = communicator.stringToProxy("SimplePrinter:tcp -h 10.126.2.115 -p 10000")
        printer = Demo.PrinterPrx.checkedCast(base)
        if not printer:
            raise RuntimeError("Invalid proxy")
        else:
            #MusiquesClient()
            path = os.path.dirname(os.path.abspath(__file__))
            print(path)
            nbMusiques=printer.GetNumberOfMusics()
            print(nbMusiques, " musiques sont disponibles")
            for i in range(nbMusiques):
                musique = printer.GetMusiques(i)
                print(musique[0],' ', musique[1],' ', musique[2],' ',musique[3])


            while True:
                print("----------------------------------------------")
                print("Que voulez vous faire ?")
                print("* Pour afficher  les musiques merci de taper \'afficher\'")

                print("* Pour chercher un Artiste merci de taper  \'artiste\'")

                print("* Pour chercher un Titre merci de taper \'titre\' ")

                print("* Pour Ajouter une Musique merci de taper \'ajouter\'")

                print("* Pour Modifier une Musique merci de taper \'modifier\'")

                print("* Pour Supprimer une Musique merci de taper \'supprimer\'")

                print("* Pour Lancer une Musique merci de taper \'play\'")

                print("* pour Stoper une Musique merci de taper \'pause\'")

                print("* pour Arreter une Musique merci de taper \'stop\'")


                print("* Pour Quitter notre application merci taper \'quitter\'")
                print("C'est a vous de saisir qu'est ce que vous avez choisi")

                print("*****************************************************")
                choice = input()
                    # Afficher les Musiques 
                if choice.lower() == "afficher":
                    try:
                        cursorDatabase.execute("SELECT Titre FROM Musiques ORDER BY Titre ")
                        for row in cursorDatabase:
                            print(row[0])
                    except Exception as e:
                        print("Une erreur s'est produite lors de l'affichage des musiques : ", e)
                    except sqlite3.Error as error:
                        print("Erreur lors de la récupération des données de la base de données : ", error)

                    # Ajouter Musique 

                elif choice.lower()== "ajouter":
                    
                    try:
                        MusiquesClient()
                        #musique=[]
                        titre=input("Titre de la chanson à ajouter : ")
                        artistes=input("Artistes : ")
                        album=input("Album : ")
                        # fichier = "/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/middlware/ice/Musiques/"+titre+".mp3"
                        fichier = "/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/middlware/ice/clientmusique/"+titre+".mp3"
                        
                        urlStream = "sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:3000/"+titre.replace(".mp3",'')+"}"

                        file = open(fichier,'rb')
                        chunkSize = 10000
                        offset = 0
                        results = []
                        numRequests = 5    
                        remotePath = "/Users/ACER/Desktop/cours/Master/M1/S2/Architecture distributé/middlware/ice/Musiques/" + titre + ".mp3"

                        #while True:
                        chunck = file.read(chunkSize)
                        if chunck == bytes('','utf-8') or chunck == None:
                            raise Exception("Impossible de lire le fichier !")
                        r = printer.begin_AjtMusique(offset, chunck, remotePath, titre, artistes, album)
                        offset += len(chunck)

                        r.waitForSent()
                        results.append(r)
                        
                        while len(results) > numRequests:
                            r = results[0]
                            del results[0]
                            r.waitForCompleted()
                        
                        while len(results) > 0:
                            r = results[0]
                            del results[0]
                            r.waitForCompleted()
                        printer.AjtMusiqueDatabase(titre, artistes, album)
                        print("Musique ajoutée avec succès !")
                    except Ice.Exception as ex:
                        print("Une exception Ice a été levée lors de l'ajout de la musique : ", ex)
                    except Exception as ex:
                        print("Une exception a été levée lors de l'ajout de la musique : ", ex)



                elif choice.lower()=="modifier":
                    try: 
                        cursorDatabase.execute("SELECT Titre FROM Musiques ")
                        for row in cursorDatabase:
                            print(row[0])
                        musique = input("Entrez le nom de la musique à modifier : ")
                        nouveauTitre = input("Entrez le nouveau titre , ou laissez vide si vous voulez le laisser comme ceci : ")
                        nouveauxArtistes = input("Entrez le nom des artistes , ou laissez vide si vous voulez les laisser comme ceci : ")
                        nouvelAlbum = input("Entrez le nouvel album , ou laissez vide si vous voulez le laisser comme ceci : ")
                        #printer.ModifMusique(musique, nouveauTitre, nouveauxArtistes, nouvelAlbum)
                        printer.ModifMusique(musique, nouveauTitre, nouveauxArtistes, nouvelAlbum)
                        print("La musique a été modifiée avec succès.")
                    except Exception as e:
                        print("Une erreur s'est produite lors de la modification de la musique : ", e)
                    except sqlite3.Error as error:
                        print("Erreur lors de la modification des données de la base de données : ", error)



                    # Delete Music

                elif choice.lower() == "supprimer":
                    try: 
                        cursorDatabase.execute("SELECT Titre FROM Musiques ")
                        for row in cursorDatabase:
                            print(row[0])
                        a_supprimer=input("Entrez le nom de la musique à supprimer : ")
                        printer.DeleteMusic(a_supprimer)
                    except Exception as e:
                        print("Erreur lors de la suppression de la musique.", e)
                    except sqlite3.Error as error:
                        print("Erreur lors de la suppression des données de la base de données : ", error)

                # lancer music

                elif choice.lower() == "play":
                    try:

                        cursorDatabase.execute("SELECT Titre FROM Musiques ")
                        for row in cursorDatabase:
                            print(row[0])
                        musique_a_jouer = input("Entrez le nom de la musique à jouer : ")
                        print(printer.Play(musique_a_jouer))
                    except sqlite3.Error as error:
                        print("Erreur lors de la récupération des données de la base de données : ", error)

                #elif choice.lower() == "play":
                 #   cursorDatabase.execute("SELECT Titre FROM Musiques ")
                 #   for row in cursorDatabase:
                #        print(row[0] + ".mp3")
               #     musique_a_jouer = input("Entrez le nom de la musique à jouer : ")
               #     print(printer.Play(musique_a_jouer.replace(".mp3", "")))


                # mettre la music en paue
                elif choice.lower() == "pause":
                    try:
                        print(printer.Pause())
                        print("La musique a été mise en pause.")
                    except:
                        print("Erreur lors de la mise en pause de la musique.")

                # arreter la music 
                elif choice.lower() == "stop":
                    try:
                        print(printer.Stop())
                        print("La musique a été arrêtée.")
                    except:
                        print("Erreur lors de l'arrêt de la musique.")


                    # Recherche Artiste 

                elif choice.lower() == "artiste":
                    # artiste = input("Entrez le(s) artistes que vous voulez rechercher : ")
                    # Artistes = printer.SearchArtist(artiste)
                    # for i in range(len(Artistes)):
                    #     print(Artistes[i])
                    try:
                        artiste = input("Entrez le artistes que vous voulez rechercher : : ")
                        Artistes = printer.SearchArtist(artiste)
                        if len(Artistes) == 0:
                            print("Aucun résultat trouvé pour cet Artiste.")
                        else:
                            for i in range(len(Artistes)):
                                print(Artistes[i])
                    except Exception as e:
                        print("Une erreur s'est produite lors de la recherche d'Artiste : ", e)


                    # Recherche Titre 

                elif choice.lower() == "titre":
                    # titre = input("Entrez le titre que vous voulez rechercher : ")
                    # Titres = printer.SearchTitle(titre)
                    # for i in range(len(Titres)):
                    #     print(Titres[i])
                    try:
                        titre = input("Entrez le titre que vous voulez rechercher : ")
                        Titres = printer.SearchTitle(titre)
                        if len(Titres) == 0:
                            print("Aucun résultat trouvé pour ce titre.")
                        else:
                            for i in range(len(Titres)):
                                print(Titres[i])
                    except Exception as e:
                        print("Une erreur s'est produite lors de la recherche de titres : ", e)

                    # Quitter 

                elif choice.lower() == "quitter":
                    # print("¨_^")
                    print("Merci pour votre confiance et a tres bientot ^_^")


                    break 
                    

            run(communicator)

    except Ice.Exception as ex:
        # print("Une exception Ice a été levée lors de l'ajout de la musique : ", ex)
        print(" ")