import tkinter as tk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
import mysql.connector

# ====== Kết nối MySQL ====== 
import mysql.connector

def connect_db(): 
    return mysql.connector.connect( 
        host="localhost", 
        user="root",        # thay bằng user MySQL của bạn 
        password="benhnhan12345",        # thay bằng password MySQL của bạn 
        database="QLBN" 
    )

def load_benhnhan():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MaBN, HoLot, Ten, Phai, NgaySinh, LoaiBenhNhan FROM BenhNhan")
    rows = cursor.fetchall()

    # Xóa dữ liệu cũ
    for item in tree.get_children():
        tree.delete(item)

    # Đổ dữ liệu mới
    for row in rows:
        tree.insert("", "end", values=row)

    cursor.close()
    conn.close()
#phòng bệnh
def load_phongbenh():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MaPhong, TenPhong, LoaiPhong FROM PhongBenh")
    rows = cursor.fetchall()

    tree_pb.delete(*tree_pb.get_children())

    for row in rows:
        tree_pb.insert("", "end", values=row)

    conn.close()
#bác sĩ
def load_bacsi():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MaBS, HoLot, Ten, Khoa, DiaChi FROM BacSi")
    rows = cursor.fetchall()

    tree_bs.delete(*tree_bs.get_children())

    for row in rows:
        tree_bs.insert("", "end", values=row)

    conn.close()
#Load dữ liệu phiếu khám
def load_phieukham():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MaPK, MaBN, MaBS, NgayKham, LoaiKham, ChanDoan,GhiChu FROM PhieuKham")
    rows = cursor.fetchall()

    tree_pk.delete(*tree_pk.get_children())

    for row in rows:
        tree_pk.insert("", "end", values=row)
#Load dữ liệu thuốc
def load_thuoc():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MaThuoc, TenThuoc, DonViThuoc, DonGia, CongDung FROM Thuoc")
    rows = cursor.fetchall()

    tree_thuoc.delete(*tree_thuoc.get_children())

    for row in rows:
        tree_thuoc.insert("", "end", values=row)
#Load dữ liệu toa thuốc
def load_cttoathuoc():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MaPK, MaThuoc, SoLuong, LieuDung FROM ChiTietToaThuoc")
    rows = cursor.fetchall()

    tree_cttt.delete(*tree_cttt.get_children())

    for row in rows:
        tree_cttt.insert("", "end", values=row)
root = tk.Tk() 
# ===== STYLE TỔNG =====
style = ttk.Style()
style.theme_use("clam")

# Chữ chung
style.configure("TLabel",
                font=("Segoe UI", 11),
                background="#EBF5FB")

style.configure("TEntry",
                font=("Segoe UI", 11))

style.configure("TRadiobutton",
                font=("Segoe UI", 11),
                background="#EBF5FB")

style.configure("TButton",
                font=("Segoe UI", 11, "bold"),
                padding=6)

# Bảng
style.configure("Treeview",
                font=("Segoe UI", 11),
                rowheight=28)

style.configure("Treeview.Heading",
                font=("Segoe UI", 12, "bold"),
                foreground="#1B4F72")

root.title("Quản lý bệnh nhân")
root.geometry("1000x750")
root.configure(bg="#EBF5FB")

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

# ======= KHUNG NÚT DÙNG CHUNG CHO TẤT CẢ TAB =======
frame_buttons = tk.Frame(root, bg="#EBF5FB")
frame_buttons.pack(pady=10)

def make_btn(parent, text, color):
    return tk.Button(
        parent, text=text, width=12,
        font=("Segoe UI", 12, "bold"),
        bg=color, fg="black", relief="ridge", bd=2
    )

btn_add = make_btn(frame_buttons, "Thêm", "#58D68D")
btn_edit = make_btn(frame_buttons, "Sửa", "#F5B041")
btn_delete = make_btn(frame_buttons, "Xóa", "#EC7063")
btn_clear = make_btn(frame_buttons, "Làm mới", "#D7DBDD")

btn_add.grid(row=0, column=0, padx=12)
btn_edit.grid(row=0, column=1, padx=12)
btn_delete.grid(row=0, column=2, padx=12)
btn_clear.grid(row=0, column=3, padx=12)

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
entry_maso = ttk.Entry(left_col, width=30)
entry_maso.pack(anchor="w", pady=5)

tk.Label(left_col, text="Họ lót:", bg="#EBF5FB").pack(anchor="w")
entry_holot = ttk.Entry(left_col, width=30)
entry_holot.pack(anchor="w", pady=5)

tk.Label(left_col, text="Phái:", bg="#EBF5FB").pack(anchor="w")
gender_var = tk.StringVar(value="Nam")
tk.Radiobutton(left_col, text="Nam", variable=gender_var, value="Nam", bg="#EBF5FB").pack(anchor="w")
tk.Radiobutton(left_col, text="Nữ", variable=gender_var, value="Nữ", bg="#EBF5FB").pack(anchor="w")

