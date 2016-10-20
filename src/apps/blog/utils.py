


def validate_params(params_dict = {}):
    """
    Global method for validating mandatory input parameters
    """
    error_msg = []
    status = True
    if params_dict:
        for key, value in params_dict.items():
            if value is None or len(str(value)) == 0:
                status = None
                error_msg.append("Enter Valid {0}".format(key))
    else:
        status = None
        error_msg.append("Enter Valid Parameters")

    return status,error_msg