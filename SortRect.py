def sort_Rect(rect, cols): # cols: width image
    tolerance_factor = 10
    origin = rect
    return ((origin[2] // tolerance_factor) * tolerance_factor) * cols + origin[1]

list_rect = [] # list of rect
list_rect.sort(key=lambda x:sort_Rect(x, im0.shape[1]))