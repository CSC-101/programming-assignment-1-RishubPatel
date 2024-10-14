import data

# Write your functions for each part in the space below.

# Part 1

def vowel_count(string:str) -> int: #returns the number of vowels in a given string
    return sum([string.count(vowel) for vowel in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]])

# Part 2

def short_lists(list:list[list[int]]) -> list: #CLARIFY WHAT THIS IS SUPPOSED TO DO BEFORE BUILDING IT
    pass
'''    shorter_list = []
    for i in range(len(list)):
        shorter_list[i//2] = list[i]'''

# Part 3

def ascending_pairs(list:list[list[int]]) -> list: #sorts items of length 2 in a given list of number lists
    return [sorted(lst) if len(lst) == 2 else lst for lst in list]

# Part 4

def add_prices(price1: data.Price, price2: data.Price) -> data.Price: #sums 2 given prices
    return (price1.cents + price2.cents + (100 * price1.dollars) + (100 * price2.dollars))/100

# Part 5

def rectangle_area(rect: data.Rectangle) -> float: #returns the area of a given rectangle
    length = abs(rect.top_left.x - rect.bottom_right.x)
    height = abs(rect.top_left.y - rect.bottom_right.y)
    return length * height

# Part 6

def books_by_author(name: str, books:list[data.Book]) -> list[data.Book]: #returns all books written by a given author from a given list of books
    return [book for book in books if name in book.authors]

# Part 7

def circle_bound(rect: data.Rectangle) -> data.Circle: #returns the smallest bounding circle for a given rectangle
    length = abs(rect.top_left.x - rect.bottom_right.x)
    height = abs(rect.top_left.y - rect.bottom_right.y)
    radius = ((length ** 2 + height **2) ** 0.5)/2
    center_point = data.Point(rect.top_left.x - (length/2), rect.top_left.y - (height/2))
    return data.Circle(center_point, radius)

# Part 8

def below_pay_average(employees: list[data.Employee]) -> list[str]: #returns a list of the employees being paid less than the mean among the employees in the given list
    average = sum([employee.pay_rate for employee in employees])/len(employees)
    return [employee.name for employee in employees if employee.pay_rate < average]
    #TEST FOR EMPTY LIST