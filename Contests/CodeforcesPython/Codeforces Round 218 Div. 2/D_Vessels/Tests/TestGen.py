import sys
import random


n = 190019

arr = [random.randint(1, 10 ** 9) for i in range(n)]
 
# myFile = open("d:/MyOneDrive/OneDrive/文档/AlwaysCode/CodeforcesPython/Codeforces Round 218 Div. 2/D_Vessels/Tests/input_1.txt", mode = "a", encoding = "utf-8")
myFile = open("d:/MyOneDrive/OneDrive/文档/AlwaysCode/CodeforcesPython/Codeforces Round 218 Div. 2/D_Vessels/Tests/input_1.txt", mode = "w", encoding = "utf-8")
 
print(n, file = myFile)
# myFile.write(str(n))
print(*arr, file = myFile)
myFile.close()
print("Finish")