# Cột phải
right_col = tk.Frame(frame_info, bg="#EBF5FB")
right_col.grid(row=0, column=1, padx=20)

tk.Label(right_col, text="Mã phòng:", bg="#EBF5FB").pack(anchor="w")
entry_map = ttk.Entry(right_col, width=30)
entry_map.pack(anchor="w", pady=5)

tk.Label(right_col, text="Tên:", bg="#EBF5FB").pack(anchor="w")
entry_ten = ttk.Entry(right_col, width=30)
entry_ten.pack(anchor="w", pady=5)

tk.Label(right_col, text="Ngày sinh:", bg="#EBF5FB").pack(anchor="w")
entry_ngaysinh = DateEntry(right_col, width=27, date_pattern="yyyy-mm-dd")
entry_ngaysinh.pack(anchor="w", pady=5)

tk.Label(right_col, text="Địa Chỉ:", bg="#EBF5FB").pack(anchor="w")
entry_diachi = ttk.Entry(right_col, width=30)
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

columns = ("MaBN", "HoLot", "Ten", "Phai", "NgaySinh", "LoaiBenhNhan")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=12)

tree.heading("MaBN", text="Mã BN")
tree.heading("HoLot", text="Họ Lót")
tree.heading("Ten", text="Tên")
tree.heading("Phai", text="Phái")
tree.heading("NgaySinh", text="Ngày Sinh")
tree.heading("LoaiBenhNhan", text="Loại Bệnh Nhân")

tree.column("MaBN", width=120, anchor="center")
tree.column("HoLot", width=180, anchor="center")
tree.column("Ten", width=120, anchor="center")
tree.column("Phai", width=80, anchor="center")
tree.column("NgaySinh", width=150, anchor="center")
tree.column("LoaiBenhNhan", width=150, anchor="center")

tree.pack(fill="both", expand=True)
load_benhnhan()
#Tab phòng khám
# --- Khung nhập liệu ---
# --- KHUNG BẢNG DƯỚI ---

frame_info = tk.LabelFrame(
    tab_phongbenh, text="THÔNG TIN PHÒNG BỆNH",
    bg="#EBF5FB", fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=15, pady=15
)
frame_info.pack(fill="x", padx=20)

