def sweep_floors(time):
    if 1100 < time < 2100:
        print("Sweeping the floors...")
    else: 
        print("I'm off duty!") 

def wash_dishes(time):
    if 1100 < time < 2100:
        print("Washing dishes...")
    else: 
        print("I'm off duty!")

def chop_vegetables(time):
    if 1100 < time < 2100:
        print("Chopping the vegetables...")
    else: 
        print("I'm off the dutty")


sweep_floors(800)

wash_dishes(1000)

chop_vegetables(1200)

# decorators concept is below 

def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else: 
            print("I'm off duty!") 
    return wrapper


@check_working_hours
def sweep_floors(time):
    print("Sweep the floors...")


@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")


@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")


sweep_floors(1240)
wash_dishes(1000)
chop_vegetables(1200)




