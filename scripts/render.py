import bpy
import json
import math
import random
import os

file_path = ""
num_renders = 10
radius_min = 3.0
radius_max = 6.0

# Store the existing models before import of new objects
before = set(bpy.context.scene.objects)

# Clear the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.obejct.delete(use_global=False)

# Import OBJ file
bpy.ops.wm.obj_import(filepath=file_path)

for obj in bpy.context.scene.object:
    print(obj.name, obj.type, obj.location)

# Force dependency graph update
bpy.context.view_layer.update()

# Find newly created objects
after = set(bpy.context.scene.object)
new_objects = list(after - before)

# Deselect everything first
bpy.ops.object.select_all(action='DESELECT')

# Select imported objects
for obj in new_objects:
    obj.select_set(True)

# Make one active object
if new_objects:
    bpy.context.view_layer.objects.active = new_objects[0]

# Try to frame in viewport (needs VEIW_3D context)
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        for region in area.regions:
            if region.type == 'WINDOW':
                override = {
                    'area': area,
                    'region': region,
                    'scene': bpy.context.scene,
                    'screen': bpy.context.screen,
                }
                
                with bpy.context.temp_override(**override):
                    bpy.ops.view3d.view_selected(use_all_regions=False)
                
                break
        break

# Force redraw
for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:
        if area.type == 'VIEW_3D':
            area.tag_redraw()

# Normalize object - bring object to origin
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
obj.location = (0, 0, 0,)

        
