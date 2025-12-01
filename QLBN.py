import tkinter as tk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
import mysql.connector
import traceback

# ====== Kết nối MySQL ====== 
import mysql.connector

def connect_db(): 
    return mysql.connector.connect( 
        host="localhost", 
        user="root",        # thay bằng user MySQL của bạn 
        password="benhnhan12345",        # thay bằng password MySQL của bạn 
        database="QLBN" 
    )
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

# ============= NOTEBOOK =============
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=20, pady=10)

tab_bn = ttk.Frame(notebook)
notebook.add(tab_bn, text="Bệnh Nhân")
tab_pb = ttk.Frame(notebook)
notebook.add(tab_pb,text="Phòng Bệnh")
tab_phieukham = ttk.Frame(notebook)
notebook.add(tab_phieukham,text="Phiếu Khám")
tab_thuoc = ttk.Frame(notebook)
notebook.add(tab_thuoc,text="Thuốc")
tab_cttoathuoc = ttk.Frame(notebook)
notebook.add(tab_cttoathuoc,text="Chi tiết toa thuốc")

# ===== FRAME THÔNG TIN CỦA BỆNH NHÂN =====
frame_info = tk.LabelFrame(tab_bn, text="THÔNG TIN BỆNH NHÂN",
                           bg="#EBF5FB", fg="#1B4F72",
                           font=("Arial", 14, "bold"),
                           padx=15, pady=15)
frame_info.pack(fill="x", padx=20)

# Cột trái
left_col = tk.Frame(frame_info, bg="#EBF5FB")
left_col.grid(row=0, column=0, padx=20)

tk.Label(left_col, text="Mã số:", bg="#EBF5FB").pack(anchor="w")
entry_mabn = ttk.Entry(left_col, width=30)
entry_mabn.pack(anchor="w", pady=5)

tk.Label(left_col, text="Họ lót:", bg="#EBF5FB").pack(anchor="w")
entry_holot_bn = ttk.Entry(left_col, width=30)
entry_holot_bn.pack(anchor="w", pady=5)

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
entry_ten_bn = ttk.Entry(right_col, width=30)
entry_ten_bn.pack(anchor="w", pady=5)

tk.Label(right_col, text="Ngày sinh:", bg="#EBF5FB").pack(anchor="w")
entry_ngaysinh = DateEntry(right_col, width=27, date_pattern="yyyy-mm-dd")
entry_ngaysinh.pack(anchor="w", pady=5)

tk.Label(right_col, text="Địa Chỉ:", bg="#EBF5FB").pack(anchor="w")
entry_diachi_bn = ttk.Entry(right_col, width=30)
entry_diachi_bn.pack(anchor="w", pady=0,padx=5)

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

columns = ("MaBN", "HoLot", "Ten", "Phai", "NgaySinh","DiaChi","LoaiBenhNhan","MaPhong")
tree_bn = ttk.Treeview(frame_table, columns=columns, show="headings", height=12)

tree_bn.heading("MaBN", text="Mã BN")
tree_bn.heading("HoLot", text="Họ Lót")
tree_bn.heading("Ten", text="Tên")
tree_bn.heading("Phai", text="Phái")
tree_bn.heading("NgaySinh", text="Ngày Sinh")
tree_bn.heading("DiaChi",text="Địa Chỉ")
tree_bn.heading("LoaiBenhNhan", text="Loại Bệnh Nhân")
tree_bn.heading("MaPhong",text="Mã Phòng")


tree_bn.column("MaBN", width=100, anchor="center")
tree_bn.column("HoLot", width=150, anchor="center")
tree_bn.column("Ten", width=100, anchor="center")
tree_bn.column("Phai", width=80, anchor="center")
tree_bn.column("NgaySinh", width=120, anchor="center")
tree_bn.column("DiaChi",width=120)
tree_bn.column("LoaiBenhNhan", width=100, anchor="center")
tree_bn.column("MaPhong",width=80,anchor="center")

tree_bn.pack(fill="both", expand=True)
#Chức năng CRUD
def clear_benhnhan():
    entry_mabn.delete(0, tk.END)
    entry_holot_bn.delete(0, tk.END)
    entry_ten_bn.delete(0, tk.END)
    entry_ngaysinh.set_date("2000-01-01")
    gender_var.set("Nam")
    entry_diachi_bn.delete(0, tk.END)
    type_var.set("NoiTru")
    entry_map.configure(state="normal")
    entry_map.delete(0, tk.END)
   
