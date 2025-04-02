class Solution:
    def fibonnaci_series(self,n):
        fibonnaci_sequence=[0,1]
        for i in range(2,n):
            next_term=fibonnaci_sequence[-1]+fibonnaci_sequence[-2]
            fibonnaci_sequence.append(next_term)
        return fibonnaci_sequence
    
n=int(input("Enter the n of your choice:"))
soln=Solution()
res=soln.fibonnaci_series(n)
print(res)
