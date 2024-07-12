---
myst:
    html_meta:
        "description": "Examples for using the ZEISS INSPECT 2025 App Python API"
        "keywords": "Metrology, ZEISS INSPECT, Python API, GOM API, Scripting, Add-ons, Apps, Examples"
---
# ZEISS INSPECT App Examples Overview

## data_interfaces &mdash; How to access data of ZEISS INSPECT elements

### <a id="ReferencePointsAndMeshData">ReferencePointsAndMeshData</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/data_interfaces/ReferencePointsAndMeshData/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ReferencePointsAndMeshData)

:Description:
    This example demonstrates how to access the reference points in a measurement and the mesh from Python.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/python_api_introduction.html#element-data-interfaces)

### <a id="CheckResultsDataArray">CheckResultsDataArray</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/data_interfaces/CheckResultsDataArray/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/CheckResultsDataArray)

:Description:
    This example demonstrates two ways of accessing result data from checks using the element properties and data interfaces.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/python_api_introduction.html#access-element-properties)

### <a id="VolumeSectionImageData">VolumeSectionImageData</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/data_interfaces/VolumeSectionImageData/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/VolumeSectionImageData)

:Description:
    This example demonstrates how to access the image data of a volume section.

:Example Projects:
    [volume_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/python_api_introduction.html#element-data-interfaces)


## dialog_widgets &mdash; How to use custom dialogs and handle user input events

### <a id="WidgetVisibility">WidgetVisibility</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/dialog_widgets/WidgetVisibility/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/WidgetVisibility)

:Description:
    This example shows how to use a dialog event handler to turn on/off widget visibilities.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/user_defined_dialogs.html)

### <a id="UnitDialogEventHandler">UnitDialogEventHandler</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/dialog_widgets/UnitDialogEventHandler/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/UnitDialogEventHandler)

:Description:
    This basic example demonstrates how to use an event handler on a script dialog to set the unit to multiple widgets.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#unit-widget)

### <a id="ExplorerSelectedElementsInDialog">ExplorerSelectedElementsInDialog</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/dialog_widgets/ExplorerSelectedElementsInDialog/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ExplorerSelectedElementsInDialog)

:Description:
    This example shows how to get a list of elements selected in the element explorer and use it in a script dialog. 

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#selection-element-widget)

### <a id="DropdownWidget">DropdownWidget</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/dialog_widgets/DropdownWidget/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/DropdownWidget)

:Description:
    This basic example shows how to use the dropdown widget and how to define items at script runtime.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#selection-list-widget)


## misc &mdash; Miscellaneous

### <a id="CSVExample">CSVExample</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/misc/CSVExample/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/CSVExample)

:Description:
    This example demonstrates how to read and write CSV files (comma separated values) from an App.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

### <a id="DialogReopenExample">DialogReopenExample</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/misc/DialogReopenExample/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/DialogReopenExample)

:Description:
    This examples demonstrates, how a dialog can be closed from its own handler, just to be opened again.

