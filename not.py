#NOT gate  0 = 1, 1 = 0

def not_gate(input1):
    return not input1

# Test the NOT gate
input1 = True

output = not_gate(input1)

print(f"NOT Gate Output for {input1} is {output}")

# Test different combinations
print(f"NOT Gate Output for True is {not_gate(True)}")
print(f"NOT Gate Output for False is {not_gate(False)}")
# What is the output of this code?