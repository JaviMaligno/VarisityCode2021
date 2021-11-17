# Challenge description

Next's online shopping bag needs to take a set of items that have been added along with a set of discount codes. We need you to calculate the total cost we should charge the customer using the following rules:


Shopping bag items will be passed in the format `ABC123`, where:

- `ABC` (3 characters) is the item code.
- `123` (3 characters) is the cost of the item in GBP. Each unique item code will always have the same price.

Discount codes will be passed in the format `ABC2P20`, where:

- `ABC` (3 characters) is the item code, which is matched to shopping bag items.
- `2` (1 character) is the minimum number of matching items needed in the bag to apply the discount.
- `P` (1 character) is the discount category, either as a percentage discount (`P`) or a cash discount in GBP (`C`).
- `20` (2 characters) is the percentage or cash discount to subtract from each qualifying item.

If an item qualifies for multiple discounts, only the highest discount should apply (i.e. the discount that results in the lowest item price). An item cannot be discounted to be less than £0. Any matching discount should apply to all matching items, i.e. if there are 4 identical items in the bag and a matching discount code has a 3 item minimum then the discount will be applied to all 4 items.


As an example:

The shopping bag `ABC010`, `DEF020`, `ABC010`
With discount codes `ABC2P50`, `DEF1C05`
Would give a total price to charge the customer of £25.