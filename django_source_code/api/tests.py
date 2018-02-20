from django.test import TestCase
import pytest

# Create your tests here.
from .versions import v1


# ------------------------------------------------------------------------------
# DiggerView?
# ------------------------------------------------------------------------------

# start_depth, amount_to_dig, dubloon_discovery_interval, expected_output
calculate_dubloon_accrual_parameters = [
    (0, -5, 5, 0),
    (0, -4, 5, 0),
    (0, -3, 5, 0),
    (0, -2, 5, 0),
    (0, -1, 5, 0),
    (0, 0, 5, 0),
    (0, 1, 5, 0),
    (0, 2, 5, 0),
    (0, 3, 5, 0),
    (0, 4, 5, 0),
    (0, 5, 5, 1),
    (0, 6, 5, 1),
    (0, 7, 5, 1),
    (0, 8, 5, 1),
    (0, 9, 5, 1),
    (0, 10, 5, 2),
    (0, 100, 5, 20),
    (0, 1000, 5, 200),
    (0, 10000, 5, 2000),
    # Random testing
    (0, 1, 5, 0),
    (1, 1, 5, 0),
    (2, 1, 5, 0),
    (3, 1, 5, 0),
    (4, 1, 5, 1),
    (5, 1, 5, 0),
    (6, 1, 5, 0),
    (7, 1, 5, 0),
    (8, 1, 5, 0),
    (9, 1, 5, 1),
    (10, 1, 5, 0),
    (59, 1, 5, 1),
]


@pytest.mark.parametrize("start_depth,amount_to_dig,dubloon_discovery_interval,expected_output",
                         calculate_dubloon_accrual_parameters)
def test_calculate_dubloon_accrual(start_depth,
                                   amount_to_dig,
                                   dubloon_discovery_interval,
                                   expected_output):
    actual_output = v1.calculate_dubloon_accrual(start_depth, amount_to_dig, dubloon_discovery_interval)
    print(("\nactual_output: {}"
           "\nexpected_output: {}"
           ).format(actual_output, expected_output))
    if(actual_output == expected_output):
        pass  # Do nothing - hooray!
    else:
        error_output = ("The `calculate_dubloon_accrual` was called with the"
                        " arguments"
                        " start_depth: {}"
                        " amount_to_dig: {}"
                        " dubloon_discovery_interval: {} and expected the"
                        " output `{}`, but received the output `{}`"
                        ).format(start_depth,
                                 amount_to_dig,
                                 dubloon_discovery_interval,
                                 actual_output)
        pytest.fail(error_output)