def load_benhnhan():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MaBN, HoLot, Ten, Phai, NgaySinh, DiaChi, LoaiBenhNhan, MaPhong FROM BenhNhan")
    rows = cursor.fetchall()

    # Xóa dữ liệu cũ trong TreeView
    for item in tree_bn.get_children():
        tree_bn.delete(item)

    # Đổ dữ liệu mới lên TreeView
    for row in rows:
        tree_bn.insert("", "end", values=row)

    cursor.close()
    conn.close()

def add_benhnhan():
    MaBN = entry_mabn.get()
    HoLot = entry_holot_bn.get()
    Ten = entry_ten_bn.get()
    NgaySinh = entry_ngaysinh.get()
    Phai = gender_var.get()
    DiaChi = entry_diachi_bn.get()
    LoaiBN = type_var.get()
    MaPhong = entry_map.get() if LoaiBN == "NoiTru" else None

    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """
            INSERT INTO BenhNhan (MaBN, HoLot, Ten, NgaySinh, Phai, DiaChi, LoaiBenhNhan, MaPhong)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (MaBN, HoLot, Ten, NgaySinh, Phai, DiaChi, LoaiBN, MaPhong))
        conn.commit()

        messagebox.showinfo("Thành công", "Đã thêm bệnh nhân!")
    except mysql.connector.Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi thêm: {e}")
    finally:
        conn.close()
        load_benhnhan()

def search_benhnhan():
    MaBN = entry_mabn.get()

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM BenhNhan WHERE MaBN = %s", (MaBN,))
        result = cursor.fetchone()

        if result:
            entry_holot_bn.delete(0, tk.END)
            entry_ten_bn.delete(0, tk.END)
            entry_ngaysinh.set_date(result[3])
            entry_diachi_bn.delete(0, tk.END)
            entry_map.delete(0, tk.END)

            entry_holot_bn.insert(0, result[1])
            entry_ten_bn.insert(0, result[2])
            gender_var.set(result[4])
            entry_diachi_bn.insert(0, result[5])
            type_var.set(result[6])

            if result[6] == "NoiTru":
                entry_map.insert(0, result[7])

            messagebox.showinfo("Kết quả", "Đã tìm thấy bệnh nhân!")
        else:
            messagebox.showwarning("Không tìm thấy", "Không có bệnh nhân này!")
    except mysql.connector.Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi tìm kiếm: {e}")
    finally:
        conn.close()

def update_benhnhan():
    MaBN = entry_mabn.get()
    HoLot = entry_holot_bn.get()
    Ten = entry_ten_bn.get()
    NgaySinh = entry_ngaysinh.get()
    Phai = gender_var.get()
    DiaChi = entry_diachi_bn.get()
    LoaiBN = type_var.get()
    MaPhong = entry_map.get() if LoaiBN == "NoiTru" else None

    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """
            UPDATE BenhNhan SET 
                HoLot=%s, Ten=%s, NgaySinh=%s, Phai=%s, DiaChi=%s,
                LoaiBenhNhan=%s, MaPhong=%s
            WHERE MaBN=%s
        """

        cursor.execute(sql, (HoLot, Ten, NgaySinh, Phai, DiaChi, LoaiBN, MaPhong,MaBN))
        conn.commit()

        messagebox.showinfo("Thành công", "Đã cập nhật thông tin!")
    except mysql.connector.Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi cập nhật: {e}")
    finally:
        conn.close()
        load_benhnhan()

def sua_benhnhan():
    selected = tree_bn.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Hãy chọn bệnh nhân cần sửa")
        return

    values = tree_bn.item(selected)["values"]

    mabn     = values[0]
    holot    = values[1]
    ten      = values[2]
    phai     = values[3]
    ngaysinh = values[4]
    diachi   = values[5]
    loai     = values[6]
    maphong  = values[7]

    entry_mabn.delete(0, tk.END)
    entry_mabn.insert(0, mabn)

    entry_holot_bn.delete(0, tk.END)
    entry_holot_bn.insert(0, holot)

    entry_ten_bn.delete(0, tk.END)
    entry_ten_bn.insert(0, ten)

    entry_ngaysinh.set_date(ngaysinh)

    gender_var.set(phai)

    entry_diachi_bn.delete(0, tk.END)
    entry_diachi_bn.insert(0, diachi)

    type_var.set(loai)

    if loai == "NoiTru":
        entry_map.configure(state="normal")
        entry_map.delete(0, tk.END)
        entry_map.insert(0, maphong)
    else:
        entry_map.configure(state="disabled")
        entry_map.delete(0, tk.END)

# ===== KHUNG NÚT CHỨC NĂNG CỦA TAB BỆNH NHÂN =====
frame_buttons_bn = tk.Frame(tab_bn)
frame_buttons_bn.pack(fill="x", pady=5, before=frame_table)

tk.Button(frame_buttons_bn, text="Thêm", width=12, bg="#A9DFBF",command=add_benhnhan).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons_bn, text="Sửa", width=12, bg="#F9E79F",command=sua_benhnhan).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons_bn, text="Cập nhật", width=12, bg="#F5B7B1",command=update_benhnhan).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons_bn, text="Tìm kiếm", width=12, bg="#D7BDE2",command=search_benhnhan).grid(row=0, column=3, padx=5)
tk.Button(frame_buttons_bn, text="Làm mới", width=12, bg="#D6EAF8",command=clear_benhnhan).grid(row=0, column=4, padx=5)
load_benhnhan()
#Tab phòng bệnh
#Frame thông tin
frame_info = tk.LabelFrame(
    tab_pb, text="THÔNG TIN PHÒNG BỆNH",
    bg="#EBF5FB", fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=15, pady=15
)
frame_info.pack(fill="x", pady=5)

# Tạo 2 cột
left_col = tk.Frame(frame_info, bg="#EBF5FB")
left_col.grid(row=0, column=0, padx=10, pady=5, sticky="nw")

right_col = tk.Frame(frame_info, bg="#EBF5FB")
right_col.grid(row=0, column=1, padx=10, pady=5, sticky="nw")

# ====== CỘT TRÁI ======
tk.Label(left_col, text="Mã Phòng:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
entry_map = ttk.Entry(left_col, width=30)
entry_map.grid(row=0, column=1, pady=5)

tk.Label(left_col, text="Tên phòng:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
entry_tenphong = ttk.Entry(left_col, width=30)
entry_tenphong.grid(row=1, column=1, pady=5)

tk.Label(left_col, text="Số lượng :", bg="#EBF5FB").grid(row=2, column=0, sticky="w")
entry_soluong = ttk.Entry(left_col, width=30)
entry_soluong.grid(row=2, column=1, pady=5)

tk.Label(left_col, text="Loại phòng:", bg="#EBF5FB").grid(row=3, column=0, sticky="w")
combo_loaiphong = ttk.Combobox(
    left_col,
    values=[
        "Thường",
        "Hồi sức tích cực",
        "Mổ",
        "VIP",
        "Cấp cứu",
    ],
    state="readonly",
    width=20
)
combo_loaiphong.grid(row=3, column=1, pady=5)
combo_loaiphong.current(0)

# ====== CỘT PHẢI ======
tk.Label(right_col, text="Ghi chú:", bg="#EBF5FB").grid(row=0, column=0, sticky="w")
entry_ghichu = ttk.Entry(right_col, width=40)
entry_ghichu.grid(row=1, column=0, pady=5, sticky="w")

# --- KHUNG BẢNG DƯỚI ---
frame_table = tk.LabelFrame(
    tab_pb, text="Danh sách phòng bệnh",
    bg="#EBF5FB", fg="#1B4F72",
    font=("Arial", 14, "bold"),
    padx=10, pady=10
)
frame_table.pack(fill="both", expand=True)

columns_phongbenh = ("Mã Phòng", "Tên Phòng", "Loại Phòng","Số Lượng","Ghi Chú")
tree_pb = ttk.Treeview(frame_table, columns=columns_phongbenh, show="headings", height=10)
tree_pb.pack(fill="both", expand=True,anchor="center")

#Chức năng CRUD cho phong bệnh
for col in columns_phongbenh:
    tree_pb.heading(col, text=col)
    tree_pb.column(col, width=150)

def clear_pb():
    entry_map.delete(0, tk.END)
    entry_tenphong.delete(0, tk.END)
    entry_soluong.delete(0, tk.END)
    combo_loaiphong.current(0)
    entry_ghichu.delete(0, tk.END)

def load_phongbenh():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MaPhong, TenPhong, LoaiPhong, SoGiuong, GhiChu FROM Phong")
    rows = cursor.fetchall()

    tree_pb.delete(*tree_pb.get_children())

    for row in rows:
        tree_pb.insert("", "end", values=row)

    conn.close()

def them_phongbenh():
    try:
        MaPhong = entry_map.get()
        TenPhong = entry_tenphong.get()
        SoLuong = entry_soluong.get()
        LoaiPhong = combo_loaiphong.get()
        GhiChu = entry_ghichu.get()

        conn = mysql.connect(...)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Phong (MaPhong, TenPhong, SoLuong, LoaiPhong, GhiChu)
            VALUES (%s, %s, %s, %s, %s)
        """, (MaPhong, TenPhong, SoLuong, LoaiPhong, GhiChu))

        conn.commit()
        messagebox.showinfo("Thành công", "Đã thêm phòng!")

        load_phongbenh()   # load lại bảng
    except Exception as e:
        messagebox.showerror("Lỗi thêm", str(e))

