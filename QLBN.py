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
tab_bacsi =ttk.Notebook(notebook)
notebook.add(tab_bacsi, text="Bác Sĩ")
tab_phieukham = ttk.Frame(notebook)
notebook.add(tab_phieukham,text="Phiếu Khám")
tab_thuoc = ttk.Frame(notebook)
notebook.add(tab_thuoc,text="Thuốc")
tab_cttoathuoc = ttk.Frame(notebook)
notebook.add(tab_cttoathuoc,text="Chi tiết toa thuốc")

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

tk.Label(right_col, text="Địa Chỉ:", bg="#EBF5FB").pack(anchor="w")
entry_diachi = tk.Entry(right_col, width=30)
entry_diachi.pack(anchor="w", pady=0,padx=5)

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

columns = ("MaBN", "Họ Lót", "Tên", "Phái", "Ngày Sinh", "Loại Bệnh Nhân")
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
# --- Khung nhập liệu ---
frame_info = tk.LabelFrame(
    tab_phongbenh, text="THÔNG TIN PHÒNG BỆNH",
    bg="#EBF5FB", fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=15, pady=15
)
frame_info.pack(fill="x", padx=20)

tk.Label(frame_info, text="Mã phòng:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
p_maphong = tk.Entry(frame_info, width=30)
p_maphong.grid(row=0, column=1, pady=5)

tk.Label(frame_info, text="Tên phòng:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
p_tenphong = tk.Entry(frame_info, width=30)
p_tenphong.grid(row=1, column=1, pady=5)

tk.Label(frame_info, text="Loại phòng:", bg="#EBF5FB").grid(row=2, column=0, sticky="w")
type_var = tk.StringVar(value="NoiTru")
tk.Radiobutton(frame_info, text="Nội trú", variable=type_var, value="NoiTru", bg="#EBF5FB").grid(row=2, column=1, sticky="e")
tk.Radiobutton(frame_info, text="Ngoại trú", variable=type_var, value="NgoaiTru", bg="#EBF5FB").grid(row=2, column=1, sticky="w")


# --- KHUNG BẢNG DƯỚI ---
frame_table = tk.LabelFrame(
    tab_phongbenh, text="Danh sách phòng bệnh",
    bg="#EBF5FB", fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=10, pady=10
)
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

# --- BẢNG TREEVIEW ---
columns_phong = ("Mã Phòng", "Tên Phòng", "Loại Phòng")

tree = ttk.Treeview(frame_table, columns=columns_phong, show="headings", height=12)
tree.pack(fill="both", expand=True)

for col in columns_phong:
    tree.heading(col, text=col)
    tree.column(col, width=150)
#Tab bác sĩ
#Frame thông tin
frame_info = tk.LabelFrame(
    tab_bacsi, text="THÔNG TIN BÁC SĨ",
    bg="#EBF5FB", fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=15, pady=15
)
frame_info.pack(fill="x", padx=20)

# Tạo 2 cột
left_col = tk.Frame(frame_info, bg="#EBF5FB")
left_col.grid(row=0, column=0, padx=10, pady=5, sticky="nw")

right_col = tk.Frame(frame_info, bg="#EBF5FB")
right_col.grid(row=0, column=1, padx=10, pady=5, sticky="nw")

# ====== CỘT TRÁI ======
tk.Label(left_col, text="Mã bác sĩ:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
entry_mabs = tk.Entry(left_col, width=30)
entry_mabs.grid(row=0, column=1, pady=5)

tk.Label(left_col, text="Họ lót:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
entry_holot = tk.Entry(left_col, width=30)
entry_holot.grid(row=1, column=1, pady=5)

tk.Label(left_col, text="Tên:", bg="#EBF5FB").grid(row=2, column=0, sticky="w")
entry_ten = tk.Entry(left_col, width=30)
entry_ten.grid(row=2, column=1, pady=5)

tk.Label(left_col, text="Khoa khám:", bg="#EBF5FB").grid(row=3, column=0, sticky="w")
combo_khoa = ttk.Combobox(
    left_col,
    values=[
        "Nội tổng hợp",
        "Ngoại tổng hợp",
        "Sản",
        "Nhi",
        "Hồi sức cấp cứu",
        "Tim mạch",
        "Da liễu",
        "Tai Mũi Họng"
    ],
    state="readonly",
    width=28
)
combo_khoa.grid(row=3, column=1, pady=5)

# ====== CỘT PHẢI ======
tk.Label(right_col, text="Địa chỉ:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
entry_diachi = tk.Entry(right_col, width=40)
entry_diachi.grid(row=1, column=0, pady=5, sticky="w")

# --- KHUNG BẢNG DƯỚI ---
frame_table = tk.LabelFrame(
    tab_bacsi, text="Danh sách bác sĩ",
    bg="#EBF5FB", fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=10, pady=10
)
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

# --- BẢNG TREEVIEW ---
columns_bacsi = ("Mã Bác Sĩ", "Họ Lót", "Tên","Địa Chỉ")

tree = ttk.Treeview(frame_table, columns=columns_bacsi, show="headings", height=12)
tree.pack(fill="both", expand=True)

for col in columns_bacsi:
    tree.heading(col, text=col)
    tree.column(col, width=150)

# =====================
# TAB PHIẾU KHÁM
# =====================
frame_info_pk = tk.LabelFrame(
    tab_phieukham,
    text="THÔNG TIN PHIẾU KHÁM",
    bg="#EBF5FB",
    fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=15, pady=15
)
frame_info_pk.pack(fill="x", padx=20, pady=10)


# ==== MÃ BỆNH NHÂN ====
tk.Label(frame_info_pk, text="Mã bệnh nhân:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
entry_mabn = tk.Entry(frame_info_pk, width=20)
entry_mabn.grid(row=0, column=1, pady=5)

label_bn_info = tk.Label(frame_info_pk, text="", bg="#EBF5FB", fg="blue", font=("Arial", 10, "italic"))
label_bn_info.grid(row=1, column=0, columnspan=3, sticky="w")


# ==== MÃ BÁC SĨ ====
tk.Label(frame_info_pk, text="Mã bác sĩ:", bg="#EBF5FB").grid(row=2, column=0, sticky="w")
entry_mabs = tk.Entry(frame_info_pk, width=20)
entry_mabs.grid(row=2, column=1, pady=5)

label_bs_info = tk.Label(frame_info_pk, text="", bg="#EBF5FB", fg="green", font=("Arial", 10, "italic"))
label_bs_info.grid(row=3, column=0, columnspan=3, sticky="w")


# ====================================
#     CÁC HÀM TỰ ĐỘNG HIỆN THÔNG TIN
# ====================================

def show_benhnhan_info(event=None):
    mabn = entry_mabn.get().strip()
    if mabn == "":
        label_bn_info.config(text="")
        return
    
    row = get_bn_info(mabn)
    if row:
        hoTen, ngaySinh, gioiTinh = row
        label_bn_info.config(
            text=f"Tên: {hoTen} | Ngày sinh: {ngaySinh} | Giới tính: {gioiTinh}"
        )
    else:
        label_bn_info.config(text="⚠ Không tìm thấy bệnh nhân!")

def show_bacsi_info(event=None):
    mabs = entry_mabs.get().strip()
    if mabs == "":
        label_bs_info.config(text="")
        return
    
    row = get_bacsi_info(mabs)
    if row:
        hoten, khoa = row
        label_bs_info.config(
            text=f"Bác sĩ: {hoten} | Khoa: {khoa}"
        )
    else:
        label_bs_info.config(text="⚠ Không tìm thấy bác sĩ!")


# GẮN SỰ KIỆN TỰ ĐỘNG TRA CỨU
entry_mabn.bind("<FocusOut>", show_benhnhan_info)
entry_mabn.bind("<KeyRelease>", show_benhnhan_info)

entry_mabs.bind("<FocusOut>", show_bacsi_info)
entry_mabs.bind("<KeyRelease>", show_bacsi_info)

frame_table_pk = tk.LabelFrame(
    tab_phieukham,
    text="DANH SÁCH PHIẾU KHÁM",
    bg="#EBF5FB",
    fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=10,
    pady=10
)
frame_table_pk.pack(fill="both", expand=True, padx=20, pady=10)

columns_pk = ("MaPK", "MaBN", "MaBS", "NgayKham", "LoaiKham", "ChanDoan")

tree_pk = ttk.Treeview(
    frame_table_pk,
    columns=columns_pk,
    show="headings",
    height=12
)

# ===== ĐẶT TÊN CỘT =====
tree_pk.heading("MaPK", text="Mã Phiếu")
tree_pk.heading("MaBN", text="Mã BN")
tree_pk.heading("MaBS", text="Mã Bác Sĩ")
tree_pk.heading("NgayKham", text="Ngày Khám")
tree_pk.heading("LoaiKham", text="Loại Khám")
tree_pk.heading("ChanDoan", text="Chẩn Đoán")

# ===== ĐỘ RỘNG CỘT =====
tree_pk.column("MaPK", width=110)
tree_pk.column("MaBN", width=110)
tree_pk.column("MaBS", width=110)
tree_pk.column("NgayKham", width=120)
tree_pk.column("LoaiKham", width=150)
tree_pk.column("ChanDoan", width=200)

tree_pk.pack(fill="both", expand=True)
#Tab thuốc
frame_info_t = tk.LabelFrame(
    tab_thuoc,
    text="THÔNG TIN THUỐC",
    bg="#EBF5FB",
    fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=15,
    pady=15
)
frame_info_t.pack(fill="x", padx=20, pady=10)

# CỘT TRÁI
left_t = tk.Frame(frame_info_t, bg="#EBF5FB")
left_t.grid(row=0, column=0, padx=20, sticky="nw")

tk.Label(left_t, text="Mã thuốc:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
t_mathuoc = tk.Entry(left_t, width=30)
t_mathuoc.grid(row=0, column=1, pady=5)

tk.Label(left_t, text="Tên thuốc:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
t_tenthuoc = tk.Entry(left_t, width=30)
t_tenthuoc.grid(row=1, column=1, pady=5)

tk.Label(left_t, text="Đơn vị:", bg="#EBF5FB").grid(row=2, column=0, sticky="w")
t_donvi = ttk.Combobox(left_t, values=["Viên", "Chai", "Hộp", "Ống"], width=27, state="readonly")
t_donvi.grid(row=2, column=1, pady=5)

# CỘT PHẢI
right_t = tk.Frame(frame_info_t, bg="#EBF5FB")
right_t.grid(row=0, column=1, padx=20, sticky="nw")

tk.Label(right_t, text="Giá thuốc:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
t_gia = tk.Entry(right_t, width=30)
t_gia.grid(row=0, column=1, pady=5)

tk.Label(right_t, text="Số lượng:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
t_soluong = tk.Entry(right_t, width=30)
t_soluong.grid(row=1, column=1, pady=5)

tk.Label(right_t, text="Công dụng:", bg="#EBF5FB").grid(row=2, column=0, sticky="w")
t_congdung = tk.Entry(right_t, width=30)
t_congdung.grid(row=2, column=1, pady=5)

# ===== KHUNG BẢNG THUỐC =====
frame_table_t = tk.LabelFrame(
    tab_thuoc,
    text="DANH SÁCH THUỐC",
    bg="#EBF5FB",
    fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=10,
    pady=10
)
frame_table_t.pack(fill="both", expand=True, padx=20, pady=10)

columns_t = ("MaThuoc", "TenThuoc", "DonVi", "Gia", "SoLuong","CongDung")

tree_thuoc = ttk.Treeview(frame_table_t, columns=columns_t, show="headings", height=12)

# ===== ĐẶT TÊN CỘT =====
tree_thuoc.heading("MaThuoc", text="Mã Thuốc")
tree_thuoc.heading("TenThuoc", text="Tên Thuốc")
tree_thuoc.heading("DonVi", text="Đơn Vị")
tree_thuoc.heading("Gia", text="Giá (VNĐ)")
tree_thuoc.heading("SoLuong", text="Số Lượng")

# ===== ĐỘ RỘNG =====
tree_thuoc.column("MaThuoc", width=120)
tree_thuoc.column("TenThuoc", width=200)
tree_thuoc.column("DonVi", width=120)
tree_thuoc.column("Gia", width=120)
tree_thuoc.column("SoLuong", width=120)

tree_thuoc.pack(fill="both", expand=True)

root.mainloop()