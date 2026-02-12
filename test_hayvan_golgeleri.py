#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for hayvan_golgeleri.py
"""

import sys
import subprocess

def test_program():
    """Test the hayvan_golgeleri program"""
    tests_passed = 0
    tests_failed = 0
    
    print("=" * 60)
    print("HAYVAN GÖLGELERİ TEST SUITE")
    print("=" * 60)
    
    # Test 1: Test mode
    print("\n[Test 1] Program test modu...")
    try:
        result = subprocess.run(
            [sys.executable, "hayvan_golgeleri.py", "--test"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0 and "Program çalışıyor" in result.stdout:
            print("✓ Test modu başarılı")
            tests_passed += 1
        else:
            print("✗ Test modu başarısız")
            print(f"  Çıktı: {result.stdout}")
            print(f"  Hata: {result.stderr}")
            tests_failed += 1
    except Exception as e:
        print(f"✗ Test modu hatası: {e}")
        tests_failed += 1
    
    # Test 2: Default run (all animals)
    print("\n[Test 2] Tüm hayvanları göster...")
    try:
        result = subprocess.run(
            [sys.executable, "hayvan_golgeleri.py"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if (result.returncode == 0 and 
            "Kedi" in result.stdout and 
            "Köpek" in result.stdout and
            "başarıyla çalıştı" in result.stdout):
            print("✓ Tüm hayvanlar gösterildi")
            tests_passed += 1
        else:
            print("✗ Tüm hayvanlar gösterilemedi")
            tests_failed += 1
    except Exception as e:
        print(f"✗ Hata: {e}")
        tests_failed += 1
    
    # Test 3: Single animal (kedi)
    print("\n[Test 3] Tek hayvan göster (kedi)...")
    try:
        result = subprocess.run(
            [sys.executable, "hayvan_golgeleri.py", "--hayvan", "kedi"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if (result.returncode == 0 and 
            "Kedi" in result.stdout and
            "Köpek" not in result.stdout):
            print("✓ Tek hayvan başarılı")
            tests_passed += 1
        else:
            print("✗ Tek hayvan başarısız")
            tests_failed += 1
    except Exception as e:
        print(f"✗ Hata: {e}")
        tests_failed += 1
    
    # Test 4: Help
    print("\n[Test 4] Yardım menüsü...")
    try:
        result = subprocess.run(
            [sys.executable, "hayvan_golgeleri.py", "--help"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0 and "usage:" in result.stdout:
            print("✓ Yardım menüsü başarılı")
            tests_passed += 1
        else:
            print("✗ Yardım menüsü başarısız")
            tests_failed += 1
    except Exception as e:
        print(f"✗ Hata: {e}")
        tests_failed += 1
    
    # Test 5: All animals individually
    print("\n[Test 5] Tüm hayvanları tek tek test et...")
    animals = ['kedi', 'kopek', 'kus', 'balik', 'tavsan']
    all_ok = True
    for animal in animals:
        try:
            result = subprocess.run(
                [sys.executable, "hayvan_golgeleri.py", "--hayvan", animal],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode != 0:
                print(f"  ✗ {animal} başarısız")
                all_ok = False
        except Exception as e:
            print(f"  ✗ {animal} hatası: {e}")
            all_ok = False
    
    if all_ok:
        print("✓ Tüm hayvanlar tek tek başarılı")
        tests_passed += 1
    else:
        print("✗ Bazı hayvanlar başarısız")
        tests_failed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"TEST SONUÇLARI: {tests_passed} başarılı, {tests_failed} başarısız")
    print("=" * 60)
    
    if tests_failed == 0:
        print("\n✓✓✓ TÜM TESTLER BAŞARILI! Program çalışıyor! ✓✓✓\n")
        return 0
    else:
        print(f"\n✗✗✗ {tests_failed} TEST BAŞARISIZ! ✗✗✗\n")
        return 1

if __name__ == "__main__":
    sys.exit(test_program())
