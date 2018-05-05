import re
import string
import sys, os

from display.colors import *

class Link :
	def __init__(self, site, link):
		self.site = site
		self.link = link

		self.URLpattern		= "^(https|http)://(.*)/"
		self.URLregex		= re.compile(URLpattern)
		self.InternLinkPattern	= "^(../|/|[a-zA-Z0-9]{1, 200}).(.*)"
		self.InternLinkRegex	= re.compile(InternLinkPattern)

		self.ParamPattern	= "[?&](?P<param>\w+)=(?P<value>\w+)"

	def ScanningOrigine(self):
		if self.URLregex.match(self.site) is not None :
			site = re.findall(HTTPpattern, self.site)

			if self.InternLinkRegex.match(self.target) is not None :
				return True, self.link
			elif self.URLregex.match(self.target) is not None :
				Target_Scan = re.findall(self.URLpattern, self.target
				if Target_Scan == site :
					return True, self.link
				else :
					return False, self.Link
			else :
				return False, self.Link

	def ScanningGetParamLink(self, link):
		GetSetting	= []
		REGEX 		= re.search(self.ParamPattern, link)

		if REGEX is not None :
			GetParam = { REGEX.group('param'):REGEX.group('value') }
			GetSetting.append(GetParam)
		else :
			GetSetting = False

		return GetSetting
