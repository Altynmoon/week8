
def cat_dog(str):
    a = str.split('cat') 
    b = str.split('dog')  
    if len(a) == len(b):
        return True
    else:
        return False
