# !/usr/bin/python3

# pokus o integrální pracovní prostředí Worplace Intelligence

import os
import os.path
import re
from pathlib import Path
from datetime import datetime
import time
import glob
import sys

def main():

	'''
	WORPI je určen výhradně pro vývoj a testování; finální podoby, byť verzované, soubory _b nepotřebují.

	Cíl pro rok 2022: >> VNITŘNÍ MÍR <<
	'''
	print(main.__doc__) # vyprintí dokumentaci o řádek výše
	print()
	a = int(input('1 = založení nového projektu, 2 = založení souboru, 3 = úpravy, 4 = doplňky, 5 = ukončení programu: '))
	if a == 1:
		print()
		print('NOVÝ MODUL:')
		create_folder_file()
	if a == 2:
		print()
		print('NOVÝ MODUL:')
		create_file_only()
	if a == 3:
		print()
		print('NOVÝ MODUL:')
		updates_v2()
	if a == 4:
		print()
		print('NOVÝ MODUL:')
		plugins()
	if a == 5:
		sys.exit()


def create_file_only():
	'''
	- kde chceš tu file?:
	=> stejný princip jako u updates_v2() => vytvořit na to modul, fci nebo třídu, protože vyhledávání folder se tu často objevuje
	'''
	list = {} # pro uchování vektoru (číslo adresy dle řádku adresy, adresa)
	list_x = {}
	cur_adr = os.path.expanduser('~')
	#################################################################################################

	x1 = input('adr. nadřazené složky bez "~": ')
	x2 = cur_adr + '/' + x1 + '*'
	x_abs_path = os.path.abspath(x2)
	x_i = 0 # pro iteraci cyklu
	x3 = glob.glob(x_abs_path) # v x3 jsou teď adr.složek do první úrovně vnoru zadané nadsložky 
	print('počet prvků v seznamu adres je: ', len(x3))
	for i in range(len(x3)):
		# print(x3[i]) # odtud mě to napadlo
		x_i += 1
		list_x.update({x_i:(x3[i])}) # do list_x se teď postupně zadávají klíče(č.adr.) a abs.adr.z x3

	for klic_x, hodnota_x in list_x.items():
		print('{}: {}'.format(klic_x, hodnota_x))

	a = int(input('zadej č. adr.: '))
	b = list_x[a] # v 'b' je teď abs.adr.dle čísla zadaného uživatelem, pomocí list_x 
	abs_path = os.path.abspath(b)
	print('výstup z abs_path:', abs_path)
	print()
	# os.system('cd {}'.format(abs_path))
	b_f = input('zadej název souboru: ')
	path_b = b + '/' + b_f
	abs_path_b = os.path.abspath(path_b)
	print('výstup z abs_path_b: ', abs_path_b)
	with open(abs_path_b, 'w') as soubor:
		pass
	os.system('nano {}'.format(abs_path_b))

def create_folder_file(): # vytvoří file + automaticky file ..._b.py(nebo cokoli) pro použití diff -r
	t = datetime.now()
	t_m = t.strftime('%d.%m.%Y %H.%M.%S')
	cur_adr = os.path.expanduser('~') # abych se nemusel dřít s home/marcel/
	adr = input('zadej adresu bez ~, tedy bez home/.../(formát: .../.../): ') # zadání /.../.../.../
	ca = cur_adr + '/' + adr
	name = input('zadej název souboru: ') # zadání jména souboru bez přípony
	suffix = input('přípona souboru: ') # zadání přípony souboru
	ns = name + '.' + suffix
	abs_adr_file_a = os.path.abspath(ca + ns)
	suffix_b = '_b'
	abs_adr_file_b = os.path.abspath(ca + name + suffix_b + '.' + suffix) # kompletní název automat.vytvořeného souboru s _b
	os.system('mkdir {}'.format(ca)) # založí v rámci procesu nového projektu složku ze zadaného input
	# os.system('cd {}'.format(ca)) # přepne se do zadané adresy
	with open(abs_adr_file_a, 'w') as soubor1: # vytvoří soubor dle zadání input
		pass
		print('název souboru ''a'': ', ns)
	with open(abs_adr_file_b, 'w') as soubor2: # vytvoření ..._b souboru po diff -r
		pass
	adr_his = os.path.abspath(ca + 'his.txt')
	adr_doc = os.path.abspath(ca + 'doc.txt')
	with open(adr_his, 'w') as soubor3: # vytvoří his file
		pass
	with open(adr_doc, 'w') as soubor4: # vytvoří doc file
		print(t_m, file=soubor4)

	# os.system('date >> doc.txt') # první, co se stane: do doc.txt se zavazbí aktuální datum
	# os.system('nano doc.txt') # druhé, co se stane: otevře se nano s doc souborem, abych napsal, o co v projektu vlastně jde
	os.system('nano {}'.format(abs_adr_file_a))

