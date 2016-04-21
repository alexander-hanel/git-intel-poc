import shutil
import os 
fam = """Adramax 
Ainslot 
Ares
Banbra 
Vkont
Wemon
Yaludle
ZeuS"""
for f in fam.split("\n"):
    name = f.strip("\n") + ".md"
    shutil.copy2("template.md", name)
    os.mkdir(f)
    print " - [%s](./families/%s)" % (f, name)

