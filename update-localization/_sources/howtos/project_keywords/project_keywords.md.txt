# Project keywords handling

> Abstract: Project keywords can be used for storing meta information. In a project with stages, project keywords can be applied to all stages or to specific stages.

## Define project keywords dialog

![Define Project Keywords Dialog](assets/define_project_keywords.png)

See [ZEISS Quality Tech Guide: Define Project Keywords](https://techguide.zeiss.com/en/zeiss-inspect-2023/article/cmd_sys_set_project_keywords.html) for an introduction.

## Reading project keywords

A project must be loaded before project keywords can be used. This can be checked with:

```{code-block} python
if not hasattr(gom.app, 'project'):
    print("No project loaded - exiting.")
    quit(0)
```

`print(gom.app.project.project_keywords)` shows the available project keywords.

From a script, you access the keyword set "User-defined". User-defined project keywords have the prefix `user_` internally, i.e. to access the project variable 'Inspector' as shown in the dialog, the following code is used:

```{code-block} python
if 'user_inspector' in gom.app.project.project_keywords:
    inspector = gom.app.project.get('user_inspector')
```

Checking if the wanted keyword exists before using `get()` prevents an exception in case the keyword is not available. You can also use exception handling instead:

```{code-block} python
try:
    inspector = gom.app.project.get('user_inspector')
except:
    inspector = None
```

To get the keyword description, you use:

```{code-block} python
try:
    inspector_desc = gom.app.project.get('description(user_inspector)')
except:
    inspector_desc = None
```

## Writing project keywords

```{note}
When using `set_project_keywords()` the keyword prefix `user_` must be omitted.
```

To add a new keyword, both a value and a keyword description must be set:

```{code-block} python
gom.script.sys.set_project_keywords (
    keywords = {'project': 'My Project'},
    keywords_description = {'project': 'Project Name'}
)
```

To modify the value of an existing keyword, it is sufficient to assign a new value: 

```{code-block} python
gom.script.sys.set_project_keywords (
    keywords = {'project': 'Project XYZ'}
)
```

## Stage specific keywords

With the code examples above, the project keywords apply to all stages.

To write a project keyword to a specific stage:

```{code-block} python
gom.script.sys.set_project_keywords(
  keywords = {'system': 'Shock'},
  keywords_description = {'system': 'System'},
  stage = gom.app.project.stages['ZEISS Training Object Mesh 3'])
```

To access project keywords per stage:

```{code-block} python
for stage in gom.app.project.stages:
	print(f"Stage: {stage.name} System='{gom.app.project.in_stage[stage.index].get('user_system')}'")
```

Example Result:
```
Stage: ZEISS Training Object Mesh 1 System=''
Stage: ZEISS Training Object Mesh 2 System=''
Stage: ZEISS Training Object Mesh 3 System='Shock'
Stage: ZEISS Training Object Mesh 4 System=''
Stage: ZEISS Training Object Mesh 5 System=''
```
