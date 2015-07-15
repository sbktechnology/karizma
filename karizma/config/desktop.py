# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"Karizma": {
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Karizma")
		},
                "Catalogue Management": {
			"color": "#3498db",
			"icon": "octicon octicon-repo",
			"type": "module"
		}
	}
