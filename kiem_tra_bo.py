#!/usr/bin/env python3
# kiem_tra_bo.py · bộ test hồi quy cho WORKOPS STARTER · v21 · 20260825
# v21 bộ kiểm: thêm hai fixture de_ngoai, tổng 68 ca. Trước đó v20 66 ca. Một dòng "Kho 01_A/" phải bao phủ
# 01_A/BC_v02.docx trong chế độ --ho (chống đề xuất _INBOX oan); cache đời cũ
# không mang theo bằng chứng ổn định sang bản mới.
# v19: fixture chế độ --ho kiểm HÀNH VI THẬT thay vì hàm khớp tên: v01 phải
# kéo theo v02 cùng họ, không kéo họ khác cùng thư mục, không kéo cùng tên ở
# dự án khác, thư mục và tên họ trơ bị từ chối, hai lần quét sát nhau không
# thành ổn định, file đổi nội dung mất mốc cũ, file đã xóa biến khỏi cache,
# không khớp file nào là LỆCH, thiếu giá trị sau --ho là lỗi cách dùng. Mọi
# fixture thời gian dùng THỜI GIAN GIẢ qua tham số bay_gio, không chờ thật.
# LƯU Ý PHẠM VI: phép kiểm 12 xác nhận LUẬT CÓ MẶT trong tài liệu (chuỗi then
# chốt); hành vi dựng digest, nhận tên người được gọi, cảnh báo dữ liệu cũ chạy
# đúng hay không phải nghiệm thu ở BỘ EMAIL THẬT, PASS ở đây không thay được.
# v15: --gop <đường dẫn> chỉ định bản gộp khi không nằm cạnh thư mục bộ (ZIP
# giờ cũng chứa sẵn _GOP để tự kiểm độc lập); mặc định im lặng với chi tiết
# fixture (các dòng LECH của tình huống ÂM là chủ ý, từng làm người dùng tưởng
# bộ hỏng), truyền --verbose để xem đủ.
# Chạy: python3 kiem_tra_bo.py <thư mục bộ starter> [--skip-gop] [--gop <file>] [--verbose]
# Mười phép kiểm, PASS hết mới được đóng gói. Thiếu bản gộp _GOP là FAIL, chỉ được
# bỏ qua khi truyền cờ --skip-gop tường minh. Thoát 0 khi sạch, 1 khi có lỗi.

import re
import sys
from pathlib import Path

# Console Windows mặc định cp1252 không in được tiếng Việt: ép UTF-8,
# lỗi ký tự thì thay thế chứ không crash giữa chừng phép kiểm.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

FILE_BAT_BUOC = [
    "DOC_TRUOC.md",
    "X0_CAUHINH_TEMPLATE.md",
    "X1_CAM_TEMPLATE.md",
    "X2_PHATHANH_TEMPLATE.md",
    "X3_CUAVAO_TEMPLATE.md",
    "X3E_EMAIL_TEMPLATE.md",
    "X4_RASOAT_TEMPLATE.md",
    "X5_HESO_TEMPLATE.md",
    "X9_CAIDAT.md",
    "_so/BANG_DIEU_KHIEN.md",
    "_so/VIEC.md",
    "_so/DUKIEN.md",
    "_so/TAILIEU.md",
    "_so/QUYETDINH.md",
    "_so/NHATKY_TEMPLATE.md",
    "_so/PLANNING.md",
    "_so/X0_INDEX.md",
    "_so/THU.md",
    "BENCHMARK_TOKEN.md",
]
# File kèm bắt buộc: kiểm CÓ MẶT và có trong _GOP, nhưng miễn kiểm ký tự cấm và
# tham chiếu chéo (script giữ danh sách ký tự cấm làm mẫu dò; GHICHU trích nguyên
# văn các vòng cũ nên được phép chứa tham chiếu lịch sử)
FILE_KEM = ["kiem_tra_bo.py", "kiem_van_hanh.py"]

# Ngân sách context, tính bằng ký tự (ước lượng token tiếng Việt = ký tự / 3)
NGAN_SACH = {
    "INSTRUCTION": 8000,          # ~2.600 token, thuế thường trực
    "X0_CAUHINH_TEMPLATE.md": 16000,  # đọc theo mục; thuế thường trực là X0_INDEX
    "X1_CAM_TEMPLATE.md": 3200,
    "X2_PHATHANH_TEMPLATE.md": 4200,
    "X3_CUAVAO_TEMPLATE.md": 4500,   # mục 6 đã tách sang X3E
    "X3E_EMAIL_TEMPLATE.md": 12000,  # chỉ nạp khi bật EMAIL, không phải thuế lõi
    "X4_RASOAT_TEMPLATE.md": 5500,  # chỉ đọc khi RA_SOAT, không phải thuế thường trực
    "X5_HESO_TEMPLATE.md": 16000,
    "X9_CAIDAT.md": 6500,  # đọc một lần mỗi công ty, không phải thuế thường trực
    "_so/X0_INDEX.md": 1500,
    "_so/BANG_DIEU_KHIEN.md": 1400,
}
KY_TU_CAM = ["—", "–", "→", "←", "≈"] + [chr(c) for c in range(0x20)
             if chr(c) not in "\n\t\r"]  # em/en-dash, mũi tên, xấp xỉ, control char
# control char: hội đồng vòng 2 bắt được backspace 0x08 lọt vào đường dẫn
# backup của X5 do escape bị nuốt khi soạn; dò cả dải để lớp lỗi này tuyệt chủng
def _muc(nd, tu, den=None):
    """Ký tự của đoạn từ heading '# tu.' tới trước '# den.' (hết file nếu None)."""
    m = re.search(rf"^# {tu}\. .*$", nd, re.M)
    if not m:
        return 0
    dau = m.start()
    if den is not None:
        m2 = re.search(rf"^# {den}\. ", nd, re.M)
        if m2:
            return len(nd[dau:m2.start()])
    return len(nd[dau:])


def do_route(docs):
    """Đo lại các con số route của BENCHMARK từ file thật (token = ký tự / 3).
    Trả dict nhãn dòng -> token. Phép 2c so, --sinh-benchmark in ra."""
    x1, x2 = docs["X1_CAM_TEMPLATE.md"], docs["X2_PHATHANH_TEMPLATE.md"]
    x3, x3e = docs["X3_CUAVAO_TEMPLATE.md"], docs["X3E_EMAIL_TEMPLATE.md"]
    x4, x5 = docs["X4_RASOAT_TEMPLATE.md"], docs["X5_HESO_TEMPLATE.md"]
    x5m1 = _muc(x5, 1, 2)
    x1m34 = _muc(x1, 3, 5)
    t = lambda n: round(n / 3)
    return {
        "NOI_BO mức A": t(x5m1 + x1m34),
        "CUA_VAO thường": t(_muc(x3, 1, 6) + x5m1),
        "CUA_VAO mail": t(_muc(x3, 1, 6) + x5m1 + len(x3e)),
        "RA_SOAT": t(len(x4)),
        "SOAN_RA thường lệ": t(len(x1) + len(x2) + x5m1),
        "SUA_FILE nội bộ": t(len(x5)),
    }


TRANG_THAI_HOP_LE = {
    "VIEC": "MỚI ĐANG LÀM CHỜ ĐỐI TÁC CHỜ DUYỆT TREO XONG HỦY",
    "DUKIEN": "CHƯA KIỂM ĐÃ KIỂM MÂU THUẪN ĐÃ THAY HẾT HẠN",
    "PLAN": "MỚI ĐANG LÀM CHỜ CHỐT ĐÃ GHI HỦY",
}

loi = []


def kiem(ten, dieu_kien, chi_tiet=""):
    if dieu_kien:
        print(f"  PASS  {ten}")
    else:
        print(f"  FAIL  {ten}" + (f": {chi_tiet}" if chi_tiet else ""))
        loi.append(ten)


