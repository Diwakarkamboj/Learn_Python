#Write a python function which converts inches to cms.
#2.54 to convert  inches to cm

def  conv_inch_cms():
    inch = float(input("Enter the length in inches: "))
    cms = inch * 2.54
    return cms

a = conv_inch_cms()
print(a)
