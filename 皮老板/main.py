class Book:  # 图书类
    """用于表示图书馆中的一本书的类."""

    def __init__(self, title, author, isbn):
        """用标题、作者和ISBN初始化书籍."""
        self._title = title
        self._author = author
        self._isbn = isbn

    def getTitle(self):
        """返回书籍的标题."""
        return self._title

    def getAuthor(self):
        """返回书籍的作者."""
        return self._author

    def getIsbn(self):
        """返回书籍的ISBN编号."""
        return self._isbn

    def setTitle(self, title):
        """设置书籍的标题."""
        self._title = title

    def setAuthor(self, author):
        """设置书籍的作者."""
        self._author = author

    def setIsbn(self, isbn):
        """设置书籍的ISBN编号."""
        self._isbn = isbn

    def displayBookInfo(self):
        """显示书籍的信息."""
        print(f"标题：{self.getTitle()}, 作者：{self.getAuthor()}, ISBN：{self.getIsbn()}")


class Member:  # 成员类
    """用于表示图书馆的成员的类."""

    def __init__(self, name):
        """用名字初始化成员，并创建一个空的借阅书籍列表."""
        self._name = name
        self._borrowedBooks = []

    def getName(self):
        """返回成员的名字."""
        return self._name

    def getBorrowedBooks(self):
        """返回借阅书籍的列表."""
        return self._borrowedBooks

    def setName(self, name):
        """设置成员的名字."""
        self._name = name

    def setBorrowedBooks(self, borrowedBooks):
        """设置借阅书籍的列表."""
        self._borrowedBooks = borrowedBooks

    def borrowBook(self, book):
        """将一本书添加到成员的借阅书籍列表中."""
        self._borrowedBooks.append(book)

    def returnBook(self, title):
        """通过标题从成员的借阅书籍列表中移除一本书."""
        newBorrowedBooks = []
        for book in self._borrowedBooks:
            if book.getTitle() != title:
                newBorrowedBooks.append(book)
        self._borrowedBooks = newBorrowedBooks

    def displayBorrowedBooks(self):
        """显示所有借阅的书籍."""
        print(f"{self.getName()}借阅的书籍：")
        bookIndex = 1
        for book in self._borrowedBooks:
            print(f"{bookIndex}. 标题：{book.getTitle()}, 作者：{book.getAuthor()}, ISBN：{book.getIsbn()}")
            bookIndex += 1


memberName = input("输入成员的名字：")
member = Member(memberName)

# 循环处理借书
optionBorrow = input('你想借书吗（"Y"继续，其他停止）？')
while optionBorrow == "Y":
    title = input("输入书籍标题：")
    author = input("输入作者名字：")
    isbn = input("输入ISBN编号：")

    # 确保所有字段都已填写
    while "" in [title, author, isbn]:
        print("错误：所有字段必须填写。请重新输入！")
        title = input("输入书籍标题：")
        author = input("输入作者名字：")
        isbn = input("输入ISBN编号：")

    book = Book(title, author, isbn)
    member.borrowBook(book)
    optionBorrow = input('你想再借一本书吗（"Y"继续，其他停止）？')

# 显示所有借阅的书籍
member.displayBorrowedBooks()

# 循环处理还书
optionReturn = input('你想还书吗（"Y"继续，其他停止）？')
while optionReturn == "Y":
    title = input("输入要还的书籍标题：")
    member.returnBook(title)
    optionReturn = input('你想再还一本书吗（"Y"继续，其他停止）？')

# 还书后显示所有借阅的书籍
member.displayBorrowedBooks()
