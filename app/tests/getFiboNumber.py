
def get_fibo_number(position):
    if position < 2:
        return position
    else:
        return get_fibo_number(position-1) + get_fibo_number(position-2)