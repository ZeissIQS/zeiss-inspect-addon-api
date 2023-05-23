# Scripted elements API

This reference describes functions and data structures necessary for the implementation of "scripted elements".

```{seealso}
If you don't know about the concept yet, take a look at the [Scripted elements introduction](../howtos/scripted_elements/scripted_elements_introduction.md).
```

## The `dialog` function

```{note}
This content was previously part of the GOM Connect. See [here](https://connect.gom.com/display/GPF/Scripted+Elements+API+Reference).
% TODO: 
Content will be migrated shortly.
```


Notes:

* The main purpose of this function is to use display a script dialog and allow the user to enter element parameters.
* All tokens of other elements can be accessed within this function.

% Parameter: `context`: ...


## The `calculation` function

```{note}
This content was previously part of the GOM Connect. See [here](https://connect.gom.com/display/GPF/Scripted+Elements+API+Reference).
% TODO: 
Content will be migrated shortly.
```

Notes:
* It is not possible to call script commands or read tokens from within this function. (Do not call `gom.app.project....`)
* The function should loop over all stages to be calculated and set a computation result  for each stage.

% `context`: ...


## Scripted actuals - Return values

```{note}
This content was previously part of the GOM Connect. See [here](https://connect.gom.com/display/GPF/Scripted+Actual+Elements).
% TODO: 
Content will be migrated shortly.
```


% ### Element type: Point

% ```{py:function} context.result[s]
% 
% Test if the referenced element is suitable for inspection with a scalar check.
% 
% :API version: 1
% :param element: Element to be checked
% :type  element: Reference
% :return: True' if the given element s suitable for inspection with a scalar check.
% :rtype: bool
% ```

## Scripted checks - Return values

Scripted Checks extend the concept of scripted actual elements to be able to calculate custom inspections based on python scripts.

### Supported Element Types

The following actual element types are currently supported:

| Dialog Choice | Comment | Result format | Result description |
| ------------- | ------- | ------------- | ------------------ |
| Scalar        | Scalar check:<br>A single scalar value is assigned to an element | `result = {"nominal" : double, "actual" : double, "reference" : gom.Reference }`{l=python} | A nominal and actual double value are set, and a reference to element which was checked. |
| Scalar Surface | Surface check:<br>A scalar deviation value is assigned to each point of a mesh. | `result = { "deviation_values" : np.array(dtype=np.float32), "reference" : gom.Reference }`{l=python} | A list of deviation values for each point of a mesh. The mesh is also set as "reference" parameter.<p>The number of points of the mesh and the "deviation_values" array must match. |
| Scalar Curve | Curve check:<br>A scalar deviation value is assigned to each point on a curve. | `result = { "actual_values" : double, 'nominal_values': double, "reference" : gom.Reference}`{l=python} | A list of nominal and actual values for each point of a curve. The deviation values are calculated automatically as a difference between both.<p>The curve is also set as "reference" parameter.<p>The number of points of the curve and the value arrays must match. |
