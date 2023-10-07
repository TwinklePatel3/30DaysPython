#                                💻 Exercises: Day 21

#                                  Exercises: Level 1

# 1. Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
# ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# print('Count:', data.count()) # 25
# print('Sum: ', data.sum()) # 744
# print('Min: ', data.min()) # 24
# print('Max: ', data.max()) # 38
# print('Range: ', data.range() # 14
# print('Mean: ', data.mean()) # 30
# print('Median: ', data.median()) # 29
# print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
# print('Standard Deviation: ', data.std()) # 4.2
# print('Variance: ', data.var()) # 17.5
# print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
# # you output should look like this
# print(data.describe())
# Count: 25
# Sum:  744
# Min:  24
# Max:  38
# Range:  14
# Mean:  30
# Median:  29
# Mode:  (26, 5)
# Variance:  17.5
# Standard Deviation:  4.2
# Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]


class Statistics:
    def __init__(self, list_of_items) -> None:
        self.list_of_items = list_of_items

    def count(self):
        return len(self.list_of_items)

    def sum(self):
        return sum(self.list_of_items)

    def min(self):
        return min(self.list_of_items)

    def max(self):
        return max(self.list_of_items)

    def range(self):
        return int(self.max()) - int(self.min())

    def mean(self):
        return self.sum()/self.count()

    def median(self):
        sorted_list = sorted(self.list_of_items)
        middleIndex = int(self.count()/2)
        median = sorted_list[middleIndex] if middleIndex % 2 == 0 else (
            sorted_list[middleIndex-1] + sorted_list[middleIndex])/2
        return median

    def mode(self):
        mode = max(self.list_of_items, key=self.list_of_items.count)
        count = self.list_of_items.count(mode)
        return {"mode": mode, "count": count}

    def var(self):
        variance = 0
        mean = self.mean()
        for item in self.list_of_items:
            variance += (item - mean)**2
        return variance/self.count()

    def std(self):
        return self.var() ** 0.5

    def freq_dist(self):
        dist = [(self.list_of_items.count(
            i)/self.count(), i) for i in set(self.list_of_items)]
        return sorted(dist, reverse=True)

    def describe(self):
        return (f'Count: {self.count()}\nSum: {self.sum()}\nMin: {self.min()} \nMax: {self.max()}\nRange:  {self.range()}\nMean:  {self.mean()}\nMedian:  {self.median()}\nMode:  {self.mode()}\nVariance:  {self.var()}\nStandard Deviation:  {self.std()}\nFrequency Distribution:  {self.freq_dist()}')


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24,
        32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count())  # 25
print('Sum: ', data.sum())  # 744
print('Min: ', data.min())  # 24
print('Max: ', data.max())  # 38
print('Range: ', data.range())  # 14
print('Mean: ', data.mean())  # 30
print('Median: ', data.median())  # 29
print('Mode: ', data.mode())  # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std())  # 4.2
print('Variance: ', data.var())  # 17.5
# [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
print('Frequency Distribution: ', data.freq_dist())
print(data.describe())
