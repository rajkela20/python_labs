a_input = input("a: ")
b_input = input("b: ")

a = float(a_input.replace(',' , '.'))
b = float(b_input.replace(',' , '.'))

total = a + b
average = total / 2 

print(f"sum{total:.2f}; avg={average:.2f} ")