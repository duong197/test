class SinhVien:
    def __init__(self, id, name, dob, avg_grade):
        self._id = id
        self._name = name
        self._dob = dob
        self._avg_grade = avg_grade
    
    def hien_thi_thong_tin(self):
        return f"ID: {self._id}, Tên: {self._name}, Ngày sinh: {self._dob}, Điểm trung bình: {self._avg_grade}"
    
class SinhVienDaiTra(SinhVien):
    def __init__(self, id, name, dob, avg_grade):
        super().__init__(id, name, dob, avg_grade)
    def tinh_hoc_bong(self):
        if self._avg_grade >= 9:
            return 1500000
        elif self._avg_grade >= 8:
            return 1000000
        else:
            return 0

class SinhVienChatLuongCao(SinhVien):
    def __init__(self, id, name, dob, avg_grade):
        super().__init__(id, name, dob, avg_grade)
    def tinh_hoc_bong(self):
        if self._avg_grade >= 9:
            return 2000000
        elif self._avg_grade >= 8:
            return 1500000
        else:
            return 0