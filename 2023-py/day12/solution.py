from functools import cache

DAY_NUM = 12  # Day number for the challenge
clue, vals = None, None  # Global variables to hold clue and values

@cache
def calc_clue(clue_off, dig, val_off, current_run):
    """
    Recursively calculates possible configurations based on the current clue character.
    
    Parameters:
    - clue_off: Current index in the clue string.
    - dig: Current character being processed ('.', '#', or '?').
    - val_off: Current index in the values list.
    - current_run: Current count of consecutive characters being processed.

    Returns:
    - Number of valid configurations from this point forward.
    """
    if dig == "E":  # If we reach the end of the clue
        if len(vals) == val_off and current_run == 0:
            return 1  # Found a valid configuration
    
    else:
        if dig == "?":  # If the character is a wildcard
            return (
                calc_clue(clue_off, ".", val_off, current_run) + 
                calc_clue(clue_off, "#", val_off, current_run)
            )
        elif dig == ".":  # If the character is '.'
            if current_run == 0:
                return calc_clue(clue_off + 1, clue[clue_off + 1], val_off, 0)
            elif current_run == vals[val_off]:
                return calc_clue(clue_off + 1, clue[clue_off + 1], val_off + 1, 0)
        else:  # If the character is '#'
            if val_off < len(vals) and current_run < vals[val_off]:
                return calc_clue(clue_off + 1, clue[clue_off + 1], val_off, current_run + 1)
    
    return 0  # No valid configuration found

def calc(log, values, mode):
    """
    Processes each row of input values and calculates total configurations.

    Parameters:
    - log: Function to log results.
    - values: List of input strings containing clues and values.
    - mode: Mode of operation (affects how clues are processed).

    Returns:
    - Total number of valid configurations across all input rows.
    """
    total_count = 0
    global clue, vals

    for row in values:
        clue, vals = row.split(" ")  # Split each row into clue and values
        if mode == 2:  # In mode 2, repeat clues and values
            clue = "?".join([clue] * 5)
            vals = ",".join([vals] * 5)
        vals = tuple(int(x) for x in vals.split(","))  # Convert value strings to integers
        clue += ".E"  # Append end marker to the clue
        calc_clue.cache_clear()  # Clear cache for fresh calculations
        total_count += calc_clue(0, clue[0], 0, 0)  # Start recursive calculation

    return total_count

def run(log, values):
    """
    Executes calculations for both modes and logs results.

    Parameters:
    - log: Function to log results.
    - values: List of input strings containing clues and values.
    """
    log(calc(log, values, 1))   # Calculate for mode 1
    log(calc(log, values, 2))   # Calculate for mode 2

if __name__ == "__main__":
    import sys
    import os
    
    def find_input_file():
        """
        Searches for the input file based on command line arguments or default names.

        Returns:
        - Path to the input file if found; otherwise None.
        """
        for fn in sys.argv[1:] + ["input.txt", f"day_{DAY_NUM:02d}_input.txt"]:
            for dn in [[], ["Puzzles"], ["..", "Puzzles"]]:
                cur = os.path.join(*(dn + [fn]))
                if os.path.isfile(cur): 
                    return cur
        return None
    
    fn = find_input_file() 
    if fn is None: 
        print("Unable to find input file!\nSpecify filename on command line")
        exit(1)

    with open(fn) as f: 
        values = [x.strip("\r\n") for x in f.readlines()]  # Read lines from the input file
    
    run(print, values)   # Execute the main logic with print as logger