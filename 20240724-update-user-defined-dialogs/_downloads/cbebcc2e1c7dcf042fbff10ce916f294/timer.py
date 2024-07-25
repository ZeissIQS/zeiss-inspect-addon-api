# -*- coding: utf-8 -*-

import gom

DIALOG=gom.script.sys.create_user_defined_dialog (dialog={
	"content": [
		[
			{
				"columns": 2,
				"name": "separator",
				"rows": 1,
				"title": {
					"id": "",
					"text": "Control",
					"translatable": True
				},
				"tooltip": {
					"id": "",
					"text": "",
					"translatable": True
				},
				"type": "separator"
			},
			{
			}
		],
		[
			{
				"button_type": "push",
				"columns": 2,
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
				"name": "start",
				"rows": 1,
				"text": {
					"id": "",
					"text": "Start",
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
			}
		],
		[
			{
				"button_type": "push",
				"columns": 2,
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
				"name": "stop",
				"rows": 1,
				"text": {
					"id": "",
					"text": "Stop",
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
			}
		],
		[
			{
				"columns": 2,
				"name": "separator_2",
				"rows": 1,
				"title": {
					"id": "",
					"text": "Parameters",
					"translatable": True
				},
				"tooltip": {
					"id": "",
					"text": "",
					"translatable": True
				},
				"type": "separator"
			},
			{
			}
		],
		[
			{
				"columns": 1,
				"name": "label_3",
				"rows": 1,
				"text": {
					"id": "",
					"text": "Interval",
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
				"maximum": 1000,
				"minimum": 0,
				"name": "interval",
				"rows": 1,
				"tooltip": {
					"id": "",
					"text": "",
					"translatable": True
				},
				"type": "input::integer",
				"value": 0
			}
		],
		[
			{
				"columns": 2,
				"name": "separator_1",
				"rows": 1,
				"title": {
					"id": "",
					"text": "State",
					"translatable": True
				},
				"tooltip": {
					"id": "",
					"text": "",
					"translatable": True
				},
				"type": "separator"
			},
			{
			}
		],
		[
			{
				"columns": 2,
				"data": "AAAAAA==",
				"file_name": "",
				"height": 0,
				"keep_aspect": True,
				"keep_original_size": True,
				"name": "image",
				"rows": 1,
				"system_image": "system_message_warning",
				"tooltip": {
					"id": "",
					"text": "",
					"translatable": True
				},
				"type": "image",
				"use_system_image": True,
				"width": 0
			},
			{
			}
		],
		[
			{
				"button_type": "push",
				"columns": 2,
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
				"name": "exit",
				"rows": 1,
				"text": {
					"id": "",
					"text": "Exit",
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
			}
		]
	],
	"control": {
		"id": "Empty"
	},
	"embedding": "always_toplevel",
	"position": "automatic",
	"size": {
		"height": 331,
		"width": 134
	},
	"sizemode": "automatic",
	"style": "",
	"title": {
		"id": "",
		"text": "Test Timer",
		"translatable": True
	}
})


#
# Event handler function called if anything happens inside of the dialog
#
state = False
def dialog_event_handler (widget):
	global state
	
	if widget == DIALOG.start:
		DIALOG.timer.interval = DIALOG.interval.value * 1000
		DIALOG.timer.enabled = True
		DIALOG.start.enabled = False
		DIALOG.stop.enabled = True
	elif widget == DIALOG.stop:
		DIALOG.timer.enabled = False
		DIALOG.start.enabled = True
		DIALOG.stop.enabled = False
	elif widget == DIALOG.interval:
		DIALOG.timer.interval = DIALOG.interval.value * 1000
	elif widget == DIALOG.exit:
		gom.script.sys.close_user_defined_dialog (dialog=DIALOG)
	elif str(widget) == 'system':
		print("Its a system event.")
	elif str(widget) == 'timer':
		print("Its a timer event. Let´s swap the image.")
		state = not state
	
		if state:
			DIALOG.image.system_image = 'system_message_warning'
		else:
			DIALOG.image.system_image = 'system_message_question'
	
DIALOG.handler = dialog_event_handler
DIALOG.stop.enabled = False

DIALOG.handler = dialog_event_handler

RESULT=gom.script.sys.show_user_defined_dialog (dialog=DIALOG)
