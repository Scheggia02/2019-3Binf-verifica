from Book import Book

book_01 = Book("Eugenio Onegin", "Aleksandr Puškin", "Rizzoli", 2010, 340, "IT\\ICCU\\ANA\\0345144")
book_02 = Book("Utz", "Bruce Chatwin", "La Biblioteca Di Repubblica", 2003, 126, "IT\\ICCU\\CAG\\0429141")
catalog = [book_01, book_02]

def get_books_list():
    return catalog