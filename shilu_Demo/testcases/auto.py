# -- coding: utf-8 --
# shilutest

import unittest


class Ces(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("最先执行")
    @classmethod
    def tearDownClass(cls) -> None:
        print("最后执行")
    def test_hh(self):
        print('执行测试用例1')
    def test_xx(self):
        print("执行测试用例2")
    def test_yy(self):
        print("执行测试用例3")
    def test_equal(self):
        print('断言：相等')
        self.assertEqual(1,2,"判断1和1")
    def test_notEqual(self):
        print("断言不相等")
        self.assertNotEqual(1,2,"判断1和1")

class Ces2(unittest.TestCase):
    def test_zz(self):
        print("执行第二类第一条")

if __name__ == '__main__':
    #方法一：运行测试用例,运行当前文件内所有unittest测试用例
    unittest.main
    #方法二：创建测试套件,添加测试用例 testsuite，执行指定测试用例
    # suite = unittest.TestSuite()
    # suite.addTest(Ces("test_hh"))
    # unittest.TextTestRunner().run(suite)
    #方法三：执行某个测试类
    # suite1 = unittest.TestLoader.loadTestsFromTestCase(Ces)
    # suite = unittest.TestSuite([suite1])
    # unittest.TextTestRunner(verbosity=2).run(suite)

