#!/usr/bin/env python3
# kiem_tra_bo.py · bộ test hồi quy cho WORKOPS STARTER · v21 · 20260825
# v21 bộ kiểm: thêm hai fixture de_ngoai và một fixture DƯƠNG hộp cũ
# @NHIP.HOPTHU_CU, tổng 69 ca; v27 thêm 3 ca bộ lọc bản sao và 1 ca kho sau
# XÓA PHÁP LÝ phải sạch; vòng 34 thêm 2 ca (cùng-tiền-tố, 12l-tombstone), vòng 35 thêm 1 ca đa-tiền-tố, vòng 36 thêm 2 ca 12l khuôn trọn, vòng 37 thêm 2 ca 12l so-đúng-ô, vòng 39 thêm 2 ca schema X3E, vòng 40 thêm 6 ca cho ba quyết định của rà 0d, 0g, 0i, tổng 88 ca. Trước đó v20 66 ca. Một dòng "Kho 01_A/" phải bao phủ
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
    "README.md",
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
    "X0_CAUHINH_TEMPLATE.md": 20000,  # đọc THEO MỤC (thuế thật là X0_INDEX ~228): nâng vòng 41, gate sẵn có
    "X1_CAM_TEMPLATE.md": 3200,
    "X2_PHATHANH_TEMPLATE.md": 4200,
    "X3_CUAVAO_TEMPLATE.md": 5500,   # 5b gate khi dán chat; nâng vòng 37: phần tăng nằm trọn trong 5b gated
    "X3E_EMAIL_TEMPLATE.md": 13000,  # gate: chỉ nạp khi bật EMAIL; nay 92,3% trần
    "X4_RASOAT_TEMPLATE.md": 5500,  # chỉ đọc khi RA_SOAT, không phải thuế thường trực
    "X5_HESO_TEMPLATE.md": 20000,  # mục 1b và 7b đều gate; nâng vòng 43 theo quy ước (headroom 98,1% là nợ)
    "X9_CAIDAT.md": 8500,  # gate: đọc MỘT LẦN mỗi công ty, KHÔNG nạp vào CHAT, ngoài mọi route
    "README.md": 9000,  # file người dùng đọc ĐẦU TIÊN: dài là mất người trước khi cài xong
    "WORKOPS_STARTER_v24_20260824_GOP.md": 400000,  # bản gộp để đánh giá, KHÔNG nạp vào phiên nào
    "kiem_tra_bo.py": 110000,   # ngoài mọi route, nhưng vào _GOP; lưới của lưới tốn chỗ
    "kiem_van_hanh.py": 104000,  # ngoài route, nhưng ĐẦU RA dán vào phiên RA_SOAT
    "_so/X0_INDEX.md": 1500,
    "_so/BANG_DIEU_KHIEN.md": 1400,
}
KY_TU_CAM = ["—", "–", "→", "←", "≈"] + [chr(c) for c in range(0x20)
             if chr(c) not in "\n\t\r"]  # em/en-dash, mũi tên, xấp xỉ, control char
# control char: hội đồng vòng 2 bắt được backspace 0x08 lọt vào đường dẫn
# backup của X5 do escape bị nuốt khi soạn; dò cả dải để lớp lỗi này tuyệt chủng
NL = chr(10)


def _ghi(f, nd):
    f.write_text(nd, encoding="utf-8", newline=NL)


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
    x5m1 = _muc(x5, 1, '1b')  # mục 1 thuần, không nuốt mục 1b gate phần mềm
    x1m34 = _muc(x1, 3, 5)
    t = lambda n: round(n / 3)
    tong_bo = sum(len(docs[k]) for k in
                  ["X0_CAUHINH_TEMPLATE.md", "X1_CAM_TEMPLATE.md",
                   "X2_PHATHANH_TEMPLATE.md", "X3_CUAVAO_TEMPLATE.md",
                   "X4_RASOAT_TEMPLATE.md", "X5_HESO_TEMPLATE.md",
                   "X9_CAIDAT.md"]) + len(docs["INSTRUCTION"])
    return {
        "thêm mục 1b": t(_muc(x5, "1b", 2)),
        "thêm X5 mục 3": t(_muc(x5, 3, 4)),
        # CHAT không nạp X9 (đọc một lần khi cài) và X4 (chỉ đọc khi RA_SOAT,
        # mà pilot đo được RA_SOAT thực tế trả 0 token vì chạy script)
        "CHAT không EMAIL": t(tong_bo - len(docs["X9_CAIDAT.md"]) - len(x4)),
        "CHAT có EMAIL": t(tong_bo - len(docs["X9_CAIDAT.md"]) - len(x4) + len(x3e)),
        "CHAT nạp cả X9 và X4": t(tong_bo),
        "NOI_BO mức A": t(x5m1 + x1m34),
        "CUA_VAO thường": t(_muc(x3, 1, 6) - _muc(x3, '5b', 6) + x5m1),
        "CUA_VAO thường của LITE": t(_muc(x3, 1, '5b')),
        "X0_INDEX": len(docs["_so/X0_INDEX.md"]) // 3,
        "BANG_DIEU_KHIEN (mẫu rỗng, chạy thật lớn hơn)":
            len(docs["_so/BANG_DIEU_KHIEN.md"]) // 3,
        # ba dòng thành phần phải cộng ĐÚNG ra dòng CỘNG: vòng 42 lệch 63 token
        # mà không ai biết vì hai dòng này đứng ngoài lưới (hội đồng vòng 15)
        "cắt bỏ X9 và X4": t(len(docs["X9_CAIDAT.md"]) + len(x4)),
        "CHAT HOI, BAN, soạn nháp (không X3, X4, X9)":
            t(tong_bo - len(docs["X9_CAIDAT.md"]) - len(x4) - len(x3)),
        # LITE không EMAIL: chỉ X3 mục 1 tới 5; 5b vẫn gate riêng khi dán chat
        # 5b gate: chỉ đọc khi dán chat, không phải thuế mọi lượt cửa vào
        "CUA_VAO mail": t(_muc(x3, 1, 6) - _muc(x3, '5b', 6) + x5m1 + len(x3e)
                         - _muc(x3e, '1c', 2)),  # 1c gate: chỉ đọc khi rà lệch
        "RA_SOAT": t(len(x4)),
        "SOAN_RA thường lệ": t(len(x1) + len(x2) + x5m1),
        "SUA_FILE nội bộ": t(len(x5) - _muc(x5, '7b')),  # 7b gate: chỉ đọc khi có Q-
        "INSTRUCTION dán trong Project": t(len(docs["INSTRUCTION"])),
        "| CỘNG | ~6969 |": (len(docs["INSTRUCTION"]) + len(docs["_so/X0_INDEX.md"])
                             + len(docs["_so/BANG_DIEU_KHIEN.md"])) // 3,
        # nhãn kèm cột lịch sử ~6969 để phần so chỉ còn số hiện tại; dùng // khớp
        # đúng phép làm tròn của dòng thuế thường trực phép 9
    }


TRANG_THAI_HOP_LE = {
    "VIEC": "MỚI ĐANG LÀM CHỜ ĐỐI TÁC CHỜ DUYỆT TREO XONG HỦY",
    "DUKIEN": "CHƯA KIỂM ĐÃ KIỂM MÂU THUẪN ĐÃ THAY HẾT HẠN",
    "PLAN": "MỚI ĐANG LÀM CHỜ CHỐT ĐÃ GHI HỦY",
}

loi = []


DA_KIEM = []
PHEP_BAT_BUOC = ["1.", "1b.", "1c.", "1d.", "1e.", "2.", "2b.", "2c.", "3.", "4.",
                 "5.", "6.", "7.", "9.", "9b.", "10.", "11.", "12.", "13.", "13b.",
                 "13c.", "14.", "14b."]
# phép 8 chạy trong nhánh riêng (bản gộp), không điểm danh ở đây


def kiem(ten, dieu_kien, chi_tiet=""):
    DA_KIEM.append(ten)
    if dieu_kien:
        print(f"  PASS  {ten}")
    else:
        print(f"  FAIL  {ten}" + (f": {chi_tiet}" if chi_tiet else ""))
        loi.append(ten)



