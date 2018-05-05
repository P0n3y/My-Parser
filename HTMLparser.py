# -*- encoding: utf-8 -*-

import requests
import sys, os
import bs4 as BeautifulSoup

from time import sleep

from sgmllib import SGMLParser
from colors import *

import FormulaireParser

color = Color()

def loading(base, string, nmbr, t):
	sys.stdout.write(base)
	x = 0
	while x < nmbr :
		sys.stdout.write(string)
		sleep(t)
		sys.stdout.flush()
		x += 1
	sys.stdout.write("\n")
	sys.stdout.flush()

class URLLISTER(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.urls = []

	def start_a(self, attrs):
		href = [v for k, v in attrs if k == 'href' ]
		if href :
			self.urls.extend(href)

def Requester(url):
	get = requests.get(url)
	put = requests.put(url)
	return (get.text, put.text,)

class Analyste :
	def __init__(self, url):
		loading(color.white + "[" + color.green + "  *" + color.white + "  ] starting Scan ", ".", 3, 0.3)

		self.url 			= url

		r 				= Requester(url)
		self.soup1 			= BeautifulSoup.BeautifulSoup(r[0])
		self.soup2 			= BeautifulSoup.BeautifulSoup(r[1])

		self.LinksGet 			= []
		self.FormulairesGet 		= []

		self.LinksPut 			= []
		self.FormulairesPut 		= []

		self.PayloadFormGet 		= []
		self.PayloadFormPut 		= []

		self.FORMULARY_SHORTED_GET 	= []
		self.FORMULARY_SHORTED_PUT 	= []

		self.SERVERS_ANALYSE		= OsServer(url)
		self.SERVERS_ANALYSE.run()


	def Links(self):
		found1 = URLLISTER()
		found2 = URLLISTER()

		r = Requester(self.url)

		loading(color.white + "[" + color.green + "  *" + color.white + "  ] traitement du resultat GET ", ".", 3, 0.3)
		found1.feed(r[0])
		sleep(0.3)
		loading(color.white + "[" + color.green + "  *" + color.white + "  ] traitement du resultat PUT ", ".", 3, 0.3)
		found2.feed(r[1])

		self.LinksGet.extend(found1.urls)
		self.LinksPut.extend(found2.urls)

	def Formulairys(self):
		formulaires = self.soup1.find_all("form")
		self.FormulairesGet.extend(formulaires)

		formulaire = self.soup2.find_all("form")
		self.FormulairesPut.extend(formulaires)

		FormPayloadGet = []
		for FormulaireGet in self.FormulairesGet :
			FormParsGet = FormulaireParser.main(FormulaireGet.encode())
			FormPayloadGet.append(FormParsGet[0])
			self.FORMULARY_SHORTED_GET.append(FormParsGet[1])

		FormPayloadPut = []
		for FormulairePut in self.FormulairesPut :
			FormParsPut = FormulaireParser.main(FormulairePut.encode())
			FormPayloadPut.append(FormParsPut[0])
			self.FORMULARY_SHORTED_PUT.append(FormParsGet[1])

		self.PayloadFormGet.extend(FormPayloadGet)
		self.PayloadFormPut.extend(FormPayloadPut)