tk.Label(frame_info, text="Mã phòng:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
p_maphong = ttk.Entry(frame_info, width=30)
p_maphong.grid(row=0, column=1, pady=5)

tk.Label(frame_info, text="Tên phòng:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
p_tenphong = ttk.Entry(frame_info, width=30)
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

tree_pb = ttk.Treeview(frame_table, columns=columns_phong, show="headings", height=12)
tree_pb.pack(fill="both", expand=True)

for col in columns_phong:
    tree_pb.heading(col, text=col)
    tree_pb.column(col, width=150)
    load_phongbenh() 
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
entry_mabs = ttk.Entry(left_col, width=30)
entry_mabs.grid(row=0, column=1, pady=5)

tk.Label(left_col, text="Họ lót:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
entry_holot = ttk.Entry(left_col, width=30)
entry_holot.grid(row=1, column=1, pady=5)

tk.Label(left_col, text="Tên:", bg="#EBF5FB").grid(row=2, column=0, sticky="w")
entry_ten = ttk.Entry(left_col, width=30)
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
entry_diachi = ttk.Entry(right_col, width=40)
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

tree_bs = ttk.Treeview(frame_table, columns=columns_bacsi, show="headings", height=12)
tree_bs.pack(fill="both", expand=True)

for col in columns_bacsi:
    tree_bs.heading(col, text=col)
    tree_bs.column(col, width=150)
    load_bacsi()
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
entry_mabn = ttk.Entry(frame_info_pk, width=20)
entry_mabn.grid(row=0, column=1, pady=5)

label_bn_info = tk.Label(frame_info_pk, text="", bg="#EBF5FB", fg="blue", font=("Arial", 10, "italic"))
label_bn_info.grid(row=1, column=0, columnspan=3, sticky="w")


# ==== MÃ BÁC SĨ ====
tk.Label(frame_info_pk, text="Mã bác sĩ:", bg="#EBF5FB").grid(row=2, column=0, sticky="w")
entry_mabs = ttk.Entry(frame_info_pk, width=20)
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

columns_pk = ("MaPK", "MaBN", "MaBS", "NgayKham", "LoaiKham", "ChanDoan","GhiChu")

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
tree_pk.heading("GhiChu", text="Ghi Chú")

# ===== ĐỘ RỘNG CỘT =====
tree_pk.column("MaPK", width=110)
tree_pk.column("MaBN", width=110)
tree_pk.column("MaBS", width=110)
tree_pk.column("NgayKham", width=120)
tree_pk.column("LoaiKham", width=150)
tree_pk.column("ChanDoan", width=150)
tree_pk.column("GhiChu", width=150)

tree_pk.pack(fill="both", expand=True)
load_phieukham()

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
t_mathuoc = ttk.Entry(left_t, width=30)
t_mathuoc.grid(row=0, column=1, pady=5)

tk.Label(left_t, text="Tên thuốc:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
t_tenthuoc = ttk.Entry(left_t, width=30)
t_tenthuoc.grid(row=1, column=1, pady=5)

tk.Label(left_t, text="Đơn vị:", bg="#EBF5FB").grid(row=2, column=0, sticky="w")
t_donvi = ttk.Combobox(left_t, values=["Viên", "Chai", "Hộp", "Ống"], width=27, state="readonly")
t_donvi.grid(row=2, column=1, pady=5)

# CỘT PHẢI
right_t = tk.Frame(frame_info_t, bg="#EBF5FB")
right_t.grid(row=0, column=1, padx=20, sticky="nw")

tk.Label(right_t, text="Giá thuốc:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
t_gia = ttk.Entry(right_t, width=30)
t_gia.grid(row=0, column=1, pady=5)

tk.Label(right_t, text="Số lượng:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
t_soluong = ttk.Entry(right_t, width=30)
t_soluong.grid(row=1, column=1, pady=5)

tk.Label(right_t, text="Công dụng:", bg="#EBF5FB").grid(row=2, column=0, sticky="w")
t_congdung = ttk.Entry(right_t, width=30)
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
tree_thuoc.heading("CongDung", text="Công Dụng")

# ===== ĐỘ RỘNG =====
tree_thuoc.column("MaThuoc", width=120)
tree_thuoc.column("TenThuoc", width=200)
tree_thuoc.column("DonVi", width=120)
tree_thuoc.column("Gia", width=120)
tree_thuoc.column("SoLuong", width=120)
tree_thuoc.column("CongDung", width=120)

tree_thuoc.pack(fill="both", expand=True)
load_thuoc()

frame_info_ct = tk.LabelFrame(
    tab_cttoathuoc,
    text="THÔNG TIN CHI TIẾT TOA THUỐC",
    bg="#EBF5FB",
    fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=15,
    pady=15
)
frame_info_ct.pack(fill="x", padx=20, pady=10)

# ---- CỘT TRÁI ----
left_ct = tk.Frame(frame_info_ct, bg="#EBF5FB")
left_ct.grid(row=0, column=0, padx=20, sticky="nw")

tk.Label(left_ct, text="Mã Phiếu Khám:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
ct_mapk = ttk.Entry(left_ct,width=27)
ct_mapk.grid(row=0, column=1, pady=5)

tk.Label(left_ct, text="Mã Thuốc:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
ct_mathuoc = ttk.Entry(left_ct,width=27)
ct_mathuoc.grid(row=1, column=1, pady=5)

# ---- CỘT PHẢI ----
right_ct = tk.Frame(frame_info_ct, bg="#EBF5FB")
right_ct.grid(row=0, column=1, padx=20, sticky="nw")

tk.Label(right_ct, text="Số lượng:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
ct_soluong = ttk.Entry(right_ct, width=30)
ct_soluong.grid(row=0, column=1, pady=5)

tk.Label(right_ct, text="Liều dùng:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
ct_lieudung = ttk.Entry(right_ct, width=30)
ct_lieudung.grid(row=1, column=1, pady=5)

# ===== KHUNG BẢNG =====
frame_table_ct = tk.LabelFrame(
    tab_cttoathuoc,
    text="DANH SÁCH CHI TIẾT TOA THUỐC",
    bg="#EBF5FB",
    fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=10,
    pady=10
)
frame_table_ct.pack(fill="both", expand=True, padx=20, pady=10)

columns_ct = ("MaPK", "MaThuoc", "SoLuong", "LieuDung")

tree_cttt = ttk.Treeview(frame_table_ct, columns=columns_ct, show="headings", height=12)

# ===== TÊN CỘT =====
tree_cttt.heading("MaPK", text="Mã PK")
tree_cttt.heading("MaThuoc", text="Mã Thuốc")
tree_cttt.heading("SoLuong", text="Số Lượng")
tree_cttt.heading("LieuDung", text="Liều Dùng")

# ===== ĐỘ RỘNG =====
tree_cttt.column("MaPK", width=120)
tree_cttt.column("MaThuoc", width=140)
tree_cttt.column("SoLuong", width=120)
tree_cttt.column("LieuDung", width=200)

tree_cttt.pack(fill="both", expand=True)
load_cttoathuoc()
root.mainloop()