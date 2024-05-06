# Using the App Editor

Script Editor and Package Manager have been integrated as the App Editor. Here you can write Python scripts, add/remove contents, create/edit, export and publish Apps.

See the ZEISS Quality Tech Guide article [App Editor](https://techguide.zeiss.com/en/zeiss-inspect-2023/article/cmd_sys_manage_add_ons.html) for more details.

- [App Editor Layout](#app-editor-layout)
- [Creating a new App](#creating-a-new-app)
- [Entering and Leaving Editing Mode](#entering-and-leaving-editing-mode)
- [Writing Python scripts](#writing-python-scripts)
  * [New Folder or Script](#new-folder-or-script)
  * [Installing Python packages](#installing-python-packages)
  * [Running Python Scripts](#running-python-scripts)
  * [Recording Commands](#recording-commands)
  * [Inserting Element Values](#inserting-element-values)
- [Adding and Removing Contents](#adding-and-removing-contents)
- [Exporting or Publishing an App](#exporting-or-publishing-an-app)
- [Apps from External Folders](#apps-from-external-folders)
  * [Connecting and Disconnecting External Folders](#connecting-and-disconnecting-external-folders)
  * [Creating Apps in External Folders](#creating-apps-in-external-folders)

## App Editor Layout

![App Editor Layout](assets/01-Add-on_Editor_Intro_v2.png)

1. App Explorer

    The App Explorer shows all installed Apps. The professional version of ZEISS INSPECT already provides some system Apps in the "Installed Apps" section of the App Explorer. You cannot delete or modify these pre-installed Apps. To install additional Apps, use the integrated "Install/Uninstall Apps" dialog or the ZEISS Quality Software Store.
    
2. Available Contents

    The Available Contents section contains all items in your active project, e.g. templates, report styles etc. Add these items by dragging and dropping them to your App in the App Explorer. If you add an item to an App, it is removed from Available Contents.

3. Preview / Editor

    The Preview / Editor section shows the contents of a file depending its file type. If the selected App is in editing mode, App properties or script contents can be edited here.  

## Creating a new App

Create a new App in the following ways:
* By using the "Create App" button in the top-right corner of the App Explorer 
* By using RMB ► Create App on Installed Apps 
* By using RMB ► Create App on a connected external folder
        
A newly created App has the default title "My App". Rename your App in the properties dialog on the right. A blue dot next to the App title indicates that the App is in editing mode.

An new App has a set of default folders and files.

**Default Folders and Files of an App**

![](assets/07-New_Add-on_v2.png)

## Entering and Leaving Editing Mode

Before you can modify an installed App, you must set it to editing mode first. A newly created App is already in editing mode.

Set an App to editing mode
* By using RMB ► Edit on the App root node in the App Explorer or
* By clicking the Edit button in the App properties window.

A blue dot next to the App title indicates that the App is in editing mode.

When you have finished editing the App, you can leave the editing mode
* By using RMB ► Finish Editing on the App root node in the App Explorer or
* By clicking the Finish Editing button in the App properties window.

```{note}
Editing is only finished after all mandatory information has been entered in the App properties dialog.
```

## Writing Python Scripts

### New Folder or Script

Click RMB on the 'scripts' folder of an App (in editing mode) ► New Folder/Script

### Installing Python Packages

Python packages can be installed to the App and the installed python packages are only valid for scripts in the same App. This concept is like in [Conda](https://docs.conda.io/en/latest/) or [VirtualEnv](https://virtualenv.pypa.io/en/latest/). If you click RMB on the 'scripts' folder or 'modules' folder and select ► Install Python Packages..., the dialog for the installation is shown.

* From network
    The package list from network must be separated with a comma. To install the packages of a specific version, write the version after “==”, e.g. `numpy==1.22.0`

    ![](assets/install_network.png)

* From local file system
    Python wheel files (*.whl) can be added or removed.

    ![](assets/install_local.png)

### Running Python Scripts

![](assets/Script_Run.png)

You start or stop script execution with the buttons in the top right corner of the Script Editor.

### Recording Commands

You start or stop recording of commands executed in ZEISS INSPECT by using the Record button in the top right corner of the Script Editor. The recorded commands can be edited afterwards.

### Inserting Element Values

You insert objects from ZEISS INSPECT into your Python script by using RMB ► Insert ►  Element Value in the script editor.

## Adding and Removing Contents

You add contents from the Available Contents section to Apps (in editing mode) by drag and drop. You remove contents from an App by drag and drop to Available Contents. Moving contents between Apps (in editing mode) is also supported.

![](assets/add_on_editor_dnd.gif)

## Exporting or Publishing an App

* Export

    Click RMB on the installed App ► Export: Save the selected App as a .zapp file.

* Publish in Software Store

    Click RMB on the installed App ► Publish in Software Store: Upload the selected App into the Zeiss Quality Software Store. The uploaded App will be queued into the staging area and will be release after approval.
    
    ```{note}
    Publishing an App requires special permission that ZEISS grants upon request.
    ```

## Apps from External Folders

### Connecting and Disconnecting External Folders

![](assets/03-Add-on_External_Folder_v2.png)

External Folder enables the user to run scripts from a selected path. More than one external folders can be added.

* Connecting

    Click RMB in an area of the App Explorer where no object is selected ► Connect External Folder...
    
* Disconnecting

    Click RMB on the external folder you want to delete ► Disconnect...
    
    The External Folder is removed from the App Explorer but its contents remain in the file system.

### Creating Apps in External Folders

* Creating a new App in an external folder
    
    Click RMB on the External Folder ► New App

"Finish Editing" is not available for Apps from external folders, however they can be published, although they are considered still to be work in progress.
