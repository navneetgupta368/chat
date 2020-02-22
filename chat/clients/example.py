from chat.protocol import parcel


def user_input(host, port):
    """
    You need to take input from user and
    send it to the server.

    This needs to be an infinite loop.

    Use
    s.sendall(parcel(message,
    myself=myname,
    to=toname))

    to send messages.
    """


def show_message(msg: str, myself: str, sender: str) -> str:
    ...
