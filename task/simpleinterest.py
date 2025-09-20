# Write a program to calculate simple and
# compound interest.
# 𝑆𝑖𝑚𝑝𝑙𝑒 𝐼𝑛𝑡𝑒𝑟𝑒𝑠𝑡 = 𝑃 * 𝑅 * 𝑇
# 100
# 𝐶𝑜𝑚𝑝𝑜𝑢𝑛𝑑 𝐼𝑛𝑡𝑒𝑟𝑒𝑠𝑡 = 𝑃 * 1 + 𝑅
# ( 100 * 𝑛 )𝑛 * 𝑇

p=int(input("Enter the principle amount:"))
r=int(input("Enter the rate of interest:"))
t=int(input("Enter the time:"))

simple_intrest =(p*r*t)/100
compound_intrest = p*(1+r/100)**t

print("Simple Intrest is:",simple_intrest)
print("Compound Intrest is:",compound_intrest)

