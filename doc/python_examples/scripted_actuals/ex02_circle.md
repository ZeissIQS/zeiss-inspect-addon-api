# ex2_circle

![Scripted circle element example](ex02_circle.png)

This is an example for a scripted 'circle' element.

```{note}
Please see [offset_point_v2.md](offset_point_v2.md) for a complete example with detailed description.
```

## Dialog event handler

```{code-block} python
---
linenos:
---
def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='ex02_circle.gdlg')

    if 'center_x' in params:
        DIALOG.center_x.value = params['center_x']
    if 'center_y' in params:
        DIALOG.center_y.value = params['center_y']
    if 'center_z' in params:
        DIALOG.center_z.value = params['center_z']
    if 'dir_x' in params:
        DIALOG.dir_x.value = params['dir_x']
    if 'dir_y' in params:
        DIALOG.dir_y.value = params['dir_y']
    if 'dir_z' in params:
        DIALOG.dir_z.value = params['dir_z']
    if 'radius' in params:
        DIALOG.radius.value = params['radius']

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
        params['center_x'] = DIALOG.center_x.value
        params['center_y'] = DIALOG.center_y.value
        params['center_z'] = DIALOG.center_z.value
        params['dir_x'] = DIALOG.dir_x.value
        params['dir_y'] = DIALOG.dir_y.value
        params['dir_z'] = DIALOG.dir_z.value
        params['radius'] = DIALOG.radius.value

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

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = {
                'center': (params['center_x'], params['center_y'], params['center_z']),
                'direction': (params['dir_x'], params['dir_y'], params['dir_z']),
                'radius': params['radius']
            }
            context.data[stage] = {"ude_mykey": "Example 2"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
```

## Related

* [Scripted actuals - Circle](../../python_api/scripted_elements_api.md#circle)
* [How-to: User-defined dialogs](../../howtos/python_api_introduction/user_defined_dialogs.md)