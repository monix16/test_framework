
import pytest
from lib.utils import *
from lib.plivo import *


class TestContext(object):
    """ Base class for all plivo tests. """

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(cls, request, logger):
        """

        The purpose of this fixture is to prepare the TestContext for test classes that
        are implementing it. Environment configuration made available from `self.config`
        dict.

        """
        logger.debug("initializing plivo test context")
        cls.config = iniread(env=request.config.option.environment)
        request.module.config = cls.config
        request.cls.config = cls.config

        # switch between quick and extended options here
        if request.config.option.auth_token and request.config.option.api_url:
            auth_token = request.config.option.auth_token
            api_url = request.config.option.api_url
            auth_id = request.config.option.auth_id
        else:
            auth_token = cls.config.get('auth_token')
            api_url = cls.config.get('api_url')
            auth_id = cls.config.get('auth_id')

        Plivo.configure(
            auth_token=auth_token,
            auth_id=auth_id,
            api_url=api_url,
            skip_ssl_cert_check=False,
            version="v1"
        )

