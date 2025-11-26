import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

root = tk.Tk()
root.title("Quản lý bệnh nhân")
root.geometry("900x700")
root.resizable(False, False)

# ===== TIÊU ĐỀ =====
tk.Label(root, text="QUẢN LÝ BỆNH NHÂN",
         font=("Arial", 22, "bold"),
         fg="#003366").pack(pady=15)

# ===== KHUNG THÔNG TIN =====
frame_info = ttk.LabelFrame(root, text="Thông tin bệnh nhân", padding=15)
frame_info.pack(fill="x", padx=20, pady=5)

# Dòng 1
tk.Label(frame_info, text="Mã số:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_maso = tk.Entry(frame_info, width=25)
entry_maso.grid(row=0, column=1, sticky="w", padx=5)

tk.Label(frame_info, text="Mã phòng:").grid(row=0, column=2, sticky="e", padx=5)
entry_map = tk.Entry(frame_info, width=25)
entry_map.grid(row=0, column=3, sticky="w", padx=5)

# Dòng 2
tk.Label(frame_info, text="Họ lót:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_holot = tk.Entry(frame_info, width=25)
entry_holot.grid(row=1, column=1, sticky="w", padx=5)

tk.Label(frame_info, text="Tên:").grid(row=1, column=2, sticky="e", padx=5)
entry_ten = tk.Entry(frame_info, width=25)
entry_ten.grid(row=1, column=3, sticky="w", padx=5)

# Dòng 3
tk.Label(frame_info, text="Phái:").grid(row=2, column=0, sticky="e", padx=5)
gender_var = tk.StringVar(value="Nam")
tk.Radiobutton(frame_info, text="Nam", variable=gender_var, value="Nam").grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame_info, text="Nữ", variable=gender_var, value="Nữ").grid(row=2, column=1, sticky="e", padx=50)

# Dòng 4
tk.Label(frame_info, text="Ngày sinh:").grid(row=2, column=2, sticky="e", padx=5)
entry_ngaysinh = DateEntry(frame_info, width=22, date_pattern='yyyy-mm-dd')
entry_ngaysinh.grid(row=2, column=3, sticky="w", padx=5)

# Dòng 5
tk.Label(frame_info, text="Loại bệnh nhân:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
type_var = tk.StringVar(value="NoiTru")
tk.Radiobutton(frame_info, text="Nội trú", variable=type_var, value="NoiTru").grid(row=3, column=1, sticky="w")
tk.Radiobutton(frame_info, text="Ngoại trú", variable=type_var, value="NgoaiTru").grid(row=3, column=2, sticky="w")

# ========= NOTEBOOK =========
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=5)

tab_benhnhan = ttk.Frame(notebook)
tab_bacsi = ttk.Frame(notebook)
tab_phong = ttk.Frame(notebook)
tab_phieukham = ttk.Frame(notebook)
tab_thuoc = ttk.Frame(notebook)
tab_toathuoc = ttk.Frame(notebook)

notebook.add(tab_benhnhan, text="Bệnh nhân")
notebook.add(tab_phong, text="Phòng bệnh")
notebook.add(tab_phieukham, text="Phiếu khám")
notebook.add(tab_thuoc, text="Thuốc")
notebook.add(tab_toathuoc, text="Toa thuốc")

# ======== BẢNG DỮ LIỆU ========
frame_table = ttk.LabelFrame(tab_benhnhan, text="Danh sách bệnh nhân", padding=10)
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("MaBN", "HoLot", "Ten", "Phai", "NgaySinh", "LoaiBN")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")

tree.pack(fill="both", expand=True)

# ======== NÚT ========
frame_buttons = tk.Frame(tab_benhnhan)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Thêm", width=12, bg="#c9c2f7")
btn_add.grid(row=0, column=0, padx=10)

btn_update = tk.Button(frame_buttons, text="Sửa", width=12, bg="#ffd900")
btn_update.grid(row=0, column=1, padx=10)

btn_delete = tk.Button(frame_buttons, text="Xóa", width=12, bg="#ec1818")
btn_delete.grid(row=0, column=2, padx=10)

btn_clear = tk.Button(frame_buttons, text="Làm mới", width=12, bg="#e0e0e0")
btn_clear.grid(row=0, column=3, padx=10)

# ===== TAB BÁC SĨ =====

def create_tab_bacsi(notebook):
    tab = ttk.Frame(notebook, padding=10)
    notebook.add(tab, text="Bác sĩ")

    # ===== KHUNG THÔNG TIN =====
    frame_info = ttk.LabelFrame(tab, text="Thông tin bác sĩ", padding=10)
    frame_info.pack(fill="x", padx=10, pady=10)

    # --- Hàng 1 ---
    ttk.Label(frame_info, text="Mã BS:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_mabs = ttk.Entry(frame_info, width=20)
    entry_mabs.grid(row=0, column=1, sticky="w")

    ttk.Label(frame_info, text="Họ lót:").grid(row=0, column=2, sticky="e", padx=5)
    entry_holot = ttk.Entry(frame_info, width=20)
    entry_holot.grid(row=0, column=3, sticky="w")

    # --- Hàng 2 ---
    ttk.Label(frame_info, text="Tên:").grid(row=1, column=0, sticky="e", padx=5)
    entry_ten = ttk.Entry(frame_info, width=20)
    entry_ten.grid(row=1, column=1, sticky="w")

    ttk.Label(frame_info, text="Khoa:").grid(row=1, column=2, sticky="e")
    combo_khoa = ttk.Combobox(frame_info, values=[
        "Nội tổng quát", "Ngoại", "Da liễu", "Nhi", "Tim mạch", "Cấp cứu"
    ], width=18, state="readonly")
    combo_khoa.grid(row=1, column=3, sticky="w")

    # --- Hàng 3 ---
    ttk.Label(frame_info, text="Địa chỉ:").grid(row=2, column=0, sticky="e", padx=5)
    entry_diachi = ttk.Entry(frame_info, width=50)
    entry_diachi.grid(row=2, column=1, columnspan=3, sticky="w")

    # ===== KHUNG TABLE =====
    frame_table = ttk.LabelFrame(tab, text="Danh sách bác sĩ", padding=10)
    frame_table.pack(fill="both", expand=True, padx=10, pady=10)

    columns = ("MaBS", "HoLot", "Ten", "Khoa", "DiaChi")
    tree_bs = ttk.Treeview(frame_table, columns=columns, show="headings", height=12)

    for col in columns:
        tree_bs.heading(col, text=col)
        tree_bs.column(col, width=150)

    tree_bs.pack(fill="both", expand=True)

    # ===== KHUNG BUTTON =====
    frame_btn = ttk.Frame(tab)
    frame_btn.pack(pady=10)

    ttk.Button(frame_btn, text="Thêm", width=12).grid(row=0, column=0, padx=5)
    ttk.Button(frame_btn, text="Sửa", width=12).grid(row=0, column=1, padx=5)
    ttk.Button(frame_btn, text="Xóa", width=12).grid(row=0, column=2, padx=5)
    ttk.Button(frame_btn, text="Làm mới", width=12).grid(row=0, column=3, padx=5)

    return tab

tab_bacsi = create_tab_bacsi(notebook)
notebook.add(tab_bacsi, text="Bác sĩ")

root.mainloop()
