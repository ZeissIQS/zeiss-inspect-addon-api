---
myst:
    html_meta:
        "description": "Examples for using the ZEISS INSPECT 2025 App Python API"
        "keywords": "Metrology, ZEISS INSPECT, Python API, GOM API, Scripting, Add-ons, Apps, Examples"
---

<style>
    .example-block-odd {
        background-color: #f3f6f6;
        padding: 10px;
    }
    .example-block-even {
        background-color: #ffffff;
        padding: 10px;
    }
    h2 {
        margin-top: 24px;
        margin-bottom: 4px;
    }
    .rst-content h2 {
        margin-bottom: 4px;
    }
    .small-margin {
        margin-top: 4px;
    }
</style>
# ZEISS INSPECT App Examples Overview

## data_interfaces &mdash; How to access data of ZEISS INSPECT elements

<hr class="small-margin">
<section id="checkresultsdataarray">
<div id="checkresultsdataarray" class="example-block-odd">
<h3>CheckResultsDataArray — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/data_interfaces/CheckResultsDataArray/doc/Documentation.md">view</a>  
<a class="headerlink" href="#checkresultsdataarray" title="Link to this heading"></a></h3>


:Description:
    This example demonstrates two ways of accessing result data from checks using the element properties and data interfaces.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/python_api_introduction.html#access-element-properties)
