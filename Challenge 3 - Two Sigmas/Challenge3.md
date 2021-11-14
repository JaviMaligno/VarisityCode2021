# Challenge description

After staying at home for a while, you decide it's time for adventure: You take your car for a ride in the country side. However the car has been left unused for too long and while driving, you realize something is wrong.

Every now and then the car makes a worrying noise and will stop performing well for some time before the issue fixes itself.

The good news is that the car has a debug serial point - you decide to connect your laptop to it to see what's going on. What you discover is that the part of the engine computer that is doing some fine tuning is misbehaving.

To get the fuel injected properly, the car takes into account many parameters (wind speed, road slope, $\dots$ ) and creates 4 points $(x,y)$ that are supposed to be collinear. However, it seems to be broken.

Sometimes the points are not collinear. When this happens you can tell the car to ignore this config and fallback to the previous one.

- The format of the config is a string made up of 4 points delimited by a semi-colon.
- Each point consists of a pair of floating point numbers between 0 and 100, separated by a colon.
- When the 4 points are collinear (i.e. a valid config) you simply return the input string.
When they are not, or if several points have the same $x$ (another form of bad config), then instead return the magic value `"KEEP_PREVIOUS"`.
    - For example, `"1:2;2:4;3.5:7;4:8"` is a valid config, so you should return it.
`"1:1;2:5;3:3;4:6"` or `"1:1;1:2;3:3;4:4"` are not, so you should return `"KEEP_PREVIOUS"`.
- In instances where there are complications, such as two identical points that are not colinear with the second pair, rather than correcting both you should return `"KEEP_PREVIOUS"`.

This makes the car run much better. However you realise that when you use `"KEEP_PREVIOUS"` the car does not perform as well as it should as it's not tuned to the current conditions. You also notice that (most of the time) only one of the points is out of place and the rest are collinear.

When that's the case you need to find that number, fix it and return a fixed configuration.

For example, the first 3 points in `"1:1;2:2;3.5:3.5;4:5"` are collinear, only the last point is not. You can fix that last point by changing the $y$, keeping the same $x$, in the same order. In this instance, you should return `"1:1;2:2;3.5:3.5;4:4"`.

One final note here is that due to the internal representation of numbers in the car computer, all values are fully representable in base ten, it would never be possible to have $\frac{1}{3}$ $(0.333333\dots)$ as a value.