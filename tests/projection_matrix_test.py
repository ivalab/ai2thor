import __init__paths

import ai2thor.controller

controller = ai2thor.controller.Controller(local_executable_path = '/home/ruinian/IVALab/Project/TaskGrounding/ai2thor/unity/builds/thor-Linux64-local/thor-Linux64-local')

controller.reset(scene="FloorPlan1",

                 # image modalities
                 renderDepthImage=True,
                 renderInstanceSegmentation=True,
                 # camera properties
                 width=640,
                 height=480,
                 )

while 1:
    print(controller.last_event.metadata["agent"]["projectionMatrix"])
