
import logging
import pytest
import sys

def pytest_addoption(parser):
    """  Add option --env to specify environment found in setup.cfg
    """
    quickgroup = parser.getgroup("plivo quick options")
    quickgroup.addoption("--auth-token", dest="auth_token", help="Auth Token",
                         default="Mzk0MzU1Mzc3MTc1MTEyMGU2M2RlYTIwN2UyMzk1")
    quickgroup.addoption("--url", dest="api_url", help="api endpoint for the Plivo",
                         default=None)
    quickgroup.addoption("--auth_id", dest="auth_id", help="Authentication ID",
                         default="MAODUZYTQ0Y2FMYJBLOW")
    group = parser.getgroup("plivo extended options")
    group.addoption('--env', dest='environment', help='Specify environment profile section: "test-qa"')


@pytest.fixture(scope="module", autouse=True)
def logger(request):
    """
    This fixture returns a logger with level DEBUG.
    """
    # turn off logging from requests module
    requests_log = logging.getLogger("requests")
    requests_log.setLevel(logging.ERROR)
    # turn off ssh key auth warning from paramiko
    paramiko_log = logging.getLogger("paramiko")
    paramiko_log.setLevel(logging.ERROR)
    try:
        LOG = logging.getLogger(request.function.__name__)
    except AttributeError:
        LOG = logging.getLogger(request.module.__name__)
    if not len(LOG.handlers):
        LOG.setLevel(logging.DEBUG)
        stream = logging.StreamHandler(sys.stdout)
        stream.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s [%(levelname)s] (%(threadName)s) %(message)s')
        stream.setFormatter(formatter)
        LOG.addHandler(stream)
    return LOG