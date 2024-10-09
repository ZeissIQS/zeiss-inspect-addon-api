# gom.Resource API

## Summmary

The `gom.Resource` API can be used to access binary data of files included in an App's scripts folder.

```{seealso}
For a description of the general concept, see [Using script resources](../howtos/python_api_introduction/using_script_resources.md).

For examples, see <a href="https://github.com/ZEISS/zeiss-inspect-app-examples/blob/main/AppExamples/README.md#script_resources--how-to-access-binary-data-of-your-app-resources">Examples of category `script_resources`</a>.
```

## Class definition

```{eval-rst}
.. py:class:: gom.Resource
   
   This module represents the Resource class. A utility to access resource data using relative paths and shared memory.

   .. py:staticmethod:: Resource.list()

      Lists all resources

      :returns: List of resources

   .. py:staticmethod:: Resource.cleanup()

      Closing all dangling resources (API call to free memory on C++ side)
      
   .. py:method:: __init__(path)

      Constructor

      :param path: Qualified name of the resource

   .. py:method:: isLoaded()

      Check if the resource is loaded

      :returns: True if the resource is loaded, False otherwise

   .. py:method:: close()

      Release resource from shared memory

   .. py:method:: open(size=0)

      Open the resource in shared memory

   .. py:method:: exists()

      Check if the resource exists

      :returns: True if the resource exists, False otherwise

   .. py:method:: byteSize()

      Get the size of the resource in bytes

      :returns: The size of the resource in bytes

   .. py:method:: keepInMemory()

      Keep the resource in memory

   .. py:method:: save(size=0)

      Save the resource

      :param size: Size of the resource
      :returns: True if the save was successful, False otherwise

   .. py:method:: saveAsUserResource(new_path, overwrite=True)

      Save the resource to a new path

      :param new_path: New path to save the resource
      :param overwrite: True to overwrite existing files, False to not overwrite

```
