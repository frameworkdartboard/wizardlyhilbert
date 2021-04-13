# wizardlyhilbert.py
#
# Draws the space filling curve known as the Hilbert Curve.
# The more iterations you request, the bigger the curve.
# The base case is a single character.

current_curve = [["#"]]
num_iters = 4
DEBUG = False

def create_middle_column(source_curve):
    middle_column = [[" "] for ii in range(len(source_curve))]
    middle_column[len(middle_column) - 1] = ["#"]
    return middle_column

def create_empty_column(source_curve):
    empty_column = [[" "] for ii in range(len(source_curve))]
    return empty_column

def join_left_array_to_right(left_array,right_array):
    if len(left_array) != len(right_array):
        print ("ERROR: len(left_array) != len(right_array)")
        return []
    
    new_array = []
    for ii in range(len(left_array)):
        new_row = left_array[ii] + right_array[ii]
        new_array.append(new_row)
    return new_array

def create_middle_row(source_curve):
    middle_row = list(" " for ii in range(len(source_curve[0])))
    middle_row[0] = "#"
    middle_row[len(middle_row) - 1] = "#"
    return [middle_row]

def join_top_array_to_bottom_array(top_array,bottom_array):
    new_array = top_array + bottom_array
    return new_array

def rotate_curve_90(source_array):
    num_rows = len(source_array)
    new_array=[[] for ii in range(num_rows)]
    for source_row in source_array:
        for jj in range(num_rows):
            new_array[jj].insert(0,source_row[jj])
    return new_array

def reflect_curve_vertically(source_array):
    new_array = []
    for source_row in source_array:
        reverse_row = source_row
        reverse_row.reverse()
        new_array.append(reverse_row)
    return new_array

def render_curve(curve):
    printable_rows = ["%s" % "".join(ii) for ii in curve]
    rendered_curve = "\n".join(printable_rows)
    print ("%s" % rendered_curve)

# main
for ii in range(num_iters):
    middle_column = create_middle_column(current_curve)
    new_curve = join_left_array_to_right(current_curve,middle_column)
    temp_curve = new_curve
    new_curve = join_left_array_to_right(temp_curve,current_curve)
    middle_row = create_middle_row(new_curve)
    temp_curve = new_curve
    new_curve = join_top_array_to_bottom_array(temp_curve,middle_row)
    current_curve_rotated_90 = rotate_curve_90(current_curve)
    empty_column = create_empty_column(current_curve)
    lower_new_curve = join_left_array_to_right(current_curve_rotated_90,empty_column)
    reflected_rotated_curve = reflect_curve_vertically(current_curve_rotated_90)
    lower_temp_curve = lower_new_curve
    lower_new_curve = join_left_array_to_right(lower_temp_curve,reflected_rotated_curve)
    temp_curve = new_curve
    new_curve = join_top_array_to_bottom_array(temp_curve,lower_new_curve)
    current_curve = new_curve

render_curve(current_curve)
    
