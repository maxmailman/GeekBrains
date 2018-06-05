class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        log_string = func.__name__ + " была исполнена"
        print(log_string)
        # Открываем логфайл и записваем данные
        with open(self.logfile, 'a') as opened_file:
            # Мы записываем логи в конкретный файл
            opened_file.write(log_string + '\n')
        # Отправляем сообщение
        self.notify()

    def notify(self):
        # Только записываем логи
        pass


@logit()
def myfunc():
    pass


class email_logit(logit):
    """
    Реализация logit для отправки писем администраторам при вызове
    функции
    """

    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # Отправляем письмо в self.email
        # Реализация не будет здесь приведена
        pass
