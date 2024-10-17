page = 100
string = 50
symbol = 25
disk = 1.44
book_size = 4 * (string * symbol * page)
size_kilo = book_size / 1024
size_mega = size_kilo / 1024
number_of_books = int(disk // size_mega)
print("Количество книг, помещающихся на дискету:", number_of_books)
