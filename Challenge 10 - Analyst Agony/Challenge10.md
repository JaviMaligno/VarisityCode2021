# Challenge description

Welcome to McGraw & Daughters Asset Management. Here we deal with everything from blue-chip stocks to soy futures. Except for Onions! You'll get your orientation from a Senior Analyst, but we need you to get started working on some automated insights right away.

We receive a stream of market events from the stock exchange, and we need you to create an hourly Open-High-Low-Close-Volume aggregation for each day. You can find the specifications on your desk. I need it by 4pm.

The specification reads:

- Market data arrives as an array of strings, with values separated by commas.
- Each market event corresponds to a trade someone made on the exchange. Each trade has 3 fields that we care about.
  - Time: an integer showing the minutes passed since market open.
  - Price: a decimal showing the price at which the trade was made.
  - Quantity: a positive integer showing the number of contracts traded.
- The data comes pre-sorted. It may have duplicate times, but the sorting has accounted for second/millisecond differences that have already been discarded. You only get market data for a single trading day. It will always be in the same, correct format.
- We need you to aggregate the data into buckets for every hour during the trading day. The market closes exactly 8 hours after the market opened. You may see market data from outside of trading hours, ignore these.
- Each aggregate should have values in the same format to the market data. Each bucket has the following fields:
  - Time: the hour for which the aggregate is made. Starts at 0.
  - Open: the first price in the hour.
  - High: the highest price traded during the hour.
  - Low: the lowest price traded during the hour.
  - Close: the last price in the hour.
  - Volume: the total quantity traded during the hour.

- Return this data for all hours that had market activity ordered by time

## Example

Let's look at some example market data:

```
"15,12.5000,50",
"25,10.2000,100",
"45,14.8000,20",
"55,13.1000,30"
```

Looking at the first trade, you can see that it was made 15 minutes after market open, the price was 12.5000 and the quantity was 50.

Overall, the result would look like this: 

`["0,12.5000,14.8000,10.2000,13.1000,200"]` 

The data is for hour 0, and it has in order the first, highest, lowest and last price and the total volume. There is no data for any other hours.