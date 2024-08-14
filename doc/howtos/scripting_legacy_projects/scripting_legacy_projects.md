---
myst:
   html_meta:
      "description": "Python API for extending ZEISS INSPECT 2025 with Apps - Legacy Projects"
      "keywords": "Metrology, ZEISS INSPECT, Python API, GOM API, Scripting, Add-ons, Apps, How-tos, Partless Projects"
---
# Scripting with legacy projects (part-less)

```{caution}
You can skip this section unless you are dealing with legacy projects!
```

As shown in [ZEISS INSPECT Python API Introduction](../python_api_introduction/python_api_introduction.md), the following code creates a project in the part-based workflow, which allows to analyze multiple parts:

``` Python
# Create a project (default; part-based workflow)
gom.script.sys.create_project ()

# For compatibility, the kind of project can be stated explicitely:
# Create a project (part-based workflow)
gom.script.sys.create_project (type=2018)
```

You can still create a project in the legacy workflow, which is restricted to a single part:

``` Python
# Create a project (part-less workflow)
# Note: This allows to analyze a single part only!
gom.script.sys.create_project (type=2016)
```

Use the following code to determine the type of an existing project:

``` Python
if gom.app.project.is_part_project:
    print ('Is part project: True')
else:
    print ('Is part project: False')
```

In former projects, the CAD or the actual mesh have been accessed via their proxies:

*All CADGroup proxy*

*Actual Master*

## Measurement series and Measuring environment

The access and information about the VMR, measuring setups and measurement series  are much more separated in the part-based workflow as compared to the part-less workflow. New categories and `ElementSelection` categories were introduced. If you have further questions regarding scripting purposes, please contact the ZEISS support.

Here just the most important information follows. The measurements have their own category in the part-based workflow. A measurement can be accessed via the attribute `measurement_series` and no longer via `actual_elements`.

``` Python
MEASUREMENT = gom.app.project.measurement_series['Scan 1']
 
MEASUREMENTS = gom.ElementSelection ({'category': ['key', 'elements', 'explorer_category', 'measurements', 'object_family', 'measurement_series']})
```

## Reports

Reports did not change significantly in the part-based workflow. Reports are not assigned to a part, they show the situation of measurement series, VMR or multiple parts at the same time. Some slight changes must be taken into account: The keyword `alignment` could now return names of more than one alignment (comma separated, i.e. a Python list) due to the fact that multiple parts (if visible in the report page) with their own alignment must be respected.

## CAD structure and contents

For scripting with CADs in part-based projects, some additional information are necessary. Most importantly:

Only one CAD Group per part is supported. <!-- The same also applies to the actual content of a part - only one mesh per part is supported. -->
<!-- 
How about stages?

The following code prints the surface area of each stage:

for s in gom.app.project.stages:
	print (gom.app.project.parts['Part'].actual.in_stage[s.index].area)

According to this, the stage (i.e. a mesh) would be a sub-element of the part. Or does this have anything to do with a proxy?
-->

The *CAD Group* (in a part-based workflow) now supports the access via an internal file structure to represent structures stored in CAD files like *CATProduct*. These entities are imported in the part-less workflow as separated *CAD Groups*.

The following simple code examples show how to access bodies or files of a CAD Group.

```{caution}
This access gives you information about the bodies or files. You can use this also for the deletion of bodies. Visibility operations are suppressed by intention. Usage for construction purposes is not recommended due to the fact that exchanging CAD structures would **not** work as expected.
```

``` Python
# This example code list all bodies of all CADs for all parts

# Iterate through each element
for element in nominal_elements:
    # Check if the element is a CAD
    if element.type == "cad":
        # Print the name and type
        print(element.name, element.type)
        
        # Iterate through each body in the CAD
        for body in element.bodies:
            # Print the name of the body
            print(body.name)
```

This is an example to list files by `cat_part`:

``` Python
cad = filter (lambda c: c.type == "cad", gom.app.project.nominal_elements)
 
# for all cads in all parts list the file structure of each CAD of one part and furthermore all bodies of each file
for c in cad:
    print (c.name)
    print ('Number of files: ' + str (len (c.file)))
    for file in c.file:
        print (file)
        for b in file.bodies:
            print (' {}'.format (b.name))
```

## CAD assembly structure in the *Elements in clipboard*

These information are usually not necessary for scripting. The most important fact is that the assembly structure does not represent our CAD structure. The assembly structure shows much more internal details.

## Script compatibility

### Actual master and All CAD Group proxy

For the single part workflow old scripts using *Actual Master* and the *All CAD Group proxy* in creation commands should usually work.

```{caution}
The functionality of these proxies is no longer present in the part-based workflow. Therefore functionalities like *Define Actual Master* will not work anymore. If the scripting tries to resolve the elements for the *Actual Master* a mapping takes place and the *ActualValues-Reference* of the unique part is returned. The same happens for the *All CAD Group proxy* and the *NominalValues-Reference*.
```

### Measurement series

The script compatibility for the current measurement list is given in most cases. Normal information is usually accessible via the same attributes as before.

### Tesselate Geometrical Element

The obsolete command `gom.script.mesh.tesselate_geometrical_element` creates an element of type mesh.

In the part-based workflow this command has been replaced with the command `gom.script.primitive.tesselate_geometrical_element`, which creates elements of type surface.