:References:
    [HowTo]( https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#executing-dialogs)

### <a id="PointPixelTransformations">PointPixelTransformations</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/misc/PointPixelTransformations/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/PointPixelTransformations)

:Description:
    This example demonstrates how to find the 2D pixel coordinates of a 3D point coordinate and vice versa.

:Example Projects:
    [zeiss_part_test_measurement](#example-projects)

:References:
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/python_api.html#gom-api-imaging)


## projects &mdash; ZEISS INSPECT projects

### <a id="ExampleProjects">ExampleProjects</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/projects/ExampleProjects/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ExampleProjects)

:Description:
    ZEISS INSPECT Example Projects


## script_icons &mdash; How to set icons for scripts or buttons

### <a id="ScriptIcon">ScriptIcon</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/script_icons/ScriptIcon/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptIcon)

:Description:
    This example shows how an icon can be set to a script, whereas the icon itself resides in the App as a resource.


## script_resources &mdash; How to access binary data of your App (resources)

### <a id="ScriptResources">ScriptResources</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/script_resources/ScriptResources/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptResources)

:Description:
    A simple example showing the usage of script resources.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/using_script_resources.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/resource_api.html)


## scripted_actuals &mdash; Building custom actual elements with Python code

### <a id="ScriptedActualVolume">ScriptedActualVolume</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualVolume/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualVolume)

:Description:
    This is an example for a scripted actual ‘volume’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#volume)

:Tags:
    <a href="#xray">![Static Badge](https://img.shields.io/badge/xray-blue)</a> 
### <a id="ScriptedElementProgress">ScriptedElementProgress</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedElementProgress/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedElementProgress)

:Description:
    This examples demonstrates how to show progress information to the user while calcualting a scripted element.

### <a id="ScriptedActualCircle">ScriptedActualCircle</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualCircle/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualCircle)

:Description:
    This is an example for a scripted actual ‘circle’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#circle)

### <a id="ScriptedActualCone">ScriptedActualCone</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualCone/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualCone)

:Description:
    This is an example for a scripted actual ‘cone’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#cone)

### <a id="ScriptedActualDistance">ScriptedActualDistance</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualDistance/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualDistance)

:Description:
    This is an example for a scripted actual ‘distance’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#distance)

### <a id="ScriptedActualSection">ScriptedActualSection</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualSection/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualSection)

:Description:
    This is an example for a scripted actual ‘section’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#section)

### <a id="ScriptedActualPoint">ScriptedActualPoint</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualPoint/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualPoint)

:Description:
    These are two examples for scripted actual points, which serve as an introduction to the concept of scripted actual elements.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#point)

### <a id="ScriptedActualVolumeDefects">ScriptedActualVolumeDefects</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualVolumeDefects/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualVolumeDefects)

:Description:
    This is an example for a scripted actual ‘volume defects’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#volume-defects)

:Tags:
    <a href="#xray">![Static Badge](https://img.shields.io/badge/xray-blue)</a> 
### <a id="ScriptedActualVolumeRegion">ScriptedActualVolumeRegion</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualVolumeRegion/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualVolumeRegion)

:Description:
    This is an example for a scripted actual ‘volume region’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#volume-region)

:Tags:
    <a href="#xray">![Static Badge](https://img.shields.io/badge/xray-blue)</a> 
### <a id="ScriptedActualCurve">ScriptedActualCurve</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualCurve/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualCurve)

:Description:
    This is an example for a scripted actual ‘curve’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#curve)

### <a id="ScriptedActualSurface">ScriptedActualSurface</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualSurface/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualSurface)

:Description:
    This is an example for a scripted actual ‘surface’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#surface)

### <a id="ScriptedActualCylinder">ScriptedActualCylinder</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualCylinder/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualCylinder)

:Description:
    This is an example for a scripted actual ‘cylinder’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#cylinder)

### <a id="ScriptedActualPointCloud">ScriptedActualPointCloud</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualPointCloud/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualPointCloud)

:Description:
    This is an example for a scripted actual ‘point cloud’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#point-cloud)

### <a id="ScriptedActualVolumeSection">ScriptedActualVolumeSection</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualVolumeSection/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualVolumeSection)

:Description:
    This is an example for a scripted actual ‘volume section’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#volume-section)

:Tags:
    <a href="#xray">![Static Badge](https://img.shields.io/badge/xray-blue)</a> 
### <a id="ScriptedActualSurfaceCurve">ScriptedActualSurfaceCurve</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/ScriptedActualSurfaceCurve/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedActualSurfaceCurve)

:Description:
    This is an example for a scripted actual ‘surface curve’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#surface-curve)

### <a id="TrimeshDeformMesh">TrimeshDeformMesh</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_actuals/TrimeshDeformMesh/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/TrimeshDeformMesh)

:Description:
    This example demonstrates how to generate a custom surface element using a scripted element. The example script accesses mesh information from an existing mesh in the project and adds a random deformation to each point.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#surface)

:Tags:
    <a href="#surface">![Static Badge](https://img.shields.io/badge/surface-blue)</a> <a href="#scripted-actual">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

## scripted_checks &mdash; Building custom checks with Python code

### <a id="ScriptedSurfaceCheck">ScriptedSurfaceCheck</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_checks/ScriptedSurfaceCheck/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedSurfaceCheck)

:Description:
    This example demonstrates how to create a scalar surface check by a script. Also, the usage of custom coordinate systems and element preview in scripted checks is shown.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_checks.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#scalar-surface)

:Tags:
    <a href="#scripted-check">![Static Badge](https://img.shields.io/badge/scripted--check-blue)</a> <a href="#surface">![Static Badge](https://img.shields.io/badge/surface-blue)</a> 
### <a id="ScriptedScalarCheck">ScriptedScalarCheck</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_checks/ScriptedScalarCheck/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedScalarCheck)

:Description:
    This example shows how to create a scalar check by script. A scalar check is the most basic check, as it assigns a scalar value to an element. Nearly all elements you can find in the software can be checked like this.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_checks.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#scalar)

:Tags:
    <a href="#scripted-check">![Static Badge](https://img.shields.io/badge/scripted--check-blue)</a> <a href="#scalar">![Static Badge](https://img.shields.io/badge/scalar-blue)</a> 
### <a id="ScriptedCurveCheck">ScriptedCurveCheck</a> &mdash; [view](https://github.com/ZEISS/zeiss-inspect-app-examples/blob/dev/AppExamples/scripted_checks/ScriptedCurveCheck/doc/Documentation.md) / [download](https://software-store.zeiss.com/products/apps/ScriptedCurveCheck)

:Description:
    This example demonstrates how to create a scalar curve check by a script. Also, the usage of custom coordinate systems in scripted checks is shown.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_checks.html)
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#scalar-curve)

:Tags:
    <a href="#scripted-check">![Static Badge](https://img.shields.io/badge/scripted--check-blue)</a> <a href="#curve">![Static Badge](https://img.shields.io/badge/curve-blue)</a> 

## Example projects

* zeiss_part_test_project
* zeiss_part_test_measurement
* volume_test_project

[Download Example Projects App](https://software-store.zeiss.com/products/apps/ExampleProjects)

## Tag Index

### <a id="curve">![Static Badge](https://img.shields.io/badge/curve-blue)<a>

* <a href="#ScriptedCurveCheck">ScriptedCurveCheck</a>


### <a id="scalar">![Static Badge](https://img.shields.io/badge/scalar-blue)<a>

* <a href="#ScriptedScalarCheck">ScriptedScalarCheck</a>


### <a id="scripted-actual">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)<a>

* <a href="#TrimeshDeformMesh">TrimeshDeformMesh</a>


### <a id="scripted-check">![Static Badge](https://img.shields.io/badge/scripted--check-blue)<a>

* <a href="#ScriptedCurveCheck">ScriptedCurveCheck</a>
* <a href="#ScriptedScalarCheck">ScriptedScalarCheck</a>
* <a href="#ScriptedSurfaceCheck">ScriptedSurfaceCheck</a>


### <a id="surface">![Static Badge](https://img.shields.io/badge/surface-blue)<a>

* <a href="#ScriptedSurfaceCheck">ScriptedSurfaceCheck</a>
* <a href="#TrimeshDeformMesh">TrimeshDeformMesh</a>


### <a id="xray">![Static Badge](https://img.shields.io/badge/xray-blue)<a>

* <a href="#ScriptedActualVolume">ScriptedActualVolume</a>
* <a href="#ScriptedActualVolumeDefects">ScriptedActualVolumeDefects</a>
* <a href="#ScriptedActualVolumeRegion">ScriptedActualVolumeRegion</a>
* <a href="#ScriptedActualVolumeSection">ScriptedActualVolumeSection</a>


## Related

* [ZEISS IQS GitHub &mdash; App Development Documentation](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/index.html)
* [ZEISS Quality Software Store](https://software-store.zeiss.com)
