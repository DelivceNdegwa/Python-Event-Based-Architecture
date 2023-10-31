import datetime

def send_email(**kwargs):
    """
    Email logic comes here
    """
    username = kwargs.get("username")
    email = kwargs.get("email")
    if not username or not email:
        raise ValueError("Please provide a username and email")
    print(f"EMAIL: Hello {username}({email}), welcome to our platform")


def notify_slack_users(**kwargs):
    username = kwargs.get("username")
    if not username:
        raise ValueError("Please provide a username")
    print(f"SLACK: New user {username}, say hi to them")


def notify_admin(**kwargs):
    username = kwargs.get("username")
    time = kwargs.get("time")
    if not username:
        raise ValueError("Please add a username")
    print(time)
    print(f"ADMIN: User {username}, has just joined")


def create_log(**kwargs):
    username = kwargs.get("username")
    if not username:
        raise ValueError("Please add a username")
    print(f"NEW_USER: User {username}, joined at {datetime.datetime.now()}")
