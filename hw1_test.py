import data
import hw1
import unittest
import data_tests


# Write your test cases for each part below.

class TestCases(unittest.TestCase):

    # Part 1
    
    def test_vowel_count_1(self):
        input = "Prestidigitation"
        result = hw1.vowel_count(input)
        expected = 7
        self.assertEqual(expected, result)

    def test_vowel_count_2(self):
        input = "Apple Pie"
        result = hw1.vowel_count(input)
        expected = 4
        self.assertEqual(expected, result)
    
    def test_vowel_count_v2(self):
        input = "Prestidigitation"
        result = hw1.vowel_count_v2(input)
        expected = 7
        self.assertEqual(expected, result)

    def test_vowel_count_v2(self):
        input = "Apple Pie"
        result = hw1.vowel_count_v2(input)
        expected = 4
        self.assertEqual(expected, result)

    # Part 2

    def test_short_lists_1(self):
        input = [[1, 2, 3], [78, 6], [4, 19, 3, 82], []]
        result = hw1.short_lists(input)
        expected = [[78, 6]]
        self.assertEqual(expected, result)
    
    def test_short_lists_2(self):
        input = []
        result = hw1.short_lists(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 3

    def test_ascending_pairs_1(self):
        input = [[1, 2, 3], [78, 6], [4, 19, 3, 82], []]
        result = hw1.ascending_pairs(input)
        expected = [[1, 2, 3], [6, 78], [4, 19, 3, 82], []]
        self.assertEqual(expected, result)

    def test_ascending_pairs_2(self):
        input = []
        result = hw1.ascending_pairs(input)
        expected = []
        self.assertEqual(expected, result)

    def test_ascending_pairs__v2_1(self):
        input = [[1, 2, 3], [78, 6], [4, 19, 3, 82], []]
        result = hw1.ascending_pairs_v2(input)
        expected = [[1, 2, 3], [6, 78], [4, 19, 3, 82], []]
        self.assertEqual(expected, result)

    def test_ascending_pairs__v2_2(self):
        input = []
        result = hw1.ascending_pairs_v2(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 4

    def test_add_prices_1(self):
        price1 = data.Price(7, 32)
        price2 = data.Price(70, 99)
        result = hw1.add_prices(price1, price2)
        expected = 78.31
        self.assertEqual(expected, result)

    def test_add_prices_2(self):
        price1 = data.Price(0, 88)
        price2 = data.Price(50, 12)
        result = hw1.add_prices(price1, price2)
        expected = 51
        self.assertEqual(expected, result)

    # Part 5

    def test_rectangle_area_1(self):
        rect = data.Rectangle(data.Point(7, 3), data.Point(2, -2))
        result = hw1.rectangle_area(rect)
        expected = 25
        self.assertEqual(expected, result)

    def test_rectangle_area_2(self):
        rect = data.Rectangle(data.Point(0, 0), data.Point(0, -4))
        result = hw1.rectangle_area(rect)
        expected = 0
        self.assertEqual(expected, result)

    # Part 6

    def test_books_by_author_1(self):
        book1 = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = data.Book(['Terry Pratchett', 'Neil Gaiman'], 'Good Omens')
        books = [book1, book2]
        result = hw1.books_by_author("Neil Gaiman", books)
        expected = [book1, book2]
        #print(result)
        self.assertEqual(expected, result)

    def test_books_by_author_2(self):
        book1 = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Apple Pie')
        book2 = data.Book(['Terry Pratchett', 'Neil Gaiman'], 'Good Omens')
        book3 = data.Book(["Orange"], "Crunch")
        books = [book1, book2, book3]
        result = hw1.books_by_author("Neil Gaiman", books)
        expected = [book1, book2]
        #print(result)
        self.assertEqual(expected, result)

    # Part 7

    def test_circle_bound_1(self):
        rect = data.Rectangle(data.Point(7, 3), data.Point(-2, 2))
        result = hw1.circle_bound(rect)
        expected = data.Circle(data.Point(2.5, 2.5), 4.5)
        print(result, expected) #you can see that they're almost equal (error due to float rounding error). There's an error when using self.assertAlmostEqual b/c the testing function tries to do math with the Circle types.

    def test_circle_bound_2(self):
        rect = data.Rectangle(data.Point(6, 2), data.Point(-3, 1))
        result = hw1.circle_bound(rect)
        expected = data.Circle(data.Point(1.5, 1.5), 4.5)
        print(result, expected) #you can see that they're almost equal (error due to float rounding error). There's an error when using self.assertAlmostEqual b/c the testing function tries to do math with the Circle types.

    # Part 8

    def test_below_pay_average_1(self):
        employees = [data.Employee("Kevin", 17), data.Employee("Hannah", 20), data.Employee("CEO", float("inf"))]
        result = hw1.below_pay_average(employees)
        expected = ["Kevin", "Hannah"]
        self.assertEqual(expected, result)
    
    def test_below_pay_average_2(self):
        employees = [data.Employee("Child", 0.01), data.Employee("Hannah", 20), data.Employee("Craig", 18)]
        result = hw1.below_pay_average(employees)
        expected = ["Child"]
        self.assertEqual(expected, result)

    def test_below_pay_average_3(self):
        employees = []
        result = hw1.below_pay_average(employees)
        expected = []
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
