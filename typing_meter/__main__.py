"""typing_meter."""

from app import App
choice = input("Enter the language you want to practise on: (English/Hindi): ")
if choice == 'Hindi':
    pass
else:
    mode = input("Enter the mode (practise/exam): ")
    if mode == 'practise':
        App()
    else:
        print("To be implemented")