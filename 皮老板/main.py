# 导入 Python 的 random 模块，用于生成随机数
import random

# 定义一个名为 GameCharacter 的类，用于创建游戏中角色的基本属性和行为
class GameCharacter:
    # 生命值初始为 400
    HP = 400
    # 攻击力初始为 200
    attack_power = 200

    def __init__(self, name):
        self.name = name

    # 处理角色的防御行为
    def defend(self, command):
        # 如果防御指令为 1，打印角色进入格挡姿态的消息，并返回 0.5 作为防御效果
        if command == 1:
            print(f"{self.name} is in a blocking stance ~")
            return 0.5
        # 如果防御指令为 2，打印角色尝试闪避的消息，并随机返回 0.3 或 1 作为防御效果
        elif command == 2:
            print(f"{self.name} tries to dodge the attack ~")
            return random.choice([0.3, 1])

class Warrior(GameCharacter):
    def attack(self, command):
        # 如果攻击指令为 1，打印战士执行突刺攻击的消息，并返回 200 作为攻击力
        if command == 1:
            print(f"{self.name} performs a thrust attack!!")
            return 200
        # 如果攻击指令为 2，打印战士执行回旋挥砍的消息，并随机返回 300 或 100 作为攻击力
        elif command == 2:
            print(f"{self.name} executes a spinning slash!")
            return random.choice([300, 100])

class Monster(GameCharacter):
    def attack(self, command):
        # 如果攻击指令为 1，打印怪物使用爪击攻击的消息，并返回 180 作为攻击力
        if command == 1:
            print(f"{self.name} uses a claw attack!")
            return 180
        # 如果攻击指令为 2，打印怪物喷吐毒液的消息，并随机返回 320 或 100 作为攻击力
        elif command == 2:
            print(f"{self.name} sprays venom!")
            return random.choice([320, 100])

# 输入玩家的姓名
player_name = input("Please enter your name: ")
# 创建 Warrior(战士)类的实例，并传入输入的姓名
player = Warrior(player_name)
# 创建 Monster 类的实例，命名为 "Goblin"
enemy = Monster("Goblin")
# 生成一个随机数，用于决定怪物的攻击指令
random_command = random.choice([1, 2])

while True:
    attack_command = int(input("Enter your attack command (1) Normal Attack (2) Special Attack: "))
    # 调用 player 的 attack 方法，并获取攻击力
    player_attack_power = player.attack(attack_command)

    # 调用 enemy 的 defend 方法，传入随机生成的指令，计算 player 攻击对 enemy 造成的伤害
    damage = int(enemy.defend(random_command) * player_attack_power)

    # 从 enemy 的 HP 中减去计算出的伤害
    enemy.HP -= damage

    # 从 enemy 的 HP 中减去计算出的伤害
    if enemy.HP <= 0:
        print(f"{enemy.name} has fallen, {player.name} wins!")
        break
    # 打印 enemy 受到的伤害和剩余 HP
    else:
        print(f"{enemy.name} took {damage} damage! HP remaining {enemy.HP}")
    print("")

    # 输入防御指令，并将其转换为整数
    defend_command = int(input("Enter your defense command (1) Block (2) Dodge: "))

    # 调用 enemy 的 attack 方法，传入随机生成的指令，获取 enemy 的攻击力
    enemy_attack_power = enemy.attack(random_command)

    # 根据输入的防御指令，调用 player 的 defend 方法，并计算 enemy 攻击对 player 造成的伤害
    damage = int(player.defend(defend_command) * enemy_attack_power)

    # 从 player 的 HP 中减去计算出的伤害
    player.HP -= damage
    # 如果 player 的 HP 小于等于 0，打印游戏结束的消息并退出循环
    if player.HP <= 0:
        print(f"{player.name} has been defeated, game over ~")
        break
    # 打印 player 受到的伤害和剩余 HP
    else:
        print(f"{player.name} took {damage} damage! HP remaining {player.HP}")
    print("")

'''
这是中文版，比较好理解
import random
class 游戏角色:
    生命值 = 400
    攻击力 = 200

    def __init__(self, 姓名):
        self.姓名 = 姓名

    def 防御(self, 指令):
        if 指令 == 1:
            print(f"{self.姓名}摆出了格挡姿势 ~")
            return 0.5
        elif 指令 == 2:
            print(f"{self.姓名}尝试闪避攻击 ~")
            return random.choice([0.3,1])

class 战士(游戏角色):
    def 攻击(self, 指令):
        if 指令 == 1:
            print(f"{self.姓名}使出了突刺攻击！！")
            return 200
        elif 指令 == 2:
            print(f"{self.姓名}奋力使出了回旋挥砍！！")
            return random.choice([300, 100])

class 魔物(游戏角色):
    def 攻击(self, 指令):
        if 指令 == 1:
            print(f"{self.姓名}使出了利爪攻击！！")
            return 180
        elif 指令 == 2:
            print(f"{self.姓名}张出血口喷出了毒液！！")
            return random.choice([320, 100])


玩家姓名 = input("请输入你的姓名：")
玩家 = 战士(玩家姓名)
敌方 = 魔物("哥布林")
随机 = random.choice([1, 2])
while True:
    攻击指令 = int(input("请输入您的攻击指令(1)普通攻击(2)特殊攻击："))
    玩家攻击力 = 玩家.攻击(攻击指令)
    损血 = int(敌方.防御(随机) * 玩家攻击力)
    敌方.生命值 -= 损血
    if 敌方.生命值 <= 0:
        print(f"{敌方.姓名}倒下了，{玩家.姓名}胜利！！")
        break
    else:
        print(f"{敌方.姓名}受到了{损血}伤害！生命值剩下 {敌方.生命值}")
    print("")

    防御指令 = int(input("请输入您的防御指令(1)格挡(2)闪避："))
    敌方攻击力 = 敌方.攻击(随机)
    损血 = int(玩家.防御(防御指令) * 敌方攻击力)
    玩家.生命值 -= 损血
    if 玩家.生命值 <= 0:
        print(f"{玩家.姓名}受伤过重倒下了，游戏结束 ~")
        break
    else:
        print(f"{玩家.姓名}受到了{损血}伤害！生命值剩下 {玩家.生命值}")
    print("")
'''
