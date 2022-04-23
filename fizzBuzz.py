import pandas as pd

import unittest


class Test(unittest.TestCase):
    def test_simple(self):
        """ Test a simple example with 15 rows
        """
        df = pd.DataFrame({"number": list(range(1, 16))})
        fb = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", 
              "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
        expected = pd.DataFrame({"number": list(range(1, 16)), "fizz_buzz": fb})
        actual = add_fizz_buzz_column(df)
        pd.testing.assert_frame_equal(actual, expected)

    def test_non_sequential(self):
        """ Test an example with a few non-sequential rows
        """
        df = pd.DataFrame({"number": [11, 15, 570]})
        expected = pd.DataFrame({"number": [11, 15, 570], 
                                 "fizz_buzz": [11, "FizzBuzz", "FizzBuzz"]})
        actual = add_fizz_buzz_column(df)
        pd.testing.assert_frame_equal(actual, expected)

def fizzBuzz(n):
    """ Return a string representing the Fizz Buzz value for `n`.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

def add_fizz_buzz_column(df):
    """ Return a dataframe with a new column added to `df` 
        titled "fizz_buzz" representing the Fizz Buzz value 
        for every number in the existing "number" column.
    """
    df["fizz_buzz"] = df["number"].apply(fizzBuzz)	
    return df

#Run the tests
if __name__ == "__main__":
    unittest.main()
