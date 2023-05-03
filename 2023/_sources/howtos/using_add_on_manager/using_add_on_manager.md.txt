# Using Add-on Manager
Script Editor and Package Manager have been integrated as the Add-on Manager. Here you can write python scripts, add/remove contents, create/edit and publish Add-ons.

## Add-on Manager Formation
![Add-on Manager formation](assets/formation.png)
1. Add-on Explorer

    Installed Add-ons and being edited add-ons are displayed in the explorer.
    
    * Installed
      <br/>All of the installed Add-ons (System, User, Public) are listed and these are not editable. If you click RMB on an installed Add-on, you can select "edit", "uninstall", or "publish" the Add-on.
      
      ![](assets/installed.png)
      
    * Being Edited
      <br/>Being edited Add-ons are in this category listed and you can add or remove contents to them. If you click RMB on a being edited Add-ons, you can select "complete the edit" or "delete".
      
      ![](assets/edited2.png)
    
2. Contents Provider

    Here are contents from the current project which are able to be added to an Add-on. Contents can be moved by dragging and dropping between contents provider and a being edited Add-on. For more information about contents providers, please see the Add-on Format documentation.
    
3. Top of Display

    The name of selected object in Add-on explorer is displayed.
    
4. Tool Bar

    If selected object is a
    
    * Script object
    <br/>Save | Record Run Stop | Collapse/Expand
    
    * Editable object
    <br/>Save
    
    * Others
    <br/>No
        
    Buttons are shown.
    
5. Editor
    
    Content of the selected object are displayed and if it is editable object, you can edit in the editor.
    
6. Output Controller

    The output of the executed script is displayed.

## Creating a new Add-on

1. Click RMB on the header of being edited category or in an area of the Add-on explorer where no object are selected.
2. Click "New Add-on" in context menu.
3. An Add-on being edited will be created, including default folders and files.

~~~
🛈 Default folders and files of an Add-on
~~~

## Writing python scripts
### New folder/script

1. Click RMB on the 'scripts' folder of an Add-on being edited.
2. Select New Folder or New Script.

### Install python packages

Python packages can be installed to the Add-on and the installed python packages are only valid for scripts in the same Add-on. If you click RMB on the 'scripts' folder or 'modules' folder and select 'Install Python Packages...', the dialog for the installation will be popped up.

#### from Network
#### from Local

## Add- and removing contents

## Complting the edit

## Editing an Add-on

## Publishing an Add-on

## Add-ons from External Folder
### Add- and removing External Folder
### Publishing an Add-on from External Folder

