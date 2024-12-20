from sinhVien import SinhVien
class QuanLySinhVien:
    def __init__(self):
        self.sinh_vien_list = []
        self.next_id = 1 

    def them_sinh_vien(self, ten, gioi_tinh, tuoi, dtoan, dly, dhoa):
        sv = SinhVien(self.next_id, ten, gioi_tinh, tuoi, float(dtoan), float(dly), float(dhoa))
        self.sinh_vien_list.append(sv)
        self.next_id += 1

    def cap_nhat_sinh_vien(self, id, ten, gioi_tinh, tuoi, dtoan, dly, dhoa):
        for sv in self.sinh_vien_list:
            if sv._id == id:
                sv._ten = ten
                sv._gioi_tinh = gioi_tinh
                sv._tuoi = tuoi
                sv._dtoan = float(dtoan)
                sv._dly = float(dly)
                sv._dhoa = float(dhoa)
                sv._diem_trung_binh = sv.tinh_diem_trung_binh()
                sv._hoc_luc = sv.tinh_hoc_luc()
                return
        print("Không tìm thấy sinh viên với ID:", id)

    def xoa_sinh_vien(self, id):
        self.sinh_vien_list = [sv for sv in self.sinh_vien_list if sv._id != id]

    def tim_kiem_sinh_vien(self, ten):
        return [sv for sv in self.sinh_vien_list if ten.lower() in sv._ten.lower()]

    def sap_xep_sinh_vien_theo_gpa(self):
        self.sinh_vien_list.sort(key=lambda sv: sv._diem_trung_binh, reverse=True)

    def sap_xep_sinh_vien_theo_ten(self):
        self.sinh_vien_list.sort(key=lambda sv: sv._ten)

    def sap_xep_sinh_vien_theo_id(self):
        self.sinh_vien_list.sort(key=lambda sv: sv._id)

    def hien_thi_danh_sach_sinh_vien(self):
        for sv in self.sinh_vien_list:
            print(f"ID: {sv._id}, Tên: {sv._ten}, Giới tính: {sv._gioi_tinh}, Tuổi: {sv._tuoi}, "
                  f"Điểm TB: {sv._diem_trung_binh:.2f}, Học lực: {sv._hoc_luc}")
