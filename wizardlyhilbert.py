# wizardlyhilbert.py

current_curve = [[#]]
num_iters = 4

def create_middle_column(source_curve):
    height = len(source_curve)
    middle_column = [[" "] for ii in range(height)]
    middle_column[height - 1] = [#]
    return middle_column
    
def render_curve(source_curve):
    for source_row in source_curve:
        print("".join(source_row))

# main
for ii in range(num_iters):
    # make a column as high as the current curve
    middle_column = create_middle_column(current_curve)
    new_curve = middle_column
    current_curve=new_curve
    
render_curve(current_curve)