import numpy
                  
arrDis = numpy.array([[.15, .10, .05, .10],
                      [.25, .25, .15, .15],
                      [.10, .30, .50, .25],
                      [.50, .35, .30, .50]])



inverseDis = numpy.linalg.inv(arrDis)

arrX0 = numpy.array([[1000],
                    [100],
                    [500],
                    [500]])


arrXminus1 = numpy.dot(inverseDis,arrX0)
print("Inverse Y0-3 Spread Matrix")
print(inverseDis,"\n")

year = -1
print("Year:", year)
print(arrXminus1,"\n")
print("Total number of buyers for year:", year)
print((numpy.sum(arrXminus1,axis=0)),"\n")

year += 1
print("Year:", year)
print(arrX0,"\n")
print("Total number of buyers for year:", year)
print((numpy.sum(arrX0,axis=0)),"\n")

for i in range(0,3):
    year += 1    
    result = numpy.dot(arrDis,arrX0)
    print("Year:", year)
    print(result)
    print()
    print("Total number of buyers for year:", year)
    print((numpy.sum(result,axis=0)),"\n")
    arrX0 = result

arrX02 = numpy.vstack((arrX0,[100]))

print("Year 3 initial buyers (After Volvo is added): ")
print(arrX02,"\n")


arrDis2 = numpy.array([[.15,  .095, .05, .10,  .005],
                       [.245, .25,  .14, .145, .005],
                       [.095, .295, .50, .245, .01 ],
                       [.50,  .35,  .30, .50,  .01 ],
                       [.01,  .01,  .01, .01,  .97 ]])

for i in range(0,3):
    year += 1   
    result2 = numpy.dot(arrDis2,arrX02)
    print("Year:", year)
    print(result2)
    print()
    print("Total number of buyers for year:", year)
    print((numpy.sum(result2,axis=0)),"\n")
    arrX02 = result2
