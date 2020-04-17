# Generate static integer for ID
def idGenerator():
    # Retrieve ID from database here instead
    if 'id' not in idGenerator.__dict__:
        idGenerator.id = 0
    idGenerator.id += 1
    return idGenerator.id

def userIdGenerator():
    pass

def carIdGenerator():
    pass

def bookingIdGenerator():
    pass

def historyIdGenerator():
    pass