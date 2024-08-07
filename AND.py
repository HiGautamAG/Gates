#logic gates AND gate   0 0 = 0, 0 1 = 0, 1 0 = 0, 1 1 = 1


def and_gate(input1, input2):
    return input1 and input2

# Test the AND gate
input1 = True
input2 = False

output = and_gate(input1, input2)
print(f"AND Gate Output for {input1} AND {input2} is {output}")

# Test different combinations
print(f"AND Gate Output for True AND True is {and_gate(True, True)}")
print(f"AND Gate Output for True AND False is {and_gate(True, False)}")
print(f"AND Gate Output for False AND True is {and_gate(False, True)}")
print(f"AND Gate Output for False AND False is {and_gate(False, False)}")

    