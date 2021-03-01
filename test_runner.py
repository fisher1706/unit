import unittest
import utest_calc

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(utest_calc.CalcBasicTests))
calcTestSuite.addTest(unittest.makeSuite(utest_calc.CalcExTests))

print('count of tests: ' + str(calcTestSuite.countTestCases()) + '\n')

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)


# testCases = []
# testCases.append(utest_calc.CalcBasicTests)
# testCases.append(utest_calc.CalcExTests)
#
# testLoad = unittest.TestLoader()
#
# suites = []
#
# for tc in testCases:
#     suites.append(testLoad.loadTestsFromTestCase(tc))
#
# res_suite = unittest.TestSuite(suites)
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(res_suite)


# testLoad = unittest.TestLoader()
# suites = testLoad.loadTestsFromModule(utest_calc)
#
# testResult = unittest
#
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suites)


# testLoad = unittest.TestLoader()
# suites = testLoad.loadTestsFromModule(utest_calc)
#
# testResult = unittest.TestResult()
#
# runner = unittest.TextTestRunner(verbosity=1)
# testResult = runner.run(suites)
# print('errors')
# print(len(testResult.errors))
# print("failures")
# print(len(testResult.failures))
# print("skipped")
# print(len(testResult.skipped))
# print("testsRun")
# print(testResult.testsRun)