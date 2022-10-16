BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = 100
lines = 50
chars = 25

total_chars = pages * lines * chars
total_bytes = BYTES_ONE_CHAR * total_chars  # TODO размер одной книги в байтах

disk_size = 1.44 * 1024 * 1024

print(disk_size // total_bytes)  # TODO найти количество книг, которое поместится на дискете
