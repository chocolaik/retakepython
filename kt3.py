import csv


def get_books(filename):
    books = []

    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file, delimiter="|")
        next(reader, None)

        for row in reader:
            if len(row) < 5:
                continue

            book = [
                row[0].strip(),
                row[1].strip(),
                row[2].strip(),
                int(row[3]),
                float(row[4])
            ]

            books.append(book)

    return books


def filtered_books(books, search):
    result = []

    for book in books:
        if search.lower() in book[1].lower():
            result.append([
                book[0],
                book[1] + ", " + book[2],
                book[3],
                book[4]
            ])

    return result


def books_price(books):
    result = []

    for book in books:
        result.append((book[0], book[2] * book[3]))

    return result


books = get_books("books.csv")
filtered = filtered_books(books, "python")
prices = books_price(filtered)

print("Все книги:")
print(books)

print("Книги с python в названии:")
print(filtered)

print("Общая стоимость книг:")
print(prices)
