


def get_flow(args):
    if hasattr(args, 'webui_online_type'):
        if args.webui_online_type == "Natural":
            from .Online_Web_CoT_Natural import OnlinePlan
            return OnlinePlan
        if args.webui_online_type == "MergeNoDes":
            from .Online_Web_CoT_MergeNoDes import OnlinePlan
            return OnlinePlan
        if args.webui_online_type == "NoCoT":
            from .Online_Web_NoCoT import OnlinePlan
            return OnlinePlan
        if args.webui_online_type == "NoIMG":
            from .Online_Web_CoT_NoImg import OnlinePlan
            return OnlinePlan

    typ = (args.env, args.flow_type, args.Human_Knowledge)
    if typ == ("Sokoban", "Online", False) or typ == ("Football", "Online", False):
        from .Online_HL_FBandSB import OnlinePlan
        return OnlinePlan
    elif typ == ("WebUI", "Global", False) or typ == ("Sokoban", "Global", False):
        from .GlobalPlanning import GlobalPlan
        return GlobalPlan
    else:
        raise NotImplementedError("error environment or flow type")

