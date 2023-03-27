# Calculate volume of a rectangular prism in cubic feets
length=int(input("Please enter length : "))
width=int(input("Please enter width : "))
height=int(input("Please enter height : "))

#function to create volume of rectangular prism
def volume_of_prism(length,width,height):
    return length*width*height

print("The volume of the rectangular prism is : "+str(volume_of_prism(length,width,height)) +" cubic feet.")