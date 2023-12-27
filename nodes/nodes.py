#====----REroute_RE----====



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
               
        return {"required": {"int": ("INT", {"multiline": False, "default": "0"})}}
                   
    RETURN_TYPES = ("INT",)
    FUNCTION = "get_int"
    CATEGORY = "(RE)route"

    def get_int(self, int):
        
        return (int,)
