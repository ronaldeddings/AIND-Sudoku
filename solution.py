import collections

assignments = []

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return



def grid_values(grid):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    assert len(grid) == 81
    values = []
    for item in grid:
        if item == '.':
            values.append('123456789')
        else:
            values.append(item)
    return dict(zip(boxes,values))
    

def eliminate(values):
    """
    Use Elimination constraint propagation technique to eliminate values.
    Input: The sudoku in dictionary form
    Output: Reduced sudoku puzzle in dictionary form
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for value in solved_values:
        for peer in peers[value]:
            values[peer] = values[peer].replace(values[value],"")
    return values

def only_choice(values):
    """
    Use Only Choice constraint propogation technique to reduce values.
    Input: The sudoku in dictionary form
    Output: Reduced sudoku puzzle in dictionary form
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    """
    Iteratively use eliminate and only choice strategy.
    Input: The sudoku in dictionary form
    Output: Reduced sudoku puzzle in dictionary form
    """
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Use the Eliminate Strategy
        values = eliminate(values)
        
        #  Use the Only Choice Strategy
        values = only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    """
    "Using depth-first search and propagation, try all possible values..
    Input: The sudoku in dictionary form
    Output: Reduced sudoku puzzle in dictionary form
    """
    
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt
        
def naked_twins(values):
    """
    "Use naked twins propagation technique to reduce puzzle
    Input: The sudoku in dictionary form
    Output: Reduced sudoku puzzle in dictionary form
    """
    # Iterate through each list of units in unitlist
    for units in unitlist:
        # Retrieve values for each unit in list
        unit_values = [values[value] for value in units]
        # Find all naked twin values
        nt = [item for item, count in collections.Counter(unit_values).items() if count > 1 and len(item)==2]
        
        # If there is not any naked twins move to the next list of units
        if not nt:
            continue
        
        #Iterate through each unit in unitlist
        for unit in units:
            for twin in nt:
                if values[unit] == twin:
                    continue
                #If unit is not a naked twin remove naked twin values
                for val in twin:
                    values[unit] = values[unit].replace(val,"")
    return values


def cross(a,b):
    return [s+t for s in a for t in b]


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = search(grid_values(grid))
    #If puzzle is solved return the values in dictionary form, else return False
    if all(len(values[s]) == 1 for s in boxes):
        return values
    else:
        return False

rows = "ABCDEFGHI"
cols = "123456789"    
boxes = cross(rows,cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(r,x) for r in ("ABC","DEF","GHI") for x in ("123","456","789")]
# diag units for solving diagonal sudoku
diag_units = [[chr(64 + x) + str(x) for x in range(1,10)],[chr(74 - x) + str(x) for x in range(1,10)]]
unitlist = row_units + column_units + square_units + diag_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
