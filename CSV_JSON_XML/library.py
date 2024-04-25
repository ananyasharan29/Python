import csv
import json

# with open('library.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for r in reader:
#         print(r)

books = []

with open('library.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        books.append({
            'BookName': row['BookName'], 
            'AuthoName': row['AuthorName'],
            'PublisherName': row['PublisherName'],
            'NumberofCopies': int(row['NumberofCopies']) 
        })

max_copies_book = max(books, key=lambda x: x['NumberofCopies'])
min_copies_book = min(books, key=lambda x: x['NumberofCopies'])

with open('max_copies_book.json', 'w') as json_file:
    json.dump(max_copies_book, json_file, indent=4)

with open('min_copies_book.json', 'w') as json_file:
    json.dump(min_copies_book, json_file, indent=4)
