# City Dispatch Simulation
# Primary Author: Shyamal Chandra
# July 27, 2024

import os
import sys
import string
import random

class Player:

    name = ''
    order = -1

    def __init__ (self, name, order):
        self.name = name
        self.order = order

class CityCall:

    location = ''
    calltype = ''
    callid = -1
    solutions = {}

    def __init__ (self, location, calltype, callid, solutions):
        self.location = location
        self.calltype = calltype
        self.callid = callid
        self.solutions = solutions

# To String function
    def __str__ (self):
        return str("CityCall: " + self.location + " " + self.calltype + " " + str(self.callid) + " ")

class city_dispatch_simulator:

    CallQueue = []
    starting_time = -1

    def __init__(self, CallQueue, starting_time):
        self.CallQueue = CallQueue
        self.starting_time = starting_time
        return

    def print_queues(self):
        print("Queue items:")
        for items in self.CallQueue:
            print(items)
        return True

    def is_valid_solutions(self, position):

        if position > 0 and position < 5:
            return True
        else:
            return False

    def make_move(self, move, order, solutions):
        print("Player " + str(order) + " moved solution " + str(move) + ".")
        if solutions[str(move)] != "solved":
            return False
        else:
            return True

    def check_if_win(self):
        if len(self.CallQueue):
            print("Game Over!")
            return True
        else:
            return False

    def check_if_time_done(self):
        if self.starting_time == 0:
            print("Time is up!")
            return True
        else:
            return False

    def get_next_item(self):
        return self.CallQueue.pop()

# To String function
    def __str__ (self):
        return str("" + self.CallQueue + " " + str(self.time) + "")

def caller_generate_random(typeOfEmergency, callerid):

    location = ["Frontenac", "Pittsburg", "Arma", "Columbus", "Arcadia"]

    fire_candidates = ["Home burning", "Car burning", "Shop burning", "People burning"]
    ER_candidates = ["Old timer sick", "Mortally wounded", "Asthma attack", "First-degree burn"]
    police_candidates = ["1st-degree murder","robbery","vandalism","arson"]

    unshuffled_number = ['1', '2', '3', '4']
    unshuffled_result = ['solved', 'unsolved', 'incomplete', 'add back']

    random.shuffle(unshuffled_number)
    random.shuffle(unshuffled_result)

    choices = {}

    for item in range(len(unshuffled_number)):
        print(item)
        choices[str(unshuffled_number[int(item)])] = str(unshuffled_result[int(item)])

    solutions = []

    match typeOfEmergency:
        case "fire":
            return CityCall(random.choice(location), random.choice(fire_candidates), callerid, choices)
        case "ER":
            return CityCall(random.choice(location), random.choice(ER_candidates), callerid, choices)
        case "police":
            return CityCall(random.choice(location), random.choice(police_candidates), callerid, choices)

if __name__ == "__main__":

    upper_bound = 10

    lower_bound = 100
    highest_bound = 200

    police_num = random.randint(1, upper_bound)
    medical_num = random.randint(1, upper_bound)
    fire_num = random.randint(1, upper_bound)

    dispatch_queue = []

    for police_call in range(police_num):
        dispatch_queue.append(caller_generate_random("police", random.randint(lower_bound, highest_bound)))
    for medical_call in range(medical_num):
        dispatch_queue.append(caller_generate_random("ER", random.randint(lower_bound, highest_bound)))
    for fire_num in range(fire_num):
        dispatch_queue.append(caller_generate_random("police", random.randint(lower_bound, highest_bound)))

    random.shuffle(dispatch_queue)

    time_limit = random.randint(lower_bound, highest_bound)
    penalty = 10
    win = 10

    print(dispatch_queue)
    print(len(dispatch_queue))

    testcall = city_dispatch_simulator(dispatch_queue, time_limit)
    end_of_game = False
    quit = False
    all_players = []
    all_players.append(Player('Human', 1))
    all_players.append(Player('CPU', 2))

    while not quit:

        while not end_of_game:

            for play in all_players:

                print(testcall.CallQueue)
                newCall = testcall.get_next_item()

                print(newCall)

                next_move = input("Which solution (1, 2, 3, 4)? ")

                if not testcall.is_valid_solutions(int(next_move)):
                    print("Invalid input for solution")
                    exit(0)

                if not testcall.make_move(int(next_move), play.order, newCall.solutions):
                    print("Bad move")
                    time_limit = time_limit - penalty
                else:
                    print("Good move")
                    time_limit = time_limit + win

                testcall.print_queues()

                end_of_game = testcall.check_if_win()
                end_of_game = testcall.check_if_time_done()

                if end_of_game:
                    print('End of game!')

        keep_on_playing = input('Keep on playing ([y], n): ')
        if keep_on_playing == 'y':
            quit = False
        else:
            quit = True

main()
