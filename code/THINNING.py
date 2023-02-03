#KWABIA_ISAAC
# thinning ratio calculation
#thinning ratio = TR
#average diameter before thinning = DBHa_cm
#average diameter of trees removed = DBHb_cm
#these averages are adapted from the data source
input("KWABIA_ISAAC")
species1 = "pine_in_pure_stand"
DBHa_cm = 37.12
DBHb_cm = 11.07

species2 = "oak_in_pure_stand"
DBHa1_cm = 35.88
DBHb1_cm = 16.82

species3 = "oak_in_mixed_stand"
DBHa2_cm =20.28
DBHb2_cm =15.81

species4 = "pine_in_mixed_stand"
DBHa3_cm = 33.08
DBHb3_cm = 33.08

def TR(species,DBHa_cm,DBHb_cm):
    TR = DBHb_cm/DBHa_cm
    print("TR:")
    print(TR) 
    if TR < 1.0 :
        return species  +  " :  low thinning "
    else:
        if TR == 1.0:
            return species + ": perfect thinning"
        else:
            return species + ":thinning of dominants"
    
result1= TR(species1,DBHa_cm,DBHb_cm)
result2= TR(species2,DBHa1_cm,DBHb1_cm)
result3= TR(species3,DBHa2_cm,DBHb2_cm)
result4= TR(species4,DBHa3_cm,DBHb3_cm)

print(result1)
print(result2)
print(result3)
print(result4)


#calculation of the averages of the DBH for pines
# list of dbh of pines before thinning for pure pine stand (P_DBHb_cm) = x
#list of dbh of pines after thining for pure pine stand(P_DBHa_cm)= y
x= [40.8,27.8,37.4,36.6,47.1,35,34.9,32.5,40.2,34.1,34,28,29.2,43.1,28.1,38.8,46,44.8,39.2,43.7]
print("PINE IN PURE STAND")
x.sort()
print(x)

total = 0
for elements in x:
    total = total + elements
print("sum:")
print(format(total,".2f"))

print("total number of trees :")
print(len(x))

print("PRE-THINNED")
print("average diameter:")
print(format(total/len(x),".2f"))

y= [41.2,27.9,38.1,37.2,49,36.1,37.2,33,41,35.2,35.2,29.4,30.1,45,28.1,38.8,46.4,45.6,40.1,43.8]

total = 0
for e in y:
    total = total + e
print("sum:")
print(format(total,".2f"))

print("total number of trees:")
print(len(y))

print("POST-THINNED")
print("average diameter:")
print(format(total/len(y),".2f"))


#calculation of the averages of the DBH for pines
# list of dbh of pines before thinning for pine_oak mixed stand (P_DBHb_cm) = x3
#list of dbh of pines after thining for  pine_oak mixed stand(P_DBHa_cm)= y3

x3= [39,30.6,38.7,58,28.3,30.1,31.7,37.7,26.5,41.2,41.5,31.5,30.1,36.7,40,31.4]
print("PINE IN PINE_OAK MIXED STAND")
x3.sort()
print(x3)

total = 0
for elements in x3:
    total = total + elements
print("sum:")
print(format(total,".2f"))

print("total number of trees :")
print(len(x3))

print("PRE-THINNED")
print("average diameter:")
print(format(total/len(x3),".2f"))

y3= [39.1,31,39.8,61.4,30.1,32.3,32.9,40.2,29,43.4,44.3,35.2,31.1,38.1,41,32.7]

total = 0
for e in y3:
    total = total + e
print("sum:")
print(format(total,".2f"))

print("total number of trees:")
print(len(y3))

print("POST-THINNED")
print("average diameter:")
print(format(total/len(y3),".2f"))


#calculation of the averages of the DBH for oak
# list of dbh of oak before thinning for pine_oak mixed stand (O_DBHb_cm) = x2
#list of dbh of oak after thining for pine_oak mixed stand(O_DBHa_cm)= y2

x2 = [21.6,31.9,22.6,14.3,27.2,24.9,34.8,37.8,18.2,15.4,9.7,13.5,22.9,34.5,25.4,15.8,45.7,24,35.2,35.1,22,18.1,18,14.9]
print("OAK IN PINE_OAK MIXED STAND")
x2.sort()
print(x2)

total= 0
for e in x2:
    total = total + e
print("sum:")
print(format(total,".2f"))

print("total number of trees :")
print(len(x2))

print("PRE THINNED")
print("average diameter:")
print(format(total/len(x2),".2f"))

y2= [21.7,32,22.7,14.3,27.2,24.9,35.7,39.9,18.3,14.9,9.6,13.9,23.2,34.6,25.3,15.4,46.3,24.1,35.7,36.2,23,18.8,19,14.4]
total = 0
for e in y2:
    total = total + e
print("sum:")
print(format(total,".2f"))

print("total number of trees:")
print(len(y2))

print("POST THINNED")
print("average diameter:")
print(format(total/len(y2),".2f"))


#calculation of the averages of the DBH for oak
# list of dbh of oak before thinning for pure oak stand (O_DBHb_cm) = x1
#list of dbh of oak after thining for pure oak stand(O_DBHa_cm)= y1

x1 = [53.3,42.8,27.8,55.8,31.5,40.2,33.7,35.5,42.5,11.5,40.3,51.2,26.9,35,49.8,26.3,29.8,33.9,38,36.7]
print("OAK IN PURE STAND")
x1.sort()
print(x1)

total= 0
for e in x1:
    total = total + e
print("sum:")
print(format(total,".2f"))

print("total number of trees :")
print(len(x1))

print("PRE THINNED")
print("average diameter:")
print(format(total/len(x1),".2f"))

y1= [53.6,42.8,27.9,56,31.5,40.2,33.8,35.7,42.5,11.8,40.5,52,27,35.1,50,26.4,30,33.9,38.1,36.9]
total = 0
for e in y1:
    total = total + e
print("sum:")
print(format(total,".2f"))

print("total number of trees:")
print(len(y1))

print("POST THINNED")
print("average diameter:")
print(format(total/len(y1),".2f"))

#checking the increase of dbh with respect to thinning
#this is done by subtraction of pre-thinned from post-thinned
species1 = "pine_in_pure_stand"
x= 37.07
y= 37.92

species2 = "oak_in_pure_stand"
x1=37.12
y1=37.28

species3 = "oak_in_mixed_stand"
x2=24.31
y2=24.63

species4 = "pine_in_mixed_stand"
x3=35.81
y3=37.60

def increased_dbh(species,x,y):
    increased_dbh=y-x
    print("Resulting Change In DBH:")
    print(format(increased_dbh,".2f"))
    if increased_dbh > 1.0 :
        return species  +  ":significant effect "
    else:
         return species + ":insignificant effect" 
    

    
result1= increased_dbh(species1,x,y)
result2= increased_dbh(species2,x1,y1)
result3= increased_dbh(species3,x2,y2)
result4= increased_dbh(species4,x3,y3)

print(result1)
print(result2)
print(result3)
print(result4)


print("results show thinning effect on mostly pine and thinning ratio had effect")
print("FIELD CAMPAIGNS;NEUENDORF")
print("THANK YOU FOR YOUR TIME************************")

input("please press enter to exit")
