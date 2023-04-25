import pyautogui
import time
import keyboard


cps = int(input("Combien de clics par seconde voulez-vous effectuer ?  7 max"))
print("appuyez sur H pour démarer les clics")
print("appuyez sur Y pour mettre en pause")
print("appuyez sur U pour mettre reprendre")
print("appuyez sur I pour fermer le programme")


clics_en_cours = False

while True:
    if keyboard.is_pressed('i'):
        print("Programme terminé")
        break
    elif keyboard.is_pressed('h'):
        if not clics_en_cours:
            clics_en_cours = True
            print("Clics en cours")
        else:
            print("Clics déjà en cours")
    elif keyboard.is_pressed('y'):
        if clics_en_cours:
            clics_en_cours = False
            print("Programme en pause")
        else:
            print("Clics non en cours")
            time.sleep(1)
    elif keyboard.is_pressed('u'):
        if not clics_en_cours:
            clics_en_cours = True
            print("Clics repris")
        else:
            print("Clics déjà en cours")
    if clics_en_cours:
        pyautogui.click(button='left')
        time.sleep(1/cps)