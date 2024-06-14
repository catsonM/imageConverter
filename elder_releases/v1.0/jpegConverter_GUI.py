import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, Scale, HORIZONTAL
from PIL import Image

def convert_webp_to_jpeg(input_path, output_path, quality):
    try:
        # Resmi aç
        image = Image.open(input_path)
        # Resmi JPEG formatında kaydet, kaliteyi ayarla
        image = image.convert("RGB")
        image.save(output_path, "JPEG", quality=quality)
        messagebox.showinfo("Başarılı", f"{input_path} başarıyla {output_path} olarak kaydedildi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Resmi dönüştürme sırasında bir hata oluştu: {e}")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("WEBP files", "*.webp")])
    if file_path:
        input_entry.delete(0, 'end')
        input_entry.insert(0, file_path)

def select_output_dir():
    dir_path = filedialog.askdirectory()
    if dir_path:
        output_entry.delete(0, 'end')
        output_entry.insert(0, dir_path)

def get_unique_output_path(output_path):
    base, ext = os.path.splitext(output_path)
    counter = 1
    new_output_path = output_path

    while os.path.exists(new_output_path):
        new_output_path = f"{base}({counter}){ext}"
        counter += 1

    return new_output_path

def process_conversion():
    input_file = input_entry.get().strip()
    output_dir = output_entry.get().strip()
    quality = quality_slider.get()

    if not input_file:
        messagebox.showerror("Hata", "Lütfen dönüştürmek istediğiniz .webp dosyasının yolunu girin.")
        return

    input_file = os.path.abspath(input_file)
    if not os.path.isfile(input_file):
        messagebox.showerror("Hata", f"Girdi dosyası bulunamadı: {input_file}")
        return

    if not output_dir:
        output_dir = os.path.dirname(input_file)
        output_dir = os.path.join(output_dir, "jpeg_convert")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(input_file))[0] + ".jpeg")
    
    # Quality scale from 50 to 100
    quality = int((quality / 100) * 50 + 50)
    
    # Get unique output path
    output_file = get_unique_output_path(output_file)
    
    convert_webp_to_jpeg(input_file, output_file, quality)

app = Tk()
app.title("WEBP to JPEG Converter")

Label(app, text="Dönüştürülecek .webp dosyasının yolu:").grid(row=0, column=0, padx=10, pady=5)
input_entry = Entry(app, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=5)
Button(app, text="Dosya Seç", command=select_file).grid(row=0, column=2, padx=10, pady=5)

Label(app, text="Kaydedilecek dizin (boş bırakılırsa varsayılan dizin):").grid(row=1, column=0, padx=10, pady=5)
output_entry = Entry(app, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=5)
Button(app, text="Dizin Seç", command=select_output_dir).grid(row=1, column=2, padx=10, pady=5)

Label(app, text="Kalite (0-100):").grid(row=2, column=0, padx=10, pady=5)
quality_slider = Scale(app, from_=0, to=100, orient=HORIZONTAL)
quality_slider.set(100)  # Default value 100 (mapped to quality 100)
quality_slider.grid(row=2, column=1, padx=10, pady=5)

Button(app, text="Dönüştür", command=process_conversion).grid(row=3, column=0, columnspan=3, pady=10)

app.mainloop()
