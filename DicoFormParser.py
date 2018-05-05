import string
import re
import sys, os

class DicoFormParser :
	def __init__(self, origin):
		self.ORIGIN		= origin
		self.SOURCE		= 'no source'
		self.METHODE		= 'no methode'
		self.FORMULAIRE		= {}
		self.JUST_NAME 		= {}
		self.NAME_VALUE		= {}
		self.NAME_ID		= {}
		self.ID_VALUE		= {}

		for key, value in origin.items():
			self.SOURCE = key
			for key2, value2 in value.items() :
				self.METHODE = key2
				for VAL in value2 :
					for key3, value3 in VAL.items():
						self.FORMULAIRE[key3] = value3

		for key, value in self.FORMULAIRE.items() :
			self.JUST_NAME[key] = ''

		for key, value in self.FORMULAIRE.items() :
			name = key
#			print value
			for key, val in value.items() :
				self.NAME_VALUE[name] = val

		for key, value in self.FORMULAIRE.items() :
			name = key
			for key, val in value.items():
				self.NAME_ID[name] = key

		for key, value in self.FORMULAIRE.items() :
			for id, val in value.items() :
				self.ID_VALUE[id] = val


def main(test):		# FONCTION DE TEST
	NewForm = Formulaire(test)
	print "VARIABLE : \t\t", NewForm.SOURCE
	print "METHODE : \t\t", NewForm.METHODE
	print "JUST NAME : \t\t", NewForm.JUST_NAME
	print "NAME_VALUE : \t\t", NewForm.NAME_VALUE
	print "NAME_ID : \t\t", NewForm.ID_VALUE

#main(DICO)
