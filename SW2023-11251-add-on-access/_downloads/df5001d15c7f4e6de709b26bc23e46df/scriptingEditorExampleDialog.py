# -*- coding: utf-8 -*-

import gom


DIALOG=gom.script.sys.create_user_defined_dialog (dialog={
                "content": [
                                [
                                                {
                                                                "columns": 1,
                                                                "data": "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",
                                                                "file_name": "Y:/gomServiceArea/DokumentationDerDialoge/widgetDescription/LineForDialogImage.png",
                                                                "height": 140,
                                                                "keep_aspect": True,
                                                                "keep_original_size": True,
                                                                "name": "image",
                                                                "rows": 6,
                                                                "system_image": "system_message_warning",
                                                                "tooltip": {
                                                                                "id": "",
                                                                                "text": "",
                                                                                "translatable": True
                                                                },
                                                                "type": "image",
                                                                "use_system_image": False,
                                                                "width": 140
                                                },
                                                {
                                                                "columns": 2,
                                                                "name": "parametersSeparator",
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
                                                },
                                                {
                                                                "columns": 1,
                                                                "name": "nameLabel",
                                                                "rows": 1,
                                                                "text": {
                                                                                "id": "",
                                                                                "text": "Name:",
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
                                                                "name": "name",
                                                                "password": False,
                                                                "read_only": False,
                                                                "rows": 1,
                                                                "tooltip": {
                                                                                "id": "",
                                                                                "text": "",
                                                                                "translatable": True
                                                                },
                                                                "type": "input::string",
                                                                "value": ""
                                                }
                                ],
                                [
                                                {
                                                },
                                                {
                                                                "columns": 2,
                                                                "name": "pointsSeparator",
                                                                "rows": 1,
                                                                "title": {
                                                                                "id": "",
                                                                                "text": "Points",
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
                                                },
                                                {
                                                                "columns": 1,
                                                                "name": "point1Label",
                                                                "rows": 1,
                                                                "text": {
                                                                                "id": "",
                                                                                "text": "Point 1",
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
                                                                "name": "point1",
                                                                "rows": 1,
                                                                "supplier": "any",
                                                                "tooltip": {
                                                                                "id": "",
                                                                                "text": "",
                                                                                "translatable": True
                                                                },
                                                                "type": "input::point3d"
                                                }
                                ],
                                [
                                                {
                                                },
                                                {
                                                                "columns": 1,
                                                                "name": "point2Label",
                                                                "rows": 1,
                                                                "text": {
                                                                                "id": "",
                                                                                "text": "Point 2",
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
                                                                "name": "point2",
                                                                "rows": 1,
                                                                "supplier": "any",
                                                                "tooltip": {
                                                                                "id": "",
                                                                                "text": "",
                                                                                "translatable": True
                                                                },
                                                                "type": "input::point3d"
                                                }
                                ],
                                [
                                                {
                                                },
                                                {
                                                                "columns": 2,
                                                                "maximum_size": -1,
                                                                "minimum_size": 0,
                                                                "name": "spacer",
                                                                "rows": 1,
                                                                "tooltip": {
                                                                                "id": "",
                                                                                "text": "",
                                                                                "translatable": True
                                                                },
                                                                "type": "spacer::vertical"
                                                },
                                                {
                                                }
                                ]
                ],
                "control": {
                                "id": "OkCancel"
                },
                "embedding": "always_toplevel",
                "position": "automatic",
                "size": {
                                "height": 291,
                                "width": 434
                },
                "sizemode": "automatic",
                "style": "Standard",
                "title": {
                                "id": "",
                                "text": "Line from two points",
                                "translatable": True
                }
})

# Handler function registered to the dialog
def handler_function (widget): 
    # Print information about the modified widget
    print ("Modified:", str (widget))
    # If the 'name' widget is empty, the 'ok' button is disabled.
    if DIALOG.name.value == "":
        DIALOG.control.ok.enabled = False
    else :
        DIALOG.control.ok.enabled = True
        
    if str(widget) == 'system':
        print("It is a global event.")
    elif str(widget) == 'initialize':
        print("Dialog is displayed for the first time.")
    
# Register dialog handler
DIALOG.handler = handler_function
# Execute dialog
RESULT=gom.script.sys.show_user_defined_dialog (dialog=DIALOG)

# Print content of the 'name' widget
print( RESULT.name )
# output: Line 1
    
# Print content of the widget named 'point1'. This can again be an element reference.
print( RESULT.point1 ) 
# output: gom.app.project.actual_elements['Point 5']
    
# Print content of the widget named 'point2'.
print( RESULT.point2 )
# output: gom.app.project.actual_elements['Point 6']

# construct a line with the user input. Therefore our dialog works similar to the 2-point Line
# construction dialog
MCAD_ELEMENT=gom.script.primitive.create_line_by_2_points (
    name= RESULT.name, 
    point1 = RESULT.point1, 
    point2 = RESULT.point2
)
