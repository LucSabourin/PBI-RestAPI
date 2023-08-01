from __init__ import configIni, credentials
from datasets import buildPowerBiClient
from datamgmt.filemgmt import fileExists
from config.config import buildConfig

if __name__ == '__main__':
    # Note: You must register the api with Power BI/Azure in order to get:
    #       client_id
    #       client_secret
    #       group_id
    if not fileExists(configIni):
        buildConfig()

    # When the console prompts with a url, ctrl+click to open the url. It will
    # look broken (because it is) - copy and paste the url generated in your
    # browser back into the console.
    if not fileExists(credentials):
        buildPowerBiClient()
