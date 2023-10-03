import urwid


def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_letters(password):
    return any(letter.isalpha() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def is_very_long(password):
    min_length = 12
    return len(password) > min_length


def has_symbols(password):
    return any(
        (not letter.isdigit() and not letter.isalpha()) for letter in password
    )


def check_password(password):
    checks = [
        has_digit(password),
        has_letters(password),
        has_lower_letters(password),
        has_upper_letters(password),
        is_very_long(password),
        has_symbols(password)
    ]
    score = 0
    for check in checks:
        if check:
            score += 2
    return score


if __name__ == "__main__":
    def on_ask_change(edit, score):
        reply.set_text("Рейтинг этого пароля: %s" % check_password(score))
   
    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
