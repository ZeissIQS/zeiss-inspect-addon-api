# ex14_volume_section

![Scripted volume section element example](ex14_volume_section.png)

This is an example for a scripted 'volume section' element. The dialog allows to select an image file, which is converted to a grayscale image and then to an `np.array()`. Further, a transformation is applied to the image.

```{note}
Please see [offset_point_v2.md](offset_point_v2.md) for a complete example with detailed description.
```

## Dialog event handler

```{code-block} python
---
linenos:
---
def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='ex14_volume_section.gdlg')

    if 'rx' in params:
        DIALOG.rx.value = params['rx']
    if 'ry' in params:
        DIALOG.ry.value = params['ry']
    if 'rz' in params:
        DIALOG.rz.value = params['rz']

    if 'dx' in params:
        DIALOG.dx.value = params['dx']
    if 'dy' in params:
        DIALOG.dy.value = params['dy']
    if 'dz' in params:
        DIALOG.dz.value = params['dz']

    if 'file' in params:
        DIALOG.file.value = params['file']

    # Get previous element name, when started from "Edit creation"
    if len(params) > 0:
        DIALOG.name.value = context.name

    # -------------------------------------------------------------------------
    def dialog_event_handler(widget):
        # No treatment of system events
        if str(widget) == 'system':
            return
        # If preview calculation returned with error
        if str(widget) == 'error':
            DIALOG.control.status = context.error
            return
        # If preview calculation was successful
        if str(widget) == 'calculated':
            DIALOG.control.status = ''
            DIALOG.control.ok.enabled = True
            return

        # All other changes in the dialog --> calculate preview
        params['rx'] = DIALOG.rx.value
        params['ry'] = DIALOG.ry.value
        params['rz'] = DIALOG.rz.value
        params['dx'] = DIALOG.dx.value
        params['dy'] = DIALOG.dy.value
        params['dz'] = DIALOG.dz.value
        params['file'] = DIALOG.file.value

        context.name = DIALOG.name.value
        DIALOG.control.ok.enabled = False
        context.calc(params=params, dialog=DIALOG)

    DIALOG.handler = dialog_event_handler
    # -------------------------------------------------------------------------
    RESULT = gom.script.sys.show_user_defined_dialog(dialog=DIALOG)
    return params
```

## Stageful calculation and error handling

```{code-block} python
---
linenos:
---
def calculation(context, params):
    valid_results = False

    file = params['file']

    # if filename starts with ':', it is an add-on resource used for testing,
    # e.g. ':ScriptedElementsExamples/Grayscale_8bits_palette.png'
    if file and file[0] == ':':
        # read resource
        test_image_resource = gom.Resource(file)
        test_image = test_image_resource.open().read()

        # convert resource to file object
        file = BytesIO(test_image)

    try:
        image = Image.open(file)
    except AttributeError:
        return False

    # convert image to grayscale
    image = image.convert('L')
    # print (image)
    img_array = np.array(image, dtype=np.float32)
    # print(f"img_array: {img_array}")
    # print(f"img_array.shape: {img_array.shape}")

    rx = params['rx']
    ry = params['ry']
    rz = params['rz']
    dx = params['dx']
    dy = params['dy']
    dz = params['dz']

    transformation = gom.Mat4x4([
        cos(rz) * cos(ry), cos(rz) * sin(ry) * sin(rx) - sin(rz) *
        cos(rx), cos(rz) * sin(ry) * cos(rx) + sin(rz) * sin(rx), dx,
        sin(rz) * cos(ry), sin(rz) * sin(ry) * sin(rx) + cos(rz) *
        cos(rx), sin(rz) * sin(ry) * sin(rx) - cos(rz) * sin(rx), dy,
        -sin(ry), cos(ry) * sin(rx), cos(ry) * cos(rx), dz,
        0, 0, 0, 1
    ])
    # print(transformation)

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = {
                'pixel_data': img_array,
                'transformation': transformation
            }
            context.data[stage] = {"ude_mykey": "Example 14"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
```

## Related

* [Scripted actuals - Volume section](../../python_api/scripted_elements_api.md#volume-section)
* [How-to: User-defined dialogs](../../howtos/python_api_introduction/user_defined_dialogs.md)