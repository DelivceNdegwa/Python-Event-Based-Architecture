import datetime


def send_email(username: str):
    """
    Email logic comes here
    """
    print(f"EMAIL: Hello {username}, welcome to our platform")


def notify_slack_users(username: str):
    print(f"SLACK: New user {username}, say hi to them")


def notify_admin(username: str):
    print(f"ADMIN: User {username}, has just joined")


def create_log(username: str):
    print(f"NEW_USER: User {username}, joined at {datetime.datetime.now()}")
