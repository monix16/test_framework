
class Plivo:
    """
    Singleton for storing authorization credentials and other
    configuration parameters for Plivo.
    """
    auth_token = None
    baseurl = None
    version = None
    skip_ssl_cert_check = None
    auth_id = None

    @classmethod
    def configure(cls, auth_token, auth_id,
                  api_url="https://api.plivo.com/", version="v1",
                  skip_ssl_cert_check=False):
        """
        Set parameters governing interaction with Plivo

        Args:
            `auth_token`: authorization token for Plivo. required

            `api_url`: the base URL for Plivo API. configurable for testing only

            `version`: Plivo REST api version.
        """
        cls.auth_token = auth_token
        cls.auth_id = auth_id
        cls.version = version
        cls.baseurl = api_url
        cls.skip_ssl_cert_check = skip_ssl_cert_check