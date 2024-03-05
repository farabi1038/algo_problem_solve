
#Staircase traversal or how to reach a staircase in a given max count

def staircaseTraversal(height, maxSteps):
    # Return the result from ways to the caller
    return ways(height, maxSteps)
    
def ways(height, maxSteps):
    if height <= 1:
        return 1
    numWays = 0
    for i in range(1, min(maxSteps,height) + 1):
        # Debug print before recursive call
        print(f"Before: Height={height-i}, NumWays={numWays}")
        numWays += ways(height - i, maxSteps)
        # Debug print after recursive call
        print(f"After: Height={height-i}, NumWays={numWays}")
        print("----")
    return numWays

# Example usage
height = 4  # Height of the staircase
maxSteps = 2  # Maximum steps you can climb at once
result = staircaseTraversal(height, maxSteps)
print(f"Total ways to traverse {height} steps with max {maxSteps} steps at a time: {result}")
