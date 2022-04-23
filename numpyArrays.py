from unicodedata import mirrored
import numpy as np
import inspect
import unittest

def select_alternating_columns(a: np.ndarray) -> np.ndarray:
    """ 
    Select alternating columns starting from the 0-th
    index of `a`. `a` will be at least 2 dimensions.
    
    >>> a = np.array([[0, 1, 2],
    ...               [3, 4, 5]])
    >>> select_alternating_columns(a)
    array([[0, 2],
           [3, 5]])
    """
    if a.shape[1]%2 == 0:
        valid_columns = np.array([True if i % 2 == 0 else False for i in range(a.shape[1])])
        return a[:, valid_columns]
    valid_columns = np.array([True if i % 2 == 0 else False for i in range(a.shape[1])])
    return a[:, valid_columns]
  
def popcount_rows(a: np.ndarray) -> np.ndarray:
    """
    Return an array containing the popcount of every row 
    in `a`. `a` is 2d and consists of 0s and 1s only.
    
    >>> a = np.array([[0, 0, 1],
    ...               [0, 0, 0],
    ...               [1, 0, 1],
    ...               [1, 1, 1]])
    >>> popcount_rows(a)
    array([1, 0, 2, 3])
    """
    return np.array([np.sum(row) for row in a])

def remove_all_zero_rows(a: np.ndarray) -> np.ndarray:
    """ 
    Removes any rows that entirely consist of zeros from `a`.
    
    >>> a = np.array([[0, 0, 0],
    ...               [0, 0, 1]])
    >>> remove_all_zero_rows(a)
    array([[0, 0, 1]])
    """
    count_non_zero = np.array([np.sum(row) for row in a])
    return a[count_non_zero != 0]
    
