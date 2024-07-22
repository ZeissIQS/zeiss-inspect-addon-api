# check_results_data_array

![](check_results_data_array.png)

## Short description

This example demonstrates two ways of accessing result data from checks using the element properties and data interfaces.

## Highlights

Basically, if you have obtained an `gom.Reference` element reference, e.g. by selecting an element by name (`gom.app.project.inspection['Surface comparison 1']`), you can access the results of the check:

1. **By evaluating an expression**

   `single_scalar_value = element.get ('result_dimension[0].deviation')`
  
* simple for single values
* works without using `numpy` library

2. **By the data interface of this element using the `.data` token**

   `scalars = np.array (element.data.result_dimension.deviation)`

* gets large datasets of all stages very efficiently

## Related

* How-to: [Access element properties and data](../../howtos/python_api_introduction/python_api_introduction.md#access-element-properties)