def sua_phongbenh():
    selected = tree_pb.selection() 
    if not selected: 
        messagebox.showwarning("Chưa chọn", "Hãy chọn phòng bệnh để sửa") 
        return 
    values = tree_pb.item(selected)["values"] 
    entry_map.delete(0, tk.END) 
    entry_map.insert(0, values[0]) 
    entry_tenphong.delete(0, tk.END) 
    entry_tenphong.insert(0, values[1]) 
    entry_soluong.delete(0, tk.END) 
    entry_soluong.insert(0, values[2]) 
    combo_loaiphong.set(values[3]) 
    entry_ghichu.delete(0, tk.END)
    entry_ghichu.insert(0, values[4])

def luu_phongbenh():
    map = entry_map.get().strip()
    tenphong = entry_tenphong.get().strip()
    soluong = entry_soluong.get().strip()
    loaiphong = combo_loaiphong.get().strip()
    ghichu = entry_ghichu.get().strip()

    if map == "":
        messagebox.showwarning("Thiếu dữ liệu", "Không tìm thấy mã phòng cần cập nhật")
        return

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
    UPDATE Phong
    SET MaPhong=%s, TenPhong=%s, SoLuong=%s, GhiChu=%s
    WHERE MaBS=%s
""", (tenphong, soluong, loaiphong, ghichu, map))

    conn.commit()
    conn.close()

    load_phongbenh()
  
    messagebox.showinfo("Thành công", "Đã cập nhật thông tin phòng bệnh")
frame_buttons = tk.Frame(tab_pb)
frame_buttons.pack(fill="x",pady=5,before=tree_pb)

tk.Button(frame_buttons, text="Thêm", width=12, bg="#A9DFBF", command=them_phongbenh).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Sửa", width=12, bg="#F9E79F", command=sua_phongbenh).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Lưu", width=12, bg="#F5B7B1", command=luu_phongbenh).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Làm mới", width=12, bg="#D6EAF8", command=clear_pb).grid(row=0, column=3, padx=5)
load_phongbenh()
# TAB PHIẾU KHÁM
frame_info_pk = tk.LabelFrame(tab_phieukham, text="THÔNG TIN BỆNH NHÂN",
                           bg="#EBF5FB", fg="#1B4F72",
                           font=("Arial", 14, "bold"),
                           padx=15, pady=15)
frame_info_pk.pack(fill="x", padx=20)

# Các ô nhập liệu
style.configure("TLabel",
                font=("Segoe UI", 9),     # ↓ nhỏ hơn
                background="#E8F4FC")

ttk.Label(frame_info_pk, text="Mã PK:").grid(row=0, column=0, padx=5, pady=5)
entry_maphieu = ttk.Entry(frame_info_pk, style="TEntry")
entry_maphieu.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_info_pk, text="Mã BN:").grid(row=0, column=2, padx=5, pady=5)
entry_mabn_pk = ttk.Entry(frame_info_pk, style="TEntry")
entry_mabn_pk.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(frame_info_pk, text="Mã BS:").grid(row=1, column=0, padx=5, pady=5)
entry_mabs_pk = ttk.Entry(frame_info_pk, style="TEntry")
entry_mabs_pk.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_info_pk, text="Ngày khám:").grid(row=1, column=2, padx=5, pady=5)
entry_ngaykham = ttk.Entry(frame_info_pk, style="TEntry")
entry_ngaykham.grid(row=1, column=3, padx=5, pady=5)

ttk.Label(frame_info_pk, text="Loại khám:").grid(row=2, column=0, padx=5, pady=5)
entry_loaikham = ttk.Entry(frame_info_pk, style="TEntry")
entry_loaikham.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_info_pk, text="Chẩn đoán:").grid(row=2, column=2, padx=5, pady=5)
entry_chandoan = ttk.Entry(frame_info_pk, style="TEntry")
entry_chandoan.grid(row=2, column=3, padx=5, pady=5)

ttk.Label(frame_info_pk, text="Ghi chú:").grid(row=3, column=0, padx=5, pady=5)
entry_ghichu = ttk.Entry(frame_info_pk, width=50, style="TEntry")
entry_ghichu.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

# ===== Bảng =====
frame_tree_pk = ttk.Frame(tab_phieukham)
frame_tree_pk.pack(fill="both", expand=True, padx=10, pady=5)

columns = ("MaPK","MaBN","MaBS","NgayKham","LoaiKham","ChanDoan","GhiChu")
tree_pk = ttk.Treeview(frame_tree_pk, columns=columns, show="headings")

for col in columns:
    tree_pk.heading(col, text=col)
    tree_pk.column(col, width=120)

tree_pk.pack(fill="both", expand=True)

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

def clear_phieukham():
    entry_maphieu.delete(0, tk.END)
    entry_mabn_pk.delete(0, tk.END)
    entry_mabs_pk.delete(0, tk.END)
    entry_ngaykham.delete(0, tk.END)
    entry_loaikham.delete(0, tk.END)
    entry_chandoan.delete(0, tk.END)
    entry_ghichu.delete(0, tk.END)

def load_phieukham():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MaPK, MaBN, MaBS, NgayKham, LoaiKham, ChanDoan, GhiChu FROM PhieuKham")
    rows = cursor.fetchall()

    tree_pk.delete(*tree_pk.get_children())

    for row in rows:
        tree_pk.insert("", "end", values=row)

def them_phieukham():
    MaPK = entry_maphieu.get()
    MaBN = entry_mabn_pk.get()
    MaBS = entry_mabs_pk.get()
    NgayKham = entry_ngaykham.get()
    LoaiKham = entry_loaikham.get()
    ChanDoan = entry_chandoan.get()
    GhiChu = entry_ghichu.get()

    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """
        INSERT INTO PhieuKham (MaPK, MaBN, MaBS, NgayKham, LoaiKham, ChanDoan, GhiChu)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(sql, (MaPK, MaBN, MaBS, NgayKham, LoaiKham, ChanDoan, GhiChu))
        conn.commit()

        messagebox.showinfo("Thành công", "Đã thêm phiếu khám!")

    except mysql.connector.Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi thêm: {e}")
    finally:
        conn.close()
        load_phieukham()

