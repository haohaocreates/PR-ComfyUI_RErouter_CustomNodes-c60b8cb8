from .nodes.nodes import *
from .nodes.rerouter import *
#from .nodes.nodes_dev import *

NODE_CLASS_MAPPINGS = {
    "RErouter =>": re_router_pack,
    "RErouter <=": re_router_unpack,
    "String (RE)": re_string,
    "Int (RE)": re_int
#    "Test1 DEV": test1,
#    "Test2 DEV": test2,
    }
    
print("\033[34mComfyUI REroute Nodes: \033[92mLoaded\033[0m")
