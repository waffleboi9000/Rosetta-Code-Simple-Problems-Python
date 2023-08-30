first_string = input("Enter the first integer: ")
second_string = input("Enter the second integer: ")
first_int = int(first_string)
second_int = int(second_string)
sum_int = first_int + second_int
difference_int = first_int - second_int
product_int = first_int * second_int
integer_quotient_int = first_int // second_int
remainder_int = first_int % second_int
exponentiation_int = first_int ** second_int
print("The sum is: " + str(sum_int))
print("The difference is: " + str(difference_int))
print("The product is: " + str(product_int))
print("The integer quotient (rounded down to negative infinity) is: " + str(integer_quotient_int))
print("The remainder is: " + str(remainder_int))
print("The exponentiation is: " + str(exponentiation_int))