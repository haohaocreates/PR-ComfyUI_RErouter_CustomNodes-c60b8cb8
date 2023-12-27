#====----REroute----====
class reroute_rrt:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "MODEL": ("MODEL",),
                "CLIP": ("CLIP",),
                "VAE": ("VAE",),
                "UPSC": ("UPSCALE_MODEL",)
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "UPSCALE_MODEL",)
    RETURN_NAMES = ("MODEL", "CLIP", "VAE", "UPSC",)
    FUNCTION = "reroute"
    CATEGORY = "1Girl Nodes"

    def reroute(self, MODEL, CLIP, VAE, UPSCALE_MODEL):
	return (MODEL, CLIP, VAE, UPSCALE_MODEL,)
#====----String_Input----====
class string_input:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"prompt": ("STRING", {"default": "prompt", "multiline": True})}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "get_value"
    CATEGORY = "1Girl Nodes"

    def get_value(self, prompt):
        return (prompt,)        
