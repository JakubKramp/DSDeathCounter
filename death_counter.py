import mss
import time

bounding_box = {'top': 100, 'left': 0, 'width': 400, 'height': 300}


i = 0
while True:
    with mss.mss() as sct:
        time.sleep(5)
        i += 1
        # The screen part to capture
        monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
        output = f'file{i}'

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)
