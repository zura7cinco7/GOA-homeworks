# 1) შექმენით ფუნქცია, manual_capitalize რომელიც იქნება capitalize ფუნქციის კლონი
#2) შექმენით ფუნქცია, manual_title, რომელიც იქნება title ფუნქციის კლონი

def manual_capitalize(z):
 
    if len(z) == 0:
        return z

    return z[0].upper() + z[1:].lower()

print(manual_capitalize("hello")) 
print(manual_capitalize("i"))  
print(manual_capitalize("am"))  
print(manual_capitalize("zura"))  
print(manual_capitalize(""))      


def manual_title(zuka):

    return ' '.join([word.capitalize() for word in zuka.split()])


print(manual_title("hello teacher")) 
print(manual_title("this is my klasswork")) 
