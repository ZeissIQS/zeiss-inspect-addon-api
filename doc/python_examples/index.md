---
myst:
   html_meta:
      "description": "Examples for using the ZEISS INSPECT 2025 App Python API"
      "keywords": "Metrology, ZEISS INSPECT, Python API, GOM API, Scripting, Add-ons, Apps, Examples"
---
#  Introduction to the Python API Examples

Welcome to the ZEISS INSPECT Python API Examples. Here you find the [App Examples Overview](examples_overview) with a list ordered by topics and tagged with keywords. You can view the source code and download the Apps for importing into ZEISS INSPECT. You can reuse and adapt these code examples to your specific use case and learn the best-practices we recommend.

## How the examples are structured

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

If you are interested in testing Apps (which you should be), learn more in our [Testing Apps How-To](../howtos/testing_apps/testing_apps.md).

## Example projects

Most of the example scripts rely on a certain project file to be loaded. The project files are provided in the App <a href="examples_overview.html#projects-zeiss-inspect-projects">ExampleProjects</a>. Some of the App examples load the required project file automatically if this is possible (E.g. in the `if __name__ == '__main__'` block).

Sometimes it is necessary to load projects manually. You can do this easily using the `setup_project.py` script provided in <a href="examples_overview.html#projects-zeiss-inspect-projects">ExampleProjects</a>.

See <a href="examples_overview.html#example-projects">App Examples Overview &mdash; Example projects</a>