def m_nano_doc(): # otevře nano pro úpravu .xy source souboru zadané adr. protože už budu přepnutý do adr., nepotřebuji ji; stačí jméno souboru
	(a, b) = create_file() # nefunguje: nevrací adresu a název souboru = projede se tedy celá fce create_file()
	c = 'doc.txt'
	# os.system('cd {}'.format(a)) # přepne se do zadané adr.
	os.system('nano {}'.format(c)) # otevře nano v již založeném souboru pro dokumentaci 'doc.txt'
'''
def m_nano_source(): # užívá jméno souboru
	(a, b) = create_file()
	os.system('nano {}'.format(b))
'''
def create_his_file(): # vytvoří, pokud bude třeba, history file pro uložení historie změn verzí
	with open('his.txt', 'w') as soubor:
		pass

def create_doc_file(): # vytvoří dokumentační soubor, abych věděl, o čem ten projekt vlastně je a bude
	with open('doc.txt', 'w') as soubor: # vytvoří dokumentační soubor, abych věděl, o čem ten projekt vlastně je a bude
		pass

def create_folder(): # vytvoří složku
	adr = str(input('adr.(.../.../): ')) # zadání /.../.../.../
	name = str(input('jméno souboru: ')) # zadání jména souboru bez přípony
	an = adr + name
	os.system('mkdir {}'.format(an))

def diff_file_compare(): # porovná files v aktuální složce; půjde i do modulu 'úpravy'
	'''
	předpokládá, že porovná soubory v aktuální složce; půjde i do modulu 'úpravy'
	'''
	print(diff_file_compare.__doc__)
	print(os.system('pwd'))
	# os.system('date >> his.txt')
	# os.system('diff -r {} {} >> his.txt'.format(a, b))
	# os.system('cat his.txt')
	# os.system('cp {} {}'.format(a, b)) # potom, co porovná a zapíše změny,musí cp a->b,jinak bude diff -r zapisovat i staré změny=
					   # duplicita změn
def wiu_v3():
	'''
	vrátí jméno souboru ve složce 'python', ve které se něco měnilo v aktuálním datumu;  toto se pak může upload na cloud nebo flash
	'''
	print(wiu_v3.__doc__)
	print()
	t = datetime.now()
	t_main = t.strftime('%d.%m.%Y')
	a = str(input('zadej absolutní adresu složky ve formě /.../.../: '))
	for path, subdir, files in os.walk(a):
		for name in files:
			o = os.path.join(path, name)
			x = os.stat(o)
			y = time.localtime(x.st_mtime)
			z = time.strftime('%d.%m.%Y %H.%M.%S', y)
			w = str(z)
			if t_main in w:
				print(o,'', 'ZMĚNĚNO DNE: ', w)
def plugins(): # doplňky
	a = int(input('1 = wiu, 2 = úkoly, 3 = asist: '))
	if a == 1:
		wiu_v3()
	if a == 2:
		print('úkoly:')
		os.system('python todo.py')
	if a == 3:
		os.system('python asist.py')

def updates_v2(): 
	'''
	verze, ve které se nejdříve zadá nadřazená složka, ve které 'tuším', že existuje hledaná složka kýženého projektu
	což ovšem znamená, že pokud v ní tu složku nenajdu, musím mít možnost bezbolestně se vrátit zpět do programu
	'''
	list = {} # pro uchování vektoru (číslo adresy dle řádku adresy, adresa)
	list_x = {}
	cur_adr = os.path.expanduser('~')
	#################################################################################################
	'''
	zkusím to glob.glob(), protože výstup je asi seznam všech adres a prvky tohoto seznamu bych 
	nějak dal do slovníku, tak, aby byl přijatelný print() s key = číslo abs.adr.: abs.adr.
	'''

	x1 = input('adr. nadřazené složky bez "~": ')
	x2 = cur_adr + '/' + x1 + '*'
	x_abs_path = os.path.abspath(x2)
	x_i = 0 # pro iteraci cyklu
	x3 = glob.glob(x_abs_path) # v x3 jsou teď adr.složek do první úrovně vnoru zadané nadsložky 
	print('počet prvků v seznamu adres je: ', len(x3))
	for i in range(len(x3)):
		# print(x3[i]) # odtud mě to napadlo
		x_i += 1
		list_x.update({x_i:(x3[i])}) # do list_x se teď postupně zadávají klíče(č.adr.) a abs.adr.z x3

	for klic_x, hodnota_x in list_x.items():
		print('{}: {}'.format(klic_x, hodnota_x))

	##################################################################################################

	a = int(input('zadej č. adr.: '))
	b = list_x[a] # v 'b' je teď abs.adr.dle čísla zadaného uživatelem, pomocí list_x 
	abs_path = os.path.abspath(b)
	os.system('cd {}'.format(abs_path))
	i = 0 # pro zjištění, kolik iterací cyklu proběhlo, protože iterace = číslo adr.
	for path, subdir, files in os.walk(abs_path):
		for name in files:
			o = os.path.join(path, name)
			i += 1
			list.update({i:(o)})
	for klic, hodnota in list.items():
		print('{}: {}'.format(klic, hodnota))
	print()
	c = int(input('číslo adresy pro otevření: '))
	d = list[c] # stačí vložit prom. obsahující klíč a ten do další pro. zavazbí adresu tohoto klíče => prom. v 'd' obsahuje adresu
	d_str = str(d) # d převedeno na string proto, aby se do his.txt zavazbila adr. porovnávaného souboru 
	print(d)
	e = new_str_b(d) # teď je v e adr. pro otevření, 'e' tedy po projetí fce new_str_b obsahuje _b verzi souboru 'a' 
	os.system('nano {}'.format(d))

	'''
	automaticky se musí zapsat do his.txt rozdíl mezi souborem 'a' a '_b'
	do his.txt musí ale jít i název souboru, protože je to společný soubor 
	historie změn pro všechny soubory dané složky
	'''
	####################################################################################################################
	his = '/his.txt'
	his_path = b + his
	abs_path_his = os.path.abspath(his_path)
	print('výstup z abs_path_his: je tam adr. nebo není?', abs_path_his)
	os.system('date >> {}'.format(abs_path_his)) # mám tady ale abs_path, takže stačí k ní přidat / a his.txt
	with open(abs_path_his, 'a') as soubor: # zapíše se název souboru, který byl prověřován na diff -r
		print(d_str,file=soubor)
	os.system('diff -r {} {} >> {}'.format(d_str, e, abs_path_his))
	# teď ale se musí cp -> _b souboru, aby se v příští seanci projevily nové změny provedené v <t2>
	os.system('cp {} {}'.format(d_str, e))
	os.system('cat {}'. format(abs_path_his))
	######################################################################################################################


