from quanLySinhVien import QuanLySinhVien
def menu():
    qlsv = QuanLySinhVien()
    
    while True:
        print("\n=== Quản Lý Sinh Viên ===")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên")
        print("3. Xóa sinh viên")
        print("4. Tìm kiếm sinh viên theo tên")
        print("5. Sắp xếp sinh viên theo điểm trung bình")
        print("6. Sắp xếp sinh viên theo tên")
        print("7. Sắp xếp sinh viên theo ID")
        print("8. Hiển thị danh sách sinh viên")
        print("0. Thoát")

        lua_chon = input("Chọn chức năng (0-8): ")
        
        if lua_chon == "1":
            ten = input("Nhập tên sinh viên: ")
            gioi_tinh = input("Nhập giới tính sinh viên: ")
            tuoi = int(input("Nhập tuổi sinh viên: "))
            dtoan = float(input("Nhập điểm toán: "))
            dly = float(input("Nhập điểm lý: "))
            dhoa = float(input("Nhập điểm hóa: "))
            qlsv.them_sinh_vien(ten, gioi_tinh, tuoi, dtoan, dly, dhoa)
        
        elif lua_chon == "2":
            try:
                id = int(input("Nhập ID sinh viên cần cập nhật: "))
            except ValueError:
                print("ID phải là số.")
                continue
            ten = input("Nhập tên mới: ")
            gioi_tinh = input("Nhập giới tính mới: ")
            tuoi = input("Nhập tuổi mới: ")
            dtoan = input("Nhập điểm toán mới: ")
            dly = input("Nhập điểm lý mới: ")
            dhoa = input("Nhập điểm hóa mới: ")
            qlsv.cap_nhat_sinh_vien(id, ten, gioi_tinh, tuoi, dtoan, dly, dhoa)
        
        elif lua_chon == "3":
            id = int(input("Nhập ID sinh viên cần xóa: "))
            qlsv.xoa_sinh_vien(id)
        
        elif lua_chon == "4":
            ten = input("Nhập tên sinh viên cần tìm: ")
            ket_qua = qlsv.tim_kiem_sinh_vien(ten)
            if ket_qua:
                for sv in ket_qua:
                    print(f"ID: {sv._id}, Tên: {sv._ten}, Giới tính: {sv._gioi_tinh}, Tuổi: {sv._tuoi}, "
                          f"Điểm TB: {sv._diem_trung_binh:.2f}, Học lực: {sv._hoc_luc}")
            else:
                print("Không tìm thấy sinh viên.")

        elif lua_chon == "5":
            qlsv.sap_xep_sinh_vien_theo_gpa()
            print("Danh sách sinh viên đã được sắp xếp theo điểm trung bình.")

        elif lua_chon == "6":
            qlsv.sap_xep_sinh_vien_theo_ten()
            print("Danh sách sinh viên đã được sắp xếp theo tên.")

        elif lua_chon == "7":
            qlsv.sap_xep_sinh_vien_theo_id()
            print("Danh sách sinh viên đã được sắp xếp theo ID.")

        elif lua_chon == "8":
            qlsv.hien_thi_danh_sach_sinh_vien()

        elif lua_chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    menu()