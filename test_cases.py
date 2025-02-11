#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))
                
        # 1. 有効な整数のテスト（通常ケース）
        def test_sample5(self):
                self.assertEqual(21, calc(7, 3))
        
        def test_sample6(self):
                self.assertEqual(300, calc(10, 30))
        
        # 2. 境界値テスト
        def test_sample7(self):
                self.assertEqual(1, calc(1, 1))
        
        def test_sample8(self):
                self.assertEqual(998001, calc(999, 999))
        
        def test_sample9(self):
                self.assertEqual(999, calc(1, 999))
        
        # 3. 無効な整数のテスト（範囲外）
        def test_sample10(self):
                self.assertEqual(-1, calc(0, 10))
        
        def test_sample11(self):
                self.assertEqual(-1, calc(1000, 500))
        
        def test_sample12(self):
                self.assertEqual(-1, calc(-1, 50))
        
        # 4. 浮動小数点のテスト
        def test_sample13(self):
                self.assertEqual(-1, calc(3.5, 2))
        
        def test_sample14(self):
                self.assertEqual(-1, calc(2.0, 3.0))
                
        def test_sample15(self):
                self.assertEqual(-1, calc(999.1, 2))
        
        # 5. 文字列のテスト
        def test_sample16(self):
                self.assertEqual(-1, calc("abc", 10))
        
        def test_sample17(self):
                self.assertEqual(-1, calc("5", "10"))
        
        # 6. 組み合わせテスト
        def test_sample18(self):
                self.assertEqual(-1, calc(100, -1))
        
        def test_sample19(self):
                self.assertEqual(-1, calc(1000, "5"))
                
        # 7. NULL等のテスト
        
        def test_sample19(self):
                self.assertEqual(-1, calc(None, 5))

        def test_sample20(self):
                self.assertEqual(-1, calc([5], {10:20}))
                
        def test_sample21(self):
                self.assertEqual(-1, calc("", 5))
                
        def test_sample22(self):
                self.assertEqual(-1, calc("5.0", "3"))
                
        def test_sample23(self):
                self.assertEqual(-1, calc(True, 10)) 


