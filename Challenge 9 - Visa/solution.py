class Clearing:

    def calculate_settlement(self, account, amount, merchantType, acquirer, issuer):
        # Your code goes here
        invalid = []
        settlement = [0] * 64

        merchant_types = [0, 1, 2, 3, 4, 5, 6, 7]  # same list for banks

        extra_invalid = [] # it is not clear if we should consider transactions with missing fields to be invalid or if we should just ignore them
        accounts = len(account)
        amounts = len(amount)
        merchantTypes = len(merchantType)
        acquirers = len(acquirer)
        issuers = len(issuer)
        sizes = [accounts, amounts, merchantTypes, acquirers, issuers]
        shortest = min(sizes)
        if len(set(sizes)) > 1:
            largest = max(sizes)
            for j in range(shortest, largest):
                extra_invalid.append(j)

        for i in range(shortest):

            accounti = account[i]
            validity = self.invalid_account(accounti)[0]
            mod_value = self.invalid_account(accounti)[1]
            if validity:
                invalid.append(i)
                continue

            amounti = amount[i]
            if amounti < 0:
                invalid.append(i)
                continue

            merchanti = merchantType[i]
            acquireri = acquirer[i]
            issueri = issuer[i]
            if any(x not in merchant_types for x in [merchanti, acquireri, issueri]):
                invalid.append(i)
                continue

            if acquireri == 5 or issueri == 5: # I am not sure if "accepts" refers to just receiving money or also to sending it
                if merchanti not in [1, 2, 5]:
                    invalid.append(i)
                    continue

            if issueri == 7:
                invalid.append(i)
                continue

            if acquireri == 2:
                invalid.append(i)
                continue

            if mod_value == 37 and merchanti == 4:
                invalid.append(i)
                continue

            if merchanti == 0 and amounti != 0:
                invalid.append(i)
                continue

            index = (issueri * 8) + acquireri
            settlement[index] += amounti
        invalid += extra_invalid
        return invalid if invalid else settlement

    def invalid_account(self, accounti):
        cond1 = 10000000 <= accounti <= 99999999  # check for many values of n if this is more efficient than counting digits, plotting the results
        x = accounti % 42
        cond2 = x in [17, 27, 37]
        return [not (cond1 and cond2), x]

