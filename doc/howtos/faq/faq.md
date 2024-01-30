# Frequently asked questions

If you did not find an answer here, you might want to check <a href="https://forum.gom.com/forum/8-customizations/" target="_blank" rel="noopener noreferrer">ZEISS Quality Forum - Customizations</a>.

## Where are Add-ons located in the file system?

Add-ons which are edited are located in `C:\Users\<USERID>\AppData\Roaming\GOM\<VERSION>\gom_edited_addons` (or `%APPDATA%\GOM\<VERSION>\gom_edited_addons`, respectively). There is a subfolder for each Add-on named by its UUID.

When editing is finished, an Add-on file (see [Add-on file format](../add_on_file_format/add_on_file_format.md)) is created and saved in `C:\Users\<USERID>\AppData\Roaming\GOM\<VERSION>\gom_addons`.

## How can I stop script execution?

In a user defined dialog, you can call `gom.script.sys.close_user_defined_dialog (dialog=\<your_dialog\>)`.

In general, you can use

```{code-block} python
import sys

# ...

sys.exit(0)

```

## How do I filter nominal, actual or inspection elements?

Use `print (gom.app.project.<element_type>.__doc__)` where you replace `<element_type>` by `actual_elements`, `nominal_elements` or `inspection` as needed to get the available properties.

To show all actual elements by name and type:

```{code-block} python
for element in gom.app.project.actual_elements:
    print (f'{element.name} - type: {element.type}')
```

You can create a loop in Python to iterate over the elements as shown above and apply a comparison to their attributes, but there is a faster solution!

The `filter()` method handles this far more efficiently!

### Examples for filtering actual elements

```{code-block} python
group = gom.app.project.actual_elements

f = group.filter("is_selected", True)
print (f) # array of elements matching the filter criterion 'is_selected == True'

f = group.filter("type", "plane")
print (f) # array of elements matching the filter criterion 'type == Plane'
```

### Examples for filtering nominal elements

```{code-block} python
group = gom.app.project.nominal_elements

f = group.filter("is_visible", True)
print (f) # array of elements matching the filter criterion 'is_visible == True'

f = group.filter("type", "cad")
print (f) # array of elements matching the filter criterion 'type == cad'
```

### Examples for filtering inspection elements

```{code-block} python
group = gom.app.project.inspection

f = group.filter("is_element_modified_since_import", True)
print (f) # array of elements matching the filter criterion 'is_element_modified_since_import == True'

f = group.filter("type", "cad")
print (f) # array of elements matching the filter criterion 'type == surface_comparison'
```

## How do I check if a dialog was closed with 'Ok', 'Yes'/'No' or 'Close', respectively? (And not with 'Cancel' or by closing the dialog window.)

![Dialog types](assets/dialog_types.png)

![Window closed](assets/dialog_close.png)

Closing a dialog window or pressing the 'Cancel' button raises a `gom.BreakError` exception. To check if any type of dialog was closed via the window close control (see figure) or via the 'Cancel' button (in case of the 'Ok/Cancel' dialog type), use the following code:

```{code-block} python
try:
	RESULT = gom.script.sys.show_user_defined_dialog (dialog=DIALOG)
except gom.BreakError as e:
	print("Dialog window was closed or 'Cancel' button was pressed")
else:
	print("'Ok' button was pressed")
```

## How can I retrieve dialog results as a Python dictionary?

```{code-block} python
print (RESULT.__dict__['__args__'][0])
# example output: {'distance': 2.0, 'label': None}
```

See [User-defined dialogs / Executing dialogs / Dialog results](../python_api_introduction/user_defined_dialogs.md#dialog-results) for more details.

## How can I use an image from a script resource file in a user defined dialog?

You add your image file as a resource to the Add-on:

![Add-on Explorer - PNG file as resource](assets/resource_file_as_image_data.png)

You create a dialog file with an [Image widget](../python_api_introduction/user_defined_dialogs.md#image-widget), but without setting the actual image in the dialog editor.

In the Python script, you assign the resource as data to the image widget object:

```{code-block} python
import gom

DIALOG=gom.script.sys.create_user_defined_dialog (file='dialog.gdlg')

#
# Event handler function called if anything happens inside of the dialog
#
def dialog_event_handler (widget):
	pass

DIALOG.handler = dialog_event_handler

DIALOG.image.data = gom.app.resource[":example.png"]

RESULT=gom.script.sys.show_user_defined_dialog (dialog=DIALOG)
``` 

## How can I get the position of a label and apply it to another label? 

You can use `gom.script.cad.set_label_position()` to set the offset of the new label to the offset of the old label:

```{code-block} python
label_old = gom.app.project.inspection['Surface comparison 1'].deviation_label['Surface comparison 1.1']
label_new =gom.app.project.inspection['Surface comparison 1'].deviation_label['Surface comparison 1.2']

gom.script.cad.set_label_position(elements = [label_new], offset = label_old.label_offset_in_3d_view)
```

`offset` has the type `gom.Vec3d`.

## How can I conditionally set the label (border) color?

In the label properties, you can create a new label template and change the background color to 'dynamic'. This allows to add an expression in a Python-like syntax, e.g.

```{code-block} python
if result_dimension < result_dimension.upper_tolerance_limit:
    return color('#00ff5e')
else:
    return color('#ff0000')
```

See also [ZEISS Quality Tech Guide: Edit Expression (label background color)|https://techguide.zeiss.com/en/zeiss-inspect-2023/article/dlg_edit_dynamic_label_background_color_expression.html]

## How do I check if the sensor warm-up is completed or how long it will take, respectively?

```{code-block} python
remaining_warmup_time_in_seconds = gom.script.atos.wait_for_sensor_warmup (timeout = my_timeout)
```

The function blocks until the sensor is ready or the timeout specified with `my_timeout` occurs.
