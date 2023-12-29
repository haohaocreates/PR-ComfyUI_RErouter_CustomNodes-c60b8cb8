from .nodes.nodes import *
from .nodes.rerouter import *
from .nodes.cliptextencode import *

NODE_CLASS_MAPPINGS = {
    "RErouter =>": re_router_pack,
    "RErouter <=": re_router_unpack,
    "String (RE)": re_string,
    "Int (RE)": re_int,
    "CLIPTextEncode (RE)": CLIPTextEncode,
    "CLIPTextEncodeSDXL (RE)": CLIPTextEncodeSDXL,
    "CLIPTextEncodeSDXLRefiner": CLIPTextEncodeSDXLRefiner

    }
    
