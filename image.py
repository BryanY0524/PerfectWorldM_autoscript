import pyautogui
from PIL import Image
import time
import random
import pytesseract
from pytesseract import image_to_string
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def screenshot():
    # take screenshot
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('./screenshot/temp_ss.png')


def get_stats():
    # get pet stats in a list from screenshot
    im = Image.open('./screenshot/temp_ss.png')

    left = 1160
    right = 1231
    str_top = 448
    str_bot_agi_top = 480
    agi_bot_sta_top = 530
    sta_bot_int_top = 571
    int_bot = 625

    str_crop = im.crop((left, str_top, right, str_bot_agi_top))
    agi_crop = im.crop((left, str_bot_agi_top+17, right, agi_bot_sta_top))
    sta_crop = im.crop((left, agi_bot_sta_top, right, sta_bot_int_top))
    int_crop = im.crop((left, sta_bot_int_top, right, int_bot))

    str_stat = image_to_string(str_crop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    agi_stat = image_to_string(agi_crop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    sta_stat = image_to_string(sta_crop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    int_stat = image_to_string(int_crop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

    while str_stat == '' or agi_stat == '' or sta_stat == '' or int_stat == '':
        # redo screenshot when there is an error
        screenshot()
        im = Image.open('./screenshot/temp_ss.png')
        str_crop = im.crop((left, str_top, right, str_bot_agi_top))
        agi_crop = im.crop((left, str_bot_agi_top + 17, right, agi_bot_sta_top))
        sta_crop = im.crop((left, agi_bot_sta_top, right, sta_bot_int_top))
        int_crop = im.crop((left, sta_bot_int_top, right, int_bot))

        str_stat = image_to_string(str_crop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        agi_stat = image_to_string(agi_crop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        sta_stat = image_to_string(sta_crop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        int_stat = image_to_string(int_crop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

    stats = [int(str_stat), int(agi_stat), int(sta_stat), int(int_stat)]
    print(stats)
    for index in range(len(stats)):
        if stats[index] > 5000:
            stats[index] = 1000
        if stats[index] > 4000:
            temp_stat = stats[index] - 3000
            stats[index] = temp_stat

    print(stats)
    return stats


def get_power():
    # get pet power level from screenshot
    im = Image.open('./screenshot/temp_ss.png')
    left = 575
    right = 665
    top = 859
    bot = 893

    power_crop = im.crop((left, top, right, bot))

    power = image_to_string(power_crop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

    while power == '':
        # redo when there is an error
        screenshot()
        im = Image.open('./screenshot/temp_ss.png')

        power_crop = im.crop((left, top, right, bot))

        power = image_to_string(power_crop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

    print(power)
    return int(power)


def get_level():
    # get pet level from screenshot
    im = Image.open('./screenshot/temp_ss.png')

    left = 1160
    right = 1215
    top = 410
    bot = 444

    level_crop = im.crop((left, top, right, bot))
    level = image_to_string(level_crop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    fail_count = 0
    while level == '':
        # redo when there is an error, fail safe hard coded level to keep the
        # programming running due to inaccurate reading from OCR

        screenshot()
        level_crop = im.crop((left, top, right, bot))
        level = image_to_string(level_crop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        fail_count += 1
        print(fail_count)
        if fail_count > 5:
            pyautogui.click(1700, 500)  # 培養
            time.sleep(0.5 + random.random())
            level = '31'

    if int(level) > 60:
        level = '35'
    print(level)
    return int(level)

