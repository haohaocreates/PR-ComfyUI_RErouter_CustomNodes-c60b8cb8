#====----Test_node----====
class test:

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
    CATEGORY = "1Girl Nodes"

    def reroute(self, STR_p):
        return (STR_p,)   
