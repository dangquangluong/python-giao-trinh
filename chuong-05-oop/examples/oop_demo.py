# OOP Demo - Hệ thống quản lý thư viện

class Sach:                                          # Định nghĩa class (khuôn mẫu) Sach
    def __init__(self, tieu_de, tac_gia, nam, so_trang):  # __init__ = constructor, chạy khi tạo object mới
        self.tieu_de = tieu_de                       # self = object hiện tại, lưu tiêu đề vào object
        self.tac_gia = tac_gia                       # Lưu tên tác giả vào object
        self.nam = nam                               # Lưu năm xuất bản vào object
        self.so_trang = so_trang                     # Lưu số trang vào object
        self.da_muon = False                         # Mặc định sách chưa được mượn (False)

    def muon(self):                                  # Method (hàm trong class) để mượn sách
        if not self.da_muon:                         # Nếu sách chưa được mượn (not False = True)
            self.da_muon = True                      # Đánh dấu đã mượn
            return True                              # Trả về True = mượn thành công
        return False                                 # Sách đã được mượn rồi, trả về False

    def tra(self):                                   # Method để trả sách
        self.da_muon = False                         # Đặt lại trạng thái = chưa mượn

    def __str__(self):                               # __str__ = method đặc biệt, gọi khi print(object)
        status = "📕 Đã mượn" if self.da_muon else "📗 Có sẵn"  # Ternary: chọn emoji theo trạng thái
        return f"{status} | {self.tieu_de} - {self.tac_gia} ({self.nam})"  # Trả về chuỗi mô tả sách

    def __repr__(self):                              # __repr__ = biểu diễn chính thức (dùng cho debug)
        return f"Sach('{self.tieu_de}', '{self.tac_gia}')"  # Trả về chuỗi có thể tái tạo object


class ThuVien:                                       # Class ThuVien quản lý danh sách sách
    def __init__(self, ten):                         # Constructor nhận tên thư viện
        self.ten = ten                               # Lưu tên thư viện
        self.sach_list = []                          # Tạo list rỗng để chứa các object Sach

    def them_sach(self, sach):                       # Method thêm sách vào thư viện
        self.sach_list.append(sach)                  # .append() thêm object sách vào cuối list

    def tim_kiem(self, tu_khoa):                     # Method tìm sách theo từ khóa
        tu_khoa = tu_khoa.lower()                    # Chuyển từ khóa thành chữ thường để so sánh
        return [s for s in self.sach_list            # List comprehension: lọc sách phù hợp
                if tu_khoa in s.tieu_de.lower() or tu_khoa in s.tac_gia.lower()]  # Tìm trong tiêu đề hoặc tác giả

    def sach_co_san(self):                           # Method lấy danh sách sách chưa được mượn
        return [s for s in self.sach_list if not s.da_muon]  # Lọc sách có da_muon = False

    def hien_thi(self):                              # Method hiển thị toàn bộ thư viện
        print(f"\n📚 Thư viện: {self.ten} ({len(self.sach_list)} sách)")  # In tên + số sách
        print("-" * 60)                              # In đường kẻ phân cách
        for s in self.sach_list:                     # Lặp qua từng cuốn sách
            print(f"  {s}")                          # print(s) tự gọi __str__() của object Sach

    def __len__(self):                               # __len__ cho phép dùng len(thu_vien)
        return len(self.sach_list)                   # Trả về số sách trong thư viện


# === SỬ DỤNG ===
if __name__ == "__main__":                           # Chỉ chạy khi file được thực thi trực tiếp (không phải import)
    # Tạo thư viện
    tv = ThuVien("Thư viện Python")                  # Tạo object ThuVien, gọi __init__ tự động

    # Thêm sách
    tv.them_sach(Sach("Clean Code", "Robert Martin", 2008, 464))         # Tạo object Sach và thêm vào thư viện
    tv.them_sach(Sach("Python Crash Course", "Eric Matthes", 2019, 544)) # Thêm sách thứ 2
    tv.them_sach(Sach("Design Patterns", "Gang of Four", 1994, 395))     # Thêm sách thứ 3
    tv.them_sach(Sach("The Pragmatic Programmer", "Hunt & Thomas", 1999, 352))  # Thêm sách thứ 4

    # Hiển thị
    tv.hien_thi()                                    # Gọi method hiển thị toàn bộ sách

    # Mượn sách
    print("\n--- Mượn 'Clean Code' ---")             # In tiêu đề hành động
    sach = tv.tim_kiem("clean")[0]                   # Tìm sách có chữ "clean", lấy kết quả đầu tiên [0]
    if sach.muon():                                  # Gọi method muon(), kiểm tra thành công
        print(f"✅ Đã mượn: {sach.tieu_de}")        # In xác nhận mượn thành công

    # Hiển thị lại
    tv.hien_thi()                                    # Hiển thị lại để thấy sách đã đổi trạng thái

    # Tìm kiếm
    print("\n--- Tìm 'python' ---")                  # In tiêu đề tìm kiếm
    ket_qua = tv.tim_kiem("python")                  # Tìm sách có chứa "python"
    for s in ket_qua:                                # Lặp qua kết quả tìm được
        print(f"  {s}")                              # In từng kết quả

    # Sách có sẵn
    print(f"\n📗 Sách có sẵn: {len(tv.sach_co_san())}/{len(tv)}")  # len(tv) gọi __len__()
