'''
books.txt 里面的信息:
101,The Dream of the Red Chamber,available
102,Journey to the West,borrowed
103,Water Margin,available
104,Romance of the Three Kingdoms,borrowed
'''

def loadBooks():
    """把 'books.txt' 文件中书籍信息到加载在一个列表的列表中"""
    # 初始化一个空列表 books，用于存储书籍信息
    books = []
    try:
        with open("books.txt") as file:
            for line in file:
                # 去除每行末尾的换行符，并根据逗号将行分割成一个列表 book
                book = line.strip().split(",")
                # 将分割后的书籍信息列表添加到 books 列表中
                books.append(book)
    except FileNotFoundError as e:
        print("Error: The file 'books.txt' was not found.", e)
    except Exception as e:
        print("An error occurred:", e)

    return books

def printBooks(books):
    """打印数据库中的所有书籍记录"""
    for book in books:
        # 打印每本书的 ID、标题 和 状态
         print("book:", book[0], "-", book[1], "-", book[2])

def addBook(books):
    """将一本新书添加到数据库中"""
    bookId = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    status = input("Enter Availability Status (available/borrowed): ")
    # 检查 bookId、title 和 status 是否为空
    while "" in [bookId, title, status]:
        print("Enter error, please enter again!")
        bookId = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        status = input("Enter Availability Status (available/borrowed): ")
    # 将新书记录添加到书籍列表中
    newBook = [bookId, title, status]
    books.append(newBook)
    printBooks(books)

    return books

def deleteBook(books, bookId):
    """根据书籍编号从数据库中删除一本书"""
    # 用于标记是否找到并删除了书籍
    bookFound = False
    for book in books:
        # 要把 bookId 转换为 str，因为函数传入的参数 bookId 为整型
        if book[0] == str(bookId):
            books.remove(book)
            bookFound = True
            break
    if bookFound:
        print("Book with ID", bookId, "has been deleted.")
    else:
        print("No book with ID", bookId, "found.")
    printBooks(books)

    return books

def searchBook(books, title):
    """通过标题搜索书籍并打印其可用状态"""
    bookFound = False
    for book in books:
        if book[1] == title:
            # 因为要打印寻找目标 book 的 3 个信息，所以不能最后做判断，然后打印信息
            print("Book found:", book)
            bookFound = True
            break
    if not bookFound:
        print("Book not found.")

def saveBooks(books):
    """将书籍记录保存到 'newBooks.txt' 文件中"""
    try:
        with open("newBooks.txt", "w") as file:
            for book in books:
                # 不要忘掉 , 和 \n，特别是 \n, 没写这个，信息会在写在同一行
                bookString = book[0] + "," + book[1] + "," + book[2] + "\n"
                file.write(bookString)
            print("Save to file newBooks.txt correctly")
    except Exception as e:
        print("An error occurred while saving:", e)

books = loadBooks()           # 加载书籍
printBooks(books)             # 列出所有书籍记录
books = addBook(books)        # 添加书籍记录
books = deleteBook(books, 103) # 删除书籍记录
searchBook(books, "The Dream of the Red Chamber")  # 搜索书籍
saveBooks(books)              # 保存书籍记录
