class WordbookException(Exception):
    """ Base exception class for Wordbook. Should not be raised directly """
    pass


class DictionaryException(WordbookException):...


class TranslateException(WordbookException):...


class ApiException(WordbookException):...

