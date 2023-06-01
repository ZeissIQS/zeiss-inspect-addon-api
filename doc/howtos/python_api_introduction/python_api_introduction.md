# Python API introduction

```{note}
The basic introduction for the Python API used to be part of the GOM FAQ:

[Python API introduction - GOM FAQ](https://connect.gom.com/display/GKB/Expert+Knowledge+-+Scripting+in+GOM+Software)

Content will be migrated to here shortly.
```

## Access element properties

The "elements" of the GOM Software, i.e. what you see in the element explorer of your project, hold several properties and data which you can access using the Python API.

First of all, you need a reference to an element, which you can get either by [using a script dialog](user_defined_dialogs.md) or simply by referencing it by name.

If you have installed the `Python API Examples` add-on from the store and loaded the `gom_part_test_project` (see the [Python API Examples Documentation](../../python_examples/index.md)), you can reference the mesh like this:

```python
mesh_element = gom.app.project.parts['Part'].actual
```

### Explore available properties

Once you have a reference to the element, you can access its properties using several keywords in the form `element.<keyword>`.

One way to inspect the available keys is by using the 'Script Object' explorer, which is available from the context menu `-> Insert -> Element Value` or by shortcut `F2`.


```{image} assets/script_object_explorer.jpg
:alt: Script Object Explorer
:width: 350px
```

You will find several keywords there, with a preview of the current value.
If you click `OK`, the complete call, including element reference by name, will be copied to your current script. If you already have a name reference, you can of course use this reference.

```python
mesh_element = gom.app.project.parts['Part'].actual
print (mesh_element.area)
```
Output:
```
>>> 207422.1875
```

### Element properties in VSCode

Using Visual Studio Code, you can get auto-completion for the usable keywords directly in a pop-up. 

![Keywords in VSCode](../using_vscode_editor/assets/inserting_keywords.png)

See [Using VSCode Editor](../using_vscode_editor/using_vscode_editor.md) for details.


### Properties of different stages

If you are using a multi-stage project, the approach as described above will always give you the element properties in the current stage. If you need access to properties in a different stage, you can use the `in_stage[s]` modifier:

```python
mesh_element = gom.app.project.parts['Part'].actual
print (mesh_element.in_stage[0].area)
```
Output:
```
>>> 207422.1875
```

```{note}
Stage indices start with index `0`.
```

In this way, you can get simple properties of a different stage. If you need access to data of all stages at once, especially for larger data (like arrays of vertices), use "Data interfaces" as described below.


## Element data interfaces

In a script, each element present in the application (project, inspection elements, reports, ...) can be referenced by a named identifier. Each identifier consists of a type and some index, which can be a name or an integer number.

### Concept
This is already the case for access via the data interface instead of the token interface: The returned value has the format `(stages, <index dimensions>)`.

```{code-block} python
:caption: Example 1 - Mesh

# Mesh in 8 stage trend project with 238654 points, each with one (x, y, z) triple
> print (gom.app.project.parts['Part'].actual.data.coordinate.shape)
(8, 238654, 3)
```

```{code-block} python
:caption: Example 2 - Scalar value

# Single scalar value in a 8 stages trend project
> print (gom.app.project.inspection['My Check'].data.result_dimension.deviation.shape)
(8, 1)
```

```{code-block} python
:caption: Example 3 - Image

# Image in 8 stage trend project with 4000x3000 pixels, each with one (r, g, b, a) tuple
> print (gom.app.project.measurement_list['Scan'].measurement['M1'].images['Left camera'].data.rgb.shape)
(8, 3000, 4000, 4)
```

⚠️ When accessing the image, the complete data set is *not* transferred immediately from C++ to Python! Instead this happens just in the moment when it is converted into a numpy array!

```{code-block} python
:caption: Example 4 - Transferring image data

# Fetch gom.Array with image data in all stages (not transferred !)
> image = gom.app.project.measurement_list['Scan'].measurement['M1'].images['Left camera'].data.rgb
> print (image.shape, type (image))
(8, 3000, 4000, 4), gom.Array ()
# 45 MB Image data if on stage, transferred in < 100 ms
> data = np.array (image[0])
> print (data.shape)
(3000, 4000, 4)
```

<!--
About the notation:
We thought about this for quite a long time. The problem is, that we have multiple data dimensions on one hand (elements, stages, indices, alignments), but just one index operator '[]' on the other hand. We cannot mix this up like {{A[element name].B[stage]...}}.
Well, this is not entirely true, as expressions like {{gom.app.project.actual['Mesh'].coordinate[1000]}} are possible, but in this case at least the index is (element, element, element, ..., point) and not something when a stage of point is in the middle of the path.

So the following procedure is recommended:
* Evaluate if the staged {{data}} tokens plus the regular stageless global tokens are sufficient.
* If it is really necessary to access a token which is not delivered via a data interface in another stage, we must think again.
* Global stage switching cannot be the solution in UDEs at all, of course. So I would prefer something like this *if really necessary* 

Example:

```Python
current_stage = context.stage
context.stage = 14
# Query token in stage 14
value = gom.app.project.nominal['Nominal value'].scalar_value
context.stage = current_stage
```

* This will not switch stages, but all future token queries of this UDE script run will use stage 14.
* Of course, this can be done much more simple with:

```Python
# Deformation project with 800 stages
> values = gom.app.project.nominal['Nominal value'].data.scalar_value
> print (value.shape)
(800, 1)
```

-->

% TODO: 