# Documenting Apps

```{note}
The App documentation is part of the packaged App.
```

```{eval-rst}
.. toctree::
   :hidden:

   assets/Releasenotes.md
```

## Terminology

![ZEISS Quality Software Store &ndash; Product overview](assets/software_store-1.png)

![ZEISS Quality Software Store &ndash; Product details](assets/software_store-2.png)

| Item                           | Description                                                | Origin                                                              |
| ------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------------- |
| Title                          | App title                                                  | 'Title' field in the App properties /<br>`"title"` in <a href="../app_file_format/app_file_format.html#metainfojson-documentation">metainfo.json</a> |
| One-Liner                      | App short description, a single line                       | 'Description' field in the App properties /<br>`"description"` in <a href="../app_file_format/app_file_format.html#metainfojson-documentation">metainfo.json</a> |
| Short description              | App short description                                      | `doc/README.md`, first paragraph,<br>see below                      |
| Long description               | App long description                                       | `doc/README.md`, starting from second<br>paragraph, see below       |
| Documentation                  | Documentation as PDF (optional)<br>(in download area, not shown above)  | `doc/Documentation.md/.pdf`                            |
| Releasenotes                   | Releasenotes as PDF                                        | `doc/Releasenotes.md`                                               |
| App category                   | App category (optional)                                    | `"technical-category"` in <a href="../app_file_format/app_file_format.html#metainfojson-documentation">metainfo.json</a> |
| Versions                       | Main software version and App version                      | `"software-version"` and  `"version"`<br>in <a href="../app_file_format/app_file_format.html#metainfojson-documentation">metainfo.json</a> |
| Compatible software            | Compatible main software product(s)                        | `"compatible-software"` in <a href="../app_file_format/app_file_format.html#metainfojson-documentation">metainfo.json</a> |

## App documentation structure

```{caution}
App short / long descriptions can only be rendered as plain text without formatting in the ZEISS Quality Software Store.
```

```{note}
An App (`.addon` file) is technically a ZIP file. See [App file format](../app_file_format/app_file_format.md) for details.
```

* Mandatory contents:
  * `doc/README.md` &mdash; App short / long description
  * `doc/Releasenotes.md/.pdf` &mdash; The Markdown file allows viewing in the App Editor while the PDF file is used in the ZEISS Quality Software Store. 
* Optional contents:
  * `doc/Documentation.md/.pdf` &mdash; Extended App documentation / user manual
  * `doc/...` &mdash; any number of additional files

### Example

#### Source: `doc/README.md`

```markdown
# Airfoil Inspection

Contains relevant functions to inspect airfoils. The app also supports the acquisition and preparation of optical and tactile measurement data. The industry-specific
Airfoil Inspection workspace is optimized for analyzing airfoils, such as blades, vanes or blisks.

The Airfoil Inspection App provides functions to prepare your measured data, no matter if tactile or optical, and to analyze airfoils, such as blades, vanes or blisks.
In addition, the App also provides the Smart Teach functionality for profile edge points, to measure airfoils in a dedicated way. 

Further functionality provided by Airfoil Inspection: 
 - specific Airfoil workspaces 
 - import and processing of tactile measured curves (incl. stylus sphere radius correction) 
 - interface to CALYPSO for data acquisition 
 - advanced Airfoil functionalities for profile inspection 
 - industry specific Apps  
     - Efficient Blisk Measurement and Inspection 
     - Airfoil Bow and Sweep Inspection 
     - Virtual Balancing 
     - Throat Area - together with Local Minimal Surface 

Want to know more? Check the related articles in the ZEISS Quality Tech Guide.
```

#### Short description

> Contains relevant functions to inspect airfoils. The app also supports the acquisition and preparation of optical and tactile measurement data. The industry-specific
> Airfoil Inspection workspace is optimized for analyzing airfoils, such as blades, vanes or blisks.

#### Long description


> The Airfoil Inspection App provides functions to prepare your measured data, no matter if tactile or optical, and to analyze airfoils, such as blades, vanes or blisks.
> In addition, the App also provides the Smart Teach functionality for profile edge points, to measure airfoils in a dedicated way. 
>
> Further functionality provided by Airfoil Inspection: 
> - specific Airfoil workspaces 
> - import and processing of tactile measured curves (incl. stylus sphere radius correction) 
> - interface to CALYPSO for data acquisition 
> - advanced Airfoil functionalities for profile inspection 
> - industry specific Apps  
>     - Efficient Blisk Measurement and Inspection 
>     - Airfoil Bow and Sweep Inspection 
>     - Virtual Balancing 
>     - Throat Area - together with Local Minimal Surface 
>
> Want to know more? Check the related articles in the ZEISS Quality Tech Guide.

## Markdown

```{caution}
App short / long descriptions can only be rendered as plain text without formatting in the ZEISS Quality Software Store.
```

```{note}
See [markdown guide](https://www.markdownguide.org/basic-syntax/) for a brief description of the markdown format.
```

See [ZEISS Quality Software Store &mdash; FileSelectionAndFiltering](https://software-store.zeiss.com/products/apps/FileSelectionAndFiltering) for example.

![ZEISS INSPECT App editor with Markdown viewer](assets/markdown_editor_viewer.png)
A markdown editor/viewer is integrated in the ZEISS INSPECT App editor.

See [Releasenotes template](assets/Releasenotes.md).

## Converting Markdown files to Portable Document Format (PDF)

The [Visual Studio Code](https://code.visualstudio.com/) extension [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) allows to convert Markdown files to PDF.
The ZEISS App Development Environment converts Releasenotes from Markdown to PDF automatically. 

## Link to external documentation

![New in Version 2025](https://img.shields.io/badge/New-Version_2025-orange)

You can create a link to a website providing App documentation by adding a JSON object `"documentation": "<url>"` to the App's `metainfo.json` file:

```{code-block}
:caption: Example documentation link in `metainfo.json`

{
    ...
    "documentation": "https://zeissiqs.github.io/zeiss-inspect-addon-api/2025/index.html",
    ...
}
```

If a documentation link is defined in an App, each dialog window will provide a help button in its title bar.

![App dialog window with help button](assets/dialog_help_button.png)

When the help button is clicked, the user must confirm that the linked documentation pages is openened in the system's web browser.

![Open documentation page confirmation dialog](assets/open_documentation_confirmation.png)
