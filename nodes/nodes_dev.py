#====----Test1_DEV----====
class test1:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "RE_tuple": ("RE_TUPLE",),
                "STP_T": ("INT", {"forceInput": True}),
                "STP_R": ("INT", {"forceInput": True}),
                "STP_U": ("INT", {"forceInput": True})

            }
        }

    RETURN_TYPES = ("RE_TUPLE","INT", "INT", "INT",)
    RETURN_NAMES = ("RE_tuple","STP_T", "STP_R", "STP_U",)
    FUNCTION = "reroute"
    CATEGORY = "(RE)route"
	
    def reroute(self, RE_tuple, STP_T, STP_R, STP_U):
        return ((STP_T, STP_R, STP_U), STP_T, STP_R, STP_U,)
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
