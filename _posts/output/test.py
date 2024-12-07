import random
import unittest

result = {0: "정답", 1: "Up", 2: "dwon"}
# 스무고개 게임 + test코드


# 프로그램 실행시 랜덤으로 1~100사이의 숫자 생성
def check(player_num, computer_num):
    if player_num - computer_num == 0:
        return 0
    elif player_num - computer_num < 0:
        return 1
    else:
        return 2


def have_health(health_par):
    if health_par == 0:
        return True
    else:
        return False


def out_numcheck(num):
    if num not in range(1, 101):
        return True
    else:
        return False


random_number = random.randint(1, 101)
health = 10
while True:
    input_number = int(input("1~100사이의 숫자를 입력하세요"))
    if out_numcheck(input_number):
        print("숫자 잘못 입력")
    else:
        print(result[check(input_number, random_number)])
        if check(input_number, random_number) == 0:
            break
        else:
            health -= 1

    if have_health(health) is True:
        print("게임종료 (기회소진)")
        break


class test(unittest.TestCase):
    def test_current(self):  # 정답 체크
        self.assertAlmostEqual(check(1, 1), 0)

    def test_input_up(self):  # 사용자가 랜덤숫자보다 큰 수를 입력한 경우
        self.assertAlmostEqual(check(2, 1), 2)

    def test_input_down(self):  # 사용자가 랜덤숫자보다 작은 수를 입력한 경우
        self.assertAlmostEqual(check(1, 2), 1)

    def test_health_check(self):  # 10번의 기회가 정상적으로 감소하는 기능 테스트
        self.assertAlmostEqual(have_health(10), False)
        self.assertAlmostEqual(have_health(0), True)


if __name__ == "__main__":
    unittest.main()
