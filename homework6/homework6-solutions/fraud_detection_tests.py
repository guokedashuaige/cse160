import math

import fraud_detection as fd
from utils import assert_equals


def test_ones_and_tens_digit_histogram():
    # example from spec
    actual = fd.ones_and_tens_digit_histogram([127, 426, 28, 9, 90])
    expected = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])
    actual = fd.ones_and_tens_digit_histogram(
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
         1597, 2584, 4181, 6765])
    expected = [0.21428571428571427, 0.14285714285714285, 0.047619047619047616,
                0.11904761904761904, 0.09523809523809523, 0.09523809523809523,
                0.023809523809523808, 0.09523809523809523, 0.11904761904761904,
                0.047619047619047616]
    assert_equals(actual, expected)

    print("😄 make a histogram tests passed")

# write other test functions here


def test_extract_election_votes():
    actual = fd.extract_election_votes(
        'election-iran-2009.csv',
        ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])
    expected = [1131111, 16920, 7246, 837858, 623946, 12199, 21609, 656508,
                325911, 6578, 2319, 302825, 1799255, 51788, 14579, 746697,
                199654, 5221, 7471, 96826, 299357, 7608, 3563, 177268, 3819495,
                147487, 67334, 3371523, 359578, 22689, 4127, 106099, 285984,
                3962, 928, 90363, 2214801, 44809, 13561, 884570, 341104, 4129,
                2478, 113218, 1303129, 139124, 15934, 552636, 444480, 7276,
                2223, 126561, 295177, 4440, 2147, 77754, 450269, 6616, 12504,
                507946, 1758026, 23871, 16277, 706764, 498061, 7978, 2690,
                177542, 422457, 16297, 2314, 148467, 315689, 7140, 13862,
                261772, 1160446, 12016, 4977, 318250, 573568, 11258, 10798,
                374188, 253962, 8542, 4274, 98937, 515211, 5987, 10097, 325806,
                998573, 12022, 7183, 453806, 677829, 14920, 44036, 219156,
                1289257, 19587, 10050, 585373, 572988, 10057, 4675, 190349,
                482990, 7237, 5126, 241988, 765723, 13117, 12032, 218481,
                337178, 8406, 2565, 255799]
    assert_equals(actual, expected)
    actual = fd.extract_election_votes(
        'election-us-2008.csv',
        ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"])[:16]
    expected = [813479, 1266546, 6788, 4991, 4310, 123594, 193841,
                3783, 1589, 1660, 1034707, 1230111, 11301, 12555, 1371, 3406]
    assert_equals(actual, expected)
    actual = fd.extract_election_votes(
        'election-us-2008.csv',
        ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"])[-16:]
    expected = [303857, 397466, 7219, 2465, 2355, 1677211, 1262393,
                17605, 8858, 5072, 4216, 82868, 164958, 2525, 1594, 1192]
    assert_equals(actual, expected)

    print("😄 read and clean election data tests passed")


def test_mean_squared_error():
    nums1 = [1, 4, 9]
    nums2 = [2, 3, 4]
    nums3 = [6, 5, 4]
    assert_equals(fd.mean_squared_error(nums1, nums2), 9)
    assert_equals(fd.mean_squared_error(nums1, nums3), 17)
    assert_equals(fd.mean_squared_error(nums2, nums3), 20/3)

    print("😄 get mean squared error between the lists tests passed")


def test_calculate_mse_with_uniform():
    numbers = fd.extract_election_votes(
        'election-iran-2009.csv',
        ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])
    histogram = fd.ones_and_tens_digit_histogram(numbers)
    mse = fd.calculate_mse_with_uniform(histogram)
    assert_equals(mse, 0.000739583333333)

    print("😄 calculate mean squared error of the given histogram with the"
          " uniform distribution tests passed")

# -------------------------------------------------------------------


def main():
    test_ones_and_tens_digit_histogram()
    # call other test functions here
    test_extract_election_votes()
    test_mean_squared_error()
    test_calculate_mse_with_uniform()

    print("🐮 all tests passed")


if __name__ == "__main__":
    main()
