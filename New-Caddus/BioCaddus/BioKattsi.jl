println("BioKattsi (Testing)")
print("Your Name: ")
name = readline()
A0 = [1, 0]
A1 = [1, 5]
#virus
counterex = 1
virus = [1, counterex]
while counterex != 5
    global counterex += 1
    global virus = [1, counterex]
end
if virus == [1, 5]
    sleep(0.1)
    println("ACERTOU")
end