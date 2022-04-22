"""typing_meter."""
from app import App
choice = input("Enter the language you want to practise on: (English/Hindi): ").lower()
if choice == "hindi":
    import os
    os.chdir("./typing_meter")
    print(os.getcwd())
    from subprocess import call
    call(["python", "__main__.py"])
else:
    App()
