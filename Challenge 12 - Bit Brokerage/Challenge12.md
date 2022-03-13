# Challenge Description

Here at Michael Lewis Daughter & Sons High-Frequency Trading and Shortcake Shop Incorporated we take data integrity very seriously. A single bit flipped in our transition can mean the difference between making a lot of money and triggering the next financial crisis. Needless to say, we'd prefer to make money. As a result, we must ensure the integrity of all of our data transmissions. We use a system built on parity checks to achieve this.

A parity check involves counting all the bits in a binary array that are 1, and flipping a special parity bit, so that the total number of bits in the array that are 1, including the parity bit, is even.

## Mutiple parity check
But this is not enough. We need to know not only if a bit got flipped, but where exactly in the message that happened. To do this, we use multiple parity bits. Each bit with index `i` that is a power of 2 is used as the parity bit for all bits with index `j`  where `(j / i) % 2 == 1`. (Division, in this case, means integer division, where all decimal values are discarded afterwards). Bit 0 is always ignored.

This sounds complicated, so let me show you an example. Let's consider the below 16-bit binary number, with Bit 0 on the left and Bit 15 on the right.
<pre>
Bit 0
|    Bit 4        Bit 15
|    |            |
0010 <b><i>1</i>011</b> 1000 <b>1110</b>
</pre>
Bit 4 is the parity bit for all indices that if we divide by 4 we are left with an odd number:
<pre>
Bit 4:  <b>1</b>
Bit 5:  <b>0</b>
Bit 6:  <b>1</b>
Bit 7:  <b>1</b>
Bit 12: <b>1</b>
Bit 13: <b>1</b>
Bit 14: <b>1</b>
Bit 15: <b>0</b>
</pre>
We can see, that Bit 4 is set correctly because the total number of `1`s is even. What's even more important, is if we look at the whole number, all parity bits are set correctly:

<pre>
Bit 1:
0<b><i>0</i>10 1011 1000 1110</b>
Bit 2:
00<b><i>1</i>0 1011 1000 1110</b>
Bit 4:
0010 <b><i>1</i>011 1000 1110</b>
Bit 8:
0010 1011 <b><i>1</i>000 1110</b>
</pre>
The nice thing about this system is that if a bit gets flipped, we can tell where it was, based on the parity bits. Let's look at the same example, but with Bit 10 flipped:

Bit 10 flipped
<pre>            |
0010 1011 10<i>1</i>0 1110
</pre>  
If we do the above checks again, we will see that Bits 2 and 8 now have the wrong parity. Finding the number that, if divided by 2 and 8 is odd, but when divided by 1 or 4 is even, tells us that bit 10 must be wrong. So if we flip it back, we get the original, uncorrupted message.

Even better, this system scales to any sized message that is a power of 2 bits long (which is more than 4). So even though the example message has 16 bits, it would work for a message with 8 bits or 64 bits just as well.

## Challange

As your input, you are given a hexadecimal number (digits 0-9, a-f), that was correctly encoded using the system above, and then had at most 1 bit flipped. The input will always be in the correct format. The input is at least 1 digit (4 bits) and at most 16 digits (64 bits) long.

Your job is to find the bit that was flipped using the parity bits, and return the corrected message in the same hexadecimal format. If the message is already correct, return it unchanged. So for the above example, your input is `2bae` and you should return `2b8e`.

If it works, all of our systems will keep hamming along nicely. If not, it may have catastrophic consequences, if a ghost or cosmic ray flips a bit.