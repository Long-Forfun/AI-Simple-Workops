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
    "X1_CAM_TEMPLATE.md": 2900,   # hạ vòng 83 làm BÙ cho X5 (X1 dùng ~1.900)
    "X2_PHATHANH_TEMPLATE.md": 4200,
    "X3_CUAVAO_TEMPLATE.md": 5500,   # 5b gate khi dán chat; nâng vòng 37: phần tăng nằm trọn trong 5b gated
    "X3E_EMAIL_TEMPLATE.md": 13000,  # gate: chỉ nạp khi bật EMAIL; nay 92,3% trần
    "X4_RASOAT_TEMPLATE.md": 5500,  # chỉ đọc khi RA_SOAT, không phải thuế thường trực
    "X5_HESO_TEMPLATE.md": 20300,  # mục 1b, 7b gate; nâng vòng 43 (nợ) rồi
    # vòng 83 cho neo QUYETDINH - BÙ bằng hạ X1 xuống 2900, tổng trần luật giữ
    "X9_CAIDAT.md": 8500,  # gate: đọc MỘT LẦN mỗi công ty, KHÔNG nạp vào CHAT, ngoài mọi route
    "README.md": 9000,  # file người dùng đọc ĐẦU TIÊN: dài là mất người trước khi cài xong
    "WORKOPS_STARTER_v24_20260824_GOP.md": 260000,  # bản gộp để đánh giá, KHÔNG nạp
    # vào phiên nào; vòng 46 gỡ hai script ra nên hạ trần 400.000 xuống 260.000
    "kiem_tra_bo.py": 210000,   # ngoài mọi route, và từ vòng 46 KHÔNG còn
    # trong bản gộp: file này không tốn token của phiên nào. Trần ở đây chỉ là
    # tín hiệu BẢO TRÌ. Nâng vòng 47 cho phép 15 (danh mục trạng thái); ràng
    # buộc thật của nó là 14, 14b, 14c và 15 phải xanh, không phải số ký tự
    "kiem_van_hanh.py": 195000,  # ngoài route, nhưng ĐẦU RA dán vào phiên RA_SOAT;
    # trần THẬT của file này là phép 13b và 13c trên ĐẦU RA, số ký tự chỉ là
    # proxy. Nâng vòng 47 cho 7f, 7g, 3g và các vá của hội đồng vòng 17; hai
    # trần ĐẦU RA vẫn xanh, tức thứ người dùng THẬT SỰ trả tiền không tăng
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
                 "5.", "5c.", "6.", "7.", "9.", "9b.", "10.", "11.", "12.", "13.", "13b.", "1f.",
                 "13c.", "13d.", "14.", "14b.", "14c.", "14d.", "14e.", "15.", "15b.", "2d.", "9c."]
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
    # backup ngày của lượt ghi mẫu: kho lành phải LÀM MẪU đúng X5 mục 7,
    # không thì LƯU Ý 0m2 in trên chính kho lành và 13b/13d phình oan
    (idx / "_so" / "_lich_su" / "backup_20260828").mkdir(parents=True)
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
    # hạn 2099: ngày trong fixture phải là TƯƠNG LAI XA, không thì phép 8e
    # (đếm quá hạn) đổi kết quả theo ngày chạy thật và ca hỏng dần (vòng 51)
    _ghi(so / "VIEC.md", v + NL + "| DA1 | V-DA1-001 | Viec mot | buoc sau | toi | |"
         " 2099-12-31 | XONG | | " + G + " |" + NL)  # XONG: ca I2 chuyển _lich_su
    # theo X5 mục 5 chỉ đúng luật với việc XONG hay HỦY (hội đồng vòng 15b)
    for t in ["DUKIEN.md", "TAILIEU.md", "QUYETDINH.md", "PLANNING.md", "THU.md"]:
        _ghi(so / t, (so / t).read_text(encoding="utf-8").replace("<MÃ>", "FUZ"))
    dk = (so / "DUKIEN.md").read_text(encoding="utf-8").rstrip(NL)
    _ghi(so / "DUKIEN.md", dk + NL + "| DA1 | D-DA1-001 | Gia von hang A |"
         " 120000 | 2026-08-01 | noi bo | bao gia NCC | B | HIỆU LỰC |"
         " 2098-01-01 | " + G + " |" + NL)  # lane DUKIEN của 3g cần dòng
    # lành để quan sát HAI CHIỀU - mutant đọc lệch cột báo oan mà suite
    # vẫn xanh khi kho lành trống lane này (giám khảo rubric 08, m08)
    pl = (so / "PLANNING.md").read_text(encoding="utf-8").rstrip(NL)
    _ghi(so / "PLANNING.md", pl + NL + "| P-001 | 2098-01-01 | DA1 | mini |"
         " Viec mot | X5 muc 3 | VIEC.md | V-DA1-001 | thap | ĐÃ GHI | " + G
         + " |" + NL)  # 2098: plan ĐÃ GHI quá 30 ngày phải chuyển _lich_su,
    # ngày quá khứ làm kho lành tự hỏng dần theo thời gian thật (khuôn 2099
    # của VIEC, vòng 51); lane PLANNING của 3g nhờ dòng này được quan sát
    # HAI CHIỀU - trước đây mutant đọc lệch cột báo oan mà mọi ca vẫn xanh
    _ghi(idx / "_moc_ghi.txt", G + NL)
    # X5 mục 3 bước 6 BẮT nối mã G vào neo ngoài _so. Thiếu nó thì vế I2 của
    # phép 13 đang khẳng định một kho THIẾU NEO là "đúng luật", nhánh PASS của
    # 0k chưa từng được quan sát, và trần 13b/13c đo trên đầu ra mang sẵn một
    # dòng LƯU Ý không đáng có (hội đồng vòng 16).
    _ghi(so / "X0_INDEX.md", "# X0_INDEX · FUZ" + NL * 2 + "```yaml" + NL
         + "may_sinh: true · sinh_boi: " + G + " · x0_rev: 1 · instruction: v11"
         + NL + "```" + NL)
    _ghi(so / "BANG_DIEU_KHIEN.md", "# BANG_DIEU_KHIEN · FUZ" + NL * 2 + "```yaml" + NL
         + "may_sinh: true · sinh_boi: " + G + " · x0_rev: 1" + NL
         + "watermark: CUA1=" + G + NL + "```" + NL * 2 + "bàn sạch · mốc: chưa có" + NL)
    return kho, idx, so, G


RA_SOAT_VAN = [""]   # toàn văn đầu ra của lượt _ra_soat gần nhất


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
    K.CHO_VAO_SO.clear()   # cộng dồn qua các lượt trong CÙNG tiến trình thì
    # mọi fixture chạy hai lượt đọc ra con số sai
    try:
        sys.argv = ["kvh", str(idx), str(kho)]
        with contextlib.redirect_stdout(_io2.StringIO()) as _bva:
            try:
                K.main(idx)
            except SystemExit:
                pass  # main() kết thúc bằng sys.exit theo số lệch, không phải lỗi
        RA_SOAT_VAN[0] = _bva.getvalue()
    finally:
        sys.argv = argv
    return set(K.loi)


# Phép 15 đi từ NGHĨA VỤ, không đi từ danh sách phép. Mỗi dòng X4 mà chính X4
# khai là "dò được bằng máy" phải có ÍT NHẤT MỘT trạng thái mẫu ở đây, và rà
# soát phải kêu khi gặp nó. Dòng nào X4 khai máy dò mà không dựng nổi ca là
# LỜI KHAI VƯỢT CÁI MÁY LÀM - lớp lỗi mà cả bốn defect nặng của vòng 46 đều
# thuộc về. Miễn trừ phải ghi LÝ DO, và phải RỖNG DẦN.
X4_MAY_DO = {1, 2, 3, 4, 5, 12, 17, 19, 22, 23, 24, 31}
X4_MIEN = {3: "X4 tự khai kiểm TAY (hai kho cùng giữ bản cuối)",
           5: "X4 tự khai kiểm TAY (file 99_Goc chưa có sha256)",
           24: "nhóm EMAIL: cần fixture profile EMAIL có nhật ký và registry;"
               " phép 12 canh riêng, danh mục trạng thái chưa với tới",
           31: "nhóm EMAIL: như trên"}


def phep_danh_muc(goc):
    """Phép 15: DANH MỤC TRẠNG THÁI HỎNG. Trả (hong, phu, so_ca)."""
    import tempfile
    import hashlib
    import kiem_van_hanh as K15

    TL = ("| DA1 | T-{ma} | {ten} | v1 | 2026-08-28 | {noi} | HIỆN HÀNH |"
          " ĐANG DÙNG | 2026-08-28 | quan sat | doi tac | | | {sha} | {G} |")

    def _sha(s):
        return hashlib.sha256(s.encode("utf-8")).hexdigest()

    def _noi(p, d):
        _ghi(p, p.read_text(encoding="utf-8").rstrip(NL) + NL + d + NL)

    # ---- các trạng thái, mỗi cái gắn ĐÚNG dòng nghĩa vụ của X4 ----
    def s1a(k, i, so, G):
        (so / "QUYETDINH.md").unlink()

    def s1b(k, i, so, G):
        _noi(so / "TAILIEU.md", TL.format(ma="001", ten="Hop dong A",
             noi="Kho 01_Phap_ly\\hopdong_a.pdf", sha="", G=G))

    def s2(k, i, so, G):
        (k / "01_Phap_ly").mkdir(exist_ok=True)
        _ghi(k / "01_Phap_ly" / "hopdong_moi.md", "noi dung")

    def s4a(k, i, so, G):
        (k / "99_Goc").mkdir(exist_ok=True)
        _ghi(k / "99_Goc" / "goc_a.md", "ban goc")
        _noi(so / "TAILIEU.md", TL.format(ma="002", ten="Ban goc a",
             noi="Kho 99_Goc\\goc_a.md", sha=_sha("khac han"), G=G))

    def s4b(k, i, so, G):
        (k / "01_Phap_ly").mkdir(exist_ok=True)
        _ghi(k / "01_Phap_ly" / "hd.pdf", "BAN DA BI SUA DE")
        _noi(so / "TAILIEU.md", "| DA1 | T-004 | Hop dong da ky | v1 |"
             " 2026-08-28 | Kho 01_Phap_ly\\hd.pdf | HIỆN HÀNH | ĐÃ KÝ |"
             " 2026-08-28 | ban giay | doi tac | | | "
             + _sha("ban goc luc ky") + " | " + G + " |")

    def s4c(k, i, so, G):
        """ô "Ở đâu" gõ "kho " thường: 9, 10a, 10b BỎ QUA lặng lẽ dòng này."""
        (k / "01_Phap_ly").mkdir(exist_ok=True)
        _ghi(k / "01_Phap_ly" / "hd.pdf", "BAN DA BI SUA DE")
        _noi(so / "TAILIEU.md", "| DA1 | T-005 | Hop dong da ky | v1 |"
             " 2026-08-28 | kho 01_Phap_ly\\hd.pdf | HIỆN HÀNH | ĐÃ KÝ |"
             " 2026-08-28 | ban giay | doi tac | | | "
             + _sha("ban goc luc ky") + " | " + G + " |")

    def s12a(k, i, so, G):
        _ghi(so / "VIEC.md", (so / "VIEC.md").read_text(encoding="utf-8")
             .rstrip(NL) + NL + "| DA1 | V-DA1-001 | Viec trung ma | buoc |"
             " toi | | 2026-12-31 | MỚI | | " + G + " |" + NL)

    def s12b(k, i, so, G):
        _ghi(so / "VIEC.md", (so / "VIEC.md").read_text(encoding="utf-8")
             .replace("| XONG | | " + G, "| XONG | Q-999 | " + G))

    def s17(k, i, so, G):
        _ghi(i / "X0_CAUHINH_FUZ.md",
             (i / "X0_CAUHINH_FUZ.md").read_text(encoding="utf-8")
             .replace("instruction_yeu_cau: v11", "instruction_yeu_cau: v99"))

    def s19a(k, i, so, G):
        _ghi(so / "NHATKY_2026Q3.md",
             (so / "NHATKY_2026Q3.md").read_text(encoding="utf-8")
             .replace("| XONG |", "| ĐANG GHI |"))

    def s19b(k, i, so, G):
        _ghi(so / "VIEC.md", (so / "VIEC.md").read_text(encoding="utf-8")
             .replace(" | " + G + " |", " |  |"))

    def s22(k, i, so, G):
        _ghi(so / "VIEC.md", (so / "VIEC.md").read_text(encoding="utf-8")
             .rstrip(NL) + NL + NL.join(
                 f"| DA1 | V-DA1-{n:03d} | Viec {n} | buoc | toi | |"
                 f" 2026-12-31 | MỚI | | {G} |" for n in range(2, 620)) + NL)

    def s23(k, i, so, G):
        G2 = "G-20260828-CUA1-02"
        _ghi(so / "NHATKY_2026Q3.md",
             (so / "NHATKY_2026Q3.md").read_text(encoding="utf-8").rstrip(NL)
             + NL + "| " + G2 + " | 2026-08-28 | CUA1.1000.c3d4 | C |"
             " doi cau truc so | VIEC V-DA1-001 | khong | XONG | khong |" + NL)
        for cu, moi in [(" | " + G + " |", " | " + G + " " + G2 + " |")]:
            _ghi(so / "VIEC.md", (so / "VIEC.md")
                 .read_text(encoding="utf-8").replace(cu, moi))
        b = (so / "BANG_DIEU_KHIEN.md").read_text(encoding="utf-8")
        _ghi(so / "BANG_DIEU_KHIEN.md", b.replace("CUA1=" + G, "CUA1=" + G2)
             .replace("sinh_boi: " + G, "sinh_boi: " + G2))

    # ---- trạng thái ĐÚNG LUẬT: không được kêu (vế chống báo oan) ----
    def L1(k, i, so, G):
        (k / "99_Goc").mkdir(exist_ok=True)
        _ghi(k / "99_Goc" / "goc_b.md", "ban goc b")
        _noi(so / "TAILIEU.md", TL.format(ma="003", ten="Ban goc b",
             noi="Kho 99_Goc\\goc_b.md", sha=_sha("ban goc b"), G=G))

    def L2(k, i, so, G):
        (k / "01_Phap_ly").mkdir(exist_ok=True)
        _ghi(k / "01_Phap_ly" / "a.md", "a")
        _noi(so / "TAILIEU.md", TL.format(ma="006", ten="Bo ho so",
             noi="Kho 01_Phap_ly\\", sha="", G=G))

    def L3(k, i, so, G):
        _noi(so / "TAILIEU.md", TL.format(ma="007", ten="Tai lieu Drive",
             noi="Drive 1AbC_dEf", sha="", G=G))

    DANH_MUC = [
        (1, "sổ lõi QUYETDINH vắng trên đĩa", s1a, True),
        (1, "TAILIEU khai file mà kho không có", s1b, True),
        (2, "file trên kho chưa vào TAILIEU", s2,
         "sạch về ràng buộc, nhưng 1 mục chờ vào sổ"),
        (4, "sha256 khai khác nội dung thật", s4a, True),
        (4, "mốc ĐÃ KÝ bị sửa đè tại chỗ", s4b, True),
        (4, 'ô "Ở đâu" gõ "kho" thường: tắt lặng lẽ 9, 10a, 10b', s4c, True),
        (12, "mã V trùng giữa hai dòng", s12a, True),
        (12, "ô Liên kết trỏ mã không tồn tại", s12b, True),
        (17, "X0 khai instruction_yeu_cau bản không có thật", s17, True),
        (19, "NHATKY còn ĐANG GHI", s19a, True),
        (19, "lượt XONG mà sổ chạm chưa mang mã ghi", s19b, True),
        (22, "sổ vượt ngưỡng lưu trữ mà chưa tách", s22, True),
        (23, "lượt mức C đã ghi mà không có plan", s23, True),
    ]
    LANH = [("file thật, sha256 thật", L1),
            ("dòng trỏ THƯ MỤC, sha256 bỏ trống", L2),
            ("dòng dạng Drive (một trong bốn dạng)", L3)]

    hong, phu = [], set()
    cu_on = K15.KHOANG_ON_DINH

    def _chay(sua):
        """Dựng kho lành, ép trạng thái, quét HAI lượt (luật ổn định), trả
        (tập lệch, toàn văn đầu ra). Hạ KHOANG_ON_DINH về 0 để fixture không
        phải chờ thật - không hạ thì mọi ca quan sát file báo LỌT OAN."""
        with tempfile.TemporaryDirectory() as td:
            kho, idx, so, G = _kho_song(goc, td)
            if _ra_soat(idx, kho):
                return None, ""
            sua(kho, idx, so, G)
            K15.KHOANG_ON_DINH = 0
            try:
                _ra_soat(idx, kho)          # lượt nạp mốc ổn định
                lech = _ra_soat(idx, kho)   # lượt đủ luật ổn định hai lần
                return lech, RA_SOAT_VAN[0]
            finally:
                K15.KHOANG_ON_DINH = cu_on

    for x4, ten, sua, mong in DANH_MUC:
        lech, van = _chay(sua)
        if lech is None:
            hong.append(f"X4#{x4} {ten}: KHO LÀNH đã lệch sẵn, ca không tin được")
            continue
        phu.update(l.split(" ")[0] for l in lech)
        if mong is True and not lech:
            hong.append(f"X4#{x4} {ten}: trạng thái HỎNG mà không phép nào kêu")
        elif isinstance(mong, str) and mong not in van:
            hong.append(f"X4#{x4} {ten}: đầu ra không có \"{mong}\"")
    for ten, sua in LANH:
        lech, _ = _chay(sua)
        if lech is None:
            hong.append(f"LÀNH {ten}: KHO LÀNH đã lệch sẵn")
        elif lech:
            hong.append(f"LÀNH {ten}: ĐÚNG LUẬT mà bị báo {sorted(lech)[:2]}")

    # vế còn lại: dòng X4 khai máy dò mà DANH MỤC chưa có ca nào
    co_ca = {x for x, _, _, _ in DANH_MUC}
    thieu = sorted(X4_MAY_DO - co_ca - set(X4_MIEN))
    if thieu:
        hong.append(f"X4 khai máy dò dòng {thieu} mà danh mục chưa có ca nào")
    return hong, phu, len(DANH_MUC) + len(LANH)


