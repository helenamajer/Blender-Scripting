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

