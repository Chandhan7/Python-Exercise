# Opening sample_file.txt in write mode
with open("sample_file.txt", "w") as file:
    file.write("Hello World\n")
    file.write("Hello Python\n")
    file.close()

# Opening sample_file.txt in read mode
with open("sample_file.txt", "r") as file:
    print(file.read())
    # print(file.readline())

# Opening sample_file.txt in append mode
with open("sample_file.txt", "a") as file:
    (file.write("Line is added"))
