class LoginMetaClass(type):
    def __getattribute__(cls, name):
        attr = super().__getattribute__(name)
        if callable(attr) and name != 'login':  # Exclude the login method itself

            def login_enforcer(*args, **kwargs):
                if not cls.logged_in:
                    raise PermissionError("You must be logged in to access this method.")
                return attr(*args, **kwargs)

            return login_enforcer
        return attr

