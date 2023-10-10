---
myst:
   html_meta:
      "description": "ZEISS INSPECT 2023 Add-on Python API Documentation"
      "keywords": "Metrology, ZEISS INSPECT, Python API, Scripting, Add-ons, How-tos, Examples, Specification, Documentation"
--- 

# Add-On Documentation 2023

Welcome to the Add-On documentation. With Add-Ons, you will be able to customize and extend the functionality of your ZEISS INSPECT software. 
You can include several template configurations from the software, as well as completely new workflows programmed in Python.

```{important}
Creating add-ons is a rather advanced topic, so you should be familiar with the basic inspection concept of ZEISS INSPECT beforehand. New to ZEISS INSPECT? This free course teaches you the basics:

[(eLearning) 780 Starter Training ZEISS INSPECT](https://training.gom.com/home/LearningPath/7265)

Or, depending on your application, you might be interested in the specific starter trainings for [ZEISS INSPECT X-Ray](https://training.gom.com/home/LearningPath/7280), [ZEISS INSPECT Correlate](https://training.gom.com/home/LearningPath/7282), or [ZEISS INSPECT Airfoil](https://training.gom.com/home/LearningPath/7281).

```

If you are new to add-ons, we recommend following our how-to guides to get you started.

```{eval-rst}
.. toctree::
   :maxdepth: 1
   :caption: How-to Guides

   howtos/python_api_introduction/python_api_introduction
   howtos/using_add_on_manager/using_add_on_manager
   howtos/add_on_file_format/add_on_file_format
   howtos/add_on_documentation/add_on_documentation
   howtos/using_vscode_editor/using_vscode_editor
   howtos/python_api_introduction/user_defined_dialogs
   howtos/python_api_introduction/creating_wizard_dialogs
   howtos/scripted_elements/scripted_elements_toc
   howtos/python_api_introduction/using_script_resources
   howtos/using_shared_environments/using_shared_environments
   howtos/adding_workspaces_to_addons/adding_workspaces_to_addons
   howtos/localization/localization
   howtos/testing_addons/testing_addons
```


If you already know how to create an add-on and now you are interested in Python programming in ZEISS INSPECT, take a look at our collection of Python examples.

```{eval-rst}
.. toctree::
   :maxdepth: 1
   :caption: Python API Examples
   :titlesonly:

   python_examples/index
   python_examples/data_interfaces
   python_examples/dialog_widgets
   python_examples/misc
   python_examples/script_icons
   python_examples/script_resources
   python_examples/scripted_actuals
   python_examples/scripted_checks
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
