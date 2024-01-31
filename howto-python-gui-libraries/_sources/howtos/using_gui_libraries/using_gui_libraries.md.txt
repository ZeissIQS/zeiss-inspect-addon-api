# Using an additional Python GUI library

> Abstract: The Add-on Editor and the Dialog Designer provide an easy and convenient way of adding a graphical user interface to your Add-on &mdash; see <a href="../python_api_introduction/user_defined_dialogs.md">User-defined dialogs</a>. GUIs which are created this way seamlessly integrate into the look and feel of ZEISS INSPECT. However, there are reasons why using a separate Python GUI library might be preferred. This article gives a brief overview on use-cases, options and installation.

## Use-cases

There are three main reasons for using an additional GUI library:

* You are missing an important feature in the Add-on development environment
* You want to integrate existing Python GUI code into an Add-on
* You are already familiar with a GUI library as a developer

## Options

<a href="https://www.pythonguis.com/faq/which-python-gui-library/" target="_blank" rel="noopener noreferrer">Which Python GUI library should you use? - Comparing the Python GUI libraries available in 2023</a> gives an excellent overview on available options.

The most relevant libraries for Add-on development are:

* PyQt5/PySide2
* PyQt6/PySide6
* Tkinter

PyQt and Pyside are technical siblings, but they are provided with different licenses &mdash; see <a href="https://www.pythonguis.com/faq/pyqt-vs-pyside/" target="_blank" rel="noopener noreferrer">PyQt vs PySide Licensing</a>.

ZEISS INSPECT currently uses Qt5, so implementing an Add-on with PyQt5/Pyside2 will definitely integrate seamlessly into the look and feel. 

Tkinter's look and feel differs significantly from the usual Windows/ZEISS INSPECT GUIs. It is probably only an option if you have to integrate legacy code.

### Installing PyQt

Both PyQt5 and PyQt6 have to be installed as described in <a href="../using_wheelhouses/using_wheelhouses.md">Using Python wheelhouses</a>. Additionally, the Python packages `PyQt5-sip` or `PyQt6-sip`, respectively,  have to be installed with the Add-on Explorer.

### Installing PySide

Both PySide2 and PySide6 have to be installed as described in <a href="../using_wheelhouses/using_wheelhouses.md">Using Python wheelhouses</a>.

### Tkinter

Tkinter is already part of the ZEISS INSPECT Python installation. 
