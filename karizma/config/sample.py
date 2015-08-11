from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer database."),
				},
				{
					"type": "doctype",
					"name": "Sample Requisition",
					"description": _("Samples Requisition from Leads or Customers."),
				},
                   		{
					"type": "doctype",
					"name": "Sample Issue",
					"description": _("Samples Issue to Leads or Customers."),
				},
				
			]
		},
		{
			"label": _("Masters"),
			"items": [
				{
					"type": "doctype",
					"name": "Sample",
					"description": _("Sample Item"),
				},
				{
					"type": "doctype",
					"name": "Color",
					"description": _("Color of Sample"),
				},
				{
					"type": "doctype",
					"name": "Article Number",
					"description": _("Article Number of sample."),
				},
				{
					"type": "doctype",
					"name": "Brand",
					"description": _("Brand of sample"),
				}
			]
		},
	]
