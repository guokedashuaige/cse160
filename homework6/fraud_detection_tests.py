import fraud_detection as fd
import math


def test_ones_and_tens_digit_histogram():
    # example from spec
    actual = fd.ones_and_tens_digit_histogram([127, 426, 28, 9, 90])
    expected = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])
    # add more test cases here


# write other test functions here


def main():
    test_ones_and_tens_digit_histogram()
    # call other test functions here


if __name__ == "__main__":
    main()
