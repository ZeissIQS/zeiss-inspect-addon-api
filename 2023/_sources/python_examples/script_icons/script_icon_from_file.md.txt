# script_icon_from_file

![](menu_icon_lightbg.jpg)


## Short description

This is a small example to show how an icon can be set to a script, whereas the icon itself resides in the add-on as a resource.

```{note}
This example is meant as addition to the information given in how-to: [Adding workspaces to packages - Icon guidelines](../../howtos/adding_workspaces_to_addons/adding_workspaces_to_addons.md#icon-guidelines).
```

## Highlights

Normally, the icon can be set using the "Script properties" dialog accessible by right-click in the Script Editor of the GOM Software.

However, using VS Code or another text editor, the corresponding `.metainfo` files of the scripts can be edited directly. If you have icon files within your add-on, you can directly enter the relative path to the icon in the `"icon"` property.

![](script_icon_from_file.jpg)

If you use this approach, and follow our [icon guidelines](../../howtos/adding_workspaces_to_addons/adding_workspaces_to_addons.md#icon-guidelines), the icons get inverted in dark themes automatically.

![](menu_icon_darkbg.jpg)

## Related

* How-to: [Adding workspaces to packages](../../howtos/adding_workspaces_to_addons/adding_workspaces_to_addons.md)