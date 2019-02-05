names="abhay,jay,veeru,suru,anna,essakar"
li = names.split(",")
li_copy = names.split(",")
print li
for name in li_copy:
    if name.find("a") > -1:
            li.remove(name)
print "after removing:"
print li

