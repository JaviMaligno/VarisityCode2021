# Challenge description
Welcome to the fraud prevention unit! We hare here to catch bad guys and crunch numbers. And we have plenty of both. We are monitoring every transaction that flows through our system. Most of them exhibit one of the usually observed behaviours. Some however are unlike any other we have seen before. Those should be flagged up, and investigated.

A transactions is represented as a 2-dimentional point. We determine which transactions belong in the same group, by the euclidian distance between two points. For any given transaction `T`, find the next closest transaction. The distance between them is `C`. The transaction `T` is similar to all transactions that are no more than `3C` away from it. All transactions in a group must be similar to all other transactions in the group.

Fortunately, using this representation, the bad guys are pretty easy to spot. As a result, all transactions will belong to exactly zero or one groups. Your job is to find the transactions that are not in any groups.

The points are represented as a list of numbers. The first two numbers are the first point, the second two are the second point and so on. You should return the results in the same format, and in the same order as you have received the points.

## Example
Let's consider an example. Given this input:
```
10, 10, -10, -10, 11, 10, -13, -12, 15, 18, 9, 11, -12, -8, -13, -12, -15, -10, 0, -13
```
The transaction points are:
```
(10, 10), (-10, -10), (11, 10), (-13, -12), (15, 18), (9, 11), (-12, -8), (-15, -10), (0, -13)
```
These form two groups:
```
(10, 10), (11, 10), (9, 11)
(-10, -10), (-13, -12), (-12, -8), (-15, -10)
```
And there are two outliers:
```
(15, 18)
(0, -13)
```
As a result, you should return
```
15, 18, 0, -13
```

### Breakdown
A breakdown of a few points to further illustrate the process.

Let's consider the point `(10, 10)`. The closest point to it is `(11, 10)`. Their distance is 1. This means that only points that are within `3 * 1 = 3` of `(10, 10)` are similar to it. The points that are similar to `(10, 10)` are `(11, 10)` and `(9, 11)`. When examined, these two points are also similar to `(10, 10)` and to each other. As a result, they form a group.

Next, consider the point `(0, -13)`. The closest point to it is `(-10, -10)`. Their distance is 10.44. This means that points that are within `3 * 10.44 = 31.32` of `(0, -13)` are similar to it. This is almost all points. However, because the points that `(0, -13)` is similar to are not similar to `(0, -13)` (they are further than `3C` away), it is not in any other clusters.