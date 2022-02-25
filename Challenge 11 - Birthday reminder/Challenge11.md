# Challenge description

You are working on a calendar app. You would like to add a feature, where events for a certain day can repeat periodically in the future.

You are given a date in the following format: `YYYY/MM/DD` and a string describing how it should repeat like this: `every n units`. `Y` denotes years, `M` denotes months with a leading zero if needed and `D` denotes days with a leading zero if needed. `n` is a positive number that is less than 100, and `units` can be `day`, `week`, `month`, `year`. The final `s` is optional.

Your job is to calculate the first four occurrences of the event, starting with the date given and followed by the first 3 repetitions. Return it in the same format as given, padding months and days with zeros to be 2 digits long if needed. The returned year will always be 4 digits long.

The date will always be valid and between 1970 and 2700. If the repeat instruction is not valid, return an empty array.

## Examples

Here are some examples:

Starting date of `2021/10/14` and repeat instruction `every 3 days` should produce `["2021/10/14", "2021/10/17", "2021/10/20", "2021/10/23"]`.

Starting date of `2021/04/04` and repeat instruction `every 1 week` should produce `["2021/04/04", "2021/04/11", "2021/04/18", "2021/04/25"]`. Note how there is no trailing `s` after the unit in the repeat instruction.

Finally, starting date of `2021/01/01` and repeat instruction `every foo bar` should produce `[]`, as the repeat instruction is not valid.

There are some more useful examples as test cases.