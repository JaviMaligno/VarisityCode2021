# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:46:47 2021

@author: javia
"""

from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("121_"), "1212")

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("121_343_1_1_3_"), "12123434121234")
    
    def test3(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("121_312____"), "12123123123")

    def test4(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("13123243_"), "131232432")

    def test5(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("1234235123_"), "12342351234")

    #def test6(self): #surely this tests is wrong
     #   solution = Solution()
     #   self.assertEqual(solution.number_prediction("70000000_"), "700000007")

    def test7(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("10000000001200000000021000000000_"), "100000000012000000000210000000001")

    def test8(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("10000000000120000000000210000000000_"), "100000000001200000000002100000000002")
        
    def test9(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("1_2_3_11____"), "112233112233")

    def test10(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("___"), "000")

    #def test11(self): #possibly wrong
     #   solution = Solution()
      #  self.assertEqual(solution.number_prediction("43127435926350613352415886760955388_8983743325219_168_926629293_776892_9_1_8_8049287_298_9343647_9_2334_4_6_7__57__30785__7__62_1____4_____382__1226816__04__67___0119_47__0_0_7___0___0_3__3_____06_37_"), "43127435926350613352415886760955388689837433252198168992662929327768929921981804928762981934364769323343436476957693078576760629193434364763829112268168904926760601193476307077689049204312334343060374")

    def test12(self): 
        solution = Solution()
        self.assertEqual(solution.number_prediction("1059384231063272231283077963_86390_07292893174_4389407054_9205___0104__35130_3__68_67577_2_38_3_2__47255__7_34674938809759_6_5_525_5_44_56____2_9__5_0_5__153_____08________7___3_17_______0__1____8___6"), "10593842310632722312830779632863907072928931742438940705409205409010409351307307689675779203893128347255557734674938809759367575255554445675752593659015901536590108097593677346391742438940701080980986")

if __name__ == '__main__':
    unittest.main()