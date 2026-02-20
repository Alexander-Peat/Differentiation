no_variables = 0
no_variables = int(input("Enter the number of variables in the expression: "))
coefficients = [0] * no_variables
powers = [0] * no_variables

for loop in range(no_variables):
    coefficients[loop] = int(input("Coefficient " + str(loop + 1) + ": "))
    powers[loop] = int(input("Power " + str(loop + 1) + ": "))

line = "f(x) = "

for loop in range(no_variables):
    if loop > 0:
        line = line + " + " + str(coefficients[loop]) + "x^" + str(powers[loop])
    else:
        line = line + str(coefficients[loop]) + "x^" + str(powers[loop])

print(line)

def differentiate(coefficients_f, powers_f, no_variables_f):
    for loop in range(no_variables_f):
        if powers_f[loop] > 1:
            coefficients_f[loop] = coefficients_f[loop] * powers_f[loop]
            powers_f[loop] = powers_f[loop] - 1
        elif powers_f[loop] == 1:
            powers_f[loop] = "NO X"
        elif powers_f[loop] == 0:
            powers_f[loop] = "GONE"

    return coefficients_f, powers_f

coefficients, powers = differentiate(coefficients, powers, no_variables)

#print(coefficients)
#print(powers)

new_line = "f'(x) = "

for loop in range(no_variables):
    if loop > 0 and loop != (no_variables - 1):
        new_line = new_line + " + "
    if powers[loop] != "NO X" and powers[loop] != "GONE":
        new_line = new_line + str(coefficients[loop]) + "x^" + str(powers[loop])
    elif powers[loop] == "NO X":
        new_line = new_line + str(coefficients[loop])
    elif powers[loop] == "GONE":
        pass

print(new_line)
