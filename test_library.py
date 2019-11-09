from Library import Library
from Book import Book

marconi = Library("IIS Marconi Library", "CIVMA")

def test_name():

    assert (marconi.name == "IIS Marconi Library")
    assert(marconi.sbn_code != "")
    assert len(marconi.catalog) == 0

    harry_potter = Book("Harry Potter e la Pietra Filosofale", "J.K Rownling", "Salani Editore", 1997, 294, 990239089128 )
    marconi.add_book(harry_potter)