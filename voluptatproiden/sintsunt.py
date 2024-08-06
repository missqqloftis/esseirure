def calculate_sine(radian):
    if not isinstance(radian, (int, float)):
        raise TypeError("Input must be an integer or float")
    
    return math.sin(radian)
