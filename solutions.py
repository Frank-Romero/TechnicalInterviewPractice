# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring
# of s. For example: if s = "udacity" and t = "ad", then the function returns
# True. Your function definition should look like: question1(s, t) and return
# a boolean True or False.


def question1(s, t):
    if len(s) < len(t):
        return False
    dict_t = {}
    for x in range(97, 123):
        dict_t[chr(x)] = t.count(chr(x))
    for x in range(len(s) - len(t) + 1):
        bool_has = True
        for i in range(97, 123):
           if dict_t[chr(i)] > s[x:x+len(t)].count(chr(i)):
              bool_has = False
              break
        if bool_has:
           return True


print "Q 1"
print "test1: Is some anagram of 'ad' a substring of 'udacity'?",
print question1('udacity', 'ad')
print "test2: Is some anagram of '' a substring of 'udacity'?",
print question1('udacity', '')
print "test3: Is some anagram of 'yudacitryaya' a substring of 'ayayrticadu'?",
print question1('ayayrticadu', 'yudacitryaya')
print "test4"
print question1('stackoverflow', 'sw')
print "test5"
print question1('stackoverflow', 'ckoverf')
print "test6"
print question1('stackoverflow', 'frevokc')



# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.

def expand_center(s, l_index, r_index):
    (left, right) = (l_index, r_index)
    i = len(s) - 1
    while left >= 0 and right <= i and s[left] == s[right]:
        left -= 1
        right += 1
    return (left, right)


def question2(a):
    i = len(a)
    if i == 0:
        return ""
    p_l_index = 0
    p_r_index = 1
    for x in xrange(0, i - 1):
        (l, r) = expand_center(a, x, x)
        if r - l - 1 > p_r_index - p_l_index:
            p_r_index = r
            p_l_index = l + 1
        (l, r) = expand_center(a, x, x + 1)
        if r - l - 1 > p_r_index - p_l_index:
            p_r_index = r
            p_l_index = l + 1

    return a[p_l_index:p_r_index]


print "Q 2"
print "test1: What is the longest palindromic substring in 'abccbccbaa'?",
print question2('abccbccbaa')
print "test2: What is the longest palindromic substring in ''?",
print question2('')
print "test2: What is the longest palindromic substring in ",
print "'ayuuyuyuyuyyfdsasduyuuya'?",
print question2('ayuuyuyuyuyyfdsasduyuuya')


# Question 3
# Given an undirected graph G, find the minimum spanning tree within G. A
# minimum spanning tree connects all vertices in a graph with the smallest
# possible total weight of edges. Your function should take in and return an
# adjacency list structured like this:
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should
# be question3(G)

def question3(G):
    if type(G) != dict:
        return "Not an adjacency list, please provide correct input!"
    total_edges = len(G) - 1
    if total_edges < 1:
        return G + " The tree has one node. No need to find the mst"
    vertices = G.keys()
    edges = set()
    for i in vertices:
        for x in G[i]:
            if i > x[0]:
                edges.add((x[1], x[0], i))
            elif i < x[0]:
                edges.add((x[1], i, x[0]))
    edges = sorted(list(edges))

    result_edges = []
    vertices = [set(i) for i in vertices]
    for i in edges:
        for x in xrange(len(vertices)):
            if i[1] in vertices[x]:
                index_1 = x
            if i[2] in vertices[x]:
                index_2 = x
        if index_1 < index_2:
            vertices[index_1] = set.union(vertices[index_1],
                    vertices[index_2])
            vertices.pop(index_2)
            result_edges.append(i)
        elif index_1 > index_2:
            vertices[index_2] = set.union(vertices[index_1],
                    vertices[index_2])
            vertices.pop(index_1)
            result_edges.append(i)
        if len(vertices) == 1:
            break

    result = {}
    for x in result_edges:
        if x[1] in result:
            result[x[1]].append((x[2], x[0]))
        else:
            result[x[1]] = [(x[2], x[0])]

        if x[2] in result:
            result[x[2]].append((x[1], x[0]))
        else:
            result[x[2]] = [(x[1], x[0])]
    return result


