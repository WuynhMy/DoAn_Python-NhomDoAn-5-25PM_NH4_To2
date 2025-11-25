import tkinter as tk 
from tkinter import ttk, messagebox 
from tkcalendar import DateEntry 

root = tk.Tk()
root.title("Quản lý bệnh nhân")
root.geometry("850x650")
root.resizable(False, False)

tk.Label(root, text="QUẢN LÝ BỆNH NHÂN", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=4, pady=15)

# ===== HÀNG 1 =====
tk.Label(root, text="Mã số:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
tk.Entry(root, width=20).grid(row=1, column=1, sticky="w", padx=5)

tk.Label(root, text="Mã phòng:").grid(row=1, column=2, sticky="e", padx=5, pady=5)
tk.Entry(root, width=20).grid(row=1, column=3, sticky="w", padx=5)

# ===== HÀNG 2 =====
tk.Label(root, text="Họ lót:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
tk.Entry(root, width=20).grid(row=2, column=1, sticky="w", padx=5)

tk.Label(root, text="Tên:").grid(row=2, column=2, sticky="e", padx=5, pady=5)
tk.Entry(root, width=20).grid(row=2, column=3, sticky="w", padx=5)

# ===== HÀNG 3 =====
tk.Label(root, text="Phái:").grid(row=3, column=0, sticky="e", padx=5)
tk.Radiobutton(root, text="Nam", value="Nam").grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="Nữ", value="Nữ").grid(row=3, column=1, sticky="e")

# ===== HÀNG 4 =====
tk.Label(root, text="Ngày sinh:").grid(row=3, column=2, sticky="e", padx=5)
DateEntry(root, width=17, date_pattern='yyyy-mm-dd').grid(row=3, column=3, sticky="w")

# ===== HÀNG 5 =====
tk.Label(root, text="Loại bệnh nhân:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
tk.Radiobutton(root, text="Nội trú", value="NoiTru").grid(row=5, column=1, sticky="w")
tk.Radiobutton(root, text="Ngoại trú", value="NgoaiTru").grid(row=5, column=2, sticky="w")

# Canh đều cột
for i in range(4):
    root.columnconfigure(i, weight=1)

# ===== Notebook dùng GRID ====
notebook = ttk.Notebook(root)
notebook.grid(row=6, column=0, columnspan=4, sticky="nsew")

notebook.add(ttk.Frame(notebook), text="Bệnh nhân")
notebook.add(ttk.Frame(notebook), text="Bác sĩ")
notebook.add(ttk.Frame(notebook), text="Phòng bệnh")
notebook.add(ttk.Frame(notebook), text="Phiếu khám")
notebook.add(ttk.Frame(notebook), text="Thuốc")
notebook.add(ttk.Frame(notebook), text="Toa thuốc")

tab_benhnhan = ttk.Frame(notebook, padding=10)
tab_bacsi = ttk.Frame(notebook, padding=10)
tab_phong = ttk.Frame(notebook, padding=10)
tab_phieukham = ttk.Frame(notebook, padding=10)
tab_thuoc = ttk.Frame(notebook, padding=10)
tab_toathuoc = ttk.Frame(notebook, padding=10)  

frame_table = ttk.LabelFrame(tab_benhnhan, text="Danh sách bệnh nhân", padding=10)
frame_table.pack(expand=True, fill="both")

# Lấy tab bệnh nhân từ Notebook
tab_benhnhan = notebook.tabs()  # lấy danh sách tab
tab_benhnhan = notebook.nametowidget(tab_benhnhan[0])  # lấy tab đầu tiên "Bệnh nhân"

# ===== KHUNG TABLE =====
frame_table = ttk.LabelFrame(tab_benhnhan, text="Danh sách bệnh nhân", padding=10)
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

# Tạo bảng Treeview
columns = ("MaBN", "HoLot", "Ten", "Phai", "NgaySinh", "LoaiBN")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(fill="both", expand=True)

# ===== KHUNG NÚT =====
frame_buttons = tk.Frame(tab_benhnhan)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Thêm", width=12, bg="#d1ffd1")
btn_add.grid(row=0, column=0, padx=5)

btn_update = tk.Button(frame_buttons, text="Sửa", width=12, bg="#fff5cc")
btn_update.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_buttons, text="Xóa", width=12, bg="#ffd6d6")
btn_delete.grid(row=0, column=2, padx=5)

btn_clear = tk.Button(frame_buttons, text="Làm mới", width=12)
btn_clear.grid(row=0, column=3, padx=5)

root.mainloop()
