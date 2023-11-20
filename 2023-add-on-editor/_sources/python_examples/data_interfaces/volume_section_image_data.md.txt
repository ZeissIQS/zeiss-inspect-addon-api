# volume_section_image_data

![](volume_section_image.jpg)

## Short description

This example demonstrates how to access the image data of a volume section.

## Highlights

There are two output formats available.

1. **The raw image data**

   This is essentially the same as getting a slice of the volume. Data type and value are the same as the volume the section belongs to.
   
   `raw_image = np.array (element.data.raw)`
   
2. **The rendered image**
   
   This yields the the image as rendered for the 3D view. 
   
   `rgb_image = np.array (element.data.rgb)`
   
   This image is in RGBA format. Therefore you'll get the array shape of (1, 305, 295, 4). 1 project stage, 305x295 pixels, and 4 pixel values (RGBA).
   You can use this image also for processing with other libraries. The screenshot above shows the image opened with `Pillow`.
   
## Related

* How-to: [Access element properties and data](../../howtos/python_api_introduction/python_api_introduction.md#access-element-properties)