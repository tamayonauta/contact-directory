from multiprocessing import Pool

from .validations import CriminalRecordValidator
from .validations import PersonalDataValidator
from .validations import ScoreValidator


def run_score_validator(person):
    """
    Run score validator
    """

    return run_validator(ScoreValidator, person)


def run_parallel_validators(person):
    """
    Run parallel validators:

    1. PersonalDataValidator
    2. CriminalRecordValidator
    """

    # Init validator pool
    validator_pool = Pool(processes=2)
    # Run validator pool
    validation_results = validator_pool.starmap(
        run_validator,
        [
            (Validator, person) for Validator in (
                PersonalDataValidator,
                CriminalRecordValidator
            )
        ]
    )
    # Close validator pool
    validator_pool.close()

    return validation_results


def run_validator(Validator, person):
    """
    Execute validate function of the validator
    """

    return Validator.validate(person)
