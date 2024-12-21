import argparse
import json
import numpy as np


def get_matrix(str_json: str):
    clusters = [c if isinstance(c, list) else [c] for c in json.loads(str_json)]
    n = sum(len(cluster) for cluster in clusters)

    matrix = np.ones((n,n), dtype=int)

    worse = []
    for cluster in clusters:
        for worse_element in worse:
            for element in cluster:
                matrix[element - 1][worse_element - 1] = 0
        for element in cluster:
            worse.append(int(element))

    return matrix

def get_clusters(matrix):
    clusters = []

    n = len(matrix)

    for i in range(0, n):
        for j in range(i+1, n):
            if matrix[i][j] == 0 and matrix[j][i] == 0:
                pair = sorted([i + 1, j + 1])
                if pair not in clusters:
                    clusters.append(pair)
    final_result = [pair[0] if len(pair) == 1 else pair for pair in clusters]
    return str(final_result)


def task(string1:str , string2:str):
    matrix1 = get_matrix(string1)
    matrix2 = get_matrix(string2)

    matrix_and = np.multiply(matrix1, matrix2)
    matrix_and_t = np.multiply(np.transpose(matrix1), np.transpose(matrix2))

    matrix_or = np.maximum(matrix_and, matrix_and_t)
    clusters = get_clusters(matrix_or)
    return clusters

def find_sublists(array_str):
    array = json.loads(array_str)
    sublists = [element for element in array if isinstance(element, list)]
    return sublists


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file1", type=str)
    parser.add_argument("file2", type=str)
    args = parser.parse_args()
    with open(args.file1, "r") as f1:
        string1 = f1.read().strip()

    with open(args.file2, "r") as f2:
        string2 = f2.read().strip()

    clusters = task(string1, string2)
    results = find_sublists(clusters)
    print(results)