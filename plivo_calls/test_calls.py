
from core import TestContext
import pytest
from lib.calls import PlivoCalls
from lib.utils import check_call_uuid
from assertion import assert_valid_schema


DEFAULT_COUNTRY_ISO = "US"


def create_oubound_data(from_number=None , to_number=None , answer_url=None, answer_method=None):
    """ Invokes the Plivo REST API.

    @from: The phone number to be used as the caller id
    @to: The regular number(s) or sip endpoint(s) to call.
    @answer_url: The URL invoked by Plivo when the outbound call is answered.
    @answer_method: The method used to call the answer_url. Defaults to POST.
    """
    data={"from": from_number, "to": to_number, "answer_url": answer_url, "answer_method": answer_method}
    return data


class TestPlivoCalls(TestContext):

    @pytest.mark.timeout(timeout=30 * 60, method='signal')
    def test_plivo_1(self, logger):
        phone_numbers = PlivoCalls.get_numbers_based_on_iso_code(DEFAULT_COUNTRY_ISO)
        PlivoCalls.buy_number(phone_numbers[0])
        PlivoCalls.buy_number(phone_numbers[1])
        data = create_oubound_data(phone_numbers[0],phone_numbers[1],"https://s3.amazonaws.com/static.plivo.com/answer.xml", "GET")
        call_uuid = PlivoCalls.make_oubound_call(data)
        calls_uuid = PlivoCalls.get_live_calls()
        check_call_uuid(logger, calls_uuid, call_uuid)
        res = PlivoCalls.get_details_of_a_live_call(call_uuid)
        assert_valid_schema(res, 'live_call.json')
        assert res['call_uuid'] == calls_uuid
        assert res['from'] == phone_numbers[0]
        assert res['to'] == phone_numbers[1]