def _kho_song(goc, td):
    """Dựng một KHO LÀNH tối thiểu từ chính bộ mẫu ở goc: X0 rev 1, C12 đúng
    tập mục trống, một lượt ghi hoàn tất có dấu ở NHATKY, VIEC và bảng."""
    import shutil
    import kiem_van_hanh as K
    kho = Path(td) / "kho"
    idx = kho / "00_Index"
    idx.mkdir(parents=True)
    for f in FILE_BAT_BUOC + FILE_KEM:
        (idx / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(goc / f, idx / f)
    shutil.copy(sorted(goc.glob("INSTRUCTION_WORKOPS_v*.md"))[0], idx)
    (idx / "_so" / "_inbox" / "_da_nap").mkdir(parents=True)
    for a, b in [("X0_CAUHINH_TEMPLATE.md", "X0_CAUHINH_FUZ.md"),
                 ("X1_CAM_TEMPLATE.md", "X1_CAM_FUZ.md"),
                 ("X2_PHATHANH_TEMPLATE.md", "X2_PHATHANH_FUZ.md"),
                 ("X3_CUAVAO_TEMPLATE.md", "X3_CUAVAO_FUZ.md"),
                 ("X3E_EMAIL_TEMPLATE.md", "X3E_EMAIL_FUZ.md"),
                 ("X4_RASOAT_TEMPLATE.md", "X4_RASOAT_FUZ.md"),
                 ("X5_HESO_TEMPLATE.md", "X5_HESO_FUZ.md")]:
        (idx / a).rename(idx / b)
    so = idx / "_so"
    x0p = idx / "X0_CAUHINH_FUZ.md"
    x0 = x0p.read_text(encoding="utf-8").replace("<MÃ>", "FUZ")
    x0 = x0.replace("v13 · rev 0 · <YYYYMMDD>", "v13 · rev 1 · 20260828")
    x0 = x0.replace("@DUAN.<MÃ DA>    <tên dự án>          đang chạy | NGỪNG",
                    "@DUAN.DA1        Du an mot                    đang chạy")
    x0 = x0.replace(
        "                 CUA1 = <điền: đường dẫn gốc trên máy 1> · thiết bị <điền: tên>",
        "                 CUA1 = " + str(kho) + " · thiet bi MAY1")
    # KHÔNG dựng C12 bằng muc_con_trong: dùng chính hàm mà rà 0i sẽ chấm thì
    # vế I2 luôn ĐÚNG bất kể hàm sai thế nào - hội đồng vòng 15 tái nhập được
    # nguyên con bug NẶNG của vòng 40 mà phép 13 vẫn im. Tập này dựng ĐỘC LẬP
    # theo LUẬT VIẾT DẤU khai ở đầu X0: dòng khai "@KEY " mang <điền hay <N.
    _vung = x0[:x0.index("# C12.")] + x0[x0.index("# C13."):]
    _kh, _tron, _khoi = None, [], {}
    for _dg in _vung.splitlines():
        if re.match(r"# C\d+\.", _dg):
            _kh = None          # tiêu đề mục đóng khối: văn xuôi của mục KHÔNG
            continue            # có tham số (C11...) không thuộc khối nào
        _m = re.match(r"\s*(@[A-Z][A-Z0-9._]*)\s", _dg)
        if _m:
            _kh = _m.group(1)
            _khoi.setdefault(_kh, [])
        if _kh:
            _khoi[_kh].append(_dg)
    _bat = set(re.findall(r"\[x\]\s+(REGULATED|PARALLEL|AUTOMATED|EMAIL)", x0))
    for _k, _dong in _khoi.items():
        _t = NL.join(_dong)
        _pf = set(re.findall(r"\((?:profile )?(REGULATED|PARALLEL|AUTOMATED|EMAIL)\)", _t))
        if _pf and not (_pf & _bat):
            continue  # X0 C0: profile chưa bật thì không hỏi, nên không vào C12
        if (re.search(r"<(?:chưa )?điền|<N>", _t) and "chỉ khai khi" not in _t
                and "(cú pháp)" not in _t and not re.search(r"@[A-Z][A-Z0-9._]*<", _t)):
            _tron.append(_k)
    x0 = x0.replace("[ ] <X9 liệt kê mọi mục chưa trả lời được vào đây>",
                    NL.join("[ ] " + k for k in sorted(_tron)))
    _ghi(x0p, x0)
    G = "G-20260828-CUA1-01"
    nk = (so / "NHATKY_TEMPLATE.md").read_text(encoding="utf-8")
    nk = nk.replace("<năm>Q<quý>", "2026Q3").replace("<MÃ>", "FUZ").rstrip(NL)
    _ghi(so / "NHATKY_2026Q3.md", nk + NL + "| " + G + " | 2026-08-28 | CUA1.0900.a1b2"
         " | A | mo viec V-DA1-001 | VIEC V-DA1-001 | khong | XONG | khong |" + NL)
    v = (so / "VIEC.md").read_text(encoding="utf-8")
    v = v.replace("<MÃ>", "FUZ").replace("## <KHỐI>", "## KHOI1").rstrip(NL)
    _ghi(so / "VIEC.md", v + NL + "| DA1 | V-DA1-001 | Viec mot | buoc sau | toi | |"
         " 2026-12-31 | XONG | | " + G + " |" + NL)  # XONG: ca I2 chuyển _lich_su
    # theo X5 mục 5 chỉ đúng luật với việc XONG hay HỦY (hội đồng vòng 15b)
    for t in ["DUKIEN.md", "TAILIEU.md", "QUYETDINH.md", "PLANNING.md", "THU.md"]:
        _ghi(so / t, (so / t).read_text(encoding="utf-8").replace("<MÃ>", "FUZ"))
    _ghi(so / "X0_INDEX.md", "# X0_INDEX · FUZ" + NL * 2 + "```yaml" + NL
         + "may_sinh: true · sinh_boi: " + G + " · x0_rev: 1 · instruction: v11"
         + NL + "```" + NL)
    _ghi(so / "BANG_DIEU_KHIEN.md", "# BANG_DIEU_KHIEN · FUZ" + NL * 2 + "```yaml" + NL
         + "may_sinh: true · sinh_boi: " + G + " · x0_rev: 1" + NL
         + "watermark: CUA1=" + G + NL + "```" + NL * 2 + "bàn sạch · mốc: chưa có" + NL)
    return kho, idx, so, G


def _ra_soat(idx, kho):
    """Chạy TRỌN main() của kiem_van_hanh, trả TẬP tên phép LỆCH. Kẹp CHỖ GỌI
    chứ không chỉ hàm helper: hội đồng vòng 14 đo được 12/25 đột biến lọt vì
    fixture chỉ khẳng định giá trị trả về của hàm, không ai gọi main()."""
    import contextlib
    import io as _io2
    import kiem_van_hanh as K
    argv = sys.argv
    K.loi.clear()
    K.LOI_DOC.clear()
    try:
        sys.argv = ["kvh", str(idx), str(kho)]
        with contextlib.redirect_stdout(_io2.StringIO()):
            try:
                K.main(idx)
            except SystemExit:
                pass  # main() kết thúc bằng sys.exit theo số lệch, không phải lỗi
    finally:
        sys.argv = argv
    return set(K.loi)


def phep_fuzz(goc):
    """Phép 13: hai BẤT BIẾN đối xứng, đo bằng cách ép trạng thái thật.
    I1  mọi trạng thái làm MẤT dấu mã G phải sinh ÍT NHẤT MỘT lệch
    I2  mọi trạng thái ĐÚNG LUẬT không được sinh lệch nào
    Vế I2 chính là thứ vòng 38, 40 và 41 vi phạm ba lần: vá một lỗ rồi quay
    ra phạt người dùng vì làm đúng. Không có lưới này thì lớp lỗi đó chỉ lộ
    khi có hội đồng chạy tay (hội đồng vòng 14 đo được 14,2 phần trăm trạng
    thái mất dấu đi im)."""
    import tempfile
    import shutil
    hong, phu, _dem = [], set(), {"I1": 0, "I2": 0, "I3": 0}

    def _sua(f, cu, moi):
        _ghi(f, f.read_text(encoding="utf-8").replace(cu, moi))

    def thu(ten, sua, mat_dau):
        _dem["I1" if mat_dau else "I2"] += 1
        with tempfile.TemporaryDirectory() as td:
            kho, idx, so, G = _kho_song(goc, td)
            if _ra_soat(idx, kho):
                hong.append(ten + ": KHO LÀNH đã lệch sẵn, ca không tin được")
                return
            sua(kho, idx, so, G, _sua)
            lech = _ra_soat(idx, kho)
            phu.update(l.split(" ")[0] for l in lech)
            if mat_dau and not lech:
                hong.append("I1 " + ten + ": mất dấu mã G mà KHÔNG phép nào kêu")
            if not mat_dau and lech:
                hong.append("I2 " + ten + ": ĐÚNG LUẬT mà bị báo " + str(sorted(lech)[:2]))

    # ---- I1: trạng thái MẤT dấu, phải kêu ----
    thu("xóa trọn file NHATKY quý",
        lambda k, i, so, G, sua: (so / "NHATKY_2026Q3.md").unlink(), True)
    thu("xóa dòng NHATKY, file còn",
        lambda k, i, so, G, sua: sua(so / "NHATKY_2026Q3.md", "| " + G, "| x-" + G), True)
    thu("xóa ô Ghi lần của dòng VIEC",
        lambda k, i, so, G, sua: sua(so / "VIEC.md", " | " + G + " |", " |  |"), True)
    thu("xóa trọn dòng VIEC",
        lambda k, i, so, G, sua: sua(so / "VIEC.md", "| DA1 | V-DA1-001", "x| DA1 |"), True)
    thu("cắt cụt dòng NHATKY ở mức byte (hỏng schema, mã G ở ô đầu còn)",
        lambda k, i, so, G, sua: _ghi(so / "NHATKY_2026Q3.md",
            (so / "NHATKY_2026Q3.md").read_text(encoding="utf-8")[:-24]), True)
    thu("bản conflicted copy của sổ (thêm bản, không mất dấu)",
        lambda k, i, so, G, sua: shutil.copy(so / "VIEC.md",
                                             so / "VIEC (conflicted copy).md"), True)

    # ---- I2: trạng thái ĐÚNG LUẬT, không được kêu ----
    def _tach_quy(k, i, so, G, sua):
        (so / "_lich_su").mkdir(exist_ok=True)
        shutil.move(str(so / "NHATKY_2026Q3.md"), str(so / "_lich_su" / "NHATKY_2026Q3.md"))
    thu("tách NHATKY quý cũ vào _lich_su (X5 mục 7)", _tach_quy, False)

    def _luu_viec(k, i, so, G, sua):
        (so / "_lich_su").mkdir(exist_ok=True)
        _ghi(so / "_lich_su" / "VIEC_2026.md", (so / "VIEC.md").read_text(encoding="utf-8"))
        sua(so / "VIEC.md", "| DA1 | V-DA1-001", "x| DA1 |")
    thu("chuyển dòng VIEC đã xong sang _lich_su (X5 mục 5)", _luu_viec, False)

    def _danh_dau(k, i, so, G, sua):
        x0 = i / "X0_CAUHINH_FUZ.md"
        sua(x0, "@NHIP.MUIGIO     <điền>", "@NHIP.MUIGIO     UTC+7")
        sua(x0, "[ ] @NHIP.MUIGIO", "[x] @NHIP.MUIGIO - điền lần đầu rev 2 ngày 20260828")
        sua(x0, "v13 · rev 1 · 20260828", "v13 · rev 2 · 20260828")
        sua(so / "X0_INDEX.md", "x0_rev: 1", "x0_rev: 2")
    thu("điền lần đầu rồi đánh dấu [x] ở C12 (C11 ngoại lệ 2)", _danh_dau, False)

    def _them_luot(k, i, so, G, sua):
        G2 = "G-20260828-CUA1-02"
        _ghi(so / "NHATKY_2026Q3.md", (so / "NHATKY_2026Q3.md").read_text(encoding="utf-8")
             + "| " + G2 + " | 2026-08-28 | CUA1.1000.c3d4 | A | cap nhat buoc |"
             " VIEC V-DA1-001 | khong | XONG | khong |" + NL)
        sua(so / "VIEC.md", " | " + G + " |", " | " + G + " " + G2 + " |")
        sua(so / "BANG_DIEU_KHIEN.md", "sinh_boi: " + G, "sinh_boi: " + G2)
        sua(so / "BANG_DIEU_KHIEN.md", "watermark: CUA1=" + G, "watermark: CUA1=" + G2)
    thu("lượt hai nối thêm mã vào ô Ghi lần (X5 mục 3 bước 3)", _them_luot, False)

    # I3: mỗi phép KHÔNG dính mã G cũng phải có một trạng thái mẫu vi phạm, và
    #     rà soát phải sinh ĐÚNG TÊN phép đó. I1 và I2 chỉ nói về mã G nên theo
    #     định nghĩa không với tới 0h, 0i, 0j, 1a, 3f, 7b - hội đồng vòng 15 đo
    #     được 14/16 đột biến vào vùng đó lọt.
    def thu3(ten, sua, ten_phep):
        _dem["I3"] += 1
        with tempfile.TemporaryDirectory() as td:
            kho, idx, so, G = _kho_song(goc, td)
            if _ra_soat(idx, kho):
                hong.append("I3 " + ten + ": KHO LÀNH đã lệch sẵn")
                return
            sua(kho, idx, so, G, _sua)
            _l3 = _ra_soat(idx, kho)
            phu.update(l.split(" ")[0] for l in _l3)
            if not any(l.startswith(ten_phep) for l in _l3):
                hong.append("I3 " + ten + ": " + ten_phep + " không kêu ở CHỖ GỌI")

    thu3("C12 rụng dòng mà giá trị vẫn trống",
         lambda k, i, so, G, sua: sua(i / "X0_CAUHINH_FUZ.md", "[ ] @NHIP.MUIGIO", ""), "0i.")
    thu3("file lạ rơi vào 00_Index",
         lambda k, i, so, G, sua: _ghi(i / "rac_la.md", "x"), "0j.")
    thu3("X0 tụt về rev 0 mà sổ đã mang dấu",
         lambda k, i, so, G, sua: sua(i / "X0_CAUHINH_FUZ.md", "rev 1 · 20260828",
                                      "rev 0 · 20260828"), "0h.")
    thu3("hai bản INSTRUCTION cùng nằm trong 00_Index",
         lambda k, i, so, G, sua: shutil.copy(i / "INSTRUCTION_WORKOPS_v11.md",
                                              i / "INSTRUCTION_WORKOPS_v9.md"), "1a.")
    thu3("dòng dán tay vào sổ, không mã G",
         lambda k, i, so, G, sua: _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8")
             + "| DA1 | V-DA1-009 | dan tay | x | toi | | 2026-12-31 | MỚI | | |" + NL), "3f.")
    thu3("_moc_ghi giữ mã mà NHATKY không có (rollback trọn _so)",
         lambda k, i, so, G, sua: _ghi(i / "_moc_ghi.txt",
             G + NL + "G-20260828-CUA1-77" + NL), "0k.")
    thu3("bảng rụng bộ đếm mà banner phải in",
         lambda k, i, so, G, sua: _ghi(so / "BANG_DIEU_KHIEN.md",
             (so / "BANG_DIEU_KHIEN.md").read_text(encoding="utf-8")
             .replace("bàn sạch · mốc: chưa có", "0 quá hạn")), "8b.")
    thu3("liên kết trong sổ trỏ mã không tồn tại",
         lambda k, i, so, G, sua: sua(so / "VIEC.md", "| XONG | |",
                                      "| XONG | Q-999 |"), "7c.")
    thu3("kho đang chạy còn nằm trong bản làm việc git",
         lambda k, i, so, G, sua: (k / ".git").mkdir(exist_ok=True), "0g.")
    thu3("plan mức C ĐÃ GHI mà không mang mã G",
         lambda k, i, so, G, sua: _ghi(so / "PLANNING.md",
             (so / "PLANNING.md").read_text(encoding="utf-8").rstrip() + NL
             + "| P-20260828-09 | 2026-08-28 | DA1 | x | x | x | x | x | x |"
               " ĐÃ GHI |  |" + NL), "4.")
    thu3("dự án phần mềm khai thiếu trường phạm vi tổ chức",
         lambda k, i, so, G, sua: sua(i / "X0_CAUHINH_FUZ.md",
             "@DUAN.PHANMEM    dự án PHẦN MỀM khai thêm PHẠM VI TỔ CHỨC, mỗi phần mềm một dòng:",
             "@DUAN.PHANMEM    dự án PHẦN MỀM khai thêm PHẠM VI TỔ CHỨC, mỗi phần mềm một dòng:"
             + NL + "  APP  Ung dung dat hang · repo git.cty.vn/app · web"), "7d.")
    thu3("lượt mức C trong NHATKY mà không plan nào mang mã đó",
         lambda k, i, so, G, sua: _ghi(so / "NHATKY_2026Q3.md",
             (so / "NHATKY_2026Q3.md").read_text(encoding="utf-8").rstrip() + NL
             + "| G-20260828-CUA1-09 | 2026-08-28 | CUA1.1100.k2m4 | C | phat hanh"
               " | VIEC V-DA1-001 | khong | XONG | khong |" + NL), "3d.")
    thu3("cửa ma sinh lane watermark giả",
         lambda k, i, so, G, sua: sua(so / "NHATKY_2026Q3.md", "CUA1-01", "CUAX-01"), "7b.")

    # CA MỒI: kho LÀNH khai nhầm là "mất dấu". Nếu vế I1 bị tắt thì ca này im,
    # và phép 13 tự tố cáo mình chỉ còn là trang trí (hội đồng vòng 15).
    _n = len(hong)
    thu("CA MỒI: kho LÀNH khai nhầm là mất dấu", lambda *a: None, True)
    if len(hong) == _n:
        hong.append("CA MỒI không kêu: vế I1 đã bị tắt, phép 13 chỉ còn trang trí")
    elif hong[-1].startswith("I1 CA MỒI"):
        hong.pop()   # pop() mù từng nuốt được thông điệp "KHO LÀNH đã lệch sẵn"

    # CA MỒI chỉ canh vế I1. Ghim SỐ CA thì tắt I2, tắt I3, hay bỏ bớt ca đều
    # đỏ - hội đồng vòng 15b tắt được cả I2 lẫn I3 mà bộ vẫn in "sạch".
    if (_dem["I1"], _dem["I2"], _dem["I3"]) != (7, 4, 13):
        hong.append(f"số ca phép 13 lệch: {_dem}; bộ khai I1 7 (kể CA MỒI), I2 4,"
                    f" I3 13 - bớt ca là bớt lưới; đổi số thì sửa con số này"
                    f" trong CÙNG lượt vá")

    # 14b. ĐIỂM DANH PHÉP CỦA kiem_van_hanh. Phép 14 chỉ điểm danh phép của
    #      CHÍNH kiem_tra_bo, nên xóa một phép khỏi kiem_van_hanh vẫn "sạch".
    #      Danh bạ PHEP_VH là DỮ LIỆU: phép mới không kèm ca của chính nó thì
    #      14b đỏ NGAY LƯỢT VÁ ĐÓ - quy tắc mà ba vòng liền tự viết rồi không
    #      thi hành, nay thành MÁY chứ không còn là lời dặn (vòng 15b).
    import kiem_van_hanh as K14
    MIEN_TRU = ["0.", "0b.", "0c.", "0e.", "0f.", "1.", "1b.", "1c.", "2.",
                "3a.", "3b.", "4.", "5.", "6.", "7.", "9.", "10a.", "10b.",
                "10c.", "11."]  # phải RỖNG DẦN: mỗi mục là một phép chưa ai canh
    _ho = [pp for pp in K14.PHEP_VH if pp not in phu and pp not in MIEN_TRU]
    kiem("14b. mọi phép của kiem_van_hanh đều có ca ép trạng thái ở phép 13",
         not _ho, f"phép {_ho} không có ca nào: xóa trọn phép đó thì bộ vẫn in"
         f" 'hệ sạch'. Thêm một ca I1, I2 hay I3 cho nó, hay khai vào MIEN_TRU"
         f" trong CÙNG lượt vá")

    kiem("13. fuzz ba bất biến: mất dấu phải kêu, đúng luật không được kêu,"
         " mỗi phép phải kêu đúng tên mình", not hong, "; ".join(hong[:4]))

    # 13b. Trần ĐẦU RA: bảng kiem_van_hanh được DÁN VÀO phiên RA_SOAT nên là
    #      context thật, dù file .py đứng ngoài mọi route. Đo được 1.762 ký tự
    #      ở vòng 42 và 1.506 ở vòng 39: đang phình mà không phép nào giữ.
    import contextlib
    import io as _io3
    with tempfile.TemporaryDirectory() as td:
        kho, idx, so, G = _kho_song(goc, td)
        buf, argv = _io3.StringIO(), sys.argv
        import kiem_van_hanh as K3
        try:
            sys.argv = ["kvh", str(idx), str(kho)]
            with contextlib.redirect_stdout(buf):
                try:
                    K3.main(idx)
                except SystemExit:
                    pass
        finally:
            sys.argv = argv
        n_ra = len(buf.getvalue())
    kiem("13b. bảng kết quả kiem_van_hanh trong trần đầu ra 2.400 ký tự",
         n_ra <= 2400, f"{n_ra} ký tự ~{n_ra // 3} token: đầu ra này DÁN VÀO"
         f" phiên RA_SOAT, là context thật của người dùng")

    # 13c. Trần trên kho TOÀN PASS là ca DỄ NHẤT; RA_SOAT chỉ chạy khi kho CÓ
    #      vấn đề. Hội đồng vòng 15b: kho 8 lệch cho 3.832 ký tự, vượt 60%.
    with tempfile.TemporaryDirectory() as td:
        kho, idx, so, G = _kho_song(goc, td)
        _ghi(idx / "rac_la.md", "x")
        shutil.copy(idx / "INSTRUCTION_WORKOPS_v11.md",
                    idx / "INSTRUCTION_WORKOPS_v9.md")
        _ghi(so / "VIEC.md", (so / "VIEC.md").read_text(encoding="utf-8")
             + "| DA1 | V-DA1-009 | dan tay | x | toi | | 2026-12-31 | MỚI | | |" + NL)
        buf2, argv = _io3.StringIO(), sys.argv
        try:
            sys.argv = ["kvh", str(idx), str(kho)]
            with contextlib.redirect_stdout(buf2):
                try:
                    K3.main(idx)
                except SystemExit:
                    pass
        finally:
            sys.argv = argv
        n_lech = len(buf2.getvalue())
    kiem("13c. bảng kiem_van_hanh trên kho ĐANG LỆCH trong trần 4.400 ký tự",
         n_lech <= 4400, f"{n_lech} ký tự ~{n_lech // 3} token: đây mới là ca"
         f" người dùng THẬT SỰ dán vào phiên RA_SOAT")


