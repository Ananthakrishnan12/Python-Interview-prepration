# class Solution:
#     def is_prime(self,nums):
#         if nums <2:
#             return " "
        
#         for i in range(2,int(nums**0.5)+1):
#             if nums%i==0:
#                 return "Non prime"
#         return "prime"

# nums=7  
# soln=Solution()
# res=soln.is_prime(nums)
# print(res)

# dict1={"a","b","c"}
# mapping={"a":"x","b":"y","c":"z"}
# result=list(map(lambda x:mapping.get(x,x),dict1))
# print(result)


# class Solution:
#     def sum_pairs(self,nums,target):
#         seen=set()
#         pairs=[]
#         for i in nums:
#             compliment=target-i
#             if compliment in seen:
#                 pairs.append((compliment,i))
#             seen.add(i)
#         return pairs
    

# nums=[1, 2, 3, 4, 5, 6, 7]
# target=8
# soln=Solution()
# res=soln.sum_pairs(nums,target)
# print(res)

# class Solution:
#     def remove_duplicates(self,string):
#         seen=set()
#         result=[]
#         for i in string:
#             if i not in seen:
#                 seen.add(i)
#                 result.append(i)
#         return " ".join(result)
   
# string="leetcode" 
# soln=Solution()
# res=soln.remove_duplicates(string)
# print(res)


input="abbbb"
print(input[-4])