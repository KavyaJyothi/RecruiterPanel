import unittest
from Tests.edit_job_test import EditJob_Test
from Tests.plan_purchase_test import PlanPurchase_Test
from Tests.post_job_test import Post_Job_Test


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(EditJob_Test)
tc2 = unittest.TestLoader().loadTestsFromTestCase(PlanPurchase_Test)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Post_Job_Test)
# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)