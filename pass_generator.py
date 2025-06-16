import random
import string 


def pass_generator(min_chars,max_chars,digit=True,special=True):
    letters=string.ascii_letters
    digits=string.digits
    specials=string.punctuation
    
    characters=letters
    if digit:
        characters+=digits
    if special:
        characters+=specials
    done=False
    hasd=False
    hass=False

    psw=''
    try:
        length=random.randint(min_chars,max_chars)

        while not done or len(psw)<length  :
            psw+=characters[random.randint(0,len(characters)-1)]
            if digit and special:
                for i in psw:
                    if i in digits:
                        hasd=True
                    if i in specials:
                        hass=True
                if hasd and hass:
                    done=True
            elif digit :
                for i in psw:
                    if i in digits:
                        hasd=True
                if hasd :
                    done=True
            else:
                done=True
            
        return psw
    except ValueError:
        print('value error')
        
    


print(pass_generator(9,19,True,True))