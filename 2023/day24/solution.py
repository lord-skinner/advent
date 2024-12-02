import itertools as it

# Read input data from the file and parse it into a list of tuples
InputList = []
with open("input.txt", "r") as data:
    for line in data:
        # Split position and velocity components
        P, V = line.strip().split(" @ ")
        PX, PY, PZ = map(int, P.split(", "))
        VX, VY, VZ = map(int, V.split(", "))
        NewTuple = (PX, PY, PZ, VX, VY, VZ)
        InputList.append(NewTuple)

# Initialize variables for calculations
NumHails = len(InputList)
one = 0
NumCombos = 0
Min = 200000000000000  # Minimum X position to consider
Max = 400000000000000  # Maximum X position to consider

# Sort the input list for consistent processing
InputList.sort()

# Calculate potential collisions between pairs of hailstones
for A, B in it.combinations(InputList, 2):
    NumCombos += 1
    APX, APY, APZ, AVX, AVY, AVZ = A
    BPX, BPY, BPZ, BVX, BVY, BVZ = B
    
    # Calculate slopes for Y positions based on velocities
    MA = (AVY / AVX) if AVX != 0 else float('inf')
    MB = (BVY / BVX) if BVX != 0 else float('inf')
    
    # Calculate intercepts for Y positions
    CA = APY - (MA * APX)
    CB = BPY - (MB * BPX)
    
    # Skip if slopes are equal (parallel lines)
    if MA == MB:
        continue
    
    # Calculate intersection point in X and corresponding Y position
    XPos = (CB - CA) / (MA - MB)
    YPos = MA * XPos + CA
    
    # Check if the intersection point is valid for both hailstones
    if (XPos < APX and AVX > 0) or (XPos > APX and AVX < 0) or \
       (XPos < BPX and BVX > 0) or (XPos > BPX and BVX < 0):
        continue
    
    # Count valid collisions within specified bounds
    if Min <= XPos <= Max and Min <= YPos <= Max:
        one += 1

# Initialize sets to track potential velocities for each axis
PotentialXSet = None
PotentialYSet = None
PotentialZSet = None

# Calculate potential velocities for each axis based on collisions
for A, B in it.combinations(InputList, 2):
    APX, APY, APZ, AVX, AVY, AVZ = A
    BPX, BPY, BPZ, BVX, BVY, BVZ = B

    # Check for potential matching velocities in the X direction
    if AVX == BVX and abs(AVX) > 100:
        NewXSet = set()
        Difference = BPX - APX
        
        # Find valid velocities that align with the difference in positions
        for v in range(-1000, 1000):
            if v == AVX:
                continue
            if Difference % (v - AVX) == 0:
                NewXSet.add(v)

        # Update potential velocities set for X direction
        PotentialXSet = PotentialXSet.intersection(NewXSet) if PotentialXSet else NewXSet.copy()
    
    # Check for potential matching velocities in the Y direction
    if AVY == BVY and abs(AVY) > 100:
        NewYSet = set()
        Difference = BPY - APY
        
        for v in range(-1000, 1000):
            if v == AVY:
                continue
            if Difference % (v - AVY) == 0:
                NewYSet.add(v)

        PotentialYSet = PotentialYSet.intersection(NewYSet) if PotentialYSet else NewYSet.copy()
    
    # Check for potential matching velocities in the Z direction
    if AVZ == BVZ and abs(AVZ) > 100:
        NewZSet = set()
        Difference = BPZ - APZ
        
        for v in range(-1000, 1000):
            if v == AVZ:
                continue
            if Difference % (v - AVZ) == 0:
                NewZSet.add(v)

        PotentialZSet = PotentialZSet.intersection(NewZSet) if PotentialZSet else NewZSet.copy()


# Extract one velocity from each potential set to calculate final positions
RVX, RVY, RVZ = PotentialXSet.pop(), PotentialYSet.pop(), PotentialZSet.pop()

# Calculate final positions based on selected velocities from the first two hailstones
APX, APY, APZ, AVX, AVY, AVZ = InputList[0]
BPX, BPY, BPZ, BVX, BVY, BVZ = InputList[1]

MA = (AVY - RVY) / (AVX - RVX)
MB = (BVY - RVY) / (BVX - RVX)
CA = APY - (MA * APX)
CB = BPY - (MB * BPX)

# Calculate intersection point and corresponding Z position at that time
XPos = int((CB - CA) / (MA - MB))
YPos = int(MA * XPos + CA)
Time = (XPos - APX) // (AVX - RVX)
ZPos = APZ + (AVZ - RVZ) * Time

# Print final positions and answers for both parts of the problem 

two = XPos + YPos + ZPos

print(one)
print(two)