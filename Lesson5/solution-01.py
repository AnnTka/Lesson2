def three_args(var_1, var_2=None, var_3=None):
    if var_1 is not None:
        print(f"var 1 = {var_1}")
    if var_2 is not None:
        print(f"var 2 = {var_2}")
    if var_3 is not None:
        print(f"var 3 = {var_3}")


three_args(None, 1, 3)
