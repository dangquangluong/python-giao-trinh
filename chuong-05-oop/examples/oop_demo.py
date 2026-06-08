# OOP Demo - Hệ thống quản lý thư viện

class Sach:
    def __init__(self, tieu_de, tac_gia, nam, so_trang):
        self.tieu_de = tieu_de
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_trang = so_trang
        self.da_muon = False

    def muon(self):
        if not self.da_muon:
            self.da_muon = True
            return True
        return False

    def tra(self):
        self.da_muon = False

    def __str__(self):
        status = "📕 Đã mượn" if self.da_muon else "📗 Có sẵn"
        return f"{status} | {self.tieu_de} - {self.tac_gia} ({self.nam})"

    def __repr__(self):
        return f"Sach('{self.tieu_de}', '{self.tac_gia}')"


class ThuVien:
    def __init__(self, ten):
        self.ten = ten
        self.sach_list = []

    def them_sach(self, sach):
        self.sach_list.append(sach)

    def tim_kiem(self, tu_khoa):
        tu_khoa = tu_khoa.lower()
        return [s for s in self.sach_list
                if tu_khoa in s.tieu_de.lower() or tu_khoa in s.tac_gia.lower()]

    def sach_co_san(self):
        return [s for s in self.sach_list if not s.da_muon]

    def hien_thi(self):
        print(f"\n📚 Thư viện: {self.ten} ({len(self.sach_list)} sách)")
        print("-" * 60)
        for s in self.sach_list:
            print(f"  {s}")

    def __len__(self):
        return len(self.sach_list)


# === SỬ DỤNG ===
if __name__ == "__main__":
    # Tạo thư viện
    tv = ThuVien("Thư viện Python")

    # Thêm sách
    tv.them_sach(Sach("Clean Code", "Robert Martin", 2008, 464))
    tv.them_sach(Sach("Python Crash Course", "Eric Matthes", 2019, 544))
    tv.them_sach(Sach("Design Patterns", "Gang of Four", 1994, 395))
    tv.them_sach(Sach("The Pragmatic Programmer", "Hunt & Thomas", 1999, 352))

    # Hiển thị
    tv.hien_thi()

    # Mượn sách
    print("\n--- Mượn 'Clean Code' ---")
    sach = tv.tim_kiem("clean")[0]
    if sach.muon():
        print(f"✅ Đã mượn: {sach.tieu_de}")

    # Hiển thị lại
    tv.hien_thi()

    # Tìm kiếm
    print("\n--- Tìm 'python' ---")
    ket_qua = tv.tim_kiem("python")
    for s in ket_qua:
        print(f"  {s}")

    # Sách có sẵn
    print(f"\n📗 Sách có sẵn: {len(tv.sach_co_san())}/{len(tv)}")
