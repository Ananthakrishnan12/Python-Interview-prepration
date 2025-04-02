class Solution:
    def found_words(self,input,check):
        founded_words=[]
        for i in check:
            if i in input:
                founded_words.append(i)
        return founded_words
    
input="hgsvhsvhsvsujithhsgvhsvsh hsvhsvshAnanthakrishnansvhssgsv ssvhsvsvReshmasvshvsghvs"
check=["sujith","Ananthakrishnan","Reshma"]
soln=Solution()
res=soln.found_words(input,check)
print(res)
