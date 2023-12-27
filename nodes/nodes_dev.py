#====----Test1_DEV----====
class test1:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "STR_p": ("STRING", {"forceInput": True})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STR_p",)
    FUNCTION = "reroute"
    CATEGORY = "REroute Nodes/Test"

    def reroute(self, STR_p):
        return (STR_p,)
#====----Test2_DEV----====
class test2:

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
    CATEGORY = "REroute Nodes/Test"

    def reroute(self, MODEL, CLIP, VAE, UPSCALE_MODEL):
        return (MODEL, CLIP, VAE, UPSCALE_MODEL,)
