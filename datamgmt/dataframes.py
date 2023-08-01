# Import Pandas dependencies
from pandas import DataFrame
# Import Json dependency
import json
# Import uuid dependency
import uuid

# Import local dependencies
from datamgmt import cache
from datamgmt.filemgmt import deleteFile, fileExists

def jsonifyDf(df : DataFrame, file : str = None) -> str:
    """Jsonifies DataFrame, including encoding data with utf-8. This is done
    by caching data in order to encode with utf-8 as dataframes cannot do this.

    Parameters:
    -----------
    df : DataFrame
        DataFrame to be jsonified

    Returns:
    --------
    str
        json string encoded to utf-8
    """

    data = df.to_json(orient='records', force_ascii=False)
    
    # Generate cached file name
    if file is None:
        fileName = str(uuid.uuid4()) + '.json'
        while fileExists('/'.join([cache, fileName])):
            fileName = str(uuid.uuid4()) + '.json'
        fileName = '/'.join([cache, fileName])
    else:
        fileName = '/'.join([cache, 'catalog', file + '.json'])
    
    # Encodes json string in utf-8 by caching it
    with open(fileName, 'wt', encoding='utf-8') as f:
        json.dump(data, f)
    with open(fileName, 'rt', encoding='utf-8') as f:
        data = json.load(f)

    # Delete cached data and return utf-8 encoded json string
    if file is None:
        deleteFile(fileName)
    return data
