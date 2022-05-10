from time import sleep
from lifxlan import BLUE, CYAN, GREEN, LifxLAN, ORANGE, PINK, PURPLE, RED, YELLOW

def rainbow(bulb, duration_secs=0.5, smooth=False):
    colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK]
    transition_time_ms = duration_secs*1000 if smooth else 0
    rapid = True if duration_secs < 1 else False
    for color in colors:
        bulb.set_color(color, transition_time_ms, rapid)
        sleep(duration_secs)

while True:
    while True:
        print("Searching")
        lifx = LifxLAN(verbose=True)
        devices = lifx.get_lights()
        try:
            bulb = devices[0]
            original_power = bulb.get_power()
            original_color = bulb.get_color()
            bulb.set_power("on")

            sleep(1) # for looks

            print("Smooth slow rainbow")
            break
        except:
            print("No Devices Found.")
        sleep(5)
    breaker = 0
    while True:
        try:
            rainbow(bulb, 10, smooth=True)
        except:
            if breaker >= 20:
                break
            else:
                breaker += 1