def sua_phieukham():
    selected = tree_pk.focus()
    if not selected:
        messagebox.showwarning("Chú ý", "Hãy chọn phiếu khám để sửa!")
        return

    values = tree_pk.item(selected, "values")

    entry_maphieu.delete(0, tk.END)
    entry_mabn_pk.delete(0, tk.END)
    entry_mabs_pk.delete(0, tk.END)
    entry_ngaykham.delete(0, tk.END)
    entry_loaikham.delete(0, tk.END)
    entry_chandoan.delete(0, tk.END)
    entry_ghichu.delete(0, tk.END)

    entry_maphieu.insert(0, values[0])
    entry_mabn_pk.insert(0, values[1])
    entry_mabs_pk.insert(0, values[2])
    entry_ngaykham.insert(0, values[3])
    entry_loaikham.insert(0, values[4])
    entry_chandoan.insert(0, values[5])
    entry_ghichu.insert(0, values[6])

def luu_phieukham():
    MaPK = entry_maphieu.get()
    MaBN = entry_mabn_pk.get()
    MaBS = entry_mabs_pk.get()
    NgayKham = entry_ngaykham.get()
    LoaiKham = entry_loaikham.get()
    ChanDoan = entry_chandoan.get()
    GhiChu = entry_ghichu.get()

    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """
        UPDATE PhieuKham SET
            MaBN=%s, MaBS=%s, NgayKham=%s, LoaiKham=%s, ChanDoan=%s, GhiChu=%s
        WHERE MaPK=%s
        """

        cursor.execute(sql, (MaBN, MaBS, NgayKham, LoaiKham, ChanDoan, GhiChu, MaPK))
        conn.commit()

        messagebox.showinfo("Thành công", "Đã cập nhật!")

    except mysql.connector.Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi lưu: {e}")
    finally:
        conn.close()
        load_phieukham()