def main(goc):
    goc = Path(goc)

    # 1. Đủ file bắt buộc, có đúng một INSTRUCTION và một GHICHU
    thieu = [f for f in FILE_BAT_BUOC + FILE_KEM if not (goc / f).is_file()]
    instr = sorted(goc.glob("INSTRUCTION_WORKOPS_v*.md"))
    ghichu = sorted(goc.glob("GHICHU_DOI_MOI_v*.md"))
    kiem("1. đủ file bắt buộc, gồm benchmark và hai script", not thieu, f"thiếu {thieu}")
    # 1d. File MÁY SINH không được đóng gói/commit: cache quan sát và bộ _thu_*
    #     bị track là "git pull" của công ty đang chạy sẽ kẹt vì cache local bẩn
    #     (hội đồng vòng 8). Kiểm qua .gitignore - tất định, không phụ thuộc git.
    gi_nd = (goc / ".gitignore").read_text(encoding="utf-8") if (goc / ".gitignore").is_file() else ""
    gi = "\n".join(l.split(" ")[0] for l in gi_nd.splitlines()
                   if not l.lstrip().startswith(("#", "!")))
    # loại dòng comment, dòng negation "!" và đuôi sau khoảng trắng: các khe
    # tự phá mà so chuỗi thô nhận nhầm (hội đồng vòng 10)
    seg_ok = any(seg.startswith("_thu_") for l in gi.splitlines()
                 for seg in l.split("/"))
    thieu_gi = ([] if "_quan_sat_truoc.json" in gi else ["_quan_sat_truoc.json"]) \
               + ([] if seg_ok else ["_thu_"])
    kiem("1d. .gitignore che các file máy sinh (_quan_sat_truoc, _thu_*)",
         not thieu_gi, f"thiếu khuôn {thieu_gi} trong .gitignore")
    # 1e. Phép BÙ của phép 1: lưới là allow-list nên thứ DÔI RA vô hình theo cấu
    #     trúc. .codex_audit_mutant lọt commit vòng 37, assets\ lọt vòng 38, cả hai
    #     qua sạch phép 1. Bộ ship "NGUYÊN TRẠNG" nên rác ở đây hạ cánh vào
    #     00_Index của MỌI công ty, nơi 0j của kiem_van_hanh mới nhặt lên được.
    #     File MÁY SINH đã khai ở .gitignore không tính là thừa: khuôn được đọc
    #     ĐẦY ĐỦ (cả dòng có đường dẫn lẫn dòng có *), nếu không thì mọi người
    #     dùng chạy kiem_van_hanh trước kiem_tra_bo đều bị báo oan cache của
    #     chính máy (bắt được ở lượt kiểm chứng đầu-cuối vòng 40).
    import fnmatch
    khuon_bo = ["__pycache__", ".git", ".venv", ".idea", ".vscode"] + [
        l.strip().rstrip("/") for l in gi_nd.splitlines()
        if l.strip() and not l.strip().startswith(("#", "!"))]

    def da_khai_bo(rel):
        for k in khuon_bo:
            if fnmatch.fnmatch(rel, k) or fnmatch.fnmatch(rel, k + "/*"):
                return True
            if any(fnmatch.fnmatch(seg, k) for seg in rel.split("/")):
                return True
        return False

    # _quan_sat_bo.txt do CHÍNH lời sửa của 0j bảo người dùng tạo; kho công ty
    # còn mang bộ X đã đổi tên theo mã - chạy kiem_tra_bo ở đó là chế độ KHO,
    # không phải bộ mẫu, nên 1e không áp (hội đồng vòng 14).
    if list(goc.glob("X0_CAUHINH_*.md")) and not (goc / "X0_CAUHINH_TEMPLATE.md").is_file():
        print("  BỎ QUA  1e: đây là KHO CÔNG TY (bộ X đã mang mã), không phải bộ mẫu")
        cho_phep = None
    else:
        cho_phep = set(FILE_BAT_BUOC + FILE_KEM) | {".gitignore", "_so/_quan_sat_bo.txt"}
    thua = []
    for f in (goc.rglob("*") if cho_phep is not None else []):
        rel = str(f.relative_to(goc)).replace("\\", "/")
        if not f.is_file() or da_khai_bo(rel):
            continue
        if rel not in cho_phep and not re.fullmatch(
                r"INSTRUCTION_WORKOPS_v\d+\.md|GHICHU_DOI_MOI_v.*\.md"
                r"|WORKOPS_.*_GOP\.md|_so/NHATKY_\d{4}Q[1-4]\.md", rel):
            thua.append(rel)
    kiem("1e. không file thừa ngoài danh sách bộ", not thua,
         f"{sorted(thua)[:5]}: xóa khỏi repo hay đưa vào .gitignore; bộ ship"
         f" NGUYÊN TRẠNG nên thứ ở đây vào 00_Index của mọi công ty")
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
        # MỌI dòng mang nhãn, không chỉ dòng ĐẦU: vòng 42 để lọt "Route ~1506"
        # vì một dòng khác cùng nhãn khớp trước (hội đồng vòng 15). Tổng của MỖI
        # dòng là số lớn nhất trên dòng đó (các số nhỏ hơn là thành phần).
        # ~1.059 (số có dấu nghìn) là số VĂN XUÔI hay snapshot, không phải số
        # route: bỏ qua, nếu không "NOI_BO mức A" đọc nhầm thành ~1. Và bỏ dòng
        # mang nhãn DÀI HƠN chứa nhãn này ("CUA_VAO thường" vs "... của LITE").
        dai_hon = [k for k in do if k != nhan and nhan in k]
        cac_max = [max(int(x) for x in re.findall(r"~(\d+)(?![\d.])", m.group(1)))
                   for m in re.finditer(re.escape(nhan) + r"([^\n]*)", bm)
                   if re.search(r"~\d+(?![\d.])", m.group(1))
                   and not any(k in m.group(0) for k in dai_hon)]
        if not cac_max:
            lech_bm.append(f"{nhan}: không thấy dòng trong BENCHMARK")
        # dòng CỘNG là thuế thường trực, tính bằng // nên khớp TUYỆT ĐỐI được:
        # dung sai 10% ở đó là 232 token trôi mà máy im (đo được +81 vòng 40-42)
        nguong = 0 if "CỘNG" in nhan else (0.02 if gia_tri > 5000 else 0.10)
        for _so in cac_max:
            if abs(_so - gia_tri) > nguong * gia_tri:
                lech_bm.append(f"{nhan}: BENCHMARK ~{_so}, đo thật ~{gia_tri}")
    kiem("2c. số route BENCHMARK khớp số đo thật (dung sai 0 cho dòng CỘNG,"
         " 2% trên 5.000 token, 10% còn lại)", not lech_bm,
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
        nd = (docs["INSTRUCTION"] if ten == "INSTRUCTION"
              else docs.get(ten) or kem.get(ten, ""))
        if nd and len(nd) > tran:
            vuot_ns.append((ten, len(nd), tran))
    # 9b. Bảng trần khai ở BENCHMARK phải khớp NGAN_SACH: vòng 13 phạt 9/13 số
    #     route stale; không giữ thì lớp lỗi đó chỉ dời sang bảng trần.
    TEN_BM = {"INSTRUCTION": "INSTRUCTION", "X0_CAUHINH_TEMPLATE.md": "X0",
              "X5_HESO_TEMPLATE.md": "X5", "X3_CUAVAO_TEMPLATE.md": "X3",
              "X3E_EMAIL_TEMPLATE.md": "X3E", "X9_CAIDAT.md": "X9",
              "X4_RASOAT_TEMPLATE.md": "X4", "X2_PHATHANH_TEMPLATE.md": "X2",
              "X1_CAM_TEMPLATE.md": "X1", "_so/X0_INDEX.md": "X0_INDEX",
              "_so/BANG_DIEU_KHIEN.md": "BANG_DIEU_KHIEN", "README.md": "README",
              "WORKOPS_STARTER_v24_20260824_GOP.md": "bản gộp _GOP"}
    # chỉ đọc KHỐI "Trần từng file": chỗ khác cũng có "X0_INDEX 2.400" nhưng đó
    # là trần RUNTIME của view, khác trần file mẫu ở NGAN_SACH
    _bm = docs["BENCHMARK_TOKEN.md"]
    _khoi_tran = _bm[_bm.find("## Trần từng file"):]
    _khoi_tran = _khoi_tran[:_khoi_tran.find("\n## ", 5)] if "\n## " in _khoi_tran[5:] else _khoi_tran
    lech_tran = []
    for ten, tran in NGAN_SACH.items():
        if ten not in TEN_BM:
            continue
        m_t = re.search(re.escape(TEN_BM[ten]) + r"\s+(\d{1,3}(?:\.\d{3})+)", _khoi_tran)
        khai = int(m_t.group(1).replace(".", "")) if m_t else None
        if khai != tran:
            lech_tran.append(f"{TEN_BM[ten]}: BENCHMARK {khai}, NGAN_SACH {tran}")
    kiem("9b. bảng trần ở BENCHMARK khớp NGAN_SACH", not lech_tran, str(lech_tran))
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
        # BA HÀNH VI v26/v27 của bộ lọc bản sao (ghim máy, hội đồng vòng 7)
        import kiem_van_hanh as _kv26
        ca.append(("khuôn bản sao đồng bộ bị nhận diện, tên thường không oan",
                   all(_kv26.la_file_tam(t) for t in
                       ["BC (1).docx", "HD copy.xlsx", "HD copy 2.xlsx",
                        "BC - Copy.docx", "PL(bản sao).pdf"])
                   and not any(_kv26.la_file_tam(t) for t in
                               ["copy_of_process.md", "BC_copyright.docx",
                                "BC_v01.docx"])))
        ca.append(("loc_ban_chinh chọn đúng bản chính theo tên chuẩn",
                   [q.name for q in _kv26.loc_ban_chinh(
                       [Path("NHATKY_2026Q3.md"),
                        Path("NHATKY_2026Q3-DESKTOP-A1B2.md"),
                        Path("NHATKY_2026Q3 (1).md"),
                        Path("NHATKY_TEMPLATE.md")],
                       r"NHATKY_\d{4}Q[1-4]\.md")] == ["NHATKY_2026Q3.md"]))
        ca.append(("tên X0 chuẩn 3-4 ký tự, có dấu hay 5 ký tự bị loại",
                   [q.name for q in _kv26.loc_ban_chinh(
                       [Path("X0_CAUHINH_ABC.md"), Path("X0_CAUHINH_ĐT.md"),
                        Path("X0_CAUHINH_ABCDE.md"), Path("X0_CAUHINH_TEMPLATE.md")],
                       r"X0_CAUHINH_[A-Z0-9]{3,4}\.md")] == ["X0_CAUHINH_ABC.md"]))
        # HEURISTIC CÙNG TIỀN TỐ (ghim v29/v30, hội đồng vòng 9): ca dương
        # -DESKTOP-XXXX bị nghi kèm tên tiền tố; ca âm -v02 vẫn được đề xuất
        stem_map = {"01_A": {"BC", "BC-DESKTOP-A1B2", "BC-v02"}}
        giu9, nghi9 = _kv26.loc_nghi_ban_sao(
            ["01_A/BC-DESKTOP-A1B2.docx", "01_A/BC-v02.docx"], stem_map)
        ca.append(("cùng-tiền-tố: bản OneDrive bị nghi kèm tiền tố, -v02 không oan",
                   giu9 == ["01_A/BC-v02.docx"]
                   and [(r, g) for r, g in nghi9] == [("01_A/BC-DESKTOP-A1B2.docx", "BC")]))
        # 12l MIỄN SO HASH cho dòng tombstone "[đã xóa theo Q-": index mang ô
        # hash của dòng gốc, dòng đã trung hòa đúng luật 7b thì không lệch oan
        idx_hash = {"<a@x>|op1": {"so": "VIEC", "dong": "V-001",
                                  "hash": "0" * 64}}
        r = chay_email(nk=P("<a@x>") + "\n" + C("<a@x>") + "\n", reg=["<a@x>"],
                       idx=idx_hash,
                       files=dict(FILES_SACH,
                                  **{"_so/VIEC.md": "| V-001 | [đã xóa theo Q-20260825-01] |\n",
                                     "_so/QUYETDINH.md": "| Q-20260825-01 | xóa CV |\n"}))
        ca.append(("12l miễn so hash cho dòng tombstone xóa pháp lý",
                   r.get(TEN_12L) is not False))
        # 12l KHUÔN TRỌN (v32): chuỗi lửng "[đã xóa theo Q-x" không ngoặc đóng
        # KHÔNG được miễn hash; và Q ma (không có trong QUYETDINH) cũng KHÔNG
        r = chay_email(nk=P("<a@x>") + "\n" + C("<a@x>") + "\n", reg=["<a@x>"],
                       idx={"<a@x>|op1": {"so": "VIEC", "dong": "V-001",
                                          "hash": "0" * 64}},
                       files=dict(FILES_SACH,
                                  **{"_so/VIEC.md": "| V-001 | [đã xóa theo Q-x |\n",
                                     "_so/QUYETDINH.md": "| Q-20260826-01 | x |\n"}))
        ca.append(("12l khuôn lửng không ngoặc đóng không được miễn hash",
                   r.get(TEN_12L) is False))
        r = chay_email(nk=P("<a@x>") + "\n" + C("<a@x>") + "\n", reg=["<a@x>"],
                       idx={"<a@x>|op1": {"so": "VIEC", "dong": "V-001",
                                          "hash": "0" * 64}},
                       files=dict(FILES_SACH,
                                  **{"_so/VIEC.md": "| V-001 | [đã xóa theo Q-MA-KHONG-CO] |\n",
                                     "_so/QUYETDINH.md": "| Q-20260826-01 | x |\n"}))
        ca.append(("12l tombstone mang Q ma không có trong QUYETDINH bị bắt",
                   r.get(TEN_12L) is False))
        # 12l SO MÃ Q ĐÚNG Ô (v33, hội đồng vòng 12): substring toàn văn từng
        # cho hai ca này lọt - Q là TIỀN TỐ của mã thật, và Q chỉ được nhắc
        # trong Ô GHI CHÚ của dòng quyết định khác ("cân nhắc, không ban hành")
        r = chay_email(nk=P("<a@x>") + "\n" + C("<a@x>") + "\n", reg=["<a@x>"],
                       idx={"<a@x>|op1": {"so": "VIEC", "dong": "V-001",
                                          "hash": "0" * 64}},
                       files=dict(FILES_SACH,
                                  **{"_so/VIEC.md": "| V-001 | [đã xóa theo Q-2026] |\n",
                                     "_so/QUYETDINH.md": "| Q-20260826-01 | x |\n"}))
        ca.append(("12l Q tiền tố của mã thật không được miễn hash",
                   r.get(TEN_12L) is False))
        r = chay_email(nk=P("<a@x>") + "\n" + C("<a@x>") + "\n", reg=["<a@x>"],
                       idx={"<a@x>|op1": {"so": "VIEC", "dong": "V-001",
                                          "hash": "0" * 64}},
                       files=dict(FILES_SACH,
                                  **{"_so/VIEC.md": "| V-001 | [đã xóa theo Q-77] |\n",
                                     "_so/QUYETDINH.md": "| Q-20260826-01 | cân nhắc Q-77, không ban hành |\n"}))
        ca.append(("12l Q chỉ nằm trong ghi chú dòng khác không được miễn hash",
                   r.get(TEN_12L) is False))
        # SCHEMA KHAI Ở X3E MỤC 1b PHẢI ĐƯỢC CHÍNH MÁY CHẤP NHẬN (PILOT vòng 39:
        # thực thi X3E theo văn xuôi cũ sinh ra payload bị 12h từ chối, vì tên
        # trường máy đòi không được khai ở đâu; nay khai rồi thì phải khớp)
        _khoa_pl = "<a@x>"
        _pl_dung = {"conv_id": "c1", "nguoi_gui": "a@x", "thoi_diem": "2026-08-28T03:10:00Z",
                    "tieu_de": "tieu de", "eml_sha256": "0" * 64,
                    "staging": "_so/_thu_staging/" + __import__("hashlib").sha256(
                        _khoa_pl.encode("utf-8")).hexdigest(),
                    "dinh_kem": [{"ten": "f.pdf", "sha256": "1" * 64, "bytes": 12}],
                    "thao_tac": [{"operation_id": "op1", "so": "VIEC",
                                  "dong": "V-001", "noi_dung": "| V-001 | x |"}]}
        ca.append(("payload dựng đúng SCHEMA khai ở X3E mục 1b thì máy nhận",
                   _kv26.kiem_payload(_pl_dung, _khoa_pl) == []))
        _pl_cu = dict(_pl_dung)
        del _pl_cu["conv_id"], _pl_cu["thoi_diem"]
        _pl_cu["convId"], _pl_cu["thoi_diem_utc"] = "c1", "2026-08-28T03:10:00Z"
        ca.append(("payload dùng tên trường ngoài schema thì máy từ chối",
                   len(_kv26.kiem_payload(_pl_cu, _khoa_pl)) == 2))
        # BA QUYẾT ĐỊNH của rà 0d, 0g, 0i (hội đồng vòng 13: vùng rà soát từng
        # có mutation score 0% vì main() không hàm nào gọi được; ba hàm này nay
        # ở tầng module nên fixture kẹp thẳng)
        import tempfile as _tf
        with _tf.TemporaryDirectory() as _td:
            _g = Path(_td) / "kho" / "00_Index"
            (_g / "_so").mkdir(parents=True)
            _so = _g / "_so"
            (_so / "VIEC.md").write_text("| V-001 | x |\n", encoding="utf-8")
            (_so / "BANG_DIEU_KHIEN.md").write_text("bàn sạch\n", encoding="utf-8")
            ca.append(("0d: kho chưa ghi lần nào thì không có dấu vết",
                       _kv26.loc_dau_vet_ghi(_so) == []))
            (_so / "BANG_DIEU_KHIEN.md").write_text(
                "sinh_boi: G-20260828-CUA1-01\n", encoding="utf-8")
            ca.append(("0d: mã G chỉ ở BANG_DIEU_KHIEN vẫn là dấu vết đã ghi",
                       _kv26.loc_dau_vet_ghi(_so) == ["BANG_DIEU_KHIEN.md"]))
            ca.append(("0g: kho không nằm trong bản làm việc git nào",
                       _kv26.tim_vung_git(_g) is None))
            (Path(_td) / ".git").mkdir()
            ca.append(("0g: .git ở THƯ MỤC CHA vẫn bị bắt",
                       _kv26.tim_vung_git(_g) == Path(_td).resolve()))
        _x0 = ("# C1.\n@A.MOT   giá trị thật\n@A.HAI   <điền, mô tả>\n"
               "@A.BA    13  <điền thêm>\n@A.BON   <chưa điền, chỉ khai khi dùng>\n"
               "# C12.\n[ ] @A.HAI\n[ ] @A.BA\n# C13.\n")
        ca.append(("0i: C12 khai đúng tập mục còn dấu chưa điền",
                   _kv26.lech_c12(_x0) == []))
        ca.append(("0i: xóa dòng khỏi C12 mà giá trị vẫn trống thì lệch",
                   _kv26.lech_c12(_x0.replace("[ ] @A.BA\n", "")) == ["@A.BA"]))
        # ghim trên CHÍNH template, không trên bản tổng hợp: bản tổng hợp không
        # có dòng cú pháp lẫn khóa C13 nên con bug NẶNG của vòng 40 tái nhập
        # được mà mọi lưới im (hội đồng vòng 15)
        _tpl = (goc / "X0_CAUHINH_TEMPLATE.md").read_text(encoding="utf-8")
        _mt = _kv26.muc_con_trong(_tpl)
        ca.append(("0i trên CHÍNH template: 38 ô trống khi chưa bật profile nào,"
                   " 44 khi bật REGULATED và EMAIL; không nuốt dòng cú pháp hay ô"
                   " đã điền; có khóa của C13",
                   len(_mt) == 38 and len(_kv26.muc_con_trong(
                       _tpl.replace("  [ ] EMAIL", "  [x] EMAIL")
                           .replace("  [ ] REGULATED", "  [x] REGULATED"))) == 44
                   and not ({"@DUAN.", "@NGUON.", "@TEN.PROJECT"} & _mt)
                   and "@MUC.NANG" in _mt))
        # PH-5: ghim CHIỀU của lời dặn phép 8, thứ mà phán quyết không giữ
        ca.append(("8: bảng mới hơn watermark thì lời dặn phải là CẤM sinh lại",
                   _kv26.bang_moi_hon("G-20260828-CUA1-09", "CUA1",
                                      {"CUA1": "G-20260828-CUA1-01"}) is True))
        ca.append(("8: bảng cũ hơn watermark thì lời dặn phải là SINH LẠI",
                   _kv26.bang_moi_hon("G-20260828-CUA1-01", "CUA1",
                                      {"CUA1": "G-20260828-CUA1-09"}) is False))
        # ĐA TIỀN TỐ: hai tiền tố cùng khớp thì nhãn phải TẤT ĐỊNH = dài nhất
        giu10, nghi10 = _kv26.loc_nghi_ban_sao(
            ["01_A/BC-KH-PHULUC-2026.docx"],
            {"01_A": {"BC", "BC-KH", "BC-KH-PHULUC-2026"}})
        ca.append(("đa tiền tố: nhãn tất định, chọn tiền tố dài nhất",
                   nghi10 == [("01_A/BC-KH-PHULUC-2026.docx", "BC-KH")]))
        # KHO SAU XÓA PHÁP LÝ đúng luật phải SẠCH: đính kèm tombstone de_ngoai
        # "đã xóa theo Q-", staging đã dọn có manifest, dòng sổ giữ mã (12h/12j/
        # 12k/12l đều phải xanh) - lớp lỗi ba vòng cùng họ, có lưới hồi quy riêng
        pay_xoa = dict(PAY, dinh_kem=[{"ten": "CV.pdf", "de_ngoai": True,
                                       "ly_do": "đã xóa theo Q-20260825-01"}])
        don_xoa = {"<a@x>": {"purged_at": "2026-08-25", "eml_final_path": "x",
                             "attachment_final_paths": [], "sha256": EML_SHA}}
        r = chay_email(nk=P("<a@x>", pay=pay_xoa) + "\n" + C("<a@x>") + "\n",
                       reg=["<a@x>"], files={"_so/VIEC.md": "| V-001 | viec |\n"},
                       idx=IDX_SACH, don=don_xoa)
        ca.append(("kho sau XÓA PHÁP LÝ đúng luật phải sạch (12h, 12j, 12k, 12l)",
                   all(r.get(t) is not False
                       for t in (TEN_12H, TEN_12J, TEN_12K, TEN_12L))))
        # HỘP CŨ hợp lệ: nhật ký mang hộp lịch sử, X0 khai @NHIP.HOPTHU_CU
        # -> 12e phải PASS (fixture dương cho vá đổi hộp thư vòng 28)
        THU_MUC_CU = _hl.sha256(b"<cu@x>").hexdigest()
        PAY_CU = dict(PAY, staging=f"_so/_thu_staging/{THU_MUC_CU}/", dinh_kem=[])
        P_CU = _json.dumps({"ev": "PREPARED", "khoa": "<cu@x>",
                            "hop_thu": "cu@abc-cu.vn", "payload": PAY_CU})
        C_CU = _json.dumps({"ev": "COMMITTED", "khoa": "<cu@x>",
                            "hop_thu": "cu@abc-cu.vn"})
        import contextlib as _ctx, io as _io2
        with tempfile.TemporaryDirectory() as tdc:
            gc9 = Path(tdc); sc9 = gc9 / "_so"; sc9.mkdir()
            (gc9 / "X0_CAUHINH_T.md").write_text(
                "@NHIP.HOPTHU (EMAIL) mail@congty.vn\n"
                "@NHIP.HOPTHU_CU (EMAIL) cu@abc-cu.vn\n", encoding="utf-8")
            st9 = sc9 / "_thu_staging" / THU_MUC_CU
            st9.mkdir(parents=True)
            (st9 / "thu.eml").write_text("eml", encoding="utf-8")
            (sc9 / "VIEC.md").write_text("| V-001 | viec |\n", encoding="utf-8")
            (sc9 / "_thu_nhat_ky.ndjson").write_text(
                P_CU + "\n" + C_CU + "\n", encoding="utf-8")
            (sc9 / "_thu_da_nap.json").write_text(
                _json.dumps(["<cu@x>"]), encoding="utf-8")
            (sc9 / "_thu_ap_dung.json").write_text(
                _json.dumps({"<cu@x>|op1": {"so": "VIEC", "dong": "V-001"}}),
                encoding="utf-8")
            with _ctx.redirect_stdout(_io2.StringIO()):
                rcu = {t: ok for t, ok, _ in kiem_email(gc9, sc9)}
            ca.append(("hộp cũ khai @NHIP.HOPTHU_CU không bị 12e đá oan",
                       rcu.get(TEN_12E) is not False))
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
        kiem(f"11. fixture bộ quan sát ({len(ca)} ca)",
             not hong and len(ca) == 91,
             str(hong) + (f" · đếm được {len(ca)} ca mà bộ khai 91: bớt ca là"
                          f" bớt lưới không ai hay; đổi số thì sửa con số này"
                          f" trong CÙNG lượt vá" if len(ca) != 91 else ""))
    except Exception as e:
        kiem("11. fixture bộ quan sát", False, f"lỗi chạy: {e}")

    # 12. Luật nghiệp vụ then chốt phải có mặt trong X5 và X3 (chống rơi khi rút gọn)
    x5nd = docs["X5_HESO_TEMPLATE.md"]
    _luat = [
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
        ("mail máy có lối thoát nghiệp vụ, không nuốt hóa đơn bản ký", "THOÁT luật gom" in docs["X3E_EMAIL_TEMPLATE.md"]),
        ("bảng mức thao tác repo tồn tại, rollback chạy thật là C", "ROLLBACK" in docs["X5_HESO_TEMPLATE.md"] and "REPO" in docs["X5_HESO_TEMPLATE.md"]),
        # PHẠM VI TỔ CHỨC PHẦN MỀM: sáu luật giữ TRỌN chuỗi từ README tới X2.
        # Đây là yêu cầu nghiệp vụ có thật của người dùng ("công ty có dự án
        # phần mềm cần nắm rõ phạm vi tổ chức để các vận hành liên quan
        # chính xác hơn"), nên nó phải do MÁY giữ chứ không do lời khai.
        ("README có mục riêng cho công ty phần mềm, kèm LÝ DO phải khai", "## Công ty có phần mềm" in docs["README.md"] and "KHAI RÕ PHẠM VI TỔ" in docs["README.md"] and "vận hành liên quan mới chính xác" in docs["README.md"]),
        ("X9 hỏi phạm vi tổ chức ngay phiên cài đặt khi dự án là phần mềm", "là PHẦN MỀM thì hỏi thêm phạm vi tổ chức" in docs["X9_CAIDAT.md"] and "nơi giữ secret" in docs["X9_CAIDAT.md"]),
        ("X0 C2 khai đủ NĂM trường phạm vi tổ chức phần mềm", all(t in docs["X0_CAUHINH_TEMPLATE.md"] for t in ["@DUAN.PHANMEM", "repo <URL hay đường dẫn>", "thành phần chính", "môi trường", "nơi chạy thật", "nơi giữ secret"])),
        ("repo là nguồn sự thật của code, code KHÔNG chép vào kho", "Repo là NGUỒN SỰ THẬT" in docs["X0_CAUHINH_TEMPLATE.md"] and "code KHÔNG chép vào kho" in docs["X0_CAUHINH_TEMPLATE.md"]),
        ("X5 mục 1b có gate, bảng mức repo, luật SECRET và dữ liệu khách", "# 1b." in docs["X5_HESO_TEMPLATE.md"] and "CHỈ đọc khi dự án thuộc X0 C2" in docs["X5_HESO_TEMPLATE.md"] and "SECRET" in docs["X5_HESO_TEMPLATE.md"] and "dữ liệu khách" in docs["X5_HESO_TEMPLATE.md"]),
        ("phát hành phần mềm cho khách có bảng kiểm riêng ở X2", "Phát hành PHẦN MỀM cho khách" in docs["X2_PHATHANH_TEMPLATE.md"] and "release note" in docs["X2_PHATHANH_TEMPLATE.md"]),
        ("ngoại lệ sự cố cho thông báo đang cháy, DUKIEN ghi bù", "NGOẠI LỆ SỰ CỐ" in docs["X2_PHATHANH_TEMPLATE.md"]),
        ("xóa theo yêu cầu pháp lý có thủ tục xuyên tầng", "XÓA THEO YÊU CẦU PHÁP LÝ" in docs["X5_HESO_TEMPLATE.md"]),
        ("RA_NGOAI là phạm vi bao trùm có luật quan hệ", "BAO TRÙM" in docs["X0_CAUHINH_TEMPLATE.md"]),
        ("hộp thư cũ sau đổi domain có chỗ khai", "@NHIP.HOPTHU_CU" in docs["X0_CAUHINH_TEMPLATE.md"]),
        ("chat dán tay đi cửa người dùng đưa trực tiếp, không cấp luồng THU", "dán CẢ ĐOẠN" in docs["X3_CUAVAO_TEMPLATE.md"] and "KHÔNG cấp mã luồng THU" in docs["X3_CUAVAO_TEMPLATE.md"]),
        ("phục hồi sự cố tách mục 1c có gate chỉ đọc khi rà lệch", "# 1c." in docs["X3E_EMAIL_TEMPLATE.md"] and "CHỈ đọc khi rà 24-31" in docs["X3E_EMAIL_TEMPLATE.md"]),
        ("xóa pháp lý tách mục 7b có gate chỉ đọc khi có Q", "# 7b." in docs["X5_HESO_TEMPLATE.md"] and "CHỈ đọc khi có Q-" in docs["X5_HESO_TEMPLATE.md"]),
        ("chat dán lặp có mốc đã-nạp-tới ghi ô Bước tiếp theo, sau mốc theo vị trí", "CHỐNG DÁN LẶP" in docs["X3_CUAVAO_TEMPLATE.md"] and "đã nạp tới tin" in docs["X3_CUAVAO_TEMPLATE.md"] and "Bước tiếp theo" in docs["X3_CUAVAO_TEMPLATE.md"] and "VỊ TRÍ" in docs["X3_CUAVAO_TEMPLATE.md"]),
        ("chat 5b có gate chỉ đọc khi dán, không phải thuế mọi lượt", "# 5b." in docs["X3_CUAVAO_TEMPLATE.md"] and "CHỈ đọc khi người dùng dán chat" in docs["X3_CUAVAO_TEMPLATE.md"]),
        ("event_id tin chat có số thứ tự trong khối, trùng khóa thì so nội dung", "-chat-<NN>" in docs["X3_CUAVAO_TEMPLATE.md"] and "SO NỘI DUNG" in docs["X3_CUAVAO_TEMPLATE.md"]),
        ("X3E khai nguyên văn schema file máy sinh mà máy thực thi", all(t in docs["X3E_EMAIL_TEMPLATE.md"] for t in ["conv_id", "nguoi_gui", "thoi_diem", "tieu_de", "eml_sha256", "operation_id", "_so/_thu_staging/"])),
        # PILOT vòng 38: hai luật do vận hành thật phơi ra
        ("điền lần đầu mục CHƯA TỪNG có giá trị là mức B, đổi giá trị đã điền vẫn C", "ĐIỀN LẦN ĐẦU một mục CHƯA TỪNG mang giá trị" in docs["X0_CAUHINH_TEMPLATE.md"] and "CHỐT CHỐNG LÁCH" in docs["X0_CAUHINH_TEMPLATE.md"] and all("CHƯA TỪNG" in docs[k] for k in ("X5_HESO_TEMPLATE.md", "INSTRUCTION"))),
        ("mức của ĐIỀN LẦN ĐẦU khớp nhau ở cả ba nơi khai, không nơi nào nói A", all("CHƯA TỪNG" in d and re.search(r"ĐIỀN LẦN ĐẦU[\s\S]{0,260}?(?:mức B|, là\s*\n?\s*B)", d) and not re.search(r"ĐIỀN LẦN ĐẦU[\s\S]{0,60}?mức A", d) for d in [docs["X0_CAUHINH_TEMPLATE.md"], docs["X5_HESO_TEMPLATE.md"], docs["INSTRUCTION"]])),
        ("số ngoại lệ C11 khai đúng bằng số ngoại lệ liệt kê", ("BA ngoại lệ" in docs["X0_CAUHINH_TEMPLATE.md"]) == (len(re.findall(r"\((\d)\) ", docs["X0_CAUHINH_TEMPLATE.md"].split("# C11.")[1].split("# C12.")[0])) == 3)),
        ("README cấm git pull và stash trong kho, kèm lối thoát, không khuyên ngược", "ĐỪNG chạy `git pull` trong 00_Index" in docs["README.md"] and "git stash pop" in docs["README.md"] and not re.search(r"(nên|cứ|hãy)\s+`?git\s+(pull|stash)", docs["README.md"], re.I)),
        ("nâng cấp chở CẢ script, INSTRUCTION và MỐC VERSION, không chỉ _TEMPLATE", "chép ĐÈ" in docs["X9_CAIDAT.md"] and all(t in docs["X9_CAIDAT.md"] for t in ["INSTRUCTION_WORKOPS_v*.md", "README.md", "X9_CAIDAT.md", "DOC_TRUOC.md", "kiem_van_hanh.py", "kiem_tra_bo.py"]) and "Bỏ nhóm" in docs["X9_CAIDAT.md"] and "LƯỚI RÀ" in docs["X9_CAIDAT.md"]),
        ("CHỐT CHỐNG LÁCH giữ nguyên vế khóa C11 và C12, không bị đảo ngược", "Bản thân hai danh sách C11 và C12 cũng thuộc nhóm khóa" in docs["X0_CAUHINH_TEMPLATE.md"] and not re.search(r"C11 và C12 (KHÔNG|không) thuộc nhóm khóa", docs["X0_CAUHINH_TEMPLATE.md"])),
        ("X9 mục 4 ĐÁNH DẤU dòng C12, không xóa, khớp C11 ngoại lệ 2", "ĐÁNH DẤU dòng C12" in docs["X9_CAIDAT.md"] and "xóa dòng khỏi C12" not in docs["X9_CAIDAT.md"]),
        ("KHÔNG chỗ nào khai nhóm (b) của nâng cấp là tùy chọn", not re.search(r"[Nn]hóm \(b\)[^.]{0,60}(TÙY CHỌN|tùy chọn|bỏ cũng được|không bắt buộc)", docs["X9_CAIDAT.md"])),
        ("nâng cấp đọc X9 mục 3c của BẢN MỚI, không đọc bản trong kho", "CỦA BẢN MỚI" in docs["X9_CAIDAT.md"] and "THƯ MỤC BẢN MỚI" in docs["README.md"]),
        ("mốc vòng vá ở DOC_TRUOC khớp vòng mới nhất của GHICHU", (lambda a, b: bool(a and b and int(a.group(1)) == max(int(x) for x in b)))(re.search(r"vòng vá (\d+)", docs["DOC_TRUOC.md"]), re.findall(r"## Vòng (\d+)", kem[ghichu[0].name]))),
        ("X0 khai luật viết dấu chưa điền để rà 0i đọc được", "Ô CHƯA ĐIỀN của X0 viết bằng ĐÚNG MỘT khuôn" in docs["X0_CAUHINH_TEMPLATE.md"]),
        ("chuyển _lich_su không làm mất dấu mã G", "_lich_su" in docs["X5_HESO_TEMPLATE.md"] and "giữ nguyên ô \"Ghi lần\"" in docs["X5_HESO_TEMPLATE.md"]),
        ("một cửa một phiên ĐANG GHI là luật CORE, không riêng PARALLEL", "MỌI profile, kể cả LITE" in docs["X5_HESO_TEMPLATE.md"]),
        ("ô Ghi lần là danh sách chỉ-thêm, cấm ghi đè mã lượt trước", "CHỈ-THÊM" in docs["X5_HESO_TEMPLATE.md"]),
        ("người vận hành là tham số có thật để bàn giao đổi", "@VANHANH.NGUOI" in docs["X0_CAUHINH_TEMPLATE.md"] and "đổi @VANHANH.NGUOI ở C6" in docs["X0_CAUHINH_TEMPLATE.md"]),
        ("có chỗ khai nơi phát hành bộ để biết bản mới sau khi gỡ .git", "@NHIP.BANMOI" in docs["X0_CAUHINH_TEMPLATE.md"] and "@NHIP.BANMOI" in docs["X5_HESO_TEMPLATE.md"]),
        ("kho đang chạy không phải bản làm việc git, cài xong gỡ .git kể cả ở thư mục cha", "XÓA `00_Index\\.git`" in docs["X9_CAIDAT.md"] and "CẤM `git pull`" in docs["X9_CAIDAT.md"] and "THƯ MỤC CHA" in docs["X9_CAIDAT.md"] and "git stash" in docs["README.md"]),
    ]
    thieu_luat = [t for t, dk in _luat if not dk]
    kiem(f"12. luật nghiệp vụ then chốt có mặt ({len(_luat)} luật)",
         not thieu_luat and len(_luat) == 73,
         str(thieu_luat) + (f" · đếm được {len(_luat)} luật mà bộ khai 73: bớt"
                            f" luật là bớt lưới không ai hay; đổi số thì sửa"
                            f" con số này trong CÙNG lượt vá"
                            if len(_luat) != 73 else ""))

    phep_fuzz(goc)


    # 10. Tham chiếu chéo "X<k> mục <n>" và "INSTRUCTION mục <n>" phải trỏ tới mục có thật
    muc_cua = {}
    for k in ["X1_CAM_TEMPLATE.md", "X2_PHATHANH_TEMPLATE.md", "X3_CUAVAO_TEMPLATE.md",
              "X4_RASOAT_TEMPLATE.md", "X5_HESO_TEMPLATE.md"]:
        muc_cua["X" + k[1]] = set(re.findall(r"^# (\d+[a-z]?)\.", docs[k], re.M))
    muc_cua["X3E"] = set(re.findall(r"^# (\d+[a-z]?)\.", docs["X3E_EMAIL_TEMPLATE.md"], re.M))
    muc_cua["X9"] = set(re.findall(r"^# (\d+[a-z]?)\.", docs["X9_CAIDAT.md"], re.M))
    muc_cua["INSTRUCTION"] = set(re.findall(r"^# (\d+[a-z]?)\.", docs["INSTRUCTION"], re.M))
    sai_ref = []
    for ten, nd in docs.items():
        for dich, n in re.findall(r"(X[1-5]E?|X9|INSTRUCTION)\s+mục\s+(\d+[a-z]?)", nd):
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

    # 14. ĐIỂM DANH PHÉP, đặt CUỐI cùng: xóa trọn một phép thì bộ vẫn in "sạch,
    #     đóng gói được" và dòng của nó chỉ lặng lẽ biến mất - hội đồng vòng 15
    #     xóa được cả phép 13, sản phẩm đầu bảng của vòng 42.
    _da = {t.split(" ")[0] for t in DA_KIEM} | {"14."}  # tự điểm danh mình
    thieu_phep = [pp for pp in PHEP_BAT_BUOC if pp not in _da]
    kiem("14. điểm danh: đủ mọi phép bắt buộc đã chạy", not thieu_phep,
         f"phép {thieu_phep} biến khỏi lượt chạy. Xóa một phép mà bộ vẫn 'sạch'"
         f" là lưới tự mất không ai hay; thêm phép lại, hay khai vào"
         f" PHEP_BAT_BUOC trong CÙNG lượt vá")

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
