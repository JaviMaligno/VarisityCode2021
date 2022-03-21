class MatchingEngine:

    def handle_orders(self, orders):
        # Your code goes here
        trades = []
        if len(orders) <= 1:
            return trades

        listed_orders = [x.split(",") for x in orders]
        numerical_orders = [[int(x[0]),x[1],x[2],int(x[3]),x[4]] for x in listed_orders]
        #not converting the price x[2] into float yet because I don't want to lose trailing 0s
        ask = [x for x in numerical_orders if x[1] == "A"]
        bid = [x for x in numerical_orders if x[1] == "B"]
        for order in numerical_orders[1:]:
            if order[1] == "A":
                trades+=self.compute_trades(order,"A",opposite=bid,own=ask)
            if order[1] == "B":
                trades += self.compute_trades(order, "B", opposite=ask,own=bid)

        return trades

    def compute_trades(self,order, type, opposite,own):
        #consider defining a dicitionary {"A":ask, "B":bid} to call the correct list  with this
        trades=[]
        order_price = float(order[2])
        index_own = own.index(order)
        if type == "A":
            candidates = [x for x in opposite if x[0] < order[0] and float(x[2]) >= order_price]
            if candidates:
                sort_candidates = sorted(candidates, key=lambda x: (-float(x[2]), x[1]))
                self.trade_loop(sort_candidates, order, own, opposite, trades, index_own)
                # while sort_candidates:
                #     match = sort_candidates[0]
                #     index_opp = opposite.index(match)
                #     if order[3] < match[3]:
                #         trade = [order[0],match[2],order[3],match[4],order[4]]
                #         output_trade = ",".join(map(lambda x:str(x),trade))
                #         trades.append(output_trade)
                #         own.remove(order)
                #         diff = match[3]-order[3]
                #         opposite[index_opp][3]=diff
                #         break
                #     elif order[3] == match[3]:
                #         trade = [order[0], match[2], order[3], match[4], order[4]]
                #         output_trade = ",".join(map(lambda x: str(x), trade))
                #         trades.append(output_trade)
                #         own.remove(order)
                #         opposite.remove(match)
                #         break
                #     else:
                #         trade = [order[0], match[2], match[3], match[4], order[4]]
                #         output_trade = ",".join(map(lambda x: str(x), trade))
                #         trades.append(output_trade)
                #         diff = order[3]-match[3]
                #         own[index_own][3]=diff
                #         opposite.remove(match)
                #         sort_candidates=sort_candidates[1:]

                return trades

            else:
                return trades

        if type == "B":
            candidates = [x for x in opposite if x[0] < order[0] and float(x[2]) <= order_price]
            if candidates:
                sort_candidates = sorted(candidates, key=lambda x: (float(x[2]), x[1]))
                self.trade_loop(sort_candidates,order,own,opposite,trades,index_own)
                # while sort_candidates:
                #     match = sort_candidates[0]
                #     index_opp = opposite.index(match)
                #     if order[3] < match[3]:
                #         trade = [order[0],match[2],order[3],match[4],order[4]]
                #         output_trade = ",".join(map(lambda x:str(x),trade))
                #         trades.append(output_trade)
                #         own.remove(order)
                #         diff = match[3]-order[3]
                #         opposite[index_opp][3]=diff
                #         break
                #     elif order[3] == match[3]:
                #         trade = [order[0], match[2], order[3], match[4], order[4]]
                #         output_trade = ",".join(map(lambda x: str(x), trade))
                #         trades.append(output_trade)
                #         own.remove(order)
                #         opposite.remove(match)
                #         break
                #     else:
                #         trade = [order[0], match[2], match[3], match[4], order[4]]
                #         output_trade = ",".join(map(lambda x: str(x), trade))
                #         trades.append(output_trade)
                #         diff = order[3]-match[3]
                #         own[index_own][3]=diff
                #         opposite.remove(match)
                #         sort_candidates=sort_candidates[1:]

                return trades

            else:
                return trades



    def trade_loop(self,sort_candidates,order,own,opposite,trades,index_own):
        while sort_candidates:
            match = sort_candidates[0]
            index_opp = opposite.index(match)
            if order[3] < match[3]:
                trade = [order[0], match[2], order[3], match[4], order[4]]
                output_trade = ",".join(map(lambda x: str(x), trade))
                trades.append(output_trade)
                own.remove(order)
                diff = match[3] - order[3]
                opposite[index_opp][3] = diff
                break
            elif order[3] == match[3]:
                trade = [order[0], match[2], order[3], match[4], order[4]]
                output_trade = ",".join(map(lambda x: str(x), trade))
                trades.append(output_trade)
                own.remove(order)
                opposite.remove(match)
                break
            else:
                trade = [order[0], match[2], match[3], match[4], order[4]]
                output_trade = ",".join(map(lambda x: str(x), trade))
                trades.append(output_trade)
                diff = order[3] - match[3]
                own[index_own][3] = diff
                opposite.remove(match)
                sort_candidates = sort_candidates[1:]



