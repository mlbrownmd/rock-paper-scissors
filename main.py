def on_gesture_shake():
    global hand1
    hand1 = randint(1, 3)
    if hand1 == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand1 == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)

hand1 = 0
hand2 = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
led.set_display_mode(DisplayMode.BLACK_AND_WHITE)
basic.show_number(hand1)
basic.show_number(hand2)
if hand1 == hand2:
    basic.show_string("Tie!")
if hand1 > hand2:
    basic.show_string("Hand1Wins!")
else:
    basic.show_string("Hand2Wins!")