# scripted_scalar_check

![](scripted_scalar_check.jpg)

## Short description

This example shows how to create a scalar check by script. A scalar check is the most basic check, as it assigns a scalar value to an element. Nearly all elements you can find in the software can be checked like this.

```{note}
A scripted check has a lot in common with the scripted actual elements. Therefore, the identical mechanisms and concepts will not be explained here. See [How-to: Scripted actuals](../../howtos/scripted_elements/scripted_actuals.md) if you are not already familiar with the concept of scripted elements. 
```

## Highlights

First of all, we need to check if the element selected by the user by the `DIALOG.slct_element` widget is suitable for being checked with a scalar check. You can implement your own filter for that, but you can also use the API convenience function for that purpose:

```python
DIALOG.slct_element.filter = gom.api.scripted_checks_util.is_scalar_checkable
```

As you can assign a scalar value to all common element types, this filter allows all element types available in the *element explorer*.

Furthermore, as described in the [How-to: Scripted checks](../../howtos/scripted_elements/scripted_checks.md), the special parameters for scripted checks are also assigned in the `dialog` function. For ease of use, the respective dialog widgets are used, so we only need to assign the widgets' values to the parameters array.

```python 
def dialog (context, params):
  # [...]
  params['tolerance']     = DIALOG.tolerances.value
  params['unit']          = DIALOG.unit.value
  params['abbreviation']  = 'ScrSca'
```

In the calculation function, there is not much calculation but just an exemplary assignment of scalar values to the result. For the scripted `Scalar check`, the result dictionary needs to contain `"nominal"` and `"actual"` members, as well as a reference to the element which is checked.


```python
def calculation (context, params):
  # [...]
  for s in context.stages:
    actual_result  = 1.0
    nominal_result = 2.0
    
    context.result[s] = {"nominal" : nominal_result, 
              "actual" : actual_result, 
              "reference" : element }
  return True
```

## Related

* [How-to: Scripted checks](../../howtos/scripted_elements/scripted_checks.md)
* [Scripted Element API](../../python_api/scripted_elements_api.md)