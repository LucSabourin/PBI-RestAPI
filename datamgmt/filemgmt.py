from datamgmt import os

def deleteFile(path : str) -> None:
    """Used to delete a file at the given path.

    Parameters:
    -----------
    path : str
        path of file to be deleted
    """

    try:
        if os.path.isfile(path):
            os.remove(path)
    except Exception as e:
        print(f'Failed to delete {path}. Reason: {e}')

def fileExists(path : str) -> bool:
    """
    """
    
    return os.path.isfile(path)
