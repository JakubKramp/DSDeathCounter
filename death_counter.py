import mss
import time
from collections import deque
from detectors import detect_death, detect_boss, detect_game
from csv_creator import FileHandler



i = 0
cache = deque([], 5)
f_handler = FileHandler(detect_game())
f_handler.create_file()

while True:
    with mss.mss() as sct:
        time.sleep(1)
        i += 1
        monitor = {"top": 650, "left": 460, "width": 1000, "height": 250}
        output = f'file{i}.jpg'
        cache.extend([output])
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        if detect_death(output):
            boss = detect_boss(cache)
            f_handler.increment_boss(boss)


