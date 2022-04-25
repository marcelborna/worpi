# !/usr/bin/python3

# pauzy s viditelným odpočítáváním v bash ve skutečných cyklech
# 19112021: zavést zvukové návěstí pro pauzu!!! + vypnutí monitoru: if 20:50 => shutdown now -h
# opravit nefunkčnost def shut

from time import time, sleep
from datetime import datetime
#from subprocess import check_call
import pyautogui
import os
from PIL import Image
import schedule
import time

t_time = '21:10'
shut_time = '21:49'
def beep():
	for i in range(1, 2):
		os.system('beep -f 555 -l 460')

def pauza_hlaseni():
	pyautogui.alert("Ulož si to! Za chvíli přijde pauza!",title="Výzva k uložení") # viz modul pyautogui
	im = Image.open('1.jpg') # viz modul PIL a Image
	im.show()

def konec():
	pyautogui.alert("Ulož si to! Za 10 minut přijde KONEC!",title="Výzva k uložení")

def shut():
	# Do some work that only needs to happen once...
	os.system("shutdown")  # tohle je snad jasné :)

def do_som():
	beep()
	for i in range(1, 45): # 1, 45
		a = c_time()
		countdown(a)
		t = sleep(60) # (60) minuta
		print('dělej něco!!!', i)
	beep() # po skončení cyklu se ozve beep a nahlásí se pauza
	pauza_hlaseni()

def do_not():        # teď musí dojít k odpočítávání pauzy
	for j in range(1, 10): # 1, 30
		a = c_time()
		countdown(a)
		t = sleep(60) # (60) minuta
		print('klííííídek!', j)	

def c_time(): # převede aktuální čas na string
	t_now =	datetime.now()
	dt = t_now.strftime('%H:%M')
	return dt

def main():
	'''
	UPRAVENO NA 45 MINUT PRÁCE NA PC A 10 MINUT PAUZA
	'''
	print(os.system.__doc__)
	while True:
		do_som()
		do_not()

def countdown(tm):
	tm = c_time()
	if tm == t_time:
		konec()
		for i in range(1,600): # odpočítávání, neboli reverzní cyklus: 10 minut
			t = sleep(1)
			x = 600
			y = x - i
			print('do vypnutí zbývá sekund: ',y)
		shut()

	# schedule.every().day.at('20:50').do(konec) # upozornění před shutdown now

# tady musí být fce zavazbená do schedule.every().day.at('20:52').do(jméno nové fce), která ze zaznamenaných složek a 
# souborů budu volat apl. 'transfer.py', která vezme všechny soubory ze složky home/marcel/marcel_backup/python/, kde se něco
# změnilo a ty pomocí pyautogui a auomatického klikání zavazbí do předem dané složky v cloudu)

	# schedule.every().day.at('21:10').do(shut) # provede shutdown now -h

main()

