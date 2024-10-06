let hand1 = 0
let hand2 = 0
input.onGesture(Gesture.Shake, function on_gesture_shake1() {
    
    hand1 = randint(1, 3)
    if (hand1 == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (hand1 == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    
})
led.setDisplayMode(DisplayMode.BlackAndWhite)
input.onGesture(Gesture.Shake, function on_gesture_shake2() {
    
    hand2 = randint(1, 3)
    if (hand2 == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (hand2 == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    
})
basic.showNumber(hand1)
basic.showNumber(hand2)
if (hand1 == hand2) {
    basic.showString("Tie!")
}

if (hand1 > hand2) {
    basic.showString("Hand1 Wins!")
} else {
    basic.showString("Hand2 Wins!")
}

