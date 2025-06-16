This is an automation challenge for designing a test case around "book a flight" feature on delta.com.

Prerequisite installs for running the test scripts:
 1. python
 2. pytest
 3. pytest-playwright
 4. playwright install (browser installation)
 5. pyyaml

Recommended IDE - VSCode

How to execute:
 1. Clone the repo
 2. Set up a venv (https://docs.python.org/3/library/venv.html)
 3. Install prerequisites
 4. Run the pytest test_booking.py

Additional info: 
pytest.ini file contains presets for the pytest run that can be changed. It's currently set to run in verbose, on chromium browser and to display the run on the screen in a slow motion.
All of that is set for ease of use for the manual runner to see what's happening on the screen and can be disabled at any point for a much faster test run.
