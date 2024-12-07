import sqlalchemy

from sqlalchemy.orm import sessionmaker

from model import create_tables, Pyblisher, Book, Shop, Sale, Stock

login = input("Введите ваш логин: ")
password = input("Введите ваш пароль: ")
database = input("Введите название вашей базы данных: ")

DSN = f"postgresql://{login}:{password}@localhost:5432/{database}"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publ1 = Pyblisher(name="Стрекоза-Пресс")
publ2 = Pyblisher(name="Манн, Иванов и Фербер")
publ3 = Pyblisher(name="Росмэн")
publ4 = Pyblisher(name="Центрполиграф")
session.add_all([publ1, publ2, publ3, publ4])
session.commit()

b1 = Book(title="Над пропастью во ржи", id_pyblisher=1)
b2 = Book(title="Овод", id_pyblisher=1)
b3 = Book(title="Портрет Дориана Грея", id_pyblisher=1)
b4 = Book(title="Отверженные", id_pyblisher=2)
b5 = Book(title="Война и мир", id_pyblisher=2)
b6 = Book(title="Унесённые ветром", id_pyblisher=2)
b7 = Book(title="Гроздья гнева", id_pyblisher=3)
b8 = Book(title="Сто лет одиночества", id_pyblisher=3)
b9 = Book(title="Маленький принц", id_pyblisher=3)
b10 = Book(title="Гордость и предубеждение", id_pyblisher=4)
b11 = Book(title="Повелитель мух", id_pyblisher=4)
b12 = Book(title="Лед и пламя", id_pyblisher=4)
session.add_all([b1, b2, b3, b4, b5, b6, b7, b8, b9, b9, b10, b11, b12])
session.commit()

sh1 = Shop(name="Литрес")
sh2 = Shop(name="Book24")
sh3 = Shop(name="Буквоед")
sh4 = Shop(name="Майшоп")
session.add_all([sh1, sh2, sh3, sh4])
session.commit()

st1 = Stock(id_book=1, id_shop=1, count=57)
st2 = Stock(id_book=2, id_shop=1, count=42)
st3 = Stock(id_book=3, id_shop=1, count=28)
st4 = Stock(id_book=4, id_shop=2, count=62)
st5 = Stock(id_book=5, id_shop=2, count=133)
st6 = Stock(id_book=6, id_shop=2, count=88)
st7 = Stock(id_book=7, id_shop=3, count=7)
st8 = Stock(id_book=8, id_shop=3, count=74)
st9 = Stock(id_book=9, id_shop=3, count=32)
st10 = Stock(id_book=10, id_shop=4, count=96)
st11 = Stock(id_book=11, id_shop=4, count=10)
st12 = Stock(id_book=12, id_shop=4, count=68)
session.add_all([st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11, st12])
session.commit()

s1 = Sale(price="832", date_sale="2024-01-01", id_stock=1, count=2)
s2 = Sale(price="1423", date_sale="2024-02-01", id_stock=2, count=12)
s3 = Sale(price="1789", date_sale="2024-03-01", id_stock=3, count=21)
s4 = Sale(price="500", date_sale="2024-04-01", id_stock=4, count=1)
s5 = Sale(price="5000", date_sale="2024-05-01", id_stock=5, count=30)
s6 = Sale(price="2643", date_sale="2024-06-01", id_stock=6, count=10)
s7 = Sale(price="486", date_sale="2024-07-01", id_stock=7, count=1)
s8 = Sale(price="1000", date_sale="2024-08-01", id_stock=8, count=5)
s9 = Sale(price="3500", date_sale="2024-09-01", id_stock=9, count=14)
s10 = Sale(price="800", date_sale="2024-10-01", id_stock=10, count=3)
s11 = Sale(price="4000", date_sale="2024-11-01", id_stock=11, count=4)
s12 = Sale(price="900", date_sale="2024-12-01", id_stock=12, count=6)
session.add_all([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12])
session.commit()


def get_shops(res_):
    query = (
        session.query(
            Book.title,
            Shop.name,
            Sale.price,
            Sale.date_sale,
        )
        .select_from(Shop)
        .join(Stock)
        .join(Book)
        .join(Pyblisher)
        .join(Sale)
    )
    if res_.isdigit():
        query = query.filter(Pyblisher.id == res_).all()
    else:
        query = query.filter(Pyblisher.name == res_).all()
    print(f"Информация о продажах книг данного издательства в книжных магазинах: ")
    for title, name, price, date_sale in query:
        print(f"{title:<30} | {name:<20} | {price:<5} | {date_sale}")


if __name__ == "__main__":
    res_ = input("Введите ID или название издательства: ")
    get_shops(res_)

session.close()
