import random



length=int(input("Please enter password/key length (16+ recommended): "))
print()
print("Your Password: ",end="")
for i in range(0,length):
  print(chr(random.randint(33,126)),end="" )

print()
print()
