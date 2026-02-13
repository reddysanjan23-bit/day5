# task 1 :
def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area, perimeter = calc_rectangle(length, width)

print("Area:", area, "Perimeter:", perimeter)



def power(base, exp):
    return base ** exp


def average(numbers_list):
    return sum(numbers_list) / len(numbers_list)