def xoa_phieukham():
    selected = tree_pk.focus()
    if not selected:
        messagebox.showwarning("Chú ý", "Hãy chọn phiếu khám cần xóa!")
        return

    MaPK = tree_pk.item(selected, "values")[0]

    if not messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa phiếu {MaPK}?"):
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM PhieuKham WHERE MaPK=%s", (MaPK,))
        conn.commit()

        messagebox.showinfo("Thành công", "Đã xóa phiếu khám!")

    except mysql.connector.Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi xóa: {e}")

    finally:
        conn.close()
        load_phieukham()
#CRUD CHO PHIẾU KHÁM
frame_buttons = tk.Frame(tab_phieukham)
frame_buttons.pack(fill="x",pady=5,before=tree_pk)
load_phieukham()
tk.Button(frame_buttons, text="Thêm", width=12, bg="#A9DFBF", command=them_phieukham).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Sửa", width=12, bg="#F9E79F", command=sua_phieukham).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Lưu", width=12, bg="#F5B7B1", command=luu_phieukham).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Làm mới", width=12, bg="#D6EAF8", command=clear_phieukham).grid(row=0, column=3, padx=5)
tk.Button(frame_buttons, text="Xóa", width=12, bg="#E2122B", command=xoa_phieukham).grid(row=0, column=4, padx=5)

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

