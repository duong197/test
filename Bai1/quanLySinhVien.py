from sinhVien import SinhVien
class QuanLySinhVien:
    def __init__(self):
        self.sinh_vien_list = []
        self.next_id = 1  # Khởi tạo id tự động tăng

    def them_sinh_vien(self, ten, gioi_tinh, tuoi, dtoan, dly, dhoa):
        sv = SinhVien(self.next_id, ten, gioi_tinh, tuoi, dtoan, dly, dhoa)
        self.sinh_vien_list.append(sv)
        self.next_id += 1

    def cap_nhat_sinh_vien(self, id, ten=None, gioi_tinh=None, tuoi=None, dtoan=None, dly=None, dhoa=None):
        for sv in self.sinh_vien_list:
            if sv.id == id:
                if ten is not None:
                    sv.ten = ten
                if gioi_tinh is not None:
                    sv.gioi_tinh = gioi_tinh
                if tuoi is not None:
                    sv.tuoi = tuoi
                if dtoan is not None:
                    sv.dtoan = dtoan
                if dly is not None:
                    sv.dly = dly
                if dhoa is not None:
                    sv.dhoa = dhoa
                sv.diem_trung_binh = sv.tinh_diem_trung_binh()  # Cập nhật điểm trung bình
                sv.hoc_luc = sv.xac_dinh_hoc_luc()  # Cập nhật học lực
                return
        print("Không tìm thấy sinh viên với ID:", id)

    def xoa_sinh_vien(self, id):
        self.sinh_vien_list = [sv for sv in self.sinh_vien_list if sv.id != id]

    def tim_kiem_sinh_vien(self, ten):
        return [sv for sv in self.sinh_vien_list if ten.lower() in sv.ten.lower()]

    def sap_xep_sinh_vien_theo_gpa(self):
        self.sinh_vien_list.sort(key=lambda sv: sv.diem_trung_binh, reverse=True)

    def sap_xep_sinh_vien_theo_ten(self):
        self.sinh_vien_list.sort(key=lambda sv: sv.ten)

    def sap_xep_sinh_vien_theo_id(self):
        self.sinh_vien_list.sort(key=lambda sv: sv.id)

    def hien_thi_danh_sach_sinh_vien(self):
        for sv in self.sinh_vien_list:
            print(f"ID: {sv.id}, Tên: {sv.ten}, Giới tính: {sv.gioi_tinh}, Tuổi: {sv.tuoi}, "
                  f"Điểm TB: {sv.diem_trung_binh:.2f}, Học lực: {sv.hoc_luc}")
