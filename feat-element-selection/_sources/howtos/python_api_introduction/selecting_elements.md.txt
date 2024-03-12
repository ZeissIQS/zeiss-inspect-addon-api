# Selecting elements in scripts

> Selecting elements using `gom.ElementSelection()` has been mentioned in [ZEISS INSPECT Python API Introduction](python_api_introduction.md) briefly. This section describes how `ElementSelection` is used in more details.

```{note}
You are advised to create element selections by script recording, because this is less error-prone than programming the needed command parameters.
```

## Recording element selections

You record an element selection by marking the desired groups of elements in the Explorer and executing a command on this selection. For convenience, you can use the command `gom.script.cad.show_element()` (shortcut: `v`) and replace it by the actual command in the script later. You can also select multiple elements at once.

![Explorer - Nominal Elements selected](assets/explorer-element_selection-1.png)

```{code-block} python
gom.script.cad.show_element (
    elements=gom.ElementSelection (
        {'category': ['key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'nominal']}
    )
)
```

## Accessing elements in a selection

`ElementSelection` is a reference to the selected elements:

```{code-block} Python
elements=gom.ElementSelection (
    {'category': [
        'key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'nominal'
    ]}
)
print(elements)
# output: gom.ElementSelection ({'category': ['key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'nominal']})
```

To access the selected elements for reading their properties (e.g. element names), you use the returned reference in an iteration:

```{code-block} Python
elements=gom.ElementSelection (
    {'category': [
        'key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'nominal'
    ]}
)

for element in elements:
    print(element.name)
# Example output:
# Plane 1
# Plane 2
# Circle 1
```

You use the Python list comprehension to get a list of element references:
```{code-block} Python
elements=gom.ElementSelection (
    {'category': ['key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'nominal']}
)

element_list = [element for element in elements]
print(element_list)
# example output: [gom.app.project.inspection['Plane 1'], gom.app.project.inspection['Plane 2'], gom.app.project.inspection['Circle 1']]
```  

## Examples

The following Explorer element tree is used to give some `ElementSelection` examples:
![Explorer - Examples](assets/explorer-elements_with_labels.png)

```{note}
In the examples below, all selections are restricted to a specific part (part name: `Part`). You can omit the filter specification `'part', gom.app.project.parts['Part']` to get a selection across any part or &mdash; if the project contains multiple parts &dash; all parts.
```

1. Part

   ```{code-block} Python
   elements=gom.ElementSelection (
       {'category': ['key', 'elements', 'part', gom.app.project.parts['Part']]}
   )
   ```

2. CAD (Nominal part)
   
   ```{code-block} Python
   elements=gom.ElementSelection (
       {'category': [
           'key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'nominal_part'
       ]}
   )
   ```
   
3. Mesh (Actual part)

   ```{code-block} Python
   elements=gom.ElementSelection (
       {'category': [
           'key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'actual_part'
       ]}
   )
   ```
   
4. Nominal Elements

   ```
   elements=gom.ElementSelection (
       {'category': [
           'key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'nominal'
       ]}
   )
   ```
   
5. Nominal Elements &mdash; Geometries
   
   ```{code-block} Python
   elements=gom.ElementSelection (
       {'category': [
           'key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'nominal',
           'object_family', 'geometrical_element'
       ]}
   )
   ```
   
6. Nominal Elements &mdash; Geometries &mdash; Planes 

   ```{code-block} Python
   elements=gom.ElementSelection (
       {'category': [
           'key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'nominal',
           'object_family', 'geometrical_element', 'type', 'inspection_plane'
       ]}
   )
   ```
   
7. Nominal Elements &mdash; Geometries &mdash; Planes mdash; Plane 1 

   💡 The leaf nodes of the element tree are elements, not element selections!

   ```{code-block} Python
   elements=[gom.app.project.inspection['Plane 1']]
   ```
   
8. Inspection

   ```{code-block} Python
   elements=gom.ElementSelection (
       {'category': [
           'key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'inspection'
       ]}
   )
   ```

9. Actual Elements

   ```{code-block} Python
   elements=gom.ElementSelection (
       {'category': [
           'key', 'elements', 'part', gom.app.project.parts['Part'], 'explorer_category', 'actual'
       ]}
   )
   ```
   
10. Tags

   ```{code-block} Python
   elements=gom.ElementSelection (
       {'category': ['key', 'elements', 'explorer_category', 'tags']}
   )
   ```

## Syntax

```{code-block}
ElementSelection (
    {'category': [
        'key', 'elements'
        [, 'part', <part_reference>]
        [, 'is_element_in_clipboard', 'True' |
                                      'False'
        ]
        [, 'explorer_category': 'measurements' |
                                'nominal_part' |
                                'actual_part' |
                                'linked_volumes' |
                                'nominal' | 
                                'inspection' | 
                                'actual' | 
                                'coordinate_systems' |
                                'alignment' |
                                'reports' | 
                                'stage_ranges' |
                                'tags' | 
                                ... 
                                  [, 'object_family', <object_family_name> [, 'type': <type_name>]]
        ]
    ]}
)

ElementSelection (
    {'category': [
        'key', 'elements',
        'overview_explorer_categories', 'required_for' | 
                                        'depends_on'
    ]}
)

```

You can also use the `ElementSelection` command with multiple selection filters:

```{code-block} Python
elements = gom.ElementSelection (
    {'category': ['key', 'elements', 'explorer_category', 'nominal']},
    {'category': ['key', 'elements', 'explorer_category', 'actual']}
)
```