def main(goc):
    goc = Path(goc)

    # 1. Đủ file bắt buộc, có đúng một INSTRUCTION và một GHICHU
    thieu = [f for f in FILE_BAT_BUOC + FILE_KEM if not (goc / f).is_file()]
    instr = sorted(goc.glob("INSTRUCTION_WORKOPS_v*.md"))
    ghichu = sorted(goc.glob("GHICHU_DOI_MOI_v*.md"))
    kiem("1. đủ file bắt buộc, gồm benchmark và hai script", not thieu, f"thiếu {thieu}")
    kiem("1b. đúng một file INSTRUCTION", len(instr) == 1, f"thấy {len(instr)}")
    kiem("1c. đúng một file GHICHU_DOI_MOI_v*", len(ghichu) == 1, f"thấy {len(ghichu)}")
    if thieu or not instr or not ghichu:
        return

    docs = {f: (goc / f).read_text(encoding="utf-8") for f in FILE_BAT_BUOC}
    docs["INSTRUCTION"] = instr[0].read_text(encoding="utf-8")
    kem = {f: (goc / f).read_text(encoding="utf-8") for f in FILE_KEM}
    kem[ghichu[0].name] = ghichu[0].read_text(encoding="utf-8")

    # 2. Phiên bản khớp: instruction_yeu_cau trong X0 = vN trong header INSTRUCTION
    m_yc = re.search(r"instruction_yeu_cau:\s*(v\d+)", docs["X0_CAUHINH_TEMPLATE.md"])
    m_iv = re.search(r"INSTRUCTION · WORKOPS · (v\d+)", docs["INSTRUCTION"])
    m_dt = re.search(r"INSTRUCTION_WORKOPS_(v\d+)\.md", docs["DOC_TRUOC.md"])
    m_bo = re.search(r"BỘ KHỞI TẠO WORKOPS · (v\d+)", docs["DOC_TRUOC.md"])
    m_bm = re.search(r"BENCHMARK_TOKEN · STARTER (v\d+)", docs["BENCHMARK_TOKEN.md"])
    # 2c. các con số route trong BENCHMARK phải khớp file thật (dung sai 10%);
    #     hội đồng vòng 2-3: lời tự nhận "sinh từ kích thước thật" phải được máy giữ
    do = do_route(docs)
    bm = docs["BENCHMARK_TOKEN.md"]
    lech_bm = []
    for nhan, gia_tri in do.items():
        m_rt = re.search(re.escape(nhan) + r"([^\n]*)", bm)
        cac_so = [int(x) for x in re.findall(r"~(\d+)", m_rt.group(1))] if m_rt else []
        if not cac_so:
            lech_bm.append(f"{nhan}: không thấy dòng trong BENCHMARK")
        elif abs(max(cac_so) - gia_tri) > 0.10 * gia_tri:
            # tổng của dòng là số LỚN NHẤT (các số nhỏ hơn là thành phần)
            lech_bm.append(f"{nhan}: BENCHMARK ~{max(cac_so)}, đo thật ~{gia_tri}")
    kiem("2c. số route BENCHMARK khớp số đo thật (dung sai 10%)", not lech_bm,
         str(lech_bm) + " ; chạy --sinh-benchmark để lấy số mới")
    if "--sinh-benchmark" in sys.argv:
        print("  SỐ ĐO route hiện tại (dán vào BENCHMARK):")
        for nhan, gia_tri in do.items():
            print(f"    {nhan}: ~{gia_tri}")

    kiem("2b. version BENCHMARK khớp version bộ ở DOC_TRUOC",
         bool(m_bo and m_bm and m_bo.group(1) == m_bm.group(1)),
         f"DOC_TRUOC={m_bo and m_bo.group(1)} BENCHMARK={m_bm and m_bm.group(1)}")
    kiem("2. instruction_yeu_cau khớp bản INSTRUCTION và DOC_TRUOC",
         m_yc and m_iv and m_dt and m_yc.group(1) == m_iv.group(1) == m_dt.group(1)
         and instr[0].name == f"INSTRUCTION_WORKOPS_{m_iv.group(1)}.md",
         f"X0={m_yc and m_yc.group(1)} INSTR={m_iv and m_iv.group(1)} DOC={m_dt and m_dt.group(1)}")

    # 3. Mọi tham chiếu "X0 Cn" đều có mục "# Cn." trong X0
    co_muc = set(re.findall(r"^# (C\d+)\.", docs["X0_CAUHINH_TEMPLATE.md"], re.M))
    dung = set()
    for ten, nd in docs.items():
        if ten == "X0_CAUHINH_TEMPLATE.md":
            continue
        dung |= set(re.findall(r"X0 (C\d+)", nd))
    thieu_muc = sorted(dung - co_muc)
    kiem("3. tham chiếu X0 Cn tồn tại", not thieu_muc, f"thiếu mục {thieu_muc}")

    # 4. Không ký tự cấm trong mọi file
    dinh = []
    for ten, nd in docs.items():
        for ch in KY_TU_CAM:
            if ch in nd:
                dinh.append((ten, hex(ord(ch))))
    kiem("4. không ký tự cấm (em/en-dash, mũi tên, xấp xỉ)", not dinh, str(dinh))

    # 5. Bảng sổ mẫu: dòng header và dòng kẻ cùng số cột
    lech = []
    for ten in ["_so/VIEC.md", "_so/DUKIEN.md", "_so/TAILIEU.md",
                "_so/QUYETDINH.md", "_so/NHATKY_TEMPLATE.md", "_so/PLANNING.md"]:
        dong = docs[ten].splitlines()
        for i, d in enumerate(dong[:-1]):
            if d.startswith("|") and re.match(r"^\|[\s:|-]+\|$", dong[i + 1] or ""):
                so_cot = d.count("|") - 1
                so_ke = dong[i + 1].count("|") - 1
                if so_cot != so_ke:
                    lech.append((ten, so_cot, so_ke))
    kiem("5. bảng sổ mẫu đúng số cột", not lech, str(lech))

    # 6. Danh sách trạng thái trong X5 chứa đủ bộ giá trị hợp lệ
    x5 = docs["X5_HESO_TEMPLATE.md"]
    thieu_tt = [gt for gt in ["MỚI", "ĐANG LÀM", "CHỜ ĐỐI TÁC", "CHỜ DUYỆT", "TREO",
                              "XONG", "HỦY", "CHƯA KIỂM", "ĐÃ KIỂM", "MÂU THUẪN",
                              "ĐÃ THAY", "HẾT HẠN", "CHỜ CHỐT", "ĐÃ GHI"]
                if gt not in x5]
    kiem("6. bộ trạng thái VIEC, DUKIEN, PLAN có mặt đủ trong X5", not thieu_tt,
         f"thiếu {thieu_tt}")

    # 7. Định dạng mã nhất quán: X5 và NHATKY template cùng một dạng mã G
    dang_g = re.findall(r"G-<YYYYMMDD>-<C\S*>-<NN>", x5 + docs["_so/NHATKY_TEMPLATE.md"])
    kiem("7. dạng mã G có định danh cửa, khai ở cả X5 và NHATKY", len(dang_g) >= 2,
         f"thấy {len(dang_g)} chỗ")

    # 9. Ngân sách token: file vượt budget là FAIL (enforce bằng máy, không bằng cảm giác)
    vuot_ns = []
    for ten, tran in NGAN_SACH.items():
        nd = docs["INSTRUCTION"] if ten == "INSTRUCTION" else docs.get(ten, "")
        if nd and len(nd) > tran:
            vuot_ns.append((ten, len(nd), tran))
    kiem("9. mọi file trong ngân sách context", not vuot_ns,
         "; ".join(f"{t} {c} ký tự / trần {tr}" for t, c, tr in vuot_ns))
    print(f"        thuế thường trực (INSTRUCTION + X0_INDEX + BANG_DIEU_KHIEN mẫu): "
          f"~{(len(docs['INSTRUCTION']) + len(docs['_so/X0_INDEX.md']) + len(docs['_so/BANG_DIEU_KHIEN.md'])) // 3} token")

    # 11. Fixture hồi quy cho bộ quan sát (import hàm thật từ kiem_van_hanh.py)
    sys.path.insert(0, str(goc))
    sys.dont_write_bytecode = True  # không sinh __pycache__ vào trong bộ
    try:
        import tempfile
        from kiem_van_hanh import suy_hien_hanh, la_file_tam, quet_ho
        ca = []
        S = lambda ds: suy_hien_hanh(ds)
        # a. v01 v02 (đã ổn định) thì v02 hiện hành, v01 cũ
        r = S([{"ten": "BC_v01.docx", "sha": "a", "on_dinh": True},
               {"ten": "BC_v02.docx", "sha": "b", "on_dinh": True}])
        ca.append(("v02 hiện hành, v01 cũ", r["hien_hanh"] == ["BC_v02.docx"] and r["cu"] == ["BC_v01.docx"]))
        # b. file tạm và conflicted copy bị bỏ
        r = S([{"ten": "BC_v02.docx", "sha": "a", "on_dinh": True},
               {"ten": "~$BC_v03.docx", "sha": "x", "on_dinh": True}])
        ca.append(("file tạm bị bỏ", r["bo"] and r["hien_hanh"] == ["BC_v02.docx"]))
        ca.append(("nhận diện conflicted copy", la_file_tam("BC (conflicted copy).docx")))
        # c. hai v03 CÙNG DUNG LƯỢNG khác sha thật thì XUNG ĐỘT (không dùng size)
        r = S([{"ten": "DA_v03.docx", "sha": "sha-khac-1", "on_dinh": True},
               {"ten": "DA v03.docx", "sha": "sha-khac-2", "on_dinh": True}])
        ca.append(("cùng vN khác nội dung là XUNG ĐỘT", r["xung_dot"] and not r["hien_hanh"]))
        # d. chưa ổn định (mới thấy lần đầu) thì KHÔNG XÁC ĐỊNH, không nhận vội
        r = S([{"ten": "BC_v03.docx", "sha": "m", "on_dinh": False}])
        ca.append(("chưa ổn định thì chờ, không nhận", r["khong_xac_dinh"] and not r["hien_hanh"]))
        # e. không có vN: chọn theo mtime; mtime không phân định được thì KHÔNG XÁC ĐỊNH
        r = S([{"ten": "A.docx", "sha": "1", "mtime": 200, "on_dinh": True},
               {"ten": "Z.docx", "sha": "2", "mtime": 100, "on_dinh": True}])
        ca.append(("không vN chọn theo mtime, không theo tên", r["hien_hanh"] == ["A.docx"]))
        r = S([{"ten": "A.docx", "sha": "1", "mtime": 100, "on_dinh": True},
               {"ten": "Z.docx", "sha": "2", "mtime": 100, "on_dinh": True}])
        ca.append(("mtime bằng nhau thì KHÔNG XÁC ĐỊNH", len(r["khong_xac_dinh"]) == 2))
        # f. quét kho thật: file mới độc lập vẫn ra hiện hành; hai thư mục trùng tên
        #    file là hai họ riêng; hai lần quét mới ổn định
        with tempfile.TemporaryDirectory() as td:
            kho = Path(td)
            (kho / "01_A").mkdir(); (kho / "02_B").mkdir()
            (kho / "01_A" / "MoiToanh.docx").write_text("x", encoding="utf-8")
            (kho / "02_B" / "MoiToanh.docx").write_text("noi dung khac", encoding="utf-8")
            T = 10_000_000.0                            # thời gian giả, khỏi chờ thật
            n1, st1 = quet_ho(kho, {}, (), None, T)     # lần 1: chưa ổn định
            chua = all(not kq["hien_hanh"] for kq in n1.values())
            n0, _ = quet_ho(kho, st1, (), None, T + 10)  # quét lại NGAY: vẫn chưa
            chua = chua and all(not kq["hien_hanh"] for kq in n0.values())
            n2, st2 = quet_ho(kho, st1, (), None, T + 400)  # đủ năm phút: ổn định
            hh = sorted(it for kq in n2.values() for it in kq["hien_hanh"])
            ca.append(("lần quét đầu chưa công nhận, lần hai mới nhận", chua and hh == ["MoiToanh.docx", "MoiToanh.docx"]))
            ca.append(("hai thư mục trùng tên file là hai họ riêng, không xung đột",
                       len(n2) == 2 and all(not kq["xung_dot"] for kq in n2.values())))
        # g. vN dạng gạch ngang và ngoặc cũng được nhận (vá theo team agent)
        from kiem_van_hanh import ho_va_v, BAT_BIEN
        cung_ho = {ho_va_v(t)[0] for t in ["BC-v03.docx", "BC_v02.docx", "BC(v3).docx"]}
        ca.append(("(v3), -v03, _v02 về CÙNG MỘT họ chuẩn hóa",
                   len(cung_ho) == 1
                   and ho_va_v("BC(v3).docx")[1] == 3
                   and ho_va_v("Server1.docx")[1] is None
                   and ho_va_v("BC_v2abc.docx")[1] is None))
        # chuẩn hóa không được quá tay: AB_C và A_BC là HAI họ khác nhau
        ca.append(("AB_C_v01 và A_BC_v02 không bị trộn họ",
                   ho_va_v("AB_C_v01.docx")[0] != ho_va_v("A_BC_v02.docx")[0]))
        # 00_Index bị loại, nhưng script NGHIỆP VỤ ngoài 00_Index vẫn được quét
        with tempfile.TemporaryDirectory() as td3:
            kho3 = Path(td3)
            (kho3 / "00_Index").mkdir(); (kho3 / "01_A").mkdir()
            (kho3 / "00_Index" / "X5_HESO.md").write_text("luat", encoding="utf-8")
            (kho3 / "00_Index" / "kiem_he_thong.py").write_text("code", encoding="utf-8")
            (kho3 / "01_A" / "tinh_toan_v01.py").write_text("code nghiep vu", encoding="utf-8")
            (kho3 / "01_A" / "BaoCao_v01.docx").write_text("bc", encoding="utf-8")
            _, st3 = quet_ho(kho3, {}, (), None, 10_000_000.0)
            n3, _ = quet_ho(kho3, st3, (), None, 10_000_400.0)
            thay3 = sorted(it for kq in n3.values() for it in kq["hien_hanh"])
            ca.append(("00_Index bị loại, script nghiệp vụ ngoài đó vẫn được quét",
                       thay3 == ["BaoCao_v01.docx", "tinh_toan_v01.py"]))
        # dòng sổ trỏ THƯ MỤC bao phủ mọi file con
        from kiem_van_hanh import bao_phu, da_vao_so
        fs, ds = bao_phu([["P", "T-1", "Bo ho so", "v1", "1/1",
                           "Kho 01_A/Bundle\\", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
                          ["P", "T-2", "File le", "v1", "1/1",
                           "Kho 01_A/Le_v01.docx", "x", "x", "x", "x", "x", "x", "x", "x", "x"]])
        ca.append(("dòng trỏ thư mục bao phủ file con, dòng trỏ file khớp đúng file",
                   da_vao_so("01_A/Bundle/BC_v01.docx", fs, ds)
                   and da_vao_so("01_A/Le_v01.docx", fs, ds)
                   and not da_vao_so("01_A/Khac_v01.docx", fs, ds)
                   and not da_vao_so("01_A/Bundle2/BC_v01.docx", fs, ds)))
        # 98_Assets và 99_Goc PHẢI được quét (X4 kiểm sha 99_Goc); 99_Archive loại
        with tempfile.TemporaryDirectory() as td4:
            kho4 = Path(td4)
            for d in ("98_Assets", "99_Goc", "99_Archive"):
                (kho4 / d).mkdir()
            (kho4 / "98_Assets" / "Logo_v01.png").write_text("x", encoding="utf-8")
            (kho4 / "99_Goc" / "HopDong_SIGNED.pdf").write_text("goc", encoding="utf-8")
            (kho4 / "99_Archive" / "Cu_v01.docx").write_text("cu", encoding="utf-8")
            _, st4 = quet_ho(kho4, {}, (), None, 10_000_000.0)
            n4, _ = quet_ho(kho4, st4, (), None, 10_000_400.0)
            thay4 = sorted(it for kq in n4.values() for it in kq["hien_hanh"])
            ca.append(("98_Assets và 99_Goc được quét, 99_Archive bị loại",
                       thay4 == ["HopDong_SIGNED.pdf", "Logo_v01.png"]))
        # email: gọi CẢ kiem_email() trên các kịch bản hỏng, không thử lẻ từng hàm
        from kiem_van_hanh import kiem_email
        import json as _json

        import hashlib as _hl

        import contextlib, io as _io
        _verbose = "--verbose" in sys.argv

        def chay_email(nk=None, reg=None, thu_rows="", x0_hop="mail@congty.vn",
                       idx=None, files=None, don=None):
            """Dựng hệ EMAIL tạm rồi gọi TOÀN BỘ kiem_email(). files: dict
            đường dẫn tương đối từ gốc sang nội dung (staging, sổ đích...).
            Mặc định nuốt output chi tiết (LECH của tình huống ÂM là chủ ý);
            --verbose in đủ."""
            with tempfile.TemporaryDirectory() as td9:
                g9 = Path(td9); s9 = g9 / "_so"; s9.mkdir()
                if x0_hop is not None:
                    (g9 / "X0_CAUHINH_T.md").write_text(
                        f"@NHIP.HOPTHU (EMAIL) {x0_hop}\n", encoding="utf-8")
                else:
                    (g9 / "X0_CAUHINH_T.md").write_text("rong\n", encoding="utf-8")
                if nk is not None:
                    (s9 / "_thu_nhat_ky.ndjson").write_text(nk, encoding="utf-8")
                if reg is not None:
                    (s9 / "_thu_da_nap.json").write_text(_json.dumps(reg), encoding="utf-8")
                if idx is not None:
                    (s9 / "_thu_ap_dung.json").write_text(_json.dumps(idx), encoding="utf-8")
                if don is not None:
                    (s9 / "_thu_don_staging.json").write_text(_json.dumps(don), encoding="utf-8")
                for rp, nd_f in (files or {}).items():
                    f = g9 / rp
                    f.parent.mkdir(parents=True, exist_ok=True)
                    f.write_text(nd_f, encoding="utf-8")
                (s9 / "THU.md").write_text(
                    "# T\n\n| Mã | Luồng | Conversation-ID | Message-ID cuối | Trạng thái |\n"
                    "|---|---|---|---|---|\n" + thu_rows, encoding="utf-8")
                if _verbose:
                    return {t: ok for t, ok, _ in kiem_email(g9, s9)}
                with contextlib.redirect_stdout(_io.StringIO()):
                    return {t: ok for t, ok, _ in kiem_email(g9, s9)}

        ATT_SHA = _hl.sha256(b"PDF").hexdigest()
        EML_SHA = _hl.sha256(b"eml").hexdigest()
        THU_MUC_A = _hl.sha256(b"<a@x>").hexdigest()
        PAY = {"conv_id": "c1", "nguoi_gui": "doi_tac@x.vn",
               "thoi_diem": "2026-08-23T09:00:00Z", "tieu_de": "chao",
               "eml_sha256": EML_SHA,
               "staging": f"_so/_thu_staging/{THU_MUC_A}/",
               "thao_tac": [{"operation_id": "op1", "so": "VIEC",
                             "dong": "V-001", "noi_dung": "| V-001 | viec |"}],
               "dinh_kem": [{"ten": "f.pdf", "sha256": ATT_SHA, "bytes": 3}]}
        FILES_SACH = {f"_so/_thu_staging/{THU_MUC_A}/thu.eml": "eml",
                      f"_so/_thu_staging/{THU_MUC_A}/f.pdf": "PDF",
                      "_so/VIEC.md": "| V-001 | viec |\n"}
        IDX_SACH = {"<a@x>|op1": {"so": "VIEC", "dong": "V-001"}}
        P = lambda k, pay=PAY, **t: _json.dumps({"ev": "PREPARED", "khoa": k,
                                        "hop_thu": "mail@congty.vn", "payload": pay, **t})
        C = lambda k, **t: _json.dumps({"ev": "COMMITTED", "khoa": k,
                                        "hop_thu": "mail@congty.vn", **t})
        TEN_12D = "12d. registry là DANH SÁCH CHUỖI và BẰNG ĐÚNG tập khóa COMMITTED"
        TEN_12G = ("12g. mỗi khóa đúng mô hình PREPARED rồi COMMITTED, không mồ côi,"
                   " không lặp, không ngược thứ tự")
        TEN_12H = "12h. mọi PREPARED mang payload phục hồi đạt schema"
        TEN_12J = "12j. staging đúng vòng đời: còn thì đúng nội dung, vắng thì có manifest dọn"
        TEN_12K = "12k. tập mục index bằng đúng tập thao tác COMMITTED và khớp payload"
        TEN_12L = "12l. index trỏ tới mã dòng có thật trong sổ đích (so đúng ô)"
        TEN_12E = "12e. mọi mail trong nhật ký thuộc ĐÚNG hộp thư khai báo"
        # bộ SẠCH phải PASS hết
        SACH = P("<a@x>") + "\n" + C("<a@x>") + "\n"
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=IDX_SACH, files=FILES_SACH,
                       thu_rows="| #L-001 | L1 | c1 | <a@x> | CHỜ TÔI |\n")
        ca.append(("email bộ sạch PASS hết", all(r.values()) and len(r) >= 11))
        # có nhật ký, MẤT registry: phải LỆCH
        r = chay_email(nk=SACH)
        ca.append(("mất registry bị bắt", r.get("12a. nhật ký nạp và registry cùng tồn tại") is False))
        # có registry, MẤT nhật ký nguồn sự thật: phải LỆCH
        r = chay_email(reg=["<a@x>"])
        ca.append(("mất nhật ký nguồn sự thật bị bắt", r.get("12a. nhật ký nạp và registry cùng tồn tại") is False))
        # dòng rác và dòng "42" không crash, thành LỆCH
        r = chay_email(nk="DONG RAC\n42\n" + SACH, reg=["<a@x>"])
        ca.append(("dòng hỏng và không-object thành LỆCH, không crash",
                   r.get("12b. nhật ký không có dòng hỏng") is False))
        # PREPARED không COMMITTED: dở dang bị bắt
        r = chay_email(nk=P("<a@x>") + "\n", reg=[])
        ca.append(("lượt dở dang bị bắt",
                   r.get("12c. không lượt nạp nào DỞ DANG (PREPARED thiếu COMMITTED)") is False))
        # registry THỪA mã không có trong nhật ký: bị bắt
        r = chay_email(nk=SACH, reg=["<a@x>", "<ma@x>"])
        ca.append(("registry thừa mã bị bắt", r.get(TEN_12D) is False))
        # hộp thư giả chứa chuỗi đúng dạng substring: so chính xác nên bị bắt
        r = chay_email(nk=P("<g@x>") + "\n" + C("<g@x>", hop_thu="mail@congty.vn.hacker.com") + "\n",
                       reg=["<g@x>"])
        ca.append(("hộp thư giả kiểu substring bị bắt",
                   r.get("12e. mọi mail trong nhật ký thuộc ĐÚNG hộp thư khai báo") is False))
        # khóa fallback KHÔNG có dấu @ đứng cuối hai luồng: vẫn bị bắt
        r = chay_email(nk=SACH, reg=["<a@x>"],
                       thu_rows="| #L-001 | L1 | c1 | FBKEY-123 | CHỜ TÔI |\n"
                                "| #L-002 | L2 | c2 | FBKEY-123 | CHỜ TÔI |\n")
        ca.append(("khóa fallback không @ trùng hai luồng bị bắt",
                   r.get("12f. không khóa nào đứng cuối ở HAI luồng THU") is False))
        # PREPARED KHÔNG payload (chỉ tên với dung lượng) rồi COMMITTED: bị bắt
        p_hut = _json.dumps({"ev": "PREPARED", "khoa": "<a@x>", "hop_thu": "mail@congty.vn",
                             "payload": {"ten": "f.pdf", "bytes": 1234}})
        r = chay_email(nk=p_hut + "\n" + C("<a@x>") + "\n", reg=["<a@x>"])
        ca.append(("PREPARED thiếu payload phục hồi bị bắt (dù đã COMMITTED)",
                   r.get(TEN_12H) is False))
        # đính kèm de_ngoai HỢP LỆ (ten + ly_do, không sha256): 12h phải PASS
        # và 12j không đòi file trong staging (X3E mục 2); chạy ngược trên v22
        # thì 12h FAIL oan - fixture này giữ cho máy khỏi đá luật lần nữa
        pay_dn = dict(PAY, dinh_kem=[{"ten": "video.mp4", "de_ngoai": True,
                                      "ly_do": "vượt trần 50MB"}])
        r = chay_email(nk=P("<a@x>", pay=pay_dn) + "\n" + C("<a@x>") + "\n",
                       reg=["<a@x>"], files=FILES_SACH, idx=IDX_SACH)
        ca.append(("đính kèm de_ngoai hợp lệ không bị 12h/12j báo oan",
                   r.get(TEN_12H) is not False and r.get(TEN_12J) is not False))
        # de_ngoai THIẾU ly_do: phải LỆCH schema
        pay_dn2 = dict(PAY, dinh_kem=[{"ten": "video.mp4", "de_ngoai": True}])
        r = chay_email(nk=P("<a@x>", pay=pay_dn2) + "\n" + C("<a@x>") + "\n",
                       reg=["<a@x>"], files=FILES_SACH, idx=IDX_SACH)
        ca.append(("đính kèm de_ngoai thiếu ly_do bị bắt", r.get(TEN_12H) is False))
        # COMMITTED không có PREPARED (mồ côi): bị bắt
        r = chay_email(nk=C("<a@x>") + "\n", reg=["<a@x>"])
        ca.append(("COMMITTED mồ côi bị bắt", r.get(TEN_12G) is False))
        # COMMITTED đứng TRƯỚC PREPARED: bị bắt
        r = chay_email(nk=C("<a@x>") + "\n" + P("<a@x>") + "\n", reg=["<a@x>"])
        ca.append(("COMMITTED đứng trước PREPARED bị bắt", r.get(TEN_12G) is False))
        # ev gõ sai "TYPO": dòng hỏng, KHÔNG được coi như COMMITTED
        typo = _json.dumps({"ev": "TYPO", "khoa": "<t@x>", "hop_thu": "mail@congty.vn"})
        r = chay_email(nk=typo + "\n" + SACH, reg=["<a@x>"])
        ca.append(("ev lạ thành dòng hỏng, không thành COMMITTED",
                   r.get("12b. nhật ký không có dòng hỏng") is False
                   and r.get(TEN_12D) is not False))
        # sự kiện THIẾU hop_thu: dòng hỏng
        thieu_hop = _json.dumps({"ev": "COMMITTED", "khoa": "<h@x>"})
        r = chay_email(nk=P("<h@x>") + "\n" + thieu_hop + "\n" + SACH, reg=["<a@x>"])
        ca.append(("sự kiện thiếu hop_thu thành dòng hỏng",
                   r.get("12b. nhật ký không có dòng hỏng") is False))
        # hai dòng THU cùng Conversation-ID: bị bắt
        r = chay_email(nk=SACH, reg=["<a@x>"],
                       thu_rows="| #L-001 | L1 | convA | <a@x> | CHỜ TÔI |\n"
                                "| #L-002 | L2 | convA | <b@x> | THEO DÕI |\n")
        ca.append(("Conversation-ID trùng hai dòng THU bị bắt",
                   r.get("12i. Conversation-ID duy nhất trong THU") is False))
        # registry là {} thay vì danh sách: LỆCH, không PASS
        r = chay_email(nk=SACH, reg={})
        ca.append(("registry dạng object rỗng bị bắt", r.get(TEN_12D) is False))
        # registry là danh sách chứa OBJECT: LỆCH, không crash
        r = chay_email(nk=SACH, reg=[{"msgId": "<a@x>"}])
        ca.append(("registry chứa object thành LỆCH, không crash", r.get(TEN_12D) is False))
        # khóa là ARRAY thay vì chuỗi: dòng hỏng, không crash
        arr = _json.dumps({"ev": "COMMITTED", "khoa": ["<a@x>"], "hop_thu": "mail@congty.vn"})
        r = chay_email(nk=arr + "\n" + SACH, reg=["<a@x>"])
        ca.append(("khóa dạng array thành dòng hỏng, không crash",
                   r.get("12b. nhật ký không có dòng hỏng") is False))
        # trường msgId kiểu cũ: dòng hỏng, phải migration, không đọc lẫn
        cu = _json.dumps({"ev": "COMMITTED", "msgId": "<m@x>", "hop_thu": "mail@congty.vn"})
        r = chay_email(nk=cu + "\n" + SACH, reg=["<a@x>"])
        ca.append(("trường msgId kiểu cũ thành dòng hỏng chờ migration",
                   r.get("12b. nhật ký không có dòng hỏng") is False
                   and r.get(TEN_12D) is not False))
        # staging chấm chấm thoát ra ngoài: schema payload bắt
        pay_thoat = dict(PAY, staging="../../outside/")
        r = chay_email(nk=P("<a@x>", pay=pay_thoat) + "\n" + C("<a@x>") + "\n", reg=["<a@x>"])
        ca.append(("staging thoát ra ngoài _thu_staging bị bắt", r.get(TEN_12H) is False))
        # thao_tac là [42]: bị bắt, không crash
        r = chay_email(nk=P("<a@x>", pay=dict(PAY, thao_tac=[42])) + "\n" + C("<a@x>") + "\n",
                       reg=["<a@x>"])
        ca.append(("thao tác không phải object bị bắt", r.get(TEN_12H) is False))
        # thao tác {} rỗng: bị bắt
        r = chay_email(nk=P("<a@x>", pay=dict(PAY, thao_tac=[{}])) + "\n" + C("<a@x>") + "\n",
                       reg=["<a@x>"])
        ca.append(("thao tác rỗng thiếu trường bị bắt", r.get(TEN_12H) is False))
        # hai thao tác trùng operation_id: bị bắt
        t1 = {"operation_id": "op1", "so": "VIEC", "dong": "V-001", "noi_dung": "x"}
        r = chay_email(nk=P("<a@x>", pay=dict(PAY, thao_tac=[t1, dict(t1)])) + "\n"
                       + C("<a@x>") + "\n", reg=["<a@x>"])
        ca.append(("operation_id trùng trong một mail bị bắt", r.get(TEN_12H) is False))
        # thiếu cấu hình @NHIP.HOPTHU khi EMAIL đã chạy: LỆCH, không BỎ QUA
        r = chay_email(nk=SACH, reg=["<a@x>"], x0_hop=None)
        ca.append(("thiếu @NHIP.HOPTHU thành LỆCH cấu hình", r.get(TEN_12E) is False))
        # staging khai trong payload nhưng KHÔNG tồn tại trên đĩa: bị bắt
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=IDX_SACH,
                       files={"_so/VIEC.md": "| V-001 | viec |\n"})
        ca.append(("staging không tồn tại trên đĩa bị bắt", r.get(TEN_12J) is False))
        # đính kèm sai sha256: bị bắt
        files_sai = dict(FILES_SACH); files_sai[f"_so/_thu_staging/{THU_MUC_A}/f.pdf"] = "KHAC"
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=IDX_SACH, files=files_sai)
        ca.append(("đính kèm sai sha256 hay byte bị bắt", r.get(TEN_12J) is False))
        # mail COMMITTED nhưng thao tác vắng trong index: bị bắt
        r = chay_email(nk=SACH, reg=["<a@x>"], idx={}, files=FILES_SACH)
        ca.append(("thao tác COMMITTED vắng trong index bị bắt", r.get(TEN_12K) is False))
        # index trỏ mail không có trong nhật ký: bị bắt
        idx_la = dict(IDX_SACH); idx_la["<la@x>|op9"] = {"so": "VIEC", "dong": "V-009"}
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=idx_la, files=FILES_SACH)
        ca.append(("index trỏ mail lạ bị bắt", r.get(TEN_12K) is False))
        # index trỏ mã dòng không tồn tại trong sổ đích: bị bắt
        idx_sai = {"<a@x>|op1": {"so": "VIEC", "dong": "V-999"}}
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=idx_sai, files=FILES_SACH)
        ca.append(("index trỏ mã dòng không có thật bị bắt", r.get(TEN_12L) is False))
        # staging "../_so/_thu_staging/K/": normpath vẫn phải chặn
        pay_lach = dict(PAY, staging=f"../_so/_thu_staging/{THU_MUC_A}/")
        r = chay_email(nk=P("<a@x>", pay=pay_lach) + "\n" + C("<a@x>") + "\n", reg=["<a@x>"])
        ca.append(("staging lách bằng ../_so bị normpath chặn", r.get(TEN_12H) is False))
        # tên đính kèm mang đường dẫn thoát staging: schema bắt
        pay_ten = dict(PAY, dinh_kem=[{"ten": "../../../secret.txt",
                                       "sha256": ATT_SHA, "bytes": 3}])
        r = chay_email(nk=P("<a@x>", pay=pay_ten) + "\n" + C("<a@x>") + "\n", reg=["<a@x>"])
        ca.append(("tên đính kèm mang đường dẫn bị bắt", r.get(TEN_12H) is False))
        # payload thiếu metadata nguồn (conv_id): bị bắt
        pay_thieu = {t: v for t, v in PAY.items() if t != "conv_id"}
        r = chay_email(nk=P("<a@x>", pay=pay_thieu) + "\n" + C("<a@x>") + "\n", reg=["<a@x>"])
        ca.append(("payload thiếu metadata nguồn bị bắt", r.get(TEN_12H) is False))
        # staging dùng chung thư mục (tên khác sha256 của khóa): bị bắt
        pay_chung = dict(PAY, staging="_so/_thu_staging/chung/")
        r = chay_email(nk=P("<a@x>", pay=pay_chung) + "\n" + C("<a@x>") + "\n", reg=["<a@x>"])
        ca.append(("thư mục staging không phải sha256(khóa) bị bắt", r.get(TEN_12H) is False))
        # .eml rỗng: bị bắt
        files_rong = dict(FILES_SACH); files_rong[f"_so/_thu_staging/{THU_MUC_A}/thu.eml"] = ""
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=IDX_SACH, files=files_rong)
        ca.append((".eml hay body rỗng bị bắt", r.get(TEN_12J) is False))
        # .eml không khớp eml_sha256: bị bắt
        files_khac = dict(FILES_SACH); files_khac[f"_so/_thu_staging/{THU_MUC_A}/thu.eml"] = "khac"
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=IDX_SACH, files=files_khac)
        ca.append((".eml không khớp eml_sha256 bị bắt", r.get(TEN_12J) is False))
        # index THỪA mục không có trong thao tác payload: bị bắt
        idx_thua = dict(IDX_SACH); idx_thua["<a@x>|opX"] = {"so": "VIEC", "dong": "V-001"}
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=idx_thua, files=FILES_SACH)
        ca.append(("index thừa mục ngoài payload bị bắt", r.get(TEN_12K) is False))
        # index trỏ dòng KHÁC payload nhưng dòng đó có thật: vẫn bị bắt
        files_2d = dict(FILES_SACH); files_2d["_so/VIEC.md"] = "| V-001 | a |\n| V-002 | b |\n"
        idx_lech = {"<a@x>|op1": {"so": "VIEC", "dong": "V-002"}}
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=idx_lech, files=files_2d)
        ca.append(("index trỏ dòng có thật nhưng khác payload bị bắt", r.get(TEN_12K) is False))
        # mã V-1 không được ăn theo V-10: so đúng ô
        pay_v1 = dict(PAY, thao_tac=[{"operation_id": "op1", "so": "VIEC",
                                      "dong": "V-1", "noi_dung": "| V-1 | x |"}])
        files_v10 = dict(FILES_SACH); files_v10["_so/VIEC.md"] = "| V-10 | x |\n"
        r = chay_email(nk=P("<a@x>", pay=pay_v1) + "\n" + C("<a@x>") + "\n", reg=["<a@x>"],
                       idx={"<a@x>|op1": {"so": "VIEC", "dong": "V-1"}}, files=files_v10)
        ca.append(("V-1 không ăn theo V-10, so đúng ô", r.get(TEN_12L) is False))
        # staging ĐÃ DỌN đúng luật (COMMITTED, manifest hợp lệ): PASS
        DON_OK = {"<a@x>": {"purged_at": "2026-09-23T09:00:00Z",
                            "eml_final_path": "04_Trao_doi/mail_a.eml",
                            "attachment_final_paths": ["04_Trao_doi/f.pdf"],
                            "sha256": EML_SHA}}
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=IDX_SACH,
                       files={"_so/VIEC.md": "| V-001 | viec |\n"}, don=DON_OK)
        ca.append(("staging đã dọn có manifest hợp lệ là PASS", r.get(TEN_12J) is True))
        # staging vắng khi CHƯA COMMITTED: manifest cũng không cứu được
        r = chay_email(nk=P("<a@x>") + "\n", reg=[], don=DON_OK)
        ca.append(("staging vắng khi chưa COMMITTED vẫn lệch", r.get(TEN_12J) is False))
        # schema THU đủ cột then chốt
        thu_nd = docs["_so/THU.md"]
        ca.append(("THU đủ cột Conversation-ID, Message-ID cuối, Trạng thái, Chờ từ",
                   all(c in thu_nd for c in ["Conversation-ID", "Message-ID cuối",
                                             "Trạng thái", "Chờ từ", "Nhắc lại ngày"])))
        # file nghiệp vụ ngoài 7 đuôi cũ (kmz, csv) phải được quét
        with tempfile.TemporaryDirectory() as td2:
            kho2 = Path(td2); (kho2 / "01_A").mkdir()
            (kho2 / "01_A" / "Tuyen_v01.kmz").write_text("kml", encoding="utf-8")
            (kho2 / "01_A" / "SoLieu.csv").write_text("a,b", encoding="utf-8")
            n_a, st_a = quet_ho(kho2, {}, (), None, 10_000_000.0)
            n_b, _ = quet_ho(kho2, st_a, (), None, 10_000_400.0)
            thay = sorted(it for kq in n_b.values() for it in kq["hien_hanh"])
            ca.append(("kmz và csv được quan sát", thay == ["SoLieu.csv", "Tuyen_v01.kmz"]))
        # chế độ --ho: selector và vòng đời cache (v23, sửa lỗi thực thi của v22)
        from kiem_van_hanh import (giai_ho, khoa_ho_cua, quan_sat_kho, tach_tham_so,
                                   nap_cache, KHOANG_ON_DINH)
        import json as _js
        DU = KHOANG_ON_DINH + 60  # đủ xa mốc ổn định

        def qs(*a, **k):
            """Gọi quan_sat_kho, nuốt output chi tiết như các fixture khác."""
            if _verbose:
                return quan_sat_kho(*a, **k)
            with contextlib.redirect_stdout(_io.StringIO()):
                return quan_sat_kho(*a, **k)

        def _kho_ho(td):
            """Kho mẫu: hai họ trong 01_A, một họ TRÙNG TÊN ở 02_B."""
            kho = Path(td)
            (kho / "01_A").mkdir(); (kho / "02_B").mkdir()
            (kho / "01_A" / "BC_v01.docx").write_text("bc1", encoding="utf-8")
            (kho / "01_A" / "BC_v02.docx").write_text("bc2", encoding="utf-8")
            (kho / "01_A" / "KHAC_v01.docx").write_text("khac", encoding="utf-8")
            (kho / "02_B" / "BC_v01.docx").write_text("bc du an khac", encoding="utf-8")
            return kho

        def _so_rong(kho):
            so = kho / "00_Index" / "_so"
            so.mkdir(parents=True, exist_ok=True)
            (so / "TAILIEU.md").write_text("", encoding="utf-8")
            return so

        # a. selector: truyền v01 phải kéo THEO CẢ HỌ, đúng thư mục, không kéo họ khác
        with tempfile.TemporaryDirectory() as td:
            kho = _kho_ho(td)
            k = giai_ho(kho, "01_A/BC_v01.docx")
            _, moi = quet_ho(kho, {}, (), k, 0)
            ca.append(("--ho v01 kéo theo v02 cùng họ, không kéo họ khác, không kéo dự án khác",
                       sorted(moi) == ["01_A/BC_v01.docx", "01_A/BC_v02.docx"]))
            ca.append(("--ho suy đúng khóa (thư mục, họ) từ một file",
                       k == khoa_ho_cua("01_A/BC_v02.docx") != khoa_ho_cua("02_B/BC_v01.docx")))
            # b. thư mục và tên họ trơ KHÔNG còn được nhận: phạm vi từng mơ hồ
            for xau in ("01_A", "BC.docx", "BC_v01.docx", "", "khong_co.docx",
                        "../ngoai_kho.docx"):
                try:
                    giai_ho(kho, xau); chan = False
                except ValueError:
                    chan = True
                if not chan:
                    break
            ca.append(("--ho từ chối thư mục, tên họ trơ, rỗng, file lạ và đường ra ngoài kho",
                       chan))

        # c. hai lần quét SÁT NHAU không được công nhận ổn định, kể cả chế độ --ho
        with tempfile.TemporaryDirectory() as td:
            kho = _kho_ho(td); so = _so_rong(kho)
            t0 = 1_000_000.0
            qs(kho / "00_Index", so, kho, "01_A/BC_v01.docx", t0)
            qs(kho / "00_Index", so, kho, "01_A/BC_v01.docx", t0 + 10)
            n_som, _ = quet_ho(kho, nap_cache(so / "_quan_sat_truoc.json")[0], (),
                               khoa_ho_cua("01_A/BC_v01.docx"), t0 + 20)
            som = all(not kq["hien_hanh"] for kq in n_som.values())
            n_du, _ = quet_ho(kho, nap_cache(so / "_quan_sat_truoc.json")[0], (),
                              khoa_ho_cua("01_A/BC_v01.docx"), t0 + DU)
            du = [it for kq in n_du.values() for it in kq["hien_hanh"]] == ["BC_v02.docx"]
            ca.append(("--ho quét lại ngay KHÔNG thành ổn định, chờ đủ năm phút mới nhận",
                       som and du))

        # d. file đổi nội dung phải reset mốc, không ăn theo lần quan sát cũ
        with tempfile.TemporaryDirectory() as td:
            kho = _kho_ho(td); so = _so_rong(kho)
            t0 = 2_000_000.0
            qs(kho / "00_Index", so, kho, "01_A/BC_v01.docx", t0)
            (kho / "01_A" / "BC_v02.docx").write_text("noi dung MOI", encoding="utf-8")
            n, _ = quet_ho(kho, nap_cache(so / "_quan_sat_truoc.json")[0], (),
                           khoa_ho_cua("01_A/BC_v01.docx"), t0 + DU)
            cho = sorted(it for kq in n.values() for it in kq["khong_xac_dinh"])
            hh = sorted(it for kq in n.values() for it in kq["hien_hanh"])
            ca.append(("file vừa đổi nội dung mất mốc cũ, phải chờ lại từ đầu",
                       cho == ["BC_v02.docx"] and "BC_v02.docx" not in hh))

        # e. cache: xóa file khỏi họ thì mục cũ biến mất, họ khác giữ nguyên
        with tempfile.TemporaryDirectory() as td:
            kho = _kho_ho(td); so = _so_rong(kho)
            cache = so / "_quan_sat_truoc.json"
            t0 = 3_000_000.0
            qs(kho / "00_Index", so, kho, None, t0)          # quét cả kho
            (kho / "01_A" / "BC_v01.docx").unlink()
            qs(kho / "00_Index", so, kho, "01_A/BC_v02.docx", t0 + DU)
            con = set(_js.loads(cache.read_text(encoding="utf-8"))["files"])
            ca.append(("cache bỏ file đã xóa khỏi họ, giữ nguyên các họ khác",
                       "01_A/BC_v01.docx" not in con
                       and {"01_A/BC_v02.docx", "01_A/KHAC_v01.docx",
                            "02_B/BC_v01.docx"} <= con))

        # f. không khớp file nào là LỆCH, không PASS im lặng
        with tempfile.TemporaryDirectory() as td:
            kho = _kho_ho(td); so = _so_rong(kho)
            import kiem_van_hanh as _kvh
            truoc_loi = len(_kvh.loi)
            qs(kho / "00_Index", so, kho, "01_A/khong_ton_tai.docx", 4_000_000.0)
            ca.append(("--ho không khớp file nào thì LỆCH, không PASS im lặng",
                       len(_kvh.loi) > truoc_loi))
            del _kvh.loi[truoc_loi:]

        # f2. dòng TAILIEU trỏ THƯ MỤC vẫn bao phủ file con trong chế độ --ho
        #     (v23 lọc dòng sổ theo họ TRƯỚC khi tính bao phủ nên đề xuất oan)
        with tempfile.TemporaryDirectory() as td:
            kho = _kho_ho(td); so = _so_rong(kho)
            (so / "TAILIEU.md").write_text(
                "# T\n\n| Loai | Ma | Ten | Ban | Ngay | Kho |\n|---|---|---|---|---|---|\n"
                "| P | T-1 | Bo ho so 01_A | v1 | 1/1 | Kho 01_A/ |\n", encoding="utf-8")
            t0 = 5_000_000.0
            qs(kho / "00_Index", so, kho, "01_A/BC_v01.docx", t0)
            with contextlib.redirect_stdout(_io.StringIO()) as _ra:
                quan_sat_kho(kho / "00_Index", so, kho, "01_A/BC_v01.docx", t0 + DU)
            ra = _ra.getvalue()
            if _verbose:
                print(ra, end="")
            ca.append(("dòng Kho trỏ thư mục bao phủ file con cả trong chế độ --ho",
                       "_INBOX" not in ra and "BC_v02.docx" not in ra))

        # f3. cache đời cũ (không có "v": 2) không được mang theo bằng chứng ổn định
        with tempfile.TemporaryDirectory() as td:
            kho = _kho_ho(td); so = _so_rong(kho)
            sha_cu = {r: __import__("kiem_van_hanh").sha_file(kho / r)
                      for r in ("01_A/BC_v01.docx", "01_A/BC_v02.docx")}
            (so / "_quan_sat_truoc.json").write_text(
                _js.dumps({"luc": 1000.0, "files": sha_cu}), encoding="utf-8")
            with contextlib.redirect_stdout(_io.StringIO()):
                nap, _ = nap_cache(so / "_quan_sat_truoc.json", 6_000_000.0)
            n, _ = quet_ho(kho, nap, (), khoa_ho_cua("01_A/BC_v01.docx"), 6_000_010.0)
            ca.append(("cache đời cũ bị đóng dấu lại, không nhận ổn định ngay",
                       all(not kq["hien_hanh"] for kq in n.values())))

        # g. thiếu giá trị sau --ho là lỗi cách dùng, không âm thầm quét cả kho
        try:
            tach_tham_so(["00_Index", "/kho", "--ho"]); thieu = False
        except ValueError:
            thieu = True
        ca.append(("thiếu giá trị sau --ho báo lỗi cách dùng",
                   thieu and tach_tham_so(["00_Index", "/kho", "--ho", "01_A/BC_v01.docx"])
                   == (["00_Index", "/kho"], "01_A/BC_v01.docx")))
        # h. tuple BAT_BIEN của code khớp luật X5 "từ ĐÃ GỬI DUYỆT trở đi"
        du_bb = all(t in BAT_BIEN for t in ["ĐÃ GỬI DUYỆT", "ĐÃ DUYỆT NỘI BỘ",
                                            "ĐÃ PHÁT HÀNH", "ĐÃ NỘP", "TRẢ HỒ SƠ",
                                            "ĐÃ KÝ", "ĐÃ CẤP"])
        ca.append(("BAT_BIEN đủ mọi trạng thái từ ĐÃ GỬI DUYỆT trở đi", du_bb))
        hong = [t for t, ok in ca if not ok]
        # số ca lấy từ chính danh sách, khỏi lệch nhãn khi thêm bớt fixture
        kiem(f"11. fixture bộ quan sát ({len(ca)} ca)", not hong, str(hong))
    except Exception as e:
        kiem("11. fixture bộ quan sát", False, f"lỗi chạy: {e}")

    # 12. Luật nghiệp vụ then chốt phải có mặt trong X5 và X3 (chống rơi khi rút gọn)
    x5nd = docs["X5_HESO_TEMPLATE.md"]
    thieu_luat = [t for t, dk in [
        ("im lặng không suy đã duyệt", "không bao giờ suy" in x5nd and "im lặng" in x5nd.lower()),
        ("gửi duyệt là ảnh chụp, việc tiếp trên vN+1", "ẢNH" in x5nd and "vN+1" in x5nd),
        ("bất biến chỉ cho phát hành nộp ký cấp", "ĐÃ PHÁT HÀNH" in x5nd),
        ("GHI MỐC không đóng plan", "GHI MỐC" in x5nd and "KHÔNG chốt" in x5nd),
        ("XUNG ĐỘT cấm tự chọn", "XUNG ĐỘT" in x5nd),
        ("sự kiện người dùng ghi mức A hồi tố", "không xin phép hồi tố" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("registry Message-ID chống nạp trùng", "_thu_da_nap.json" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("chờ đối tác cần bằng chứng mong phản hồi", "BẰNG CHỨNG" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("chạy lại digest sau lỗi là hợp lệ", "lần lỗi là hợp lệ" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("nhật ký nạp mail append-only dựng lại được registry", "_thu_nhat_ky" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("mất cả registry lẫn nhật ký thì chỉ đề xuất, không tự nạp", "ỨNG VIÊN" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("nhật ký sự kiện PREPARED/COMMITTED kèm payload phục hồi", "PREPARED" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "PAYLOAD PHỤC HỒI" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("ghi sổ idempotent theo khóa + operation_id", "khoa + operation_id" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("registry chỉ dựng từ COMMITTED", "CHỈ dựng từ" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) or "registry CHỈ dựng" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("fallback thiếu Message-ID đủ mạnh và duy nhất", "tiêu đề chuẩn hóa" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "khóa nào khác" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("staging bền vững lưu TRƯỚC khi append PREPARED", "STAGING trước, PREPARED sau" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "_thu_staging" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("index áp thao tác cho ghi idempotent, sổ người đọc không mang khóa máy", "_thu_ap_dung" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "operation_id" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("mỗi mail đúng hai sự kiện, PREPARED đứng trước, COMMITTED không mồ côi", "đúng HAI sự kiện" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "COMMITTED không có PREPARED" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("Conversation-ID duy nhất một dòng THU", "MỘT dòng THU" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("registry là danh sách chuỗi khóa", "DANH SÁCH CHUỖI" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("khóa một dạng duy nhất, msgId kiểu cũ chỉ qua migration", '"khoa" DUY NHẤT' in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "migration" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("khóa fallback serialize cố định FB-sha256", "FB-<sha256(" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("index đối chiếu sổ trước ghi sau, đóng khe chết giữa ghi sổ và ghi index", "ĐỐI CHIẾU trước ghi sau" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "CHỈ bổ sung index" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("staging dọn mức A theo bốn điều kiện, có thời gian đệm", "DỌN STAGING" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "@NHIP.DEMSTAGING" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("staging mỗi mail một thư mục tên sha256 của khóa", "sha256(khóa)" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("tên đính kèm basename thuần, không thoát đường dẫn", "BASENAME thuần" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("manifest dọn ghi trước khi xóa staging", "MANIFEST DỌN" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "_thu_don_staging" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("sau COMMITTED index bằng đúng tập thao tác payload", "không thừa không thiếu" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("CHỜ TÔI đủ năm điều, yêu cầu phải nhắm vào mình từ phần vừa viết", "đủ NĂM điều" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "NHẮM VÀO MÌNH" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("digest chống lặp bằng khóa nội dung, không phải khóa ngày", "khóa NỘI DUNG" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("digest có khuôn trình bày bắt buộc đúng thứ tự", "KHUÔN BẮT BUỘC" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "LÀM GÌ" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("tên và bí danh người dùng khai ở @NHIP.TENGOI, tự lấy khi cài", "@NHIP.TENGOI" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "@NHIP.TENGOI" in docs["X0_CAUHINH_TEMPLATE.md"]),
        ("giờ quét thật đọc từ nguồn @NHIP.TRANGTHAI khai ở X0", "@NHIP.TRANGTHAI" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "@NHIP.TRANGTHAI" in docs["X0_CAUHINH_TEMPLATE.md"]),
        ("tình trạng dữ liệu và việc quá hạn nằm TRONG hash, cảnh báo cũ gửi một lần", "PHẢI nằm trong hash" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"]) and "MỘT lần" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
        ("đã cũ định nghĩa tất định: chưa quét trong phiên hiện tại", "TẤT ĐỊNH" in docs["X5_HESO_TEMPLATE.md"] and "PHIÊN hiện tại" in docs["X5_HESO_TEMPLATE.md"]),
        ("schema @NHIP.TRANGTHAI bắt buộc, FAILED hay thiếu coi là dữ liệu cũ", "last_success_utc" in docs["X0_CAUHINH_TEMPLATE.md"] and "DỮ LIỆU CŨ" in docs["X0_CAUHINH_TEMPLATE.md"]),
        ("khóa digest đã gửi lưu bền ở @NHIP.DAUGUI, ghi sau xác nhận", "@NHIP.DAUGUI" in docs["X0_CAUHINH_TEMPLATE.md"] and "@NHIP.DAUGUI" in (docs["X3_CUAVAO_TEMPLATE.md"] + docs["X3E_EMAIL_TEMPLATE.md"])),
    ] if not dk]
    kiem("12. luật nghiệp vụ then chốt có mặt (37 luật)", not thieu_luat, str(thieu_luat))

    # 10. Tham chiếu chéo "X<k> mục <n>" và "INSTRUCTION mục <n>" phải trỏ tới mục có thật
    muc_cua = {}
    for k in ["X1_CAM_TEMPLATE.md", "X2_PHATHANH_TEMPLATE.md", "X3_CUAVAO_TEMPLATE.md",
              "X4_RASOAT_TEMPLATE.md", "X5_HESO_TEMPLATE.md"]:
        muc_cua["X" + k[1]] = set(re.findall(r"^# (\d+)\.", docs[k], re.M))
    muc_cua["X3E"] = set(re.findall(r"^# (\d+)\.", docs["X3E_EMAIL_TEMPLATE.md"], re.M))
    muc_cua["INSTRUCTION"] = set(re.findall(r"^# (\d+)\.", docs["INSTRUCTION"], re.M))
    sai_ref = []
    for ten, nd in docs.items():
        for dich, n in re.findall(r"(X[1-5]E?|INSTRUCTION) mục (\d+)", nd):
            if n not in muc_cua.get(dich, set()):
                sai_ref.append((ten, f"{dich} mục {n}"))
    kiem("10. tham chiếu chéo tới mục có thật", not sai_ref, str(sorted(set(sai_ref))))

    # 8. Bản gộp _GOP: BẮT BUỘC ở chế độ đóng gói, chứa nguyên văn từng file
    gop = sorted(goc.parent.glob(goc.name + "_GOP.md")) + sorted(goc.glob("*_GOP.md"))
    if "--gop" in sys.argv:
        try:
            gop = [Path(sys.argv[sys.argv.index("--gop") + 1])]
        except IndexError:
            gop = []
    if gop:
        nd_gop = gop[0].read_text(encoding="utf-8")
        thieu_gop = [t for t, nd in docs.items()
                     if t != "INSTRUCTION" and nd.strip() and nd.strip() not in nd_gop]
        if docs["INSTRUCTION"].strip() not in nd_gop:
            thieu_gop.append(instr[0].name)
        thieu_gop += [t for t, nd in kem.items() if nd.strip() and nd.strip() not in nd_gop]
        kiem("8. bản gộp _GOP chứa nguyên văn mọi file", not thieu_gop, f"lệch {thieu_gop}")
    elif "--skip-gop" in sys.argv:
        print("  BỎ QUA  8. theo cờ --skip-gop (không được dùng khi đóng gói phát hành)")
    else:
        kiem("8. bản gộp _GOP tồn tại cạnh thư mục bộ", False,
             "không thấy; đóng gói bắt buộc có _GOP, hoặc truyền --skip-gop tường minh")

    print()
    if loi:
        print(f"KẾT QUẢ: {len(loi)} phép kiểm FAIL. Chưa được đóng gói.")
        sys.exit(1)
    print("KẾT QUẢ: sạch, đóng gói được.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cách chạy: python3 kiem_tra_bo.py <thư mục bộ starter> [--skip-gop] [--gop <file>] [--verbose]")
        sys.exit(2)
    main(sys.argv[1])
