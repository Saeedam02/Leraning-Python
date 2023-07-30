#this is a data bass.
authorized_users={
    'ali':'1234',
    'saeed':'2578',
    'sara':'3654'}
def authorized(func):
    def wrapper(username,password):
        if username in authorized_users.keys() :
            if password==authorized_users[username]:
                return func(username,password)
        return 'not authorized '
    return wrapper
@authorized
def get_blogs(username,password):
    return 'this is your blog'
@authorized
def get_comments(username,password):
    return 'this is your comments'
print(get_blogs('ali','1234'))
print(get_comments('ali','1234'))