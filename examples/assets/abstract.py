class A:
    """
    Something, something talking stick?

    Document Me!

    Give the class, its attributes, methods and arguments better names.

    Please note, _x() are denoted because they are internal methods and would not
    expected to be called outside of the class.

    Raises:
        Exception: Document Me
    """

    # Give attributes better names
    x = ""

    def _b(self, c):
        if not self.x:
            self.x = c
        elif self.x != c:
            raise Exception("A different user is using this system.")

    def _c(self):
        if self.x:
            self.x = ""

    def d(self, e, f):
        if not e:
            raise Exception("Message has no contents")

        self._b(f)

        print(f"{self.x} - {e}")

        self._c()
