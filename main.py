def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.pause(2000)
    basic.show_string("Hello")
basic.forever(on_forever)
