# Add-on file format

## Introduction
An Add-on file file (extension: *.addon) is a ZIP archive with pre-defined folder- and filenames. An Add-on file can be unzipped/edited/zipped manually if necessary.

## Structure
### Folder structure
| File              | Description                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------|
| `<other folder>/` | All other folders are containing add-on content. The format of this content is discussed below.             |
| `doc/`            | Add-on documentation as displayed in the software store. Must contain a README.md  file in markdown format. |
| `icon.png`        | Add-on icon as displayed in the add-on manager and the software store                                       |
| `key.enc`         | Add-on protection and licensing information in case the add-on is protected                                 |
| `license/`        | Terms-of-use related to this add-on. Can contain a set of text files like license.txt , license_numpy.txt , ... which will be displayed and must be acknowledged upon add-on installation                                               |
| `metainfo.json`   | Add-on metainfo data (title, description, version, ...)                                                     |

### Content types
Top level folders determine the content type. For every content entry, a sub folder must be present in that top level folder.

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
| terms_of_use	            | Collection of terms-of-use for add-on creation  |              |
| tolerance_legends	        | Tolerance legends (3D)	                      |              |
| user_defined_checks	    | User defined checks	                          |              |
| user_defined_inspection_principles | User defined inspection principles     |              |
| workspaces                | Workspace definitions                           |              |

### Content data
