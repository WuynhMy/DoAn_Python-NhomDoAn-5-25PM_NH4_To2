import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

# ====== WINDOW ======
root = tk.Tk()
root.title("Quản lý bệnh nhân")
root.geometry("1000x750")
root.configure(bg="#EBF5FB")

# ===== STYLE =====
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", font=("Segoe UI", 12))
style.configure("TEntry", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 12))
style.configure("Treeview.Heading", font=("Segoe UI", 12, "bold"))

# ===== TIÊU ĐỀ =====
tk.Label(root,
         text="QUẢN LÝ BỆNH NHÂN",
         font=("Arial", 26, "bold"),
         fg="#1B4F72",
         bg="#EBF5FB").pack(pady=20)

# ============= NOTEBOOK =============
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=20, pady=10)

tab_bn = ttk.Frame(notebook)
notebook.add(tab_bn, text="Bệnh Nhân")
tab_phongbenh=ttk.Frame(notebook)
notebook.add(tab_phongbenh,text="Phòng Bệnh")

# ===== FRAME THÔNG TIN =====
frame_info = tk.LabelFrame(tab_bn, text="THÔNG TIN BỆNH NHÂN",
                           bg="#EBF5FB", fg="#1B4F72",
                           font=("Arial", 14, "bold"),
                           padx=15, pady=15)
frame_info.pack(fill="x", padx=20)

# Cột trái
left_col = tk.Frame(frame_info, bg="#EBF5FB")
left_col.grid(row=0, column=0, padx=20)

tk.Label(left_col, text="Mã số:", bg="#EBF5FB").pack(anchor="w")
entry_maso = tk.Entry(left_col, width=30)
entry_maso.pack(anchor="w", pady=5)

tk.Label(left_col, text="Họ lót:", bg="#EBF5FB").pack(anchor="w")
entry_holot = tk.Entry(left_col, width=30)
entry_holot.pack(anchor="w", pady=5)

tk.Label(left_col, text="Phái:", bg="#EBF5FB").pack(anchor="w")
gender_var = tk.StringVar(value="Nam")
tk.Radiobutton(left_col, text="Nam", variable=gender_var, value="Nam", bg="#EBF5FB").pack(anchor="w")
tk.Radiobutton(left_col, text="Nữ", variable=gender_var, value="Nữ", bg="#EBF5FB").pack(anchor="w")

# Cột phải
right_col = tk.Frame(frame_info, bg="#EBF5FB")
right_col.grid(row=0, column=1, padx=20)

tk.Label(right_col, text="Mã phòng:", bg="#EBF5FB").pack(anchor="w")
entry_map = tk.Entry(right_col, width=30)
entry_map.pack(anchor="w", pady=5)

tk.Label(right_col, text="Tên:", bg="#EBF5FB").pack(anchor="w")
entry_ten = tk.Entry(right_col, width=30)
entry_ten.pack(anchor="w", pady=5)

tk.Label(right_col, text="Ngày sinh:", bg="#EBF5FB").pack(anchor="w")
entry_ngaysinh = DateEntry(right_col, width=27, date_pattern="yyyy-mm-dd")
entry_ngaysinh.pack(anchor="w", pady=5)

tk.Label(frame_info, text="Loại bệnh nhân:", bg="#EBF5FB").grid(row=1, column=0, sticky="w", pady=10)
type_var = tk.StringVar(value="NoiTru")
tk.Radiobutton(frame_info, text="Nội trú", variable=type_var, value="NoiTru", bg="#EBF5FB").grid(row=1, column=0, sticky="e")
tk.Radiobutton(frame_info, text="Ngoại trú", variable=type_var, value="NgoaiTru", bg="#EBF5FB").grid(row=1, column=1, sticky="w")

# ===== BẢNG =====
frame_table = tk.LabelFrame(tab_bn, text="DANH SÁCH BỆNH NHÂN",
                            bg="#EBF5FB", fg="#1B4F72",
                            font=("Arial", 14, "bold"),
                            padx=10, pady=10)
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("MaBN", "HoLot", "Ten", "Phai", "NgaySinh", "LoaiBN")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill="both", expand=True)

# ===== NÚT =====
btn_frame = tk.Frame(tab_bn, bg="#EBF5FB")
btn_frame.pack(pady=10)

def make_btn(parent, text, color):
    return tk.Button(parent, text=text, width=12, font=("Segoe UI", 12, "bold"),
                     bg=color, fg="black", relief="ridge", bd=2)

btn_add = make_btn(btn_frame, "Thêm", "#58D68D")
btn_update = make_btn(btn_frame, "Sửa", "#F5B041")
btn_delete = make_btn(btn_frame, "Xóa", "#EC7063")
btn_clear = make_btn(btn_frame, "Làm mới", "#D7DBDD")

btn_add.grid(row=0, column=0, padx=12)
btn_update.grid(row=0, column=1, padx=12)
btn_delete.grid(row=0, column=2, padx=12)
btn_clear.grid(row=0, column=3, padx=12)

#Tab phòng khám
frame_info = tk.LabelFrame(tab_phongbenh, text="DANH SÁCH PHÒNG BỆNH",
                           bg="#EBF5FB", fg="#1B4F72",
                           font=("Arial", 14, "bold"),
                           padx=15, pady=15)
frame_info.pack(fill="x", padx=20)

tk.Label(frame_info, text="Mã phòng:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
p_maphong = tk.Entry(frame_info, width=30)
p_maphong.grid(row=0, column=1, pady=5)

tk.Label(frame_info, text="Tên phòng:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
p_tenphong = tk.Entry(frame_info, width=30)
p_tenphong.grid(row=1, column=1, pady=5)

tk.Label(frame_info, text="Số giường:", bg="#EBF5FB").grid(row=2, column=0, sticky="w")
p_sogiuong = tk.Entry(frame_info, width=30)
p_sogiuong.grid(row=2, column=1, pady=5)

tk.Label(frame_info, text="Ghi chú:", bg="#EBF5FB").grid(row=3, column=0, sticky="w")
p_note = tk.Entry(frame_info, width=30)
p_note.grid(row=3, column=1, pady=5)

Frame_table = tk.LabelFrame(tab_bn, text="DANH SÁCH PHÒNG BỆNH",
                            bg="#EBF5FB", fg="#1B4F72",
                            font=("Arial", 14, "bold"),
                            padx=10, pady=10)
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

columns_phong = ("MaPhong", "TenPhong", "SoGiuong", "GhiChu")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=12)

tree.pack(fill="both", expand=True)
root.mainloop()
