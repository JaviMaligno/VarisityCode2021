# Challenge description

Oh, the cinema. Popcorn and big-screen explosions. Is there anything better? Yes. People consuming entertainment in a safe and controlled manner. That is what's even better.

Now that the cinema has reopened, we need to make sure everyone follows the guidelines and sits at a safe distance from each other. As a result, people no longer get to pick where they sit, instead, we are allocating seats for them. They just specify how many people are in their group.

However, we can't just sit them in any way, we must sit them together, and we must try to maximise their viewing experience. And we must be able to do this for all of our movie theatres. From that one in that closet to the one that is the size of a stadium.

## Instructions 

It is well known that the best seat is the one in the middle of the middle row. Thus, a viewing experience score for any given seat is calculated like this:

`1 + number_of_rows_from_the_middle + number_of_seats_from_the_middle`

So the middle seat in the middle row has a score of 1. A seat that is one row down and one seat to the right has a score of 3. The lower the score, the better.

You are given:

- The number of rows in a theatre. This is always a positive odd number
- The number of seats in each row (same for all rows). This is always a positive odd number
- The number of people in each group that bought a ticket. Each group has at least 1 person

You need to seat everyone in the same group on the same row next to each other. You are not allowed to break groups up. You must also leave at least one gap between each group. Find and return the lowest possible score while seating everyone.

If it is not possible to seat every group, the system must have made an error, and you should return -1.

Let's consider some examples:

Given a 3x3 theatre (3 rows, 3 seats each), and 3 groups: 1, 2, 3, one of the possible optimal seating arrangements is: (numbers mark which group each person belongs to and . marks empty seats)
```
-------
|. 1 .|
|3 3 3|
|2 2 .|
-------
```
In this configuration, the score is (row by row, left to right):
```
--------
|  2+  |
|2+1+2+|
|3+2   |
--------
= 12
```
Here is another example:

Given a 5x5 theatre (5 rows, 5 seats each) and 6 groups: 4, 5, 2, 5, 3, 1, one of the possible optimal seating arrangements is:
```
-----------
|. 3 3 3 .|
|5 5 5 5 5|
|5 5 5 5 5|
|4 4 4 4 .|
|. 2 2 . 1|
-----------
```
Note the one gap in the last row between the two groups.

In this configuration, the score is:
```
------------
|  4+3+4+  |
|4+3+2+3+4+|
|3+2+1+2+3+|
|4+3+2+3+  |
|  4+3+  5 |
------------
= 62
```
But given the same groups in a 7x5 theatre (7 rows, 5 seats each), a possible optimal seating would look like this:

```
-----------
|. . 1 . .|
|. 3 3 3 .|
|5 5 5 5 5|
|5 5 5 5 5|
|4 4 4 4 .|
|. 2 2 . .|
|. . . . .|
-----------
```
Which results in a score:
```
------------
|    4+    |
|  4+3+4+  |
|4+3+2+3+4+|
|3+2+1+2+3+|
|4+3+2+3+  |
|  4+3     |
|          |
------------
= 61
```