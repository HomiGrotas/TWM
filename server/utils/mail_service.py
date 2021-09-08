from os import environ
from smtplib import SMTP_SSL
from queue import Queue
from ssl import create_default_context
from threading import Thread
import random
import string


class MailWorkers:
    port = 465  # For SMTP SSL
    smtp_server = "smtp.gmail.com"
    sender_email = environ['MAIL_ADDRESS']
    password = environ['MAIL_PASSWORD']

    def __init__(self, workers_amount=1):
        context = create_default_context()
        self.__mails_queue = Queue()
        self.__server = SMTP_SSL(MailWorkers.smtp_server, MailWorkers.port, context=context)
        self.__server.login(MailWorkers.sender_email, MailWorkers.password)
        self.__run = True

        # create workers
        for worker in range(workers_amount):
            Thread(target=self.__send_mail).start()

    def add_mail(self, receiver_email: str, subject: str, message: str) -> None:
        """
        add mail function
        this method puts new email in the emails queue
        :param receiver_email: to who the email should be sent
        :param subject: email subject
        :param message: email body
        :return: None
        """
        self.__mails_queue.put((MailWorkers.sender_email, receiver_email, "Subject:" + subject + "\n" + message))

    def __send_mail(self) -> None:
        """
        send mail method
        sends mail to the clients
        :return: None
        """
        while self.__run:
            self.__server.sendmail(*self.__mails_queue.get())       # send mail arguments that got from the queue
            print("SENT MAIL")
        print("FINISHED MAIL SERVICE")

    def stop_service(self):
        """
        stops the mail service (stops all the workers)
        :return: None
        """
        self.__run = False


def send_welcome_email(email: str, first_name: str):
    """
    sends welcome message to new users
    :return: None
    """
    mail_worker.add_mail(email, f"Hi {first_name}, Welcome to TWM",
                         f"Hi {first_name}, Welcome to TWM! \nWe appreciate you!")


def send_reset_password_email(email: str, code: str) -> None:
    mail_worker.add_mail(email, "RESET PASSWORD FOR TWM", f"Hello,\n"
                                                          f"We received a request to reset your password.\n"
                                                          f"Use the following code in order to reset your password:\n"
                                                          f"{code}\nGood luck!")


mail_worker = MailWorkers()  # default with one worker
