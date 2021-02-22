import os
try:
    os.system("cp pass.sh /bin/passgen")
    
    print("autofile created!")
    print('''type "passgen" from an directory to access password generator.''')
except Exception as e:
    print(e)
    print("cannot create the autofile")
