import time
import sys


# Colours and formatting
endc = '\033[0m'
redbg = '\33[101m'
bold = '\33[1m'
green = '\33[32m'
red = '\33[31m'
whitebg = '\33[107m'
black = '\33[30m'
yellow = '\33[93m'


def countdown():
    """
    Function starts countdown for the pomodoro session and outputs the remaining time.
    """
    start_epoch = time.time()
    current_time = time.gmtime(start_epoch)
    current_time_formatted = time.strftime('%H:%M:%S',  current_time)
    print(f"{bold}{green}Your start time is: {current_time_formatted}{endc}")
    end_epoch = start_epoch + 60*25 # 25 minutes later
    end_time = time.gmtime(end_epoch)
    end_time_formatted = time.strftime('%H:%M:%S', end_time)
    print(f"{bold}{red}Your end time is: {end_time_formatted}{endc}")
    print()

    # Print time remaining
    while time.time() < start_epoch + 60*25:
        delta = end_epoch - time.time()
        time.sleep(1)
        print(f"{whitebg}{black} Remaining {time.strftime('%M:%S',time.gmtime(delta))} {endc}", end="\r", flush=True)

    print('\nYour session has ended. Take a deserved 5 minute break!')


print()
i = input(f"{redbg}Press the enter key to begin a Pomodoro session.{endc}")
print()

# First session
if i == '':
    countdown()
    session_counter = 1
    print()
    print(f"{yellow}You have completed {session_counter} pomodoro session. Well done!{endc}")
    print()
    cont = input('Enter e to exit or simply press the enter key to have another session...\n')
    if cont == 'e':
        sys.exit()
    print('------------------------------------------------------------------------------')

# Additional sessions
while True:
    c = input('\nPress the enter key to begin another session.\n')
    countdown()
    session_counter += 1
    print()
    print(f"{yellow}You have completed {session_counter} pomodoro sessions. Well done!{endc}")
    print()
    cont = input('Enter e to exit or simply press enter key to have another session...\n')
    if cont == 'e':
        sys.exit()
    print('------------------------------------------------------------------------------')