# Python API functions

## Basics

```{note}
This document describes the emerging GOM Python API.
```

```{important}
The now preliminary API is currently under heavy development and will change massively in the near future.
```

## Image processing

Image related functions can be used to query images from the measurements of a project. This is not done directly, but via an 'image acquisition' object which acts as a proxy between the image storing data structured and the functions which can be used to process the image data.

Terminology:

* 'point': 3D coordinate in the project.
* 'pixel': 2D coordinate in an image.

### gom.api.project

```{py:function} gom.api.project.get_image_aquisition (measurement, camera, stages)

Generate a list of image acquisition objects which can be used as input for image processing functions.

:API version: 1
:param measurement: Measurement the image is to be queried from
:type  measurement: Reference
:param camera: Identifier for the camera which contributed to the measurement. Valid values are:
               * 'left camera': Left camera in a two camera system or the only existing camera in a single camera system
               * 'right camera': Right camera in a two camera system
               * 'photogrammetry': Photogrammery (TRITOP) camera
:type  camera: str
:param stages: (*Optional*) Indices of the stages for which an image acquisition object is to be generated.
:type  stages: list [int]
:return: List of image acquisition objects which can be used by image processing functions. The number of objects matches the number of stage indices in the stages parameter of the function call.
:rtype: List [Reference]
```

**Example**

```
measurement = gom.app.project.measurement_series['Deformation series'].measurements['D1']
stage = gom.app.project.stages['Stage 1']
point = gom.app.project.actual_elements['Point 1'].coordinate
 
left = gom.api.project.get_image_acquisition (measurement, 'left camera', [stage.index])[0]
right = gom.api.project.get_image_acquisition (measurement, 'right camera', [stage.index])[0]
```

### gom.api.imaging

```{py:function} gom.api.imaging.compute_pixels_from_point (point_and_image_acquisition)

Compute pixel coordinates from point coordinates

:API version: 1
:param point_and_image_acquisition: List of pairs where each entry describes a point coordinate plus the image acquisition object which should be used to compute the matching image pixel.
:type  point_and_image_acquisition: List
:return: List of image pixels where each entry is the result of projecting the point via the associated image acquisition structure into the image. The pixel coordinate system center is located in the upper left corner.
:rtype: List
```

**Example**

```
measurement = gom.app.project.measurement_series['Deformation series'].measurements['D1']
stage = gom.app.project.stages['Stage 1']
point = gom.app.project.actual_elements['Point 1'].coordinate
 
left = gom.api.project.get_image_acquisition (measurement, 'left camera', [stage.index])[0]
right = gom.api.project.get_image_acquisition (measurement, 'right camera', [stage.index])[0]
 
p = gom.api.imaging.compute_pixels_from_point ([(point, left), (point, right)])
 
print (p)
```
```
[gom.Vec2d (1031.582008690226, 1232.4155555222544), gom.Vec2d (1139.886626169376, 1217.975608783256)]
```

```{py:function} gom.api.imaging.compute_point_from_pixels ([[pixel_and_image acquisition]], use_calibration)

Compute point coordinate from pixel coordinates

:API version: 1
:param pixel_and_image_acquisition: List of pairs where each entry describes a pixel image coordinate plus the image acquisition object which should be used to compute the matching point.
:type  pixel_and_image_acquisition: List
:param use_calibration: If set, the information from the calibration is used to compute the point. Project must provide a calibration for that case.
:type  use_calibration: bool
:return: List of lists of (pixel, residuum) where each entry is the result of projecting the point via the associated image acquisition structure into the image. The pixel coordinate system center is located in the upper left corner.
:rtype: List
```

```
measurement = gom.app.project.measurement_series['Deformation 1'].measurements['D1']
stage = gom.app.project.stages[0]
point = gom.app.project.actual_elements['Start Point 1'].coordinate
 
left = gom.api.project.get_image_acquisition (measurement, 'left camera', [stage.index])[0]
 
p = gom.api.imaging.compute_point_from_pixels ([[(gom.Vec2d (10, 10), left)]], False)
 
print (p)
```
```
[[gom.Vec3d (-638.2453100625158, 1627.6169782583584, 0.0), 0.0]]
```

```{py:function} gom.api.imaging.compute_epipolar_line (image_acquisition_1, [pixel_and_image_acquisition]_2, max_distance)

Compute epipolar line coordinates

:API version: 1
:param image_aquisition_1: Handle of the image acquisition the epipolar line should be found in.
:type  image_aquisition_1: List
:param pixel_and_image_aquisition_2: List of pairs where each entry describes a pixel image coordinate plus the image acquisition object which should be used to compute the matching point. The image acquisition object here. is the "other" acquisition providing the pixels used to find the matching epipolar lines in the image_acquisition_1 object.
:type  pixel_and_image_aquisition_2: List
:param max_distance: Maximum search distance in mm.
:type  max_distance: double
:return: List of epipolar line coordinates, each one consisting of a list of image pixels.
:rtype: List
```

```
stage = gom.app.project.stages['Stage 1']
point = gom.app.project.actual_elements['Point 1'].coordinate
 
left = gom.api.project.get_image_acquisition (measurement, 'left camera', [stage.index])[0]
right = gom.api.project.get_image_acquisition (measurement, 'right camera', [stage.index])[0]
 
l = gom.api.imaging.compute_epipolar_line (left, [(gom.Vec2d (1617, 819), right)], 10.0)
 
print (l)
```
```
[[gom.Vec2d (4.752311764226988, 813.7915394509045), gom.Vec2d (10.749371580282741, 813.748887458453), gom.Vec2d (16.73347976996274, 813.706352662515), ...]]
```

## Checks

Functions used to handle checks.

### gom.api.scripted_checks_util

```{py:function} gom.api.scripted_checks_util.is_scalar_checkable (element)

Test if the referenced element is suitable for inspection with a scalar check.

:API version: 1
:param element: Element to be checked
:type  element: Reference
:return: True' if the given element s suitable for inspection with a scalar check.
:rtype: bool
```

```
element = gom.app.project.inspection['Point 1']
state = gom.api.scripted_checks_util.is_scalar_checkable (element)
print (state)
```
```
True
```

```{py:function} gom.api.scripted_checks_util.is_surface_checkable (element)

Test if the referenced element is suitable for inspection with a surface check.

:API version: 1
:param element: Element to be checked
:type  element: Reference
:return: True' if the given element s suitable for inspection with a surface check.
:rtype: bool
```

```
element = gom.app.project.inspection['Point 1']
state = gom.api.scripted_checks_util.is_surface_checkable (element)
print (state)
```
```
True
```

```{py:function} gom.api.scripted_checks_util.is_curve_checkable (element)

Test if the referenced element is suitable for inspection with a curve check.

:API version: 1
:param element: Element to be checked
:type  element: Reference
:return: True' if the given element s suitable for inspection with a curve check.
:rtype: bool
```

```
element = gom.app.project.inspection['Point 1']
state = gom.api.scripted_checks_util.is_curve_checkable (element)
print (state)
```
```
True
```