def swap_halves(a: np.ndarray) -> np.ndarray:
    """
    Swaps the front and back halves of `a`, which
    is at least 2 dimensions. If the array's size 
    is odd, includes the middle element as the 
    first element of the back half.
    
    >>> swap_halves(np.array([0, 1, 2, 3]))
    array([2, 3, 0, 1])
    >>> swap_halves(np.array([0, 1, 2]))
    array([1, 2, 0])
    >>> a = np.reshape(range(8), [4, 2])
    >>> a
    array([[0, 1],
           [2, 3],
           [4, 5],
           [6, 7]])
    >>> swap_halves(a)
    array([[4, 5],
           [6, 7],
           [0, 1],
           [2, 3]])
    """
    firs_half = a[:len(a) // 2]
    second_half = a[len(a) // 2:]
    return np.concatenate([second_half, firs_half])
  
def trim_zeros_on_edges_2d(a: np.ndarray) -> np.ndarray:
    """
    Trims zeros around a rectangular 1-delimited section.
    The section delimited by 1s will always be
    rectangular and there is only one such section.
    `a` will be 2d and consist of 0s and 1s only.

    >>> a = np.array([[0, 0, 0, 0, 0, 0],
    ...               [0, 1, 1, 1, 0, 0],
    ...               [0, 1, 0, 1, 0, 0],
    ...               [0, 1, 1, 1, 0, 0],
    ...               [0, 0, 0, 0, 0, 0]])
    >>>
    >>> trim_zeros_on_edges_2d(a)
    array([[1, 1, 1],
           [1, 0, 1],
           [1, 1, 1]])
    """
    #rows with all zeros
    b = np.array([np.sum(row) for row in a])
    zero_columns = np.array([True if i == 0 else False for i in b])
    #columns with all zeros
    c = np.array([np.sum(column) for column in a.T])
    zero_rows = np.array([True if i == 0 else False for i in c])
    #select only rows and columns that are not all zeros
    v = a[~zero_columns, :]
    v = v[:, ~zero_rows]	
    return v

  
def one_hot_encode_1d(a: np.ndarray) -> np.ndarray:
    """ 
    One hot encode every row in `a`. Values of `a` are
    unique positive whole numbers or zero in the range [0-n).

    >>> one_hot_encode_1d(np.array([3, 0, 1, 2]))
    array([[0, 0, 0, 1],
           [1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0]])
    """
    #max value of a
    m = a.max() + 1
    return np.array([[ 1 if i == v else 0 for i in range(m)] for v in a])
  
def make_chessboard(size: int) -> np.ndarray:
    """
    Makes a 2d chessboard pattern with both dimensions 
    equal to `size`. The top-left corner should be 0.
    `size` must be >= 0.
    
    >>> make_chessboard(3)
    array([[0, 1, 0],
           [1, 0, 1],
           [0, 1, 0]])
    >>> make_chessboard(4)
    array([[0, 1, 0, 1],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [1, 0, 1, 0]])
    """
    return np.array([[0 if i % 2 == j % 2 else 1 for j in range(size)] for i in range(size)])
  
def quad(a: np.ndarray) -> np.ndarray:
    """
    Repeat the array horizontally and vertically.
    
    >>> quad(np.array([0, 1]))
    array([[0, 1, 0, 1],
           [0, 1, 0, 1]])
    >>> quad(np.array([[0, 1], [2, 3]]))
    array([[0, 1, 0, 1],
           [2, 3, 2, 3],
           [0, 1, 0, 1],
           [2, 3, 2, 3]])
    """
    return np.tile(a, (2, 2))
  
def reflect_quad(a: np.ndarray) -> np.ndarray:
    """
    Repeat the array horizontally and vertically but
    also flip/mirror/reflect the repeated array around 
    the middle.
    
    >>> reflect_quad(np.array([0, 1, 2]))
    array([[0, 1, 2, 2, 1, 0],
           [0, 1, 2, 2, 1, 0]])
    >>> a = np.array([[0, 1],
    ...               [2, 3]])
    >>> reflect_quad(a)
    array([[0, 1, 1, 0],
           [2, 3, 3, 2],
           [2, 3, 3, 2],
           [0, 1, 1, 0]])
    """
    #flip vertical and join rows
    b = []
    if len(a.shape) > 1:
        b = np.flip(a, 0)
        b = np.concatenate([a, b])
    c = []
    #flip horizontal and join columns
    if a.shape[0] > 1:
        c = np.flip(b, 1)
        c = np.concatenate([b, c], 1)
    return c

def rows_where_bits_set_at_idxes(a: np.ndarray, 
                                 set_idxes: np.ndarray) -> np.ndarray:
    """
    Return a list of indexes of rows with bits 
    set at indexes specified by `set_idxes`.
    
    >>> a = np.array([[1, 0, 1, 0],
    ...               [0, 1, 1, 0],
    ...               [0, 1, 0, 1],
    ...               [0, 1, 1, 1]])
    >>> rows_where_bits_set_at_idxes(a, np.array([1, 3]))
    array([2, 3], dtype=int64)
    """
    return np.array([i for i in range(len(a)) if np.any(a[i, set_idxes])])

 
class Test(unittest.TestCase):
    def test_select_alternating_columns_even(self):
        """ select alternating columns (even length)
        """
        a = np.reshape(np.arange(16), [4, 4])
        actual = select_alternating_columns(a)
        expected = np.array([[0, 2], [4, 6], [8, 10], [12, 14]])
        np.testing.assert_equal(actual, expected)
        
    def test_select_alternating_columns_odd(self):
        """ select alternating columns (odd length)
        """
        a = np.reshape(np.arange(6), [2, 3])
        actual = select_alternating_columns(a)
        expected = np.array([[0, 2], [3, 5]])
        np.testing.assert_equal(actual, expected)
        
    def test_popcount_rows(self):
        """ popcount rows
        """
        a = np.array([[0, 0, 1],   
                      [0, 0, 0],
                      [1, 0, 1],
                      [1, 1, 1]])
        actual = popcount_rows(a)
        expected = np.array([1, 0, 2, 3])
        np.testing.assert_equal(actual, expected)
        
    def test_remove_all_zero_rows(self):
        """ remove all zero rows (integer)
        """
        a = np.array([[0, 0, 0], [0, 0, 1]])
        actual = remove_all_zero_rows(a)
        expected = np.array([[0, 0, 1]])
        np.testing.assert_equal(actual, expected)
        
    def test_remove_all_zero_rows_float(self):
        """ remove all zero rows (float)
        """
        a = np.array([[0., 0., 0.], [0., 0., 1.]])
        actual = remove_all_zero_rows(a)
        expected = np.array([[0., 0., 1.]])
        np.testing.assert_equal(actual, expected)
        
    def test_swap_halves_even(self):
        """ swap halves (even length)
        """
        a = np.arange(8)
        actual = swap_halves(a)
        expected = np.array([4, 5, 6, 7, 0, 1, 2, 3])
        np.testing.assert_equal(actual, expected)
        
    def test_swap_halves_odd(self):
        """ swap halves (odd length)
        """
        a = np.arange(7)
        actual = swap_halves(a)
        expected = np.array([3, 4, 5, 6, 0, 1, 2])
        np.testing.assert_equal(actual, expected)
        
    def test_swap_halves_2d_arr(self):
        """ swap halves (2d array)
        """
        a = np.reshape(np.arange(8), [4, 2])
        actual = swap_halves(a)
        expected = np.array([[4, 5], [6, 7], [0, 1], [2, 3]])
        np.testing.assert_equal(actual, expected)
        
    def test_trim_zeroes_on_edges_2d(self):
        """ trim zeros on edges 2d
        """
        a = np.array([[0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 0, 0],   
                      [0, 1, 0, 1, 0, 0],
                      [0, 1, 1, 1, 0, 0],     
                      [0, 0, 0, 0, 0, 0]])
        expected = np.array([[1, 1, 1],
                             [1, 0, 1],
                             [1, 1, 1]])
        actual = trim_zeros_on_edges_2d(a)
        np.testing.assert_equal(actual, expected)
        
    def test_one_hot_encode_1d(self):
        """ one hot encode 1d
        """
        a = np.array([3, 0, 1, 2])
        expected = np.array([[0, 0, 0, 1],
                             [1, 0, 0, 0],
                             [0, 1, 0, 0],
                             [0, 0, 1, 0]])
        actual = one_hot_encode_1d(a)
        np.testing.assert_equal(actual, expected)
        
    def test_make_chessboard_even(self):
        """ make chessboard (even size)
        """
        expected = np.array([[0, 1, 0, 1],
                             [1, 0, 1, 0],
                             [0, 1, 0, 1],
                             [1, 0, 1, 0]])
        actual = make_chessboard(4)
        np.testing.assert_equal(actual, expected)
        
    def test_make_chessboard_odd(self):
        """ make chessboard (odd size)
        """
        expected = np.array([[0, 1, 0],
                             [1, 0, 1],
                             [0, 1, 0]])
        actual = make_chessboard(3)
        np.testing.assert_equal(actual, expected)
        
    def test_quad(self):
        """ quad 
        """
        a = np.array([0, 1])
        expected = np.array([[0, 1, 0, 1],
                             [0, 1, 0, 1]])
        actual = quad(a)
        np.testing.assert_equal(actual, expected)
        
    def test_quad_larger(self):
        """ quad (larger array)
        """
        a = np.array([[0, 1],
                      [2, 3]])
        expected = np.array([[0, 1, 0, 1],
                             [2, 3, 2, 3],
                             [0, 1, 0, 1],
                             [2, 3, 2, 3]])
        actual = quad(a)
        np.testing.assert_equal(actual, expected)
        
    def test_reflect_quad(self):
        """ reflect quad 
        """
        a = np.array([0, 1, 2])
        expected = np.array([[0, 1, 2, 2, 1, 0],
                             [0, 1, 2, 2, 1, 0]])
        actual = reflect_quad(a)
        np.testing.assert_equal(actual, expected)
        
    def test_reflect_quad_larger(self):
        """ reflect quad (larger array)
        """
        a = np.array([[0, 1],
                      [2, 3]])
        expected = np.array([[0, 1, 1, 0],
                             [2, 3, 3, 2],
                             [2, 3, 3, 2],
                             [0, 1, 1, 0]])
        actual = reflect_quad(a)
        np.testing.assert_equal(actual, expected)
        
    def test_rows_where_bits_set_at_idxes(self):
        """ rows where bits are set at indexes
        """
        a = np.array([[1, 0, 1, 0],
                      [0, 1, 1, 0],
                      [0, 1, 0, 1],
                      [0, 1, 1, 1]])
        expected = np.array([2, 3])
        set_idxes = np.array([1, 3])
        actual = rows_where_bits_set_at_idxes(a, set_idxes)
        np.testing.assert_equal(actual, expected)

test_src = inspect.getsource(Test)
unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: (
    test_src.index(f"def {x}") - test_src.index(f"def {y}")
)

#run tests
if __name__ == "__main__":
    unittest.main()