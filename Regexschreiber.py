import clipboard
import keyboard
import time







while True:
    Antwort = input("1. Basis, 2. VisualStudioCode-Regex oder Regex fixen?    Gebe 1 oder 2 ein um deine Antwort zu geben!")
    try:
        Antwort = int(Antwort)
    except:
        pass

    if Antwort == 1:
        Antwort = 0
    elif Antwort == 2:
        Antwort = 1
    elif Antwort == 3:
        Antwort = 2
    else:
        print("bitte gebe entweder 1 für AdminTool ein oder 2 für VisualStudioCode (2nd und 3rd Level) oder alten Regex fixen 3")
    if Antwort == 0 or Antwort == 1 or Antwort == 2:
        print("hi")
        break
    else:
        pass
        
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nTool kann nun genutzt werden!")



if Antwort == 0:  #AdminTool
    def customize_string(input_string):
        result = ""
        i = 0
        while i < len(input_string):
            letter = input_string[i]
            if letter == " " or letter == " ":
                result += "([\\s]?)"
            elif letter in ["ä", "Ä", "ö", "Ö", "ü", "Ü", "ß"]:
                result += "(.|..)"
            elif letter in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`–{|}~€£¥©®°∞∑√±×÷<>≤≥≠≈≡≅≫≪∫∏∈∉∋∀∃∴∵∧∨¬∩∪⊕⊗⊥⌈⌉⌊⌋〈〉◯◻△▲▽▼◀▶↖↗↙↘∠∟∡∢∣∥⊂⊃⊆⊇⊈⊉⊊⊋★☆☉♀♂☼☽☾♠♣♥♦♪♫♯":
                result += "."
            else:
                result += letter
            i += 1
        return "([\\s\\S]*?)"+result

    while True:
        time.sleep(0.002)
        if keyboard.is_pressed("ctrl+alt+shift"):
            time.sleep(0.6)
            input_str = clipboard.paste()
            customized_str = customize_string(input_str)
            print("Originaler String:", input_str)
            print("Angepasster String:", customized_str)
            clipboard.copy(customized_str)
            time.sleep(0.7)



if Antwort == 1:#VisualStudioCode
    def customize_string(input_string):
        result = ""
        i = 0
        while i < len(input_string):
            letter = input_string[i]
            if letter == " " or letter == " ":
                result += "([\\\s]?)"
            elif letter == "\\":
                if i + 1 < len(input_string) and input_string[i + 1] == "n":
                    result += "([\\\s]?)"
                    i += 1  
                else:
                    result += "\\\\"
            elif letter in ["ä", "Ä", "ö", "Ö", "ü", "Ü", "ß"]:
                result += "(.|..)"
            elif letter in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`–{|}~€£¥©®°∞∑√±×÷<>≤≥≠≈≡≅≫≪∫∏∈∉∋∀∃∴∵∧∨¬∩∪⊕⊗⊥⌈⌉⌊⌋〈〉◯◻△▲▽▼◀▶↖↗↙↘∠∟∡∢∣∥⊂⊃⊆⊇⊈⊉⊊⊋★☆☉♀♂☼☽☾♠♣♥♦♪♫♯":
                result += "."
            else:
                result += letter
            i += 1
        return "([\\\s\\\S]*?)"+result


    while True:
        time.sleep(0.006) #chance sollte höher als 98% sein, dass "keyboard.is_pressed" greift
        if keyboard.is_pressed("ctrl+alt+shift"):
            time.sleep(0.3) #because after copying people need some time before they reach ctrl+alt+shift with their hands // delay is needed for input_str = clipboard.paste() to get the right string
            input_str = clipboard.paste()
            customized_str = customize_string(input_str)
            print("Originaler String:", input_str)
            print("Angepasster String:", customized_str)
            clipboard.copy(customized_str)
            time.sleep(1)



if Antwort == 2:  # AdminTool
    def customize_string(input_string):
        result = ""
        i = 0
        while i < len(input_string):
            if input_string[i] == " " or input_string[i] == " ":
                result += "([\\s]?)"
            elif input_string[i] in "äöüßÄÖÜ":
                result += "(.|..)"
            elif input_string[i] in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`–{|}~€£¥©®°∞∑√±×÷<>≤≥≠≈≡≅≫≪∫∏∈∉∋∀∃∴∵∧∨¬∩∪⊕⊗⊥⌈⌉⌊⌋〈〉◯◻△▲▽▼◀▶↖↗↙↘∠∟∡∢∣∥⊂⊃⊆⊇⊈⊉⊊⊋★☆☉♀♂☼☽☾♠♣♥♦♪♫♯":
                result += "."
            else:
                result += input_string[i]
            i += 1
        return result



    while True:
        time.sleep(0.002)
        if keyboard.is_pressed("ctrl+alt+shift"):
            time.sleep(0.6)
            input_str = clipboard.paste()
            customized_str = customize_string(input_str)
            print("Originaler String:", input_str)
            print("Angepasster String:", customized_str)
            clipboard.copy(customized_str)
            time.sleep(0.7)



