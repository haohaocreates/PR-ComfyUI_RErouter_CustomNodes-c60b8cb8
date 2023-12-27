from .nodes.nodes import *
from .nodes.nodes_dev import *

NODE_CLASS_MAPPINGS = {
    "String (RE)": re_string,
    "INT (RE)": re_int,
    "Test1 DEV": test1,
    "Test2 DEV": test2,
    }
    
print("\033[34mComfyUI REroute Nodes: \033[92mLoaded\033[0m")
