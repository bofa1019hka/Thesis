VALIDATION_RULES = {
    "companyID": {"required": True, "alphanumeric": True, "length": 24},
    "siteID": {"required": True, "alphanumeric": True, "length": 24},
    "siteAreaID": {"required": True, "alphanumeric": True, "length": 24},
    "connectorId": {"required": True, "numeric": True, "min": 1, "max": 3},
    "tagID": {"required": True, "alphanumeric": True, "length": 8},
    "carID": {"required": True, "alphanumeric": True, "length": 24},
    "carCatalogID": {"required": True, "numeric": True, "length": 4},
    "userID": {"required": True, "alphanumeric": True, "length": 24},
    "chargeBoxID": {"required": True, "numeric": True, "min": 1, "max": 26},
    "meterStart": {"required": True, "numeric": True, "min": 1},
    "timestamp": {"required": True},
    "stateOfCharge": {"required": True, "numeric": True, "min": 0, "max": 100},
    "phasesUsed.csPhase1": {"required": True, "bool": True},
    "phasesUsed.csPhase2": {"required": True, "bool": True},
    "phasesUsed.csPhase3": {"required": True, "bool": True},
    "stop.userID": {"required": True, "alphanumeric": True, "length": 24},
    "stop.timestamp": {"required": True},
    "stop.tagID": {"required": True, "alphanumeric": True, "length": 8},
    "stop.meterStop": {"required": True, "numeric": True, "min": 1},
    "stop.stateOfCharge": {"required": True, "numeric": True, "min": 0, "max": 100},
    "stop.totalConsumptionWh": {"required": True, "numeric": True, "min": 1, "max": 120000},
    "stop.totalInactivitySecs": {"required": True, "numeric": True, "max": 604800}, #Unterscheidung Langzeitparker?
    "stop.totalDurationSecs": {"required": True, "alphanumeric": True, "min": 1, "max": 604800}
}

FIELDS_TO_DROP = {
    "issuer",
    "price",
    "roundedPrice",
    "priceUnit",
    "pricingSource",
    "timezone",
    "signedData",
    "migrationTag",
    "stop.transactionData",
    "stop.signedData",
    "stop.extraInactivitySecs",
    "stop.extraInactivityComputed",
    "stop.inactivityStatus",
    "stop.price",
    "stop.roundedPrice",
    "stop.priceUnit",
    "stop.pricingSource",
    "remotestop",
    "billingData"
}

VALUE_COMPLETION = {
    "meterStart": "processing.completion.meterStart",
    "carID": "processing.completion.carID",
    "carCatalogID": "processing.completion.carCatalogID",
    "stateOfCharge": "processing.completion.stateOfCharge",
    "phasesUsed": "processing.completion.phasesUsed",
    "stop.reason": "processing.completion.stop.reason"
}