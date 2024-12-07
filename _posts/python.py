import random
import unittest

result_num = {
    0: "비김",
    1: "승리",
    2: "패배",
}


def calculate_result(player, computer):
    iswin = (player - computer + 3) % 3
    return result_num[iswin]


player_val = int(input("입력하세요(1:가위,2:바위,3:보)")) - 1

computer_val = random.randint(0, 2)


1
