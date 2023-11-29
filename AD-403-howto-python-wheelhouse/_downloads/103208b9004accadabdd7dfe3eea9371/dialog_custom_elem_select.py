# -*- coding: utf-8 -*-

import gom

DIALOG4=gom.script.sys.create_user_defined_dialog (dialog={
	"content": [
		[
			{
				"columns": 1,
				"name": "label_6",
				"rows": 1,
				"text": {
					"id": "",
					"text": "New",
					"translatable": True
				},
				"tooltip": {
					"id": "",
					"text": "",
					"translatable": True
				},
				"type": "label",
				"word_wrap": False
			},
			{
				"columns": 1,
				"fast_filter": False,
				"name": "input_new",
				"rows": 1,
				"supplier": "custom",
				"tooltip": {
					"id": "",
					"text": "",
					"translatable": True
				},
				"type": "input::point3d"
			}
		]
	],
	"control": {
		"id": "OkCancel"
	},
	"embedding": "",
	"position": "",
	"size": {
		"height": 112,
		"width": 200
	},
	"sizemode": "",
	"style": "",
	"title": {
		"id": "",
		"text": "Demo \"New selection element\"",
		"translatable": True
	}
})

def dialog_event_handler (widget):
	pass

# filter system planes
def element_filter( element ):
	try:
		if element.type == 'plane':
			return True
	except Exception as e:
		pass
	return False

DIALOG4.handler = dialog_event_handler
DIALOG4.input_new.filter = element_filter

RESULT=gom.script.sys.show_user_defined_dialog (dialog=DIALOG4)

print("Chosen system plane:", RESULT.input_new.name)


