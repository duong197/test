from sinhVien import *
class QuanLySinhVien:
    def __init__(self):
        self.sinh_vien_list = []
    
    def add_sinh_vien(self, sv: SinhVien):
        self.sinh_vien_list.append(sv)
    
    def hoc_bong_list(self):
        dai_tra_hoc_bong = [sv._name for sv in self.sinh_vien_list if isinstance(sv, SinhVienDaiTra) and sv.tinh_hoc_bong() != 0]
        chat_luong_cao_hoc_bong = [sv._name for sv in self.sinh_vien_list if isinstance(sv, SinhVienChatLuongCao) and sv.tinh_hoc_bong() != 0]
        return dai_tra_hoc_bong, chat_luong_cao_hoc_bong

    def tong_tien_hoc_bong(self):
        tong_tien = sum(sv.tinh_hoc_bong() for sv in self.sinh_vien_list)
        return tong_tien
    
    def sinh_vien_cao_nhat(self):
        if not self.sinh_vien_list:
            return None
        sv_cao_nhat = max(self.sinh_vien_list, key=lambda sv: sv._avg_grade)
        return sv_cao_nhat.hien_thi_thong_tin()
