import re

# Read and preprocess input data
ll = [x for x in open('input.txt').read().strip().split('\n\n')]
workflow, parts = ll  # Split into workflow and parts

# Function to extract integers from a string
def extract_integers(s):
    return list(map(int, re.findall(r'\d+', s)))

# Parse parts using the extract_integers function
parts = [extract_integers(line) for line in parts.split("\n")]

# Parse the workflow into a dictionary
workflow = {line.split("{")[0]: line.split("{")[1][:-1] for line in workflow.split("\n")}

# Function to evaluate conditions based on parts and workflow
def evaluate_condition(part, work):
    # Get the conditions associated with the given work
    work_conditions = workflow[work]
    x, m, a, s = part

    # Process each condition in the workflow
    for condition in work_conditions.split(","):
        if condition == "R":
            return False  # Reject the part if the condition is "R"
        if condition == "A":
            return True  # Accept the part if the condition is "A"
        
        # If the condition has no ":" symbol, recursively evaluate it
        if ":" not in condition:
            return evaluate_condition(part, condition)
        
        # Process the condition with ":" to check the expression
        cond = condition.split(":")[0]
        if eval(cond):  # Evaluate the condition
            # If condition leads to rejection or acceptance, return accordingly
            if condition.split(":")[1] == "R":
                return False
            if condition.split(":")[1] == "A":
                return True
            return evaluate_condition(part, condition.split(":")[1])
    
    # Raise an exception if no valid condition was met
    raise Exception(work_conditions)

# Initialize counter for part 1
p1 = 0

# Loop through each part and check if it passes the evaluation
for part in parts:
    if evaluate_condition(part, 'in'):
        p1 += sum(part)  # Add the sum of the part if it passes
print(p1)

# Function to update the range based on conditions
def update_range(ch, gt, val, ranges):
    ch = 'xmas'.index(ch)  # Map the character to its index
    updated_ranges = []

    # Iterate over each range and update it based on the condition
    for rng in ranges:
        rng = list(rng)
        lo, hi = rng[ch]
        
        if gt:  # If greater than, adjust the lower bound
            lo = max(lo, val + 1)
        else:  # If less than, adjust the upper bound
            hi = min(hi, val - 1)

        # If the range becomes invalid, skip it
        if lo > hi:
            continue
        
        rng[ch] = (lo, hi)  # Update the range
        updated_ranges.append(tuple(rng))  # Add the updated range to the list
    
    return updated_ranges

# Function to get acceptance ranges for the outer conditions
def get_acceptance_ranges_outer(work):
    return get_acceptance_ranges_inner(workflow[work].split(","))

# Function to get acceptance ranges for the inner conditions
def get_acceptance_ranges_inner(work):
    condition = work[0]
    
    # Handle base conditions "R" (Reject) and "A" (Accept)
    if condition == "R":
        return []
    if condition == "A":
        return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]  # Default valid range
    
    # If ":" is not present, evaluate the outer condition
    if ":" not in condition:
        return get_acceptance_ranges_outer(condition)

    # Parse the condition and determine if it is greater than or less than
    cond = condition.split(":")[0]
    gt = ">" in cond
    ch = cond[0]
    val = int(cond[2:])
    val_inverted = val + 1 if gt else val - 1

    # Recursively evaluate the ranges based on the condition
    if_true = update_range(ch, gt, val, get_acceptance_ranges_inner([condition.split(":")[1]]))
    if_false = update_range(ch, not gt, val_inverted, get_acceptance_ranges_inner(work[1:]))
    
    return if_true + if_false

# Initialize counter for part 2
p2 = 0

# Loop through the acceptance ranges for 'in' and calculate the result
for rng in get_acceptance_ranges_outer('in'):
    result = 1
    for lo, hi in rng:
        result *= hi - lo + 1  # Multiply the range sizes
    p2 += result  # Add the result to the total
print(p2)
