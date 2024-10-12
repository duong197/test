class SinhVien:
    def __init__(self, id, ten, gioi_tinh, tuoi, dtoan, dly, dhoa) -> None:
        self._id = id
        self._ten = ten
        self._gioi_tinh = gioi_tinh
        self._tuoi = tuoi
        self._dtoan = dtoan
        self._dly = dly
        self._dhoa = dhoa
        self._diem_trung_binh = (dtoan + dly + dhoa) / 3
        if self._diem_trung_binh < 5:
            self._hoc_luc = "Yếu"
        elif 5 <= self._diem_trung_binh < 6.5:
            self._hoc_luc = "Trung bình"
        elif 6.5 <= self._diem_trung_binh < 8:
            self._hoc_luc = "Khá"
        elif 8 <= self._diem_trung_binh < 10:
            self._hoc_luc = "Giỏi"
        else: 
            print("Điểm trung bình không hợp lệ")
            self._hoc_luc = None