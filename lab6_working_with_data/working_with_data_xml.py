from xml.dom import minidom

tree = minidom.parse("sample.xml")
collection = tree.documentElement
books = collection.getElementsByTagName("book")

for book in books:
    title = book.getElementsByTagName("title")[0]
    print("Title:", title.childNodes[0].data)

    author = book.getElementsByTagName("author")[0]
    print("Author:", author.childNodes[0].data)

    genre = book.getElementsByTagName("genre")[0]
    print("Genre:", genre.childNodes[0].data)

    price = book.getElementsByTagName("price")[0]
    print("Price:", price.childNodes[0].data)

    publish_date = book.getElementsByTagName("publish_date")[0]
    print("Publish date:", publish_date.childNodes[0].data)

    description = book.getElementsByTagName("description")[0]
    print("Description:", description.childNodes[0].data)