tk.Label(right_t, text="Công dụng:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
t_congdung = ttk.Entry(right_t, width=30)
t_congdung.grid(row=1, column=1, pady=5)

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

columns_t = ("MaThuoc", "TenThuoc", "DonVi", "Gia","CongDung")

tree_thuoc = ttk.Treeview(frame_table_t, columns=columns_t, show="headings", height=12)

# ===== ĐẶT TÊN CỘT =====
tree_thuoc.heading("MaThuoc", text="Mã Thuốc")
tree_thuoc.heading("TenThuoc", text="Tên Thuốc")
tree_thuoc.heading("DonVi", text="Đơn Vị")
tree_thuoc.heading("Gia", text="Giá (VNĐ)")
tree_thuoc.heading("CongDung", text="Công Dụng")

# ===== ĐỘ RỘNG =====
tree_thuoc.column("MaThuoc", width=120)
tree_thuoc.column("TenThuoc", width=200)
tree_thuoc.column("DonVi", width=120)
tree_thuoc.column("Gia", width=120)
tree_thuoc.column("CongDung", width=120)

tree_thuoc.pack(fill="both", expand=True)
def clear_thuoc():
    t_mathuoc.delete(0, tk.END)
    t_tenthuoc.delete(0, tk.END)
    t_donvi.delete(0, tk.END)
    t_gia.delete(0, tk.END)
    t_congdung.delete(0, tk.END)

#Load dữ liệu thuốc
def load_thuoc():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MaThuoc, TenThuoc, DonViThuoc, DonGia, CongDung FROM Thuoc")
    rows = cursor.fetchall()

    tree_thuoc.delete(*tree_thuoc.get_children())

    for row in rows:
        tree_thuoc.insert("", "end", values=row)
def add_thuoc():
    MaThuoc = t_mathuoc.get()
    TenThuoc = t_tenthuoc.get()
    DonVi = t_donvi.get()
    DonGia = t_gia.get()
    CongDung = t_congdung.get()

    # --- KIỂM TRA RỖNG ---
    if DonGia.strip() == "":
        messagebox.showwarning("Thiếu dữ liệu", "Đơn giá không được để trống!")
        return

    # --- KIỂM TRA ĐƠN GIÁ CÓ PHẢI SỐ ---
    try:
        DonGia = float(DonGia)
    except:
        messagebox.showerror("Lỗi", "Đơn giá phải là một số hợp lệ!")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """
            INSERT INTO Thuoc (MaThuoc, TenThuoc, DonViThuoc, DonGia, CongDung)
            VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (MaThuoc, TenThuoc, DonVi, DonGia, CongDung))
        conn.commit()

        messagebox.showinfo("Thành công", "Đã thêm thuốc!")
    except mysql.connector.Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi thêm thuốc: {e}")
    finally:
        conn.close()
        load_thuoc()

def search_thuoc():
    MaThuoc = t_mathuoc.get()

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Thuoc WHERE MaThuoc = %s", (MaThuoc,))
        result = cursor.fetchone()

        if result:
            t_tenthuoc.delete(0, tk.END)
            t_donvi.delete(0, tk.END)
            t_gia.delete(0, tk.END)
            t_congdung.delete(0, tk.END)

            t_tenthuoc.insert(0, result[1])
            t_donvi.insert(0, result[2])
            t_gia.insert(0, result[3])
            t_congdung.insert(0, result[4])

            messagebox.showinfo("Kết quả", "Đã tìm thấy thuốc!")
        else:
            messagebox.showwarning("Không tìm thấy", "Không có thuốc này trong hệ thống!")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tìm thuốc!\n{e}")

    finally:
        try:
            conn.close()
        except:
            pass

def update_thuoc():
    MaThuoc = t_mathuoc.get()
    TenThuoc = t_tenthuoc.get()
    DonVi = t_donvi.get()
    DonGia = t_gia.get()
    CongDung = t_congdung.get()

    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """
            UPDATE Thuoc SET 
                TenThuoc=%s, DonViThuoc=%s, DonGia=%s, CongDung=%s
            WHERE MaThuoc=%s
        """

        cursor.execute(sql, (TenThuoc, DonVi, DonGia, CongDung, MaThuoc))
        conn.commit()

        messagebox.showinfo("Thành công", "Đã cập nhật thuốc!")
    except mysql.connector.Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi cập nhật: {e}")
    finally:
        conn.close()
        load_thuoc()

def sua_thuoc():
    selected = tree_thuoc.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Hãy chọn thuốc cần sửa!")
        return

    values = tree_thuoc.item(selected)["values"]

    math = values[0]
    tenthuoc = values[1]
    donvi = values[2]
    dongia = values[3]
    congdung = values[4]

    t_mathuoc.delete(0, tk.END)
    t_mathuoc.insert(0, math)

    t_tenthuoc.delete(0, tk.END)
    t_tenthuoc.insert(0, tenthuoc)

    t_donvi.delete(0, tk.END)
    t_donvi.insert(0, donvi)

    t_gia.delete(0, tk.END)
    t_gia.insert(0, dongia)

    t_congdung.delete(0, tk.END)
    t_congdung.insert(0, congdung)
frame_buttons_thuoc = tk.Frame(tab_thuoc)
frame_buttons_thuoc.pack(fill="x", pady=5,before=tree_thuoc)

tk.Button(frame_buttons_thuoc, text="Thêm", width=12, bg="#A9DFBF", command=add_thuoc).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons_thuoc, text="Sửa", width=12, bg="#F9E79F", command=sua_thuoc).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons_thuoc, text="Cập nhật", width=12, bg="#F5B7B1", command=update_thuoc).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons_thuoc, text="Tìm kiếm", width=12, bg="#D7BDE2", command=search_thuoc).grid(row=0, column=3, padx=5)
tk.Button(frame_buttons_thuoc, text="Làm mới", width=12, bg="#D6EAF8", command=clear_thuoc).grid(row=0, column=4, padx=5)

load_thuoc()
#Tab chi tiết toa thuốc
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
ct_mapk_cttt = ttk.Entry(left_ct,width=27)
ct_mapk_cttt.grid(row=0, column=1, pady=5)

tk.Label(left_ct, text="Mã Thuốc:", bg="#EBF5FB").grid(row=1, column=0, sticky="w")
ct_mathuoc_cttt = ttk.Entry(left_ct,width=27)
ct_mathuoc_cttt.grid(row=1, column=1, pady=5)

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
tree_cttt.column("MaThuoc", width=140,anchor="center")
tree_cttt.column("SoLuong", width=120,anchor="center")
tree_cttt.column("LieuDung", width=200,anchor="center")

tree_cttt.pack(fill="both", expand=True)

def clear_cttt():
    ct_mapk_cttt.delete(0, tk.END)
    ct_mathuoc_cttt.delete(0, tk.END)
    ct_soluong.delete(0, tk.END)
    ct_lieudung.delete(0, tk.END)

#Load dữ liệu toa thuốc
def load_cttoathuoc():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MaPK, MaThuoc, SoLuong, LieuDung FROM ChiTietToaThuoc")
    rows = cursor.fetchall()

    tree_cttt.delete(*tree_cttt.get_children())

    for row in rows:
        tree_cttt.insert("", "end", values=row)

def add_cttt():
    MaPK = ct_mapk_cttt.get()
    MaThuoc = ct_mathuoc_cttt.get()
    SoLuong = ct_soluong.get()
    LieuDung = ct_lieudung.get()

    if not (MaPK and MaThuoc and SoLuong and LieuDung):
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập đầy đủ thông tin!")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """
        INSERT INTO ChiTietToaThuoc (MaPK, MaThuoc, SoLuong, LieuDung)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (MaPK, MaThuoc, SoLuong, LieuDung))

        conn.commit()
        messagebox.showinfo("Thành công", "Đã thêm chi tiết toa thuốc!")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi thêm dữ liệu:\n{e}")

    finally:
        cursor.close()
        conn.close()
