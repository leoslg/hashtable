#! usr/bin/env python

def hash_f(key):
    return sum(
        index * ord(char) for index, char in enumerate(repr(key), start=1)
    )


print(hash_f(20))

print(hash_f('Python'))

print(hash_f('Lembre-se de que escolher um pool menor de códigos hash aumenta a probabilidade de colisões de códigos hash.'))

print(hash_f(33.43))
