#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hayvan Gölgeleri (Animal Shadows)
A simple program that displays ASCII art animal shadows
"""

import sys
import argparse

def kedi_golgesi():
    """Cat shadow"""
    return r"""
    /\_/\  
   ( o.o ) 
    > ^ <
    """

def kopek_golgesi():
    """Dog shadow"""
    return r"""
    / \__
   (    @\___
   /         O
  /   (_____/
 /_____/   U
    """

def kus_golgesi():
    """Bird shadow"""
    return r"""
    \    /
     \  /
      \/
     /  \
    /    \
    """

def balik_golgesi():
    """Fish shadow"""
    return r"""
      ><(((*>
    """

def tavsan_golgesi():
    """Rabbit shadow"""
    return r"""
    (\__/)
    (•ㅅ•)
    / 　 づ
    """

def main():
    """Main function to display all animal shadows"""
    parser = argparse.ArgumentParser(
        description='Hayvan Gölgeleri (Animal Shadows) - ASCII art hayvan gölgeleri gösterir',
        epilog='Örnek: python3 hayvan_golgeleri.py --hayvan kedi'
    )
    parser.add_argument(
        '--hayvan', 
        choices=['kedi', 'kopek', 'kus', 'balik', 'tavsan', 'hepsi'],
        default='hepsi',
        help='Gösterilecek hayvan (kedi, kopek, kus, balik, tavsan, hepsi)'
    )
    parser.add_argument(
        '--test',
        action='store_true',
        help='Program test modu - çalışıyor mu kontrol et'
    )
    
    args = parser.parse_args()
    
    # Test mode
    if args.test:
        print("✓ Program çalışıyor! (Program is working!)")
        print(f"✓ Python version: {sys.version}")
        print(f"✓ Encoding: {sys.stdout.encoding}")
        return 0
    
    animals = {
        'kedi': ("Kedi (Cat)", kedi_golgesi),
        'kopek': ("Köpek (Dog)", kopek_golgesi),
        'kus': ("Kuş (Bird)", kus_golgesi),
        'balik': ("Balık (Fish)", balik_golgesi),
        'tavsan': ("Tavşan (Rabbit)", tavsan_golgesi),
    }
    
    try:
        print("=" * 50)
        print("HAYVAN GÖLGELERİ (Animal Shadows)")
        print("=" * 50)
        
        if args.hayvan == 'hepsi':
            # Show all animals
            for key, (name, func) in animals.items():
                print(f"\n{name}:")
                print(func())
        else:
            # Show specific animal
            name, func = animals[args.hayvan]
            print(f"\n{name}:")
            print(func())
        
        print("\n" + "=" * 50)
        print("Program başarıyla çalıştı! (Program ran successfully!)")
        print("=" * 50)
        return 0
        
    except UnicodeEncodeError as e:
        print(f"HATA: Karakter kodlama sorunu - {e}", file=sys.stderr)
        print("Çözüm: Terminalinizin UTF-8 kodlamasını desteklediğinden emin olun", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"HATA: Beklenmeyen hata - {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
