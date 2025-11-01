import tkinter as tk 
from tkinter import ttk, messagebox 
from tkcalendar import DateEntry 
import mysql.connector 
 
# ====== Kết nối MySQL ====== 
def connect_db(): 
    return mysql.connector.connect( 
        host="localhost", 
        user="root",        # thay bằng user MySQL của bạn 
        password="2703",        # thay bằng password MySQL của bạn 
        database="QLBN" 
    ) 
# ====== Hàm canh giữa cửa sổ ====== 
def center_window(win, w=700, h=500): 
    ws = win.winfo_screenwidth() 
    hs = win.winfo_screenheight() 
    x = (ws // 2) - (w // 2) 
    y = (hs // 2) - (h // 2) 
    win.geometry(f'{w}x{h}+{x}+{y}') 
 
# ====== Cửa sổ chính ====== 
root = tk.Tk() 
root.title("Quản lý nhân viên") 
center_window(root, 700, 500) 
root.resizable(False, False) 
 
# ====== Tiêu đề ====== 
lbl_title = tk.Label(root, text="QUẢN LÝ NHÂN VIÊN", font=("Arial", 18, "bold")) 
lbl_title.pack(pady=10) 
 
# ====== Frame nhập thông tin ====== 
frame_info = tk.Frame(root) 
frame_info.pack(pady=5, padx=10, fill="x") 
 
tk.Label(frame_info, text="Mã số").grid(row=0, column=0, padx=5, pady=5, 
sticky="w") 
entry_maso = tk.Entry(frame_info, width=10) 
entry_maso.grid(row=0, column=1, padx=5, pady=5, sticky="w") 

tk.Label(frame_info, text="Mã phòng").grid(row=0, column=2, padx=5, pady=5, 
sticky="w") 
entry_maphong = tk.Entry(frame_info, width=10) 
entry_maphong.grid(row=0, column=1, padx=5, pady=5, sticky="w") 

 
tk.Label(frame_info, text="Họ lót").grid(row=1, column=0, padx=5, pady=5, 
sticky="w") 
entry_holot = tk.Entry(frame_info, width=25) 
entry_holot.grid(row=1, column=1, padx=5, pady=5, sticky="w") 
 
tk.Label(frame_info, text="Tên").grid(row=1, column=2, padx=5, pady=5, sticky="w") 
entry_ten = tk.Entry(frame_info, width=15) 
entry_ten.grid(row=1, column=3, padx=5, pady=5, sticky="w")
root.mainloop()