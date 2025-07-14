# NOVA - Text-based Python AI Assistant
import datetime
import random
import webbrowser
import os
import sys

def greet_user():
  greetings = ["Hi there!", "Hello", "Hey!", "Namaste", "Welcome back!"]
  return random.choice(greetings)

def tell_time():
  now = datetime.datetime.now()
  return f"The current time is {now.strftime('%I:%M %p')}"

def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "What did the Python say to the loop? 'You complete me.'",
        "Why was the computer cold? It forgot to close its Windows!"
    ]
    return random.choice(jokes)

def python_tip():
   tips = [
      "Use list comprehensions for cleaner loops.",
      "Remember to use virtual environments for projects.",
      "Use f-strings for better formatting in python 3.6+."
   ]

   return random.choice(tips)

def open_google():
   webbrowser.open("https://www.google.com")
   return "Opening Google..."

def process_command(command):
   command = command.lower()

   if "hello" in command or "hi" in command:
      return greet_user()
   
   elif "time" in command:
      return tell_time()
   
   elif "joke" in command:
      return tell_joke()
   
   elif "tip" in command:
      return python_tip()
   
   elif "google" in command:
      return open_google()
   
   elif command in ["exit", "quit", "bye"]:
      print("NOVA: Goodbye! Have a great day 😊")
      sys.exit()

   else:
      return "Sorry, I didn't understand that. Try something else."  


def main():
   print("Welcome to NOVA - your Python AI Assistant!")
   print("Type something or try: hello, time, joke, tip, google, exit\n")

   while True:
      user_input = input("You: ")
      response = process_command(user_input)
      print(f"NOVA: {response}\n")

if __name__ == "__main__":
   main()      
