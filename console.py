import pdb
from models.author import Author
from models.book import Book
import repositories.author_repository  as author_repository

author_repository.delete_all()

author_1 = Author("C.S. Lewis")
author_2 = Author("Tom Clancy")
author_3 = Author("James Patterson")
author_repository.save(author_1)
author_repository.save(author_2)
author_repository.save(author_3)

book1 = Book("The Lion, the Witch and The Wardrobe", author_1)
book2 = Book("Prince Caspian", author_1)
book_3 = Book("Rainbow Six", author_2)
book_4 = Book("Red Winter", author_2)
book_5 = Book("Fear No Evil", author_3)
book_6 = Book("Shattered", author_3)

# results = author_repository.select_all()
# for author in results:
#     print(author.__dict__)

pdb.set_trace()