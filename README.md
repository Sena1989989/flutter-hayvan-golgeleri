# hayvan_golgeleri

Hayvan Gölgeleri (Animal Shadows) - Hayvan gölgelerini ASCII sanatı olarak gösteren basit bir Python programı.

## Çalıştırma (Running)

Programı çalıştırmak için:

```bash
python3 hayvan_golgeleri.py
```

veya:

```bash
./hayvan_golgeleri.py
```

### Tek bir hayvan gösterme (Show a single animal):

```bash
python3 hayvan_golgeleri.py --hayvan kedi
python3 hayvan_golgeleri.py --hayvan kopek
python3 hayvan_golgeleri.py --hayvan kus
python3 hayvan_golgeleri.py --hayvan balik
python3 hayvan_golgeleri.py --hayvan tavsan
```

### Program test et (Test program):

```bash
python3 hayvan_golgeleri.py --test
```

## Açıklama (Description)

Bu program aşağıdaki hayvan gölgelerini gösterir:
- Kedi (Cat)
- Köpek (Dog)
- Kuş (Bird)
- Balık (Fish)
- Tavşan (Rabbit)

## Gereksinimler (Requirements)

- Python 3.x

Herhangi bir ek kütüphane gerekmez (No additional libraries required).

## Sorun Giderme (Troubleshooting)

### Program çalışmıyor mu? (Program not working?)

1. **Python kurulu mu kontrol edin (Check if Python is installed):**
   ```bash
   python3 --version
   ```

2. **Test modunu çalıştırın (Run test mode):**
   ```bash
   python3 hayvan_golgeleri.py --test
   ```

3. **Windows'ta (On Windows):**
   ```cmd
   python hayvan_golgeleri.py
   ```

4. **Karakter kodlama sorunları (Encoding issues):**
   - Terminalinizin UTF-8 kodlamasını desteklediğinden emin olun
   - Windows'ta: `chcp 65001` komutunu çalıştırın

5. **İzin hatası (Permission error):**
   ```bash
   chmod +x hayvan_golgeleri.py
   ./hayvan_golgeleri.py
   ```

## Yardım (Help)

```bash
python3 hayvan_golgeleri.py --help
```

