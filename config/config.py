from configparser import ConfigParser

def buildConfig():
    """
    """

    config = ConfigParser()

    config.add_section('power_bi_app')

    # client_id, client_secret, group_id from registering api with azure/pbi
    config.set('power_bi_app', 'client_id', 'Some-Client-Id-1234')
    config.set('power_bi_app', 'client_secret', 'Some-Client-Secret-1234=')
    config.set('power_bi_app', 'uri', 'https://localhost')
    config.set('power_bi_app', 'redirect_uri', 'https://localhost/redirect')
    config.set('power_bi_app', 'group_id', 'Some-Group-Id-1234')

    with open(file='config/config.ini', mode='w+', encoding='utf-8') as f:
        config.write(f)

if __name__ == '__main__':
    buildConfig()
