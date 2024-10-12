from sinhVien import *
from quanLySinhVien import *
qlsv = QuanLySinhVien()

dt1 = SinhVienDaiTra(1, "Duong", "13/06/2005", 8.63)
dt2 = SinhVienDaiTra(2, "Tam", "23/10/2005", 8.43)
dt3 = SinhVienDaiTra(3, "Duy", "03/04/2005", 8.5)

clc1 = SinhVienChatLuongCao(4, "Chau", "14/07/2005", 8.4)
clc2 = SinhVienChatLuongCao(5, "Bao", "14/08/2005", 7.4)
clc3 = SinhVienChatLuongCao(6, "Chau", "14/09/2005", 9.4)

print("Số sinh viên chính quy có học bổng")


qlsv.add_sinh_vien(dt1)
qlsv.add_sinh_vien(dt2)
qlsv.add_sinh_vien(dt3)
qlsv.add_sinh_vien(clc1)
qlsv.add_sinh_vien(clc2)
qlsv.add_sinh_vien(clc3)
dai_tra, chat_luong_cao = qlsv.hoc_bong_list()

print("Danh sách sinh viên đại trà có học bổng:", dai_tra)
print("Danh sách sinh viên chất lượng cao có học bổng:", chat_luong_cao)

tong_hoc_bong = qlsv.tong_tien_hoc_bong()
print("Tổng số tiền học bổng:", tong_hoc_bong)

sinh_vien_gioi_nhat = qlsv.sinh_vien_cao_nhat()
print("Sinh viên có thành tích cao nhất:", sinh_vien_gioi_nhat)
