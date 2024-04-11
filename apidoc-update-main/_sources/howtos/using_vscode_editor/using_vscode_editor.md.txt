# Using Visual Studio Code as an App editor

## Setup

### Installation

1. Installation
   * Install the extension directly from the Visual Studio Code extension tab or from the marketplace. 
   * VSCode version 1.64 or higher is needed for this to work properly.

     ![](assets/extension.png)

2. Configure connection
 
    * Ensure that the python API preferences in ZEISS INSPECT are set up properly 
    
      ![](assets/setup2.png)
      
    * Ensure that the python API settings are correct in VSCode and are matching these in ZEISS INSPECT: 
    
      ![](assets/setup4.png)

### Connecting

1. Have ZEISS INSPECT running as a host
2. In the VSCode status bar, the connection status is displayed:

   ![](assets/connecting1.png)
 
3. Press onto the "Host: Disconnected" status entry to connect to the host application.
4. After the connection has been established,
    * the connection status will reflect that and
    * the ZEISS INSPECT App Explorer content is mirrored and displayed in VSCode:
    
      ![](assets/connecting2.png)

## Editing

### Creating scripts

1. Select 'New GOM script' from the file explorers right mouse menu.
2. Enter unique name for that script.

  ![](assets/editing1.png)


### Executing scripts

1. Select script to execute in the VSCode explorer.
    * The script can either reside in the internal edited Apps folder or be a local file from any other workspace location.
2. Select "Run script in ZEISS INSPECT host" from the editors toolbar
3. The script outputs will be shown in the "debug console".

   ![](assets/editing2.png)

### Recording commands

1. Make sure that your App in is in editing mode
2. Select the script into which you want to record commands for displaying in the editor.
3. In that editor, select "Record commands" from the editor toolbar.
4. Execute commands in the ZEISS INSPECT application
    * The executed commands will be recorded in the currently edited VSCode script.
    * In addition, the "ZEISS INSPECT script commands" subsection of the output tab shows a log of the executed commands.
    
      ![](assets/recording1.png)

5. For recording into a different position of the script, set the cursor to that line first or while recording.
6. Press "Record commands" again to stop command recording.

### Inserting elements

> Elements in ZEISS INSPECT are represented by 'element references' in the script. These are python expressions which, when executed, return a reference to that element.

1. When connected to a ZEISS INSPECT application host, select the 'Elements' in the explorer view.
    * There, all elements in the project are listed.
2. Set editor cursor to the place the element should be into inserted into.
3. Select "Insert element into editor" from the top toolbar of the 'Elements' tab
    * You will get an 'element reference', an expression which, when, executed, returns the element referenced.
    
      ![](assets/inserting_elements.png)

### Inserting keywords

> A keyword is an attribute used to query an element property. Various element attributes are existing depending on the element type.

1. Insert an element reference in the script as mentioned above.
2. After the element reference, press '.' to insert a dot
    * A selection menu opens presenting the available keywords for that element
    
      ![](assets/inserting_keywords.png)

## Debugging

### Start debugging

1. Prepare debugged script as usual by setting breakpoints etc.

   ![](assets/debugging1.png)

2. Start debugger by selecting "Debug script in ZEISS INSPECT host" from the editor toolbar

   ![](assets/debugging2.png)

3. Full VSCode debugging functionality can be used now, including

   ![](assets/debugging3.png)

    * breakpoints and triggered breaks,
    * step over/in/out,
    * tracebacks,
    * variable inspection etc.

## User defined script dialogs

```{note}
User defined script dialogs cannot be edited graphically in VSCode at the moment. Instead, an application based script dialog can be opened. A connection to a running application must be present for that purpose.
```

### Create new user defined script dialog

1. Select "Python API: Insert new user defined script dialog" from the command selector or from the right mouse menu while editing the script into which the dialog should be inserted.

   ![](assets/userdialog1.png)

2. Choose a name for the dialog file which will then be created.

   ![](assets/userdialog2.png)

3. The edited script will contain the necessary dialog commands then and a separate dialog definition file (*.gdlg) has been created.

   ![](assets/userdialog3.png)

4. Select the dialog definition file to open the 

   ![](assets/userdialog4.png)

5. When the script is executed, the user defined script dialog is displayed.

   ![](assets/userdialog5.png)
   
### Edit user defined script dialog

1. Edit script dialog file (*.gdlg) can be edited either in JSON format directly (possible, but not recommended) or by opening the script dialog editor in the connected application:

   ![](assets/userdialog6.png)
   
2. The application will then open the script dialog editor. After closing it again, the edited *.gdlg file will be adapted accordingly.

   ![](assets/userdialog7.png)

```{note}
Due to an unsolved bug, the script editor window might open below the VSCode window or on another display in some multi display settings. There is a hint box as indicator that the script editor windows has been opened at all.

![](assets/userdialog8.png)
```

## FAQ

### Configuration

#### How do I set a shortcut to toggle the recording mode ?

* Select the "Keyboard Shortcuts" properties from the configurations menu:

  ![](assets/toggle_recording_1.png)

* Assign the command "Python API: Toggle command recording" to a key:

  ![](assets/toggle_recording_2.png)

* The 'when' clause determines when the command is available. The correct 'when' clause here ist:

  resourceLangId == python && scriptingHostConnected

* If necessary, existing command bindings to that key can be removed here, too:

  ![](assets/toggle_recording_3.png)

#### How do I set shortcuts for starting the current script in the ZEISS INSPECT host ?

* See above for the general process.
* The relevant commands here are:
  * 'Python API: Run script in ZEISS INSPECT host': Start the script.
  * 'Python API: Debug script in ZEISS INSPECT host': Start the script with debugger attached.
* F9 / CTRL + F9 might be valid keys for that.

### Script editing

#### Can I use local workspaces from disk instead of the application script database for my project ?

* Yes. You can add arbitrary folders to the workspace and edit and starts scripts from right there.
* The edited external folder can be connected to the ZEISS INSPECT App Explorer, so that it can be used from there:

  ![](assets/03-Add-on_External_Folder_v2.png)

### Troubleshooting

#### When using IntelliSense completion, the keyword list stalls

* When using the '.' or a hotkey to access the list of possible completions, a tooltip displays 'Loading...' but nothing happens:

  ![](assets/keyword_list_1.png)

* This bug is caused by the 'Microsoft Python' extension in connection with the script database filesystem.
* There is currently no fix, so disabling this extension is the only way here. This does not affect most python editor features:

  ![](assets/keyword_list_2.png)

#### When starting both the application and a script from within Visual Studio Code, crashes can happen

* This is more a ZEISS internal issue. When developing application code and script code at the same time from the same VSCode instance, this can happen.
* The parallel debugging session (application and scripting) seem to be the problem.
* Workaround: Do not start ZEISS INSPECT application via the VSCode launcher, but e.g. from a command prompt.

