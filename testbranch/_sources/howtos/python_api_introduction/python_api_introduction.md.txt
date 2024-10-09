---
myst:
   html_meta:
      "description": "Introduction to the Python API for extending ZEISS INSPECT 2025 with Apps"
      "keywords": "Metrology, ZEISS INSPECT, Python API, GOM API, Scripting, Add-ons, Apps, How-tos"
---

# ZEISS INSPECT Python API Introduction

Welcome to the ZEISS INSPECT Python API introduction. This is your starting point into App development for ZEISS INSPECT. Here you find out what you can do with Apps, how they work and how you create them.

See [Introduction to Python Scripting](https://techguide.gom.com/en/zeiss-inspect-2023/article/introduction_to_python_scripting.html) if you are new to Python or the ZEISS INSPECT Python interface.

## Creating projects

You can create a new, empty project as follows:

``` Python
# Create a new project
gom.script.sys.create_project ()
```

```{note}
This way, a project in the default workflow (part-based) is created. For the legacy workflow (part-less), please refer to [Scripting with legacy projects \(part-less\)](../scripting_legacy_projects/scripting_legacy_projects.md)
```

## Creating parts

The evaluation elements are usually placed under a "part". Accordingly, an empty part can be created as follows:

``` Python
# Creates a new part in your project with the name 'Part 1'
PART_OBJECT = gom.script.part.create_new_part (name='Part 1')
```

An existing part can be accessed via name or index in the new category:

``` Python
# Access the part object via name
PART_OBJECT = gom.app.project.parts['Part 1']
 
# or via index
PART_OBJECT = gom.app.project.parts[0]
 
# you can access all parts via iterating over the parts attribute
for p in gom.app.project.parts:
    print (p)
```

## Adding elements to a part

If an actual mesh or CAD or elements are imported into a part project, different options are available. For scripting, the import is always separated into two different steps.

1. Importing the elements into the *Elements in clipboard*
2. Add the imported elements to a created part

Example:

``` Python
gom.script.part.create_new_part (name='Part 1')
 
# import element into 'Element in clipboard'
gom.script.sys.import_g3d (
  files=['D:/zeiss_part.g3d'],
  import_mode='clipboard'
)
 
# Move it to a created part
gom.script.part.add_elements_to_part (
  delete_invisible_elements=True,
  elements=[gom.app.project.clipboard.actual_elements['zeiss_part']],
  import_mode='new_elements',
  part=gom.app.project.parts['Part 1'])

```

In the same way, a CAD can be imported into a part project.

Constructing new elements based on elements which already belong to a part are automatically added to that part.

## Accessing CAD and actual mesh

A **mesh element** of a part can be accessed in the following ways:

``` Python
# This is usually the most elegant way and is recommended.
# Replacing your mesh will keep the correct parametric if you use
# the actual values reference (like formerly the 'Actual master' in the part-less workflow).
PART_OBJECT = gom.app.project.parts['Part 1']
MESH_PROXY = gom.ActualReference (PART_OBJECT)
 
# If you really like to access the representing CAD Element (which is not always existing, e.g. for planning)
# you can access this element via
MESH_ELEMENT = gom.ActualReference(PART_OBJECT).actual

```

The **CAD** of a part can be addressed in the following ways:

``` Python
# This is usually the most elegant way and is recommended.
# Replacing your CAD will keep the correct parametric if you use
# the nominal values reference (like formerly the 'All CAD Group proxy' in the part-less workflow)
PART_OBJECT = gom.app.project.parts['Part 1']
CAD_PROXY = gom.NominalReference (PART_OBJECT)
 
# If you really like to access the representing CAD Element (which is not always existing, e.g. for planning)
# you can access this element via
CAD_ELEMENT = gom.NominalReference(PART_OBJECT).nominal
```

## Accessing an object's part

This information can be retrieved via an attribute of the object. Here is an example:

``` Python
PART_OBJECT = gom.app.project.inspection['Point 1'].part
```

## Accessing all elements and alignments of a part

One possibility is to iterate over all elements in the different categories (nominal, actual, inspection, alignments) and to check the part attribute. Usually, for most applications this can be achieved easier using an `ElementSelection` (some elements are hidden and not listed, but usually you do not need access to these elements). Here is an example:

``` Python
for x in gom.ElementSelection ({'category': ['key', 'elements', 'part', gom.app.project.parts['Part']]}):
    print (x)
```

See [Selecting elements in scripts](selecting_elements.md) for more details.

## Accessing elements and alignments of *Element in clipboard*

Also, these elements can be easily accessed via an `ElementSelection`:

``` Python
for x in gom.ElementSelection ({'category': ['key', 'elements', 'is_element_in_clipboard', 'True']}):
    print (x)
```

## Alignments

Alignments are still accessible via `gom.app.project.alignments` (like in the legacy workflow). The same is valid for `gom.app.project.nominal_elements`, `gom.app.project.actual_elements` and `gom.app.project.inspection`. You have to keep in mind that you will get all elements or alignments of all parts. You can use the `part` token to establish to which part an alignment belongs to or you use an `ElementSelection` (see examples above):

``` Python
for x in gom.ElementSelection ({'category': ['key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'alignment']}):
    print (x)
```

There is one special handling for multiple parts and scripting with the *Original alignment*. To distinguish these alignments for different parts, the scripting name contains the part name and is modified into:

``` Python
gom.app.project.alignments['<Name of the part>::Original alignment']
```

## Access element properties

The "elements" of the GOM Software, i.e. what you see in the element explorer of your project, hold several properties and data which you can access using the Python API.

First of all, you need a reference to an element, which you can get either by [using a script dialog](user_defined_dialogs.md) or simply by referencing it by name.

If you have installed the `Python API Examples` App from the store and loaded the `zeiss_part_test_project` (see the [Python API Examples Documentation](../../python_examples/index.md)), you can reference the mesh like this:

```python
mesh_element = gom.app.project.parts['Part'].actual
```

### Explore available properties

Once you have a reference to an element, you can access its properties using several keywords in the form `element.<keyword>`.

One way to inspect the available keys is by using the 'Script Object' explorer, which is available from the Script Editor's context menu: RMB ► Insert ► Element Value (shortcut `F2`).

```{image} assets/insert_element_value.png
:alt: Insert Element Value
:width: 350px
```

```{image} assets/script_object_explorer.png
:alt: Script Object Explorer
:width: 350px
```

You will find several keywords in the Object Explorer, with a preview of the current value.
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

In most cases, the data interfaces are based on the Python package [NumPy](https://numpy.org/).

```{caution}
Due to breaking changes in NumPy 2.0.0 (see [NumPy 2.0.0 Release Notes](https://github.com/numpy/numpy/releases/tag/v2.0.0)), the latest NumPy 1.x version must be used with ZEISS INSPECT 2025.
```

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

```{note}
When accessing the image, the complete data set is *not* transferred immediately from C++ to Python! Instead this happens just in the moment when it is converted into a numpy array!
```

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

## Exception handling

With the ZEISS INSPECT App API, three different types of exceptions can occur:
* Python built-in exceptions
* User defined exceptions, e.g. from a Python module
* ZEISS INSPECT App API exceptions

It is [recommended practice](https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/bare-except.html) to avoid bare except clauses, i.e. to specify an exception type:

```{code-block} python
try:
    calling_for_trouble() # could raise an exception
except <exception_type>:
    # exception handling
```

If the type of exception is unknown, it can be identified as follows:
```{code-block} python
try:
    calling_for_trouble() # could raise an exception; type unknown yet
except Exception as e:
    print( type(e) ) # e.g.: <class 'gomlib.api.GomApiError'>
```

Now you can specify the expected exception type correctly:
```{code-block} python 
import gomlib
...
try:
    calling_for_trouble() # could raise a GomApiError exception
except gomlib.api.GomApiError:
    # exception handling
