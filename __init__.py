from .nodes.nodes import *
from .nodes.nodes_dev import *

NODE_CLASS_MAPPINGS = {
    "Rrt": reroute_rrt,
    "String Input": string_input,
    "Test DEV": test1,
    "Test2 DEV": test2,
    }
    
print("\033[34mComfyUI 1GirlFanboy Nodes: \033[92mLoaded\033[0m")
