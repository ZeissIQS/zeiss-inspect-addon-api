# Using Python wheelhouses

> Abstract: Usually installing Python packages via the App Explorer in the App Editor works just fine. In certain cases, the installation succeeds but the App will fail with the error message `The specified module could not be found.` This could be caused by inter-wheel dependencies or by hardcoded paths in packages, which are different from the ones used by the ZEISS INSPECT software. This is solved by creating a Python wheelhouse, which is installed in the same way as a normal Python wheel. Technically, a wheelhouse is a ZIP archive of Python wheels.

## Creating a wheelhouse

[PyQt5](https://pypi.org/project/PyQt5/) is used as a real-world example here.

1. Install all required Python wheels into a temporary folder

```
python -m pip install PyQt5 --target=tmp --upgrade
```

2. Create a ZIP archive of all files **below** the temporary folder

E.g. using 7-Zip

```
cd tmp
"C:\Program Files\7-Zip\7z.exe" a PyQt5-Wheelhouse.zip *
```

3. Install the wheelhouse using the App Explorer

![Install Python Package dialog - install from local file](install_python_package.png)

![Add Python Packages dialog - add Python wheelhouse files](add_wheelhouse.png)

```{note}
For some reason, `PyQt5.sip` (a Python wheel required by `PyQt5`) could not be used from the Python wheelhouse, but had to be installed additionally using the App Explorer.
```
