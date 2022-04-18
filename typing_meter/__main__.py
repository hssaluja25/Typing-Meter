"""typing_meter."""

from app import App
choice = input("Enter the language you want to practise on: (English/Hindi): ").lower()
if choice == 'English'.lower():
    App()