# ex05_cone

![Scripted cone element example](ex06_cone.png)

This is an example for a scripted 'cone' element. 

```{caution}
Due to the internal represenstation of a Cone Element, the direction of the vector `point1` -> `point2` is always from the smaller to the larger circle (`radius1` < `radius2`).

If you specify `radius1` > `radius2` in the creation parameters, [`point1`; `radius1`] and [`point2`; `radius2`] are swapped automatically.
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
    DIALOG = gom.script.sys.create_user_defined_dialog(file='ex06_cone.gdlg')

    if 'p1_x' in params:
        DIALOG.p1_x.value = params['p1_x']
    if 'p1_y' in params:
        DIALOG.p1_y.value = params['p1_y']
    if 'p1_z' in params:
        DIALOG.p1_z.value = params['p1_z']
    if 'p2_x' in params:
        DIALOG.p2_x.value = params['p2_x']
    if 'p2_y' in params:
        DIALOG.p2_y.value = params['p2_y']
    if 'p2_z' in params:
        DIALOG.p2_z.value = params['p2_z']
    if 'radius_1' in params:
        DIALOG.radius_1.value = params['radius_1']
    if 'radius_2' in params:
        DIALOG.radius_2.value = params['radius_2']

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
        params['p1_x'] = DIALOG.p1_x.value
        params['p1_y'] = DIALOG.p1_y.value
        params['p1_z'] = DIALOG.p1_z.value
        params['p2_x'] = DIALOG.p2_x.value
        params['p2_y'] = DIALOG.p2_y.value
        params['p2_z'] = DIALOG.p2_z.value
        params['radius_1'] = DIALOG.radius_1.value
        params['radius_2'] = DIALOG.radius_2.value

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
            context.result[stage] = {'default': {
                'point1': gom.Vec3d(params['p1_x'], params['p1_y'], params['p1_z']),
                'radius1': params['radius_1'],
                'point2': gom.Vec3d(params['p2_x'], params['p2_y'], params['p2_z']),
                'radius2': params['radius_2']
            }}
            context.data[stage] = {"ude_mykey": "Example 6"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
```

## Related

* [Scripted actuals - Cone](../../python_api/scripted_elements_api.md#cone)
* [How-to: User-defined dialogs](../../howtos/python_api_introduction/user_defined_dialogs.md)