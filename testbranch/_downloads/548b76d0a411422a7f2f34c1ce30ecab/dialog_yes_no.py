# -*- coding: utf-8 -*-

import gom

DIALOG=gom.script.sys.create_user_defined_dialog (dialog={
				"content": [
								[
												{
																"columns": 2,
																"name": "label",
																"rows": 1,
																"text": {
																				"id": "",
																				"text": "Choose a button. Any button.",
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
												}
								],
								[
												{
																"button_type": "push",
																"columns": 1,
																"icon": "AAAAAA==",
																"icon_file_name": "",
																"icon_size": {
																				"value": "icon"
																},
																"icon_system_size": {
																				"value": "default"
																},
																"icon_system_type": {
																				"value": "ok"
																},
																"icon_type": {
																				"value": "none"
																},
																"name": "button_yes",
																"rows": 1,
																"text": {
																				"id": "",
																				"text": "Yes",
																				"translatable": True
																},
																"tooltip": {
																				"id": "",
																				"text": "",
																				"translatable": True
																},
																"type": "button::pushbutton"
												},
												{
																"button_type": "push",
																"columns": 1,
																"icon": "AAAAAA==",
																"icon_file_name": "",
																"icon_size": {
																				"value": "icon"
																},
																"icon_system_size": {
																				"value": "default"
																},
																"icon_system_type": {
																				"value": "ok"
																},
																"icon_type": {
																				"value": "none"
																},
																"name": "button_no",
																"rows": 1,
																"text": {
																				"id": "",
																				"text": "No",
																				"translatable": True
																},
																"tooltip": {
																				"id": "",
																				"text": "",
																				"translatable": True
																},
																"type": "button::pushbutton"
												}
								]
				],
				"control": {
								"id": "Empty"
				},
				"embedding": "",
				"position": "",
				"size": {
								"height": 121,
								"width": 230
				},
				"sizemode": "",
				"style": "",
				"title": {
								"id": "",
								"text": "Push a button",
								"translatable": True
				}
})

#
# Event handler function called if anything happens inside of the dialog
#
def dialog_event_handler (widget):
	if widget == DIALOG.button_yes:
		gom.script.sys.close_user_defined_dialog( dialog = DIALOG, result = 'Yes' )
	if widget == DIALOG.button_no:
		gom.script.sys.close_user_defined_dialog( dialog = DIALOG, result = 'No' )

DIALOG.handler = dialog_event_handler

try:
	RESULT=gom.script.sys.show_user_defined_dialog (dialog=DIALOG)
except gom.BreakError as e:
	RESULT = 'Cheater'

print('RESULT', RESULT)
