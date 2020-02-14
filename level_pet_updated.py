import pyautogui
import image
import time
import random

## List of position on screen to launch marco records from android emulator
## pyautogui.moveTo(2280, 140) 寵食小
## pyautogui.moveTo(2280, 175) 寵食大
## pyautogui.moveTo(2280, 210) 全寵加
## pyautogui.moveTo(2280, 245) 加體
## pyautogui.moveTo(2280, 280) 加靈
## pyautogui.moveTo(2280, 315) 加敏
## pyautogui.moveTo(2280, 350) 加力


def bag_pet():
    time.sleep(2+random.random()*2)

    pyautogui.click(1670, 415)  # open bag
    time.sleep(2+random.random()*2)

    for i in range(30):
        pyautogui.click(1300, 438)  # consume pet item
    time.sleep(1.5+random.random())

    pyautogui.click(1750, 150)  # cancel extra prompt
    time.sleep(0.5 + random.random() * 2)
    pyautogui.click(1750, 150)  # close bag
    time.sleep(0.5 + random.random() * 2)
    pyautogui.click(1750, 150)  # open map
    time.sleep(0.5 + random.random() * 2)

    pyautogui.click(1770, 100)  # close map
    time.sleep(1 + random.random() * 2)

    pyautogui.click(570, 110)  # open pet screen
    time.sleep(2+random.random()*2)


def add_stat(index):
    if index == 0:
        pyautogui.click(2280, 350)  # 加力/str
    elif index == 1:
        pyautogui.click(2280, 315)  # 加敏/agi
    elif index == 2:
        pyautogui.click(2280, 245)  # 加體/sta
    elif index == 3:
        pyautogui.click(2280, 280)  # 加靈/int


def train_6():
    time.sleep(0.5 + random.random())

    pyautogui.click(330, 720)  # 尾寵/select last pet
    time.sleep(0.5 + random.random())

    pyautogui.click(1700, 500)  # 培養/train screen
    time.sleep(0.5 + random.random())

    pyautogui.click(1300, 840)  # 培養-選石/pick item 2
    time.sleep(0.5 + random.random())

    pyautogui.click(1320, 650)  # 培養-使用/use item
    time.sleep(0.5 + random.random())

    for i in range(5):
        pyautogui.click(330, 720)  # 尾寵/select last pet
        time.sleep(0.5 + random.random())

        pyautogui.click(1700, 500)  # 培養/train screen
        time.sleep(0.5 + random.random())

        pyautogui.click(1320, 650)  # 培養-使用/use item
        time.sleep(0.5 + random.random())

    pyautogui.click(1675, 250)  #精靈屬/stats screen
    time.sleep(1.5 + random.random())


