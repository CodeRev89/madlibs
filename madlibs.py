from typing import ItemsView
from unicodedata import name


def main():
	name = input ("enter name: ").capitalize()
	time = input ("enter time:")
	item =input ("enter item:")
	scream = input ("scream here:").upper()
	action = input ("do an action:")
	print (f"hi my name is  {name}, it is currently {time}, I am currently carrying my  {item}, but just incase you didnt hear me, MY NAME IS {scream}, and im about to go {action} ")
if __name__ == '__main__':
	main()