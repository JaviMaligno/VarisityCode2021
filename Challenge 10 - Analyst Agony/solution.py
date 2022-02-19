from collections import defaultdict


class Traders:

    def aggregate_ohlcv(self, trades):
        # Your code goes here
        # I am going to keep the original strings and keep track of them so that I don't lose trailing zeroes
        trades_per_hour = defaultdict(list)
        output = []
        for trade in trades:
            t = trade.split(",")  # the date comes separated with commas
            # I am going to group the data by hours
            # Possibly, there will be no trades in some hours, so I will specify the hour as the key of a dictionary
            minute = int(t[0])


            if minute < 0 or minute >= 8 * 60:
                continue
            else:
                hour = minute // 60
                trades_per_hour[hour].append(t)

        for hour in trades_per_hour.keys():
            hour_trades = trades_per_hour[hour]
            open_price = hour_trades[0][1]
            close_price = hour_trades[-1][1]
            high_low = self.highest_lowest(hour_trades)
            volume = sum(int(x[2]) for x in hour_trades)
            bucket = str(hour) + "," + open_price + "," + high_low + "," + close_price + "," + str(volume)
            output.append(bucket)

        return output

    def highest_lowest(self, list_of_trades):
        sort_by_price = sorted(list_of_trades, key=lambda x: float(x[1]))
        highest = sort_by_price[-1][1]
        lowest = sort_by_price[0][1]
        return highest + "," + lowest

