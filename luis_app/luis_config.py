import os

class DefaultConfig:
    """ LUIS Configuration """

    # AUTHORING_KEY = os.environ.get('authoringKey', 'ADD_YOUR_AUTHORING_KEY_HERE')
    AUTHORING_KEY = os.environ.get('authoringKey', '0fa672cf0afb4c13831dafac089ac1bb')
    
    # AUTHORING_ENDPOINT = os.environ.get('authoringEndpoint', 'ADD_YOUR_AUTHORING_ENDPOINT_HERE')
    AUTHORING_ENDPOINT = os.environ.get('authoringEndpoint', 'https://flymeluis-authoring.cognitiveservices.azure.com/')
    
    # PREDICTION_KEY = os.environ.get('PredictionKey', 'ADD_YOUR_PREDICTION_KEY_HERE')
    PREDICTION_KEY = os.environ.get('PredictionKey', '395e4906bb76499ab4fc7ad268f92df2')

    # PREDICTION_ENDPOINT = os.environ.get('predictionEndpoint', 'ADD_YOUR_PREDICTION_ENDPOINT_HERE')
    PREDICTION_ENDPOINT = os.environ.get('predictionEndpoint', 'https://westeurope.api.cognitive.microsoft.com/')

    # After the creation of the APP
    LUIS_APP_ID = os.environ.get("LuisAppId", "d0fa5cf1-f6b8-406d-a309-71361e2e3a4d")
    LUIS_SLOT_NAME = 'Production'