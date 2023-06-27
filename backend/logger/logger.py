import logging

class CustomFormatter(logging.Formatter):
    # code adapted from
    # https://stackoverflow.com/a/72168517

    # format explanation help: https://tforgione.fr/posts/ansi-escape-codes/
    # format: x1b[ followed by ;-separated styles
    # example: x1b[<bold,italics,etc>;<foreground-colour>;<background-colour>m
    # magenta example: x1b[3(italics);30(black foreground);45(magenta background)m

    grey = "\x1b[3;30;38m"
    green = "\x1b[0;30;42m"
    magenta = "\x1b[3;30;45m"
    red = "\x1b[0:30;41m"
    bold_red = "\x1b[1;30;1m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: f"%(asctime)s::{grey}%(levelname)s{reset}: %(message)s",
        logging.INFO: f"%(asctime)s::{green}%(levelname)s{reset}: %(message)s",
        logging.WARNING: f"%(asctime)s::{magenta}%(levelname)s{reset}: %(message)s",
        logging.ERROR: f"%(asctime)s::{red}%(levelname)s{reset}: %(message)s",
        logging.CRITICAL: f"%(asctime)s::{bold_red}%(levelname)s{reset}: %(message)s"
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger("core")
# TODO update to INFO before prod push
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
# TODO update to INFO before prod push
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)