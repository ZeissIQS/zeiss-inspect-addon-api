---
myst:
   html_meta:
      "description": "Python API for extending ZEISS INSPECT 2025 with Apps - Stages"
      "keywords": "Metrology, ZEISS INSPECT, Python API, GOM API, Scripting, Add-ons, Apps, How-tos, Stages"
---

# Working with stages

> Abstract: Stages are used in ZEISS INSPECT for comparing inspection results of the same nominal part but different actual meshes. In ZEISS INSPECT Correlate, stages are used for 3D image series. This section provides some basic information about using stages in Apps and shows typical applications of Python scripts for working with stages.

Stage reference
: The ZEISS INSPECT internal reference to a stage

Stage index
: Numerical index of a stage

Stage name
: Name of a stage


% Referencing stages by index and by name, iterating over stages
% https://forum.gom.com/topic/3150-how-to-find-last-stageframe-index-used-in-the-project-with-python/
% https://forum.gom.com/topic/377-how-to-show-stage-with-stageindex-in-script/
% https://forum.gom.com/topic/493-iterate-over-stages/
% https://forum.gom.com/topic/3298-the-use-of-python-in-combination-with-stages/

## Referencing stages and iterating over stages

In the following examples, the current project has five stages named 'ZEISS Training Object Mesh 1' to 'ZEISS Training Object Mesh 5'.

```{code-block} python
# Number of stages
print(len(gom.app.project.stages))
# output: 5

# Select stage by name
print(gom.app.project.stages['ZEISS Training Object Mesh 2'])
# output: gom.app.project.stages['ZEISS Training Object Mesh 2']

# Select stage by index
print(gom.app.project.stages[1])
# output: gom.app.project.stages['ZEISS Training Object Mesh 2']

# Reference to last stage
print(gom.app.project.stages[-1])
# output: gom.app.project.stages['ZEISS Training Object Mesh 5']

# Index of stage selected by name
print(gom.app.project.stages['ZEISS Training Object Mesh 2'].index)
# output: 1

# Name of stage selected by index
print(gom.app.project.stages[1].name)
# output: ZEISS Training Object Mesh 2

# Show the specified stage
gom.script.sys.show_stage (stage=gom.app.project.stages[1])

# Basic iteration over all stages (all stages enabled)
for stage in gom.app.project.stages:
    print(f'Stage {stage.index} Name: {stage.name}')

# output:
# Stage 0 Name: ZEISS Training Object Mesh 1
# Stage 1 Name: ZEISS Training Object Mesh 2
# Stage 2 Name: ZEISS Training Object Mesh 3
# Stage 3 Name: ZEISS Training Object Mesh 4
# Stage 4 Name: ZEISS Training Object Mesh 5

# Iteration over selected stages
# Note: 
# The order is always the same as in the timeline, even if the values of `first` and `last` are swapped!
for stage in gom.StageSelection(first=gom.app.project.stages['ZEISS Training Object Mesh 2'],
                                last=gom.app.project.stages['ZEISS Training Object Mesh 4']):
    print(f'Stage {stage.index} Name: {stage.name}')
    
# output:
# Stage 1 Name: ZEISS Training Object Mesh 2
# Stage 2 Name: ZEISS Training Object Mesh 3
# Stage 3 Name: ZEISS Training Object Mesh 4
```

% https://forum.gom.com/topic/80-how-to-access-results-of-surface-point-inspections-within-the-script-faster/
To access element values in a specific stage, you can use the `in_stage` accessor. The following example shows how strain values of a set of points are printed for a set of stages:

```{code-block} python
for i in range(NPOINTS):
    for j in STAGES:
        x_strain = gom.app.project.inspection[f'Point {i+1}.epsX'].in_stage[gom.app.project.stages[j].index].result_dimension
        print(f'Point {i+1}, Stage {j}: {x_strain}')
```

## Setting or modifying timestamps

It is possible to apply timestamps to stages. A common use case are deformation measurements, which are typically performed at a fixed interval.

The following code writes timestamps to all stages:

```{code-block} python
timestamp = 0.0
for stage in gom.app.project.stages:
    # Set the timestamp of each stage to a new value
    gom.script.sys.set_stage_time_stamp(
        stage=stage,
        timestamp=gom.StageTimeStamp(year=2024, month=1, day=29, 
                                     hour=8, minute=30, second=timestamp, millisecond=0))
    timestamp += 1
```

## Reordering stages

% https://forum.gom.com/topic/1348-how-to-change-stages-order-using-python/

Occasionally, stages in the timeline are not in the required order and must be reordered.

Create an array with the stage names in the target order - this is typically done with the built-in Python sorting function `sorted()`.

```{code-block} python
target_list = [
    'ZEISS Training Object Mesh 5',
    'ZEISS Training Object Mesh 4',
    'ZEISS Training Object Mesh 3',
    'ZEISS Training Object Mesh 2',
    'ZEISS Training Object Mesh 1']
```

Use the function `change_stage_order()` to move each stage to the desired position: 

```{code-block} python
for i, stage_name in enumerate(target_list):
    print(f'Moving {stage_name} to index {i}')
    gom.script.sys.change_stage_order(
        stages=gom.StageSelection(first=gom.app.project.stages[stage_name],
                                  last=gom.app.project.stages[stage_name]),
        target=gom.app.project.stages[i])
```

## Related

* <a href="../python_api_introduction/python_api_introduction.html#properties-of-different-stages">ZEISS INSPECT Python API Introduction - Access element properties - Properties of different stages</a>
* <a href="../project_keywords/project_keywords.html#stage-specific-keywords">Project keyword handling - Stage specific keywords</a>
