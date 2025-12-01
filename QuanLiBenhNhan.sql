CREATE DATABASE QLBN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE QLBN;


CREATE TABLE BenhNhan (
    MaBN VARCHAR(10) PRIMARY KEY,
    HoLot VARCHAR(100),
    Ten VARCHAR(50),
    NgaySinh DATE,
    Phai VARCHAR(10),
    DiaChi VARCHAR(100),
    LoaiBenhNhan ENUM('NoiTru','NgoaiTru') NOT NULL,  -- phân biệt nội trú / ngoại trú
    MaPhong VARCHAR(10),                               -- chỉ dùng cho bệnh nhân nội trú
);

CREATE TABLE BacSi (
    MaBS VARCHAR(10) PRIMARY KEY,
    HoLot VARCHAR(100),
    Ten VARCHAR(50),
    Khoa VARCHAR(50),
    DiaChi VARCHAR(100)
);



CREATE TABLE PhieuKham (
    MaPK VARCHAR(10) PRIMARY KEY,
    MaBN VARCHAR(10),
    MaBS VARCHAR(10),
    NgayKham DATE,
    LoaiKham VARCHAR(100),
    ChanDoan VARCHAR(100),
    GhiChu TEXT,
    FOREIGN KEY (MaBN) REFERENCES BenhNhan(MaBN),
    FOREIGN KEY (MaBS) REFERENCES BacSi(MaBS)
);

CREATE TABLE Thuoc (
    MaThuoc VARCHAR(10) PRIMARY KEY,
    TenThuoc VARCHAR(100),
    DonViThuoc VARCHAR(20),
    DonGia DECIMAL(10,2),
    CongDung VARCHAR(200)
);

CREATE TABLE ChiTietToaThuoc (
    MaPK VARCHAR(10),
    MaThuoc VARCHAR(10),
    SoLuong INT,
    LieuDung VARCHAR(100),
    PRIMARY KEY (MaPK, MaThuoc),
    FOREIGN KEY (MaPK) REFERENCES PhieuKham(MaPK),
    FOREIGN KEY (MaThuoc) REFERENCES Thuoc(MaThuoc)
);

INSERT INTO benhnhan (MaBN, HoLot, Ten, NgaySinh, Phai, DiaChi, LoaiBenhNhan, MaPhong) VALUES
('BN001', 'Nguyen Van', 'An', '2002-05-12', 'Nam', 'HCM', 'NoiTru', 'P101'),
('BN002', 'Tran Thi', 'Hoa', '1999-11-02', 'Nu', 'Can Tho', 'NgoaiTru', 'K02'),
('BN003', 'Le Minh', 'Khang', '2001-07-22', 'Nam', 'Long An', 'NoiTru', 'P102'),
('BN004', 'Pham Thu', 'Trang', '2000-09-30', 'Nu', 'HCM', 'NgoaiTru', 'K01'),
('BN005','Tran Minh', 'Phung', '2002-09-12', 'Nu', 'Vung Tau', 'NgoaiTru', 'K02'),
('BN006', 'Dao Mai', 'Thuy', '1997-04-30', 'Nam', 'Can Tho', 'NoiTru', 'P101');
INSERT INTO bacsi (MaBS, HoLot, Ten, Khoa, DiaChi) VALUES
('BS01', 'Nguyễn Văn', 'Hòang', 'Nội', '123/34, Phường Sài Gòn,Thành phố Hồ Chí Minh'),
('BS02', 'Trần Thị', 'Nhung', 'Ngoại', 'Phường Bến Thành,Thành phố Hồ Chí Minh'),
('BS03', 'Võ Minh', 'Phúc', 'Nhi', 'Châu Thành,Tiền Giang');
INSERT INTO phieukham (MaPK, MaBN, MaBS, NgayKham, LoaiKham, ChanDoan, GhiChu) VALUES
('PK001', 'BN001', 'BS01', '2025-01-10', 'Khám nội tổng quát', 'Viêm họng', 'Cần uống thuốc đúng liều'),
('PK002', 'BN002', 'BS02', '2025-01-12', 'Khám ngoại', 'Đau vai', 'Hạn chế mang vác nặng'),
('PK003', 'BN003', 'BS03', '2025-01-14', 'Khám nhi', 'Sốt siêu vi', 'Theo dõi thêm'),
('PK004', 'BN001', 'BS02', '2025-01-16', 'Khám ngoại', 'Chấn thương nhẹ', NULL),
('PK005', 'BN004', 'BS01', '2025-01-18', 'Khám nội', 'Rối loạn tiêu hoá', NULL);
INSERT INTO Thuoc (MaThuoc, TenThuoc, DonViThuoc, DonGia, CongDung) VALUES
('T001', 'Paracetamol', 'Viên', 5000, 'Giảm đau hạ sốt'),
('T002', 'Amoxicillin', 'Viên', 8000, 'Kháng sinh'),
('T003', 'Vitamin C', 'Viên', 3000, 'Tăng đề kháng'),
('T004', 'Oresol', 'Gói', 2000, 'Bù nước điện giải'),
('T005', 'Ibuprofen', 'Viên', 7000, 'Giảm đau, kháng viêm'),
('T006', 'Cetirizine', 'Viên', 6000, 'Chống dị ứng'),
('T007', 'Omeprazole', 'Viên', 9000, 'Điều trị dạ dày'),
('T008', 'Smecta', 'Gói', 4000, 'Chống tiêu chảy'),
('T009', 'Clorpheniramin', 'Viên', 1500, 'Giảm dị ứng, sổ mũi'),
('T010', 'Natri Clorid 0.9%', 'Chai', 12000, 'Nước muối sinh lý');
INSERT INTO ChiTietToaThuoc (MaPK, MaThuoc, SoLuong, LieuDung) VALUES
('PK001', 'T001', 10, 'Ngày 3 lần'),
('PK001', 'T003', 5, 'Ngày 1 lần'),
('PK002', 'T002', 15, 'Ngày 2 lần'),
('PK003', 'T003', 10, 'Ngày 1 lần'),
('PK003', 'T004', 3, 'Pha uống khi sốt'),
('PK004', 'T001', 6, 'Ngày 2 lần'),
('PK005', 'T004', 5, 'Uống bù nước');
GRANT ALL PRIVILEGES ON QLBN.* TO 'QLBenhNhan'@'localhost';
FLUSH PRIVILEGES;
select *from phongbenh