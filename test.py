import os


file_name = "test.txt"
file_size = os.path.getsize(file_name)

print(file_size)
print(file_size/1024)