def add_stat_release():
    for i in range(6):

        time.sleep(1 + random.random())
        pyautogui.click(230, 460)  #頭寵/select first pet
        time.sleep(0.5 + random.random())

        pyautogui.click(1675, 250)  #精靈屬/stats screen
        time.sleep(1.5 + random.random())

        image.screenshot()
        time.sleep(0.5 + random.random())

        stat_list = image.get_stats()
        time.sleep(0.5 + random.random())

        stat_max_ind = stat_list.index(max(stat_list))

        add_stat(stat_max_ind)
        time.sleep(10 + random.random())

        image.screenshot()
        time.sleep(0.5 + random.random())

        power = image.get_power()
        time.sleep(0.5 + random.random())

        if power < 3400:
            if power < 3000:
                while power < 3000:
                    time.sleep(0.5 + random.random())

                    pyautogui.click(1700, 500)  # 培養/training screen
                    time.sleep(0.5 + random.random())

                    image.screenshot()
                    time.sleep(0.5 + random.random())

                    old_level = image.get_level()

                    pyautogui.click(1130, 840)  # 培養-選粉/select item 1
                    # pyautogui.click(1300, 840)  # 培養-選石/select item 2
                    time.sleep(0.5 + random.random())

                    pyautogui.click(1320, 650)  # 培養-使用/use item
                    time.sleep(0.5 + random.random())

                    image.screenshot()
                    time.sleep(0.5 + random.random())

                    new_level = image.get_level()
                    time.sleep(0.5 + random.random())

                    while new_level == old_level:
                        pyautogui.click(1320, 650)  # 培養-使用/use item
                        time.sleep(0.2 + random.random())

                        image.screenshot()
                        time.sleep(1 + random.random())
                        new_level = image.get_level()
                        time.sleep(0.5 + random.random())

                    pyautogui.click(1675, 250)  # 精靈屬/stat screen
                    time.sleep(2 + random.random())

                    image.screenshot()
                    time.sleep(0.5 + random.random())

                    power = image.get_power()
                    time.sleep(0.5 + random.random())

                    if power < 3000:
                        add_stat(stat_max_ind)
                        time.sleep(10 + random.random())

                        image.screenshot()
                        time.sleep(0.5 + random.random())

                        power = image.get_power()
                        time.sleep(0.5 + random.random())

            # release pet
            pyautogui.click(1130, 950)  # 放生1
            time.sleep(0.5 + random.random())
            pyautogui.click(1130, 800)  # 放生2
            time.sleep(0.5 + random.random())
        else:
            while power < 5000:
                if power < 4850:
                    pyautogui.click(1700, 500)  # 培養/training screen
                    time.sleep(0.5 + random.random())

                    pyautogui.click(1300, 840)  # 培養-選石/select item 2
                    time.sleep(0.5 + random.random())

                    if power < 4500:
                        # use item based on approximate number of times needed to get to 5000 power
                        for k in range(int((5000-power)/280)):
                            pyautogui.click(1320, 650)  # 培養-使用/use item
                            time.sleep(0.3 + random.random())
                    else:
                        pyautogui.click(1320, 650)  # 培養-使用/use item
                        time.sleep(0.3 + random.random())

                    pyautogui.click(1675, 250)  # 精靈屬/stat screen
                    time.sleep(0.5 + random.random())

                    add_stat(stat_max_ind)
                    time.sleep(10 + random.random())

                    image.screenshot()
                    time.sleep(0.5 + random.random())

                    power = image.get_power()
                    time.sleep(0.5 + random.random())
                else:
                    time.sleep(0.5 + random.random())

                    pyautogui.click(1700, 500)  # 培養/training screen
                    time.sleep(0.5 + random.random())

                    image.screenshot()
                    time.sleep(0.5 + random.random())

                    old_level = image.get_level()

                    pyautogui.click(1300, 840)  # 培養-選石/select item 2
                    time.sleep(0.5 + random.random())

                    pyautogui.click(1320, 650)  # 培養-使用/use item
                    time.sleep(0.5 + random.random())

                    image.screenshot()
                    time.sleep(0.5 + random.random())

                    new_level = image.get_level()
                    time.sleep(0.5 + random.random())

                    while new_level == old_level:
                        pyautogui.click(1320, 650)  # 培養-使用/use item
                        time.sleep(0.2 + random.random())

                        image.screenshot()
                        time.sleep(0.2 + random.random())
                        new_level = image.get_level()
                        time.sleep(0.5 + random.random())

                    pyautogui.click(1675, 250)  # 精靈屬/stat screen
                    time.sleep(2 + random.random())

                    image.screenshot()
                    time.sleep(0.5 + random.random())

                    power = image.get_power()
                    time.sleep(0.5 + random.random())

                    if power < 5000:
                        add_stat(stat_max_ind)
                        time.sleep(10 + random.random())

                        image.screenshot()
                        time.sleep(0.5 + random.random())

                        power = image.get_power()
                        time.sleep(0.5 + random.random())

            # release pet
            pyautogui.click(1130, 950)  # 放生1
            time.sleep(0.5 + random.random())
            pyautogui.click(1130, 800)  # 放生2
            time.sleep(0.5 + random.random())

    pyautogui.click(1750, 140)  # 關背包/close bag
    time.sleep(2+random.random()*2)


def repeat_run():
    user_in = input("Number of pets to be released：")
    # determine the number of times the program need to run based on number of pets
    count = int(int(user_in)/6)

    for i in range(count):
        bag_pet()
        train_6()
        add_stat_release()


repeat_run()
