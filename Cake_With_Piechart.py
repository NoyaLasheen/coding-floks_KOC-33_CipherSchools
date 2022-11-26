# Python Project for dividing a cake into 
# "n" number of pieces in three different ways as follows :
    # Into n number of equal pieces
    # Into n number of unequal pieces
    # Into n number of random pieces

# Group Name : coding-folks
# Section : KOC 33
# Group members 
    # Name                      Roll No.      Reg No.
    # Noya Lasheen              B 67          12218742
    # Sachin Dubey              B 66          12217929
    # Jithendra Kumar Pandit    B 68          12219066
    
# importing "matplotlib.pyplot" for ploting the data as pie charts
import matplotlib.pyplot as plt

# importing "random" for random number generation 
import random

n = int(input("\nEnter the number of pieces: "))
print("")
if n<2 or n>360:
    print("Number of pieces should be > 1 and <= 360\n")      
    exit()

slices = []
axistitle = []
count = 0

# Colors to be used in the pie chart
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'red', 'orange']

if 360 % n == 0 :
    print("Cake can be cut into",n,"number of equal pieces having an angle of",int(360/n))
    # Data to plot on axis 1
    slices.append([])            
    
    for i in range(1,n+1):
        slices[count].append(int(360/n))

    # Cake will be cut into pieces as per the angles given below    
    print(slices[count],"\n") 

    axistitle.append(str(n) + " number of equal pieces")   
else:
    print("Cake cannot be cut into",n,"number of equal pieces having a positive integer angle\n")

if n > 26:
    print("Cake cannot be cut into",n,"number of unequal pieces having a positive integer angle\n")
else:
    print("Cake can be cut into",n,"number of unequal pieces having a positive integer angle")

    Total = sum(range(1,n+1))
    if len(slices) > 0:
        count = count + 1
    
    slices.append([])
    
    # Data to plot on axis 2

    # Generate the values in the range of 1 and n using for loop
    for i in range(1,n+1): 
        # calculate the proportion of the value against 360 
        # and append the value to the slices list
        slices[count].append(round(i*360/Total))
    
    sumslices = sum(slices[count])

    # Last element in the list is updated 
    # in order to make the sum of pieces equal to 360
    if sumslices > 360:
        slices[count][n-1] = slices[count][n-1] - (sumslices - 360)
    elif sumslices < 360:
        slices[count][n-1] = slices[count][n-1] + (360 - sumslices)

    # Cake will be cut into pieces as per the angles given below
    print(slices[count])
    print("Sum of slices =",sum(slices[count]),"\n")
    
    axistitle.append(str(n) + " number of unequal pieces")

# Data to plot on axis 3

print("Cake can be cut into",n,"number of random pieces having a positive integer angle")

if len(slices)>0:
    count = count + 1

slices.append([])

# Generate the values in the range of 1 and n using the for loop
for i in range(1,n+1):
    # Generate random values in the range of 1 and (360 / n) + 1 
    # and append the value to the slices list
    slices[count].append(random.randrange(1,int(360/n)+1))

sumslices = sum(slices[count])

# Last element in the list is updated 
# in order to make the sum of pieces equal to 360

if sumslices > 360:
    slices[count][i-1] = slices[count][i-1] - (sumslices - 360)
elif sumslices < 360:
    slices[count][i-1] = slices[count][i-1] + (360 - sumslices)

# Cake will be cut into pieces as per the angles given below

print(slices[count])
print("Sum of slices =",sum(slices[count]),"\n")

axistitle.append(str(n) + " number of random pieces")

# Plot
# create a figure with subplots
if count == 0 : # if only one chart has to be plotted
    fig, (ax1) = plt.subplots(1,1)
    ax1.pie(slices[0], labels=slices[0], colors=colors,
        shadow=True, startangle=140)
    ax1.title.set_text(axistitle[0])

elif count == 1 : # if two charts have to be plotted
    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.pie(slices[0], labels=slices[0], colors=colors,
        shadow=True, startangle=140)
    ax1.title.set_text(axistitle[0])

    ax2.pie(slices[1], labels=slices[1], colors=colors,
        shadow=True, startangle=140)
    ax2.title.set_text(axistitle[1])
 
else : # if all the three charts have to be plotted
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3) 
    ax1.pie(slices[0], labels=slices[0], colors=colors, 
        shadow=True, startangle=140)
    ax1.title.set_text(axistitle[0])

    ax2.pie(slices[1], labels=slices[1], colors=colors,
        shadow=True, startangle=140)
    ax2.title.set_text(axistitle[1])

    ax3.pie(slices[2], labels=slices[2], colors=colors,
        shadow=True, startangle=140)
    ax3.title.set_text(axistitle[2])

# plot each pie chart in a separate subplot

plt.show()