def search_cttt():
    MaPK = ct_mapk_cttt.get()
    MaThuoc = ct_mathuoc_cttt.get()

    if not (MaPK and MaThuoc):
        messagebox.showwarning("Thiếu dữ liệu", "Nhập Mã PK và Mã Thuốc để tìm!")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = "SELECT * FROM ChiTietToaThuoc WHERE MaPK = %s AND MaThuoc = %s"
        cursor.execute(sql, (MaPK, MaThuoc))

        result = cursor.fetchone()

        if result:
            ct_soluong.delete(0, tk.END)
            ct_lieudung.delete(0, tk.END)

            ct_soluong.insert(0, result[2])
            ct_lieudung.insert(0, result[3])

            messagebox.showinfo("Kết quả", "Đã tìm thấy!")
        else:
            messagebox.showwarning("Không tìm thấy", "Không có chi tiết toa thuốc này!")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi tìm:\n{e}")

    finally:
        cursor.close()
        conn.close()
def update_cttt():
    MaPK = ct_mapk_cttt.get().strip()
    MaThuoc = ct_mathuoc_cttt.get().strip()
    SoLuong = ct_soluong.get().strip()
    LieuDung = ct_lieudung.get().strip()

    if not (MaPK and MaThuoc):
        messagebox.showwarning("Thiếu dữ liệu", "Cần Mã PK và Mã Thuốc để cập nhật!")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """
        UPDATE chitiettoathuoc
        SET SoLuong = %s, LieuDung = %s
        WHERE MaPK = %s AND MaThuoc = %s
        """
        cursor.execute(sql, (SoLuong, LieuDung, MaPK, MaThuoc))
        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Thành công", "Đã cập nhật!")
            load_cttt()   # nhớ refresh bảng
        else:
            messagebox.showwarning("Không tìm thấy", "Không có chi tiết toa thuốc để cập nhật!")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi cập nhật:\n{e}")

    finally:
        cursor.close()
        conn.close()

