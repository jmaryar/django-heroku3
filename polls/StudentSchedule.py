#jr7yj
#Julia Rudy
import random
orders = 0

books = ['calculus', 'physics', 'chemistry','history','literature','french','astronomy']
ordersList = []


for a in books:
    for b in books:
        if a != b and a > b:
            for c in books:
                if c!= a and c!= b and c >a and c >b:
                    for d in books:
                        if d!= a and d!=b and d!=c and d>a and d>b and d > c:
                            orders += 1
                            ordersList.append(a + " " + b + " "+ c + " " +  d )

print(orders)
print("The book orders list" , ordersList)


passwords = 0

indices = ['1','2','3',"4","5","6","7",'8']
passwordsList = []
for zero1index in indices:
    for zero2index in indices:
        if zero1index != zero2index and zero1index > zero2index:
            for zero3index in indices:
                if zero3index != zero1index and zero3index != zero2index and zero1index > zero3index and zero2index > zero3index:
                    passwords +=1
                    passwordsList.append(zero3index+zero2index+zero1index)
                    #print(zero3index+zero2index+zero1index)
print(passwordsList)
print("The number of passwords is" , passwords)

passwords = 0

count = 0
passwords2 = 0
passwordDict = {}
passwordsList = []
availableNumsList = [['1', '2', '3', "4", "5"], ['1', '2', '3', "4", "6"],['1', '2', '3', "4", "7"],['1', '2', '3', "5", "6"],['1', '2', '3', "5", "7"],['1', '2', '3', "6", "7"],['1', '2', '4', "5", "6"],['1', '2', '4', "5", "7"],['1', '2', '4', "6", "7"],['1', '2', '5', "6", "7"],['1', '3', '4', "5", "6"],['1', '3', '4', "5", "7"],['1', '3', '4', "6", "7"],['1', '3', '5', "6", "7"],['1', '4', '5', "6", "7"],['2', '3', '4', "5", "6"],['2', '3', '4', "5", "7"],['2', '3', '4', "6", "7"],['2', '3', '5', "6", "7"],['2', '4', '5', "6", "7"],['3', '4', '5', "6", "7"]]
for availableNums in availableNumsList:

    for zero1index in indices:
        for zero2index in indices:
            if zero1index != zero2index and zero1index > zero2index:
                for zero3index in indices:
                    if zero3index != zero1index and zero3index != zero2index and zero1index > zero3index and zero2index > zero3index:
                        passwords +=1
                        zeros = zero3index+zero2index+zero1index

                        for i in indices:
                            if i!= zero1index and i != zero2index and i != zero3index:
                                for digit4 in availableNums:
                                    for j in indices:
                                        if i != j and i > j  and j!= zero1index and j != zero2index and j!= zero3index:
                                            for digit5 in availableNums:
                                                if digit5 != digit4:
                                                    for k in indices:
                                                        if k != i and k != j and i > k and j > k and k!= zero1index and k != zero2index and k != zero3index:
                                                            for digit6 in availableNums:
                                                                if digit6 != digit5 and digit6 != digit4:
                                                                    for l in indices:
                                                                        if l != i and l != j and l!=k and i > l and j > l and k >l and l!= zero1index and l != zero2index and l != zero3index:
                                                                            for digit7 in availableNums:
                                                                                if digit7 != digit4 and digit7 != digit5 and digit7 != digit6:
                                                                                    for m in indices:
                                                                                        if m != i and m != j and m != k and m != l and i > m and j > m and k > m and l >m and m!= zero1index and m!= zero2index and m!= zero3index:
                                                                                            for digit8 in availableNums:
                                                                                                if digit8 != digit7 and digit8 != digit6 and digit8 != digit5 and digit8 != digit4:

                                                                                                    passwords2 += 1
                                                                                                    passwordDict[zero1index] = "0"
                                                                                                    passwordDict[zero2index] = "0"
                                                                                                    passwordDict[zero3index] = "0"

                                                                                                    passwordDict[i] = digit4
                                                                                                    passwordDict[j] = digit5
                                                                                                    passwordDict[k] = digit6
                                                                                                    passwordDict[l] = digit7
                                                                                                    passwordDict[m] = digit8

                                                                                                    passwordString = ""
                                                                                                    for numIndex in indices:
                                                                                                        passwordString += passwordDict[numIndex]

                                                                                                    passwordsList.append(passwordString)
                                                                                                    #print( passwordString)
                                                                                                    takenspots = zeros
                                                                                                    count += 1

print("passwords2" , passwords2)
print(passwordsList[:100])
