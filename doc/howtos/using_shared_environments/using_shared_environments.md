# Using shared environments

> Abstract: With software version 2023, each Add-on has a separate script execution environment. That means, a script can only `import` Python modules located in the same Add-on and can only use Python modules (wheels) installed in the same Add-on's `scripts/modules` folder. This property can be changed by using the shared environment concept described in this How-to Guide. 

## Why separate script environments are useful

Separate script environments prevent conflicts between Add-ons. An Add-on is self-contained, i.e. there are no dependencies on Python modules installed in other Add-ons or in a global script environment. There is no impact on other Add-ons by installing, uninstalling or updating a module.

In most cases, using the separate script environment in an Add-on is the preferred way.

## Use cases for shared environments

Shared environments are useful if
* Modules (wheels) from external sources shall be installed in a shared folder
    * for keeping the versions synchronized across multiple Add-ons
    * to apply software security measures before installing
* Add-ons are used in a hierarchical fashion, i.e. Add-ons are implemented using other Add-ons

## How to create a shared environment

Add a key-value pair `"environment": <environment_name>` to the `metainfo.json` files of all Add-ons which you want to share the environment. `<environment_name>` can be any string, but you are adviced to use a unique name to avoid potential conflicts with other, separate environments. The `environment` element can be placed at any position within the JSON file.

## Example:

### Add-on "SharedEnvProvider"
```{code-block}
:caption: File structure

SharedEnvProvider
|-- scripts
|   |-- modules
|   |   |-- numpy-xyz.whl
|   |
|   |-- SharedEnvProvider.py
|
|-- metainfo.json
```

```{code-block} python
:caption: SharedEnvProvider&sol;scripts&sol;SharedEnvProvider.py

# -*- coding: utf-8 -*-

import gom

Data = 42

def hello(name):
	print(f"Hello {name}!")

class TestObject:
	def __init__(self, material):
		self.material = material
		
	def print_material(self):
		print(self.material)
```

```{code-block} json
:caption: SharedEnvProvider&sol;metainfo.json

{
    "author": "Test user",
    "description": "Example for shared environment",
    "environment": "SharedEnv1234",
    "labels": [
    ],
    "licensing": {
        "licenses": [
        ],
        "product-codes": [
        ]
    },
    "software-revision": "735",
    "software-version": "ZEISS INSPECT 2023",
    "tags": [
    ],
    "title": "SharedEnvBase",
    "uuid": "178f89cc-fc62-413f-b692-dbc68bf67ec8",
    "version": "1.0.2"
}
```

### Add-on "SharedEnvUser"
```{code-block}
:caption: File structure

SharedEnvUser
|-- scripts
|   |-- modules
|   |-- SharedEnvUser.py
|
|-- metainfo.json
```

```{code-block} python
:caption: SharedEnvUser&sol;scripts&sol;SharedEnvUser.py

# -*- coding: utf-8 -*-

import gom
import SharedEnvProvider

# Importing a package installed in SharedEnvProvider
import numpy as np

# Accessing data in SharedEnvProvider
print(f"Data: {SharedEnvProvider.Data}")

# Calling a function in SharedEnvProvider
SharedEnvProvider.hello("unknown Python programmer")

# Using a class from SharedEnvProvider
testObject = SharedEnvProvider.TestObject("Sheet Metal")
testObject.print_material()

# Using the numpy package from SharedEnvProvider
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
```

```{code-block} json
:caption: SharedEnvUser&sol;metainfo.json

{
    "title": "SharedEnvUser",
    "...": "...",
    "environment": "SharedEnv1234",
    "...": "..."
}
```

```{note}
An Add-on has to be finished (with **Finish Editing**) before its Python files can be imported as modules in another Add-on, otherwise a `ModuleNotFoundError` will be thrown. 
```

## Using shared environments with protected Add-ons

| Provider Add-on | User Add-on | Description                                                        |
| --------------- | ----------- | ------------------------------------------------------------------ |
| protected       | unprotected | &#x274c; curently not supported                                         |
| unprotected     | protected   | &#x2714; no additional measures required                 |
| protected       | protected   | &#x1f511; 'shared secret' must be created when applying the protection |

Protecting an Add-on and creating the shared secret is done with a tool by ZEISS IQS, which is currently provided on request.
