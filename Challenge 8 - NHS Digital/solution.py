class ReportingData:

    def cleaner(self, data):
        # Your code goes here
        while len(data) < 4:
            data.append("0")

        #it is very likely that I won't need to store them individually for the most part
        cases = data[0]
        isolating = data[1]
        care = data[2]
        icu = data[3]

        data = self.remove_symbols(data)
        cases = data[0]
        isolating = data[1]
        care = data[2]
        icu = data[3]

        #This changes should be done in context, cause changes in one needs checking the breakdown
        #data[0]=0 if data[0]<1 else data[0] #if the cases are given as a percentage, they're wrong,  may be fixed  later
        #data[1]=data[0]*data[1] if data[1]<1 else data[1]
        #data[2]=data[0]*data[2] if data[2]<1 else data[2]
        #data[3]=data[2]*data[3] if data[3]<1 else data[3]

        if data[0]<1: #if cases = 0,  I check the other values to try to add isolating and care
            if data[2]<1: #I should do this when  data[0]>=1 as well
                data[2]=0
            if data[3]<1:
                data[3]=data[2]*data[3]
            if data[2] < data[3]:
                data[2] += data[3]
            if data[1]<1:
                data[1]=0
            data[0]=data[1]+data[2]

        else:
            if 0<data[2] < 1:  # I should do this when  data[0]>=1 as well
                data[2] = data[0]*data[2]
            if data[3] < 1:
                data[3] = data[2] * data[3]
            if data[2] < data[3]:
                data[2] += data[3]
            if data[2] > data[0]:
                data[2] = 0
            if data[3]>data[0]:
                data[0]=0
            if 0<data[1]<1:
                data[1]=data[0]*data[1]
            if data[1]>data[0]:
                data[1]=0
            if data[1]*data[2]==0:
                if data[2] != data[1]:
                    data[1]=data[0]-data[2] if data[1]==0 else data[1]
                    data[2]=data[0]-data[1] if data[2]==0 else data[2]
            elif data[0]!=data[1]+data[2]:
                data[2]=data[0]-data[1]
#at the moment the tests are working fine
#wait until I get instructions about what to do if the numbers are valid but the cases don't add up
        data=[int(x) for x in data]
        return data
    def remove_symbols(self,data): #MAYBE I SHOULD CHECK IF I MUST RETURN A NON ZERO NUMBER, AS IN THE CASE WHERE ISOLATING IS MISSING BUT CAN BE DDEDUCED FROM OTHER DATA (BUT THAT SHOULD PROBABLY NOT MAKE A DIFFERENCE WITH FIRST SETTING IT TO 0)
        i=0
        for datum in data:
            if datum.endswith("%"):
                try:
                    data[i]=float(datum[:-1])*0.01
                except:
                    data[i]=0
            else:
                try:
                    data[i]=float(datum)
                except:
                    data[i]=0
            i+=1
        return data

if __name__ == '__main__':
    solution=ReportingData()
    print(solution.cleaner(["0","40","40","0"]))


