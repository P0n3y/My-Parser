#-*- coding: utf-8 -*-

import sys, os
import bs4 as BeautifulSoup
import re

from display.colors import *
from DicoFormParser import *

color = Color()

def Define(Tab):
#	print "####", Tab
	Values = []
	for val in Tab :
		if val is not None :
			Values.append(val)
		else :
			pass
	return "".join(Values)

class FormulaireParser :
	def __init__(self, formulaire):
		print color.white + "[" + color.green + "  *" + color.white + "  ] find values in formulairy"

		self.FormulairesPayload = []

#		print color.red + formulaire

		self.methode = []
		self.actions = []
		self.SomeInputs = []

		pars = BeautifulSoup.BeautifulSoup(formulaire)

		for FormBalise in pars.find_all("form"):
			try :
				allMethode = []
				method = FormBalise.get("methode")
				methode = FormBalise.get("method")
				METHOD = FormBalise.get("METHOD")
				METHODE = FormBalise.get("METHODE")
				Method = FormBalise.get("Method")
				Methode = FormBalise.get("Methode")
				allMethode = [method, methode, METHOD, METHODE, Method, Methode]
				self.methode.extend(Define(allMethode))

				action = FormBalise.get("action")
				Action = FormBalise.get("Action")
				ACTION = FormBalise.get("ACTION")
				actions = [action, Action, ACTION]
				self.actions = Define(actions)
			except Exception as err :
				print "[-] ERROR 1 DETECTED : " + str(err)

		for Input in pars.find_all("input") :
			try :
				AllN = []
				AllI = []
				AllV = []

				name = Input.get("name")
				Name = Input.get("Name")
				NAME = Input.get("NAME")
				AllN.extend([name, Name, NAME])

				id = Input.get("id")
				Id = Input.get("Id")
				ID = Input.get("ID")
				AllI.extend([id, Id, ID])

				value = Input.get("value")
				Value = Input.get("Value")
				VALUE = Input.get("VALUE")
				AllV.extend([value, Value, VALUE])

				TheName = Define(AllN)
				TheId = Define(AllI)
				TheValue = Define(AllV)

				Parm = {TheName:{TheId:TheValue}}
				self.SomeInputs.append(Parm)

			except Exception as err :
				print "[-] ERROR 2 DETECTED : " + str(err)


		for Select in pars.find_all("select") :
			options = []
			try :
				name = Select.get("name")
				for option in Select.find_all("option"):
					try :
						value = option.get("value")
						options.append(value)
					except Exception as err :
						print "[-] ERROR 4 DETECTED : " + str(err)
			except Exception as err :
				print "[-] ERROR 3 DETECTED : " + str(err)

			Parm = {name:{"":options}}
			self.SomeInputs.append(Parm)

		parm = {Define(self.actions):{Define(self.methode):self.SomeInputs}}
		self.FormulairesPayload.append(parm)

def main(form):
	Form 		= FormulaireParser(form)	# Cherche le formulaire
#	print ">>>>>>>>>", Form.FormulairesPayload[0]
	NewForm		= DicoFormParser(Form.FormulairesPayload[0])

	return Form.FormulairesPayload, NewForm
