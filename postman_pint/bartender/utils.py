from bartender.models import Bartender, Institution


def pour_pint(pint, institution, customer, bartender):
    """
    POUR A PINT

    This function is intended to activate a gifted pint.

    It will update the status of that pint to settings.PINT_STATUS_POURED and will populate the field: Pint.Institution
    """


def get_poured_pints(bartender):
    """
    This function will return all of the pints that the bartender has activated as well as their statuses
    """


def get_bartenders():
    bartenders = Bartender.objects.all()
    return bartenders


def get_institutions():
    institutions = Institution.objects.all()
    return institutions
