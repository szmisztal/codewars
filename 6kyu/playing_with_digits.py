"""Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :

(
�
�
+
�
�
+
1
+
�
�
+
2
+
�
�
+
3
+
.
.
.
)
=
�
∗
�
(a
p
 +b
p+1
 +c
p+2
 +d
p+3
 +...)=n∗k
If it is the case we will return k, if not return -1.

Note: n and p will always be strictly positive integers."""


def dig_pow(n, p):
    n = str(n)
    l = []
    for i in range(len(n)):
        l.append(int(n[i])**(p + i))
    result = sum(l) / int(n)
    return int(result) if result.is_integer() else -1
