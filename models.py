from pony.orm import Database, PrimaryKey, Required, db_session

db = Database()
db.bind(provider='sqlite', filename='BookRentalDB.db', create_db=True)


class Book(db.Entity):
    id = PrimaryKey(int, auto=True)
    book_title = Required(str)
    book_author = Required(str)
    book_genre = Required(str)
    book_rating = Required(int)
    book_price = Required(float)
    book_availability = Required(str)

    @staticmethod
    def add_book(book_title, book_author, book_genre, book_rating, book_price):
        with db_session:
            return Book(book_title=book_title, book_author=book_author, book_genre=book_genre,
                        book_rating=book_rating, book_price=book_price, book_availability="yes")

    @staticmethod
    def delete_book(book_title):
        with db_session:
            Book.select(lambda b: b.book_title == book_title).delete(bulk=True)


db.generate_mapping(create_tables=True)
