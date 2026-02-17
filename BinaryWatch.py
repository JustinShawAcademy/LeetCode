class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        #Watch in Binary
        #From 0 - 11 hours   [8 4 2 1]
        #From 0-59 minutes [32 16 8 4 2 1]

        results = []

        for h in range(12): # iterate through all hours
            for m in range(60): #Iterate through all minutes

                #Add up the 1's from iterating through hour LED's and minute LED's and return the timeslot combinations 
                if bin(h).count("1") + bin(m).count("1") == turnedOn: 
                    results.append(f"{h}:{m:02d}")
        return results
    