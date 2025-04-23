def desitkova_na_dvojkovou(cislo):
    return bin(cislo)[2:]

def dvojkova_na_desitkovou(dvojkove_cislo):
    return int(dvojkove_cislo, 2)

def scitej_desitkova(a, b):
    return a + b

def scitej_dvojkova(bin1, bin2):

    des1 = int(bin1, 2)
    des2 = int(bin2, 2)
    soucet = des1 + des2
    return bin(soucet)[2:]  

print("Desítková na dvojkovou:", desitkova_na_dvojkovou(42))  
print("Dvojková na desítkovou:", dvojkova_na_desitkovou("101010"))  
print("Sčítání v desítkové:", scitej_desitkova(25, 17)) 
print("Sčítání ve dvojkové:", scitej_dvojkova("11001", "10001")) 