def delete_cttt():
    MaPK = ct_mapk_cttt.get()
    MaThuoc = ct_mathuoc_cttt.get()

    if not (MaPK and MaThuoc):
        messagebox.showwarning("Thiếu dữ liệu", "Nhập Mã PK và Mã Thuốc để xóa!")
        return

    if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa không?"):
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = "DELETE FROM ChiTietToaThuoc WHERE MaPK = %s AND MaThuoc = %s"
        cursor.execute(sql, (MaPK, MaThuoc))

        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Thành công", "Đã xóa chi tiết!")
            ct_soluong.delete(0, tk.END)
            ct_lieudung.delete(0, tk.END)
        else:
            messagebox.showwarning("Không tìm thấy", "Không có chi tiết để xóa!")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi xóa:\n{e}")

    finally:
        cursor.close()
        conn.close()
#Frame cho cttt
frame_buttons_cttt = tk.Frame(tab_cttoathuoc)
frame_buttons_cttt.pack(fill="x", pady=5,before=tree_cttt)

tk.Button(frame_buttons_cttt, text="Thêm", width=12, bg="#A9DFBF", command=add_cttt).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons_cttt, text="Cập nhật", width=12, bg="#F9E79F", command=update_cttt).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons_cttt, text="Tìm kiếm", width=12, bg="#F5B7B1", command=search_cttt).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons_cttt, text="Xóa", width=12, bg="#D7BDE2", command=delete_cttt).grid(row=0, column=3, padx=5)
load_cttoathuoc()
root.mainloop()