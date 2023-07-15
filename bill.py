# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the values of X and Y
    X, Y = map(int, input().split())

    # Check if Chef has enough money to pay the bill
    if X >= Y:
        print("YES")
    else:
        print("NO")
