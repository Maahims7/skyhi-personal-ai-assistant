
import datetime as dt

print("Initializing SkyHi...")
print("=" * 35)

name = input("What is your name? ")
print(f"\nHello {name}! I am SkyHi, your personal assistant.")
print("Type 'help' to see what I can do. Type 'bye' to exit.\n")

while True:
    message = input("You: ").lower().strip()
    now=dt.datetime.now()
    
    if "hello" in message or "hi" in message:
        print(f"SkyHi: Hello {name}! Good to see you.")
    
    elif "time" in message:
        print(f"SkyHi: Current time is {now.strftime('%H:%M:%S')}")
    elif "date" in message:
        print(f"SkyHi: Today is {now.strftime('%d %B %Y')}")
    elif "day"in message:
        print(f"SkyHi: Today is {now.strftime('%A')}")
    elif "name" in message:
        print("SkyHi: I am SkyHi, built by", name)
    elif "help" in message:
        print("SkyHi: I can respond to — hello, name, time, date, day, bye")
    
    elif "bye" in message or "exit" in message:
        print(f"SkyHi: Goodbye {name}! Keep building.")
        break
    
    else:
        print("SkyHi: I am still learning. Try 'help'.")