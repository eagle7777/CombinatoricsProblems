#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/7/18


"""
Алгоритм Крускала изначально помещает каждую вершину в своё дерево, а затем постепенно объединяет эти деревья,
объединяя на каждой итерации два некоторых дерева некоторым ребром. Перед началом выполнения алгоритма,
все рёбра сортируются по весу (в порядке неубывания). Затем начинается процесс объединения: перебираются все
рёбра от первого до последнего (в порядке сортировки), и если у текущего ребра его концы принадлежат разным
поддеревьям, то эти поддеревья объединяются, а ребро добавляется к ответу. По окончании перебора всех рёбер
все вершины окажутся принадлежащими одному поддереву, и ответ найден.
"""

parent = {}  # словарь вершмни
rank = {}  # словарь весов


def make_set(vertice):
    """
    добавляет веришну в словари
    :param vertice: вершниа
    :return:
    """
    parent[vertice] = vertice
    rank[vertice] = 0


def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


def union(vertice1, vertice2):
    """
    объеденяет поддеревья
    :param vertice1:
    :param vertice2:
    :return:
    """
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def kruskal(graph):
    """
    алгоритм Крускала
    :param graph: граф
    :return:
    """
    minimum_spanning_tree = set()  # инициализируем минимальное остовное дерево
    edges = list(graph['edges'])  # список ребер - кортежи (вес, первая вершина, вторая вершина)
    edges.sort()
    for vertice in graph['vertices']:  # добавляем вершины в граф
        make_set(vertice)
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return sorted(minimum_spanning_tree)


if __name__ == '__main__':
    l = [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (15, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F'),
    ]
    graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'edges': set(l)
    }
    print(kruskal(graph))
