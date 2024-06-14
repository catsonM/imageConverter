import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, Scale, HORIZONTAL, Listbox, StringVar, OptionMenu, Checkbutton, IntVar, Toplevel, ttk
from PIL import Image, ImageTk

def convert_image(input_path, output_path, quality, output_format):
    try:
        image = Image.open(input_path)
        image = image.convert("RGB")
        image.save(output_path, format=output_format, quality=quality)
        return True, None
    except Exception as e:
        return False, str(e)

def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.webp *.png *.bmp *.gif")])
    if file_paths:
        for file_path in file_paths:
            file_listbox.insert('end', file_path)

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
    output_dir = output_entry.get().strip()
    quality = quality_slider.get()
    output_format = format_var.get()
    use_subdir = subdir_var.get()
    errors = []

    if not output_dir:
        messagebox.showerror("Hata", "Lütfen çıktı dizinini seçin.")
        return

    if use_subdir:
        output_dir = os.path.join(output_dir, "jpeg_converted")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    progress_bar['maximum'] = file_listbox.size()
    progress_bar['value'] = 0

    for idx in range(file_listbox.size()):
        input_file = file_listbox.get(idx)
        input_file = os.path.abspath(input_file)
        if not os.path.isfile(input_file):
            errors.append(f"Girdi dosyası bulunamadı: {input_file}")
            continue

        output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(input_file))[0] + f".{output_format.lower()}")
        output_file = get_unique_output_path(output_file)
        
        quality = int((quality / 100) * 50 + 50)
        
        success, error = convert_image(input_file, output_file, quality, output_format)
        if not success:
            errors.append(f"Başarısız dönüştürme: {input_file} - Hata: {error}")

        progress_bar['value'] += 1
        app.update_idletasks()

    if errors:
        log_path = os.path.join(output_dir, "conversion_errors.txt")
        with open(log_path, 'w') as log_file:
            for error in errors:
                log_file.write(error + "\n")
        messagebox.showerror("Dönüştürme Tamamlandı", f"Bazı dosyalar dönüştürülemedi. Ayrıntılar için {log_path} dosyasına bakın.")
    else:
        messagebox.showinfo("Başarılı", "Tüm dosyalar başarıyla dönüştürüldü.")

def show_preview(event):
    try:
        file_path = file_listbox.get(file_listbox.curselection())
        image = Image.open(file_path)
        image.thumbnail((int(image.width * 0.8), int(image.height * 0.8)))
        photo = ImageTk.PhotoImage(image)
        preview_label.config(image=photo)
        preview_label.image = photo
    except Exception as e:
        preview_label.config(text="Önizleme yüklenemedi")

def set_output_dir(event):
    try:
        file_path = file_listbox.get(file_listbox.curselection())
        dir_path = os.path.dirname(file_path)
        output_entry.delete(0, 'end')
        output_entry.insert(0, dir_path)
    except Exception as e:
        pass

def remove_selected_files():
    selected_indices = file_listbox.curselection()
    for index in reversed(selected_indices):
        file_listbox.delete(index)

def select_all_files():
    file_listbox.select_set(0, 'end')

def show_help():
    help_window = Toplevel(app)
    help_window.title("Yardım")
    Label(help_window, text="Bu uygulama, seçtiğiniz görüntü dosyalarını dönüştürmek için kullanılır.").pack(padx=10, pady=10)
    Label(help_window, text="1. 'Dosyalar Seç' düğmesine tıklayarak dönüştürmek istediğiniz dosyaları seçin.").pack(padx=10, pady=5)
    Label(help_window, text="2. 'Dizin Seç' düğmesine tıklayarak çıktı dizinini seçin.").pack(padx=10, pady=5)
    Label(help_window, text="3. Kalite ve format ayarlarını yapın.").pack(padx=10, pady=5)
    Label(help_window, text="4. 'Dönüştür' düğmesine tıklayın.").pack(padx=10, pady=5)
    Label(help_window, text="Eğer dönüştürme sırasında hata alırsanız, hataları içeren bir log dosyası oluşturulacaktır.").pack(padx=10, pady=5)
    Button(help_window, text="Kapat", command=help_window.destroy).pack(pady=10)

app = Tk()
app.title("Image Converter")

Label(app, text="Dönüştürülecek dosyaların yolu:").grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky='w')
file_listbox = Listbox(app, width=60, height=10, selectmode='extended')
file_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
file_listbox.bind('<<ListboxSelect>>', show_preview)
file_listbox.bind('<Double-Button-1>', set_output_dir)

Button(app, text="Dosyalar Seç", command=select_files, width=20, height=2).grid(row=2, column=0, padx=10, pady=5, sticky='e')
Button(app, text="Tümünü Seç", command=select_all_files, width=20, height=2).grid(row=2, column=1, padx=10, pady=5, sticky='w')
Button(app, text="Seçilen Dosyaları Kaldır", command=remove_selected_files, width=20, height=2).grid(row=2, column=2, padx=10, pady=5, sticky='w')

Label(app, text="Kaydedilecek dizin:").grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky='w')
output_entry = Entry(app, width=50)
output_entry.grid(row=4, column=0, padx=10, pady=5, columnspan=2, sticky='we')
Button(app, text="Dizin Seç", command=select_output_dir, width=20, height=2).grid(row=4, column=2, padx=10, pady=5)

subdir_var = IntVar()
subdir_check = Checkbutton(app, text="JPEG dosyalarını alt dizine kaydet", variable=subdir_var)
subdir_check.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

Label(app, text="Kalite (0-100):").grid(row=6, column=0, padx=10, pady=5, sticky='e')
quality_slider = Scale(app, from_=0, to=100, orient=HORIZONTAL)
quality_slider.set(100)
quality_slider.grid(row=6, column=1, padx=10, pady=5, columnspan=2, sticky='we')

Label(app, text="Çıktı Formatı:").grid(row=7, column=0, padx=10, pady=5, sticky='e')
format_var = StringVar(app)
format_var.set("JPEG")
format_menu = OptionMenu(app, format_var, "JPEG", "PNG", "BMP", "GIF")
format_menu.grid(row=7, column=1, padx=10, pady=5, columnspan=2, sticky='w')

progress_bar = ttk.Progressbar(app, orient='horizontal', mode='determinate')
progress_bar.grid(row=8, column=0, columnspan=3, padx=10, pady=10, sticky='we')

Button(app, text="Dönüştür", command=process_conversion, width=20, height=2).grid(row=9, column=0, padx=10, pady=10, sticky='e')
Button(app, text="Yardım", command=show_help, width=20, height=2).grid(row=9, column=1, padx=10, pady=10, sticky='w')

preview_label = Label(app, text="Önizleme Yok", width=80, height=30)
preview_label.grid(row=1, column=3, rowspan=6, padx=10, pady=5, sticky='n')

app.mainloop()
