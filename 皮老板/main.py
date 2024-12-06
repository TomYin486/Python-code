# 定义 Customer 类
class Customer:
    # 创建 Customer 对象时初始化属性
    def __init__(self, name, ID):
        self._name = name        # 客户的名字
        self._ID = ID            # 客户的唯一标识符
        self._loyaltyPoints = 0  # 客户的忠诚度积分，初始化为 0

    # 获取客户名字
    def getName(self):
        return self._name

    # 获取客户 ID
    def getID(self):
        return self._ID

    # 显示客户忠诚度积分
    def showPoints(self):
        return self._loyaltyPoints

    # 更新客户忠诚度积分，参数 purchaseAmount 为消费金额
    def updatePoints(self, purchaseAmount):
        self._loyaltyPoints += purchaseAmount / 10  # 将消费金额除以 10，得到积分，并累加到 _loyaltyPoints

# 获取用户输入的命令
def getUserCommand():
    print("\nWhat do you want to do next?")
    print("1. Display all customers")        # 选项1： 显示所有客户信息
    print("2. Add a new customer")           # 选项2： 添加一个新的客户
    print("3. Update loyalty points for a customer")  # 选项3： 更新某个客户的忠诚度积分
    print("4. Remove a customer")            # 选项4： 删除一个客户
    print("5. Update customer information")  # 选项5： 更新客户信息
    print("0. Exit")                         # 选项0： 退出程序
    while True:  # 循环直到输入有效的命令
        command = input("Please enter your choice (1 - 5 for options, 0 to exit): ")
        if command.isdigit() and 0 <= int(command) <= 5:  # 检查输入是否为数字且在 0 - 5 之间
            return int(command)  # 返回输入的命令作为整数
        else:
            # 如果输入无效，提示重新输入
            print("Invalid input, please enter a number between 0 and 5.")

# 显示数据库中的所有客户信息
def displayCustomers(customerDB):
    # 如果客户数据库为空，打印没有客户信息
    if not customerDB:
        print("No customers in the database.")
    else:
        # 遍历客户数据库中的每个客户
        for ID, customer in customerDB.items():
            # 打印客户 ID、名字和积分
            print(f"ID: {ID}, Name: {customer.getName()}, Loyalty Points: {customer.showPoints()}")

# 添加新客户到数据库
def addCustomer(customerDB):
    while True:  # 循环直到用户输入一个唯一的 ID
        ID = input("Enter the new customer's ID: ")
        # 检查 ID 是否已经存在于数据库中
        if ID in customerDB:
            # 如果 ID 已被占用，提示用户
            print("ID already exists. Please try a different ID.")
        else:
            # 如果 ID 唯一，跳出循环
            break
    while True:  # 循环直到输入一个非空的名字
        name = input("Enter the new customer's name: ")
        # 如果名字不为空，跳出循环
        if name:
            break
        else:
            # 如果名字为空，打印提示
            print("Name cannot be empty.")
    customerDB[ID] = Customer(name, ID)  # 创建新的客户对象并添加到数据库
    print(f"Customer {name} added with ID {ID}.")  # 打印添加成功的信息

# 更新客户的忠诚度积分
def updatePoints(customerDB):
    while True:  # 循环直到输入一个存在的客户 ID
        customerID = input("Enter the customer's ID to update loyalty points: ")
        # 如果客户 ID 存在于数据库中
        if customerID in customerDB:
            break  # 跳出循环
        else:
            # 如果客户 ID 不存在，提示用户
            print("Customer not found. Please try again.")
    while True:  # 循环直到输入一个有效的消费金额
        try:
            amount = float(input(f"Enter the amount spent by {customerDB[customerID].getName()}: "))
            customerDB[customerID].updatePoints(amount)  # 更新客户的积分
            print(f"Updated {customerDB[customerID].getName()}'s points successfully.")  # 打印更新成功的信息
            break  # 跳出循环
        except ValueError:  # 如果输入不是有效的数字，提示输入有效的数字
            print("Invalid amount. Please enter a valid number.")

# 从数据库中删除客户
def removeCustomer(customerDB):
    while True:  # 循环直到输入一个存在的客户 ID
        customerID = input("Enter the customer's ID to remove: ")
        # 如果客户 ID 存在于数据库中，删除客户
        if customerID in customerDB:
            del customerDB[customerID]
            print("Customer removed successfully.")  # 打印删除成功的信息
            break
        else:
            # 如果客户 ID 不存在，打印提示
            print("Customer not found. Please try again.")

# 更新客户的信息
def updateCustomerInfo(customerDB):
    while True:  # 循环直到输入一个存在的客户 ID
        customerID = input("Enter the customer's ID to update information: ")
        # 如果客户 ID 存在于数据库中，跳出循环
        if customerID in customerDB:
            break
        else:
            # 如果客户 ID 不存在，打印提示
            print("Customer not found. Please try again.")
    while True:  # 循环直到输入一个非空的新名字
        new_name = input(f"Enter the new name for customer ID {customerID}: ")
        # 如果新名字不为空，更新客户的名字，跳出循环
        if new_name:
            customerDB[customerID]._name = new_name
            break
        else:
            # 如果新名字为空，打印提示
            print("Name cannot be empty.")
    print(f"Customer information updated successfully.")  # 打印更新成功的信息

# 使用空字典初始化客户数据库
customerDB = {}

# 获取用户命令
userCommand = getUserCommand()
# 循环直到选择退出程序
while userCommand != 0:
    if userCommand == 1:
        displayCustomers(customerDB)    # 显示所有客户
    elif userCommand == 2:
        addCustomer(customerDB)         # 添加新客户
    elif userCommand == 3:
        updatePoints(customerDB)        # 更新积分
    elif userCommand == 4:
        removeCustomer(customerDB)      # 删除客户
    elif userCommand == 5:
        updateCustomerInfo(customerDB)  # 更新客户信息

    userCommand = getUserCommand()      # 再次获取输入的命令

print("Bye")
