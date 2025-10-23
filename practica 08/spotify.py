from time import sleep
from os import system
system ("cls")
playlist_music=["Bohemia rhapsody","Hotel California","Stairway to heaven","B.Y.O.B"]
print(playlist_music)
playlist_music[1]="shape of you"
print (playlist_music)
playlist_music.insert(0,"watermelon sugar")
print (playlist_music)
playlist_music.pop()
print(playlist_music)

input("Press Enter to continue...")
opcion=int (input("Elige una cancion de la lista del 0 al 3: "))
while opcion>0 or opcion<3:
    print("Reproduciendo..." + playlist_music[opcion])
    for i in range(3):
        print (".")
        sleep(1)
    desea_cambiar=int(input("Desea cambiar de cancion? 1.Si| 2.No: "))
    if desea_cambiar==1: 
        opcion=int (input("Elige una cancion de la lista del 0 al 3: "))
    else:
        print("Gracias por usar Spotify")
        break