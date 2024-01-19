# ex03_curve

![Scripted curve element example](ex03_curve.png)

This is an example for a scripted 'curve' element. A parametric function is used to create a 3-dimensional curve - a helix - with a fixed number of points. `np.arange()` is used to iterate from `t_min` to `t_max` with a non-integer step size.

```{note}
Please see [offset_point_v2.md](offset_point_v2.md) for a complete example with detailed description.
```

## Dialog event handler

```{code-block} python
---
linenos:
---
def dialog(context, params):
    DIALOG = gom.script.sys.create_user_defined_dialog(file='ex03_curve.gdlg')

    if 'x0' in params:
        DIALOG.x0.value = params['x0']
    if 'y0' in params:
        DIALOG.y0.value = params['y0']
    if 'z0' in params:
        DIALOG.z0.value = params['z0']
    if 'radius' in params:
        DIALOG.radius.value = params['radius']
    if 'j' in params:
        DIALOG.j.value = params['j']
    if 'k' in params:
        DIALOG.k.value = params['k']
    if 't_min' in params:
        DIALOG.t_min.value = params['t_min']
    if 't_max' in params:
        DIALOG.t_max.value = params['t_max']

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
        params['x0'] = DIALOG.x0.value
        params['y0'] = DIALOG.y0.value
        params['z0'] = DIALOG.z0.value
        params['radius'] = DIALOG.radius.value
        params['j'] = DIALOG.j.value
        params['k'] = DIALOG.k.value
        params['t_min'] = DIALOG.t_min.value
        params['t_max'] = DIALOG.t_max.value

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
import math
import numpy as np

def calculation(context, params):
    valid_results = False

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            # Creating a list of points using a parametric curve function:
            # P(t) = ( x0 + (j * t + r) * cos(t), y0 + (j * t + r) * cos(t), z0 + k * t )
            # with t in [t_min...t_max], 1000 steps
            points = []
            for t in np.arange(params['t_min'], params['t_max'], (params['t_max'] - params['t_min']) / 1000):
                points.append((params['x0'] + (params['j'] * t + params['radius']) * math.cos(t),
                            params['y0'] + (params['j'] * t + params['radius']) * math.sin(t),
                            params['z0'] + params['k'] * t)
                            )
            context.result[stage] = [{'points': points}]
            context.data[stage] = {"ude_mykey": "Example 3"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
```

## Related

* [Scripted actuals - Curve](../../python_api/scripted_elements_api.md#curve)
* [How-to: User-defined dialogs](../../howtos/python_api_introduction/user_defined_dialogs.md)