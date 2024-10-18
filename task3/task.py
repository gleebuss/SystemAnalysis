import argparse
import csv
import math


def read_csv() -> list[list[str]]:
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    args = parser.parse_args()
    with open(args.filepath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        str_csv = list(reader)
    return str_csv


def task(csv_str:  list[list[str]]) -> float:
    answer: float = 0
    n = len(csv_str)

    for i in csv_str:
        for j in i:
            if j != '0':
                value = float(j) / (n - 1)
                answer += -value * math.log2(value)

    return round(answer,1)

def main():
    str_csv = read_csv()
    answer = task(str_csv)
    print(answer)


if __name__ == '__main__':
    main()