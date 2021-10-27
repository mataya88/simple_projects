import re


regulars_list = [r"[a-z]",
                 r"[A-Z]",
                 r"[0-9]",
                 r"[^\w]"]

errors_list = ["small letter",
               "capial letter",
               "number",
               "non-alphanumeric character"]
# These two lists will be used below


def checker(regex, error):
    """ Function to check if the input password includes the given regular expression.

    Arguments:
        regex (str): The function will check if this regular expression is in the input password.

        error (str): This is the error message that will be printed if the regex is not in the input password.

    Returns:
        None
        The function will only increase passed_conditions_int by one if the given regex is included in the input password.
    """
    global passed_conditions_int
    if not re.search(regex, in_pw_str):
        print(f"The password must contain at least one {error}.")
    else:
        passed_conditions_int += 1


passed_conditions_int = 0
while passed_conditions_int < 5:
    passed_conditions_int = 0
    in_pw_str = input("Please enter a password:\n")
    if len(in_pw_str) < 8:
        print("The password must be more than 8 characters.")
    else:
        passed_conditions_int += 1
    for reg, err in zip(regulars_list, errors_list):
        checker(reg, err)
    if passed_conditions_int != 5:
        print(f"{5 - passed_conditions_int} conditions were not met.")
    else:
        print("YOUR PASSWORD IS 100% VALID!!!!")
