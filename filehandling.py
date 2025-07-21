file_noparam = open("testfile.txt")

file_default = open("testfile.txt","rt")



# "r" - read	if not exists, error
# 				FileNotFoundError: [Errno 2] No such file or directory: 'testfile.txt'
# "a" - append	if not exists, create
# "w" - write	if not exists, create
# "x" - create	if exists, error


# "t" - text
# "b" - binary


print(type(file_default))
print(file_default.read())