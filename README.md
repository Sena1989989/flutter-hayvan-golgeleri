# hayvan_golgeleri

Hayvan Gölgeleri (Animal Shadows) - Hayvan gölgelerini ASCII sanatı olarak gösteren basit bir Python programı.

## Visual Studio'da Açma (Opening in Visual Studio)

### Visual Studio (Windows)

1. **Python desteğini yükleyin (Install Python support):**
   - Visual Studio Installer'ı açın
   - "Python development" workload'unu yükleyin

2. **Projeyi açın (Open the project):**
   - Visual Studio'yu açın
   - `File` → `Open` → `Project/Solution`
   - `hayvan_golgeleri.sln` dosyasını seçin

3. **Çalıştırın (Run):**
   - `F5` tuşuna basın veya
   - `Debug` → `Start Debugging`

### Visual Studio Code (Tüm platformlar / All platforms)

1. **VS Code'u açın (Open VS Code)**

2. **Workspace'i açın (Open workspace):**
   - `File` → `Open Workspace from File`
   - `hayvan_golgeleri.code-workspace` dosyasını seçin

3. **Veya klasörü açın (Or open folder):**
   - `File` → `Open Folder`
   - `hayvan_golgeleri` klasörünü seçin

4. **Çalıştırın (Run):**
   - `F5` tuşuna basın veya
   - `Run` → `Start Debugging`
   - Veya terminalde: `python3 hayvan_golgeleri.py`

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

