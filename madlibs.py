from typing import ItemsView
from unicodedata import name


def main():
	name = input ("enter name: ") 
	time = input ("enter time:")
	item =input ("enter item:")
	scream = input ("scream here:")
	print("hi my name is "  + name, "it is currently "  + time, "I am currently carrying my " + item, "but just incase you didnt hear me, MY NAME IS " + scream)
if __name__ == '__main__':
	main()