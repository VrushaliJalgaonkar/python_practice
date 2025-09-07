name = "vrushali"
age = 31
print(name) ; print(31)
print(type(name) == str)
print(isinstance(name, str))
print(isinstance(age, float))

def is_adult(age):
    return True if age > 18 else False

print(is_adult(age))
print(name[1:6])

book_1_read = True
book_2_read = False
print(any([book_1_read,book_2_read]))
print(all([book_1_read,book_2_read]))

num1 = 2+3j
num2 = complex(2,3)
print(num2.real,num2.imag)

print(abs(-5.5))
print(round(5.48,1))