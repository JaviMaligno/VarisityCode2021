# Challenge description

## Background
Every day at Visa, we process millions of transactions through a process of Authorisation and then subsequently Clearing and Settling. A key part of this process is Clearing where the day's transactions are sorted and sifted into a settlement file that can then be used to move money between banks.

We do this because we use what's known as a 'four party model' -- the four parties are below:

- Account Holder: The holder of an account. Synonymous with the term 'Cardholder'. For example, you!
- Merchant: This is the place the Account Holder is purchasing from. For example, your supermarket or online shop.
- Issuer: The bank which maintains the Account Holder's account.
- Acquirer: The bank which maintains the Merchant's account.
- 
Visa sits in the middle connecting all the Issuers and Acquirers with each other globally.

## Challenge

In this challenge, your task is to create a clearing function which will generate one of these settlement files.

You are given a list of transactions, in the form of five arrays:

`Account`, `Amount`, `Merchant Type`, `Acquirer` and `Issuer`.

Your task is to process it for validity and calculate how much each bank owes each other.

## Parameters

All parameters are arrays of integers. Treat each index across all parameters as one transaction.

For example, for the 1st transaction, the account would be `account[0]`, the amount `amount[0]`, and so on. For the 2nd transaction, it would be `account[1]`, `amount[1]`, and so on.

### Account
- This is an array of account numbers.
- Valid account numbers are present in the range `1000_0000-9999_9999` (8 digits).
- Valid account numbers follow the rule `x = account mod 42`, where x must be one of:
  - 17: debit.
  - 27: credit.
  - 37: corporate.
- Example: `42424259` is a valid account number (debit), while `-42424259` is not.

### Amount
- Array of transaction amounts.
- Valid amounts are non-negative integers.
- Amounts are expressed in pence.
- Note: Amounts in the tests will not pass the limit of a 32 bit signed integer.
- Example: `15124` is a valid amount, while `-5` is not.

### Merchant Type
- This is an array of the various merchant categories.
- The valid categories of merchant are:
  - 0 - Verification.
  - 1 - Supermarket.
  - 2 - Travel.
  - 3 - Restaurant.
  - 4 - Gambling.
  - 5 - Retail.
  - 6 - Service.
  - 7 - Other.
- Example: `5` is a valid category of merchant, while `10` is not.

### Acquirer and Issuer (Banks)
- This section covers both Acquirer and Issuer.
- Acquirer is an array of banks.
- Issuer is an array of banks.
- In a transaction, the acquirer receives funds, while issuer sends them.
- There are 8 banks, represented by the numbers 0 through 7.
- If the acquirer and issuer is the same bank, for the purpose of this challenge, the Bank owes itself money.
- Example: `4` is a valid bank, while `-5` is not

## Special Conditions
Every valid transaction follows these rules:

- Bank 5 only accepts Supermarket, Travel, and Retail transactions.
- Bank 7 is only an Acquirer.
- Bank 2 is only an Issuer.
- Corporate accounts do not accept gambling transactions.
- Verification transactions always have an amount of `0`.

## Return Value
You must return an integer array containing what each bank owes each other.
Use the formula `(Issuer * 8) + Acquirer` to generate the array index.


## Invalid Transactions
- If a transaction is invalid, an array of the invalid transactions should be returned instead.
- Some causes of this might be failing a special condition, or an invalid value.
- For example, if the first transaction's account is `1234`, the return array should be `[0]`.

## Examples

### Example 1
- Bank 0 owes bank 4 an amount of 100:
`Account[0] = 42424259`; `Amount[0] = 100`; `Merchant[0] = 1`; `Acquirer[0] = 1`; `Issuer[0] = 4`.
- Bank 4 owes bank 1 an amount of 40:
`Account[1] = 42424259`; `Amount[1] = 40`; `Merchant[1] = 1`; `Acquirer[1] = 4`; `Issuer[1] = 1`.
- If these are the only transactions, the returned array would be: `[(0*8)+4: 100, (4*8)+0: 40]`:
- All other indexes from `0-63 (7*8+7)` are 0
`[0: 0, ..., 4: 100, ..., 32: 40, ...]`.

### Example 2
- Bank 6 owes bank 2 an amount of 20.
- Bank 6 owes bank 4 an amount of 40.
- Bank 6 owes bank 7 an amount of 70.
- Bank 6 owes bank 2 an amount of 100.
- If these are the only rules, the returned array would be: `[(6*8)+2: 120, (6*8)+4: 40, (6*8)+7: 70]`.
- This returns `[50: 120, 52: 40, 55: 70]`. 
- All other indexes are 0.

### Example 3
- The fifth, seventh and eighth transactions are invalid.
- The array `[4, 6, 7]` should be returned.
- Note: There are no amounts owed in this return!