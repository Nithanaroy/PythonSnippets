# Complete the function below.


def computeAverages(numbers):
    l = len(numbers)
    mean = sum(numbers) / l
    numbers.sort()
    if l % 2 == 0:
        median = (numbers[l / 2] + numbers[l / 2 - 1]) / 2
    else:
        median = numbers[l / 2]
    return [round(mean, 2), round(median, 2)]


if __name__ == '__main__':
    print computeAverages([4.0, 1.0, 2.0, 3.0, 4.0, 5.0])
