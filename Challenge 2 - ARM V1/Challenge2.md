# Challenge description

History often repeats itself and one of the keys to making our processors faster is being able to predict the future. If we predict what will happen next, we can get a jump start on the next task.

In this challenge, you are presented with a string of digits (0 to 9), among them are underscores ("_")where it is your task to predict the digit which should go there. How do you know what digit goes there? Look to the past. If you have seen the same sequence as our last few digits somewhere in the past, then we can see what the next digit of that sequence was in the past and predict that to be the next one. The longer the matching sequence the better, but you can limit your search to 10 digits. If there are multiple equal matches, the most recent sequence seen should be chosen. Digits before the start of the string can be assumed to be all 0.



For example, "12...1_" (the "..." represents some other digits which were not relevant) should predict 2 to be the next number, since last time we saw a 1 it was followed by a 2.

And "123...24...12_" should predict 3 to be the next number since the sequence "12" was followed by a 3. You may be tempted to use 4, since 2 was followed by 4 last, but "12" is the longer matching sequence.

When we have multiple matches of equal length like "123...124...12_", we match the most recently seen sequence, in this case "124".

For very long matches like "11101234567891...22201234567892...1110123456789_", the correct prediction should be 2, because even though the first matching sequence was longer, only the last 10 digits in the sequence are considered, and thus the sequences are same length and the second one more recent.

Finally, if the previous digit has never appeared before, and thus no matching sequence can be found in the history, your prediction should be a repetition of that last digit.

There is no point in making predictions if they take longer to make than calculating the actual result, so you should aim for the fastest solution possible.