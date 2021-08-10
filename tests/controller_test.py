import __init__paths

import ai2thor.controller
import ai2thor.fifo_server
import ai2thor.wsgi_server

controller = ai2thor.controller.Controller(local_executable_path = '/home/ruinian/IVALab/Project/TaskGrounding/ai2thor/unity/builds/thor-Linux64-local/thor-Linux64-local',
                                           scene="FloorPlan1",
                                           # image modalities
                                           renderDepthImage=True,
                                           renderInstanceSegmentation=True,
                                           # camera properties
                                           width=640,
                                           height=480)