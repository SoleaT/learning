from average import AverageGenerator, AverageComparator

if __name__ == '__main__':
    print(avg1 := AverageGenerator(8, 1, 100))
    print(avg2 := AverageGenerator(3, 1, 50))
    print(AverageComparator.avg_compare(avg1.average, avg2.average))
    print(AverageComparator.avg_compare(avg2.average, avg1.average))
    print(AverageComparator.avg_compare(avg1.average, avg1.average))
