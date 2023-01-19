import pyautogui
import time 
import keyboard
import webbrowser

def pornire_wapserver():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\Bot(site)\poza1.png', confidence=0.7) != None:
        pornire_wap = pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\Bot(site)\poza1.png', confidence=0.7)
        pyautogui.click(pornire_wap)
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")
        
pornire_wapserver()

time.sleep(15)
webbrowser.open("localhost/travel website/home")

time.sleep(2)
keyboard.press('esc')

def acces_book():
    time.sleep(2)
    if pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\Bot(site)\poza2.png', confidence=0.7) != None:
        accesare = pyautogui.locateOnScreen(r'C:\Users\Tudor\Desktop\Univer\Metode avansate de programare\Laborator\Bot(site)\poza2.png', confidence=0.7)
        pyautogui.click(accesare)
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")
        
acces_book()

time.sleep(3)
pyautogui.scroll(-600)

time.sleep(1)
pozitie_initiala_x1 = 447
pozitie_initiala_y1 = 296
pozitie_initiala_x2 = 1131
pozitie_initiala_y2 = 295

name = "Alin"
email = "alin.rebreanu@gmail.com"
phone = "0779456325"
address = "Calea Marasesti 157"
where_to = "Londra"
how_many = "3"
arrivals = "0922023"
leaving = "1522023"

pyautogui.click(pozitie_initiala_x1,pozitie_initiala_y1)
pyautogui.write(name)
time.sleep(1)

pyautogui.click(pozitie_initiala_x2,pozitie_initiala_y2)
pyautogui.write(email)
time.sleep(1)

pozitie_initiala_y1 = pozitie_initiala_y1 + 150
pozitie_initiala_y2 = pozitie_initiala_y2 + 150

pyautogui.click(pozitie_initiala_x1,pozitie_initiala_y1)
pyautogui.write(phone)
time.sleep(1)

pyautogui.click(pozitie_initiala_x2,pozitie_initiala_y2)
pyautogui.write(address)
time.sleep(1)

pozitie_initiala_y1 = pozitie_initiala_y1 + 140
pozitie_initiala_y2 = pozitie_initiala_y2 + 140

pyautogui.click(pozitie_initiala_x1,pozitie_initiala_y1)
pyautogui.write(where_to)
time.sleep(1)

pyautogui.click(pozitie_initiala_x2,pozitie_initiala_y2)
pyautogui.write(how_many)
time.sleep(1)

pozitie_initiala_y1 = pozitie_initiala_y1 + 140
pozitie_initiala_y2 = pozitie_initiala_y2 + 140

pyautogui.click(pozitie_initiala_x1,pozitie_initiala_y1)
pyautogui.write(arrivals)
time.sleep(1)

pyautogui.click(pozitie_initiala_x2,pozitie_initiala_y2)
pyautogui.write(leaving)
time.sleep(1)

pozitie_submit_x = 291
pozitie_submit_y = 801

pyautogui.click(pozitie_submit_x,pozitie_submit_y)

# while not keyboard.is_pressed('esc'):
#     print(pyautogui.position())