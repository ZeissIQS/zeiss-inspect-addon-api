# ex08_surface

![Scripted surface element example](ex08_surface.png)

This is an example for a scripted 'surface' element. The dialog allows to specify the coordinates of eight vertices defining a mesh. The triangles for defining the mesh are hard-coded in this example. The resulting body is a cuboid.

```{note}
The mesh triangles are defined by indices into the array of vertices. The vertices defining a triangle must be specified in counter-clockwise
order (as viewed from outside).
```

```{note}
Please see [offset_point_v2.md](offset_point_v2.md) for a complete scripted elements example with detailed description.
```

## Dialog event handler

```{code-block} python
---
linenos:
---
def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='ex08_surface.gdlg')

    if 'v0_x' in params:
        DIALOG.v0_x.value = params['v0_x']
    if 'v0_y' in params:
        DIALOG.v0_y.value = params['v0_y']
    if 'v0_z' in params:
        DIALOG.v0_z.value = params['v0_z']
    #[...]
    if 'v7_z' in params:
        DIALOG.v7_z.value = params['v7_z']

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
        
    params['v7_z'] = DIALOG.v7_z.value

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
    v0 = gom.Vec3d(params['v0_x'], params['v0_y'], params['v0_z'])
    #[...]
    v7 = gom.Vec3d(params['v7_x'], params['v7_y'], params['v7_z'])

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = {
                'vertices': [v0, v1, v2, v3, v4, v5, v6, v7],
                             # two triangles per side of the cuboid
                             # ----- front ------ , ----- right ------- , ----- top ----------
                'triangles': [(0, 1, 2), (0, 2, 3), (1, 5, 6), (1, 6, 2), (3, 2, 6), (3, 6, 7),
                             # ----- bottom ----- , ----- back -------- , ----- left ---------
                              (0, 1, 5), (0, 5, 4), (4, 5, 6), (4, 6, 7), (0, 4, 7), (0, 7, 3)]
            }
            context.data[stage] = {"ude_mykey": "Example 8"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
```

## Related

* [Scripted actuals - Surface](../../python_api/scripted_elements_api.md#surface)
* [How-to: User-defined dialogs](../../howtos/python_api_introduction/user_defined_dialogs.md)