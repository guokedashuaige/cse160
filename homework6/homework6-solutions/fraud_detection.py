import utils  # noqa: F401, do not remove if using a Mac
# add your imports BELOW this line
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Your Set of Functions for this assignment goes in here


def extract_election_votes(filename, column_names):
    numbers = pd.read_csv(
        filename, usecols=column_names, thousands=',',
    ).to_numpy().flatten()
    numbers = numbers[~np.isnan(numbers)].astype(int).tolist()
    return numbers


def ones_and_tens_digit_histogram(numbers):
    N = len(numbers) * 2
    histogram = [0] * 10
    for n in numbers:
        nn = n % 100
        ten, one = divmod(nn, 10)
        histogram[ten] += 1 / N
        histogram[one] += 1 / N
    return histogram


def plot_iran_least_digits_histogram(histogram):
    plt.figure(figsize=(7, 5))
    plt.plot([0, 9], [0.1]*2, c='tab:blue', label='ideal')
    plt.plot(histogram, '-', c='tab:orange', label='iran')
    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.title('Distribution of the last two digits in Iranian dataset')
    plt.legend(loc=2)
    plt.savefig('iran-digits.png')


def plot_dist_by_sample_size():
    datasize = [10, 50, 100, 1000, 10000]
    plt.figure(figsize=(7, 5))
    plt.plot([0, 9], [0.1]*2, '-', label='ideal')
    for L in datasize:
        numbers = np.random.randint(0, 100, L)
        histogram = ones_and_tens_digit_histogram(numbers)
        plt.plot(histogram, '-', label=f'{L} random numbers')
    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.title('Distribution of the last two digits in randomly '
              'generated samples')
    plt.legend(loc=0)
    plt.savefig('random-digits.png')


def mean_squared_error(numbers1, numbers2):
    return sum([(i-j)**2 for i, j in zip(numbers1, numbers2)]) / len(numbers1)


def calculate_mse_with_uniform(histogram):
    r = 0.1
    return sum([(i-r)**2 for i in histogram]) / len(histogram)


def compare_iran_mse_to_samples(iran_mse, number_of_iran_datapoints):
    ge_num, l_num, p = compare_mse_to_samples(iran_mse,
                                              number_of_iran_datapoints)
    print(f'2009 Iranian election MSE: {iran_mse}')
    print(f'Quantity of MSEs larger than or equal to the 2009 Iranian election'
          f' MSE: {ge_num}')
    print(f'Quantity of MSEs smaller than the 2009 Iranian election MSE:'
          f' {l_num}')
    print(f'2009 Iranian election null hypothesis rejection level p: {p}\n')


def compare_us_mse_to_samples(us_mse, number_of_us_datapoints):
    ge_num, l_num, p = compare_mse_to_samples(us_mse, number_of_us_datapoints)
    print(f'2008 United States election MSE: {us_mse}')
    print(f'Quantity of MSEs larger than or equal to the 2008 United States'
          f'  election MSE: {ge_num}')
    print(f'Quantity of MSEs smaller than the 2008 United States election MSE:'
          f' {l_num}')
    print(f'2008 United States election null hypothesis rejection level p:'
          f' {p}\n')


def compare_mse_to_samples(mse, number_of_datapoints):
    group_num = 10000
    ge_num = 0
    for i in range(group_num):
        numbers = np.random.randint(0, 100, number_of_datapoints)
        histogram = ones_and_tens_digit_histogram(numbers)
        sample_mse = calculate_mse_with_uniform(histogram)
        if sample_mse >= mse:
            ge_num += 1
    return ge_num, group_num - ge_num, ge_num / group_num

# -------------------------------------------------------------------


def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.

    iran_numbers = extract_election_votes(
        'election-iran-2009.csv',
        ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])
    iran_histogram = ones_and_tens_digit_histogram(iran_numbers)
    # plot_iran_least_digits_histogram(iran_histogram)
    # plot_dist_by_sample_size()
    iran_mse = calculate_mse_with_uniform(iran_histogram)
    number_of_iran_datapoints = len(iran_numbers)
    compare_iran_mse_to_samples(iran_mse, number_of_iran_datapoints)

    us_numbers = extract_election_votes(
        'election-us-2008.csv',
        ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"])
    us_histogram = ones_and_tens_digit_histogram(us_numbers)
    us_mse = calculate_mse_with_uniform(us_histogram)
    number_of_us_datapoints = len(us_numbers)
    compare_us_mse_to_samples(us_mse, number_of_us_datapoints)


if __name__ == "__main__":
    main()
