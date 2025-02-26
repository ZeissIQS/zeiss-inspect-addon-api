# Scripted checks

```{note}
  This section assumes that you are familiar with the basic concept of Scripted elements. If not, take a look at the [Introduction](scripted_elements_introduction.md) and [Scripted actuals](scripted_actuals.md) sections.
```
## Introduction

Scripted checks are a specialization of scripted elements to realize customized inspections in the ZEISS Software. Use checks if you want to display the deviation of certain properties of *existing* elements.

## Writing a scripted check

The script structure to create a scripted check is the same as for [Scripted actuals](scripted_actuals.md). However, there are some specialities:

### Useful dialog widgets

In most cases, you need to ask the user for the element to check, check naming or tolerance inputs. To this end, you can use the `Selection element`, `Element name`, `Unit` and `Tolerances` widgets:

![Widgets for scripted checks](assets/scripted_check_widgets.png)

### "Special" parameters

For a successful integration with the native checks, unit and tolerance need to be set to the returned `params`.

```python
  params['tolerance']    = DIALOG.tolerances.value
  params['unit']         = DIALOG.unit.value
  params['abbreviation'] = 'ScrSca'
```

Furthermore, checks shall be assigned an `abbreviation`. This is the short form you'll see in the 3D view labels of the check, or in the result table.

```{seealso}
* Detailed description of the [Scripted element API](../../python_api/scripted_elements_api.md)
* Documentation of the [Unit widget](../python_api_introduction/user_defined_dialogs.md#unit-widget)
* Documentation of the [Tolerances widget](../python_api_introduction/user_defined_dialogs.md#tolerances-widget) 
```

## Types of scripted checks

Currently, three types of scripted checks are supported. The `Python API Examples` App provides examples for all three. Click on the respective links to get to the example documentation.

* Scripted scalar check: Check an element and assign a simple scalar value pair (nominal/actual) to it. See <a href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_checks/ScriptedScalarCheck/doc/Documentation.md">ScriptedScalarCheck</a>.
* Scripted curve check: Check an existing *curve* element and assign actual/nominal values for each point of the curve. See <a href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_checks/ScriptedCurveCheck/doc/Documentation.md">ScriptedCurveCheck</a>.
* Scripted surface check: Check an existing *mesh* element and assign deviation values for each point in the mesh. See <a href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_checks/ScriptedSurfaceCheck/doc/Documentation.md">ScriptedSurfaceCheck</a>.

% Special API functions used to handle checks.
% 
% ## Special parameters of scripted checks
% 
% * tolerances
% * units
% * ...
