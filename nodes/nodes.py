#====----REroute----====
class reroute_rrt:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "MODEL": ("MODEL",),
                "CLIP": ("CLIP",),
                "VAE": ("VAE",),
                "UPSC": ("UPSCALE_MODEL",),
                "STR_p": ("STRING", {"forceInput": True}),
                "STR_n": ("STRING", {"forceInput": True}),
                "SEED": ("INT", {"forceInput": True})
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "UPSCALE_MODEL", "STRING", "STRING", "INT",)
    RETURN_NAMES = ("MODEL", "CLIP", "VAE", "UPSC", "STR_p", "STR_n", "SEED",)
    FUNCTION = "reroute"
    CATEGORY = "REroute Nodes/Test"
	
    def reroute(self, MODEL, CLIP, VAE, UPSCALE_MODEL, STR_p, STR_n, SEED):
        return (MODEL, CLIP, VAE, UPSCALE_MODEL, STR_p, STR_n, SEED,)
#====----String_Input----====
class string_input:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"prompt": ("STRING", {"default": "prompt", "multiline": True})}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "get_value"
    CATEGORY = "REroute Nodes"

    def get_value(self, prompt):
        return (prompt,)        