def phep_fuzz(goc, phu_them=()):
    """Phép 13: hai BẤT BIẾN đối xứng, đo bằng cách ép trạng thái thật.
    I1  mọi trạng thái làm MẤT dấu mã G phải sinh ÍT NHẤT MỘT lệch
    I2  mọi trạng thái ĐÚNG LUẬT không được sinh lệch nào
    Vế I2 chính là thứ vòng 38, 40 và 41 vi phạm ba lần: vá một lỗ rồi quay
    ra phạt người dùng vì làm đúng. Không có lưới này thì lớp lỗi đó chỉ lộ
    khi có hội đồng chạy tay (hội đồng vòng 14 đo được 14,2 phần trăm trạng
    thái mất dấu đi im)."""
    import tempfile
    import shutil
    # phu_them: tập phép mà PHÉP 15 đã ép kêu. 14b từng chỉ nhìn tập phủ của
    # phép 13, nên tám phép nghiệp vụ nặng nhất phải nằm trong MIEN_TRU dù
    # phép 15 canh chúng thật (hội đồng vòng 17: 8/8 đột biến vào vùng miễn
    # trừ lọt, 10/10 con ngoài vùng đó bị bắt)
    hong, phu, _dem = [], set(phu_them), {"I1": 0, "I2": 0, "I3": 0}

    def _sua(f, cu, moi):
        _ghi(f, f.read_text(encoding="utf-8").replace(cu, moi))

    def _san_tam():
        """Sân tạm DỌN ĐƯỢC cả đường dẫn quá 260 ký tự.

        TemporaryDirectory dọn bằng rmtree trần nên gãy WinError 145 ở ca thư
        mục sâu quá MAX_PATH - đúng ca mà phép 9 (gốc dài) cần tới."""
        import contextlib as _cl, os as _os, shutil as _sh, tempfile as _tf

        @_cl.contextmanager
        def _ct():
            _td = _tf.mkdtemp()
            try:
                yield _td
            finally:
                _p = _td
                if _os.name == "nt" and not _td.startswith("\\\\"):
                    _p = "\\\\?\\" + _os.path.abspath(_td)
                _sh.rmtree(_p, ignore_errors=True)

        return _ct()

    def thu(ten, sua, mat_dau):
        _dem["I1" if mat_dau else "I2"] += 1
        with _san_tam() as td:
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
    thu3("PLANNING trỏ mã việc không tồn tại (ô liên kết ngoài VIEC/QUYETDINH)",
         lambda k, i, so, G, sua: _ghi(so / "PLANNING.md",
             (so / "PLANNING.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| P-20260828-07 | 2026-08-28 | DA1 | sua file | V-DA1-999 |"
             " x | x | x | x | MỚI | |" + NL), "7c.")

    thu3("dấu ``` mở mà KHÔNG đóng (nuốt trọn phần đuôi sổ)",
         lambda k, i, so, G, sua: _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL * 2
             + "```" + NL
             + "| DA1 | V-DA1-077 | Viec that | b | toi | | 2099-12-31 |"
               " MỚI | | " + G + " |" + NL), "5e.")

    def _ca_tilde(k, i, so, G, sua):
        """ĐÚNG LUẬT: ví dụ bảng bọc trong ~~~ - fence GFM hợp lệ ngang ```,
        và là khuôn BUỘC phải dùng khi nội dung bên trong có backtick."""
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL * 2
             + "~~~" + NL
             + "| VD | V-999 | Viec vi du | b | ai | | 2020-01-01 | ĐANG LÀM |"
               " | |" + NL + "~~~" + NL)

    thu("ví dụ bảng bọc trong ~~~ (không được kêu)", _ca_tilde, False)

    import os as _os_ca
    if _os_ca.name == "nt":
        def _ca_hoa_thuong(k, i, so, G, sua):
            """Đĩa có HopDong.md, sổ khai hopdong.md: NTFS cho qua nên 9 im,
            đồng bộ sang Linux hay git checkout là mất file (vòng 22)."""
            (k / "03_Phap_ly").mkdir(exist_ok=True)
            _ghi(k / "03_Phap_ly" / "HopDong.md", "x")
            _ghi(so / "TAILIEU.md",
                 (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL)
                 + NL + "| DA1 | T-087 | Hop dong C | v01 | 2026-08-20 |"
                   " Kho 03_Phap_ly/hopdong.md | HIỆN HÀNH | NHÁP |"
                   " 2026-08-20 | qs | noi bo | | | | " + G + " |" + NL)

        thu3("sổ khai hopdong.md, đĩa là HopDong.md (NTFS cho qua)",
             _ca_hoa_thuong, "9d.")

    def _ca_junction_goc(k, i, so, G, sua):
        """99_Goc là junction (nt) / symlink (posix) trỏ RA NGOÀI kho: file
        sau link qua hết 9/10a/10b nhưng sao lưu và git không mang chúng."""
        import os as _os, subprocess as _sp
        ngoai = k.parent / "ngoai_kho"
        ngoai.mkdir(exist_ok=True)
        _ghi(ngoai / "goc.md", "x")
        dich = k / "99_Goc"
        if _os.name == "nt":
            _sp.run(["cmd", "/c", "mklink", "/J", str(dich), str(ngoai)],
                    capture_output=True)
        else:
            _os.symlink(ngoai, dich)

    thu3("99_Goc là junction trỏ ra ngoài kho", _ca_junction_goc, "0q.")

    def _dong_tl2(so, G, k, o_dau, trang_thai, sha=""):
        (k / "03_Phap_ly").mkdir(exist_ok=True)
        _ghi(k / "03_Phap_ly" / "hd.md", "x")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-085 | Hop dong B | v01 | 2026-08-20 | " + o_dau
             + " | HIỆN HÀNH | " + trang_thai + " | 2026-08-20 | qs |"
               " noi bo | | | " + sha + " | " + G + " |" + NL)

    thu3("mốc ghi 'ĐÃ KÝ (bản scan 19/8)' mà ô sha trống",
         lambda k, i, so, G, sua: _dong_tl2(so, G, k, "Kho 03_Phap_ly/hd.md",
                                            "ĐÃ KÝ (bản scan 19/8)"), "10d.")

    def _ca_bo_ho_so_nop(k, i, so, G, sua):
        """ĐÚNG LUẬT: BỘ HỒ SƠ đã nộp thầu - dòng trỏ THƯ MỤC kết thúc `\\`,
        X0 C1 bắt BỎ TRỐNG ô sha. Đòi sha ở đây là bắt người dùng làm trái
        luật của chính bộ."""
        (k / "03_Phap_ly").mkdir(exist_ok=True)
        (k / "03_Phap_ly" / "ThauA").mkdir(exist_ok=True)
        _ghi(k / "03_Phap_ly" / "ThauA" / "x.md", "x")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-086 | Bo ho so thau A | v01 | 2026-08-20 |"
               " Kho 03_Phap_ly/ThauA\\ | HIỆN HÀNH | ĐÃ NỘP | 2026-08-20 |"
               " qs | noi bo | | | | " + G + " |" + NL)

    thu("bộ hồ sơ ĐÃ NỘP trỏ thư mục, sha trống (không được kêu)",
        _ca_bo_ho_so_nop, False)

    def _dong_tl(so, G, k, het_han):
        (k / "03_Phap_ly").mkdir(exist_ok=True)
        _ghi(k / "03_Phap_ly" / "gp.md", "x")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-084 | Giay phep con | v01 | 2026-08-20 |"
               " Kho 03_Phap_ly/gp.md | HIỆN HÀNH | NHÁP | 2026-08-20 | qs |"
               " noi bo | " + het_han + " | | | " + G + " |" + NL)

    thu3("ô Hết hạn ghi 30/06/2027 kiểu Việt (bộ đếm câm)",
         lambda k, i, so, G, sua: _dong_tl(so, G, k, "30/06/2027"), "3h.")

    def _ca_iso_kem_chu(k, i, so, G, sua):
        """ĐÚNG LUẬT: ô mang ngày ISO kèm ghi chú - dem_qua_han đọc bằng
        re.search nên vẫn THẤY ngày; 3h không được tố. Người dùng cũng GHI
        MỐC vào bảng đúng X5 m3 b6 - 8e không được tố."""
        _dong_tl(so, G, k, "2098-01-31 (gia hạn)")
        sua(so / "BANG_DIEU_KHIEN.md", "mốc: chưa có", "mốc: 2098-01-31")

    thu("ô ngày ISO kèm ghi chú chữ (không được kêu)", _ca_iso_kem_chu, False)

    def _ca_dong_info(k, i, so, G, sua):
        """ĐÚNG LUẬT: trong khối ``` có một dòng ```bash - CommonMark nói dòng
        ĐÓNG không được mang info string, nên nó là RUỘT chứ không phải dòng
        đóng. Máy nào cho nó đóng sớm thì ruột ví dụ lòi ra thành dòng thật."""
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL * 2
             + "```" + NL + "```bash" + NL
             + "| DA1 | V-DA1-001 | Viec mau, dung chep | b | ai | |"
               " 2020-01-01 | ĐANG LÀM | | |" + NL + "```" + NL)

    thu("dòng ```bash nằm trong khối ``` (không được kêu)", _ca_dong_info,
        False)

    def _ca_mo_nhay(k, i, so, G, sua):
        """ĐÚNG LUẬT: dòng văn xuôi mở đầu bằng ```ma`lenh``` - info string
        của fence nháy KHÔNG được chứa nháy (CommonMark 4.5), nên dòng này là
        chữ thường. Máy nào coi nó là dòng MỞ thì khối ví dụ ngay dưới bị lộn
        ngược: dấu mở thành dấu đóng và ruột ví dụ lộ ra."""
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL * 2
             + "```ma`lenh``` la cach go lenh trong dong" + NL * 2
             + "```" + NL
             + "| DA1 | V-DA1-001 | Viec mau, dung chep | b | ai | |"
               " 2020-01-01 | ĐANG LÀM | | |" + NL + "```" + NL)

    thu("dòng chữ ```ma`lenh``` đứng trước khối ví dụ (không được kêu)",
        _ca_mo_nhay, False)

    def _ca_duongdan_truoc(k, i, so, G, sua):
        """ĐÚNG LUẬT: ô Ở đâu trỏ thư mục kết thúc `\\` gõ sát dấu ngăn (ứng
        viên TRƯỚC), ô Căn cứ mang `\\|` thoát THẬT (ứng viên SAU). Chọn đúng
        phải nhờ điểm ưu-tiên-đường-dẫn, vì hoà thì lấy phía sau là SAI."""
        (k / "10_HoSo").mkdir(exist_ok=True)
        (k / "10_HoSo" / "NhanSu").mkdir(exist_ok=True)
        _ghi(k / "10_HoSo" / "NhanSu" / "b.md", "x")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-082 | Bien ban hop | v01 | 2026-08-20 |"
               " Kho 10_HoSo/NhanSu\\|HIỆN HÀNH | NHÁP | 2026-08-20 |"
               " qs \\| mail | noi bo | | | | " + G + " |" + NL)

    thu("đường dẫn sát dấu TRƯỚC, `\\|` chữ SAU (không được kêu)",
        _ca_duongdan_truoc, False)

    def _ca_hoa_phia_sau(k, i, so, G, sua):
        """ĐÚNG LUẬT: ô Tài liệu mang `\\|` thoát THẬT mà chữ trước nó cũng
        trông như đường dẫn (Mau C:\\Bieu), ô Ở đâu trỏ thư mục sát dấu ngăn.
        Hai ứng viên CÙNG điểm - hoà phải lấy phía SAU mới ra ô Ở đâu đúng."""
        (k / "10_HoSo").mkdir(exist_ok=True)
        (k / "10_HoSo" / "NhanSu").mkdir(exist_ok=True)
        _ghi(k / "10_HoSo" / "NhanSu" / "c.md", "x")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-083 | Mau C:\\Bieu \\| loi cu | v01 | 2026-08-20 |"
               " Kho 10_HoSo/NhanSu\\|HIỆN HÀNH | NHÁP | 2026-08-20 | qs |"
               " noi bo | | | | " + G + " |" + NL)

    thu("hai ứng viên cùng điểm, ứng viên đúng ở SAU (không được kêu)",
        _ca_hoa_phia_sau, False)

    def _ca_bang_long_muc(k, i, so, G, sua):
        """Bảng lồng trong MỘT MỤC danh sách: Markdown vẫn render ra bảng, mà
        thụt bốn dấu cách nên dong_bang và mọi bộ đếm KHÔNG thấy. Giám khảo
        vòng 23 đòi MIỄN ca này; tôi giữ 5b kêu, vì miễn là để một dòng sổ
        THẬT đặt ở đó mất im lặng. Chỉ lời khuyên được sửa."""
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL * 2
             + "- Mức A" + NL
             + "  - ví dụ bảng con:" + NL * 2
             + "    | Mã | Việc |" + NL
             + "    |---|---|" + NL
             + "    | V-900 | x |" + NL)

    thu3("bảng lồng trong mục danh sách (vẫn tàng hình với bộ đếm)",
         _ca_bang_long_muc, "5b.")

    def _ca_nga_trong_nhay(k, i, so, G, sua):
        """ĐÚNG LUẬT: khối ``` có RUỘT là một dòng ~~~ (ghi chú dạy nhau cách
        mở khối bằng dấu ngã). ngoai_fence xử đúng, nhưng 5e đếm ký tự nên
        thấy dấu ~ LẺ và báo oan - hai bộ đọc fence bằng hai luật khác nhau."""
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL * 2
             + "```" + NL + "~~~" + NL + "```" + NL)

    thu("khối ``` có ruột là một dòng ~~~ (không được kêu)", _ca_nga_trong_nhay,
        False)

    def _ca_bon_nhay(k, i, so, G, sua):
        """ĐÚNG LUẬT: CommonMark 4.5 đòi fence ĐÓNG dài KHÔNG KÉM fence MỞ, nên
        muốn dán ví dụ có chứa ``` thì bắt buộc bọc ngoài bằng bốn nháy. So
        mỗi KÝ TỰ mà quên ĐỘ DÀI thì dòng ``` bên trong đóng sớm, ruột ví dụ
        lòi ra thành dòng bảng thật và ăn lệch mã trùng."""
        _dong = ("| DA1 | V-DA1-001 | Viec mau, dung chep | b | ai | |"
                 " 2020-01-01 | ĐANG LÀM | | |")
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL * 2
             + "````" + NL + "```" + NL + _dong + NL + "```" + NL
             + "````" + NL)

    thu("ví dụ bọc bốn nháy, ruột có ``` (không được kêu)", _ca_bon_nhay,
        False)

    def _ca_thoat_va_thumuc(k, i, so, G, sua):
        r"""ĐÚNG LUẬT HAI LẦN trong MỘT dòng: ô Tài liệu mang dấu | viết theo
        GFM là `\|`, ô Ở đâu trỏ BỘ HỒ SƠ nên kết thúc bằng `\` (X0 C1) và gõ
        SÁT dấu ngăn. Tách trọn GFM hụt một ô, tách trọn THÔ dôi một ô - lối
        được-ăn-cả-ngã-về-không của vòng 38 bó tay (hội đồng vòng 23)."""
        (k / "10_HoSo").mkdir(exist_ok=True)
        (k / "10_HoSo" / "NhanSu").mkdir(exist_ok=True)
        _ghi(k / "10_HoSo" / "NhanSu" / "a.md", "x")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-081 | Bao cao Q1 \\| Q2 | v01 | 2026-08-20 |"
               " Kho 10_HoSo/NhanSu\\|HIỆN HÀNH | NHÁP | 2026-08-20 | qs |"
               " noi bo | | | | " + G + " |" + NL)

    thu("một dòng vừa có `\\|` thoát vừa trỏ thư mục (không được kêu)",
        _ca_thoat_va_thumuc, False)

    def _ca_thoat_that(k, i, so, G, sua):
        r"""ĐÚNG LUẬT: ô mang dấu | viết theo GFM là `\|` - cách DUY NHẤT hợp lệ.
        Tách THÔ thì dòng dôi một ô và phép 5 tố oan, nên lối GFM phải còn."""
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-078 | Bao gia A \\| B | v01 | 2026-08-20 |"
               " Kho 03_Thuong_mai/bg.md | HIỆN HÀNH | NHÁP | 2026-08-20 | qs |"
               " noi bo | | | | " + G + " |" + NL)
        (k / "03_Thuong_mai").mkdir(exist_ok=True)
        _ghi(k / "03_Thuong_mai" / "bg.md", "x")

    thu("ô mang dấu | thoát theo GFM (không được kêu)", _ca_thoat_that, False)

    def _ca_fence_long(k, i, so, G, sua):
        """ĐÚNG LUẬT: ví dụ bọc trong ~~~ vì bên trong CÓ dòng ```. Đóng khối
        bằng ký tự bất kỳ thì ``` cắt sớm, phần đuôi lòi ra thành dòng bảng."""
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL * 2
             + "~~~" + NL + "```" + NL
             + "| VD | V-998 | Viec vi du | b | ai | | 2020-01-01 |"
               " ĐANG LÀM | | |" + NL
             + "```" + NL + "~~~" + NL)

    thu("ví dụ ~~~ có ``` lồng bên trong (không được kêu)", _ca_fence_long,
        False)

    def _ca_fence_le_doi(k, i, so, G, sua):
        """MỘT dấu ``` và MỘT dấu ~~~ : đếm CHUNG thì thành 2 - chẵn - và cả
        phần đuôi sổ tàng hình mà 5e im. Đếm RIÊNG theo ký tự mới thấy lẻ."""
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL * 2
             + "```" + NL + "~~~" + NL)

    thu3("một dấu ``` và một dấu ~~~ (mỗi loại đều lẻ)", _ca_fence_le_doi,
         "5e.")

    def _ca_duong_dai(k, i, so, G, sua):
        """Đường dẫn vượt 260 ký tự: Windows đòi tiền tố đường dẫn dài, thiếu
        nó thì phép 9 tuyên file ĐÃ MẤT trong khi tầng quan sát THẤY nó - hai
        lời khai ngược nhau trong MỘT lượt chạy (hội đồng vòng 22)."""
        import os as _os
        sau = "d" * 60
        rel = "/".join([sau] * 4)
        goc = k
        if _os.name == "nt" and not str(k).startswith("\\\\"):
            goc = Path("\\\\?\\" + str(Path(k).resolve()))
        (goc / rel).mkdir(parents=True, exist_ok=True)
        (goc / rel / "sau.md").write_text("x", encoding="utf-8", newline=NL)
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-079 | Ho so sau | v01 | 2026-08-20 | Kho " + rel
             + "/sau.md | HIỆN HÀNH | NHÁP | 2026-08-20 | qs | noi bo | | | | "
             + G + " |" + NL)

    thu("file thật ở đường dẫn quá 260 ký tự (không được kêu)", _ca_duong_dai,
        False)

    def _ca_thumuc_sat(k, i, so, G, sua):
        """ĐÚNG LUẬT: dòng trỏ BỘ HỒ SƠ kết thúc bằng \\ (X0 C1 BẮT BUỘC), bảng
        gõ SÁT dấu | (khuôn GFM hợp lệ). Hai luật của bộ cùng lúc."""
        (k / "03_Thuong_mai").mkdir(exist_ok=True)
        _ghi(k / "03_Thuong_mai" / "a.md", "x")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "|DA1|T-077|Bo ho so|v01|2026-08-20|Kho 03_Thuong_mai\\|"
               "HIỆN HÀNH|NHÁP|2026-08-20|qs|noi bo||||" + G + "|" + NL)

    thu("dòng trỏ thư mục, bảng gõ sát dấu | (không được kêu)",
        _ca_thumuc_sat, False)

    thu3("dòng bảng thụt SÂU bốn dấu cách (Markdown coi là khối code)",
         lambda k, i, so, G, sua: _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "    | DA1 | V-DA1-088 | Viec | b | toi | | 2099-12-31 |"
               " MỚI | | " + G + " |" + NL), "5b.")

    thu3("dòng thân bảng BỎ dấu | đầu (Prettier, markdownlint --fix)",
         lambda k, i, so, G, sua: _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "DA1 | V-DA1-089 | Viec | b | toi | | 2099-12-31 | dang lam |"
               " |  |" + NL), "3g.")

    def _ca_2b(k, i, so, G, sua):
        """View khai profile LITE trong khi X0 đã bật REGULATED và EMAIL: phiên
        AI đọc view NÀY trước, rồi chạy công ty REGULATED ở chế độ LITE - không
        nghi thức mức C, không plan cho thay đổi chạy thật (hội đồng vòng 20)."""
        sua(i / "X0_CAUHINH_FUZ.md", "  [ ] REGULATED", "  [x] REGULATED")
        _p = so / "X0_INDEX.md"
        _ghi(_p, _p.read_text(encoding="utf-8").rstrip(NL) + NL
             + "profile: LITE" + NL)

    thu3("X0_INDEX khai profile LITE trong khi X0 bật REGULATED", _ca_2b, "2b.")

    thu3("X0 khai HAI cửa CUA1 trỏ hai gốc khác nhau (chia đôi kho)",
         lambda k, i, so, G, sua: sua(i / "X0_CAUHINH_FUZ.md",
             "CUA1 = " + str(k) + " · thiet bi MAY1",
             "CUA1 = " + str(k) + " · thiet bi MAY1" + NL
             + "                 CUA1 = D:\\KHO_2024 · thiet bi MAY9"), "0i3.")

    _HDR_V = ("| Dự án | Mã | Việc | Bước tiếp theo | Ai làm | Chờ ai từ |"
              " Hạn | Trạng thái | Liên kết | Ghi lần |")
    _KE_V = "|---|---|---|---|---|---|---|---|---|---|"

    thu3("ô Trạng thái mang ký tự vô hình (dán từ web hay Word)",
         lambda k, i, so, G, sua: sua(so / "NHATKY_2026Q3.md",
                                      "| XONG |", "| XO\u200bNG |"), "3g.")

    def _ca_5d(k, i, so, G, sua):
        """Khối thứ hai đảo hai cột Hạn và Chờ ai từ: mọi dòng vẫn CÙNG SỐ ô
        nên phép 5 xanh, mà bộ đếm quá hạn đọc nhầm ô (hội đồng vòng 21)."""
        _dao = _HDR_V.replace("| Chờ ai từ | Hạn |", "| Hạn | Chờ ai từ |")
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL * 2
             + "## KHOI2" + NL * 2 + _dao + NL + _KE_V + NL
             + "| DA1 | V-DA1-055 | Nop ho so thau | b | toi | 2099-12-31 | |"
               " MỚI | | " + G + " |" + NL)

    thu3("khối thứ hai của sổ đảo thứ tự cột", _ca_5d, "5d.")

    def _ca_5d_lanh(k, i, so, G, sua):
        """ĐÚNG LUẬT: khối thứ hai dùng ĐÚNG header chuẩn - nhiều khối là cách
        X5 dặn tách dự án, không được phạt."""
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL * 2
             + "## KHOI2" + NL * 2 + _HDR_V + NL + _KE_V + NL
             + "| DA1 | V-DA1-056 | Nop ho so thau | b | toi | | 2099-12-31 |"
               " MỚI | | " + G + " |" + NL)

    thu("sổ có khối thứ hai dùng đúng header (không được kêu)", _ca_5d_lanh, False)

    def _ca_10d(k, i, so, G, sua):
        """Hợp đồng ĐÃ KÝ, file có thật, mà ô sha256 BỎ TRỐNG: 10a và 10b bỏ
        qua trọn dòng nên bản đã ký hết lưới toàn vẹn (hội đồng vòng 21)."""
        (k / "99_Goc").mkdir(exist_ok=True)
        _ghi(k / "99_Goc" / "HopDong_v01.md", "ban goc")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-010 | Hop dong | v1 | 2026-01-01 |"
               " Kho 99_Goc\\HopDong_v01.md | HIỆN HÀNH | ĐÃ KÝ | 2026-01-01 |"
               " doi tac | doi tac | | GỐC | | " + G + " |" + NL)

    thu3("mốc ĐÃ KÝ mà ô sha256 bỏ trống", _ca_10d, "10d.")

    def _ca_catmuc(k, i, so, G, sua):
        """Một câu trỏ chéo "# C3." trong C1 từng làm lát cắt C2 RỖNG, và cả
        ba nhánh 7b tự tắt vì chúng bọc `if ... and _da_khai` (vòng 21)."""
        sua(i / "X0_CAUHINH_FUZ.md", "# C2. Dự án",
            "Folder khối của kho: xem # C3. bên dưới." + NL * 2 + "# C2. Dự án")
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| CDW | V-CDW-001 | Viec du an ma | b | toi | | 2099-12-31 |"
               " MỚI | | " + G + " |" + NL)

    thu3("câu trỏ chéo \"# C3.\" trong C1 làm 7b tự tắt", _ca_catmuc, "7b.")

    thu3("mã G trùng ở cột Mã ghi của NHATKY",
         lambda k, i, so, G, sua: _ghi(so / "NHATKY_2026Q3.md",
             (so / "NHATKY_2026Q3.md").read_text(encoding="utf-8").rstrip(NL)
             + NL + "| " + G + " | 2026-08-28 | CUA1.1100.zz | A | viec hai |"
             " khong | khong | XONG | khong |" + NL), "3b.")

    thu3("BANG_DIEU_KHIEN phình quá trần runtime",
         lambda k, i, so, G, sua: _ghi(so / "BANG_DIEU_KHIEN.md",
             (so / "BANG_DIEU_KHIEN.md").read_text(encoding="utf-8")
             + NL + "x" * 4300 + NL), "1b.")

    thu3("X0_INDEX phình quá trần runtime",
         lambda k, i, so, G, sua: _ghi(so / "X0_INDEX.md",
             (so / "X0_INDEX.md").read_text(encoding="utf-8")
             + NL + "y" * 2500 + NL), "1c.")

    thu3("hai bản X0 đang chạy cùng lúc",
         lambda k, i, so, G, sua: _ghi(i / "X0_CAUHINH_ABC.md",
             (i / "X0_CAUHINH_FUZ.md").read_text(encoding="utf-8")), "0c.")

    thu3("THU.md vắng khi pipeline EMAIL đã có dấu vết",
         lambda k, i, so, G, sua: _ghi(so / "_thu_da_nap.json", "[]")
             or (so / "THU.md").unlink(), "0e.")

    thu3("file lạ nấp trong _so/_lich_su",
         lambda k, i, so, G, sua: (so / "_lich_su").mkdir(exist_ok=True)
             or _ghi(so / "_lich_su" / "VIEC_2025.md.bak", "x"), "0j.")

    thu3("bản conflicted copy nấp trong _so/_lich_su",
         lambda k, i, so, G, sua: (so / "_lich_su").mkdir(exist_ok=True) or _ghi(
             so / "_lich_su" / "NHATKY_2026Q2 (Long's conflicted copy).md",
             "| G-20260515-CUA1-02 | 2026-05-15 | CUA1.0900.zz | C | ky phu luc"
             " | TAILIEU | khong | XONG | khong |" + NL), "0b.")

    thu3("sổ lõi bị cắt còn 0 byte (đồng bộ hay ghi đè cắt cụt)",
         lambda k, i, so, G, sua: _ghi(so / "TAILIEU.md", ""), "0p.")

    def _ca_d2(k, i, so, G, sua):
        """secret trong README.md và trong .py NGOÀI 00_Index: miễn trừ theo
        TÊN FILE làm mọi README, mọi .gitignore và MỌI .py ở bất kỳ đâu thành
        vùng miễn dịch (hội đồng vòng 20, lỗi của bản vá vòng 58)."""
        (k / "02_Ky_thuat").mkdir(exist_ok=True)
        _ghi(k / "02_Ky_thuat" / "README.md",
             "DB=postgresql://cdv:Pr0dBacha2026x@10.0.0.9:5432/cdv" + NL)

    thu3("secret trong README.md của thư mục nghiệp vụ", _ca_d2, "7e2.")

    def _ca_baohanh(k, i, so, G, sua):
        """ĐÚNG LUẬT: dự án đã thanh lý mà nghĩa vụ bảo hành còn chạy - giữ
        việc mở là ĐÚNG SỰ THẬT, chuyển sang HỦY mới là khai sai."""
        sua(i / "X0_CAUHINH_FUZ.md",
            "@DUAN.DA1        Du an mot                    đang chạy",
            "@DUAN.DA1        Du an mot                    đang chạy" + NL
            + "@DUAN.BVH        Benh vien Hoa Lu             NGỪNG"
              " (bảo hành tới 2099-12-31)")
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| BVH | V-BVH-008 | Bao hanh he thong | kiem dinh ky | toi | |"
               " 2099-12-31 | ĐANG LÀM | | " + G + " |" + NL)

    thu("dự án NGỪNG còn bảo hành, việc mở (không được kêu)", _ca_baohanh, False)

    def _ca_khocu(k, i, so, G, sua):
        """ĐÚNG LUẬT: tài liệu ở KHO CŨ khai dạng thứ năm - kho cũ chỉ tra lịch
        sử và có thể offline nên 7f, 9, 10a, 10b đều phải im. Trước vòng 61
        KHÔNG dạng nào hợp lệ: mọi công ty vừa chuyển kho hoặc ôm lệch vĩnh
        viễn hoặc nhân đôi kho (hội đồng vòng 19)."""
        _p = so / "TAILIEU.md"
        _ghi(_p, _p.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-091 | Hop dong 2022 | v1 | 2022-03-04 |"
             " KhoCu 01_Phap_ly\\HD_2022.pdf | HIỆN HÀNH | ĐÃ KÝ | 2022-03-04 |"
             " doi tac | doi tac | | | | " + G + " |" + NL)

    thu("tài liệu ở kho cũ khai dạng KhoCu (không được kêu)", _ca_khocu, False)

    def _ca_7h(k, i, so, G, sua):
        """Phiên hẹn giờ tự chốt mức C và GỬI công văn ra ngoài công ty."""
        sua(i / "X0_CAUHINH_FUZ.md", "  [ ] AUTOMATED", "  [x] AUTOMATED")
        _p = so / "NHATKY_2026Q3.md"
        _ghi(_p, _p.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| G-20260828-CUA1-19 | 2026-08-28 | CUA1.AUTO.0300.z9q | C |"
             " phat hanh va GUI cong van giuc thanh toan cho chu dau tu |"
             " VIEC V-DA1-001 | khong | XONG | khong |" + NL)

    thu3("phiên AUTOMATED tự chốt mức C và gửi ra ngoài", _ca_7h, "7h.")

    def _ca_7h_b(k, i, so, G, sua):
        """Phiên hẹn giờ tự ghi mức B - X0 C0 chỉ cho AUTOMATED mức A; ca cũ
        chỉ thử mức C nên mutant thu hẹp ('B' ra khỏi lưới) sống (tự quét
        vòng 88)."""
        sua(i / "X0_CAUHINH_FUZ.md", "  [ ] AUTOMATED", "  [x] AUTOMATED")
        _p = so / "NHATKY_2026Q3.md"
        _ghi(_p, _p.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| G-20260828-CUA1-20 | 2026-08-28 | CUA1.AUTO.0400.y8p | B |"
             " tu cap nhat bang tong hop tuan | VIEC V-DA1-001 | khong |"
             " XONG | khong |" + NL)

    thu3("phiên AUTOMATED tự ghi mức B (chỉ được mức A)", _ca_7h_b, "7h.")

    def _ca_7h_lanh(k, i, so, G, sua):
        """ĐÚNG LUẬT: phiên AUTO mức A, chuẩn bị và mở dòng chờ duyệt - đó
        chính là việc bộ MUỐN máy làm."""
        sua(i / "X0_CAUHINH_FUZ.md", "  [ ] AUTOMATED", "  [x] AUTOMATED")
        G2 = "G-20260828-CUA1-19"
        _p = so / "NHATKY_2026Q3.md"
        _ghi(_p, _p.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| " + G2 + " | 2026-08-28 | CUA1.AUTO.0300.z9q | A |"
             " quet mail dem, xep 3 thu cho duyet | VIEC V-DA1-001 | khong |"
             " XONG | khong |" + NL)
        sua(so / "VIEC.md", " | " + G + " |", " | " + G + " " + G2 + " |")
        _b = so / "BANG_DIEU_KHIEN.md"
        _ghi(_b, _b.read_text(encoding="utf-8")
             .replace("CUA1=" + G, "CUA1=" + G2)
             .replace("sinh_boi: " + G, "sinh_boi: " + G2))

    thu("phiên AUTOMATED mức A chuẩn bị và chờ duyệt (không được kêu)",
        _ca_7h_lanh, False)

    thu3("dòng NHATKY thụt một dấu cách (Prettier, dán từ Word)",
         lambda k, i, so, G, sua: _ghi(so / "NHATKY_2026Q3.md",
             (so / "NHATKY_2026Q3.md").read_text(encoding="utf-8").rstrip(NL)
             + NL + " | G-20260828-CUA1-02 | 2026-08-28 | CUA1.0300.zz | A |"
             " viec | VIEC V-DA1-001 | khong | ĐANG GHI | khong |" + NL), "3a.")

    thu3("mật khẩu ghi bằng NHÃN TIẾNG VIỆT trong ô sổ",
         lambda k, i, so, G, sua: _ghi(so / "DUKIEN.md",
             (so / "DUKIEN.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | D-051 | Ghi chu | Mat khau: Congtruong@2026x |"
             " 2026-01-01 | NOI_BO | doi tac | A | ĐÃ KIỂM | 2099-05-01 | "
             + G + " |" + NL), "7e.")

    def _ca_13m(k, i, so, G, sua):
        """Quyết định tự khai người kế nhiệm mà vẫn đứng HIỆN HÀNH: sổ có hai
        dòng nói ngược nhau về cùng một việc (hội đồng vòng 19)."""
        _p = so / "QUYETDINH.md"
        _ghi(_p, _p.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| Q-20260828-03 | 2026-08-28 | chon ABB | vi z | mat x |"
             " HIỆN HÀNH | Q-20260828-04 | " + G + " |" + NL
             + "| Q-20260828-04 | 2026-08-28 | quay lai Schneider | vi z |"
             " mat x | HIỆN HÀNH | | " + G + " |" + NL)

    thu3("QUYETDINH khai Thay bởi mà vẫn HIỆN HÀNH", _ca_13m, "13m.")

    def _ca_13m_lanh(k, i, so, G, sua):
        """ĐÚNG LUẬT: dòng cũ ĐÃ THAY trỏ dòng mới, dòng mới HIỆN HÀNH."""
        _p = so / "QUYETDINH.md"
        _ghi(_p, _p.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| Q-20260828-03 | 2026-08-28 | chon ABB | vi z | mat x |"
             " ĐÃ THAY | Q-20260828-04 | " + G + " |" + NL
             + "| Q-20260828-04 | 2026-08-28 | quay lai Schneider | vi z |"
             " mat x | HIỆN HÀNH | | " + G + " |" + NL)

    thu("chuỗi QUYETDINH thay đúng cách (không được kêu)", _ca_13m_lanh, False)

    def _ca_0n(k, i, so, G, sua):
        """Cache mang mốc TƯƠNG LAI: mọi file lập tức "đủ ổn định" nên bộ công
        nhận HIỆN HÀNH một file có thể đang ghi dở (backlog (k), vòng 55)."""
        import json as _js0n
        _ghi(so / "_quan_sat_truoc.json", _js0n.dumps(
            {"v": 2, "luc": 32503680000,
             "files": {"01_Phap_ly/x.md": {"sha": "0" * 64,
                                           "luc": 32503680000}}}))

    thu3("cache quan sát mang mốc tương lai", _ca_0n, "0n.")

    def _ca_0n_lanh(k, i, so, G, sua):
        """ĐÚNG LUẬT: cache máy sinh bình thường, mốc trong quá khứ."""
        import json as _js0n2
        import time as _t0n2
        # files RỖNG là hình dạng ĐÚNG cho kho chưa có file nghiệp vụ nào -
        # kho lành của phép 13 chính là vậy. Trỏ một file không có thật thì
        # chính bộ quan sát kêu, và ca mất nghĩa.
        _ghi(so / "_quan_sat_truoc.json", _js0n2.dumps(
            {"v": 2, "luc": _t0n2.time() - 600, "files": {}}))

    thu("cache quan sát máy sinh bình thường (không được kêu)", _ca_0n_lanh, False)

    def _ca_0m(k, i, so, G, sua):
        """Nơi sao lưu ĐÃ KHAI và có thật, nhưng bỏ bê từ lâu."""
        _tm = k.parent / "saoluu_ngoai_kho"
        _tm.mkdir(exist_ok=True)
        _ghi(_tm / "backup_cu.md", "ban sao cu")
        import os as _os0m
        _os0m.utime(_tm / "backup_cu.md", (0, 0))
        sua(i / "X0_CAUHINH_FUZ.md", "@KHO.SAOLUU      <điền: thư mục NGOÀI",
            "@KHO.SAOLUU      " + str(_tm) + " · mỗi ngày" + NL
            + "@KHO.SAOLUU_CU   <điền: thư mục NGOÀI")

    thu3("nơi sao lưu ngoài kho đã khai mà bỏ bê từ lâu", _ca_0m, "0m.")

    def _ca_11b(k, i, so, G, sua):
        """Đối tác gửi lại bản sửa; Chrome đặt tên " (1)". Bản MỚI bị loại
        lặng lẽ và người dùng được chỉ vào bản CŨ NHẤT (hội đồng vòng 18)."""
        (k / "04_Trao_doi").mkdir(exist_ok=True)
        _ghi(k / "04_Trao_doi" / "BienBanNghiemThu.docx", "ban mot: 1.720 ty")
        _ghi(k / "04_Trao_doi" / "BienBanNghiemThu (1).docx",
             "ban hai: giam 5 phan tram, con 1.634 ty")

    thu3("bản mới đối tác gửi mang khuôn \" (1)\" bị bỏ lặng lẽ", _ca_11b, "11b.")

    def _ca_11b_lanh(k, i, so, G, sua):
        """ĐÚNG LUẬT: bản sao đồng bộ THẬT - cùng tên, CÙNG nội dung."""
        (k / "04_Trao_doi").mkdir(exist_ok=True)
        _ghi(k / "04_Trao_doi" / "PhuLuc01.docx", "y het nhau")
        _ghi(k / "04_Trao_doi" / "PhuLuc01 (1).docx", "y het nhau")

    thu("bản sao đồng bộ thật, cùng nội dung (không được kêu)",
        _ca_11b_lanh, False)

    def _ca_8e(k, i, so, G, sua):
        """Bảng khai "bàn sạch" trong lúc sổ còn một việc quá hạn từ 2019.
        Hội đồng vòng 18 dựng được kho có chứng thư số hết hạn 59 ngày, việc
        quá hạn và dữ kiện quá mốc rà lại 119 ngày mà bảng vẫn "bàn sạch"."""
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | V-DA1-007 | Viec qua han | buoc | toi | | 2019-01-05 |"
             " ĐANG LÀM | | " + G + " |" + NL)

    thu3("bảng khai bàn sạch mà sổ còn việc quá hạn từ 2019", _ca_8e, "8e.")

    def _ca_8e_lanh(k, i, so, G, sua):
        """ĐÚNG LUẬT: việc còn hạn XA, bảng vẫn được khai bàn sạch."""
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | V-DA1-008 | Viec con han | buoc | toi | | 2099-12-31 |"
             " ĐANG LÀM | | " + G + " |" + NL)

    thu("việc còn hạn xa, bảng khai bàn sạch (X4 dòng 9)", _ca_8e_lanh, False)

    thu3("gõ CUA2 ở ô Phiên của kho MỘT CỬA (cửa ma)",
         lambda k, i, so, G, sua: sua(so / "NHATKY_2026Q3.md",
                                      "| CUA1.0900.a1b2 |", "| CUA2.0900.a1b2 |"),
         "7b.")

    def _ca_env(k, i, so, G, sua):
        """.env trần: quet_ho loại dotfile TRƯỚC lưới secret, nên tên file
        secret phổ biến nhất chưa bao giờ tới được 7e2 (hội đồng vòng 18)."""
        (k / "02_Ky_thuat").mkdir(exist_ok=True)
        _ghi(k / "02_Ky_thuat" / ".env", "DB_PASSWORD=Sup3rS3cretPass99" + NL)

    thu3("file .env trần trong kho (đi qua lọc dotfile)", _ca_env, "7e2.")

    def _ca_che(k, i, so, G, sua):
        """_quan_sat_bo.txt là file NGƯỜI DÙNG SỬA TAY ĐƯỢC: nó dùng để bớt ồn
        khi quan sát tài liệu, KHÔNG được tự miễn luật X5 mục 1b."""
        (k / "02_Ky_thuat").mkdir(exist_ok=True)
        _ghi(k / "02_Ky_thuat" / "prod.pem", "-----BEGIN RSA PRIVATE KEY-----" + NL)
        _ghi(so / "_quan_sat_bo.txt", "02_Ky_thuat" + NL)

    thu3("secret bị _quan_sat_bo.txt che", _ca_che, "7e2.")

    def _ca_1d(k, i, so, G, sua):
        """X0 của kho ĐANG CHẠY phình quá trần runtime. NGAN_SACH chỉ chấm bản
        TEMPLATE trong bộ mẫu, nên trước vòng 48 file mà phiên CHAT thật sự
        nạp nguyên vẹn không ai đo (hội đồng vòng 17: 49.591 ký tự vẫn sạch)."""
        _p = i / "X0_CAUHINH_FUZ.md"
        _ghi(_p, _p.read_text(encoding="utf-8")
             + NL + "<!-- " + "x" * 25000 + " -->" + NL)

    thu3("X0 của kho đang chạy phình quá trần runtime", _ca_1d, "1d.")

    def _ca_7b2(k, i, so, G, sua):
        """TAILIEU đã tombstone theo Q-, mà dòng VIEC trỏ nó thì chưa."""
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-001 | [đã xóa theo Q-20260902-01] | v1 | 2026-08-28 |"
             " Kho 01_Phap_ly\\hd.pdf | HIỆN HÀNH | ĐÃ KÝ | 2026-08-28 | x |"
             " doi tac | | | | " + G + " |" + NL)
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | V-DA1-002 | Ban giao ho so khach | x | toi | |"
             " 2026-12-31 | MỚI | T-001 | " + G + " |" + NL)

    thu3("xóa pháp lý sót dòng khác còn trỏ tài liệu đã xóa", _ca_7b2, "7b2.")

    def _ca_7e3(k, i, so, G, sua):
        """File .env đối tác gửi rơi vào _INBOX - lối tự nhiên nhất."""
        _ghi(so / "_inbox" / "prod.env",
             "DATABASE_URL=postgres://u:S3cr3tPass99@db.x.vn:5432/d" + NL)

    thu3("file secret nằm trong _INBOX", _ca_7e3, "7e3.")

    def _ca_7e4(k, i, so, G, sua):
        """Dump CSDL chạy thật mang dữ liệu khách kéo về kho đồng bộ."""
        (k / "02_Ky_thuat").mkdir(exist_ok=True)
        _ghi(k / "02_Ky_thuat" / "qlkh_prod_dump_20260921.sql",
             "COPY khach_hang (id, ho_ten, cccd) FROM stdin;" + NL)

    thu3("dump CSDL chạy thật nằm trong kho đồng bộ", _ca_7e4, "7e4.")

    def _ca_lanh_mau(k, i, so, G, sua):
        """ĐÚNG LUẬT: file MẪU khai cấu hình, giá trị là <điền>. Không được kêu."""
        (k / "05_Mau").mkdir(exist_ok=True)
        _ghi(k / "05_Mau" / "cauhinh.env.example", "DATABASE_URL=<điền>" + NL)
        _ghi(so / "_inbox" / "cauhinh.env.sample", "API_KEY=<điền>" + NL)

    thu("file MẪU .example và .sample khai cấu hình (X5 mục 1b cho phép)",
        _ca_lanh_mau, False)

    def _dong_qd(so, G, chon="Dung Postgres"):
        _ghi(so / "QUYETDINH.md",
             (so / "QUYETDINH.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| Q-001 | 2026-08-28 | " + chon + " | re | it tien |"
               " HIỆN HÀNH | | " + G + " |" + NL)

    def _neo_qd(i, G, chon="Dung Postgres"):
        import hashlib as _hl, unicodedata as _ud
        _loi = _ud.normalize("NFC", "|".join(
            ["Q-001", "2026-08-28", chon, "re", "it tien"]))
        _ghi(i / "_moc_qd.txt",
             "Q-001 " + _hl.sha256(_loi.encode("utf-8")).hexdigest()[:12] + NL)

    def _ca_13n_sua(k, i, so, G, sua):
        """Sửa NỘI DUNG quyết định tại chỗ - thứ sổ tự cấm mà trước 13n không
        máy nào giữ (backlog a)."""
        _dong_qd(so, G)
        _neo_qd(i, G)
        sua(so / "QUYETDINH.md", "Dung Postgres", "Dung MySQL")

    thu3("sửa nội dung QUYETDINH tại chỗ (neo còn, sha lệch)", _ca_13n_sua,
         "13n.")

    def _ca_13n_xoa(k, i, so, G, sua):
        """Xóa TRỌN dòng quyết định - sổ cấm ("Không xóa dòng") mà trước 13n
        chỉ là lời tự khai; neo còn thì dòng biến mất phải kêu."""
        _dong_qd(so, G)
        _neo_qd(i, G)
        _nd = (so / "QUYETDINH.md").read_text(encoding="utf-8")
        _nd = NL.join(d for d in _nd.splitlines() if "Q-001" not in d)
        _ghi(so / "QUYETDINH.md", _nd + NL)

    thu3("xóa trọn dòng QUYETDINH (neo còn, dòng mất)", _ca_13n_xoa, "13n.")

    def _ca_13n_thay(k, i, so, G, sua):
        """ĐÚNG LUẬT: dòng cũ chỉ đổi HAI Ô QUẢN TRỊ (ĐÃ THAY + Thay bởi) -
        13n không được kêu, vì hai ô đó nằm ngoài sha."""
        _dong_qd(so, G)
        _neo_qd(i, G)
        _ghi(so / "QUYETDINH.md",
             (so / "QUYETDINH.md").read_text(encoding="utf-8")
             .replace("| HIỆN HÀNH | |", "| ĐÃ THAY | Q-002 |"))
        _ghi(so / "QUYETDINH.md",
             (so / "QUYETDINH.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| Q-002 | 2026-08-28 | Dung SQLite | re hon | don gian |"
               " HIỆN HÀNH | | " + G + " |" + NL)

    thu("QUYETDINH đổi hai ô quản trị theo luật ĐÃ THAY (không được kêu)",
        _ca_13n_thay, False)

    def _ca_13n_ghilan(k, i, so, G, sua):
        """ĐÚNG LUẬT HAI LẦN: lượt SAU đánh ĐÃ THAY và nối mã G của nó vào
        Ghi lần dòng cũ (X5 mục 3 bước 3 bắt nối với MỌI dòng chạm tới). Sha
        gồm Ghi lần thì người làm đúng cả hai luật ăn lệch oan (rubric 03).
        Lượt sau dựng ĐỦ nhân chứng: dòng NHATKY + watermark bảng."""
        _dong_qd(so, G)
        _neo_qd(i, G)
        G2 = "G-20260828-CUA1-02"
        _ghi(so / "NHATKY_2026Q3.md",
             (so / "NHATKY_2026Q3.md").read_text(encoding="utf-8").rstrip(NL)
             + NL + "| " + G2 + " | 2026-08-28 | CUA1.1700.ij | B |"
             " thay quyet dinh | QUYETDINH Q-001 | khong | XONG | khong |" + NL)
        b = (so / "BANG_DIEU_KHIEN.md").read_text(encoding="utf-8")
        _ghi(so / "BANG_DIEU_KHIEN.md", b.replace("CUA1=" + G, "CUA1=" + G2)
             .replace("sinh_boi: " + G, "sinh_boi: " + G2))
        sua(so / "QUYETDINH.md", "| HIỆN HÀNH | | " + G + " |",
            "| ĐÃ THAY | Q-002 | " + G + " " + G2 + " |")
        _ghi(so / "QUYETDINH.md",
             (so / "QUYETDINH.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| Q-002 | 2026-08-28 | Dung SQLite | re hon | don gian |"
               " HIỆN HÀNH | | " + G2 + " |" + NL)

    thu("nối mã G vào Ghi lần dòng ĐÃ THAY (không được kêu)",
        _ca_13n_ghilan, False)

    def _moi_truong_thu(i, so, G, trang_thai):
        """Môi trường EMAIL tối thiểu + một dòng THU: nhật ký rỗng, registry
        rỗng, @NHIP.HOPTHU khai - đủ cho cổng phép 12 không kêu oan."""
        _ghi(so / "_thu_nhat_ky.ndjson", "")
        _ghi(so / "_thu_da_nap.json", "[]")
        _p = i / "X0_CAUHINH_FUZ.md"
        _s = _p.read_text(encoding="utf-8")
        _s = _s.replace(
            "@NHIP.HOPTHU     (EMAIL) <điền HỘP THƯ NGHIỆP VỤ của CHÍNH công ty này. Một công ty một",
            "@NHIP.HOPTHU     (EMAIL) kinhdoanh@fuz.vn (một công ty một", 1)
        _ghi(_p, _s)
        _ghi(so / "THU.md",
             (so / "THU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | #L-001 | Bao gia dot 1 | <conv1@x> | doi_tac@x.vn |"
               " <m1@x> | 2026-08-28 | | " + trang_thai + " | | | | |"
               " V-DA1-001 | " + G + " |" + NL)

    thu3("ô Trạng thái THU ngoài từ vựng (lane THU của 3g)",
         lambda k, i, so, G, sua: _moi_truong_thu(i, so, G, "cho phan hoi"),
         "3g.")

    thu("dòng THU hợp lệ trong môi trường EMAIL tối thiểu (không được kêu)",
        lambda k, i, so, G, sua: _moi_truong_thu(i, so, G, "CHỜ TÔI"), False)

    thu3("ô Trạng thái THU bỏ RỖNG (với THU, rỗng cũng là lệch)",
         lambda k, i, so, G, sua: _moi_truong_thu(i, so, G, ""), "3g.")

    def _ca_7g_phat_hanh(k, i, so, G, sua):
        """'phat hanh ban 2.1 len <host chạy thật>' mức B: nêu ĐÍCH DANH host
        mà lọt vì thiếu động từ (giám khảo rubric vòng 02, ca g8)."""
        _p = i / "X0_CAUHINH_FUZ.md"
        _s = _p.read_text(encoding="utf-8")
        _m = re.search(r"^@DUAN\.PHANMEM.*$", _s, re.M)
        _ghi(_p, _s[:_m.end()] + NL
             + "  DA1  He ban le · repo github.com/cty/banle" + NL
             + "        · web · dev may doi, chạy thật banle.bacha.vn" + NL
             + "        · secret o Vault ·" + _s[_m.end():])
        _nk = so / "NHATKY_2026Q3.md"
        _ghi(_nk, _nk.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| G-20260828-CUA1-12 | 2026-08-28 | CUA1.1400.cd | B |"
             " phat hanh ban 2.1 len banle.bacha.vn |"
             " VIEC V-DA1-001 | khong | XONG | khong |" + NL)

    thu3("phat hanh lên host chạy thật mà ghi mức B", _ca_7g_phat_hanh, "7g.")

    thu3("ô Mức gõ chữ c thường (lách mà comment 3g tự khai)",
         lambda k, i, so, G, sua: sua(so / "NHATKY_2026Q3.md",
                                      "| A | mo viec V-DA1-001 |",
                                      "| c | mo viec V-DA1-001 |"), "3g.")

    thu("view khai du_an có CTY (X0 C2: luôn có - không được kêu)",
        lambda k, i, so, G, sua: sua(so / "X0_INDEX.md",
                                     " · instruction: v11",
                                     " · instruction: v11" + NL
                                     + "du_an: DA1, CTY"), False)

    def _ca_13m_qma(k, i, so, G, sua):
        """Dòng ĐÃ THAY mà Thay bởi trỏ Q KHÔNG TỒN TẠI: vế thứ hai của 13m -
        mutant or hóa _co_tb sống vì chưa ca nào ghim vế này (rubric 05)."""
        _ghi(so / "QUYETDINH.md",
             (so / "QUYETDINH.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| Q-001 | 2026-08-28 | Dung Postgres | re | it tien |"
               " ĐÃ THAY | Q-999 | " + G + " |" + NL)

    thu3("ĐÃ THAY mà Thay bởi trỏ Q không tồn tại", _ca_13m_qma, "13m.")

    def _ca_7g_vps(k, i, so, G, sua):
        """Máy chủ nội bộ KHÔNG dấu chấm ('chạy thật VPS-01'): trước vòng 89
        _host_pm rỗng và triển khai lên nó lọt cả 7g cứng lẫn mềm."""
        _p = i / "X0_CAUHINH_FUZ.md"
        _s = _p.read_text(encoding="utf-8")
        _m = re.search(r"^@DUAN\.PHANMEM.*$", _s, re.M)
        _ghi(_p, _s[:_m.end()] + NL
             + "  DA1  He noi bo · repo github.com/cty/nb · web · dev may"
               " doi, chạy thật VPS-01 · secret o Vault ·" + _s[_m.end():])
        _nk = so / "NHATKY_2026Q3.md"
        _ghi(_nk, _nk.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| G-20260828-CUA1-17 | 2026-08-28 | CUA1.2300.uv | B |"
             " trien khai ban moi len VPS-01 | VIEC V-DA1-001 | khong |"
             " XONG | khong |" + NL)

    thu3("triển khai lên máy chủ nội bộ không dấu chấm mà mức B", _ca_7g_vps,
         "7g.")

    def _ca_9e_thoat(k, i, so, G, sua):
        """Dòng TAILIEU trỏ '..' ra ngoài kho: mọi phép toàn vẹn sẽ đọc file
        KHÔNG thuộc công ty - chặn tại cửa (P0 vòng 96)."""
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-094 | Ho so ngoai | v01 | 2026-08-20 |"
               " Kho ..\\..\\ngoai_kho\\bi_mat.md | HIỆN HÀNH | NHÁP |"
               " 2026-08-20 | qs | noi bo | | | | " + G + " |" + NL)

    thu3("dòng sổ trỏ '..' ra ngoài kho", _ca_9e_thoat, "9e.")

    def _ca_9e_giua(k, i, so, G, sua):
        """'..' nằm GIỮA đường dẫn ('03_Phap_ly/../../ngoai') cũng thoát kho
        y hệt - mutant chỉ-bắt-đầu-chuỗi sống nếu không có ca này."""
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-095 | Ho so lach | v01 | 2026-08-20 |"
               " Kho 03_Phap_ly\\..\\..\\ngoai.md | HIỆN HÀNH | NHÁP |"
               " 2026-08-20 | qs | noi bo | | | | " + G + " |" + NL)

    thu3("dòng sổ giấu '..' giữa đường dẫn", _ca_9e_giua, "9e.")

    def _ca_7b_ngung(k, i, so, G, sua):
        """Dự án NGỪNG (thanh lý hẳn, không bảo hành) mà VIEC còn dòng ĐANG
        LÀM: vế thứ ba của 7b - chưa ca nào giữ (rubric 09, m10)."""
        sua(i / "X0_CAUHINH_FUZ.md",
            "@DUAN.DA1        Du an mot                    đang chạy",
            "@DUAN.DA1        Du an mot                    đang chạy" + NL
            + "@DUAN.DA2        Du an hai                    NGỪNG")
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA2 | V-DA2-001 | Viec sot | b | toi | | 2099-12-31 |"
               " ĐANG LÀM | | " + G + " |" + NL)

    thu3("dự án NGỪNG hẳn mà VIEC còn việc mở", _ca_7b_ngung, "7b.")

    def _ca_7b_baohanh(k, i, so, G, sua):
        """ĐÚNG LUẬT: NGỪNG (bảo hành tới ngày TƯƠNG LAI) thì việc bảo hành
        được GIỮ MỞ - rà thôi tố tới ngày ấy (X0 C2)."""
        sua(i / "X0_CAUHINH_FUZ.md",
            "@DUAN.DA1        Du an mot                    đang chạy",
            "@DUAN.DA1        Du an mot                    đang chạy" + NL
            + "@DUAN.DA3        Du an bao hanh"
              "               NGỪNG (bảo hành tới 2098-12-31)")
        _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA3 | V-DA3-001 | Bao hanh may | b | toi | | 2098-12-31 |"
               " ĐANG LÀM | | " + G + " |" + NL)

    thu("NGỪNG bảo hành còn hạn, việc bảo hành mở (không được kêu)",
        _ca_7b_baohanh, False)

    def _ca_7f_tombstone(k, i, so, G, sua):
        """ĐÚNG LUẬT: sau XÓA PHÁP LÝ, ô "Ở đâu" mang tombstone
        "[đã xóa theo Q-...]" (X5 mục 7b) - 7f phải miễn; chú thích 7f tự
        khai vá này từ vòng 19 mà chưa ca nào giữ (rubric 06, N3)."""
        _ghi(so / "QUYETDINH.md",
             (so / "QUYETDINH.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| Q-001 | 2026-08-28 | Xoa du lieu doi tac X | phap ly |"
               " mat lich su | HIỆN HÀNH | | " + G + " |" + NL)
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-091 | [đã xóa theo Q-001] | v01 | 2026-08-20 |"
               " [đã xóa theo Q-001] | HIỆN HÀNH | HẾT HIỆU LỰC |"
               " 2026-08-20 | qs | noi bo | | | | " + G + " |" + NL)

    thu("ô Ở đâu mang tombstone xóa pháp lý (không được kêu)",
        _ca_7f_tombstone, False)

    thu3("plan CHỜ CHỐT mà bảng vẫn bàn sạch (bộ đếm plan C treo)",
         lambda k, i, so, G, sua: _ghi(so / "PLANNING.md",
             (so / "PLANNING.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| P-002 | 2098-01-01 | DA1 | mini | Viec hai | X5 |"
               " VIEC.md | V-DA1-001 | thap | CHỜ CHỐT | |" + NL), "8e.")

    thu3("việc CHỜ ĐỐI TÁC quá ngưỡng mà bảng vẫn bàn sạch",
         lambda k, i, so, G, sua: _ghi(so / "VIEC.md",
             (so / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | V-DA1-003 | Cho bao gia | b | toi | 2020-01-01 |"
               " 2099-12-31 | CHỜ ĐỐI TÁC | | " + G + " |" + NL), "8e.")

    thu3("thư mục lạ rơi vào 00_Index", lambda k, i, so, G, sua:
         (i / "ban_nhap_cu").mkdir(), "0j.")

    thu3("dòng PLANNING thiếu ô (9/11) trong khối có header",
         lambda k, i, so, G, sua: _ghi(so / "PLANNING.md",
             (so / "PLANNING.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| P-003 | 2098-01-01 | DA1 | mini | Viec ba | X5 | VIEC.md |"
               " ĐANG LÀM | |" + NL), "5.")

    thu3("dòng bảng sai số ô trong KHỐI NỐI cuối sổ (không header)",
         lambda k, i, so, G, sua: _ghi(so / "PLANNING.md",
             (so / "PLANNING.md").read_text(encoding="utf-8").rstrip(NL)
             + NL * 2
             + "| P-004 | 2098-01-01 | DA1 | mini | Viec bon | X5 | VIEC.md |"
               " ĐANG LÀM | |" + NL), "5.")

    def _ca_8e_banner_day(k, i, so, G, sua):
        """Banner ĐẦY ĐỦ đúng khuôn INSTRUCTION (không nhãn hết hạn) + chứng
        thư đã quá hạn: nhánh đầy-đủ của 8e phải kêu thay vì chỉ so nhãn có
        mặt (rubric 07, N1)."""
        (k / "03_Phap_ly").mkdir(exist_ok=True)
        _ghi(k / "03_Phap_ly" / "ct2.md", "x")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-092 | Chung thu B | v01 | 2019-01-20 |"
               " Kho 03_Phap_ly/ct2.md | HIỆN HÀNH | NHÁP | 2019-01-20 | qs |"
               " noi bo | 2020-01-01 | | | " + G + " |" + NL)
        sua(so / "BANG_DIEU_KHIEN.md", "bàn sạch · mốc: chưa có",
            "quá hạn 0 · chờ đối tác 0 · plan C treo 0 · ĐANG GHI 0 · mail 0"
            " · mốc: chưa có")

    thu3("chứng thư quá hạn sau banner ĐẦY ĐỦ không nhãn hết hạn",
         _ca_8e_banner_day, "8e.")

    def _ca_8e_moc(k, i, so, G, sua):
        """Hạn ISO tương lai trên dòng sống mà bảng vẫn 'mốc: chưa có': lời
        hứa MỐC của X5 m3 b6 nay có máy (rubric 07, N1)."""
        (k / "03_Phap_ly").mkdir(exist_ok=True)
        _ghi(k / "03_Phap_ly" / "bh.md", "x")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-093 | Bao hanh may | v01 | 2026-08-20 |"
               " Kho 03_Phap_ly/bh.md | HIỆN HÀNH | NHÁP | 2026-08-20 | qs |"
               " noi bo | 2098-06-30 | | | " + G + " |" + NL)

    thu3("hạn tương lai mà bảng vẫn 'mốc: chưa có'", _ca_8e_moc, "8e.")

    def _ca_7e2_lon(k, i, so, G, sua):
        """Secret trong file VĂN BẢN 300 KB: trần đọc 2 MB cho văn bản là để
        bắt đúng ca này (vòng 19) mà chưa fixture nào ghim - đảo trần với
        256 KB nhị phân là nó lọt im (rubric 07, N2/M10)."""
        (k / "05_Bao_cao").mkdir(exist_ok=True)
        _ghi(k / "05_Bao_cao" / "ban_giao_moi_truong.md",
             ("# ban giao\n" + "x" * 300000 + "\n"
              "aws_secret_access_key = AKIAIOSFODNN7EXAMPLEKEY\n"))

    thu3("secret trong file văn bản 300 KB", _ca_7e2_lon, "7e2.")

    def _ca_7e2_nhiphan(k, i, so, G, sua):
        """File NHỊ PHÂN 300 KB chứa chuỗi giống secret: trần 256 KB miễn
        đọc là ĐÚNG thiết kế - không được kêu."""
        (k / "05_Bao_cao").mkdir(exist_ok=True)
        (k / "05_Bao_cao" / "anh_scan.zip").write_bytes(
            b"\x00" * 300000 + b"aws_secret_access_key=AKIA000000000EXAMPLE")

    thu("file nhị phân 300 KB chứa chuỗi giống secret (không được kêu)",
        _ca_7e2_nhiphan, False)

    def _ca_7d_phutrach(k, i, so, G, sua):
        """Khai đủ BẢY trường hạ tầng + dữ liệu mà thiếu NGƯỜI PHỤ TRÁCH:
        7d phải đòi - không biết ai gật thì mức C là cái gật của không ai."""
        _p = i / "X0_CAUHINH_FUZ.md"
        _s = _p.read_text(encoding="utf-8")
        _m = re.search(r"^@DUAN\.PHANMEM.*$", _s, re.M)
        _ghi(_p, _s[:_m.end()] + NL
             + "  DA1  He du trach · repo github.com/cty/dt · web · dev may"
               " doi, staging stg.dt.vn, chạy thật dt.bacha.vn" + NL
             + "        · secret o Vault · nhánh tự deploy main"
               " · CSDL chua ro ·" + _s[_m.end():])

    thu3("khai đủ hạ tầng mà thiếu người phụ trách vận hành", _ca_7d_phutrach,
         "7d.")

    def _ca_7d_csdl(k, i, so, G, sua):
        """Khai đủ mọi trường kể cả phụ trách mà thiếu CSDL: 7d phải đòi -
        thiếu nó thì update dữ liệu khách không có neo nào (rubric 03)."""
        _p = i / "X0_CAUHINH_FUZ.md"
        _s = _p.read_text(encoding="utf-8")
        _m = re.search(r"^@DUAN\.PHANMEM.*$", _s, re.M)
        _ghi(_p, _s[:_m.end()] + NL
             + "  DA1  He kho van · repo github.com/cty/tkv · web · dev may"
               " doi, staging stg.tkv.vn, chạy thật tkv.bacha.vn" + NL
             + "        · secret o Vault · nhánh tự deploy main"
               " · phụ trách vận hành: anh Bo ·" + _s[_m.end():])

    thu3("khai đủ kể cả phụ trách mà thiếu CSDL chạy thật", _ca_7d_csdl,
         "7d.")

    def _ca_7g_csdl(k, i, so, G, sua):
        """Khai CSDL chạy thật đích danh, rồi ghi update dữ liệu trên đúng
        CSDL đó mức A. X5 mục 1 định nghĩa đây là mức C mà trước vòng 85 máy
        không có neo nào (giám khảo rubric vòng 03)."""
        _p = i / "X0_CAUHINH_FUZ.md"
        _s = _p.read_text(encoding="utf-8")
        _m = re.search(r"^@DUAN\.PHANMEM.*$", _s, re.M)
        _ghi(_p, _s[:_m.end()] + NL
             + "  DA1  He ban hang · repo github.com/cty/bh · web · dev may"
               " doi, chạy thật bh.bacha.vn" + NL
             + "        · secret o Vault · CSDL chạy thật: CSDL khach hang ·"
             + _s[_m.end():])
        _nk = so / "NHATKY_2026Q3.md"
        _ghi(_nk, _nk.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| G-20260828-CUA1-15 | 2026-08-28 | CUA1.2000.op | A |"
             " chay update bang gia tren CSDL khach hang |"
             " VIEC V-DA1-001 | khong | XONG | khong |" + NL)

    thu3("update dữ liệu trên CSDL chạy thật đã khai mà ghi mức A",
         _ca_7g_csdl, "7g.")

    def _ca_7g_host2(k, i, so, G, sua):
        """Khai HAI host chạy thật trên một vế ('app... va api...'), rồi ghi
        deploy lên host THỨ HAI mức B. Bản chỉ neo host đầu để lọt ca này
        (giám khảo rubric vòng 03)."""
        _p = i / "X0_CAUHINH_FUZ.md"
        _s = _p.read_text(encoding="utf-8")
        _m = re.search(r"^@DUAN\.PHANMEM.*$", _s, re.M)
        _ghi(_p, _s[:_m.end()] + NL
             + "  DA1  He hai host · repo github.com/cty/haihost" + NL
             + "        · web + api · dev may doi, chạy thật app.bacha.vn va"
               " api.bacha.vn" + NL
             + "        · secret o Vault ·" + _s[_m.end():])
        _nk = so / "NHATKY_2026Q3.md"
        _ghi(_nk, _nk.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| G-20260828-CUA1-14 | 2026-08-28 | CUA1.1800.kl | B |"
             " deploy ban moi len api.bacha.vn |"
             " VIEC V-DA1-001 | khong | XONG | khong |" + NL)

    thu3("deploy lên host THỨ HAI của vế chạy thật mà ghi mức B",
         _ca_7g_host2, "7g.")

    def _ca_7g_squash(k, i, so, G, sua):
        """'squash branch feature vao main' mức B: nhánh tự deploy nêu đích
        danh mà lọt vì thiếu động từ (giám khảo rubric vòng 02, ca g10)."""
        _p = i / "X0_CAUHINH_FUZ.md"
        _s = _p.read_text(encoding="utf-8")
        _m = re.search(r"^@DUAN\.PHANMEM.*$", _s, re.M)
        _ghi(_p, _s[:_m.end()] + NL
             + "  DA1  He kho van · repo github.com/cty/khovan" + NL
             + "        · api · dev may doi, chạy thật khovan.bacha.vn" + NL
             + "        · secret o Vault · nhánh tự deploy main ·" + _s[_m.end():])
        _nk = so / "NHATKY_2026Q3.md"
        _ghi(_nk, _nk.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| G-20260828-CUA1-13 | 2026-08-28 | CUA1.1500.ef | B |"
             " squash branch feature vao main |"
             " VIEC V-DA1-001 | khong | XONG | khong |" + NL)

    thu3("squash vào nhánh tự deploy mà ghi mức B", _ca_7g_squash, "7g.")

    def _ca_0r_hai_noi(k, i, so, G, sua):
        """Cùng tên ở cả _inbox lẫn _da_nap: bản chép sót, phiên sau nạp lại."""
        _ghi(so / "_inbox" / "bao_gia_x.pdf", "x")
        _ghi(so / "_inbox" / "_da_nap" / "bao_gia_x.pdf", "x")

    thu3("file nằm cả _inbox lẫn _da_nap (chép sót)", _ca_0r_hai_noi, "0r.")

    thu3("file _da_nap không sổ nào mang tên gốc (nạp mồ côi)",
         lambda k, i, so, G, sua: _ghi(so / "_inbox" / "_da_nap"
                                       / "hd_thue_vp.pdf", "x"), "0r.")

    def _ca_nfd(k, i, so, G, sua):
        """ĐÚNG LUẬT: đĩa macOS/iCloud/Dropbox lưu tên dạng NFD, sổ ghi NFC -
        CÙNG một tên. Nhánh thử lại NFC/NFD của phép 9 đỡ ca này; trước đây
        không fixture nào phủ nên mutant lật điều kiện báo MẤT oan (rubric
        03, m09)."""
        import unicodedata as _ud
        (k / "05_Bao_cao").mkdir(exist_ok=True)
        _ten_nfd = _ud.normalize("NFD", "báo_cáo_quý.md")
        _ghi(k / "05_Bao_cao" / _ten_nfd, "x")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-090 | Bao cao quy | v01 | 2026-08-20 | Kho"
               " 05_Bao_cao/" + _ud.normalize("NFC", "báo_cáo_quý.md")
             + " | HIỆN HÀNH | NHÁP | 2026-08-20 | qs | noi bo | | | | "
             + G + " |" + NL)

    thu("file NFD trên đĩa, sổ ghi NFC (không được kêu)", _ca_nfd, False)

    def _ca_0r_dung(k, i, so, G, sua):
        """ĐÚNG LUẬT: file đã nạp, tên gốc nằm ở ô Căn cứ trạng thái TAILIEU
        đúng như X3 chặng 2 dặn - 0r không được kêu."""
        _ghi(so / "_inbox" / "_da_nap" / "bctc_2025.pdf", "x")
        (k / "03_Phap_ly").mkdir(exist_ok=True)
        _ghi(k / "03_Phap_ly" / "bctc.pdf", "x")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-089 | Bao cao tai chinh | v01 | 2026-08-20 |"
               " Kho 03_Phap_ly/bctc.pdf | HIỆN HÀNH | NHÁP | 2026-08-20 |"
               " ten goc bctc_2025.pdf | noi bo | | | | " + G + " |" + NL)

    thu("file _da_nap có tên gốc ở Căn cứ trạng thái (không được kêu)",
        _ca_0r_dung, False)

    def _ca_7g_khong_dau(k, i, so, G, sua):
        """Khai nhánh tự deploy, rồi ghi lượt GỘP KHÔNG DẤU vào đúng nhánh đó
        ở mức B. Động từ "gop nhanh" đã nằm trong _dv từ vòng 19; neo nhánh
        không nhận thì kiểu gõ phổ biến nhất lọt (giám khảo rubric 01)."""
        _p = i / "X0_CAUHINH_FUZ.md"
        _s = _p.read_text(encoding="utf-8")
        _m = re.search(r"^@DUAN\.PHANMEM.*$", _s, re.M)
        _ghi(_p, _s[:_m.end()] + NL
             + "  DA1  He dat hang · repo github.com/cty/dathang" + NL
             + "        · web · dev may doi, chạy thật dathang.bacha.vn" + NL
             + "        · secret o Vault · nhánh tự deploy main ·" + _s[_m.end():])
        _nk = so / "NHATKY_2026Q3.md"
        _ghi(_nk, _nk.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| G-20260828-CUA1-11 | 2026-08-28 | CUA1.1300.ab | B |"
             " Gop nhanh feature/dat-hang vao main sau review |"
             " VIEC V-DA1-001 | khong | XONG | khong |" + NL)

    thu3("gộp KHÔNG DẤU vào nhánh tự deploy mà ghi mức B", _ca_7g_khong_dau,
         "7g.")

    def _ca_8e_het_han(k, i, so, G, sua):
        """Chứng thư hết hạn 2020-01-01 (quá khứ vĩnh viễn - ca không hỏng
        theo thời gian thật) mà bảng vẫn "bàn sạch": 8e phải đỏ. Ca này ghim
        SỐNG bộ đếm hết hạn của dem_qua_han - đột biến m08 của giám khảo
        rubric giết được nó mà không phép nào kêu."""
        (k / "03_Phap_ly").mkdir(exist_ok=True)
        _ghi(k / "03_Phap_ly" / "ct.md", "x")
        _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-088 | Chung thu so | v01 | 2019-01-20 |"
               " Kho 03_Phap_ly/ct.md | HIỆN HÀNH | NHÁP | 2019-01-20 | qs |"
               " noi bo | 2020-01-01 | | | " + G + " |" + NL)

    thu3("chứng thư hết hạn mà bảng vẫn bàn sạch", _ca_8e_het_han, "8e.")

    def _ca_7g(k, i, so, G, sua):
        """Khai đủ phạm vi phần mềm (có nơi chạy thật), rồi ghi một lượt
        deploy CHÍNH cái host đó ở mức A. Đây là ca chứng minh GIÁ TRỊ khai
        ở X0 C2 thật sự điều khiển mức duyệt, chứ không nằm đó cho đẹp."""
        _p = i / "X0_CAUHINH_FUZ.md"
        _s = _p.read_text(encoding="utf-8")
        _m = re.search(r"^@DUAN\.PHANMEM.*$", _s, re.M)
        _ghi(_p, _s[:_m.end()] + NL
             + "  DA1  He quan ly · repo github.com/cty/qlkh" + NL
             + "        · web + api · dev may doi, staging stg.qlkh.vn,"
             + " chạy thật qlkh.bacha.vn" + NL
             + "        · secret o Vault noi bo" + _s[_m.end():])
        _nk = so / "NHATKY_2026Q3.md"
        _ghi(_nk, _nk.read_text(encoding="utf-8").rstrip(NL) + NL
             + "| G-20260828-CUA1-09 | 2026-08-28 | CUA1.1200.zz | A |"
             " deploy ban va len qlkh.bacha.vn (chạy thật) |"
             " VIEC V-DA1-001 | khong | XONG | khong |" + NL)

    thu3("deploy lên ĐÚNG host chạy thật đã khai mà ghi mức A", _ca_7g, "7g.")
    thu3("ô \"Ở đâu\" của TAILIEU sai khuôn (tắt lặng lẽ 9, 10a, 10b)",
         lambda k, i, so, G, sua: _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip(NL) + NL
             + "| DA1 | T-001 | Tai lieu | v1 | 2026-08-28 | Dropbox abc |"
             " HIỆN HÀNH | ĐANG DÙNG | 2026-08-28 | qs | doi tac | | | | "
             + G + " |" + NL), "7f.")
    thu3("xóa trọn mục C12 khỏi X0 (tắt luôn phép canh chính mục đó)",
         lambda k, i, so, G, sua: _ghi(i / "X0_CAUHINH_FUZ.md",
             (lambda t: t[:t.index("# C12.")] + t[t.index("# C13."):])(
                 (i / "X0_CAUHINH_FUZ.md").read_text(encoding="utf-8"))), "0i2.")
    thu3("neo _moc_ghi.txt biến mất khi kho đã có lượt ghi",
         lambda k, i, so, G, sua: (i / "_moc_ghi.txt").unlink(), "0k2.")
    thu3("ô Mức của NHATKY gõ thường, lách trọn kỷ luật mức C",
         lambda k, i, so, G, sua: sua(so / "NHATKY_2026Q3.md", "| A | mo viec",
                                      "| a | mo viec"), "3g.")
    thu3("dòng TAILIEU dạng Repo khi C2 chưa khai phần mềm nào",
         lambda k, i, so, G, sua: _ghi(so / "TAILIEU.md",
             (so / "TAILIEU.md").read_text(encoding="utf-8").rstrip() + NL
             + "| DA1 | T-009 | Dac ta API | v01 | 2026-08-28 |"
               " Repo ORD docs/api.md@v2.4.1 | HIỆN HÀNH | ĐÃ PHÁT HÀNH |"
               " 2026-08-28 | x | x | | | | " + G + " |" + NL), "7d2.")
    thu3("file secret nằm trong kho đồng bộ (X5 mục 1b)",
         lambda k, i, so, G, sua: (k / "01_Phap_ly").mkdir(exist_ok=True)
             or _ghi(k / "01_Phap_ly" / "prod.env", "DB_PASSWORD=x" + NL), "7e2.")
    thu3("secret lọt vào ô của sổ (X5 mục 1b)",
         lambda k, i, so, G, sua: _ghi(so / "DUKIEN.md",
             (so / "DUKIEN.md").read_text(encoding="utf-8").rstrip() + NL
             + "| DA1 | D-009 | Chuoi ket noi | postgres://u:p%40ss@db.x.vn:5432/d"
               " | 2026-08-28 | NOI_BO | x | A | ĐÃ KIỂM | 2026-12-31 | "
             + G + " |" + NL), "7e.")
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

    # CA MỒI chỉ canh vế I1 là chưa đủ: ghim SỐ CA đếm _dem, mà _dem vẫn tăng
    # bình thường khi KHẲNG ĐỊNH bị đục ruột. Hội đồng vòng 17 tắt được cả vế
    # I2 lẫn vế I3 mà bộ vẫn in "sạch" - và chú thích cũ ở đây khai NGƯỢC LẠI.
    # Mỗi vế nay có mồi của riêng nó.
    _n2 = len(hong)
    thu("CA MỒI I2: xóa trọn NHATKY quý mà khai là ĐÚNG LUẬT",
        lambda k, i, so, G, sua: (so / "NHATKY_2026Q3.md").unlink(), False)
    if len(hong) == _n2:
        hong.append("CA MỒI I2 không kêu: vế I2 đã bị tắt, lưới chống báo oan"
                    " chỉ còn trang trí")
    elif hong[-1].startswith("I2 CA MỒI"):
        hong.pop()

    _n3 = len(hong)
    thu3("CA MỒI I3: kho LÀNH mà đòi 0j phải kêu", lambda *a: None, "0j.")
    if len(hong) == _n3:
        hong.append("CA MỒI I3 không kêu: khẳng định I3 đã bị tắt, mọi ca I3"
                    " chỉ còn chạy cho có")
    elif hong[-1].startswith("I3 CA MỒI"):
        hong.pop()

    # Ghim SỐ CA bắt được vế "bỏ bớt ca"; hai vế kia do hai CA MỒI trên giữ.
    import os as _os_dem
    _i3_mong = 91 if _os_dem.name == "nt" else 90   # ca 9d chỉ có trên NTFS
    if (_dem["I1"], _dem["I2"], _dem["I3"]) != (7, 37, _i3_mong):
        hong.append(f"số ca phép 13 lệch: {_dem}; bộ khai I1 7 (kể CA MỒI), I2 37,"
                    f" I3 {_i3_mong} - bớt ca là bớt lưới; đổi số thì sửa con số"
                    f" này trong CÙNG lượt vá")

    # 14b. ĐIỂM DANH PHÉP CỦA kiem_van_hanh. Phép 14 chỉ điểm danh phép của
    #      CHÍNH kiem_tra_bo, nên xóa một phép khỏi kiem_van_hanh vẫn "sạch".
    #      Danh bạ PHEP_VH là DỮ LIỆU: phép mới không kèm ca của chính nó thì
    #      14b đỏ NGAY LƯỢT VÁ ĐÓ - quy tắc mà ba vòng liền tự viết rồi không
    #      thi hành, nay thành MÁY chứ không còn là lời dặn (vòng 15b).
    import kiem_van_hanh as K14
    # còn ĐÚNG BA, mỗi mục kèm LÝ DO THẬT chứ không phải nợ đọng:
    #   0f, 10c  cần KHÓA FILE ở tầng hệ điều hành nên ca phụ thuộc nền tảng -
    #            dựng được trên Windows thì hỏng trên CI Linux; và bộ CỐ Ý
    #            phân biệt "chưa kiểm được" với "bị sửa".
    #   11.      chỉ so nội dung SAU khi file đạt luật ổn định HAI LƯỢT QUÉT,
    #            mà bộ fuzz chạy rà soát một lượt. Ràng buộc của thiết kế.
    # Vòng 50 đưa danh sách này từ 16 xuống 8, vòng 69 xuống 3.
    MIEN_TRU = ["0f.", "10c.", "11."]
    # phải RỖNG DẦN: mỗi mục là một phép chưa ai canh. Vòng 16 bỏ "4." và "5.";
    # vòng 50 bỏ tiếp tám phép NGHIỆP VỤ NẶNG NHẤT (0, 1, 3a, 6, 7, 9, 10a,
    # 10b) vì phép 15 canh chúng thật - chỉ cần nối tập phủ của nó vào đây,
    # không phải viết thêm ca nào. Miễn trừ thừa là mất cảnh báo nếu ca canh
    # chúng hỏng về sau, nên danh sách này không được dài ra.
    _ho = [pp for pp in K14.PHEP_VH if pp not in phu and pp not in MIEN_TRU]
    # 14c. Danh bạ PHEP_VH là dữ liệu CHÉP TAY: vòng 45 đẻ ra 7d2 rồi quên
    #      khai, nên 14b mù đúng phép mới nhất và quy tắc vòng 44 bị phá ngay
    #      vòng sau. Đối chiếu danh bạ với NGUỒN thì lớp lỗi đó hết đường.
    _nguon_vh = Path(K14.__file__).read_text(encoding="utf-8")
    _nguon_tb = Path(__file__).read_text(encoding="utf-8")
    _ten_bao = {m.group(1) for m in re.finditer(
        r'bao\(\s*[fr]?["\']([0-9][A-Za-z0-9]*\.)\s', _nguon_vh)}
    kiem("14c. danh bạ PHEP_VH khai đủ mọi phép bao() có trong kiem_van_hanh",
         _ten_bao == set(K14.PHEP_VH),
         f"nguồn có mà danh bạ thiếu: {sorted(_ten_bao - set(K14.PHEP_VH))};"
         f" danh bạ có mà nguồn không: {sorted(set(K14.PHEP_VH) - _ten_bao)}."
         f" Danh bạ chép tay không có lưới thì 14b mù đúng phép mới nhất")
    # 14d. Danh bạ PHEP_BAT_BUOC của CHÍNH kiem_tra_bo là dữ liệu chép tay và
    #      chưa có 14c của riêng nó: hội đồng vòng 17 rút sáu phép khỏi danh bạ
    #      rồi xóa thân phep_fuzz, bộ vẫn in "đóng gói được". Phép 14 chỉ mạnh
    #      bằng danh bạ của nó, mà danh bạ đó đang trôi tự do.
    _ten_kiem = {m.group(1) for m in re.finditer(
        r'kiem\(\s*[fr]?["\']([0-9][A-Za-z0-9]*\.)\s', _nguon_tb)} - {"8."}
    kiem("14d. danh bạ PHEP_BAT_BUOC khai đủ mọi phép kiem() có trong nguồn",
         _ten_kiem == set(PHEP_BAT_BUOC),
         f"nguồn có mà danh bạ thiếu: {sorted(_ten_kiem - set(PHEP_BAT_BUOC))};"
         f" danh bạ có mà nguồn không: {sorted(set(PHEP_BAT_BUOC) - _ten_kiem)}."
         f" Rút tên khỏi danh bạ rồi xóa thân hàm là lối vá 'cho qua bộ kiểm'"
         f" rẻ nhất; 14d bịt đúng lối đó")

    # 14e. LƯỚI CỦA LƯỚI. Phép 13, 14, 14b, 14c canh kiem_van_hanh; không ai
    #      canh chính kiem_tra_bo - hội đồng vòng 17 đo được 0/9 đột biến đục
    #      ruột nhắm vào nó bị bắt. Ép điều kiện một phép thành luôn-đúng là
    #      lối vá "cho qua bộ kiểm" rẻ nhất. Hằng False vẫn HỢP LỆ (7d2, 7e2,
    #      10c cố ý gọi trong nhánh if đã quyết định xong); chỉ cấm hằng True.
    import ast as _ast

    def _hang_rong(_n):
        """Hằng rỗng theo cấu trúc: [], (), {}, "", 0, None."""
        if isinstance(_n, (_ast.List, _ast.Tuple, _ast.Set)):
            return not _n.elts
        if isinstance(_n, _ast.Dict):
            return not _n.keys
        return isinstance(_n, _ast.Constant) and not _n.value

    def _luon_dung(_n):
        """Biểu thức LUÔN ĐÚNG mà không đọc dữ liệu nào. Bản đầu của 14e chỉ
        dò hằng True nên `not []` lách được trọn (hội đồng vòng 19)."""
        if isinstance(_n, _ast.Constant) and _n.value is True:
            return True
        if isinstance(_n, _ast.UnaryOp) and isinstance(_n.op, _ast.Not):
            return _hang_rong(_n.operand)
        if isinstance(_n, _ast.BoolOp) and isinstance(_n.op, _ast.Or):
            return any(_luon_dung(_v) for _v in _n.values)
        if (isinstance(_n, _ast.Call) and isinstance(_n.func, _ast.Name)
                and _n.func.id == "all" and len(_n.args) == 1):
            return _hang_rong(_n.args[0])
        if (isinstance(_n, _ast.Compare) and len(_n.ops) == 1
                and isinstance(_n.ops[0], (_ast.Eq, _ast.Is))):
            if _hang_rong(_n.left) and _hang_rong(_n.comparators[0]):
                return True
            _t = _n.left
            if (isinstance(_t, _ast.Call) and isinstance(_t.func, _ast.Name)
                    and _t.func.id == "len" and len(_t.args) == 1
                    and _hang_rong(_t.args[0])):
                return _hang_rong(_n.comparators[0])
            return (isinstance(_t, _ast.Constant)
                    and isinstance(_n.comparators[0], _ast.Constant)
                    and _t.value == _n.comparators[0].value)
        return False

    _duc = []
    for _tenf, _ndf, _hamf in [("kiem_tra_bo", _nguon_tb, "kiem"),
                               ("kiem_van_hanh", _nguon_vh, "bao")]:
        for _nut in _ast.walk(_ast.parse(_ndf)):
            if (isinstance(_nut, _ast.Call) and isinstance(_nut.func, _ast.Name)
                    and _nut.func.id == _hamf and len(_nut.args) > 1
                    and _luon_dung(_nut.args[1])):
                _duc.append(f"{_tenf} dòng {_nut.lineno}: điều kiện LUÔN ĐÚNG"
                            f" theo cấu trúc")
            if isinstance(_nut, _ast.FunctionDef) and _nut.name == _hamf:
                _tsd = _nut.args.args[1].arg
                if not any(isinstance(_x, _ast.Name) and _x.id == _tsd
                           for _y in _ast.walk(_nut)
                           if isinstance(_y, _ast.If)
                           for _x in _ast.walk(_y.test)):
                    _duc.append(f"{_tenf}: {_hamf}() hết rẽ nhánh theo {_tsd}")
    kiem("14e. không phép nào bị đục ruột thành luôn-đúng", not _duc,
         f"{'; '.join(_duc[:4])}. Điều kiện luôn đúng theo cấu trúc (True,"
         f" not [], len([]) == 0...) thì phép đó chỉ còn in chữ PASS; muốn báo"
         f" lệch vô điều kiện thì dùng hằng False trong nhánh if như 7d2, 7e2")

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
    kiem("13b. bảng kết quả kiem_van_hanh trong trần đầu ra 2.700 ký tự",
         n_ra <= 2700, f"{n_ra} ký tự ~{n_ra // 3} token: đầu ra này DÁN VÀO"
         f" phiên RA_SOAT, là context thật của người dùng")

    # 13d. Số token đầu ra khai ở BENCHMARK nằm NGOÀI lưới 2c (2c chỉ soi dòng
    #      chứa nhãn, số này ở dòng sau nhãn RA_SOAT) nên stale 22 phần trăm
    #      suốt ba vòng dù vòng 15 đã gọi tên đích danh (hội đồng vòng 16).
    _m_ra = re.search(r"đo được ~(\d+)\s*\n?\s*token trên kho lành",
                      (goc / "BENCHMARK_TOKEN.md").read_text(encoding="utf-8"))
    kiem("13d. token đầu ra khai ở BENCHMARK khớp số đo",
         bool(_m_ra) and abs(int(_m_ra.group(1)) - n_ra // 3) <= 0.02 * (n_ra // 3),
         f"BENCHMARK ~{_m_ra and _m_ra.group(1)}, đo thật ~{n_ra // 3}")

    # 13c. Trần trên kho TOÀN PASS là ca DỄ NHẤT; RA_SOAT chỉ chạy khi kho CÓ
    #      vấn đề. Hội đồng vòng 15b: kho 8 lệch cho 3.832 ký tự, vượt 60%.
    with tempfile.TemporaryDirectory() as td:
        kho, idx, so, G = _kho_song(goc, td)
        _ghi(idx / "rac_la.md", "x")
        shutil.copy(idx / "INSTRUCTION_WORKOPS_v11.md",
                    idx / "INSTRUCTION_WORKOPS_v9.md")
        _ghi(so / "VIEC.md", (so / "VIEC.md").read_text(encoding="utf-8")
             + "| DA1 | V-DA1-009 | dan tay | x | toi | | 2026-12-31 | MỚI | | |" + NL)
        # kho CẬN XẤU, không phải ảnh chụp 3 lệch: hội đồng vòng 16 đo kho 8
        # lệch cho 4.640 ký tự, vượt trần cũ 4.400
        (so / "NHATKY_2026Q3.md").unlink()
        _sua(idx / "X0_CAUHINH_FUZ.md", "rev 1 · 20260828", "rev 0 · 20260828")
        (kho / ".git").mkdir(exist_ok=True)
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
    kiem("13c. bảng kiem_van_hanh trên kho CẬN XẤU trong trần 5.200 ký tự",
         n_lech <= 5200, f"{n_lech} ký tự ~{n_lech // 3} token: đây mới là ca"
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
    import kiem_van_hanh as _kvj
    for f in (goc.rglob("*") if cho_phep is not None else []):
        if _kvj._la_lien_ket(f):
            continue  # junction tự trỏ làm rglob sinh gần 6.000 mục, sâu
            # 11 tầng, chỉ dừng bằng MAX_PATH (hội đồng vòng 16)
        rel = str(f.relative_to(goc)).replace("\\", "/")
        if not f.is_file() or da_khai_bo(rel):
            continue
        if rel not in cho_phep and not re.fullmatch(
                r"INSTRUCTION_WORKOPS_v\d+\.md|GHICHU_(DOI_MOI|LICHSU)_v.*\.md"
                r"|WORKOPS_.*_GOP\.md|_so/NHATKY_\d{4}Q[1-4]\.md", rel):
            thua.append(rel)
    kiem("1e. không file thừa ngoài danh sách bộ", not thua,
         f"{sorted(thua)[:5]}: xóa khỏi repo hay đưa vào .gitignore; bộ ship"
         f" NGUYÊN TRẠNG nên thứ ở đây vào 00_Index của mọi công ty")
    kiem("1b. đúng một file INSTRUCTION", len(instr) == 1, f"thấy {len(instr)}")
    kiem("1c. đúng một file GHICHU_DOI_MOI_v*", len(ghichu) == 1, f"thấy {len(ghichu)}")
    # 1f. Lịch sử tách ra thì phải CÒN ĐÓ và còn LIỀN MẠCH. Nới allow-list mà
    #     không thêm nghĩa vụ là mở một lỗ: xóa file lưu trữ đi thì 25 vòng
    #     lịch sử biến mất mà không phép nào kêu (vòng 53).
    _ls = sorted(goc.glob("GHICHU_LICHSU_v*.md"))
    _loi1f = []
    if len(_ls) != 1:
        _loi1f.append(f"thấy {len(_ls)} file GHICHU_LICHSU_v*, phải đúng một")
    elif ghichu:
        _gh_nd = (goc / ghichu[0].name).read_text(encoding="utf-8")
        _ls_nd = _ls[0].read_text(encoding="utf-8")
        if _ls[0].name not in _gh_nd:
            _loi1f.append(f"GHICHU không trỏ tới {_ls[0].name}")
        _v = sorted(int(x) for x in re.findall(r"^## Vòng (\d+)", _gh_nd, re.M)
                    + re.findall(r"^## Vòng (\d+)", _ls_nd, re.M))
        _thung = [n for n in range(min(_v), max(_v) + 1) if n not in _v] if _v else []
        if _thung:
            _loi1f.append(f"thủng vòng {_thung[:5]} giữa hai file")
    kiem("1f. lịch sử đã tách vẫn còn đủ và liền mạch", not _loi1f,
         "; ".join(_loi1f))
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
        # Dung sai cũ 10%/2% cho 168 token trôi im trên một route 1.684: vòng
        # 43 phình X5 và X4 rồi chỉ dán lại MỘT số, năm số kia stale ba vòng
        # liền mà 2c vẫn PASS. Siết 2%/0,5%: sửa mục nào là buộc dán lại.
        nguong = 0 if "CỘNG" in nhan else (0.005 if gia_tri > 5000 else 0.02)
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
        if ten == "INSTRUCTION":
            nd = docs["INSTRUCTION"]
        elif ten in docs or ten in kem:
            nd = docs.get(ten) or kem.get(ten, "")
        else:
            # Khóa KHÔNG nằm trong docs lẫn kem (bản gộp _GOP): nhánh cũ rơi vào
            # nd="" rồi `if nd` chặn luôn, nên trần 400.000 của bản gộp là trần
            # GIẢ - chưa từng được đo. Hội đồng vòng 16 bơm 1.000.000 ký tự rác
            # vào bản gộp mà bộ vẫn in "sạch, đóng gói được". Một cái trần không
            # đo được là một cái trần KHÔNG TỒN TẠI.
            _p9 = goc / ten
            if not _p9.is_file():
                vuot_ns.append((ten, -1, tran))
                continue
            nd = _p9.read_text(encoding="utf-8")
        if len(nd) > tran:
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
    # 5b. SỐ CỘT của sổ mẫu phải khớp schema X5 mục 4. Mọi phép đọc sổ theo
    #     CHỈ SỐ CỘT đứng trên lời khai đó (3g cột 7 của VIEC, 8e cột 11 của
    #     TAILIEU, 13m cột 5 và 6 của QUYETDINH, 7c cột 6 của DUKIEN); thêm hay
    #     bớt một cột ở một trong hai nơi là mọi phép đó đọc lệch một ô mà
    #     không ai biết - phép 5 chỉ so các dòng VỚI NHAU. Cùng lớp "hai bản
    #     khai không ai đối chiếu" mà 9b và 14c đã đóng ở chỗ khác. Backlog (b).
    _x5m4 = docs["X5_HESO_TEMPLATE.md"]
    _m4 = _x5m4[_x5m4.find("# 4."):_x5m4.find("# 5.")]
    SO_SCHEMA = {"VIEC.md": "_so/VIEC.md", "DUKIEN.md": "_so/DUKIEN.md",
                 "TAILIEU.md": "_so/TAILIEU.md",
                 "QUYETDINH.md": "_so/QUYETDINH.md",
                 "NHATKY_<quý>": "_so/NHATKY_TEMPLATE.md"}
    _lech5b = []
    for _ten5, _tep5 in SO_SCHEMA.items():
        _i5 = _m4.find(_ten5)
        if _i5 < 0:
            _lech5b.append(f"X5 mục 4 không khai {_ten5}")
            continue
        # ranh giới khai: mục mới bắt đầu ở CỘT 0, dòng nối thì thụt. Cắt
        # theo dấu chấm câu thì khai của VIEC chạy sang tận TAILIEU (41 cột).
        _dong5 = _m4[_i5 + len(_ten5):].splitlines()
        _khai_d = [_dong5[0]] if _dong5 else []
        for _d5 in _dong5[1:]:
            if _d5[:1] not in (" ", "\t") or not _d5.strip():
                break
            _khai_d.append(_d5)
        _khai5 = " ".join(_khai_d)
        # bỏ phần văn xuôi sau khai cột (QUYETDINH có ". Không xóa..." đi kèm)
        _khai5 = re.split(r"\.\s", _khai5)[0]
        _n_khai = len([_c for _c in _khai5.split("·") if _c.strip()])
        _nd5 = docs.get(_tep5, "")
        _hdr = next((l for l in _nd5.splitlines() if l.startswith("| ")), "")
        _n_that = len([_c for _c in _hdr.strip().strip("|").split("|")]) \
            if _hdr else 0
        if _n_khai != _n_that:
            _lech5b.append(f"{_ten5}: X5 mục 4 khai {_n_khai} cột, sổ mẫu có"
                           f" {_n_that}")
    kiem("5c. số cột của sổ mẫu khớp schema X5 mục 4", not _lech5b,
         "; ".join(_lech5b[:4]) + ". Mọi phép đọc sổ theo CHỈ SỐ CỘT đứng trên"
         " lời khai đó; lệch một cột là chúng đọc lệch một ô mà không ai biết")

    kiem("9b. bảng trần ở BENCHMARK khớp NGAN_SACH", not lech_tran, str(lech_tran))
    # 9c. Ngưỡng RUNTIME cũng phải khai ở BENCHMARK và khớp hằng trong mã.
    #     Khuôn y hệt 9b - thứ DUY NHẤT đã chứng minh hiệu lực bằng đột biến:
    #     nới một trần trong NGAN_SACH thì 9b bắt, còn nới `n > 500` hay
    #     `<= 4200` thì không ai kêu (hội đồng vòng 17, 6/6 đột biến sống sót).
    NGUONG_RT = [("X0 runtime", 28000, r"_n_x0 <= (\d+)", "kiem_van_hanh"),
                 ("BANG_DIEU_KHIEN runtime", 4200, r"len\(bdk_nd\) <= (\d+)",
                  "kiem_van_hanh"),
                 ("X0_INDEX runtime", 2400, r"len\(idx_rt\) <= (\d+)",
                  "kiem_van_hanh"),
                 ("một sổ tối đa", 500, r"if n > (\d+) or p\.stat", "kiem_van_hanh"),
                 ("đầu ra kho lành", 2700, r"n_ra <= (\d+)", "kiem_tra_bo"),
                 ("đầu ra kho cận xấu", 5200, r"n_lech <= (\d+)", "kiem_tra_bo")]
    import kiem_van_hanh as _K9c
    _src9 = {"kiem_van_hanh": Path(_K9c.__file__).read_text(encoding="utf-8"),
             "kiem_tra_bo": Path(__file__).read_text(encoding="utf-8")}
    _bm9c, _lech9c = docs["BENCHMARK_TOKEN.md"], []
    for _ten9, _so9, _mau9, _tep9 in NGUONG_RT:
        _nguon9 = _src9[_tep9]
        _mm9 = re.search(_mau9, _nguon9)
        if not _mm9:
            _lech9c.append(f"{_ten9}: không tìm thấy hằng trong {_tep9}")
        elif int(_mm9.group(1)) != _so9:
            _lech9c.append(f"{_ten9}: mã {_mm9.group(1)}, bảng ghim {_so9}")
        _dang9 = f"{_so9:,}".replace(",", ".") if _so9 >= 1000 else str(_so9)
        if _dang9 not in _bm9c:
            _lech9c.append(f"{_ten9}: BENCHMARK chưa khai số {_dang9}")
    kiem("9c. ngưỡng runtime khai ở BENCHMARK khớp hằng trong mã",
         not _lech9c, "; ".join(_lech9c[:4])
         + ". Nới một ngưỡng là lối vá rẻ nhất khi bộ đỏ; 9c bắt phải nới ở"
           " CẢ HAI nơi, tức phải khai ra cho người đọc thấy")
    # GHICHU bị phép 8 ĐÒI có trong bản gộp nhưng chưa từng có trần: động cơ
    # phình thứ hai của bản gộp, không ai quản (hội đồng vòng 16).
    # Vòng 48 nâng 115.000 -> 130.000 và ghi thẳng đó là NỢ. Vòng 53 TRẢ nợ:
    # tách các mục vòng <= 25 sang GHICHU_LICHSU (131.366 -> 88.531, đúng con
    # số 37% đã đo). Giữ trần đã vay là giữ chỗ trống, nên hạ về 100.000 -
    # còn khoảng tám vòng headroom trước lượt tách kế. Phép 1f canh phần lịch
    # sử đã tách vẫn còn đủ và liền mạch.
    if len(kem[ghichu[0].name]) > 100000:
        vuot_ns.append((ghichu[0].name, len(kem[ghichu[0].name]), 100000))
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
        # TẤT ĐỊNH của loc_ban_chinh: nó đúng nhờ `sorted(cac)` ở đầu hàm, mà
        # đó là tính chất chưa ai khẳng định. Mất `sorted` thì kết quả theo thứ
        # tự glob của hệ tệp: hai máy chọn hai bản NHATKY khác nhau làm bản
        # chính, watermark khác nhau, và lượt sau cấp lại mã đã dùng (vòng 57)
        import itertools as _it57
        import kiem_van_hanh as _kv57
        _ten57 = ["NHATKY_2026Q1.md", "NHATKY_2026Q3.md", "NHATKY_2026Q2.md"]
        _kq57 = {tuple(q.name for q in _kv57.loc_ban_chinh(
                     [Path(t) for t in _hv], r"NHATKY_\d{4}Q[1-4]\.md"))
                 for _hv in _it57.permutations(_ten57)}
        ca.append(("loc_ban_chinh TẤT ĐỊNH: 6 hoán vị đầu vào, 1 kết quả",
                   len(_kq57) == 1 and next(iter(_kq57)) == (
                       "NHATKY_2026Q1.md", "NHATKY_2026Q2.md",
                       "NHATKY_2026Q3.md")))

        # NFD (macOS, iCloud, Dropbox) và NFC là CÙNG một họ. Không chuẩn hóa
        # thì phép 11 (XUNG ĐỘT) hết đường kêu về mặt cấu trúc và phép 9 báo
        # oan khi sổ ghi NFC mà đĩa giữ NFD (hội đồng vòng 17)
        import os as _os17
        import subprocess as _sp17
        import unicodedata as _ud17
        import kiem_van_hanh as _kv17
        ca.append(("tên NFD và NFC là CÙNG một họ",
                   ho_va_v(_ud17.normalize("NFC", "Hồ_sơ_v01.docx"))
                   == ho_va_v(_ud17.normalize("NFD", "Hồ_sơ_v01.docx"))))
        # Bản sao của vùng luật cũng là vùng luật: Windows Explorer đẻ
        # "00_Index - Copy", OneDrive đẻ "00_Index (1)". Mỗi bản sao lọt là
        # 14 FILE LUẬT thành ứng viên chờ vào TAILIEU (hội đồng vòng 16)
        with tempfile.TemporaryDirectory() as _td17:
            _k17 = Path(_td17) / "kho"
            for _t17 in ["00_Index - Copy", "00_Index (1)", "00_Index_20260828",
                         "01_Backup/00_Index"]:
                (_k17 / _t17).mkdir(parents=True)
                _ghi(_k17 / _t17 / "X1_CAM_ABC.md", "luat")
            (_k17 / "02_Ky_thuat").mkdir(parents=True)
            _ghi(_k17 / "02_Ky_thuat" / "tai_lieu_v01.md", "nghiep vu")
            _, _moi17 = _kv17.quet_ho(_k17, None, (), None, 1000.0)
            ca.append(("bản sao 00_Index không rò file luật thành ứng viên",
                       list(_moi17) == ["02_Ky_thuat/tai_lieu_v01.md"]))
        # Junction Windows KHÔNG phải symlink: Path.is_symlink() trả False cho
        # nó. Vá vòng 46 đọc cờ FILE_ATTRIBUTE_REPARSE_POINT, và hoàn nguyên
        # được trong im lặng cho tới vòng 47 - một junction tự trỏ đẻ 38 đường
        # dẫn ma, đệ quy chỉ dừng bằng MAX_PATH (hội đồng vòng 17)
        if _os17.name == "nt":
            with tempfile.TemporaryDirectory() as _tdj:
                _kj = Path(_tdj) / "kho" / "02_Ky_thuat"
                _kj.mkdir(parents=True)
                _ghi(_kj / "that_v01.md", "noi dung")
                _rc = _sp17.run(["cmd", "/c", "mklink", "/J",
                                      str(_kj / "vong"), str(_kj)],
                                     capture_output=True).returncode
                if _rc == 0:
                    _, _mj = _kv17.quet_ho(Path(_tdj) / "kho", None, (), None, 1000.0)
                    ca.append(("junction tự trỏ không đẻ đường dẫn ma",
                               len(_mj) == 1
                               and _kv17._la_lien_ket(_kj / "vong") is True))

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
                       idx=None, files=None, don=None, thu_header=None):
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
                    "# T\n\n" + (thu_header or
                    "| Mã | Luồng | Conversation-ID | Message-ID cuối | Trạng thái |\n"
                    "|---|---|---|---|---|\n") + thu_rows, encoding="utf-8")
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
        # đính kèm f.pdf PHẢI để lại dấu ở sổ: X3E mục ĐÍNH KÈM bắt chép về
        # chỗ xếp và trỏ vào sổ TRƯỚC khi append COMMITTED (phép 12n, vòng 54)
        FILES_SACH = {f"_so/_thu_staging/{THU_MUC_A}/thu.eml": "eml",
                      f"_so/_thu_staging/{THU_MUC_A}/f.pdf": "PDF",
                      "_so/VIEC.md": "| V-001 | viec |\n",
                      "_so/TAILIEU.md": "| T-001 | Kho 01_Phap_ly/f.pdf |\n"}
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
        # staging MẤT .eml dù còn file cùng nội dung khác đuôi (thu.txt): thân
        # thư gốc là bằng chứng pháp lý, đổi tên là 12j phải đỏ - mutant or-hóa
        # sống vì chưa ca nào giữ (rubric 09, m03)
        _files_txt = {k2: v2 for k2, v2 in FILES_SACH.items()
                      if not k2.endswith("thu.eml")}
        _files_txt[f"_so/_thu_staging/{THU_MUC_A}/thu.txt"] = "eml"
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=IDX_SACH, files=_files_txt,
                       thu_rows="| #L-001 | L1 | c1 | <a@x> | CHỜ TÔI |\n")
        ca.append(("staging mất .eml dù còn file khác đuôi bị bắt",
                   r.get(TEN_12J) is False))
        # đính kèm của mail ĐÃ COMMITTED không để lại dấu nào ở sổ: hợp đồng đã
        # ký số coi như "đã nạp", registry chặn nạp lại -> mất IM LẶNG (vòng 18)
        _f_khong_so = {k: v for k, v in FILES_SACH.items()
                       if k != "_so/TAILIEU.md"}
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=IDX_SACH, files=_f_khong_so,
                       thu_rows="| #L-001 | L1 | c1 | <a@x> | CHỜ TÔI |\n")
        ca.append(("đính kèm COMMITTED không có ở THU lẫn TAILIEU bị bắt",
                   r.get("12n. đính kèm của mail đã COMMITTED để lại dấu ở sổ")
                   is False))
        # de_ngoai theo X3E mục 2 phải có CẢ dòng TAILIEU trỏ nguồn LẪN VIEC tải tay
        _pay_ng = dict(PAY, dinh_kem=[{"ten": "Dump_KH.zip", "de_ngoai": True,
                                       "ly_do": "vượt @NHIP.TRANDINHKEM"}])
        r = chay_email(nk=P("<a@x>", pay=_pay_ng) + "\n" + C("<a@x>") + "\n",
                       reg=["<a@x>"], idx=IDX_SACH, files=_f_khong_so,
                       thu_rows="| #L-001 | L1 | c1 | <a@x> | CHỜ TÔI |\n")
        ca.append(("đính kèm de_ngoai không có nguồn ở sổ bị bắt",
                   r.get("12n. đính kèm của mail đã COMMITTED để lại dấu ở sổ")
                   is False))
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
        # metadata nguồn SAI KIỂU: vá vòng 41 chỉ ghim lane operation_id, lane
        # này để ngỏ (giám khảo rubric vòng 02)
        ca.append(("metadata nguồn sai kiểu (số) bị từ chối",
                   any("conv_id" in l for l in
                       _kv26.kiem_payload(dict(_pl_dung, conv_id=123), _khoa_pl))))
        # thao_tac RỖNG: mail nạp mà không tạo dòng sổ nào vẫn ĐẠT là vô
        # nghĩa - mutant or->and của rubric 03 sống nhờ nhánh này chưa ghim
        ca.append(("payload thao_tac rỗng bị từ chối",
                   any("thao_tac" in l for l in
                       _kv26.kiem_payload(dict(_pl_dung, thao_tac=[]), _khoa_pl))))
        # LƯỚI MỀM 7g phải IN LƯU Ý: tính năng vòng 45-46 không ca nào ghim
        # (giám khảo rubric 04, mutant m6 tắt nó mà bộ vẫn xanh). Dựng kho
        # khai host, ghi mức B động từ LẠ + chữ prod, chụp stdout.
        with tempfile.TemporaryDirectory() as _td7g:
            _kho7, _idx7, _so7, _G7 = _kho_song(goc, _td7g)
            _p7 = _idx7 / "X0_CAUHINH_FUZ.md"
            _s7 = _p7.read_text(encoding="utf-8")
            _m7 = re.search(r"^@DUAN\.PHANMEM.*$", _s7, re.M)
            _ghi(_p7, _s7[:_m7.end()] + NL
                 + "  DA1  He mem · repo github.com/cty/m · web · dev may"
                   " doi, chạy thật mem.bacha.vn · secret o Vault ·"
                 + _s7[_m7.end():])
            _nk7 = _so7 / "NHATKY_2026Q3.md"
            _ghi(_nk7, _nk7.read_text(encoding="utf-8").rstrip(NL) + NL
                 + "| G-20260828-CUA1-16 | 2026-08-28 | CUA1.2200.st | B |"
                 " push ban moi len prod | VIEC V-DA1-001 | khong | XONG |"
                 " khong |" + NL)
            import contextlib as _cl7, io as _io7
            _buf7, _argv7 = _io7.StringIO(), sys.argv
            try:
                sys.argv = ["kvh", str(_idx7), str(_kho7)]
                with _cl7.redirect_stdout(_buf7):
                    try:
                        _kv26.main(_idx7)
                    except SystemExit:
                        pass
            finally:
                sys.argv = _argv7
            ca.append(("lưới mềm 7g in LƯU Ý với động từ lạ + chữ prod",
                       "LƯU Ý  7g" in _buf7.getvalue()))
        # KHO GIỮA CÀI ĐẶT: X0 đã đổi tên theo mã nhưng còn rev 0, chưa dấu
        # vết ghi - trạng thái HỢP LỆ giữa lượt cài X9, không phép 0i* nào
        # được kêu; mutant or-hóa báo oan mà suite xanh (rubric 09, m05)
        with tempfile.TemporaryDirectory() as _tdgc:
            _ggc = Path(_tdgc) / "kho"
            _igc = _ggc / "00_Index"
            _igc.mkdir(parents=True)
            import shutil as _shgc
            for _fgc in FILE_BAT_BUOC + FILE_KEM:
                (_igc / _fgc).parent.mkdir(parents=True, exist_ok=True)
                _shgc.copy(goc / _fgc, _igc / _fgc)
            _shgc.copy(sorted(goc.glob("INSTRUCTION_WORKOPS_v*.md"))[0], _igc)
            (_igc / "_so" / "_inbox" / "_da_nap").mkdir(parents=True)
            for _agc, _bgc in [
                    ("X0_CAUHINH_TEMPLATE.md", "X0_CAUHINH_GCD.md"),
                    ("X1_CAM_TEMPLATE.md", "X1_CAM_GCD.md"),
                    ("X2_PHATHANH_TEMPLATE.md", "X2_PHATHANH_GCD.md"),
                    ("X3_CUAVAO_TEMPLATE.md", "X3_CUAVAO_GCD.md"),
                    ("X3E_EMAIL_TEMPLATE.md", "X3E_EMAIL_GCD.md"),
                    ("X4_RASOAT_TEMPLATE.md", "X4_RASOAT_GCD.md"),
                    ("X5_HESO_TEMPLATE.md", "X5_HESO_GCD.md")]:
                (_igc / _agc).rename(_igc / _bgc)
            import contextlib as _clgc, io as _iogc
            _bufgc, _argvgc = _iogc.StringIO(), sys.argv
            try:
                sys.argv = ["kvh", str(_igc), str(_ggc)]
                with _clgc.redirect_stdout(_bufgc):
                    try:
                        _kv26.main(_igc)
                    except SystemExit:
                        pass
            finally:
                sys.argv = _argvgc
            ca.append(("kho giữa cài đặt (rev 0 đã đổi tên) không LECH 0i",
                       "LECH  0i" not in _bufgc.getvalue()))

        # BIÊN 0m: backup ngoài kho đúng 7 ngày tuổi - đúng nhịp "sao mỗi
        # tuần" - KHÔNG được kêu; mutant <7 tố oan đúng người làm đúng nhịp
        # (giám khảo rubric 06, N2)
        with tempfile.TemporaryDirectory() as _td0m:
            _kho0, _idx0, _so0, _G0 = _kho_song(goc, _td0m)
            _ngoai0 = Path(_td0m) / "usb_saoluu"
            _ngoai0.mkdir()
            _f0 = _ngoai0 / "backup_tuan.zip"
            _f0.write_text("x", encoding="utf-8")
            import os as _os0m, time as _t0m
            _moc7 = _t0m.time() - 7 * 86400
            _os0m.utime(_f0, (_moc7, _moc7))
            _p0 = _idx0 / "X0_CAUHINH_FUZ.md"
            _s0 = _p0.read_text(encoding="utf-8")
            _m0 = re.search(r"^@KHO\.SAOLUU[^\n]*$", _s0, re.M)
            _ghi(_p0, _s0[:_m0.start()] + "@KHO.SAOLUU      "
                 + str(_ngoai0) + _s0[_m0.end():])
            import contextlib as _cl0, io as _io0
            _buf0, _argv0 = _io0.StringIO(), sys.argv
            try:
                sys.argv = ["kvh", str(_idx0), str(_kho0)]
                with _cl0.redirect_stdout(_buf0):
                    try:
                        _kv26.main(_idx0)
                    except SystemExit:
                        pass
            finally:
                sys.argv = _argv0
            ca.append(("backup ngoài kho đúng 7 ngày tuổi không bị 0m tố",
                       "LECH  0m." not in _buf0.getvalue()))

        # neo BÀN GIAO phải NHẮC: người cũ trong @NHIP.BANGIAO còn việc đang
        # mở gán tên - lời hứa "rà sang người mới" nay có máy (rubric 04)
        with tempfile.TemporaryDirectory() as _tdbg:
            _khob, _idxb, _sob, _Gb = _kho_song(goc, _tdbg)
            _pb = _idxb / "X0_CAUHINH_FUZ.md"
            _ghi(_pb, _pb.read_text(encoding="utf-8").replace(
                '@NHIP.BANGIAO    <điền: tên người cũ, người mới, ngày bàn giao, hoặc "chưa có">',
                "@NHIP.BANGIAO    Long, Trân, 2026-08-20", 1))
            _ghi(_sob / "VIEC.md",
                 (_sob / "VIEC.md").read_text(encoding="utf-8").rstrip(NL) + NL
                 + "| DA1 | V-DA1-002 | Van hanh he A | b | Long | |"
                   " 2099-12-31 | ĐANG LÀM | | " + _Gb + " |" + NL)
            import contextlib as _clb, io as _iob
            _bufb, _argvb = _iob.StringIO(), sys.argv
            try:
                sys.argv = ["kvh", str(_idxb), str(_khob)]
                with _clb.redirect_stdout(_bufb):
                    try:
                        _kv26.main(_idxb)
                    except SystemExit:
                        pass
            finally:
                sys.argv = _argvb
            ca.append(("neo bàn giao nhắc việc mở còn gán người cũ",
                       "LƯU Ý  bàn giao" in _bufb.getvalue()))
            # ca LÀNH đối chứng: việc mở gán NGƯỜI MỚI thì KHÔNG được nhắc -
            # mutant or-hóa điều kiện đếm mọi việc mở bị ca này giết
            # (rubric 05, m07 seed 46)
            _ghi(_sob / "VIEC.md",
                 (_sob / "VIEC.md").read_text(encoding="utf-8").replace(
                     "| Long |", "| Trân |"))
            _bufb2 = _iob.StringIO()
            try:
                sys.argv = ["kvh", str(_idxb), str(_khob)]
                with _clb.redirect_stdout(_bufb2):
                    try:
                        _kv26.main(_idxb)
                    except SystemExit:
                        pass
            finally:
                sys.argv = _argvb
            ca.append(("việc mở gán người MỚI thì bàn giao im",
                       "LƯU Ý  bàn giao" not in _bufb2.getvalue()))
            # vế PHỤ TRÁCH C2: người gật mức C đã nghỉ mà C2 còn ghi tên -
            # LƯU Ý phải nêu (rubric 05, khoản 3)
            _s_pm = _pb.read_text(encoding="utf-8")
            import re as _rebg
            _m_pm = _rebg.search(r"^@DUAN\.PHANMEM.*$", _s_pm, _rebg.M)
            # khuôn NHIỀU DÒNG - đúng khuôn ví dụ của template; bản
            # một-dòng làm regex cũ "tái đo chết" mà không phủ khuôn thật
            # (giám khảo rubric 06)
            _ghi(_pb, _s_pm[:_m_pm.end()] + NL
                 + "  DA1  He cu · repo github.com/cty/hc · web · dev may"
                   " doi, chạy thật hc.bacha.vn" + NL
                 + "        · secret o Vault · CSDL chua ro" + NL
                 + "        · phụ trách vận hành: Long ·"
                 + _s_pm[_m_pm.end():])
            _bufb3 = _iob.StringIO()
            try:
                sys.argv = ["kvh", str(_idxb), str(_khob)]
                with _clb.redirect_stdout(_bufb3):
                    try:
                        _kv26.main(_idxb)
                    except SystemExit:
                        pass
            finally:
                sys.argv = _argvb
            ca.append(("bàn giao nêu phần mềm còn ghi người cũ ở vế phụ trách",
                       "vế phụ trách" in _bufb3.getvalue()))
            # backup ngày (X5 mục 7): xóa backup_<ngày> thì 0m2 phải nhắc
            import shutil as _shbg
            _shbg.rmtree(_sob / "_lich_su" / "backup_20260828",
                         ignore_errors=True)
            _bufb4 = _iob.StringIO()
            try:
                sys.argv = ["kvh", str(_idxb), str(_khob)]
                with _clb.redirect_stdout(_bufb4):
                    try:
                        _kv26.main(_idxb)
                    except SystemExit:
                        pass
            finally:
                sys.argv = _argvb
            ca.append(("xóa backup ngày thì 0m2 nhắc",
                       "LƯU Ý  0m2" in _bufb4.getvalue()))


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
        ca.append(("0i trên CHÍNH template: 39 ô trống khi chưa bật profile nào,"
                   " 46 khi bật REGULATED và EMAIL; không nuốt dòng cú pháp hay ô"
                   " đã điền; có khóa của C13",
                   len(_mt) == 39 and len(_kv26.muc_con_trong(
                       _tpl.replace("  [ ] EMAIL", "  [x] EMAIL")
                           .replace("  [ ] REGULATED", "  [x] REGULATED"))) == 46
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
        # bằng chứng phải NẰM THẬT trên đĩa: X3E chỉ cho dọn staging KHI .eml
        # đã chuyển sang vùng lưu chính, và từ vòng 52 phép 12j mở file ra xem
        don_xoa = {"<a@x>": {"purged_at": "2026-08-25",
                             "eml_final_path": "04_Trao_doi/mail_a.eml",
                             "attachment_final_paths": [], "sha256": EML_SHA}}
        r = chay_email(nk=P("<a@x>", pay=pay_xoa) + "\n" + C("<a@x>") + "\n",
                       reg=["<a@x>"],
                       files={"_so/VIEC.md": "| V-001 | viec |\n",
                              "04_Trao_doi/mail_a.eml": "eml"},
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
        # đổi TÊN CỘT Conversation-ID: 12i2 là người canh DUY NHẤT của tình
        # huống 12f/12i cùng tắt im lặng - chưa ca nào từng ép nó đỏ (tự
        # quét vòng 90)
        r = chay_email(nk=SACH, reg=["<a@x>"], thu_header=(
            "| Mã | Luồng | Conv | Message-ID cuối | Trạng thái |\n"
            "|---|---|---|---|---|\n"))
        ca.append(("đổi tên cột Conversation-ID bị 12i2 bắt",
                   r.get("12i2. header THU còn đủ tên cột then chốt") is False))
        # thao tác {} rỗng: bị bắt
        r = chay_email(nk=P("<a@x>", pay=dict(PAY, thao_tac=[{}])) + "\n" + C("<a@x>") + "\n",
                       reg=["<a@x>"])
        ca.append(("thao tác rỗng thiếu trường bị bắt", r.get(TEN_12H) is False))
        # hai thao tác trùng operation_id: bị bắt
        t1 = {"operation_id": "op1", "so": "VIEC", "dong": "V-001", "noi_dung": "x"}
        r = chay_email(nk=P("<a@x>", pay=dict(PAY, thao_tac=[t1, dict(t1)])) + "\n"
                       + C("<a@x>") + "\n", reg=["<a@x>"])
        ca.append(("operation_id trùng trong một mail bị bắt", r.get(TEN_12H) is False))
        # operation_id SAI KIỂU (số): fixture cũ chỉ thử THIẾU trường, nên
        # đột biến isinstance->and sống sót (giám khảo rubric 01, mutant m05)
        r = chay_email(nk=P("<a@x>", pay=dict(PAY, thao_tac=[dict(t1, operation_id=123)]))
                       + "\n" + C("<a@x>") + "\n", reg=["<a@x>"])
        ca.append(("operation_id sai kiểu (số) bị bắt", r.get(TEN_12H) is False))
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
                       files={"_so/VIEC.md": "| V-001 | viec |\n",
                              "04_Trao_doi/mail_a.eml": "eml",
                              "04_Trao_doi/f.pdf": "PDF"}, don=DON_OK)
        ca.append(("staging đã dọn có manifest hợp lệ là PASS", r.get(TEN_12J) is True))
        # manifest KHAI đã chuyển bằng chứng mà file KHÔNG có trên kho: nguyên
        # văn thư của một hợp đồng đã ký biến mất vĩnh viễn, mà bản cũ chỉ kiểm
        # manifest là chuỗi RỖNG HAY KHÔNG nên in PASS (hội đồng vòng 18)
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=IDX_SACH,
                       files={"_so/VIEC.md": "| V-001 | viec |\n"}, don=DON_OK)
        ca.append(("manifest dọn khai file bằng chứng KHÔNG có trên kho bị bắt",
                   r.get(TEN_12J) is False))
        # đường dẫn đúng nhưng nội dung KHÁC sha256 manifest đã khai
        r = chay_email(nk=SACH, reg=["<a@x>"], idx=IDX_SACH,
                       files={"_so/VIEC.md": "| V-001 | viec |\n",
                              "04_Trao_doi/mail_a.eml": "ĐÃ BỊ THAY RUỘT",
                              "04_Trao_doi/f.pdf": "PDF"}, don=DON_OK)
        ca.append(("bằng chứng ở vùng lưu chính khác sha256 manifest bị bắt",
                   r.get(TEN_12J) is False))
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
             not hong and len(ca) == 111,
             str(hong) + (f" · đếm được {len(ca)} ca mà bộ khai 111: bớt ca là"
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
        ("thao tác kỹ thuật NGOÀI phạm vi thực thi; ghi nhận rollback chạy thật là C", "NGOÀI PHẠM VI" in docs["X5_HESO_TEMPLATE.md"] and "ROLLBACK" in docs["X5_HESO_TEMPLATE.md"] and "SOẠN CHECKLIST" in docs["X5_HESO_TEMPLATE.md"]),
        # PHẠM VI TỔ CHỨC PHẦN MỀM: sáu luật giữ TRỌN chuỗi từ README tới X2.
        # Đây là yêu cầu nghiệp vụ có thật của người dùng ("công ty có dự án
        # phần mềm cần nắm rõ phạm vi tổ chức để các vận hành liên quan
        # chính xác hơn"), nên nó phải do MÁY giữ chứ không do lời khai.
        ("README có mục riêng cho công ty phần mềm, kèm LÝ DO phải khai", "## Công ty có phần mềm" in docs["README.md"] and "KHAI RÕ PHẠM VI TỔ" in docs["README.md"] and "vận hành liên quan mới chính xác" in docs["README.md"] and "NGOÀI PHẠM VI" in docs["README.md"]),
        ("X9 hỏi phạm vi tổ chức ngay phiên cài đặt khi dự án là phần mềm", "là PHẦN MỀM thì hỏi đủ TÁM trường phạm vi tổ chức" in docs["X9_CAIDAT.md"] and "người phụ trách vận hành" in docs["X9_CAIDAT.md"]),
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
        ("README bước 3 nạp CHAT khớp BENCHMARK: không X9, không X4", "ĐỪNG đưa X9" in docs["README.md"] and "X0 tới X5, X9" not in
          (docs["README.md"] + docs["DOC_TRUOC.md"])),
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
         not thieu_luat and len(_luat) == 74,
         str(thieu_luat) + (f" · đếm được {len(_luat)} luật mà bộ khai 74: bớt"
                            f" luật là bớt lưới không ai hay; đổi số thì sửa"
                            f" con số này trong CÙNG lượt vá"
                            if len(_luat) != 74 else ""))

    _h15, _phu15, _n15 = phep_danh_muc(goc)
    kiem("15. danh mục TRẠNG THÁI HỎNG: mỗi nghĩa vụ X4 khai máy dò đều có"
         f" trạng thái mẫu và rà soát kêu ({_n15} ca)",
         not _h15, "; ".join(_h15[:4]))

    phep_fuzz(goc, _phu15)

    # 2d. Hệ số quy đổi ước-lượng -> token THẬT là lời khai NẶNG KÝ nhất của
    #     BENCHMARK, và trước vòng 47 không ai giữ nó: bộ tự khai "chưa đối
    #     chứng tokenizer sản xuất nào" rồi vẫn in mọi số như thể là token.
    #     Đo lại KHI CÓ thư viện; không có thì BỎ QUA, bộ giữ nguyên tính chất
    #     không phụ thuộc gói ngoài.
    _m2d = re.search(r"đo\s+thật\s+([\d.]+)\s+token\s*-\s*hệ số x([\d,]+)",
                     docs["BENCHMARK_TOKEN.md"])
    try:
        from tokenizers import Tokenizer as _Tk
        _tk = _Tk.from_pretrained("Xenova/claude-tokenizer")
    except Exception:
        _tk = None
    if _tk is None:
        print("  BỎ QUA  2d. không có tokenizers hay bản tải về; hệ số token"
              " giữ nguyên lời khai, chưa đo lại lượt này")
    else:
        _nd2d = (docs["INSTRUCTION"] + docs["_so/X0_INDEX.md"]
                 + docs["_so/BANG_DIEU_KHIEN.md"])
        _that = len(_tk.encode(_nd2d).ids)
        _khai = int(_m2d.group(1).replace(".", "")) if _m2d else 0
        kiem("2d. hệ số quy đổi token khai ở BENCHMARK khớp tokenizer thật",
             bool(_m2d) and abs(_that - _khai) <= 0.03 * _that,
             f"BENCHMARK khai {_khai} token, tokenizer Claude đo {_that}."
             f" Đây là con số nói cho người dùng biết họ TRẢ bao nhiêu; khai"
             f" sai nó là sai toàn bộ phần token của bộ")

    # 15b. Danh mục trạng thái phải kẹp vào CHÍNH LỜI KHAI của X4. X4 tự liệt
    #      dòng nào "dò được bằng máy"; thêm một dòng nghĩa vụ mà danh mục đứng
    #      yên là bộ lại hứa nhiều hơn thứ nó làm. Ghim tập số ở đây, sửa X4 là
    #      phải sửa danh mục trong CÙNG lượt vá.
    _m15 = re.search(r"Phần dò được bằng máy \(([^)]*)\)",
                     docs["X4_RASOAT_TEMPLATE.md"])
    _khai15 = {int(x) for x in re.findall(r"\d+", _m15.group(1))} if _m15 else set()
    kiem("15b. tập dòng X4 tự khai máy dò được khớp bản ghim của danh mục",
         _khai15 == X4_MAY_DO,
         f"X4 khai {sorted(_khai15)}, danh mục ghim {sorted(X4_MAY_DO)}."
         f" Sửa X4 mà không sửa danh mục là bộ hứa nhiều hơn thứ nó làm")



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
        # hai script KHÔNG nhúng nữa (49,8% bản gộp, không ai đọc ở đây):
        # chỉ đòi CON TRỎ. GHICHU và mọi file LUẬT vẫn phải nguyên văn.
        thieu_gop += [t for t, nd in kem.items()
                      if nd.strip() and not t.endswith(".py")
                      and nd.strip() not in nd_gop]
        thieu_gop += [t for t in kem if t.endswith(".py") and t not in nd_gop]
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
