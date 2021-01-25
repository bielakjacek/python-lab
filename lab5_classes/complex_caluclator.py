from complex_class import ComplexNumber

operation = input("With operation would you like to perform?\n1. add\n2. subtract\n3. abs\n4. multiplication\n5. "
                  "conjugat\n[Enter number and press Enter:]")


r1 = input("\nEnter first number real part:\n")
i1 = input("\nEnter first number imaginary part:\n")
a = ComplexNumber(float(r1), float(i1))

if operation != "3" and operation != "5":
    r2 = float(input("\nEnter second number real part:\n"))
    i2 = float(input("\nEnter second number imaginary part:\n"))
    b = ComplexNumber(float(r2), float(i2))

if operation == "1":
    print([a.add(b).r, a.add(b).i] )
elif operation == "2":
    print([a.subtract(b).r, a.subtract(b).i])
elif operation == "3":
    print(a.abs())
elif operation == "4":
    print([a.multiplication(b).r, a.multiplication(b).i])
elif operation == "5":
    print([a.conjugate().r, a.conjugate().i])
