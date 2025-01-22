x = 10  # Global variable

def show_global():
    global x
    x=20
    print(f"Global x: {x}")

show_global()  # Output: Global x: 10
print(x)       # Output: 10
