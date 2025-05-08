from config.rules import (LIMITS, FIELDS_TO_DROP, VALUE_COMPLETION)
from processing.cleanup import drop_fields
from processing.completion.dynamic_loader import apply_imputation
from processing.validation import validate_dataset
from db_io.mongo_reader import load_charging_sessions
from db_io.mongo_writer import write_data


def run_pipeline(limit=None):
    print("\tDaten laden")
    data = load_charging_sessions("Transactions December 2021",limit=limit)

    print("\tFelder entfernen")
    data = drop_fields(data, FIELDS_TO_DROP)

    # print("\tDaten validieren davor")
    # data = validate_dataset(data, LIMITS)

    # print("\tWerte ergänzen")
    # data = apply_imputation(data, VALUE_COMPLETION)

    # print("\tDaten validieren danach")
    # data = validate_dataset(data, LIMITS)

    # print("\tDaten schreiben")
    # write_data(data)

    return data
