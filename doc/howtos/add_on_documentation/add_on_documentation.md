# Documenting Add-ons

```{note}
The Add-on documentation is part of the packaged Add-on.
```

```{eval-rst}
.. toctree::
   :hidden:

   assets/Releasenotes.md
```

## Terminology

| Item                           | Description                                                | Origin                                                              |
| ------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------------- |
| Title                          | Add-on title                                               | 'Title' field in the Add-on properties/<br>`"title"` in <a href="../add_on_file_format/add_on_file_format.html#metainfojson-documentation">metainfo.json</a> |
| One-Liner                      | Add-on short description, a single line                    | 'Description' field in the Add-on properties/<br>`"description"` in <a href="../add_on_file_format/add_on_file_format.html#metainfojson-documentation">metainfo.json</a> |
| Short description              | Add-on short description                                   | `doc/README.md`, first paragraph,<br>see below                   |
| Long description               | Add-on long description                                    | `doc/README.md`, starting from second<br>paragraph, see below    |
| Documentation                  | Documentation as PDF (optional)<br>(in download area, not shown above)  | `doc/Documentation.md/.pdf`                            |
| Releasenotes                   | Releasenotes as PDF                                        | `doc/Releasenotes.md`                                               |
| Add-on category                   | Add-on category (optional)                                 | `"technical-category"` in <a href="../add_on_file_format/add_on_file_format.html#metainfojson-documentation">metainfo.json</a> |
| Versions                       | Main software / Add-on version                                | `"software-version"` and  `"version"`<br>in <a href="../add_on_file_format/add_on_file_format.html#metainfojson-documentation">metainfo.json</a> |
| Compatible software            | Compatible main software product(s)                        | `"compatible-software"` in <a href="../add_on_file_format/add_on_file_format.html#metainfojson-documentation">metainfo.json</a> |

### Rendering in the ZEISS Quality Software Store

```{figure} assets/software_store-1.png
:alt: ZEISS Quality Software Store &ndash; Product overview
:align: center
:class: bordered-figure

ZEISS Quality Software Store &ndash; Product overview
```

```{figure} assets/software_store-2.png
:alt: ZEISS Quality Software Store &ndash; Product details
:align: center
:class: bordered-figure

ZEISS Quality Software Store &ndash; Product details
```

## Add-on documentation structure

```{caution}
Add-on short / long descriptions can only be rendered as plain text without formatting in the ZEISS Quality Software Store.
```

```{note}
An Add-on (`.addon` file) is technically a ZIP file. See [Add-on file format](../add_on_file_format/add_on_file_format.md) for details.
```

* Mandatory contents:
  * `doc/README.md` &mdash; Add-on short / long description
  * `doc/Releasenotes.md/.pdf` &mdash; The Markdown file allows viewing in the Add-on Editor while the PDF file is used in the ZEISS Quality Software Store. 
* Optional contents:
  * `doc/Documentation.md/.pdf` &mdash; Extended Add-on documentation / user manual
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
Add-on short / long descriptions can only be rendered as plain text without formatting in the ZEISS Quality Software Store.
```

```{note}
See [markdown guide](https://www.markdownguide.org/basic-syntax/) for a brief description of the markdown format.
```

See [ZEISS Quality Software Store &mdash; FileSelectionAndFiltering](https://software-store.zeiss.com/products/apps/FileSelectionAndFiltering) for example.

![ZEISS INSPECT Add-on editor with Markdown viewer](assets/markdown_editor_viewer.png)
A markdown editor/viewer is integrated in the ZEISS INSPECT Add-on editor.

See [Releasenotes template](assets/Releasenotes.md).

## Converting Markdown files to Portable Document Format (PDF)

The [Visual Studio Code](https://code.visualstudio.com/) extension [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) allows to convert Markdown files to PDF.
The ZEISS App Development Environment converts Releasenotes from Markdown to PDF automatically. 
