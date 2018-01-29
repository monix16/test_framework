
from plivo import *
from connection import *
from ConfigParser import SafeConfigParser


def iniread(env=None):
    configuration = {}
    cfg = SafeConfigParser()
    cfg.read('setup.cfg')

    if env:
        overrides = dict(cfg._sections[env])
        configuration.update(overrides)
    return configuration

def log(logger_name):
    LOG = logging.getLogger(logger_name)
    if not len(LOG.handlers):
        LOG.setLevel(logging.DEBUG)
        stream = logging.StreamHandler(sys.stdout)
        stream.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s [%(levelname)s] (%(threadName)s) %(message)s')
        stream.setFormatter(formatter)
        LOG.addHandler(stream)
    return LOG

def invoke_plivo_api(url=None, entity=None, type='get', data=None, auth_token=None, auth_id=None, params=None):
    """ Invokes the Plivo REST API.

    @url: baseurl of the plivo endpoint. uses connection default if none specified
    @entity: rest entity path with version
    @type: request type GET,POST,PUT,DELETE
    @data: payload data for PUT and POST
    @auth_token: API token of Plivo user. uses connection default if not specified
    @params: GET parameters
    """
    DEFAULT_BASEURL = Plivo.baseurl
    DEFAULT_AUTHTOKEN = Plivo.auth_token
    DEFAULT_VERSION = Plivo.version
    DEFAULT_AUTHID = Plivo.auth_id
    if data and not isinstance(data, dict):  # non-null data should be sent as dict, not json string
        raise AttributeError("expected %s arg to be dict got %s instead" % (data, data.__class__))
    url = url if url else DEFAULT_BASEURL
    auth_id = auth_id if auth_id else DEFAULT_AUTHID
    url = url + DEFAULT_VERSION + "/Account/" + auth_id + "/"
    agent = Connection(auth_id, DEFAULT_AUTHTOKEN, url, False)
    if type.lower() == 'get':
        return agent._api_call_raw(req_type='GET', path=entity, params=params)
    elif type.lower() == 'post':
        return agent._api_call_raw(req_type='POST', path=entity, data=data)
    elif type.lower() == 'put':
        return agent._api_call_raw(req_type='PUT', path=entity, data=data)
    else: #type == 'delete'
        return agent._api_call_raw(req_type='DELETE', path=entity, params=params, data=data)


def check_call_uuid(logger, calls_uuid, expected_call_uuid):
    """ basic asserts for call uuid
    """
    flag = 0
    print expected_call_uuid
    for id in calls_uuid:
        print id
        if expected_call_uuid == id:
            flag = 1
    assert flag == 0, \
            "call uuid not found"
