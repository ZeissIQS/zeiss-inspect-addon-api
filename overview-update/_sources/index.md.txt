---
myst:
   html_meta:
      "description": "ZEISS INSPECT 2025 App Python API Documentation"
      "keywords": "Metrology, ZEISS INSPECT, Python API, GOM API, Scripting, Add-ons, Apps, How-tos, Examples, Specification, Documentation"
--- 

# ZEISS INSPECT 2025 App Development Documentation 

Welcome to the ZEISS INSPECT 2025 App development documentation. With Apps, you will be able to customize and extend the functionality of your ZEISS INSPECT software. 
You can include several template configurations from the software, as well as completely new workflows programmed in Python.

```{important}
Creating Apps is a rather advanced topic, so you should be familiar with the basic inspection concept of ZEISS INSPECT beforehand. New to ZEISS INSPECT? You find an introduction in the ZEISS Quality Tech Guide:

[Access Point: ZEISS INSPECT](https://techguide.zeiss.com/en/zeiss-inspect-2025/article/access_point_gom_inspect.html)

Or, depending on your application, you might be interested in the specific articles:
* [Access Point: ZEISS INSPECT X-Ray](https://techguide.zeiss.com/en/zeiss-inspect-2025/article/access_point_volume_inspect.html)
* [Access Point: Airfoil Inspection](https://techguide.zeiss.com/en/zeiss-inspect-2025/article/access_point_gom_blade_inspect.html),
* or [Access Point: ZEISS CORRELATE](https://techguide.zeiss.com/en/zeiss-inspect-2025/article/access_point_zeiss_inspect_correlate.html).

```
If you are new to Apps, you find some introductions in the ZEISS Quality Tech Guide:

* [Introduction to Add-ons](https://techguide.zeiss.com/en/zeiss-inspect-2023/article/introduction_to_add-ons.html)
* [How to Create a Basic Add-on](https://techguide.zeiss.com/en/zeiss-inspect-2023/article/how_to_create_a_basic_add_on.html)
* [How to Create an Advanced Add-on](https://techguide.zeiss.com/en/zeiss-inspect-2023/article/how_to_create_an_advanced_add_on.html)

Check out the ZEISS INSPECT Apps news page!

```{eval-rst}
.. toctree::
   :maxdepth: 1
   
   news/news
```

```{eval-rst}
.. toctree::
   :hidden:
   
   news/20240315-element-selection
   news/20240314-internationalization-tool-update
   news/20240307-mesh-selection
   news/20240307-csharp_dotnet
   news/20240209-test-coverage
   news/20240205-using-gui-libraries
   news/20240130-working-with-stages
   news/20240130-using-wheelhouses
   news/20240119-scripted-elements-examples
   news/20240115-software-starting-options
   news/20240115-project-keywords
   news/20231215-api-examples
   news/20231221-faq
   news/welcome
```

Furthermore, we recommend following our how-to guides to get you started.

```{eval-rst}
.. toctree::
   :maxdepth: 1
   :caption: How-to Guides

   howtos/python_api_introduction/python_api_introduction
   howtos/python_api_introduction/selecting_elements
   howtos/using_app_editor/using_app_editor
   howtos/app_file_format/app_file_format
   howtos/app_documentation/app_documentation
   howtos/using_vscode_editor/using_vscode_editor
   howtos/python_api_introduction/file_selection_dialog
   howtos/python_api_introduction/user_defined_dialogs
   howtos/python_api_introduction/creating_wizard_dialogs
   howtos/using_gui_libraries/using_gui_libraries
   howtos/scripted_elements/scripted_elements_toc
   howtos/python_api_introduction/using_script_resources
   howtos/stages/stages
   howtos/project_keywords/project_keywords
   howtos/using_shared_environments/using_shared_environments
   howtos/using_wheelhouses/using_wheelhouses
   howtos/adding_workspaces_to_apps/adding_workspaces_to_apps
   howtos/using_services/using_services
   howtos/using_scripted_diagrams/using_scripted_diagrams
   howtos/localization/localization
   howtos/starting_options/starting_options
   howtos/testing_apps/testing_apps
   howtos/scripting_legacy_projects/scripting_legacy_projects
   howtos/scripting_solutions/scripting_solutions
   howtos/faq/faq
```


If you already know how to create an App and now you are interested in Python programming in ZEISS INSPECT, take a look at our collection of Python examples.

```{eval-rst}
.. toctree::
   :maxdepth: 1
   :caption: Python API Examples

   python_examples/index
   python_examples/examples_overview
```

Available API functions are documented in the Specification.

```{eval-rst}
.. toctree::
   :maxdepth: 2
   :caption: Python API Specification

   python_api/python_api
   python_api/scripted_elements_api
   python_api/resource_api
```
