import psutil
from thefuzz import fuzz
import pytesseract
import constants
import cv2

def detect_boss(cache):
    for image in cache:
        for boss in constants.DARK_SOULS_BOSSES.values():
            if isinstance(boss, str):
                if fuzz.ratio(pytesseract.image_to_string(image), boss) > constants.BOSS_FUZZ_THRESHOLD:
                    return boss
            else:
                for enemy in boss:
                    if fuzz.ratio(pytesseract.image_to_string(image), enemy) > constants.BOSS_FUZZ_THRESHOLD:
                        return enemy
    return 'Other'

def detect_death(image):
    template = cv2.imread('img.png')
    img = cv2.imread(image)
    res = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val)
    if max_val > constants.DEATH_THRESHOLD:
        return True
    return False

def detect_game():
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            if processName in constants.GAMES.keys():
                return constants.GAMES[processName]
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass