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

![](assets/add-on_terminology.png)

| Index | Item                           | Description                                                | Origin                                                              |
| ----- | ------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------------- |
|     1 | Title                          | App title                                                  | 'Title' field in the App. Set during App creation.                  |
|     2 | Company                        | Company which maintains the App                            | Company the uploading account belongs to. Set during App creation.  |
|     3 | App description                | App short description                                      | 'Description' field in the App. Set during App creation.            |
|     4 | Splash description             | Some information about the App, e.g. for advertising it    | doc/README.md from the App. See below how to edit it.               |
|     5 | Link to complete documentation | Complete App documentation | Something referenced from within the doc/README.md. Can be a PDF, a link to some external site, ... | 

## App documentation structure

```{note}
An App (`.addon` file) is technically a ZIP file. See [App file format](../app_file_format/app_file_format.md) for details.
```

* Mandatory contents:
  * `doc/README.md` &mdash; this will be rendered as the product's splash description ad.
  * `Releasenotes.md` and `Releasenotes.pdf` &mdash; The Markdown file allows viewing in the App Editor while the PDF file is used in the ZEISS Quality Software Store. 
* Recommended contents:
  * `Documentation.md` (and optional `Documentation.pdf`) &mdash; full App documentation

The App can contain an arbitrary number of additional files in the `doc` folder referenced from within the files `README.md` or `Documentation.md`.

### Example

* Documentation related content of the App 'Python API Examples':

    ![](assets/7-ZIP_README.png)

* The README.md is the starting point for rendering the App's splash description and will reference other files:

    ![](assets/Edit_README.png)

* This will result in the following splash description:

    ![](assets/splash.png)

## Markdown

```{note}
See [markdown guide](https://www.markdownguide.org/basic-syntax/) for a brief description of the markdown format.
```

See [ZEISS Quality Software Store &mdash; DisplayImage](https://software-store.zeiss.com/products/apps/DisplayImage) for example.

![](assets/markdown_editor_viewer.png)
A markdown editor/viewer is integrated in the ZEISS INSPECT App editor.

See [Releasenotes template](assets/Releasenotes.md).

## Portable Document Format (PDF)

The standard expression to reference a PDF from `doc/README.md` is:

```{code-block} markdown
:caption: doc\/README.md

See [Documentation](Documentation.pdf) for detailed description.
```

## Converting Markdown files to PDF

The [Visual Studio Code](https://code.visualstudio.com/) extension [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) allows to convert a Markdown file to PDF.