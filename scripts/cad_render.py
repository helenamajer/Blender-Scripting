import bpy
import json
import math
import random
import os

num_renders = 10
radius_min = 3.0
radius_max = 6.0

# Store the existing models before import of new objects
before = set(bpy.context.scene.objects)

# Clear the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.obejct.delete(use_global=False)
