
COLOUR_CODES = {"Cyan": "#00ffff", "DarkOliveGreen1": "#caff70",
                "DarkSalmon": "#e9967a", "DeepPink1": "	#ff1493",
                "DarkSlateBlue": "#483d8b", "DarkOrange": "	#ff8c00",
                "bisque1": "#ffe4c4", "aquamarine2": "#76eec6",
                "chartreuse1": "#7fff00"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print("The code for \"{}\" is {}")
    else:
        print("Your code is unavailable")
        colour_name = input("Enter a colour name: ")