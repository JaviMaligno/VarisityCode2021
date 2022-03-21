# Challenge description

You are starting a new stock exchange. Congratulations! Most of the planning is now in place, a logo has been designed, regulators have been bribed. The only thing left is the exchange itself. Fortunately for you, exhanges are no longer large halls with people shouting at each other (the exchanges that still have that only do it as a television backdrop), instead, it's a sophisticated matching engine that takes orders from lots of market participants. Unfortunately for you, you need to develop this matching engine, like yesterday.

Here is what you need to know. The core component of this matching engine is an **Order**. An order essentially signals someone's intent to buy or sell some quantity of a stock at some price. It can be a **Bid** (intending to buy a stock at a certain price) or an **Ask** (intending to sell a stock at a certain price). It is a comma separated string with the following fields in order:

- time: a positive integer denoting the time at which the order was placed. This is in nanoseconds, so you can treat it as unique for each order.
- side: `A` or `B` for **Ask** or **Bid**.
- price: a decimal number with 4 decimal digits showing the price on the order.
- quantity: a positive integer showing the quantity (or volume) on the order, meaning the number of stocks that are up for sale (quantity and volume are terms that can be used interchangably).
- company id: an ASCII string, up to 8 characters long, denoting which market participant (trading company) placed the order.

When a new order comes in, trying to buy or sell a stock, look at orders that are already on the market, on the opposite side from the current order (trying to sell, when the current order is trying to buy). Out of the orders on the opposite side, the orders are considered better when:

- when the current order is an **Ask** (trying to sell): a **Bid** is better the higher the price is (the highest price someone is willing to pay).
- when the current order is a **Bid** (trying to buy): an **Ask** is better the lower the price is (the lowest price someone is willing to buy at).

At any given time, the current order would only match the best order already on the market (on the opposite side) if the price is at least as good as the current order (only sell for at least as much as the price on the current order/only buy for at most as much as the price on the current order). If there are multiple prices on the market at the same price, match first with the oldest (the one that was first placed on the market).

If there is a price on the market that matches, a trade takes place. The trade will have the better price in the match. The current order always tries to satisfy the entire volume (quantity) with the current trade. If the current order is fully satisfied with the matched order, a trade is created for the full volume, the quantity of the matched order is decreased by the quantity on the trade and the current order is discarded as done. If the order on the other side doesn't have enough quantity to satisfy the current order, it is removed as part of this trade, the quantity of the current order is reduced by the quantity of the trade, and the matching process is repeated to find the next best order currently on the market.

If by the end of this process, the current order wasn't fully satisfied, and there are no orders left on the market that it could match with, the order itself is placed on the market, so it can match future orders.

You are given a list of orders, all in the correct format, ordered by time. You need to produce a list of trades that were generated as the orders are processed one by one in the order they occured. Each trade is a comma separated string, with the following fields:

- time: a positive integer, the time when the order that caused this trade to happen was placed on the market. Although the time field for orders is always unique, the same field on trades fields will not be, as a single order can result in multiple trades.
- price: a decimal number with 4 decimal digits, showing the price at which the trade occurred.
- quantity: a positive integer showing the quantity on the trade.
- initiator company id: the initiator is the company id of the order that was already on the market when the trade occurred.
- aggressor company id: the aggressor is the company id of the order that was placed on the market which caused the trade to occur.

## Examples 

You still have your access to an existing stock exchange, which uses a similar matching engine, so you can observe a couple trades, which you can use as examples:

### Example 1

Orders:
```
"10,B,10.5000,50,C001",
"12,A,10.5000,25,C002",
```
When the first order is placed at time = 10, there are no other orders on the market that it could match with.

When the second order is placed on the market at time = 12, it matches with the previous order. The price is the same (`10.5000`) and the other order can fully satisfy the current order's quantity. In this scenario, `C001`  is the initiator and `C002` is the aggressor. As a result, a single trade is created at time = 12:
```
"12,10.5000,25,C001,C002"
```
### Example 2

Orders:
```
"10,A,50.8000,20,C001",
"12,A,51.4000,50,C010",
"18,B,51.5000,60,C002",
"19,A,51.6000,40,C001",
"25,B,50.9000,10,C132",
"28,B,51.6000,70,C007",
"31,A,51.0000,45,C011",
```
The first two orders at time = 10 and 12 have nothing they can match with.

The third order at time = 18 first matches with the first order placed (time = 10), as that was trying to sell for a lower price compared to the current order. As that only has quantity = 20, the current order quantity is reduced from 60 to 40. It then matches with the second order placed (time = 12) as that is also selling at a lower price. This order can now fully satisfy the current order. The order it matched with for the second time has its quantity reduced by 40. As a result, 2 trades are generated at time = 18:

"18,50.8000,20,C001,C002",
"18,51.4000,40,C010,C002",
The order at time = 19 doesn't have any other order to match with.

The order at time = 25 also doesn't match with any other orders, even though there are orders on the market on the opposite side, none of them have a price low enough to match with this one.

The order at time = 28 matches with what remains of the order placed at time = 12. It however can't fully satisfy the order, so it also matches with the order placed at time = 19. But it too can't fully satisfy it. There are no other orders left on the market it could match with, so it is placed on the market with the remaining quantity = 20. 2 trades are generated at time = 28 in order:
```
"28,51.4000,10,C010,C007",
"28,51.6000,40,C001,C007",
```
Finally the order at time = 31 matches with the order that was placed at time = 28 because that order wants to buy at a higher price compared to the current order's selling price. Although not fully satisfied 1 trade is generated at time = 31:
```
"31,51.6000,20,C007,C011"
```
At the end, there are two orders remain on the market. The **Bid** that was created at time = 25 with price `50.9000`; and the **Ask** last placed on the market (time = 31), with price `50.9000` and remaining quantity = 25.