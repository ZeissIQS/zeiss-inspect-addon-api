# ex13_volume_region

![Scripted volume region example](ex13_volume_region.png)

This is an example for a scripted 'volume region' element. The dialog allows to select a linked volume element and to set offset (in the global coordinate system) as well as the dimensions (in the voxel coordinate system) of the volume region. In this example, the volume region is shown in light green.

```{caution}
The voxel (measurement) coordinate system may differ from the CAD coordinate system. 
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
    DIALOG = gom.script.sys.create_user_defined_dialog(file='ex13_volume_region.gdlg')

    if 'x0' in params:
        DIALOG.x0.value = params['x0']
    if 'y0' in params:
        DIALOG.y0.value = params['y0']
    if 'z0' in params:
        DIALOG.z0.value = params['z0']

    if 'dx' in params:
        DIALOG.dx.value = params['dx']
    if 'dy' in params:
        DIALOG.dy.value = params['dy']
    if 'dz' in params:
        DIALOG.dz.value = params['dz']

    if 'volume_ele' in params:
        DIALOG.volume_ele.value = params['volume_ele']

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
        params['dx'] = DIALOG.dx.value
        params['dy'] = DIALOG.dy.value
        params['dz'] = DIALOG.dz.value
        params['volume_ele'] = DIALOG.volume_ele.value

        if DIALOG.volume_ele is None:
            context.name = "New Volume Region"
        else:
            context.name = str(DIALOG.volume_ele.value) + ".Region"
        DIALOG.control.ok.enabled = False
        context.calc(params=params, dialog=DIALOG)

    def element_filter(element):
        try:
            if element.type == 'volume' or element.type == 'linked_volume':
                return True
        except Exception as e:
            pass
        return False

    DIALOG.volume_ele.filter = element_filter
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

    x0 = params['x0']
    y0 = params['y0']
    z0 = params['z0']

    dx = int(params['dx'] / params['volume_ele'].voxel_size.x)
    dy = int(params['dy'] / params['volume_ele'].voxel_size.y)
    dz = int(params['dz'] / params['volume_ele'].voxel_size.z)

    # Calculating all available stages
    for stage in context.stages:
        # Access element properties with error handling
        try:
            context.result[stage] = {
                'volume_element': params['volume_ele'],
                'offset': gom.Vec3d(x0, y0, z0),
                'voxel_data': np.ones((dx, dy, dz), dtype=np.uint8)
            }
            context.data[stage] = {"ude_mykey": "Example 13"}
        except Exception as error:
            context.error[stage] = str(error)
        else:
            valid_results = True
    return valid_results
```

## Related

* [Scripted actuals - Section](../../python_api/scripted_elements_api.md#volume-region)
* [How-to: User-defined dialogs](../../howtos/python_api_introduction/user_defined_dialogs.md)