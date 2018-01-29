Run to setup dependencies (needs Python2.7):

    source ~/test_framework/develop.bash

Setup Profile
-------------

Edit the `setup.cfg` file and include an entry with your `auth_token` and `auth_id`

To run all tests

    py.test --env test-qa

To run a specific test

    py.test --env test-qa /path/to/test_file.py
