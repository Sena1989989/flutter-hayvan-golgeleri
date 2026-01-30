#!/usr/bin/env python3
"""
Hayvan Gölgeleri (Animal Shadows)
A simple program that displays ASCII art animal shadows
"""

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
    print("=" * 50)
    print("HAYVAN GÖLGELERİ (Animal Shadows)")
    print("=" * 50)
    
    animals = [
        ("Kedi (Cat)", kedi_golgesi),
        ("Köpek (Dog)", kopek_golgesi),
        ("Kuş (Bird)", kus_golgesi),
        ("Balık (Fish)", balik_golgesi),
        ("Tavşan (Rabbit)", tavsan_golgesi),
    ]
    
    for name, func in animals:
        print(f"\n{name}:")
        print(func())
    
    print("\n" + "=" * 50)
    print("Program başarıyla çalıştı! (Program ran successfully!)")
    print("=" * 50)

if __name__ == "__main__":
    main()
