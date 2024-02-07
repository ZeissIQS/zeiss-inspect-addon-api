# scripted_element_progress

![](scripted_element_progress_preview.jpg)

![](scripted_element_progress_computation.jpg)
## Short description

This examples demonstrates how to show progress information to the user while calcualting a scripted element.
## Highlights

The scripted element itself is not of interest here, as it is rather meaningless: a point that will always be created at *(1,0,0)*.
To showcase the display of calculation progress, a loop with 100 steps containing a `sleep` call to simulate computation are performed in the `calculation` function:

```python
def calculation (context, params):
  context.progress_stages_total = limit
  for i in range(limit):
    context.progress_stages_computing = i
    time.sleep (0.1)

  # [...]
``` 
To indicate progress, you need to set `context.progress_stages_total` to the amount of steps you expect to compute. This can but not has to be the number of stages in trend projects. You can also set any arbitrary number. As soon as you set `context.progress_stages_computing`, the progress will be indicated in the bottom are of the application (see top screenshot).

## Related

* How-to: [Scripted actuals](../../howtos/scripted_elements/scripted_actuals.md)