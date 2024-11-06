calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(sting):
    count_calls()
    return len(sting), sting.upper(), sting.lower()

def is_contains(sting, list_to_search):
    count_calls()
    for i in list_to_search:
        if sting.lower() == i.lower():
            return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)