# ex09_point_cloud

![Scripted point cloud element example](ex09_point_cloud.png)

This is an example for a scripted 'point cloud' element. A parametric function is used to define the points, in this case the surface points of a torus. `np.arange()` is used to iterate from `u_min` to `u_max` and from `v_min` to `v_max` with non-integer step sizes. The step sizes `u_steps` and `v_steps` define the point density.

```{note}
Please see [offset_point_v2.md](offset_point_v2.md) for a complete scripted elements example with detailed description.
```

## Dialog event handler

```{code-block} python
---
linenos:
---
def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='ex09_point_cloud.gdlg')

    if 'R' in params:
        DIALOG.R.value = params['R']
    if 'r' in params:
        DIALOG.r.value = params['r']
    if 'u_min' in params:
        DIALOG.u_min.value = params['u_min']
    if 'u_max' in params:
        DIALOG.u_max.value = params['u_max']
    if 'u_steps' in params:
        DIALOG.u_steps.value = params['u_steps']
    if 'v_min' in params:
        DIALOG.v_min.value = params['v_min']
    if 'v_max' in params:
        DIALOG.v_max.value = params['v_max']
    if 'v_steps' in params:
        DIALOG.v_steps.value = params['v_steps']

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
        params['R'] = DIALOG.R.value
        params['r'] = DIALOG.r.value
        params['u_min'] = DIALOG.u_min.value
        params['u_max'] = DIALOG.u_max.value
        params['u_steps'] = DIALOG.u_steps.value
        params['v_min'] = DIALOG.v_min.value
        params['v_max'] = DIALOG.v_max.value
        params['v_steps'] = DIALOG.v_steps.value

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
            # Creating a list of points using a parametric curve function:
            #            / (R+r*cos(v))*cos(u) \
            # P(u, v) = |  (R+r*cos(v))*sin(u)  |
            #            \ r*sin(v)            /
            # with u in [u_min...u_max], v in [v_min...v_max]
            points = []
            for u in np.arange(params['u_min'], params['u_max'], (params['u_max'] - params['u_min']) / params['u_steps']):
                for v in np.arange(params['v_min'], params['v_max'], (params['v_max'] - params['v_min']) / params['v_steps']):
                    p = gom.Vec3d(
                        (params['R'] + params['r'] * math.cos(v * math.pi)) * math.cos(u * math.pi),
                        (params['R'] + params['r'] * math.cos(v * math.pi)) * math.sin(u * math.pi),
                        params['r'] * math.sin(v * math.pi)
                    )
                    points.append(p)

            context.result[stage] = {'points': points}
            context.data[stage] = {"ude_mykey": "Example 9"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
```

## Related

* [Scripted actuals - Curve](../../python_api/scripted_elements_api.md#curve)
* [How-to: User-defined dialogs](../../howtos/python_api_introduction/user_defined_dialogs.md)