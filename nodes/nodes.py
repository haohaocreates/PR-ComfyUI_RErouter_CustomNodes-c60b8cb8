#====----REroute_RE----====
class re_reroute:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "MODEL_B": ("MODEL",),
                "CLIP_B": ("CLIP",),
                "VAE_B": ("VAE",),
                "MODEL_R": ("MODEL",),
                "CLIP_R": ("CLIP",),
                "VAE_R": ("VAE",),
                "EM_LAT": ("LATENT",),
                "UPSC": ("UPSCALE_MODEL",),
                "STR_p": ("STRING", {"forceInput": True}),
                "STR_n": ("STRING", {"forceInput": True}),
                "SEED": ("INT", {"forceInput": True}),
                "STP_T": ("INT", {"forceInput": True}),
                "STP_R": ("INT", {"forceInput": True}),
                "STP_U": ("INT", {"forceInput": True})
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "MODEL", "CLIP", "VAE", "LATENT", "UPSCALE_MODEL", "STRING", "STRING", "INT", "INT", "INT", "INT",)
    RETURN_NAMES = ("MODEL_B", "CLIP_B", "VAE_B", "MODEL_R", "CLIP_R", "VAE_R", "EM_LAT", "UPSC", "STR_p", "STR_n", "SEED", "STP_T", "STP_R", "STP_U",)
    FUNCTION = "reroute"
    CATEGORY = "(RE)route"
	
    def reroute(self, MODEL_B, CLIP_B, VAE_B, MODEL_R, CLIP_R, VAE_R, EM_LAT, UPSCALE_MODEL, STR_p, STR_n, SEED, STP_T, STP_R, STP_U):
        return (MODEL_B, CLIP_B, VAE_B, MODEL_R, CLIP_R, VAE_R, EM_LAT, UPSCALE_MODEL, STR_p, STR_n, SEED, STP_T, STP_R, STP_U,)


#====----String_RE----====
class re_string:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"string": ("STRING", {"default": "", "multiline": True})}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "get_string"
    CATEGORY = "(RE)route"

    def get_string(self, string):
        return (string,)        
#====----Int_RE----====
class re_int:     

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "int": ("INT", {"multiline": False, "default": "0"})
                    
                    }
                }

    RETURN_TYPES = ("INT",)
    FUNCTION = "get_int"
    CATEGORY = "(RE)route"

    def get_int(self, int):
        
        return (int,)
