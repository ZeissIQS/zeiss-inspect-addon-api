# Overview

Welcome to the Python API Examples. Here you can find the documentation of the examples which are provided by the
`Python API Examples` Add-On. You can reuse and adapt these code examples to your specific use case and learn the best-practices we recommend.

## How the examples are structured

You will find example scripts in a corresponding category folder, e.g. `data_interfaces`, `dialog_widgets`, etc.

The folders of the example scripts correspond to the chapters of this documentation.
Many of the examples have the following structure:

```python

def function1 ():
  <example code1>
  
def function2 ():
  # -------------------------------------------------------------------------
  <example code2>
  # -------------------------------------------------------------------------

[...]

if __name__ == '__main__':
  [...]
  something = function1()
  something2 = function2()
  [...]

```

The most important spots of the example are marked with `# ------` comments in the code. 

Overall, this structure seems to be a little bit too complex for simple examples.
The same result could be achieved by directly writing the `<example code>` in the script without separating it into functions.
*However, this has a reason*. The functions `function1` and `function2` can be tested from another test script. 
You are highly encouraged to use this modular approach as well, to keep your code testable and reusable.

If you are interested in testing add-ons (which you should be), learn more in our [Testing Add-Ons How-To](../howtos/testing_addons/testing_addons.md).

## Example projects

Most of the example scripts rely on a certain project file to be loaded. The add-on already contains these projects, and some examples load them automatically when it is possible (E.g. in the `if __name__ == '__main__'` block).

Sometimes it is necessary to load projects manually. You can do this easily using the `setup_project.py` script.

The following project files are included:

| Project name          | Description                                                               |
| --------------------- | ------------------------------------------------------------------------- |
| gom_part_test_project | Simple optically measured part with a CAD, mesh and some basic inspection |
| volume_test_part      | A small test volume for CT related inspections                            |

## Examples by topic

| Folder                                   | Description                                                  |
| ---------------------------------------- | ------------------------------------------------------------ |
| [data_interfaces](data_interfaces.rst)   | Access to data of GOM "elements"                             |
| [dialog_widgets](dialog_widgets.rst)     | Examples how use custom dialogs and handle user input events |
| [misc](misc.rst)                         | Miscellaneous examples                                       |
| [script_icons](script_icons.rst)         | Set icons for scripts or buttons                             |
| [script_resources](script_resources.rst) | How to access binary data of your add-on (resources)         |
| [scripted_actuals](scripted_actuals.rst) | Building actual elements with custom python code             |
| [scripted_checks](scripted_checks.rst)   | Building custom checks with python code                      |

 