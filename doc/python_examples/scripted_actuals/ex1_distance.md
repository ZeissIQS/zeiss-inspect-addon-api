# ex1_distance

![Scripted distance element example](ex1_distance.png)

```{note}
This is an example for a scripted 'distance' element. Please see [offset_point_v2.md](offset_point_v2.md) for a complete example with detailed description.
```

## Dialog event handler

```{code-block} python
---
linenos:
---
def dialog(context, params):
	DIALOG = gom.script.sys.create_user_defined_dialog(file='ex01_distance.gdlg')

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
		if str(widget) == 'initialize':
			gom.script.view.show_view_frustum_draft(enable=True)
			gom.script.view.auto_zoom(enable=True)

		# All other changes in the dialog --> calculate preview
		params['p1_x'] = DIALOG.p1_x.value
		params['p1_y'] = DIALOG.p1_y.value
		params['p1_z'] = DIALOG.p1_z.value
		params['p2_x'] = DIALOG.p2_x.value
		params['p2_y'] = DIALOG.p2_y.value
		params['p2_z'] = DIALOG.p2_z.value

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
				'point1': (params['p1_x'], params['p1_y'], params['p1_z']),
				'point2': (params['p2_x'], params['p2_y'], params['p2_z'])
			}
			context.data[stage] = {"ude_mykey": "Example 1"}
		except Exception as error:
			context.error[stage] = str(error)
		else:
			valid_results = True
	return valid_results
```

## Related

* [Scripted actuals](../../python_api/scripted_elements_api.md#distance)
* [How-to: User-defined dialogs](../../howtos/python_api_introduction/user_defined_dialogs.md)