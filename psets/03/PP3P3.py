#I want you to know I considered do this all with inline ternary operators
print ("Think of a SBC. ")
print ("Options are Raspberry Pi 2b, Raspberry Pi zero W, Arduino Uno, Arduino Leonardo")
if (input ("Is there food in the name? ").lower()=='yes'):
    if (input ("Native wireless networking? ").lower()=='yes'):
        print ("Pi zero")
    else:
        print ("Pi 2b")   
else: #Arduino
    if (input ("Native USB HID emulation? ").lower()=='yes'):
        print ("Leonardo")
    else:
        print ("Uno")