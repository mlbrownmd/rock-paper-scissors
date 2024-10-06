def on_gesture_shake1():
    global hand1
    hand1 = 0
    if hand1 == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand1 == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake1)
led.set_display_mode(DisplayMode.BLACK_AND_WHITE)
def on_gesture_shake2():
    global hand2
    hand2 = randint(1, 3)
    if hand2 == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand2 == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake2)
basic.show_number(hand1)
basic.show_number(hand2)
if hand1 == hand2:
    basic.show_string("Tie!")
if hand1 > hand2:
    basic.show_string("Hand1 Wins!")
else:
    basic.show_string("Hand2 Wins!")