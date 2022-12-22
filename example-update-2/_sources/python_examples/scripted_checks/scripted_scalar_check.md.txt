# scripted_scalar_check

![](scripted_scalar_check.jpg)

## Short description

This example shows how to create a scalar check by script. A scalar check is the most basic check, as it assigns a scalar value to an element. Nearly all elements you can find in the software can be checked like this.

```{note}
A scripted check has a lot in common with the scripted actual elements. Therefore, the identical mechanisms and concepts will not be explained here. See [How-to: Scripted actuals](../../howtos/scripted_elements/scripted_actuals.md) if you are not already familiar with the concept of scripted elements. 
```

## Highlights
 

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