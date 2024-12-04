
def get_generator(args):
    typ = args.API_type
    if typ == "HuggingFace":
        from .HF import generate
        return generate
    elif typ == "AzureOpenAI":
        from .AZOAI import generate
        return generate
    elif typ == "Local":
        from .local_model import generate
        return generate
    elif typ == "Gemini":
        from .Gemini import generate
        return generate
    elif typ == "Claude":
        from .Claude import generate
        return generate