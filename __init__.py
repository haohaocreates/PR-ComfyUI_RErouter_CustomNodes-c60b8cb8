from .nodes.nodes import *
from .nodes.rerouter import *
#from .nodes.nodes_dev import *

NODE_CLASS_MAPPINGS = {
    "(RE) route_": re_route_pack,
    "(RE) _route": re_reroute_unpack,
    "String (RE)": re_string,
    "Int (RE)": re_int
#    "Test1 DEV": test1,
#    "Test2 DEV": test2,
    }
    
print("\033[34mComfyUI REroute Nodes: \033[92mLoaded\033[0m")
