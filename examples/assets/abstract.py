class LoginException(Exception):
    """An exception to be thrown when a login fails."""

    def __init__(self, message: str) -> None:
        super().__init__()

        self.message = message

    def __str__(self) -> str:
        return self.message

class MessageException(Exception):
    """An exception to be thrown when leaving a message fails."""

    def __init__(self, message: str) -> None:
        super().__init__()

        self.message = message

    def __str__(self) -> str:
        return self.message

class System:
    """
    A representation of a system that users can leave a message

    Raises:
        LoginException: When another is user is using the system.
        MessageException: When the message has no contents.
    """

    # Give attributes better names
    current_user = ""

    def _login(self, new_user):
        if not self.current_user:
            self.current_user = new_user
        elif self.current_user != new_user:
            raise LoginException("A different user is using this system.")

    def _logout(self):
        if self.current_user:
            self.current_user = ""

    def leave_message(self, content, username):
        if not content:
            raise MessageException("Message has no contents")

        self._login(username)

        print(f"{self.current_user} - {content}")

        self._logout()
