import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# ====== Kết nối MySQL ====== 
def connect_db(): 
    return mysql.connector.connect( 
        host="localhost", 
        user="QLBenhNhan",        # thay bằng user MySQL của bạn 
        password="Quanlybenhnhan12345",        # thay bằng password MySQL của bạn 
        database="QLBN" 
    )

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

# TAB THUỐC
# Frame nhập liệu
frame_input_thuoc = ttk.LabelFrame(tab_thuoc, text="Thông tin thuốc", padding=10)
frame_input_thuoc.pack(fill="x", pady=10)

ttk.Label(frame_input_thuoc, text="Mã thuốc:").grid(row=0, column=0, pady=5)
ttk.Label(frame_input_thuoc, text="Tên thuốc:").grid(row=1, column=0, pady=5)
ttk.Label(frame_input_thuoc, text="Đơn giá:").grid(row=2, column=0, pady=5)

entry_ma_thuoc = ttk.Entry(frame_input_thuoc)
entry_ten_thuoc = ttk.Entry(frame_input_thuoc)
entry_gia_thuoc = ttk.Entry(frame_input_thuoc)

entry_ma_thuoc.grid(row=0, column=1, pady=5)
entry_ten_thuoc.grid(row=1, column=1, pady=5)
entry_gia_thuoc.grid(row=2, column=1, pady=5)

# Bảng
frame_table_thuoc = ttk.LabelFrame(tab_thuoc, text="Danh sách thuốc", padding=10)
frame_table_thuoc.pack(fill="both", expand=True)

tree_thuoc = ttk.Treeview(frame_table_thuoc, 
    columns=("mathuoc", "tenthuoc", "gia"), show="headings")
tree_thuoc.heading("mathuoc", text="Mã thuốc")
tree_thuoc.heading("tenthuoc", text="Tên thuốc")
tree_thuoc.heading("gia", text="Đơn giá")

tree_thuoc.pack(fill="both", expand=True)

# TAB PHÒNG BỆNH
frame_input_phong = ttk.LabelFrame(tab_phong, text="Thông tin phòng bệnh", padding=10)
frame_input_phong.pack(fill="x", pady=10)

ttk.Label(frame_input_phong, text="Mã phòng:").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(frame_input_phong, text="Tên phòng:").grid(row=1, column=0, padx=5, pady=5)
ttk.Label(frame_input_phong, text="Loại phòng:").grid(row=2, column=0, padx=5, pady=5)

entry_ma_phong = ttk.Entry(frame_input_phong, width=25)
entry_ten_phong = ttk.Entry(frame_input_phong, width=25)
combo_loai_phong = ttk.Combobox(frame_input_phong, values=["Nội trú", "Ngoại trú"], width=22, state="readonly")

entry_ma_phong.grid(row=0, column=1, pady=5)
entry_ten_phong.grid(row=1, column=1, pady=5)
combo_loai_phong.grid(row=2, column=1, pady=5)

# Bảng
frame_table_phong = ttk.LabelFrame(tab_phong, text="Danh sách phòng bệnh", padding=10)
frame_table_phong.pack(fill="both", expand=True)

columns_phong = ("MaPhong", "TenPhong", "LoaiPhong")
tree_phong = ttk.Treeview(frame_table_phong, columns=columns_phong, show="headings")

for col in columns_phong:
    tree_phong.heading(col, text=col)
    tree_phong.column(col, width=150)

tree_phong.pack(fill="both", expand=True)

# TAB PHIẾU KHÁM
frame_input_pk = ttk.LabelFrame(tab_phieukham, text="Thông tin phiếu khám", padding=10)
frame_input_pk.pack(fill="x", pady=10)

ttk.Label(frame_input_pk, text="Mã PK:").grid(row=0, column=0, pady=5)
ttk.Label(frame_input_pk, text="Mã BN:").grid(row=0, column=2, pady=5)
ttk.Label(frame_input_pk, text="Mã BS:").grid(row=1, column=0, pady=5)
ttk.Label(frame_input_pk, text="Ngày khám:").grid(row=1, column=2, pady=5)
ttk.Label(frame_input_pk, text="Loại khám:").grid(row=2, column=0, pady=5)
ttk.Label(frame_input_pk, text="Chẩn đoán:").grid(row=2, column=2, pady=5)

entry_ma_pk = ttk.Entry(frame_input_pk, width=20)
entry_ma_bn = ttk.Entry(frame_input_pk, width=20)
entry_ma_bs = ttk.Entry(frame_input_pk, width=20)
entry_ngaykham = DateEntry(frame_input_pk, width=18, date_pattern="yyyy-mm-dd")
entry_loaikham = ttk.Entry(frame_input_pk, width=20)
entry_chandoan = ttk.Entry(frame_input_pk, width=20)

entry_ma_pk.grid(row=0, column=1, pady=5)
entry_ma_bn.grid(row=0, column=3, pady=5)
entry_ma_bs.grid(row=1, column=1, pady=5)
entry_ngaykham.grid(row=1, column=3, pady=5)
entry_loaikham.grid(row=2, column=1, pady=5)
entry_chandoan.grid(row=2, column=3, pady=5)

# Bảng
frame_table_pk = ttk.LabelFrame(tab_phieukham, text="Danh sách phiếu khám", padding=10)
frame_table_pk.pack(fill="both", expand=True)

columns_pk = ("MaPK", "MaBN", "MaBS", "NgayKham", "LoaiKham", "ChanDoan")
tree_pk = ttk.Treeview(frame_table_pk, columns=columns_pk, show="headings")

for col in columns_pk:
    tree_pk.heading(col, text=col)
    tree_pk.column(col, width=120)

tree_pk.pack(fill="both", expand=True)

# TAB TOA THUỐC
frame_input_toa = ttk.LabelFrame(tab_toathuoc, text="Chi tiết toa thuốc", padding=10)
frame_input_toa.pack(fill="x", pady=10)

ttk.Label(frame_input_toa, text="Mã PK:").grid(row=0, column=0, pady=5)
ttk.Label(frame_input_toa, text="Mã thuốc:").grid(row=0, column=2, pady=5)
ttk.Label(frame_input_toa, text="Số lượng:").grid(row=1, column=0, pady=5)
ttk.Label(frame_input_toa, text="Liều dùng:").grid(row=1, column=2, pady=5)

entry_ma_pk_toa = ttk.Entry(frame_input_toa, width=20)
entry_ma_thuoc_toa = ttk.Entry(frame_input_toa, width=20)
entry_soluong_toa = ttk.Entry(frame_input_toa, width=20)
entry_lieudung_toa = ttk.Entry(frame_input_toa, width=20)

entry_ma_pk_toa.grid(row=0, column=1, pady=5)
entry_ma_thuoc_toa.grid(row=0, column=3, pady=5)
entry_soluong_toa.grid(row=1, column=1, pady=5)
entry_lieudung_toa.grid(row=1, column=3, pady=5)

# Bảng
frame_table_toa = ttk.LabelFrame(tab_toathuoc, text="Danh sách chi tiết toa thuốc", padding=10)
frame_table_toa.pack(fill="both", expand=True)

columns_toa = ("MaPK", "MaThuoc", "SoLuong", "LieuDung")
tree_toa = ttk.Treeview(frame_table_toa, columns=columns_toa, show="headings")

for col in columns_toa:
    tree_toa.heading(col, text=col)
    tree_toa.column(col, width=120)

tree_toa.pack(fill="both", expand=True)

root.mainloop()
