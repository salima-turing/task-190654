import time
from tenacity import retry, stop_after_attempt, wait_fixed
import unittest

# Function being tested that relies on an older system
def fetch_data_from_old_system():
	# Simulate a flaky behavior with a random chance of failure
	import random
	if random.randint(1, 5) == 1:
		raise Exception("System Error")
	return "Data from old system"

class TestFetchData(unittest.TestCase):

	@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
	def test_fetch_data_stabilized(self):
		data = fetch_data_from_old_system()
		self.assertEqual(data, "Data from old system")

if __name__ == '__main__':
	unittest.main()