:Tags:
    <a href="#id10">![Static Badge](https://img.shields.io/badge/element--properties-blue)</a> <a href="#id9">![Static Badge](https://img.shields.io/badge/element--data-blue)</a> 

</div>

</section>

<section id="referencepointsandmeshdata">
<div id="referencepointsandmeshdata" class="example-block-even">
<h3>ReferencePointsAndMeshData — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/data_interfaces/ReferencePointsAndMeshData/doc/Documentation.md">view</a>  
<a class="headerlink" href="#referencepointsandmeshdata" title="Link to this heading"></a></h3>


:Description:
    This example demonstrates how to access the reference points in a measurement and the mesh from Python.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/python_api_introduction.html#element-data-interfaces)
:Tags:
    <a href="#id24">![Static Badge](https://img.shields.io/badge/reference--points-blue)</a> <a href="#id18">![Static Badge](https://img.shields.io/badge/mesh-blue)</a> <a href="#id16">![Static Badge](https://img.shields.io/badge/measurement-blue)</a> 

</div>

</section>

<section id="volumesectionimagedata">
<div id="volumesectionimagedata" class="example-block-odd">
<h3>VolumeSectionImageData — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/data_interfaces/VolumeSectionImageData/doc/Documentation.md">view</a>  
<a class="headerlink" href="#volumesectionimagedata" title="Link to this heading"></a></h3>


:Description:
    This example demonstrates how to access the image data of a volume section.

:Example Projects:
    [volume_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/python_api_introduction.html#element-data-interfaces)
:Tags:
    <a href="#id9">![Static Badge](https://img.shields.io/badge/element--data-blue)</a> 

</div>

</section>


## dialog_widgets &mdash; How to use custom dialogs and handle user input events

<hr class="small-margin">
<section id="dropdownwidget">
<div id="dropdownwidget" class="example-block-odd">
<h3>DropdownWidget — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/dialog_widgets/DropdownWidget/doc/Documentation.md">view</a>  
<a class="headerlink" href="#dropdownwidget" title="Link to this heading"></a></h3>


:Description:
    This basic example shows how to use the dropdown widget and how to define items at script runtime.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#selection-list-widget)
:Tags:
    <a href="#id6">![Static Badge](https://img.shields.io/badge/dialog-blue)</a> <a href="#id32">![Static Badge](https://img.shields.io/badge/selection--list--widget-blue)</a> 

</div>

</section>

<section id="explorerselectedelementsindialog">
<div id="explorerselectedelementsindialog" class="example-block-even">
<h3>ExplorerSelectedElementsInDialog — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/dialog_widgets/ExplorerSelectedElementsInDialog/doc/Documentation.md">view</a>  
<a class="headerlink" href="#explorerselectedelementsindialog" title="Link to this heading"></a></h3>


:Description:
    This example shows how to get a list of elements selected in the element explorer and use it in a script dialog. 

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#selection-element-widget)
:Tags:
    <a href="#id6">![Static Badge](https://img.shields.io/badge/dialog-blue)</a> <a href="#id31">![Static Badge](https://img.shields.io/badge/selection--element--widget-blue)</a> 

</div>

</section>

<section id="unitdialogeventhandler">
<div id="unitdialogeventhandler" class="example-block-odd">
<h3>UnitDialogEventHandler — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/dialog_widgets/UnitDialogEventHandler/doc/Documentation.md">view</a>  
<a class="headerlink" href="#unitdialogeventhandler" title="Link to this heading"></a></h3>


:Description:
    This basic example demonstrates how to use an event handler on a script dialog to set the unit to multiple widgets.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#unit-widget)
:Tags:
    <a href="#id6">![Static Badge](https://img.shields.io/badge/dialog-blue)</a> <a href="#id39">![Static Badge](https://img.shields.io/badge/unit--widget-blue)</a> 

</div>

</section>

<section id="widgetvisibility">
<div id="widgetvisibility" class="example-block-even">
<h3>WidgetVisibility — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/dialog_widgets/WidgetVisibility/doc/Documentation.md">view</a>  
<a class="headerlink" href="#widgetvisibility" title="Link to this heading"></a></h3>


:Description:
    This example shows how to use a dialog event handler to turn on/off widget visibilities.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/user_defined_dialogs.html)
:Tags:
    <a href="#id6">![Static Badge](https://img.shields.io/badge/dialog-blue)</a> <a href="#id44">![Static Badge](https://img.shields.io/badge/widget--properties-blue)</a> 

</div>

</section>


## misc &mdash; Miscellaneous

<hr class="small-margin">
<section id="csvexample">
<div id="csvexample" class="example-block-odd">
<h3>CSVExample — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/CSVExample/doc/Documentation.md">view</a>  
<a class="headerlink" href="#csvexample" title="Link to this heading"></a></h3>


:Description:
    This example demonstrates how to read and write CSV files (comma separated values) from an App.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:Tags:
    <a href="#id15">![Static Badge](https://img.shields.io/badge/import-blue)</a> <a href="#id11">![Static Badge](https://img.shields.io/badge/export-blue)</a> <a href="#id23">![Static Badge](https://img.shields.io/badge/project--keywords-blue)</a> 

</div>

</section>

<section id="dialogreopenexample">
<div id="dialogreopenexample" class="example-block-even">
<h3>DialogReopenExample — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/DialogReopenExample/doc/Documentation.md">view</a>  
<a class="headerlink" href="#dialogreopenexample" title="Link to this heading"></a></h3>


:Description:
    This examples demonstrates, how a dialog can be closed from its own handler, just to be opened again.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/user_defined_dialogs.html#executing-dialogs)
:Tags:
    <a href="#id6">![Static Badge](https://img.shields.io/badge/dialog-blue)</a> 

</div>

</section>

<section id="displayimage">
<div id="displayimage" class="example-block-odd">
<h3>DisplayImage — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/DisplayImage/doc/Documentation.md">view</a>  
<a class="headerlink" href="#displayimage" title="Link to this heading"></a></h3>


:Description:
    Display measurement as a single image

:Tags:
    <a href="#id14">![Static Badge](https://img.shields.io/badge/image--widget-blue)</a> <a href="#id16">![Static Badge](https://img.shields.io/badge/measurement-blue)</a> 

</div>

</section>

<section id="excelexample">
<div id="excelexample" class="example-block-even">
<h3>ExcelExample — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/ExcelExample/doc/Documentation.md">view</a>  
<a class="headerlink" href="#excelexample" title="Link to this heading"></a></h3>


:Description:
    Example for reading and writing Excel files from an App

:Tags:
    <a href="#id15">![Static Badge](https://img.shields.io/badge/import-blue)</a> <a href="#id11">![Static Badge](https://img.shields.io/badge/export-blue)</a> <a href="#id23">![Static Badge](https://img.shields.io/badge/project--keywords-blue)</a> 

</div>

</section>

<section id="fileselectionandfiltering">
<div id="fileselectionandfiltering" class="example-block-odd">
<h3>FileSelectionAndFiltering — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/FileSelectionAndFiltering/doc/Documentation.md">view</a>  
<a class="headerlink" href="#fileselectionandfiltering" title="Link to this heading"></a></h3>


:Description:
    File Selection and Filtering Examples

:Tags:
    <a href="#id12">![Static Badge](https://img.shields.io/badge/file-blue)</a> <a href="#id7">![Static Badge](https://img.shields.io/badge/directory-blue)</a> <a href="#id13">![Static Badge](https://img.shields.io/badge/folder-blue)</a> <a href="#id19">![Static Badge](https://img.shields.io/badge/path-blue)</a> 

</div>

</section>

<section id="ipcsocketsexample">
<div id="ipcsocketsexample" class="example-block-even">
<h3>IPCSocketsExample — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/IPCSocketsExample/doc/Documentation.md">view</a>  
<a class="headerlink" href="#ipcsocketsexample" title="Link to this heading"></a></h3>


:Description:
    Example for triggering command execution via Internet (aka BSD) sockets

:Tags:
    <a href="#id15">![Static Badge](https://img.shields.io/badge/import-blue)</a> 

</div>

</section>

<section id="measurementsystemanalysis">
<div id="measurementsystemanalysis" class="example-block-odd">
<h3>MeasurementSystemAnalysis — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/MeasurementSystemAnalysis/doc/Documentation.md">view</a>  
<a class="headerlink" href="#measurementsystemanalysis" title="Link to this heading"></a></h3>


:Description:
    MSA conformal measurement system analysis (ANOVA, ARM)

:Tags:
    <a href="#id16">![Static Badge](https://img.shields.io/badge/measurement-blue)</a> 

</div>

</section>

<section id="pointpixeltransformations">
<div id="pointpixeltransformations" class="example-block-even">
<h3>PointPixelTransformations — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/PointPixelTransformations/doc/Documentation.md">view</a>  
<a class="headerlink" href="#pointpixeltransformations" title="Link to this heading"></a></h3>


:Description:
    This example demonstrates how to find the 2D pixel coordinates of a 3D point coordinate and vice versa.

:Example Projects:
    [zeiss_part_test_measurement](#example-projects)

:References:
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/python_api.html#gom-api-imaging)
:Tags:
    <a href="#id16">![Static Badge](https://img.shields.io/badge/measurement-blue)</a> <a href="#id24">![Static Badge](https://img.shields.io/badge/reference--points-blue)</a> 

</div>

</section>

<section id="progressbar">
<div id="progressbar" class="example-block-odd">
<h3>ProgressBar — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/ProgressBar/doc/Documentation.md">view</a>  
<a class="headerlink" href="#progressbar" title="Link to this heading"></a></h3>


:Description:
    This example shows how to display a progress bar at the bottom of the ZEISS INSPECT main window


</div>

</section>

<section id="sqlexample">
<div id="sqlexample" class="example-block-even">
<h3>SQLExample — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/SQLExample/doc/Documentation.md">view</a>  
<a class="headerlink" href="#sqlexample" title="Link to this heading"></a></h3>


:Description:
    Example for SQL Database Access

:Tags:
    <a href="#id35">![Static Badge](https://img.shields.io/badge/sql--database-blue)</a> <a href="#id23">![Static Badge](https://img.shields.io/badge/project--keywords-blue)</a> 

</div>

</section>

<section id="serviceexample">
<div id="serviceexample" class="example-block-odd">
<h3>ServiceExample — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/ServiceExample/doc/Documentation.md">view</a>  
<a class="headerlink" href="#serviceexample" title="Link to this heading"></a></h3>


:Description:
    Service API Example

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/using_services/using_services.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/python_api.html#gom-api-services)
:Tags:
    <a href="#id33">![Static Badge](https://img.shields.io/badge/service-blue)</a> 

</div>

</section>

<section id="settingsapi">
<div id="settingsapi" class="example-block-even">
<h3>SettingsAPI — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/SettingsAPI/doc/Documentation.md">view</a>  
<a class="headerlink" href="#settingsapi" title="Link to this heading"></a></h3>


:Description:
    Example App demonstrating usage of the settings API

:References:
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/python_api.html#gom-api-settings)
:Tags:
    <a href="#id34">![Static Badge](https://img.shields.io/badge/settings-blue)</a> 

</div>

</section>

<section id="templateunittestcoverage">
<div id="templateunittestcoverage" class="example-block-odd">
<h3>TemplateUnittestCoverage — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/TemplateUnittestCoverage/doc/Documentation.md">view</a>  
<a class="headerlink" href="#templateunittestcoverage" title="Link to this heading"></a></h3>


:Description:
    App template for running unit testing and generating a test coverage report

:Tags:
    <a href="#id38">![Static Badge](https://img.shields.io/badge/testing-blue)</a> 

</div>

</section>

<section id="textdetection">
<div id="textdetection" class="example-block-even">
<h3>TextDetection — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/misc/TextDetection/doc/Documentation.md">view</a>  
<a class="headerlink" href="#textdetection" title="Link to this heading"></a></h3>


:Description:
    Text detection example

:Tags:
    <a href="#id16">![Static Badge](https://img.shields.io/badge/measurement-blue)</a> <a href="#id14">![Static Badge](https://img.shields.io/badge/image--widget-blue)</a> 

</div>

</section>


## projects &mdash; ZEISS INSPECT projects

<hr class="small-margin">
<section id="exampleprojects">
<div id="exampleprojects" class="example-block-odd">
<h3>ExampleProjects — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/projects/ExampleProjects/doc/Documentation.md">view</a>  
<a class="headerlink" href="#exampleprojects" title="Link to this heading"></a></h3>


:Description:
    ZEISS INSPECT Example Projects

:Tags:
    <a href="#id22">![Static Badge](https://img.shields.io/badge/project-blue)</a> 

</div>

</section>


## script_icons &mdash; How to set icons for scripts or buttons

<hr class="small-margin">
<section id="scripticon">
<div id="scripticon" class="example-block-odd">
<h3>ScriptIcon — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/script_icons/ScriptIcon/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scripticon" title="Link to this heading"></a></h3>


:Description:
    This example shows how an icon can be set to a script, whereas the icon itself resides in the App as a resource.

:Tags:
    <a href="#id17">![Static Badge](https://img.shields.io/badge/menu-blue)</a> 

</div>

</section>


## script_resources &mdash; How to access binary data of your App (resources)

<hr class="small-margin">
<section id="resourceaccess">
<div id="resourceaccess" class="example-block-odd">
<h3>ResourceAccess — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/script_resources/ResourceAccess/doc/Documentation.md">view</a> / 
<a class="reference external" href="https://software-store.zeiss.com/products/apps/ResourceAccess">download</a>
<a class="headerlink" href="#resourceaccess" title="Link to this heading"></a></h3>
<section id="resourceaccess">
<div id="resourceaccess" class="example-block-odd">
<h3>ResourceAccess — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/script_resources/ResourceAccess/doc/Documentation.md">view</a> / 
<a class="reference external" href="https://software-store.zeiss.com/products/apps/ResourceAccess">download</a>
<a class="headerlink" href="#resourceaccess" title="Link to this heading"></a></h3>


:Description:
    Accessing an image as an App based resources

:References:
    [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/resource_api.html)
:Tags:
    <a href="#id25">![Static Badge](https://img.shields.io/badge/resources-blue)</a> <a href="#id14">![Static Badge](https://img.shields.io/badge/image--widget-blue)</a> 

</div>

</section>

<section id="scriptresources">
<div id="scriptresources" class="example-block-even">
<h3>ScriptResources — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/script_resources/ScriptResources/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptresources" title="Link to this heading"></a></h3>


:Description:
    A simple example showing the usage of script resources.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/python_api_introduction/using_script_resources.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/resource_api.html)
:Tags:
    <a href="#id25">![Static Badge](https://img.shields.io/badge/resources-blue)</a> 

</div>

</section>


## scripted_actuals &mdash; Building custom actual elements with Python code

<hr class="small-margin">
<section id="scriptedactualcircle">
<div id="scriptedactualcircle" class="example-block-odd">
<h3>ScriptedActualCircle — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualCircle/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualcircle" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘circle’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#circle)
:Tags:
    <a href="#id1">![Static Badge](https://img.shields.io/badge/circle-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualcone">
<div id="scriptedactualcone" class="example-block-even">
<h3>ScriptedActualCone — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualCone/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualcone" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘cone’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#cone)
:Tags:
    <a href="#id3">![Static Badge](https://img.shields.io/badge/cone-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualcurve">
<div id="scriptedactualcurve" class="example-block-odd">
<h3>ScriptedActualCurve — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualCurve/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualcurve" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘curve’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#curve)
:Tags:
    <a href="#id4">![Static Badge](https://img.shields.io/badge/curve-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualcylinder">
<div id="scriptedactualcylinder" class="example-block-even">
<h3>ScriptedActualCylinder — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualCylinder/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualcylinder" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘cylinder’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#cylinder)
:Tags:
    <a href="#id5">![Static Badge](https://img.shields.io/badge/cylinder-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualdistance">
<div id="scriptedactualdistance" class="example-block-odd">
<h3>ScriptedActualDistance — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualDistance/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualdistance" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘distance’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#distance)
:Tags:
    <a href="#id8">![Static Badge](https://img.shields.io/badge/distance-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualpoint">
<div id="scriptedactualpoint" class="example-block-even">
<h3>ScriptedActualPoint — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualPoint/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualpoint" title="Link to this heading"></a></h3>


:Description:
    These are two examples for scripted actual points, which serve as an introduction to the concept of scripted actual elements.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#point)
:Tags:
    <a href="#id20">![Static Badge](https://img.shields.io/badge/point-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualpointcloud">
<div id="scriptedactualpointcloud" class="example-block-odd">
<h3>ScriptedActualPointCloud — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualPointCloud/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualpointcloud" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘point cloud’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#point-cloud)
:Tags:
    <a href="#id21">![Static Badge](https://img.shields.io/badge/point--cloud-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualsection">
<div id="scriptedactualsection" class="example-block-even">
<h3>ScriptedActualSection — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualSection/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualsection" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘section’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#section)
:Tags:
    <a href="#id30">![Static Badge](https://img.shields.io/badge/section-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualsurface">
<div id="scriptedactualsurface" class="example-block-odd">
<h3>ScriptedActualSurface — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualSurface/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualsurface" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘surface’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#surface)
:Tags:
    <a href="#id36">![Static Badge](https://img.shields.io/badge/surface-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualsurfacecurve">
<div id="scriptedactualsurfacecurve" class="example-block-even">
<h3>ScriptedActualSurfaceCurve — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualSurfaceCurve/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualsurfacecurve" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘surface curve’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#surface-curve)
:Tags:
    <a href="#id37">![Static Badge](https://img.shields.io/badge/surface--curve-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualvolume">
<div id="scriptedactualvolume" class="example-block-odd">
<h3>ScriptedActualVolume — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualVolume/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualvolume" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘volume’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#volume)
:Tags:
    <a href="#id45">![Static Badge](https://img.shields.io/badge/xray-blue)</a> <a href="#id40">![Static Badge](https://img.shields.io/badge/volume-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualvolumedefects">
<div id="scriptedactualvolumedefects" class="example-block-even">
<h3>ScriptedActualVolumeDefects — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualVolumeDefects/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualvolumedefects" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘volume defects’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#volume-defects)
:Tags:
    <a href="#id45">![Static Badge](https://img.shields.io/badge/xray-blue)</a> <a href="#id41">![Static Badge](https://img.shields.io/badge/volume--defects-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualvolumeregion">
<div id="scriptedactualvolumeregion" class="example-block-odd">
<h3>ScriptedActualVolumeRegion — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualVolumeRegion/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualvolumeregion" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘volume region’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#volume-region)
:Tags:
    <a href="#id45">![Static Badge](https://img.shields.io/badge/xray-blue)</a> <a href="#id42">![Static Badge](https://img.shields.io/badge/volume--region-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedactualvolumesection">
<div id="scriptedactualvolumesection" class="example-block-even">
<h3>ScriptedActualVolumeSection — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedActualVolumeSection/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedactualvolumesection" title="Link to this heading"></a></h3>


:Description:
    This is an example for a scripted actual ‘volume section’ element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#volume-section)
:Tags:
    <a href="#id45">![Static Badge](https://img.shields.io/badge/xray-blue)</a> <a href="#id43">![Static Badge](https://img.shields.io/badge/volume--section-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>

<section id="scriptedelementprogress">
<div id="scriptedelementprogress" class="example-block-odd">
<h3>ScriptedElementProgress — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/ScriptedElementProgress/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedelementprogress" title="Link to this heading"></a></h3>


:Description:
    This examples demonstrates how to show progress information to the user while calcualting a scripted element.

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html)
:Tags:
    <a href="#id2">![Static Badge](https://img.shields.io/badge/computation--progress-blue)</a> 

</div>

</section>

<section id="trimeshdeformmesh">
<div id="trimeshdeformmesh" class="example-block-even">
<h3>TrimeshDeformMesh — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_actuals/TrimeshDeformMesh/doc/Documentation.md">view</a>  
<a class="headerlink" href="#trimeshdeformmesh" title="Link to this heading"></a></h3>


:Description:
    This example demonstrates how to generate a custom surface element using a scripted element. The example script accesses mesh information from an existing mesh in the project and adds a random deformation to each point.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_actuals.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#surface)
:Tags:
    <a href="#id18">![Static Badge](https://img.shields.io/badge/mesh-blue)</a> <a href="#id36">![Static Badge](https://img.shields.io/badge/surface-blue)</a> <a href="#id27">![Static Badge](https://img.shields.io/badge/scripted--actual-blue)</a> 

</div>

</section>


## scripted_checks &mdash; Building custom checks with Python code

<hr class="small-margin">
<section id="scriptedcurvecheck">
<div id="scriptedcurvecheck" class="example-block-odd">
<h3>ScriptedCurveCheck — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_checks/ScriptedCurveCheck/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedcurvecheck" title="Link to this heading"></a></h3>


:Description:
    This example demonstrates how to create a scalar curve check by a script. Also, the usage of custom coordinate systems in scripted checks is shown.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_checks.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#scalar-curve)
:Tags:
    <a href="#id28">![Static Badge](https://img.shields.io/badge/scripted--check-blue)</a> <a href="#id4">![Static Badge](https://img.shields.io/badge/curve-blue)</a> 

</div>

</section>

<section id="scriptedscalarcheck">
<div id="scriptedscalarcheck" class="example-block-even">
<h3>ScriptedScalarCheck — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_checks/ScriptedScalarCheck/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedscalarcheck" title="Link to this heading"></a></h3>


:Description:
    This example shows how to create a scalar check by script. A scalar check is the most basic check, as it assigns a scalar value to an element. Nearly all elements you can find in the software can be checked like this.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_checks.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#scalar)
:Tags:
    <a href="#id28">![Static Badge](https://img.shields.io/badge/scripted--check-blue)</a> <a href="#id26">![Static Badge](https://img.shields.io/badge/scalar-blue)</a> 

</div>

</section>

<section id="scriptedsurfacecheck">
<div id="scriptedsurfacecheck" class="example-block-odd">
<h3>ScriptedSurfaceCheck — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_checks/ScriptedSurfaceCheck/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scriptedsurfacecheck" title="Link to this heading"></a></h3>


:Description:
    This example demonstrates how to create a scalar surface check by a script. Also, the usage of custom coordinate systems and element preview in scripted checks is shown.

:Example Projects:
    [zeiss_part_test_project](#example-projects)

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/scripted_elements/scripted_checks.html), [API](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/python_api/scripted_elements_api.html#scalar-surface)
:Tags:
    <a href="#id28">![Static Badge](https://img.shields.io/badge/scripted--check-blue)</a> <a href="#id36">![Static Badge](https://img.shields.io/badge/surface-blue)</a> 

</div>

</section>


## scripted_diagrams &mdash; Creating custom diagrams

<hr class="small-margin">
<section id="osmmapdiagram">
<div id="osmmapdiagram" class="example-block-odd">
<h3>OSMMapDiagram — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_diagrams/OSMMapDiagram/doc/Documentation.md">view</a>  
<a class="headerlink" href="#osmmapdiagram" title="Link to this heading"></a></h3>


:Description:
    Display geolocation using a scripted diagram

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/using_scripted_diagrams/using_scripted_diagrams.html)
:Tags:
    <a href="#id34">![Static Badge](https://img.shields.io/badge/settings-blue)</a> <a href="#id29">![Static Badge](https://img.shields.io/badge/scripted--diagrams-blue)</a> 

</div>

</section>

<section id="scripteddiagrambasics">
<div id="scripteddiagrambasics" class="example-block-even">
<h3>ScriptedDiagramBasics — <a class="reference external" href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/scripted_diagrams/ScriptedDiagramBasics/doc/Documentation.md">view</a>  
<a class="headerlink" href="#scripteddiagrambasics" title="Link to this heading"></a></h3>


:Description:
    Scripted diagram basics

:References:
    [HowTo](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/howtos/using_scripted_diagrams/using_scripted_diagrams.html)
:Tags:
    <a href="#id34">![Static Badge](https://img.shields.io/badge/settings-blue)</a> <a href="#id29">![Static Badge](https://img.shields.io/badge/scripted--diagrams-blue)</a> 

</div>

</section>


## Example projects

| Project name | Description |
| ------------ | ----------- |
| zeiss_part_test_project | Simple optically measured part with a CAD, mesh and some basic inspections |
| zeiss_part_test_measurement | Optical measurement series and preliminary mesh of ZEISS part |
| volume_test_project | A small test volume for CT related inspections |

[Download Example Projects App](https://software-store.zeiss.com/products/apps/ExampleProjects)

## Tag Index

### <a name="circle"></a>![Static Badge](https://img.shields.io/badge/circle-blue)

* <a href="#scriptedactualcircle">ScriptedActualCircle</a>


### <a name="computation-progress"></a>![Static Badge](https://img.shields.io/badge/computation--progress-blue)

* <a href="#scriptedelementprogress">ScriptedElementProgress</a>


### <a name="cone"></a>![Static Badge](https://img.shields.io/badge/cone-blue)

* <a href="#scriptedactualcone">ScriptedActualCone</a>


### <a name="curve"></a>![Static Badge](https://img.shields.io/badge/curve-blue)

* <a href="#scriptedactualcurve">ScriptedActualCurve</a>
* <a href="#scriptedcurvecheck">ScriptedCurveCheck</a>


### <a name="cylinder"></a>![Static Badge](https://img.shields.io/badge/cylinder-blue)

* <a href="#scriptedactualcylinder">ScriptedActualCylinder</a>


### <a name="dialog"></a>![Static Badge](https://img.shields.io/badge/dialog-blue)

* <a href="#dialogreopenexample">DialogReopenExample</a>
* <a href="#dropdownwidget">DropdownWidget</a>
* <a href="#explorerselectedelementsindialog">ExplorerSelectedElementsInDialog</a>
* <a href="#unitdialogeventhandler">UnitDialogEventHandler</a>
* <a href="#widgetvisibility">WidgetVisibility</a>


### <a name="directory"></a>![Static Badge](https://img.shields.io/badge/directory-blue)

* <a href="#fileselectionandfiltering">FileSelectionAndFiltering</a>


### <a name="distance"></a>![Static Badge](https://img.shields.io/badge/distance-blue)

* <a href="#scriptedactualdistance">ScriptedActualDistance</a>


### <a name="element-data"></a>![Static Badge](https://img.shields.io/badge/element--data-blue)

* <a href="#checkresultsdataarray">CheckResultsDataArray</a>
* <a href="#volumesectionimagedata">VolumeSectionImageData</a>


### <a name="element-properties"></a>![Static Badge](https://img.shields.io/badge/element--properties-blue)

* <a href="#checkresultsdataarray">CheckResultsDataArray</a>


### <a name="export"></a>![Static Badge](https://img.shields.io/badge/export-blue)

* <a href="#csvexample">CSVExample</a>
* <a href="#excelexample">ExcelExample</a>


### <a name="file"></a>![Static Badge](https://img.shields.io/badge/file-blue)

* <a href="#fileselectionandfiltering">FileSelectionAndFiltering</a>


### <a name="folder"></a>![Static Badge](https://img.shields.io/badge/folder-blue)

* <a href="#fileselectionandfiltering">FileSelectionAndFiltering</a>


### <a name="image-widget"></a>![Static Badge](https://img.shields.io/badge/image--widget-blue)

* <a href="#displayimage">DisplayImage</a>
* <a href="#resourceaccess">ResourceAccess</a>
* <a href="#textdetection">TextDetection</a>


### <a name="import"></a>![Static Badge](https://img.shields.io/badge/import-blue)

* <a href="#csvexample">CSVExample</a>
* <a href="#excelexample">ExcelExample</a>
* <a href="#ipcsocketsexample">IPCSocketsExample</a>


### <a name="measurement"></a>![Static Badge](https://img.shields.io/badge/measurement-blue)

* <a href="#displayimage">DisplayImage</a>
* <a href="#measurementsystemanalysis">MeasurementSystemAnalysis</a>
* <a href="#pointpixeltransformations">PointPixelTransformations</a>
* <a href="#referencepointsandmeshdata">ReferencePointsAndMeshData</a>
* <a href="#textdetection">TextDetection</a>


### <a name="menu"></a>![Static Badge](https://img.shields.io/badge/menu-blue)

* <a href="#scripticon">ScriptIcon</a>


### <a name="mesh"></a>![Static Badge](https://img.shields.io/badge/mesh-blue)

* <a href="#referencepointsandmeshdata">ReferencePointsAndMeshData</a>
* <a href="#trimeshdeformmesh">TrimeshDeformMesh</a>


### <a name="path"></a>![Static Badge](https://img.shields.io/badge/path-blue)

* <a href="#fileselectionandfiltering">FileSelectionAndFiltering</a>


### <a name="point"></a>![Static Badge](https://img.shields.io/badge/point-blue)

* <a href="#scriptedactualpoint">ScriptedActualPoint</a>


### <a name="point-cloud"></a>![Static Badge](https://img.shields.io/badge/point--cloud-blue)

* <a href="#scriptedactualpointcloud">ScriptedActualPointCloud</a>


### <a name="project"></a>![Static Badge](https://img.shields.io/badge/project-blue)

* <a href="#exampleprojects">ExampleProjects</a>


### <a name="project-keywords"></a>![Static Badge](https://img.shields.io/badge/project--keywords-blue)

* <a href="#csvexample">CSVExample</a>
* <a href="#excelexample">ExcelExample</a>
* <a href="#sqlexample">SQLExample</a>


### <a name="reference-points"></a>![Static Badge](https://img.shields.io/badge/reference--points-blue)

* <a href="#pointpixeltransformations">PointPixelTransformations</a>
* <a href="#referencepointsandmeshdata">ReferencePointsAndMeshData</a>


### <a name="resources"></a>![Static Badge](https://img.shields.io/badge/resources-blue)

* <a href="#resourceaccess">ResourceAccess</a>
* <a href="#scriptresources">ScriptResources</a>


### <a name="scalar"></a>![Static Badge](https://img.shields.io/badge/scalar-blue)

* <a href="#scriptedscalarcheck">ScriptedScalarCheck</a>


### <a name="scripted-actual"></a>![Static Badge](https://img.shields.io/badge/scripted--actual-blue)

* <a href="#scriptedactualcircle">ScriptedActualCircle</a>
* <a href="#scriptedactualcone">ScriptedActualCone</a>
* <a href="#scriptedactualcurve">ScriptedActualCurve</a>
* <a href="#scriptedactualcylinder">ScriptedActualCylinder</a>
* <a href="#scriptedactualdistance">ScriptedActualDistance</a>
* <a href="#scriptedactualpoint">ScriptedActualPoint</a>
* <a href="#scriptedactualpointcloud">ScriptedActualPointCloud</a>
* <a href="#scriptedactualsection">ScriptedActualSection</a>
* <a href="#scriptedactualsurface">ScriptedActualSurface</a>
* <a href="#scriptedactualsurfacecurve">ScriptedActualSurfaceCurve</a>
* <a href="#scriptedactualvolume">ScriptedActualVolume</a>
* <a href="#scriptedactualvolumedefects">ScriptedActualVolumeDefects</a>
* <a href="#scriptedactualvolumeregion">ScriptedActualVolumeRegion</a>
* <a href="#scriptedactualvolumesection">ScriptedActualVolumeSection</a>
* <a href="#trimeshdeformmesh">TrimeshDeformMesh</a>


### <a name="scripted-check"></a>![Static Badge](https://img.shields.io/badge/scripted--check-blue)

* <a href="#scriptedcurvecheck">ScriptedCurveCheck</a>
* <a href="#scriptedscalarcheck">ScriptedScalarCheck</a>
* <a href="#scriptedsurfacecheck">ScriptedSurfaceCheck</a>


### <a name="scripted-diagrams"></a>![Static Badge](https://img.shields.io/badge/scripted--diagrams-blue)

* <a href="#osmmapdiagram">OSMMapDiagram</a>
* <a href="#scripteddiagrambasics">ScriptedDiagramBasics</a>


### <a name="section"></a>![Static Badge](https://img.shields.io/badge/section-blue)

* <a href="#scriptedactualsection">ScriptedActualSection</a>


### <a name="selection-element-widget"></a>![Static Badge](https://img.shields.io/badge/selection--element--widget-blue)

* <a href="#explorerselectedelementsindialog">ExplorerSelectedElementsInDialog</a>


### <a name="selection-list-widget"></a>![Static Badge](https://img.shields.io/badge/selection--list--widget-blue)

* <a href="#dropdownwidget">DropdownWidget</a>


### <a name="service"></a>![Static Badge](https://img.shields.io/badge/service-blue)

* <a href="#serviceexample">ServiceExample</a>


### <a name="settings"></a>![Static Badge](https://img.shields.io/badge/settings-blue)

* <a href="#osmmapdiagram">OSMMapDiagram</a>
* <a href="#scripteddiagrambasics">ScriptedDiagramBasics</a>
* <a href="#settingsapi">SettingsAPI</a>


### <a name="sql-database"></a>![Static Badge](https://img.shields.io/badge/sql--database-blue)

* <a href="#sqlexample">SQLExample</a>


### <a name="surface"></a>![Static Badge](https://img.shields.io/badge/surface-blue)

* <a href="#scriptedactualsurface">ScriptedActualSurface</a>
* <a href="#scriptedsurfacecheck">ScriptedSurfaceCheck</a>
* <a href="#trimeshdeformmesh">TrimeshDeformMesh</a>


### <a name="surface-curve"></a>![Static Badge](https://img.shields.io/badge/surface--curve-blue)

* <a href="#scriptedactualsurfacecurve">ScriptedActualSurfaceCurve</a>


### <a name="testing"></a>![Static Badge](https://img.shields.io/badge/testing-blue)

* <a href="#templateunittestcoverage">TemplateUnittestCoverage</a>


### <a name="unit-widget"></a>![Static Badge](https://img.shields.io/badge/unit--widget-blue)

* <a href="#unitdialogeventhandler">UnitDialogEventHandler</a>


### <a name="volume"></a>![Static Badge](https://img.shields.io/badge/volume-blue)

* <a href="#scriptedactualvolume">ScriptedActualVolume</a>


### <a name="volume-defects"></a>![Static Badge](https://img.shields.io/badge/volume--defects-blue)

* <a href="#scriptedactualvolumedefects">ScriptedActualVolumeDefects</a>


### <a name="volume-region"></a>![Static Badge](https://img.shields.io/badge/volume--region-blue)

* <a href="#scriptedactualvolumeregion">ScriptedActualVolumeRegion</a>


### <a name="volume-section"></a>![Static Badge](https://img.shields.io/badge/volume--section-blue)

* <a href="#scriptedactualvolumesection">ScriptedActualVolumeSection</a>


### <a name="widget-properties"></a>![Static Badge](https://img.shields.io/badge/widget--properties-blue)

* <a href="#widgetvisibility">WidgetVisibility</a>


### <a name="xray"></a>![Static Badge](https://img.shields.io/badge/xray-blue)

* <a href="#scriptedactualvolume">ScriptedActualVolume</a>
* <a href="#scriptedactualvolumedefects">ScriptedActualVolumeDefects</a>
* <a href="#scriptedactualvolumeregion">ScriptedActualVolumeRegion</a>
* <a href="#scriptedactualvolumesection">ScriptedActualVolumeSection</a>


## Related

* [ZEISS IQS GitHub &mdash; App Development Documentation](https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/index.html)
* [ZEISS Quality Software Store](https://software-store.zeiss.com)

