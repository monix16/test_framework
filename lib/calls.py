from utils import *


class PlivoCalls(object):

    @classmethod
    def get_numbers_based_on_iso_code(self, country):
        """
        Get phone numbers based on country iso code
        """
        logger = log("search_numbers_based_on_iso_code")
        self.entity = '/PhoneNumber/?country_iso='+country
        res = invoke_plivo_api(entity=self.entity, type='get')
        if not res.ok:
            logger.warn("unable to fetch phone number.")
            return None

        res = res.json()
        numbers = []
        for n in res['objects']:
            numbers.append(n['number'])
        return numbers

    @classmethod
    def buy_number(self, number):
        """
        Buy number of  given country
        """
        self.entity = '/PhoneNumber/'+number+'/'
        cmd = invoke_plivo_api(entity=self.entity, type='post')
        assert cmd.ok, \
            "Command execution didn't return 200 OK "

        cmd = cmd.json()
        return cmd

    @classmethod
    def make_oubound_call(self, data):
        cmd = invoke_plivo_api(entity='/Call/', type='post', data=data)
        assert cmd.ok, \
            "Command execution didn't return 200 OK "

        cmd = cmd.json()
        return cmd['request_uuid']

    @classmethod
    def get_live_calls(self):
        """
        Get all live calls
        """
        logger = log("get_live_calls")
        self.entity = '/Call/?status=live'
        res = invoke_plivo_api(entity=self.entity, type='get')
        if not res.ok:
            logger.warn("unable to fetch call details.")
            return None

        res = res.json()
        calls_uuid = res['calls']
        return calls_uuid

    @classmethod
    def get_details_of_a_live_call(self, call_uuid):
        """
            Get details of call based on uuid
        """
        logger = log("get_details_of_call_based_on_uuid")
        self.entity = '/Call/'+call_uuid+'/?status=live'
        res = invoke_plivo_api(entity=self.entity, type='get')
        if not res.ok:
            logger.warn("unable to fetch call details.")
            return None

        res = res.json()
        return res
