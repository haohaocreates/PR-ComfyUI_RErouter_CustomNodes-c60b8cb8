#====----Test1_DEV----====
class test1:

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "STP_T": ("STRING", {"forceInput": True})
            },
            "optional": {
            "STP_R": ("STRING", {"forceInput": True}),
            "STP_U": ("STRING", {"forceInput": True}),
            "RE_tuple": ("RE_TUPLE",)
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "RE_TUPLE",)
    RETURN_NAMES = ("STP_T", "STP_R", "STP_U","RE_tuple",)
    FUNCTION = "reroute"
    CATEGORY = "(RE)route"
	
    def reroute(self, STP_T, STP_R, STP_U, RE_tuple,):
        return (STP_T, STP_R, STP_U, (STP_T, STP_R, STP_U),)
#====----Test2_DEV----====
class test2:     

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "int": ("INT", {"multiline": False, "default": "0"})
                    
                    }
                }

    RETURN_TYPES = ("INT",)
    FUNCTION = "int"
    CATEGORY = "(RE)route"

    def concatenate_text(self, int):
        
        return (int,)
