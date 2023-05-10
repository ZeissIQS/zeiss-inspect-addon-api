# User-defined Dialogs

- [Creating dialogs](#creating-dialogs)
- [Dialog widgets](#dialog-widgets)
- [Executing dialogs](#executing-dialogs)
- [Wizards](#wizards)

# Creating dialogs

- [Dialog designer](#dialog-designer)
- [Dialog layout](#dialog-layout)
    - [Editing the grid](#editing-the-grid)
    - [Spacers](#spacers)
- [Widgets](#widgets)
    - [Inserting and removing widgets](#inserting-and-removing-widgets)
    - [Configuring widgets](#configuring-widgets)
- [Editing already created dialogs](#editing-already-created-dialogs)

## Dialog designer

* User defined dialogs can be inserted into the script using "Insert / Dialog..." from the right mouse menu.

![](assets/insert_dialog.png)

* When a new dialog is inserted, a dialog template and type can be selected.

![](assets/dialog_template.png)

* Dialogs are designed using a GUI based dialog editor.

![](assets/dialog_editor.png)

## Dialog layout

* The dialog designer is using a grid based layout.
* Elements can be inserted into the grid via drag and drop.

### Editing the grid

💡 Editing the layout means changing the underlying grid.

* Because the underlying layout is a grid, the following actions are possible:
    * Adding and removing rows and columns.
    * Merging and splitting rows and columns.

| Tool button                              | Function                          |
| ---------------------------------------- | --------------------------------- |
| ![](assets/split_cells_vertically.png)   | Split selected cells vertically   |
| ![](assets/split_cells_horizontally.png) | Split selected cells horizontally |
| ![](assets/merge_cells.png)              | Merge selected cells              |

* Selected cells are marked with a red overlay.

![](assets/selected_cell.png)

### Spacers

💡 **Spacers** are empty spaces extending in either horizontal or vertical direction.

* If a spacer is inserted into a cell, the cell claims the maximum available space in spacer direction.
* All remaining cells share the remaining space.

![](assets/spacer.png)

## Widgets

### Inserting and removing widgets

* The list of available widgets resides at the left of the dialog designer.
* Widgets are inserted via drag and drop.
* Newly dropped widgets overwrite widgets at the drop target cells.
* A unique name object name is assigned during insertion of a widget. This name is used to access the widget in the Python script.

💡 Removing widgets from the grid is not possible. Instead, they can be overwritten by other widgets.

* Because each cell has to be filled with a widget, widgets can not be removed from the grid. To get rid of a widget
    * Another widget can be dragged and dropped onto the existing widget or
    * The widget cell can be merged with another cell.

![](assets/separator_line.png)

### Configuring widgets

* The properties of selected widgets can be edited in the property editor at the right side of the designer dialog.
* Every widget has at least a unique name.
* Additionally, various parameters depending on the widget type can be edited.

![](assets/configuring_widgets.png)

The definition of the dialog can be found in `scriptingEditorExampleDialog.py`

## Editing already created dialogs

* Creating a dialogs leads to a script command with embedded dialog representation as XML code.
* Double clicking onto this command opens the dialog editor again

# Dialog widgets

- [Use of the \_\_doc\_\_ string](#use-of-the-__doc__-string)
- [Control widget](#control-widget)
    - [Control widget elements](#control-widget-elements)
    - [Control button properties](#control-button-properties)
    - [The status label](#the-status-label)
- [Specific widgets](#specific-widgets)
    - [Text fields](#text-fields)
    - [Images](#images)
    - [Log widget](#log-widget)
    - [Progress-bar widget](#progress-bar-widget)
    - [Integer widget](#integer-widget)
    - [Decimal widget](#decimal-widget)
    - [Text entry field](#text-entry-field)
    - [Slider widget](#slider-widget)
    - [Checkbox widget](#checkbox-widget)
    - [File widget](#file-widget)
    - [Date widget](#date-widget)
    - [Color widget](#color-widget)
    - [Selection element widget](#selection-element-widget)
    - [Selection list widget](#selection-list-widget)
    - [Button widget](#button-widget)
    - [Radio button widget](#radio-button-widget)
    - [Abort button widget](#abort-button-widget)

This section gives an overview of the available widgets. If the code examples given in this section are not intuitive to you, you might want to take a look 
into [Executing dialogs](#executing-dialogs).

## Use of the \_\_doc\_\_ string

Information about the widgets can be obtained by accessing their doc string. Let objName be the object name of a widget and DIALOG the dialog handle 
(see [Executing dialogs](#executing-dialogs) if this is unclear to you), the doc string can be obtained as follows:

```
print( DIALOG.objName.__doc__ )
```

## Control widget

💡 The control widget contains the ok/cancel or similar buttons of the dialog.

* The control element of a dialog cannot be configured like other dialog widgets.
* Therefore, their name is fixed and they are grouped together inside of the control widget named 'control'.
* The control elements consist of the dialogs lower buttons plus a configurable dialog status label.

| Handle                    | Property                                  | Example                                     |
| ------------------------- | ----------------------------------------- | ------------------------------------------- |
| DIALOG.control            | Control widget                            | -                                           |
| DIALOG.control.status     | Status icon of the control widget         | `DIALOG.control.status = 'Point 1 missing'` |
| DIALOG.control.\<button\> | Handle for a button of the control widget | `DIALOG.control.ok.enabled = False`         |

### Control widget elements

💡 The names of the control widget elements are fixed

* Usually, the names are corresponding with the elements' semantics. For example, the name of the 'ok' button is 'ok'. The names can also be 
obtained from the \_\_doc\_\_ string as shown in the code example below.
* The control elements are accessed like all other widget attributes.

> Accessing the control widget

```
# Print control widget properties
> print (DIALOG.control.__doc__)
ControlGroup
Attributes:
status (string) - Status tool tip icon
ok (unspecified/various) - Control widget
cancel (unspecified/various) - Control widge
```

### Control button properties

Control buttons only have the following two properties which can be set programmatically:

| Property | Type | Example                                 |
| -------- | ---- | --------------------------------------- |
| text     | str  | `DIALOG.control.prev.text = 'Previous'` |
| enabled  | bool | `DIALOG.control.ok.enabled = False`     |

### The status label

⚠️ The status label of the control widget is invisible until a status text is set.

* If a status text is set, a small warning icon appears, like in regular applications' dialogs.
* The status label can be configured using its properties like all other widgets.

| Dialog | Code |
| ------ | ---- |
| (figure)       | <pre>DIALOG=gom.script.sys.create_user_defined_dialog (content='dialog definition')<br># Set status label text<br>DIALOG.control.status = 'No point selected.'<br># Set 'ok' button to insensitive<br>DIALOG.control.ok.enabled = False<br>gom.script.sys.show_user_defined_dialog(dialog = DIALOG)</pre> |

You can reset the status icon and clear the error message by assigning an empty string (`DIALOG.control.status = ''`).

## Specific widgets

### Text fields

* Text field widgets are able to display multi lines text.
* In these texts keywords can also be displayed.
* A double click onto a text field widget opens a content editor.

| Dialog    | Code |
| --------- | ---- |
| (figure)  | <pre># The 'data' attribute contains the image data (shortened version here)<br>RESULT=gom.script.sys.execute_user_defined_dialog<br>(content='\<dialog\>' \\<br>' \<title\>About\</title\>' \\<br>' \<control id="Close" /\>' \\<br>' \<content rows="1" columns="1" \>' \\<br>' \<widget rowspan="1" row="0" column="0" columnspan="1" type="image" \>' \\<br>' \<name\>image\</name\>' \\<br>' \<data\>\<!\[CDATA\[eAEdWgVUFd0WHkK4IEiHSHengdKIooCA...\</data\>' \\<br>' \<file_name\>/home/develop/fcieslok/gom.jpg\</file_name\>' \\<br>' \</widget\>' \\<br>' \</content\>' \\<br>'\</dialog\>')</pre> |

| Editor    | Dialog   |
| --------- | -------- |
| (figure)  | (figure) |

* The keywords displayed in text field widgets can originate from different source:
    * Global application keywords,
    * project related keywords and
    * local script variables.

⚠️ Local script variables can be displayed in text fields by inserting them via the 'insert expression' dialog.

* Local script variables are invalid until the variable assignment is reached. They cannot be displayed statically in the text field editor prior to script 
execution, so an invalid value (???) will most certainly be displayed instead.

| Property | Type | Example                             |
| -------- | ---- | ----------------------------------- |
| enabled  | bool | `DIALOG.textWidget.enabled = False` |
| text     | str  | `print(DIALOG.textWidget.text)`     |
| wordwrap | bool | `DIALOG.textWidget.wordwrap = True` |
| visible  | bool | `DIALOG.label_name.visible = False` |

### Images

* Widgets of type image are able to display arbitrary images.
* The image data is stored together with the dialog data in the generated XML code. The \<data\>\</data\> section contains the string representing the image.

| Dialog    | Code |
| --------- | ---- |
| (figure)  | <pre># The 'data' attribute contains the image data (shortened version here)<br>RESULT=gom.script.sys.execute_user_defined_dialog <br>(content='\<dialog\>' \\<br>' \<title\>About\</title\>' \\<br>' \<control id="Close" /\>' \\<br>' \<content rows="1" columns="1" \>' \\<br>' \<widget rowspan="1" row="0" column="0" columnspan="1" type="image" \>' \\<br>' \<name\>image\</name\>' \\<br>' \<data\>\<!\[CDATA\[eAEdWgVUFd0WHkK4IEiHSHengdKIooCA...\</data\>' \\<br>' \<file_name\>/home/develop/fcieslok/gom.jpg\</file_name\>' \\<br>' \</widget\>' \\<br>' \</content\>' \\<br>'\</dialog\>')</pre> |

| Property           | Type      | Example                                              |
| ------------------ | --------- | ---------------------------------------------------- |
| enabled            | bool      | `DIALOG.image.enabled = False`                       |
| text               | str       | `DIALOG.control.prev.text = 'Previous'` ???          |
| use_system_image   | bool      | `DIALOG.image.use_system_image = True`               |
| system_image       | str       | <pre># Possible values: 'system_message_information', 'system_message_warning',<br> 'system_message_critical', 'system_message_question'<br>DIALOG.image.system_image = 'system_message_question'</pre> |
| file_name          | str       | read-only!                                           |
| keep_original_size | bool      | read-only!                                           |
| keep_aspect        | bool      | read-only!                                           |
| data               | (special) | <pre># This is the actual image data<br># Copy image from one dialog to another:<br>my_dialog.my_image.data = image_container_dialog.image_1.data</pre> |
| width              | int       | `print('image width ' + str(DIALOG.image.width))`    |
| height             | int       | `print('image height ' + str(DIALOG.image.height)) ` |
| visible            | bool      | `DIALOG.image_fixture.visible = False`               |

Note that you can switch from a system image to a user image using the property `use_system_image`. But this user image must have been selected 
beforehand in the designer. You cannot read a new image file by setting the `filename` property. Also, all of the image formatting properties (`keep_original_size`, `keep_aspect`, `width`, `height`) only work in the designer. From the script you can only read these values.
Although you cannot read images using the `filename` property you can copy images from one dialog to another using the `data` property. So you are able 
to prepare (create) a dialog as an image container holding several images. You can then use this image container dialog to copy the image you need to an 
actually displayed dialog.

### Log widget

| Dialog    | Description |
| --------- | ----------- |
| (figure)  | The log widget can display multiple lines of unformatted text, which can be easily saved to a text file by clicking the save button. |

| Property             | Type      | Example                                              |
| -------------------- | --------- | ---------------------------------------------------- |
| enabled              | bool      | `DIALOG.log.enabled = True`                          |
| text                 | str       | `DIALOG.log.text += 'Yet another log message.\n`     |
| word_wrap            | bool      | `DIALOG.log.word_wrap = True`                        |
| show_save            | bool      | `DIALOG.log.show_save = False`                       |
| save_dialog_title    | str       | `DIALOG.log.save_dialog_title = 'Save operator log'` |
| scroll_automatically | bool      | `DIALOG.log.scroll_automatically = True`             |
| visible              | bool      | `DIALOG.log.visible = False`                         |

### Progress-bar widget

| Dialog    | Description |
| --------- | ----------- |
| (figure)  | The progress bar widget can be used in the two modes _system_ and _manual_.<br><br>**Manual mode:**<br>In this mode, the user may set the progress bar through its `value` variable.<br><pre>import gom, time<br>DIALOG=gom.script.sys.create_user_defined_dialog (content='dialog defintion')<br>DIALOG.progress.minimum = 0<br>DIALOG.progress.maximum = 100<br>gom.script.sys.open_user_defined_dialog( dialog = DIALOG )<br>DIALOG.progress.value = 0<br>time.sleep(1)<br>DIALOG.progress.value = 33<br>time.sleep(1)<br>DIALOG.progress.value = 66<br>time.sleep(1)<br>DIALOG.progress.value = 100<br>gom.script.sys.close_user_defined_dialog (dialog=DIALOG)</pre><br><br>**Automatic mode:**<br>In this mode, the progress bar displays the same progress informations as the progress bar in the lower right corner of the software.<br><pre>import gom<br>DIALOG=gom.script.sys.create_user_defined_dialog (content='dialog definition')<br>gom.script.sys.open_user_defined_dialog (dialog=DIALOG)<br>gom.script.sys.create_project ()<br>gom.script.atos.import_project (file='some project')<br>gom.script.sys.close_user_defined_dialog (dialog=DIALOG)</pre><br><br>You can switch between automatic and manual mode from with the script by setting the mode variable as shown below:<br><pre># manual mode:<br>DIALOG.progress.mode = "manual"<br># automatic mode:<br>DIALOG.progress.mode = "system"</pre><br><br>**Partially controlled system progress bar:**<br>The range of a system progress bar can be divided into parts, sequentially controlled by an executed command.<br><ul><li>The progress bar range can be split into multiple parts.<li>Each part controls an equally sized progress bar interval. If, for example, there are 3 parts, the first part ranges from 0 to 33, the second from 33 to 66 and the third from 66 to 100.<li>When a command is executed, the command controlles just the one active part of the progress bar widget.</ul><br>**Example:**<pre># -*- coding: utf-8 -*-<br>import gom<br># Create a user defined dialog with a progress bar, mode 'system'<br>DIALOG=gom.script.sys.create_user_defined_dialog (content='dialog definition')<br>gom.script.sys.open_user_defined_dialog( dialog = DIALOG )<br># Split progress bar into 3 parts<br>DIALOG.progress.parts = 3<br># Current part is the first interval (part '0', because we are counting from '0')<br>DIALOG.progress.step = 0<br># Execute load command. The command will control the first progress bar range from 0% to 33%.<br># That means when the command has been finished, the progress bar will display '33%'.<br>gom.script.sys.load_project (file='some project')<br># Current part is the second interval. The progress bar runs from 33% to 66%<br>DIALOG.progress.step = 1<br>gom.script.atos.switch_to_report_mode ()<br>gom.script.report.update_report_page (<br> pages=gom.app.project.reports,<br> switch_alignment=True,<br> switch_stage=False)<br># Current part is the third interval. The progress bar runs from 66% to 100%<br>DIALOG.progress.step = 2<br>gom.script.atos.switch_to_inspection_mode ()<br>gom.script.sys.recalculate_all_elements ()</pre><br>💡 It is possible to switch  between automatic and manual mode for each part. |


### Integer widget

| Dialog    | Description |
| --------- | ----------- |
| (figure)  | The integer widget is used to require integers from the user. `integerWidget` is the object name of the integer widget in the example below.<pre>RESULT=gom.script.sys.execute_user_defined_dialog (content='dialog definition')<br>userInput = RESULT.integerWidget</pre> |

| Property | Type  | Example                                                                |
| -------- | ----- | ---------------------------------------------------------------------- |
| tooltip  | str   | <pre>DIALOG.inputInt.tooltip = 'Enter the number of points!'</pre>     |
| enabled  | bool  | <pre>DIALOG.inputInt.enabled = False</pre>                             |
| value    | int   | <pre>if DIALOG.inputInt.value < 15:</pre>                              |
| focus    | bool  | <pre>DIALOG.inputInt.focus = True</pre>⚠️ Only works if dialog is open |
| minimum  | float | <pre>DIALOG.inputInt.minimum = 20</pre>                                |
| maximum  | float | <pre>DIALOG.inputInt.maximum = 50</pre>                                |
| visible  | bool  | <pre>DIALOG.inputInt.visible = False</pre>                             |

### Decimal widget

| Dialog    | Description |
| --------- | ----------- |
| (figure)  | The decimal widget is used to get a floating point input from the user. It is possible to choose the number of digits and a unit. The selectable units are the ones from the user preferences (Edit \> Application \> Settings \> Preferences) in the _Default units_ tab. `decimalWidget` is the object name of the decimal widget in the example below.<pre>RESULT=gom.script.sys.execute_user_defined_dialog (content='dialog definition')<br>userInput = RESULT.decimalWidget</pre> |

| Property | Type  | Example                                                                  |
| -------- | ----- | ------------------------------------------------------------------------ |
| tooltip  | str   | <pre>DIALOG.floatInput.tooltip = 'Enter the number of points!'</pre>     |
| enabled  | bool  | <pre>DIALOG.floatInput.enabled = False</pre>                             |
| value    | int   | <pre>if DIALOG.floatInput.value < 15:</pre>                              |
| focus    | bool  | <pre>DIALOG.floatInput.focus = True</pre>⚠️ Only works if dialog is open |
| minimum  | float | <pre>DIALOG.floatInput.minimum = 20</pre>                                |
| maximum  | float | <pre>DIALOG.floatInput.maximum = 50</pre>                                |
| visible  | bool  | <pre>DIALOG.floatInput.visible = False</pre>                             |

### Text entry field

| Dialog    | Description |
| --------- | ----------- |
| (figure)  | The text entry field can be used to get string input from the user. A simple use case is given by the next code block. _textEntryWidget_ is the object name of the widget in the example below.<pre>DIALOG=gom.script.sys.create_user_defined_dialog (content='dialog definition')<br>DIALOG.textEntryWidget = "some default text"<br>RESULT = gom.script.sys.show_user_defined_dialog(dialog = DIALOG)<br>print( RESULT.textEntryWidget ) # the user input string</pre> |

| Property  | Type  | Example                                                                    |
| --------- | ----- | -------------------------------------------------------------------------- |
| tooltip   | str   | <pre>DIALOG.inputString.tooltip = 'Enter object description'</pre>         |
| enabled   | bool  | <pre>DIALOG.inputString.enabled = True</pre>                               |
| value     | str   | <pre>DIALOG.inputString.value = "Warsaw"</pre>                             |
| focus     | bool  | <pre>DIALOG.inputString.focus = True</pre> ⚠️ Only works if dialog is open |
| read_only | bool  | <pre>if DIALOG.inputString.read_only:</pre>                                |
| visible   | bool  | <pre>DIALOG.input_name.visible = False</pre> ???                           |

### Slider widget

| Dialog    | Description |
| --------- | ----------- |
| (figure)  | The slider widget can be used to get a float value from a certain interval from the user. _sliderWidget_ is the object name of the slider widget in the example below.<pre>DIALOG=gom.script.sys.create_user_defined_dialog (content='dialog definition')<br><br>RESULT = gom.script.sys.show_user_defined_dialog (dialog=DIALOG)<br>print( RESULT.sliderWidget ) # some float</pre> |

### Checkbox widget

The check box widget can be used to get boolean input from the user.

| Property  | Type  | Example                                                                                              |
| --------- | ----- | ---------------------------------------------------------------------------------------------------- |
| tooltip   | str   | <pre>DIALOG.inputCheckbox.tooltip = 'Check this option to clear the results after evaluation.'</pre> |
| enabled   | bool  | <pre>DIALOG.inputCheckbox.enabled = True</pre>                                                       |
| value     | bool  | <pre>print('Evaluation enabled:', str(DIALOG.inputCheckbox.value))</pre>                             |
| title     | str   | <pre>DIALOG.inputCheckbox.title = 'Mirror option'</pre>                                              |
| visible   | bool  | <pre>DIALOG.input_transparency.visible = False</pre> ???                                             |

### File widget

### Date widget

### Color widget

### Selection element widget

### Selection list widget

### Button widget

### Radio button widget

### Abort button widget

# Executing dialogs

- [Dialog commands](#dialog-commands)
    - [Blocking fixed dialogs (`execute`)](#blocking-fixed-dialogs-execute)
    - [Blocking configurable dialogs (`create` and `show`)](#blocking-configurable-dialogs-create-and-show)
    - [Non-blocking configurable dialogs (`create`, `open` and `close`)](#non-blocking-configurable-dialogs-create-open-and-close)
- [Dialog results](#dialog-results)
    - [Custom results](#custom-results)
- [Configuring dialog widgets](#configuring-dialog-widgets)
- [Event handler functions](#event-handler-functions)
    - [Registering event handlers](#registering-event-handlers)
    - [Closing dialogs from within the event handler](#closing-dialogs-from-within-the-event-handler)
    - [Using a timer to activate the event handler](#using-a-timer-to-activate-the-event-handler)
- [Determining the existing widget attributes](#determining-the-existing-widget-attributes)

## Dialog commands

### Blocking fixed dialogs (`execute`)

### Blocking configurable dialogs (`create` and `show`)

### Non-blocking configurable dialogs (`create`, `open` and `close`)

## Dialog results

### Custom results

## Configuring dialog widgets

## Event handler functions

### Registering event handlers

### Closing dialogs from within the event handler

### Using a timer to activate the event handler

## Determining the existing widget attributes

# Wizards

- [Control widgets](#control-widgets)

## Control widgets





