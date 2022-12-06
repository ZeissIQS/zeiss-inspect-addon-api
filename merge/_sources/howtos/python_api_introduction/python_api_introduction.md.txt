# Python API introduction

```{note}
The basic introduction for the Python API used to be part of the GOM FAQ:

[Python API introduction - GOM FAQ](https://connect.gom.com/display/GKB/Expert+Knowledge+-+Scripting+in+GOM+Software)

Content will be migrated to here shortly.
```

## Access element properties

The "elements" of the GOM Software, i.e. what you see in the element explorer of your project, hold several properties and data which you can access using the Python API.

First of all, you need a reference to an element, which you can get either by [using a script dialog](https://connect.gom.com/display/GKB/Scripting+-+User-Defined+Dialogs) or simply by referencing it by name.

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

```{note}
This documentation used to be part of the GOM FAQ:

[GOM Connect - Data Interface](https://connect.gom.com/display/GPF/Mesh+data+of+elements)

Content will be migrated to here shortly.
```

% TODO: 