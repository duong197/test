class SinhVien:
    def __init__(self, id, ten, gioi_tinh, tuoi, dtoan, dly, dhoa) -> None:
        self._id = id
        self._ten = ten
        self._gioi_tinh = gioi_tinh
        self._tuoi = tuoi
        self._dtoan = float(dtoan)
        self._dly = float(dly)
        self._dhoa = float(dhoa)
        self._diem_trung_binh = self.tinh_diem_trung_binh()
        self._hoc_luc = self.tinh_hoc_luc()
    
    def tinh_diem_trung_binh(self):
        return float(self._dtoan + self._dly + self._dhoa) / 3
    def tinh_hoc_luc(self):
        if self._diem_trung_binh < 5:   
            return "Yếu"
        elif 5 <= self._diem_trung_binh < 6.5:
            return "Trung bình"
        elif 6.5 <= self._diem_trung_binh < 8:
            return "Khá"
        elif 8 <= self._diem_trung_binh <= 10:
            return "Giỏi"
        
        