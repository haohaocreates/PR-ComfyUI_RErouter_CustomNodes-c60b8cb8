#====----(RE) route_----====
class re_route_pack:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"MODEL": ("MODEL",),
                "CLIP": ("CLIP",),
                "VAE": ("VAE",)},
            
            "optional": {
                "MODEL_R": ("MODEL",),
                "CLIP_R": ("CLIP",),
                "VAE_R": ("VAE",),
                "EMPT_LAT": ("LATENT",),
                "UPSC": ("UPSCALE_MODEL",),
                "PRT_p": ("STRING", {"forceInput": True}),
                "PRT_n": ("STRING", {"forceInput": True}),
                "SEED": ("INT", {"forceInput": True}),
                "INT1": ("INT", {"forceInput": True}),
                "INT2": ("INT", {"forceInput": True}),
                "INT3": ("INT", {"forceInput": True})

    RETURN_TYPES = ("BUS_BASE",)
    RETURN_NAMES = ("bus_",)
    FUNCTION = "re_pack"
    CATEGORY = "(RE)route"
	
    def re_pack(self, MODEL, CLIP, VAE, MODEL_R=None, CLIP_R=None, VAE_R=None, EMPT_LAT=None, UPSC=None, PRT_p=None, PRT_n=None, SEED=None, INT1=None, INT2=None, INT3=None):
        return ((MODEL, CLIP, VAE, MODEL_R, CLIP_R, VAE_R, EMPT_LAT, UPSC, PRT_p, PRT_n, SEED, INT1, INT2, INT3),)

#====----(RE) _route----====
class re_reroute_unpack:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"_bus": ("BUS_BASE",)}}
            
    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "MODEL", "CLIP", "VAE", "LATENT", "UPSCALE_MODEL", "STRING", "STRING", "INT", "INT", "INT", "INT",)
    RETURN_NAMES = ("MODEL", "CLIP", "VAE", "MODEL_R", "CLIP_R", "VAE_R", "EMPT_LAT", "UPSC", "PRT_p", "PRT_n", "SEED", "INT1", "INT2", "INT3",)
    FUNCTION = "re_unpack"
    CATEGORY = "(RE)route"
    
    def re_unpack(self, _bus)
        return (_bus[0], _bus[1], _bus[2], _bus[3], _bus[4], _bus[5], _bus[6], _bus[7], _bus[8], _bus[9], _bus[10], _bus[11], _bus[12], _bus[13],)
