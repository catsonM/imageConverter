# JPEG Converter GUI

EN:
JPEG Converter GUI is a user-friendly application developed in Python that allows you to convert various image files to JPEG, PNG, BMP, and GIF formats through an easy-to-use graphical interface.

## Features

- **Multiple File Selection:** Convert multiple files at once.
- **Directory Selection:** Choose the directory to save the output files.
- **Quality Setting:** Adjust the quality of the converted JPEG file (0-100).
- **Output Format:** Choose the format of the converted file (JPEG, PNG, BMP, GIF).
- **Preview:** View a preview of the selected files.
- **Error Logging:** Logs errors during the conversion process.
- **Subdirectory Option:** Save JPEG files to a specific subdirectory.
- **GUI:** User-friendly graphical interface.
- **Close Button:** A practical exit button to close the application.

## Requirements

- Python 3.x
- Pillow
- Tkinter
- PyInstaller (to convert to exe)

## Installation

1. Install the required dependencies:
    ```sh
    pip install pillow tkinter pyinstaller
    ```

2. Download or clone the project files.

3. Run the `jpegConverter_GUI_v2.3.py` file to start the application:
    ```sh
    python jpegConverter_GUI_v2.3.py
    ```

## Creating an EXE File

1. Use `pyinstaller` to convert the script to an exe file:
    ```sh
    pyinstaller --onefile --windowed jpegConverter_GUI_v2.3.py
    ```

2. Find the created exe file in the `dist` folder.

## Usage

1. **Select Files:** Click the `Select Files` button to choose the files you want to convert.
2. **Select Directory:** Click the `Select Directory` button to choose the directory to save the output files.
3. **Quality Setting:** Use the `Quality (0-100)` slider to adjust the quality of the converted JPEG files.
4. **Output Format:** Choose the format of the converted files from the `Output Format` dropdown menu.
5. **Subdirectory:** Check the `Save JPEG files to subdirectory` option to save JPEG files to a specific subdirectory.
6. **Convert:** Click the `Convert` button to start the conversion process.
7. **Preview:** View the preview of the selected files on the right side.
8. **Close:** Click the `Close` button to exit the application.
9. **Help:** Click the `Help` button to get detailed information about the application.

## Contributing

1. Fork the project.
2. Create a new branch.
3. Commit your changes.
4. Push your changes.
5. Open a Pull Request.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.

## Contact

Author: Catoglu

Email: catoglu@outlook.com

---

TR:
JPEG Converter GUI, Python ile geliştirilmiş, kullanıcı dostu bir arayüz aracılığıyla çeşitli görüntü dosyalarını JPEG, PNG, BMP ve GIF formatlarına dönüştürmenizi sağlayan bir araçtır.

## Özellikler

- **Çoklu Dosya Seçimi:** Aynı anda birden fazla dosyayı seçip dönüştürebilirsiniz.
- **Dizin Seçimi:** Çıktı dosyalarının kaydedileceği dizini seçebilirsiniz.
- **Kalite Ayarı:** Dönüştürülen JPEG dosyasının kalitesini ayarlayabilirsiniz (0-100).
- **Çıktı Formatı:** Dönüştürülen dosyanın formatını seçebilirsiniz (JPEG, PNG, BMP, GIF).
- **Önizleme:** Seçilen dosyaların önizlemesini görüntüleyebilirsiniz.
- **Hata Loglama:** Dönüştürme sırasında oluşan hatalar için log dosyası oluşturulur.
- **Alt Dizin Seçeneği:** JPEG dosyalarını belirli bir alt dizine kaydedebilirsiniz.
- **GUI:** Kullanıcı dostu grafik arayüzü ile kolay kullanım.
- **Kapat Butonu:** Uygulamayı kapatma butonu ile pratik çıkış imkanı.

## Gereksinimler

- Python 3.x
- Pillow
- Tkinter
- PyInstaller (exe dosyasına dönüştürmek için)

## Kurulum

1. Gerekli bağımlılıkları yükleyin:
    ```sh
    pip install pillow tkinter pyinstaller
    ```

2. Proje dosyasını indirin veya klonlayın.

3. `jpegConverter_GUI_v2.3.py` dosyasını çalıştırarak uygulamayı başlatın:
    ```sh
    python jpegConverter_GUI_v2.3.py
    ```

## EXE Dosyası Oluşturma

1. `pyinstaller` aracını kullanarak scripti exe dosyasına dönüştürün:
    ```sh
    pyinstaller --onefile --windowed jpegConverter_GUI_v2.3.py
    ```

2. Oluşturulan exe dosyasını `dist` klasöründe bulabilirsiniz.

## Kullanım

1. **Dosya Seç:** `Dosya Seç` butonuna tıklayarak dönüştürmek istediğiniz dosyaları seçin.
2. **Dizin Seç:** `Dizin Seç` butonuna tıklayarak çıktı dosyalarının kaydedileceği dizini seçin.
3. **Kalite Ayarı:** `Kalite (0-100)` kaydırıcısını kullanarak dönüştürülen JPEG dosyasının kalitesini ayarlayın.
4. **Çıktı Formatı:** `Çıktı Formatı` menüsünden dönüştürülen dosyanın formatını seçin.
5. **Alt Dizin:** `JPEG dosyalarını alt dizine kaydet` seçeneğini işaretleyerek JPEG dosyalarını belirli bir alt dizine kaydedin.
6. **Dönüştür:** `Dönüştür` butonuna tıklayarak dönüştürme işlemini başlatın.
7. **Önizleme:** Seçilen dosyanın önizlemesini sağ tarafta görebilirsiniz.
8. **Kapat:** `Kapat` butonuna tıklayarak uygulamayı kapatın.
9. **Yardım:** `Yardım` butonuna tıklayarak uygulama hakkında detaylı bilgi alabilirsiniz.

## Katkıda Bulunma

1. Projeyi fork edin.
2. Yeni bir dal (branch) oluşturun.
3. Yaptığınız değişiklikleri commit edin.
4. Değişikliklerinizi push edin.
5. Bir Pull Request açın.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## İletişim

Author: Catoglu

Email: catoglu@outlook.com
