# given a circular list of gas stations, where we can go from a station i to the station i +1, and the last one goes back to the first one, find the index of the station from where we start to be able to traverse all the stations and go back to the initial one without running out of gas
# note taht :
#   we can only move forwad
#   the gas tank starts empty
#   gas[i] represents the amount of gas at the station i
#   cost[i] represents the cost to go from the station i to the next one
#   the answer is guranteed to be unique
#   if  the station we're searching for doesn't exist return -1
#   |gas| = |cost| 
#   gas[i] >= 0
#   cost[i] >= 0

class Solution:
    def gasStation1(self,gas,cost):

        for i in range(len(gas)):
            total = 0
            count = 0
            for j in range(i,len(gas)):
                total = total + gas[j] - cost[j]
                count +=1
                if total < 0:
                    break
            for k in range(0,i):
                total = total + gas[k] - cost[k]
                count+=1
                if total < 0:
                    break
            if count == len(gas):
                return i
        return -1

    def gasStation2(self,gas,cost):

        pass

if __name__== "__main__":
    s = Solution()
    gas = [1,5,3,3,5,3,1,3,4,5]
    cost = [5,2,2,8,2,4,2,5,1,2]
    print(8==s.gasStation1(gas,cost))
    # print(8==s.gasStation2(gas,cost))