test = {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
test2 = {'A': [('B', 2)], 'B': [('A', 4), ('C', 2)], 'C': [('A', 2),
         ('B', 5)]}
print "Q 3"
print "test1: What is the MST of \n{'A': [('B', 2)],'B': [('A', 2),('C', 5)],",
print "'C': [('B', 5)]}? \n -"
print question3(test)
print "test2: What is the MST of ''?"
print question3('')
print "test3: What is the MST of \n{'A': [('B', 2)],'B': [('A', 4),('C', 2)],",
print "'C': [('A', 2),('B',5)]}? \n -"
print question3(test2)

# Question 4
# Find the least common ancestor between two nodes on a binary search tree. The
# least common ancestor is the farthest node from the root that is an ancestor
# of both nodes. For example, the root is a common ancestor of all nodes on the
# tree, but if both nodes are descendents of the root's left child, then that
# left child might be the lowest common ancestor. You can assume that both
# are in the tree, and the tree itself adheres to all BST properties. The
# function definition should look like question4(T, r, n1, n2), where T is the
# tree represented as a matrix, where the index of the list is equal to the
# integer stored in that node and a 1 represents a child node, r is a non-
# negative integer representing the root, and n1 and n2 are non-negative
# integers representing the two nodes in no particular order. For example, one
# test case might be
# question4([[0, 1, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [1, 0, 0, 0, 1],
#           [0, 0, 0, 0, 0]],
#          3,
#          1,
#          4)
# and the answer would be 3

Test = [[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0,
        1], [0, 0, 0, 0, 0]]

TestNone = [[0, 0, 0, 0]]

Test2 = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]


def question4(T, r, n1, n2):
    minm_node = min(n1, n2)
    maxm_node = max(n1, n2)
    if r is None:
        return "Root cannot be None"
    if r is n1 or r is n2:
        return r
    while r != None:
        if r >= minm_node and r <= maxm_node:
            return r
        elif r > maxm_node:
            sub = (T[r])[:r + 1]
            r = [i for (i, x) in enumerate(sub) if x == 1][0]
        elif r < minm_node:
            sub = (T[r])[r:]
            r = [i for (i, x) in enumerate(sub) if x == 1][0]


print "Q 4"
print "With root 3, find the LCA between the nodes 1 and 4 in binary search"
print "tree Test"
print Test
print question4(Test, 3, 1, 4)
print "With root None, find the LCA between the nodes in binary search tree"
print "TestNone"
print TestNone
print question4(TestNone, None, 0, 0)
print "With root 0, find the LCA between the nodes 1 and 2 in binary search"
print "tree Test2"
print Test2
print question4(Test2, 0, 1, 2)


# Question5
# Find the element in a singly linked list that's m elements from the end. For
# example, if a linked list has 5 elements, the 3rd element from the end is the
# 3rd element. The function definition should look like question5(ll, m), where
# ll is the first node of a linked list and m is the "mth number from the end".
# You should copy/paste the Node class below to use as a representation of a
# node in the linked list. Return the value of the node at that position.
# class Node(object):
#  def __init__(self, data):
#    self.data = data
#    self.next = None

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def question5(ll, m):
    if m == "":
        return "\nPlease input an integer to find from the end of the list."
    check_circular = ll
    n_1 = ll
    n_2 = ll
    count_end = m
    length = 0
    if count_end is 0:
        n_1 = n_1.next
    else:
        while length < count_end:
            if n_1 is None:
                return "Your input is larger than the linked list!"
            else:
                n_1 = n_1.next
            length += 1
            if n_1 is check_circular:
                return "Your list is circular!"
    while n_1 is not None:
        n_1 = n_1.next
        n_2 = n_2.next
        if n_1 is check_circular:
            return "Your list is circular!"
    return n_2.data


A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
A.next = B
B.next = C
C.next = D
D.next = E

print "Q 5"
print "singly linked list: '1', '2', '3', '4', '5'"
print "test1: What's the value of a node '3' elements away from from the end?",
print question5(A, 3)
print "test2: What is the value of a node '' element away from from the end?",
print question5(A, '')
print "test3: What's the value of a node '11' elements away from from the end?"
print question5(A, 11)
print "test4: What is the value of a node '8' elements away from from the end,"
print "after adding node F that loops back to node A?"
F = Node(6)
E.next = F
F.next = A
print question5(A, 8)
