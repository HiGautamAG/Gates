#OR gate  0 0 = 0, 0 1 = 1, 1 0 = 1, 1 1 = 1

def or_gate(input1, input2):
    return input1 or input2


# Test the OR gate
input1 = True
input2 = False

output = or_gate(input1, input2)
print(f"OR Gate Output for {input1} OR {input2} is {output}")

# Test different combinations
print(f"OR Gate Output for True OR True is {or_gate(True, True)}")
print(f"OR Gate Output for True OR False is {or_gate(True, False)}")
print(f"OR Gate Output for False OR True is {or_gate(False, True)}")
print(f"OR Gate Output for False OR False is {or_gate(False, False)}")
