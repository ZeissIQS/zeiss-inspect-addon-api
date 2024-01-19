# ex12_volume_defects

![Scripted volume defects element example](ex12_volume_defects.png)

This is an example for a scripted 'volume defects' element. Each defect is defined by a mesh. In this example, a single defect is created by setting the coordinates of four vertices from a dialog. The mesh triangles are hard-coded in the `calculation()` function. The resulting element has the shape of a tetrahedron.

```{note}
The mesh triangles are defined by indices into the array of vertices. The vertices defining a triangle must be specified in counter-clockwise
order (as viewed from outside).
```

```{note}
Please see [offset_point_v2.md](offset_point_v2.md) for a complete example with detailed description.
```

## Dialog event handler

```{code-block} python
---
linenos:
---
def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='ex12_volume_defects.gdlg')

    if 'v0_x' in params:
        DIALOG.v0_x.value = params['v0_x']
    if 'v0_y' in params:
        DIALOG.v0_y.value = params['v0_y']
    if 'v0_z' in params:
        DIALOG.v0_z.value = params['v0_z']

    #[...]
    
    if 'v3_z' in params:
        DIALOG.v3_z.value = params['v3_z']

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
        params['v0_x'] = DIALOG.v0_x.value
        params['v0_y'] = DIALOG.v0_y.value
        params['v0_z'] = DIALOG.v0_z.value
        #[...]
        params['v3_z'] = DIALOG.v3_z.value

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
    v0 = (params['v0_x'], params['v0_y'], params['v0_z'])
    v1 = (params['v1_x'], params['v1_y'], params['v1_z'])
    v2 = (params['v2_x'], params['v2_y'], params['v2_z'])
    v3 = (params['v3_x'], params['v3_y'], params['v3_z'])

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = {
                'vertices': [np.array([v0, v1, v2, v3])],
                # Note:
                # Triangles are defined by indices into the array of vertices.
                # The vertices defining a triangle must be specified in counter-clockwise
                # order, otherwise the resulting surface would be inverted, i.e. invisible!
                'triangles': [np.array([(0, 1, 2), (1, 0, 3), (0, 2, 3), (2, 1, 3)])]
            }
            context.data[stage] = {"ude_mykey": "Example 12"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
```

## Related

* [Scripted actuals - Volume defects](../../python_api/scripted_elements_api.md#volume-defects)
* [How-to: User-defined dialogs](../../howtos/python_api_introduction/user_defined_dialogs.md)