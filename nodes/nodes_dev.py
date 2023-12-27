#====----Test1_DEV----====
class test1:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "RE_tuple": ("RE_TUPLE",),
                "MODEL_B": ("MODEL",),
                "CLIP_B": ("CLIP",),
                "VAE_B": ("VAE",)

            }
        }

    RETURN_TYPES = ("RE_TUPLE","MODEL", "CLIP", "VAE",)
    RETURN_NAMES = ("RE_tuple","MODEL_B", "CLIP_B", "VAE_B",)
    FUNCTION = "reroute"
    CATEGORY = "(RE)route"
	
    def reroute(self, RE_tuple, MODEL_B, CLIP_B, VAE_B,):
        return ((MODEL_B, CLIP_B, VAE_B), MODEL_B, CLIP_B, VAE_B,)
#====----Test2_DEV----====
class test2:     

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "text1": ("STRING", {"multiline": False, "default": "Hello"}),
                    "text2": ("STRING", {"multiline": False, "default": "World"}),
                    }
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concatenate_text"
    CATEGORY = "(RE)route"

    def concatenate_text(self, text1, text2):

        text_out = text1 + " " + text2
        
        return (text_out,)
