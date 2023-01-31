temperaturen = [41,20,10,30]
temperaturen.append(21)
temperaturen.append(50)

temperaturen2 = [3,5,1,9]
temperaturen.extend(temperaturen2)
temperaturen += [33]
temperaturen.remove(50)
print(temperaturen)
