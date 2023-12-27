#====----Test1_DEV----====
class test1:

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
                "SEED": ("INT", {"forceInput": True})
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "MODEL", "CLIP", "VAE", "LATENT", "UPSCALE_MODEL", "STRING", "STRING", "INT",)
    RETURN_NAMES = ("MODEL_B", "CLIP_B", "VAE_B", "MODEL_R", "CLIP_R", "VAE_R", "EM_LAT", "UPSC", "STR_p", "STR_n", "SEED",)
    FUNCTION = "reroute"
    CATEGORY = "REroute Nodes/Test"
	
    def reroute(self, MODEL_B, CLIP_B, VAE_B, MODEL_R, CLIP_R, VAE_R, EM_LAT, UPSCALE_MODEL, STR_p, STR_n, SEED):
        return (MODEL_B, CLIP_B, VAE_B, MODEL_R, CLIP_R, VAE_R, EM_LAT, UPSCALE_MODEL, STR_p, STR_n, SEED,)
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
