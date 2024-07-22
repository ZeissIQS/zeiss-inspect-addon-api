# App file format

## Introduction

💡 An ZEISS INSPECT App file (extension: *.addon) is a ZIP archive with pre-defined folder- and filenames. 

While an App file will be created and modified with the App Editor in most cases, it can also be unzipped/edited/zipped manually if necessary.

## Structure

### Folder structure

| File              | Description                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------ |
| `<other folder>/` | All other folders are containing App content. The format of this content is discussed below.                 |
| `doc/`            | App documentation as displayed in the Software Store. Must contain a `README.md` file in markdown format.    |
| `icon.png`        | App icon as displayed in the App Manager and the Software Store                                              |
| `key.enc`         | App protection and licensing information in case the App is protected                                        |
| `license/`        | Terms-of-use related to this App. Can contain a set of text files like `license.txt` , `license_numpy.txt` , ... which will be displayed and must be acknowledged upon App installation                                                                                              |
| `metainfo.json`   | App metainfo data (title, description, version, ...)                                                         |

### Content types

💡 The top level folders determine the "content type". Inside these top level folders, a separate sub folder must be provided for each item.

| Folder / Provider name    | Content type                                    | Notes        |
| ------------------------- | ----------------------------------------------- | ------------ |
| backgrounds	            | Environment (rendering) backgrounds	          |              |
| cad_import_modes	        | CAD import templates	                          |              |
| configurations	        | Visibility settings	                          | INTERNAL     |
| diagrams	                | Diagrams (3D view)	                          |              |
| element_properties	    | Element creation properties	                  |              | 
| explorer_filter_templates	| Explorer filter settings	                      |              |
| export_templates	        | Element export scripts	                      |              |
| gradient_color_maps	    | Templates for volume color gradient	          |              |
| gvf_templates	            | Gray value feature templates	                  |              |
| inspection_styles	        | I-Inspect configurations	                      |              |
| import_templates	        | Element import scripts	                      |              |
| iso_tolerance_tables	    | ISO tolerance table templates	                  |              |
| keywordsets	            | Project keywords	                              |              |
| labels	                | Element label templates	                      |              |
| languages	                | Translation files	                              |              |
| legends	                | 3D legend templates	                          |              |
| lightingconfigs	        | Light setup templates (rendering)	              |              |
| materials                 | Material templates (rendering)	              |              |
| perspectives	            | UI configurations	                              |              |
| range_color_maps	        | Templates for volume color ranges	              |              |
| reports	                | Report page templates	                          |              |
| scripts	                | Scripts	                                      |              |
| scripted_elements	        | Scripted elements	                              |              |
| surface_classifications	| Surface defect classifications	              |              |
| tables	                | Table templates (3D view)	                      |              |
| terms_of_use	            | Collection of terms-of-use for App creation     |              |
| tolerance_legends	        | Tolerance legends (3D)	                      |              |
| user_defined_checks	    | User defined checks	                          |              |
| user_defined_inspection_principles | User defined inspection principles     |              |
| workflow_assistant        | Workflow assistant configuration                | INTERNAL     |
| workspaces                | Workspace definitions                           |              |

### Content data

💡 Each "content object" consists of a folder in one of the "content type" (top level) folders.

* A "content object" is a single template/script/element/... distributed via an App.
* Each "content object" is represented by the content of a folder in the "content type" folder matching the content type.
* The exact format of the content representation depends on the "content type".
* The name of the "content object" is the same as its folder's name.
* For template-like objects, there is always a JSON file with administrative data present. Other types may vary.

#### Example: Labels

**Folder layout 'labels'**

```
metainfo.json
labels
|-- Name
|   |--Name.json
|-- Results
|   |-- Results.json
...
```

* The folder names 'Name' and 'Results' are the templates' names
* The JSON file in each folder contains both administrative data and content information

**Name.json**

```json
{
    "content": {
        "!all:" {
            "label_background": "gom.Color (0, 0, 0, 0)",
            "label_border_mode": "'none'",
            "...": "...",
            "label_text": "..."
        },
        "...": "..."
    },
    "sort_index": 1,
    "uuid": "4a6ef87a-5214-4089-bdc3-5a96cf8b5108"
}
```

#### Example: Scripts

**Folder layout 'scripts'**
```
scripts/
|-- Tools/
|   |-- Workspaces
|       |-- create_workspace.py
|       |-- create_workspace.metainfo
|-- ...
...
```

## FAQ

### Structure

#### Why is there a folder for every single element?
* The App Editor can handle the elements transparently in this way. Just the folder is dragged & dropped, visible etc., while the content is abstracted and can edited (e.g. in a graphical editor)
* The content format specification of an element can easier be changed over time
