# -*- coding: utf-8 -*-
import sublime, sublime_plugin

class RemoveAccents(sublime_plugin.TextCommand):
	def run(self, edit):
 		for region in self.view.sel():
			if region.empty():
				sublime.message_dialog(u'Vyber niečo')
			else:
				myString = unicode(self.view.substr(region))
				myString = self.strip_accents(myString)
				self.view.replace(edit, region, myString)

	def strip_accents(self, s):
		import unicodedata
		return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))