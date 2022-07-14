### use rstrip() function to remove blank space
fav_lang='python '
print(fav_lang)
print(fav_lang.rstrip())

### this will not remove the space from the actual variable, only the print.
### to remove space from variable, you will have to revalue the variable

fav_lang = fav_lang.rstrip()
print(fav_lang)

### there is also lstrip(), which removes whitespace from the left side of the variable
fav_lang = ' python '
fav_lang = fav_lang.rstrip().lstrip()
print(fav_lang)