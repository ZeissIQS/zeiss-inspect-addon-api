# Scripted elements API

This reference describes functions and data structures necessary for the implementation of "scripted elements".

```{seealso}
If you don't know about the concept yet, take a look at the [Scripted elements introduction](../howtos/scripted_elements/scripted_elements_introduction.md).
```

## The `dialog` function

```{note}
This content was previously part of the GOM Connect. See [here](https://connect.gom.com/display/GPF/Scripted+Elements+API+Reference).

Content will be migrated shortly.
```


Notes:

* The main purpose of this function is to use display a script dialog and allow the user to enter element parameters.
* All tokens of other elements can be accessed within this function.

% Parameter: `context`: ...


## The `calculation` function

```{note}
This content was previously part of the GOM Connect. See [here](https://connect.gom.com/display/GPF/Scripted+Elements+API+Reference).

Content will be migrated shortly.
```

Notes:
* It is not possible to call script commands or read tokens from within this function. (Do not call `gom.app.project....`)
* The function should loop over all stages to be calculated and set a computation result  for each stage.

% `context`: ...


## Scripted actuals - Return values

```{note}
This content was previously part of the GOM Connect. See [here](https://connect.gom.com/display/GPF/Scripted+Actual+Elements).

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

```{note}
This content was previously part of the GOM Connect. See [here](https://connect.gom.com/display/GPF/Scripted+Checks).

Content will be migrated shortly.
```


