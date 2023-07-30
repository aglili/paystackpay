class PayStackPayErr(Exception):
    """
    There is an Error
    """

    pass


class MissingAPIKeyErr(PayStackPayErr):
    """
    API_KEY Cannot be Found
    
    """

    pass


class WrongMethodErr(PayStackPayErr):
    """
    Wrong HTTP Method/Request
    """

    pass


class InvalidDataErr(PayStackPayErr):
    """
    Invalid or Wrong Input Received
    """

    pass


