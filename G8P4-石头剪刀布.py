import random
# 选手出拳 j 表示剪刀 s 表示石头 b 表示布
player = input(" 请输入你要出的是剪刀 (j), 石头 (s), 还是布 (b)：")

playerPc = random.randint(1, 3)  # 计算机输出 1-3 之间的整数

if playerPc == 1:        # 判断随机数是否为 1
    playerPc = "j"        # 如果为 1 将 playerPc 的值改为 j
    msg = " 剪刀 (j)"      # 设置一个消息变量 msg 赋值为剪刀 (j)

if playerPc == 2:
    playerPc = "s"
    msg = " 石头 (s)"

if playerPc == 3:
    playerPc = "b"
    msg = " 布 (b)"

print(" 电脑出的是 " + msg)    # 打印电脑的手势

#1. 石头 VS 剪刀   4. 剪刀 VS 石头
#2. 布 VS 石头     5. 石头 VS 布
#3. 剪刀 VS 布     6. 布 VS 剪刀
#7. 剪刀 VS 剪刀 布 VS 布 石头 VS 石头
if player == "s" and playerPc == "j":
    print(" 玩家胜利！ ")
if player == "b" and playerPc == "s":
    print(" 玩家胜利！ ")
if player == "j" and playerPc == "b":
    print(" 玩家胜利！ ")
if player == "j" and playerPc == "s":
    print(" 计算机胜利！ ")
if player == "s" and playerPc == "b":
    print(" 计算机胜利！ ")
if player == "b" and playerPc == "j":
    print(" 计算机胜利！ ")
if player == playerPc:
    print(" 平局哦，再战一局！ ")
