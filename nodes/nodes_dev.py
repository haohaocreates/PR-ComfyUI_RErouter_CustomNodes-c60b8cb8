#====----Test1_DEV----====
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
                "STR_n": ("STRING", {"forceInput": True})
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "UPSCALE_MODEL", "STRING", "STRING",)
    RETURN_NAMES = ("MODEL", "CLIP", "VAE", "UPSC", "STR_p", "STR_n",)
    FUNCTION = "reroute"
    CATEGORY = "REroute Nodes/Test"
	
    def reroute(self, MODEL, CLIP, VAE, UPSCALE_MODEL, STR_p, STR_n):
        return (MODEL, CLIP, VAE, UPSCALE_MODEL, STR_p, STR_n,)
#====----Test2_DEV----====
class test2:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "SEED": ("INT", {"forceInput": True})

            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("SEED",)
    FUNCTION = "reroute"
    CATEGORY = "REroute Nodes/Test"

    def reroute(self, SEED):
        return (SEED,)
