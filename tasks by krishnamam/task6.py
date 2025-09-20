# Write a program to calculate area and volume of
# Sphere.
# 𝐴𝑟𝑒𝑎 𝑜𝑓 𝑆𝑝ℎ𝑒𝑟𝑒 = 4 π 𝑟2
# 𝑉𝑜𝑙𝑢𝑚𝑒 𝑜𝑓 𝑆𝑝ℎ𝑒𝑟𝑒 = 4 3 π 𝑟3


num=int(input("Enter the number of radius: "))
num1=int(input("Enter the number of radius: "))



def area_of_sphere(radius):
    area = 4 * 3.14 * radius ** 2
    return area

def volume_of_sphere(radius):
    volume = (4 / 3) * 3.14 * radius ** 3
    return volume

print("Area of sphere: ", area_of_sphere(num))
print("Volume of sphere: ", volume_of_sphere(num1))