def updates(): # přepne se do zadané adr., vytvoří číselný seznam souborů této složky a user může dle čísla vybrat, jaký soubor chce upravovat
	'''
	přepne se do zadané adr., vytvoří číselný seznam souborů této složky a user může dle čísla vybrat, jaký soubor chce upravovat
	'''
	list = {} # pro uchování vektoru (číslo adresy dle řádku adresy, adresa)
	cur_adr = os.path.expanduser('~')
	a = input('zadej adr. bez "~": ')
	b = cur_adr + '/' + a
	abs_path = os.path.abspath(b)
	os.system('cd {}'.format(abs_path))
	print('nyní jsem v adrese:', os.system('pwd'))
	i = 1 # pro zjištění, kolik iterací cyklu proběhlo, protože iterace = číslo adr.
	for path, subdir, files in os.walk(abs_path):
		for name in files:
			o = os.path.join(path, name)
			i += 1
			list.update({i:(o)})
	for klic, hodnota in list.items():
		print('{}: {}'.format(klic, hodnota))
	print()
	c = int(input('číslo adresy pro otevření: '))
	d = list[c] # stačí vložit prom. obsahující klíč a ten do další pro. zavazbí adresu tohoto klíče => prom. v 'd' obsahuje adresu
	d_str = str(d) # d převedeno na string proto, aby se do his.txt zavazbila adr. porovnávaného souboru 
	print(d)
	e = new_str_b(d) # teď je v e adr. pro otevření, 'e' tedy po projetí fce new_str_b obsahuje _b verzi souboru 'a' 
	os.system('nano {}'.format(d))
	'''
	automaticky se musí zapsat do his.txt rozdíl mezi souborem 'a' a '_b'
	do his.txt musí ale jít i název souboru, protože je to společný soubor 
	historie změn pro všechny soubory dané složky
	'''
	####################################################################################################################
	his = 'his.txt'
	his_path = b + his
	abs_path_his = os.path.abspath(his_path)
	os.system('date >> {}'.format(abs_path_his)) # mám tady ale abs_path, takže stačí k ní přidat / a his.txt
	with open(abs_path_his, 'a') as soubor: # zapíše se název souboru, který byl prověřován na diff -r
		print(d_str,file=soubor)
	os.system('diff -r {} {} >> his.txt'.format(d_str, e))
	# teď ale se musí cp -> _b souboru, aby se v příští seanci projevily nové změny provedené v <t2>
	os.system('cp {} {}'.format(d_str, e))
	os.system('cat his.txt')
	######################################################################################################################

def new_str_b(a): # vstoupí do ní adr. z 'd' z updates()
	'''
	pro vytvoření _b verze pro diff_file_compare: vytvoří z 'a' verze adresy _b verzi, takže se nebude muset zadávat 
	přes input nová adr. kvůli porovnávání dvou souborů
	'''
	b = a.split('/')
	c = len(b)
	c = c - 1
	d = b[c] # teď je v d poslední prvek seznamu b
	e = d.split('.')
	f = '_b'
	g = e[0]
	h = e[1]
	new = g + f + '.' + h
	return new

while True:
	main()

# updates_v2()
# create_file_only()
