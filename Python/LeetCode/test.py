Lambda = 435
# n1 = 7
# n2 = 10000
# z = (1/(Lambda*0.0109)*1/(1/n1**2 - 1/n2**2))**(0.5)

def z(n1,n2,Lambda):
    return (1/((Lambda*0.0109)*(1/n1**2 - 1/n2**2)))**(0.5)

possiveisZ = set()

for n1 in range(1, 100):
    for n2 in range(n1+1, 100):
        i1 = z(n1,n2,650)
        i2 = z(n1,n2,483)
        i3 = z(n1,n2,435)
        if abs(i1 - round(i1)) < 0.1 and abs(i2 - round(i2)) < 0.1 and abs(i3 - round(i3)) < 0.1:
            possiveisZ.add(round(i))
print(possiveisZ)