#!/usr/bin/env python3
# kiem_van_hanh.py · kiểm máy hệ WORKOPS đang chạy · v27 · 20260825
# v27, theo hội đồng vòng 7: loc_ban_chinh lên tầng module để fixture ghim
# được ba hành vi v26 · regex tên chuẩn X0 khớp luật (mã 3-4 ký tự A-Z 0-9,
# không dấu) và 0c có nhánh "tên không đúng chuẩn: đổi tên file" thay vì
# cáo buộc "mất cấu hình" oan · tự vệ tham số vế ba: gốc kho không tồn tại
# (ổ ngoài chưa cắm) thì bỏ qua quan sát, KHÔNG ghi đè cache mốc ổn định ·
# XÓA PHÁP LÝ khớp lưới: dòng sổ tombstone "[đã xóa theo Q-" vẫn giữ mã nên
# 12l tự khớp, fixture 70 ghim "kho sau xóa đúng luật phải sạch".
# v26, theo hội đồng vòng 6: nhận dạng bản sao đồng bộ về MỘT nguồn cho cả
# ba tầng - MAU_TAM (quan sát kho) học thêm khuôn " (1)", " copy", " copy 2"
# của Drive và macOS nên bản sao file nghiệp vụ hết được ĐỀ XUẤT vào sổ mức
# A; sổ NHATKY và X0 chọn bản chính theo TÊN CHUẨN (NHATKY_<năm>Q<quý>,
# X0_CAUHINH_<MÃ>) nên khuôn OneDrive -<TênMáy> hay bất kỳ hậu tố lạ nào
# đều bị 0b flag thay vì lọt vào glob gây lệch giả "trùng mã G" · tự vệ
# tham số vế hai: gốc kho trùng 00_Index cũng dừng sớm kèm gợi ý.
# v25, khâu đường nối theo hội đồng vòng 5 (không tính năng mới): ghi_cache
# bọc lỗi GHI, cache hỏng chỉ in lưu ý rồi chạy tiếp hết báo cáo · truyền
# nhầm gốc kho thay vì 00_Index được tự nhận, dừng sớm kèm gợi ý thay vì
# phun "khôi phục mức C" oan · 10a/10b phân nhánh KHÔNG KIỂM ĐƯỢC khi file
# bị khóa (sha rỗng), hết cáo buộc "bị sửa tại chỗ" oan cho bản ĐÃ KÝ đang
# mở trong app · bộ lọc bản chính và 0b nhận thêm khuôn bản sao đồng bộ
# " (1)", " - Copy", "(bản sao)" cho sổ.
# v24, theo hội đồng vòng 4: MỘT file không đọc được (khóa Office, sai
# encoding) không giết cả báo cáo nữa: doc() và sha_file() bắt lỗi, gom vào
# phép 0f "file không đọc được" thay vì traceback · file tạm ~$/.tmp không
# hash (đằng nào cũng bị loại khỏi suy hiện hành) · bộ lọc bản chính dùng
# CHUNG (TEMPLATE, conflicted, xung đột) cho X0 lẫn NHATKY: chỉ còn bản
# (xung đột) của NHATKY thì 0d LỆCH "bản chính mất" thay vì PASS tự mâu
# thuẫn với 0b · 12k khi nhật ký mất hay rỗng đổi chẩn đoán GIỮ index, hết
# xúi dọn _thu_ap_dung.json · kiểm basename áp cho CẢ đính kèm de_ngoai ·
# 12e nhận dạng hiển thị "Tên <mail@dom>" và danh sách hộp cũ @NHIP.HOPTHU_CU.
# v23, theo hội đồng vòng 3 (giám khảo dựng kho giả lập chạy thật): glob
# NHATKY loại _TEMPLATE (template nằm trong _so theo cài chuẩn che phép 0d,
# xóa trục sự thật vẫn "hệ sạch") · kiem_payload miễn sha256/bytes cho đính
# kèm mang cờ de_ngoai (chỉ đòi ten + ly_do), máy hết đá luật X3E mục 2 ·
# 12d và 12j2 xử cả nhật ký RỖNG (file còn, 0 sự kiện) như nhật ký vắng:
# GIỮ registry, staging không bị gọi mồ côi oan · 0c phân biệt "chưa cài,
# chỉ thấy template" (bỏ qua êm) với "mất X0" và "nhiều ứng viên" · 12e
# loại cả bản conflicted khỏi nguồn đọc cấu hình.
# v22, theo hội đồng vòng 2 (chạy thật 4 kịch bản đứt gãy): chọn X0 TẤT ĐỊNH,
# loại _TEMPLATE và conflicted khỏi glob (sau git pull template rev 0 đứng
# trước bản mã theo bảng chữ, hệ đang chạy bị báo "chưa cài" oan) · 0d đòi
# NHATKY tồn tại khi rev >= 1 và THU khi pipeline EMAIL có dấu vết (trước đây
# xóa trọn trục sự thật vẫn "hệ sạch") · 0b quét conflicted copy cả bộ X ở
# gốc 00_Index · 12e nhận dòng mang nhãn (EMAIL) đúng khuôn template, lọc
# template khỏi nguồn đọc · 12d khi nhật ký mất đổi chẩn đoán, hết xúi xóa
# registry · 12j bỏ qua đính kèm mang cờ de_ngoai (vượt @NHIP.TRANDINHKEM).
# v21, theo hội đồng đánh giá 6 lăng kính: phép 0 đòi sổ lõi TỒN TẠI trên đĩa
# (trước đây doc() nuốt file vắng thành chuỗi rỗng, mất sổ mà PASS im lặng) ·
# phép 0b dò conflicted copy của file sổ trong _so (đồng bộ mây sinh, trước
# đây vô hình vì 00_Index bị loại khỏi vùng quét, riêng bản conflict của
# NHATKY còn lọt glob gây chẩn sai "trùng mã G") · glob NHATKY loại file
# conflict · thông điệp 12a/12d hết gợi ý sai hướng khi mất RIÊNG nhật ký:
# GIỮ registry, cấm dựng lại từ tập COMMITTED rỗng.
# v20, vá chạy trên Windows: containment staging và đính kèm so bằng
# pathlib (d.parents) thay vì so chuỗi có "/", vì resolve() trên Windows
# trả "\\" nên phép so chuỗi báo lệch oan cả bộ sạch · stdout ép UTF-8,
# console cp1252 hết crash khi in tiếng Việt · docstring bao_phu thành
# raw string, hết SyntaxWarning khi import.
# v19, theo vòng đánh giá 22: phạm vi ĐÃ VÀO SỔ tính trên TOÀN BỘ TAILIEU kể cả
# ở chế độ --ho, nên một dòng trỏ THƯ MỤC vẫn bao phủ file con; v18 lọc dòng sổ
# theo họ TRƯỚC khi tính bao phủ nên file đã nằm trong bộ hồ sơ bị đề xuất
# _INBOX oan. Chỉ phần kiểm file mất, sha và bất biến mới thu về đúng họ · cache
# đời cũ (không mang "v": 2) chỉ có mốc chung toàn kho nên bằng chứng ổn định
# của nó có thể sai: nạp để so nội dung nhưng ĐÓNG DẤU LẠI mốc, lần chạy đầu sau
# nâng cấp coi như quan sát mới.
# v18, theo vòng đánh giá 18 (sửa lỗi thực thi của v17, không đổi luật):
# selector --ho CHỈ nhận đường dẫn tương đối tới MỘT FILE, từ đó suy khóa (thư
# mục, họ chuẩn hóa) rồi duyệt ĐÚNG thư mục đó bằng iterdir, hết rglob cả kho ·
# nghĩa "thư mục" và "tên họ trơ" bị bỏ vì kéo nhầm họ khác và kéo cùng tên ở
# dự án khác · cache đổi sang MỐC RIÊNG TỪNG FILE ("luc" = lần đầu thấy đúng
# nội dung đang có), nên hai lần quét sát nhau không còn công nhận ổn định, kể
# cả trong chế độ --ho · hợp nhất cache đổi thành THAY ĐÚNG HỌ đang quét, file
# đã xóa khỏi họ biến mất khỏi cache, các họ khác giữ nguyên · không khớp file
# nào là LỆCH, không PASS im lặng · thiếu giá trị sau --ho là lỗi cách dùng,
# không âm thầm quét cả kho · quet_ho và quan_sat_kho nhận bay_gio để fixture
# kiểm mốc năm phút bằng thời gian giả, không phải chờ thật.
# v17: chế độ --ho quét đúng MỘT họ tài liệu (phục vụ X5 KIỂM BẢN "lần đầu chạm
# trong phiên") thay vì quét lại cả kho.
# v15: áp trần runtime cho BANG_DIEU_KHIEN (4.200 ký tự, xấp xỉ 1.400 token):
# bảng chạy thật phình quá thì LỆCH, nhắc dọn thay vì để thuế mở phiên tăng ngầm.
# v16: áp trần runtime cho cả X0_INDEX (2.400 ký tự, xấp xỉ 800 token) để lời
# cam kết thuế mở phiên đứng vững khi vận hành lâu dài.
# Chạy: python3 kiem_van_hanh.py <thư mục 00_Index> [<gốc kho>]
#       [--ho <đường dẫn tương đối tới MỘT file>]
# Máy hóa phần rà không cần suy luận. Chỉ BÁO CÁO, không sửa gì.
# v5, sửa theo vòng đánh giá 8: sha256 THẬT thay cho dung lượng · luật "ổn định
# qua hai lần quan sát" chạy thật bằng cache _so/_quan_sat_truoc.json (máy sinh,
# không phải sổ) · file không có vN chọn theo mtime, không đủ căn cứ thì KHÔNG
# XÁC ĐỊNH · file mới độc lập vẫn được đề xuất _INBOX · khóa nhận dạng một họ
# tài liệu = thư mục tương đối + họ tên, hai dự án trùng tên file không lẫn nhau.
# v6, sau lượt team agent nội bộ: bất biến gồm cả ĐÃ DUYỆT NỘI BỘ và TRẢ HỒ SƠ ·
# cache hỏng tự phục hồi · mã G định dạng cũ bị báo riêng, không cướp watermark ·
# vN nhận cả dạng -v03 và (v03) · thêm phép 3c (lượt XONG phải để dấu ở sổ) và
# 3d (lượt mức C phải khớp plan ĐÃ GHI), khớp tuyên bố dòng 19, 23 của X4.
# v7, theo vòng đánh giá 9: họ tài liệu chuẩn hóa bỏ mọi ký tự phân cách (hết
# tách sai với dạng (v3)) · quét MỌI file thường trừ danh sách loại, không giới
# hạn 7 đuôi · hash đủ mọi cỡ file, chỉ cảnh báo thời gian với file lớn · hai lần
# quét phải cách nhau tối thiểu 5 phút mới tính ổn định · phép 3c 3d đọc đúng cột
# Ghi lần và đúng dòng plan ĐÃ GHI. Script chỉ BÁO CÁO; thứ duy nhất nó ghi là
# cache máy sinh _so/_quan_sat_truoc.json để giữ luật ổn định hai lần.
# v8, theo vòng đánh giá 10: luật 5 phút ENFORCE THẬT (cache non hơn 5 phút thì
# không được dùng làm bằng chứng ổn định) · loại hẳn 00_Index, script, config
# khỏi vùng quét nghiệp vụ · chuẩn hóa họ đổi separator về "_" thay vì xóa sạch,
# AB_C và A_BC không còn bị trộn.
# v9, theo vòng đánh giá 11: dòng TAILIEU trỏ THƯ MỤC bao phủ mọi file con, hết
# đề xuất thừa cho hồ sơ nhiều tài liệu · bỏ loại theo đuôi script/config trên
# toàn kho, chỉ loại vùng hệ thống và danh sách khai ở _so/_quan_sat_bo.txt.
# v10, theo vòng đánh giá 12: BỎ lọc tiền tố "9" (98_Assets, 99_Goc phải được
# quét, X4 đòi kiểm sha 99_Goc), chỉ loại đích danh 99_Archive · thêm phép 12
# kiểm email: nhật ký với registry lệch, Message-ID trùng trong THU, hộp thư
# ngoài khai báo · nhật ký nạp mail thêm trường hop_thu.
# v11, theo vòng đánh giá 13: kiem_email viết lại cứng tay: thiếu nhật ký HAY
# registry đều LỆCH · registry phải BẰNG ĐÚNG tập khóa COMMITTED (thiếu và thừa
# đều lệch) · parse NDJSON một lượt, dòng hỏng hay không phải object thành LỆCH
# chứ không crash · so hộp thư bằng chuẩn hóa chính xác, không substring · khóa
# cuối của luồng THU so theo CỘT header, bắt cả khóa fallback không có dấu @ ·
# PREPARED không COMMITTED là lượt dở dang · trả kết quả để fixture gọi cả hàm.
# v12, theo vòng đánh giá 14: parse nhật ký theo TỪNG KHÓA giữ thứ tự và số lần
# xuất hiện · "ev" ngoài PREPARED/COMMITTED, khóa không phải chuỗi, thiếu
# hop_thu đều là dòng hỏng, không crash · 12g mô hình mỗi khóa đúng chuỗi
# PREPARED rồi COMMITTED (mồ côi, ngược thứ tự, lặp đều lệch) · 12h mọi
# PREPARED phải mang payload phục hồi thật (staging + thao_tac) · registry
# bắt buộc DANH SÁCH CHUỖI ({} hay danh sách chứa object là lệch, không crash)
# · 12i Conversation-ID duy nhất trong THU.
# v13, theo vòng đánh giá 15: khóa MỘT dạng "khoa" (gặp msgId kiểu cũ là dòng
# hỏng, phải migration riêng) · kiem_payload kiểm DỮ LIỆU: staging là đường dẫn
# tương đối trong _so/_thu_staging không thoát ra ngoài, thao tác đủ
# operation_id duy nhất + sổ đích hợp lệ + mã dòng + nội dung, đính kèm khai
# sha256 và byte · 12e thiếu @NHIP.HOPTHU khi EMAIL đã chạy là LỆCH, hết BỎ QUA
# · 12j staging thật trên đĩa (thư mục, .eml hay body, sha và byte từng đính
# kèm) · 12k index đủ hai chiều với thao tác COMMITTED · 12l index trỏ mã dòng
# có thật trong sổ đích.
# v14, theo vòng đánh giá 16: 12j hiểu VÒNG ĐỜI staging (chưa COMMITTED thì
# staging bắt buộc còn; COMMITTED đã dọn phải có mục manifest _thu_don_staging
# hợp lệ mới PASS), .eml/body không rỗng và khớp eml_sha256, đường dẫn
# resolve() phải nằm trong _thu_staging (chặn symlink), tên đính kèm là
# basename thuần và file resolve() không thoát ra ngoài · containment staging
# bằng normpath, hết khe ../_so/_thu_staging · thư mục staging tên
# sha256(khóa), payload bắt buộc metadata nguồn (conv_id, nguoi_gui,
# thoi_diem, tieu_de) và eml_sha256 · 12k tập mục index BẰNG ĐÚNG tập thao
# tác COMMITTED, sổ và mã dòng khớp payload · 12l so mã dòng theo ĐÚNG Ô
# bảng, không so chuỗi toàn văn, có hash nội dung thì đối chiếu thêm.

import hashlib
import json
import re
import sys
from pathlib import Path

# Console Windows mặc định cp1252 không in được tiếng Việt: ép UTF-8,
# lỗi ký tự thì thay thế chứ không crash giữa chừng phép kiểm.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

loi = []
MAU_G = r"G-\d{8}(?:-[A-Z0-9]+)?-\d{2}"
BAT_BIEN = ("ĐÃ GỬI DUYỆT", "ĐÃ DUYỆT NỘI BỘ", "ĐÃ PHÁT HÀNH", "ĐÃ NỘP",
            "TRẢ HỒ SƠ", "ĐÃ KÝ", "ĐÃ CẤP")
MAU_TAM = re.compile(r"^~\$|\.tmp$|\.bak\d*$|conflicted copy|xung đột|autosave|-nhap\d+"
                     r"| \(\d+\)\.| copy( \d+)?\.| - copy|\(bản sao\)", re.I)
# khuôn " (1).", " copy.", " copy 2.", " - Copy", "(bản sao)": bản sao đồng bộ
# của Drive, macOS, Windows - coi như file tạm, không vào suy hiện hành,
# không được đề xuất vào sổ (hội đồng vòng 6)
MAU_V = re.compile(r"[-_ (]v(\d+)(?=[^0-9A-Za-z]|$)", re.I)
DUOI_BO = (".tmp", ".bak", ".log", ".lnk", ".ini", ".exe", ".dll", ".pyc",
           ".ds_store", ".crdownload", ".part")  # chỉ loại rác thật; script và
           # config NGHIỆP VỤ ngoài 00_Index vẫn được quan sát như tài liệu
THU_MUC_HE_THONG = ("00_Index",)  # vùng luật, sổ, script hệ thống
# Loại thêm theo TỪNG CÔNG TY: khai đường dẫn tương đối (một dòng một mục) trong
# _so/_quan_sat_bo.txt, truyền vào quet_ho qua tham số bo_them
TRAN_CANH_BAO = 200 * 1024 * 1024  # file lớn hơn: vẫn hash đủ, chỉ cảnh báo chậm
KHOANG_ON_DINH = 300  # giây; hai lần quét cách dưới ngưỡng này tính là một lần


CACH_CHAY = ("Cách chạy: python3 kiem_van_hanh.py <thư mục 00_Index> [<gốc kho>]"
             " [--ho <đường dẫn tương đối tới MỘT file>]")


def tach_tham_so(argv):
    """Tách cờ --ho khỏi tham số thường. Thiếu giá trị sau --ho là LỖI CÁCH DÙNG,
    không được im lặng bỏ qua rồi quét cả kho (lỗi của v17)."""
    thuong, loc_ho, i = [], None, 0
    while i < len(argv):
        a = argv[i]
        if a == "--ho":
            if i + 1 >= len(argv) or argv[i + 1].startswith("--"):
                raise ValueError("--ho thiếu giá trị: cần đường dẫn tương đối tới một file")
            loc_ho, i = argv[i + 1], i + 2
            continue
        if a.startswith("--ho="):
            loc_ho = a[len("--ho="):]
            if not loc_ho.strip():
                raise ValueError("--ho thiếu giá trị: cần đường dẫn tương đối tới một file")
            i += 1
            continue
        thuong.append(a)
        i += 1
    return thuong, loc_ho


def bao(ten, ok, chi_tiet=""):
    print(f"  {'PASS' if ok else 'LECH'}  {ten}" + (f": {chi_tiet}" if chi_tiet and not ok else ""))
    if not ok:
        loi.append(ten)


LOI_DOC = []  # (đường dẫn, lý do) các file KHÔNG ĐỌC ĐƯỢC trong lượt chạy;
              # phép 0f báo một dòng LỆCH đích danh thay vì chết traceback (v24)


def doc(p):
    try:
        return p.read_text(encoding="utf-8") if p.is_file() else ""
    except (UnicodeDecodeError, OSError) as e:
        LOI_DOC.append((str(p), type(e).__name__))
        return ""


def sha_file(p):
    try:
        if p.stat().st_size > TRAN_CANH_BAO:
            print(f"        LƯU Ý: file lớn {p.name} ({p.stat().st_size // (1 << 20)} MB), hash sẽ chậm")
        h = hashlib.sha256()
        with open(p, "rb") as f:
            for khoi in iter(lambda: f.read(1 << 20), b""):
                h.update(khoi)
        return h.hexdigest()
    except OSError as e:
        LOI_DOC.append((str(p), type(e).__name__))
        return ""


def dong_bang(nd):
    """Các dòng dữ liệu bảng (bỏ header và dòng kẻ), mỗi dòng là list ô."""
    lines = nd.splitlines()
    headers = set()
    for i, d in enumerate(lines[:-1]):
        if d.startswith("|") and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
            headers.add(tuple(o.strip() for o in d.strip("|").split("|")))
    ket = []
    for d in lines:
        if d.startswith("|") and not re.match(r"^\|[\s:|-]+\|$", d):
            r = [o.strip() for o in d.strip("|").split("|")]
            if tuple(r) not in headers:
                ket.append(r)
    return ket


def cua_cua(m):
    """Cửa của mã G; mã định dạng cũ (3 khúc, không cửa) trả None."""
    phan = m.split("-")
    return phan[2] if len(phan) == 4 else None


def watermark(ma):
    wm = {}
    for m in ma:
        c = cua_cua(m)
        if c is None:
            continue  # mã cũ không cửa: không tính watermark, báo riêng ở 3b2
        k = (m[2:10], m.split("-")[-1])
        if c not in wm or k > (wm[c][2:10], wm[c].split("-")[-1]):
            wm[c] = m
    return wm


def la_file_tam(ten):
    return bool(MAU_TAM.search(ten))


def loc_ban_chinh(cac, mau=None):
    """Bộ lọc DÙNG CHUNG cho mọi phép chọn bản đang chạy của một sổ hay file
    cấu hình: loại _TEMPLATE, conflicted, mọi khuôn bản sao đồng bộ; mau
    (regex fullmatch) là TÊN CHUẨN - có mau thì chỉ nhận đúng tên chuẩn, nên
    khuôn conflict lạ (OneDrive -<TênMáy>...) cũng không lọt. Tầng module để
    fixture ghim được hành vi (hội đồng vòng 7)."""
    ket = [q for q in sorted(cac) if "TEMPLATE" not in q.name
           and "conflicted" not in q.name.lower() and "xung đột" not in q.name.lower()
           and not la_file_tam(q.name)]
    if mau:
        ket = [q for q in ket if re.fullmatch(mau, q.name)]
    return ket


def chuan_hoa_ho(ten):
    """Họ = tên bỏ hậu tố vN, các cụm phân cách đổi về MỘT dấu "_", giữ đuôi.
    BC_v02, BC(v3), BC-BMH v04 về cùng dạng; AB_C và A_BC vẫn là hai họ khác."""
    goc, cham, duoi = ten.rpartition(".")
    if not cham:
        goc, duoi = ten, ""
    goc = re.sub(r"[-_ ().]+", "_", goc).strip("_").lower()
    return goc + ("." + duoi.lower() if duoi else "")


def ho_va_v(ten):
    m = MAU_V.search(ten)
    if not m:
        return (chuan_hoa_ho(ten), None)
    return (chuan_hoa_ho(ten[:m.start()] + ten[m.end():]), int(m.group(1)))


def suy_hien_hanh(items):
    """items: list {ten, sha, mtime, on_dinh}. Áp X5 mục 4.
    Trả {hien_hanh, cu, xung_dot, khong_xac_dinh, bo}. Chỉ suy VAI quan sát được."""
    kq = {"hien_hanh": [], "cu": [], "xung_dot": [], "khong_xac_dinh": [], "bo": []}
    on, cho = [], []
    for it in items:
        if la_file_tam(it["ten"]):
            kq["bo"].append(it["ten"])
        elif it.get("on_dinh", True):
            on.append(it)
        else:
            cho.append(it)
    kq["khong_xac_dinh"] += sorted(it["ten"] for it in cho)  # chưa ổn định: chờ lần quét sau
    if not on:
        return kq
    co_v = [it for it in on if ho_va_v(it["ten"])[1] is not None]
    if not co_v:
        # không có vN: chọn theo mtime, phải phân định được rõ ràng
        mt = sorted(on, key=lambda x: x.get("mtime") or 0)
        if len(on) == 1:
            kq["hien_hanh"] = [on[0]["ten"]]
        elif mt[-1].get("mtime") and (not mt[-2].get("mtime") or mt[-1]["mtime"] > mt[-2]["mtime"]):
            kq["hien_hanh"] = [mt[-1]["ten"]]
            kq["cu"] = sorted(it["ten"] for it in mt[:-1])
        else:
            kq["khong_xac_dinh"] += sorted(it["ten"] for it in on)
        return kq
    vmax = max(ho_va_v(it["ten"])[1] for it in co_v)
    dinh = [it for it in co_v if ho_va_v(it["ten"])[1] == vmax]
    if len(dinh) > 1 and len({it.get("sha") for it in dinh}) > 1:
        kq["xung_dot"] = sorted(it["ten"] for it in dinh)
    else:
        kq["hien_hanh"] = [dinh[0]["ten"]]
    kq["cu"] = sorted(it["ten"] for it in co_v if ho_va_v(it["ten"])[1] < vmax)
    kq["khong_xac_dinh"] += sorted(it["ten"] for it in on if it not in co_v)
    return kq


def khoa_ho_cua(rel):
    """Khóa nhận dạng MỘT họ tài liệu: (thư mục tương đối, họ đã chuẩn hóa).
    Hai dự án có file trùng tên vẫn là hai họ khác nhau."""
    p = str(rel).replace("\\", "/")
    return (str(Path(p).parent).replace("\\", "/"), ho_va_v(Path(p).name)[0])


def giai_ho(kho, loc_ho):
    """v18: --ho nhận ĐÚNG một đường dẫn tương đối tới MỘT FILE trong kho.
    Từ file đó suy ra khóa (thư mục, họ). Không nhận thư mục, không nhận tên họ
    trơ: hai dạng đó từng làm phạm vi quét mơ hồ và cập nhật nhầm họ khác.
    Ném ValueError kèm câu nhắc cách dùng khi không giải được."""
    if loc_ho is None or not str(loc_ho).strip():
        raise ValueError("--ho cần đường dẫn tương đối tới MỘT file, ví dụ 01_A/BC_v01.docx")
    raw = str(loc_ho).replace("\\", "/").strip().strip("/")
    p = Path(loc_ho).expanduser()
    if not (p.is_absolute() and p.exists()):
        p = kho / raw
    if not p.exists():
        raise ValueError(f"--ho '{loc_ho}': không có file này trong kho")
    p = p.resolve()
    try:
        rel = str(p.relative_to(kho.resolve())).replace("\\", "/")
    except ValueError:
        raise ValueError(f"--ho '{loc_ho}': nằm ngoài gốc kho")
    if p.is_dir():
        raise ValueError(f"--ho '{loc_ho}': là THƯ MỤC; chỉ nhận đường dẫn tới một file")
    if not p.is_file():
        raise ValueError(f"--ho '{loc_ho}': không phải file thường")
    return khoa_ho_cua(rel)


def nap_cache(cache, bay_gio=None):
    """Đọc cache quan sát, đưa MỌI định dạng cũ về {rel: {"sha", "luc"}}.
    "luc" là thời điểm lần đầu quan sát thấy ĐÚNG nội dung đang có: mốc riêng
    từng file, không dùng chung một mốc toàn kho (v18). Trả (files, luc_kho).
    Cache chưa mang "v": 2 là bản sinh bởi đời cũ, chỉ có MỐC CHUNG toàn kho,
    tức bằng chứng ổn định của nó có thể sai. v19 nạp nội dung để so sha nhưng
    ĐÓNG DẤU LẠI mốc bằng bây giờ: lần chạy đầu sau nâng cấp coi như quan sát
    mới, chờ đủ khoảng ổn định rồi mới công nhận hiện hành."""
    import time
    bay_gio = time.time() if bay_gio is None else bay_gio
    try:
        goi = json.loads(cache.read_text(encoding="utf-8")) if cache.is_file() else {}
        if not isinstance(goi, dict):
            raise ValueError("cache không phải dict")
    except (ValueError, OSError) as e:
        print(f"        LƯU Ý: cache quan sát hỏng ({e}), coi như lần quét đầu, tự phục hồi")
        return {}, 0
    luc_kho = goi.get("luc", 0)
    if not isinstance(luc_kho, (int, float)):
        luc_kho = 0
    tho = goi.get("files")
    if not isinstance(tho, dict):
        tho = goi if goi and "luc" not in goi else {}
    doi_cu = goi.get("v") != 2  # bản sinh trước v19: chỉ có mốc chung toàn kho
    ra = {}
    for k, v in tho.items():
        if not isinstance(k, str):
            continue
        if isinstance(v, dict) and isinstance(v.get("sha"), str):
            l = v.get("luc")
            l = l if isinstance(l, (int, float)) else luc_kho
        elif isinstance(v, str):
            l = luc_kho
            v = {"sha": v}
        else:
            continue
        ra[k] = {"sha": v["sha"], "luc": bay_gio if doi_cu else l}
    if doi_cu and ra:
        print(f"        LƯU Ý: cache đời cũ (mốc chung toàn kho), đóng dấu lại thời"
              f" điểm này; chờ {KHOANG_ON_DINH // 60} phút nữa mới công nhận ổn định")
    return ra, luc_kho


def ghi_cache(cache, luc_kho, files):
    try:
        cache.write_text(json.dumps({"v": 2, "luc": luc_kho, "files": files},
                                    ensure_ascii=False, indent=0), encoding="utf-8")
    except OSError as e:
        # cache là máy sinh, mất thì lần sau coi như quét đầu; lỗi GHI (file bị
        # khóa, thư mục thiếu) không được giết báo cáo (hội đồng vòng 5)
        print(f"        LƯU Ý: không ghi được cache {cache.name} ({type(e).__name__}),"
              f" lần quét sau coi như quan sát mới")


def quet_ho(kho, truoc=None, bo_them=(), khoa_ho=None, bay_gio=None):
    """Quét kho, nhóm theo (thư mục tương đối, họ). Trả (nhom, trang_thai_moi).
    truoc: {rel: {"sha", "luc"}} lần quan sát trước (nhận cả {rel: sha} kiểu cũ).
    trang_thai_moi cùng dạng {rel: {"sha", "luc"}}; "luc" của file KHÔNG đổi nội
    dung được GIỮ NGUYÊN, nhờ vậy luật ổn định đếm đúng khoảng thời gian thật.
    khoa_ho: (thư mục, họ) từ giai_ho; chỉ duyệt ĐÚNG thư mục đó, không rglob cả
    kho, và chỉ nhận file cùng họ. bay_gio: tiêm thời gian giả cho fixture."""
    import time
    bay_gio = time.time() if bay_gio is None else bay_gio
    truoc = truoc or {}
    moi, nhom_items = {}, {}
    if khoa_ho:
        tm = khoa_ho[0]
        thu_muc = kho if tm in ("", ".") else kho / tm
        nguon = sorted(thu_muc.iterdir()) if thu_muc.is_dir() else []
    else:
        nguon = sorted(kho.rglob("*"))
    for f in nguon:
        if not f.is_file() or f.suffix.lower() in DUOI_BO or f.name.startswith("."):
            continue
        rel = str(f.relative_to(kho)).replace("\\", "/")
        # BỎ lọc tiền tố "9" (v10): 98_Assets và 99_Goc là vùng NGHIỆP VỤ phải
        # quét (X4 kiểm sha 99_Goc); chỉ loại đích danh kho lưu trữ 99_Archive
        if rel.startswith(("_", ".")) or "/_" in rel:
            continue
        if rel.split("/")[0] == "99_Archive":
            continue
        if rel.split("/")[0] in THU_MUC_HE_THONG:
            continue  # 00_Index là vùng luật và sổ, không phải tài liệu nghiệp vụ
        if any(rel == b or rel.startswith(b.rstrip("/") + "/") for b in bo_them):
            continue  # danh sách loại của công ty ở _so/_quan_sat_bo.txt
        if la_file_tam(f.name):
            khoa = (str(Path(rel).parent), "tam")
        else:
            khoa = khoa_ho_cua(rel)
        if khoa_ho and khoa != khoa_ho:
            continue  # cùng thư mục nhưng KHÁC họ: ngoài phạm vi --ho
        # file tạm (~$ đang bị Office khóa, .tmp...) đằng nào cũng bị loại khỏi
        # suy hiện hành: không hash, vừa nhanh vừa khỏi chết vì PermissionError
        sha = "" if khoa[1] == "tam" else sha_file(f)
        tr = truoc.get(rel) or {}
        if isinstance(tr, str):
            tr = {"sha": tr, "luc": 0}
        cu = tr.get("sha") == sha
        luc = tr.get("luc", 0) if cu else bay_gio
        if not isinstance(luc, (int, float)):
            luc = 0
        moi[rel] = {"sha": sha, "luc": luc}
        nhom_items.setdefault(khoa, []).append({
            "ten": f.name, "rel": rel, "sha": sha,
            "mtime": f.stat().st_mtime,
            # ổn định = cùng nội dung VÀ đã giữ nội dung đó đủ KHOANG_ON_DINH
            "on_dinh": cu and (bay_gio - luc) >= KHOANG_ON_DINH,
        })
    nhom = {k: dict(suy_hien_hanh(v), items=v) for k, v in nhom_items.items() if k[1] != "tam"}
    return nhom, moi


def bao_phu(dong_kho):
    r"""Từ các dòng TAILIEU trỏ Kho: tách (tập đường dẫn FILE, tập đường dẫn THƯ MỤC).
    Dòng trỏ thư mục nhận diện bằng dấu / hay \ ở cuối."""
    files, dirs = set(), set()
    for h in dong_kho:
        raw = h[5][4:].strip("` ")
        rel = raw.replace("\\", "/").strip()
        if rel.endswith("/"):
            dirs.add(rel.rstrip("/").lower())
        else:
            files.add(rel.strip("/").lower())
    return files, dirs


def da_vao_so(rel, files, dirs):
    """File được coi là ĐÃ BAO PHỦ khi trùng đường dẫn file trong sổ, hoặc nằm
    trong một thư mục mà sổ đã trỏ nguyên cả bộ hồ sơ."""
    r = rel.lower()
    return r in files or any(r.startswith(d + "/") for d in dirs)


def quan_sat_kho(goc, so, kho, loc_ho=None, bay_gio=None):
    """Đối chiếu TAILIEU với file thật. Chỉ báo cáo và đề xuất _INBOX.
    loc_ho: đường dẫn tương đối tới MỘT file; quét đúng họ của file đó. Cache
    khi ấy chỉ THAY phần thuộc đúng họ này (file đã xóa khỏi họ biến mất khỏi
    cache), các họ khác giữ nguyên. bay_gio: tiêm thời gian giả cho fixture."""
    import time
    bay_gio = time.time() if bay_gio is None else bay_gio
    cache = so / "_quan_sat_truoc.json"
    truoc, luc_kho = nap_cache(cache, bay_gio)
    khoa_ho = None
    if loc_ho is not None:
        try:
            khoa_ho = giai_ho(kho, loc_ho)
        except ValueError as e:
            bao("9-11. chế độ --ho giải được đúng một họ tài liệu", False, str(e))
            return
    pv = f" [họ {khoa_ho[0]}/{khoa_ho[1]}]" if khoa_ho else ""
    lan_dau = not any(khoa_ho_cua(k) == khoa_ho for k in truoc) if khoa_ho else not truoc
    bo_them = tuple(l.strip().replace("\\", "/") for l in
                    doc(so / "_quan_sat_bo.txt").splitlines() if l.strip())
    nhom, moi = quet_ho(kho, truoc, bo_them, khoa_ho, bay_gio)
    if khoa_ho:
        if not moi:
            bao("9-11. chế độ --ho giải được đúng một họ tài liệu", False,
                f"không file nào thuộc họ '{khoa_ho[1]}' trong '{khoa_ho[0]}'")
            return
        # THAY đúng họ đang quét: bỏ mọi mục cũ của họ này rồi thêm tập hiện tại
        gop = {k: v for k, v in truoc.items() if khoa_ho_cua(k) != khoa_ho}
        gop.update(moi)
        ghi_cache(cache, luc_kho, gop)
        print(f"        chế độ --ho{pv}: {len(moi)} file cùng họ, cache thay đúng họ này")
    else:
        ghi_cache(cache, bay_gio, moi)

    hang = dong_bang(doc(so / "TAILIEU.md"))
    dong_kho_all = [h for h in hang if len(h) > 5 and h[5].startswith("Kho ")]
    # v19: phạm vi ĐÃ VÀO SỔ luôn tính trên TOÀN BỘ TAILIEU, kể cả ở chế độ --ho.
    # Một dòng trỏ THƯ MỤC bao phủ mọi file con; lọc theo họ trước khi tính bao
    # phủ làm dòng "Kho 01_A/" biến mất và đề xuất _INBOX oan cho file đã vào sổ.
    so_files, so_dirs = bao_phu(dong_kho_all)
    dong_kho = dong_kho_all
    if khoa_ho:  # chỉ phần kiểm file mất, sha và bất biến mới thu về đúng họ
        dong_kho = [h for h in dong_kho_all
                    if khoa_ho_cua(h[5][4:].strip("` ").replace("\\", "/").strip("/")) == khoa_ho]

    mat, sua_bat_bien, lech_sha, khong_kiem = [], [], [], []
    for h in dong_kho:
        rel = h[5][4:].strip("` ").replace("\\", "/").strip("/")
        duong = kho / rel
        if not duong.exists():
            mat.append((h[1], rel))
            continue
        sha_so = next((o for o in h if re.fullmatch(r"[0-9a-f]{12,64}", o)), None)
        if sha_so and duong.is_file():
            sha_that = (moi.get(rel) or {}).get("sha") or sha_file(duong)
            if not sha_that:
                # file bị khóa hay không đọc được (đã vào LOI_DOC): CHƯA KIỂM
                # ĐƯỢC, không phải "bị sửa" - hết cáo buộc oan bản ĐÃ KÝ đang mở
                khong_kiem.append((h[1], rel))
            elif not sha_that.startswith(sha_so[:12]):
                (sua_bat_bien if any(t in h for t in BAT_BIEN) else lech_sha).append(h[1])
    bao("9. file khai 'Kho' trong TAILIEU đều còn trên kho" + pv, not mat, str(mat[:5]))
    bao("10a. bản ẢNH CHỤP và mốc chính thức (từ ĐÃ GỬI DUYỆT trở đi) không bị sửa"
        " tại chỗ" + pv, not sua_bat_bien, str(sua_bat_bien))
    bao("10b. sha256 file thường khớp sổ" + pv, not lech_sha, str(lech_sha[:5]))
    if khong_kiem:
        bao("10c. sha kiểm được (file không bị khóa)" + pv, False,
            f"{khong_kiem[:5]}: file đang bị khóa hay không đọc được, CHƯA KIỂM"
            f" ĐƯỢC sha, KHÔNG kết luận bị sửa; đóng ứng dụng đang giữ rồi rà lại")

    xung_dot, de_xuat, cho_on_dinh = [], [], 0
    for (tm, ho), kq in sorted(nhom.items()):
        if kq["xung_dot"]:
            xung_dot.append((tm, kq["xung_dot"]))
        cho_on_dinh += len(kq["khong_xac_dinh"])
        for it in kq["items"]:
            if it["ten"] in kq["hien_hanh"] and not da_vao_so(it["rel"], so_files, so_dirs):
                de_xuat.append(it["rel"])
    bao("11. không họ tài liệu nào cùng vN mà khác nội dung (XUNG ĐỘT)" + pv, not xung_dot,
        str(xung_dot[:3]))
    if lan_dau:
        print(f"        LƯU Ý: lần quét ĐẦU của phạm vi này, chưa file nào đạt luật ổn"
              f" định; chạy lại sau tối thiểu {KHOANG_ON_DINH // 60} phút để nhận bản hiện hành")
    elif cho_on_dinh:
        print(f"        {cho_on_dinh} file mới đổi hay chưa giữ nguyên nội dung đủ"
              f" {KHOANG_ON_DINH // 60} phút, chờ lần quét sau")
    if de_xuat:
        print("        ĐỀ XUẤT _INBOX (bản hiện hành quan sát được, chưa vào sổ, ghi mức A):")
        for d in de_xuat[:15]:
            print(f"          - {d}")


SU_KIEN_HOP_LE = ("PREPARED", "COMMITTED")
SO_HOP_LE = ("THU", "VIEC", "DUKIEN", "TAILIEU", "QUYETDINH")


def kiem_payload(p, khoa=""):
    """Trả list lỗi schema của payload PREPARED. Rỗng nghĩa là payload đạt.
    Kiểm DỮ LIỆU chứ không chỉ tên trường: staging chuẩn hóa bằng normpath
    phải còn nằm BÊN TRONG _so/_thu_staging và thư mục phải tên sha256(khóa);
    metadata nguồn (conv_id, nguoi_gui, thoi_diem, tieu_de) và eml_sha256 bắt
    buộc; mỗi thao tác đủ operation_id (chuỗi, duy nhất trong mail), sổ đích
    hợp lệ, mã dòng, nội dung dòng; tên đính kèm là basename thuần kèm đủ
    sha256 và bytes."""
    if not isinstance(p, dict):
        return ["payload không phải object"]
    import posixpath
    loi = []
    for tr in ("conv_id", "nguoi_gui", "thoi_diem", "tieu_de", "eml_sha256"):
        if not isinstance(p.get(tr), str) or not p.get(tr).strip():
            loi.append(f"thiếu metadata nguồn {tr}")
    st = p.get("staging")
    if not isinstance(st, str) or not st.strip():
        loi.append("thiếu staging")
    else:
        s = posixpath.normpath(st.replace("\\", "/").strip())
        phan = s.split("/")
        if (st.replace("\\", "/").startswith("/") or re.match(r"^[A-Za-z]:", st)
                or ".." in phan or phan[:2] != ["_so", "_thu_staging"] or len(phan) < 3):
            loi.append("staging sau chuẩn hóa phải nằm bên trong _so/_thu_staging")
        elif khoa and phan[2] != hashlib.sha256(khoa.encode("utf-8")).hexdigest():
            loi.append("thư mục staging phải tên sha256(khóa), mỗi mail một thư mục")
    tt = p.get("thao_tac")
    if not isinstance(tt, list) or not tt:
        loi.append("thiếu danh sách thao_tac")
    else:
        ops = []
        for t in tt:
            if not isinstance(t, dict):
                loi.append(f"thao tác {t!r} không phải object")
                continue
            op = t.get("operation_id")
            if not isinstance(op, str) or not op:
                loi.append("thao tác thiếu operation_id")
            else:
                ops.append(op)
            if t.get("so") not in SO_HOP_LE:
                loi.append(f"sổ đích {t.get('so')!r} không hợp lệ")
            if not isinstance(t.get("dong"), str) or not t.get("dong"):
                loi.append("thao tác thiếu mã dòng")
            if not isinstance(t.get("noi_dung"), str) or not t.get("noi_dung"):
                loi.append("thao tác thiếu nội dung dòng")
        if len(ops) != len(set(ops)):
            loi.append("operation_id trùng trong một mail")
    dk = p.get("dinh_kem", [])
    if not isinstance(dk, list):
        loi.append("dinh_kem phải là danh sách")
    else:
        for d in dk:
            if not isinstance(d, dict) or not isinstance(d.get("ten"), str):
                loi.append("đính kèm thiếu ten")
            elif ("/" in d["ten"] or "\\" in d["ten"] or d["ten"] in (".", "..")
                  or not d["ten"].strip()):
                # basename áp cho MỌI đính kèm, kể cả de_ngoai: tên vẫn vào sổ
                loi.append(f"tên đính kèm {d['ten']!r} phải là basename thuần,"
                           f" không được mang đường dẫn")
            elif d.get("de_ngoai"):
                # vượt @NHIP.TRANDINHKEM hay dữ liệu nhạy: để ngoài staging theo
                # X3E mục 2, chỉ đòi lý do; sha256/bytes miễn vì file không kéo về
                if not (isinstance(d.get("ly_do"), str) and d["ly_do"].strip()):
                    loi.append(f"đính kèm de_ngoai {d['ten']!r} thiếu ly_do")
            elif (not isinstance(d.get("sha256"), str)
                    or not isinstance(d.get("bytes"), int)):
                loi.append("đính kèm thiếu ten, sha256 hay bytes")
    return loi


def doc_nhat_ky(nd):
    """Parse nhật ký sự kiện MỘT lượt, theo TỪNG KHÓA, không dòng nào gây crash.
    Trả (luot, hong):
      luot: dict khóa (chuỗi) sang {"seq": [ev theo thứ tự file],
            "payload": dict PREPARED cuối, "payload_loi": list lỗi schema,
            "payload_ok": bool, "hop_thu": set chuẩn hóa}
      hong: list (số dòng, lý do) cho dòng sai schema: không phải JSON object,
            trường khóa duy nhất là "khoa" ("msgId" kiểu cũ phải migration
            riêng, gặp là dòng hỏng), khóa không phải CHUỖI, "ev" ngoài
            PREPARED/COMMITTED (kể cả thiếu hay gõ sai), thiếu "hop_thu"."""
    luot, hong = {}, []
    for i, l in enumerate(nd.splitlines(), 1):
        l = l.strip()
        if not l:
            continue
        try:
            r = json.loads(l)
        except ValueError:
            hong.append((i, "không phải JSON"))
            continue
        if not isinstance(r, dict):
            hong.append((i, "không phải object"))
            continue
        if "msgId" in r:
            hong.append((i, "dùng trường msgId kiểu cũ, phải migration sang khoa"))
            continue
        khoa = r.get("khoa")
        if not isinstance(khoa, str) or not khoa.strip():
            hong.append((i, "khóa thiếu hoặc không phải chuỗi"))
            continue
        ev = r.get("ev")
        if ev not in SU_KIEN_HOP_LE:
            hong.append((i, f"ev {ev!r} ngoài PREPARED/COMMITTED"))
            continue
        hop = r.get("hop_thu")
        if not isinstance(hop, str) or not hop.strip():
            hong.append((i, "thiếu hop_thu"))
            continue
        m = luot.setdefault(khoa, {"seq": [], "payload": None,
                                   "payload_loi": ["chưa có PREPARED"],
                                   "payload_ok": False, "hop_thu": set()})
        m["seq"].append(ev)
        m["hop_thu"].add(hop.strip().lower())
        if ev == "PREPARED":
            m["payload"] = r.get("payload")
            m["payload_loi"] = kiem_payload(m["payload"], khoa)
            m["payload_ok"] = not m["payload_loi"]
    return luot, hong


def doc_index(nd):
    """Đọc index _thu_ap_dung. Trả (dict, ok). ok=False khi không phải object
    của các mục {"so": chuỗi, "dong": chuỗi}."""
    try:
        raw = json.loads(nd or "{}")
    except ValueError:
        return {}, False
    if not isinstance(raw, dict):
        return {}, False
    ok = all(isinstance(k, str) and isinstance(v, dict)
             and isinstance(v.get("so"), str) and isinstance(v.get("dong"), str)
             for k, v in raw.items())
    return raw, ok


def khoa_committed(luot):
    """Tập khóa có sự kiện COMMITTED (nguồn duy nhất để dựng registry)."""
    return {k for k, m in luot.items() if "COMMITTED" in m["seq"]}


def dung_lai_registry(nd):
    """Registry dựng lại CHỈ từ sự kiện COMMITTED. Trả (tập khóa, số dòng hỏng)."""
    luot, hong = doc_nhat_ky(nd)
    return khoa_committed(luot), len(hong)


def doc_registry(nd):
    """Đọc registry. Trả (tập khóa chuỗi, ok). ok=False khi không phải DANH SÁCH
    CHUỖI: JSON hỏng, object {}, danh sách chứa phần tử không phải chuỗi."""
    try:
        raw = json.loads(nd or "[]")
    except ValueError:
        return set(), False
    if not isinstance(raw, list):
        return set(), False
    ok = all(isinstance(x, str) for x in raw)
    return {x for x in raw if isinstance(x, str)}, ok


def hop_thu_cua(luot):
    """Tập hop_thu chuẩn hóa xuất hiện ở các sự kiện hợp lệ."""
    ket = set()
    for m in luot.values():
        ket |= m["hop_thu"]
    return ket


def cot_thu(nd, ten_cot):
    """Giá trị một cột của bảng THU theo TÊN cột trong header, không đoán vị trí."""
    lines = nd.splitlines()
    for i, d in enumerate(lines[:-1]):
        if d.startswith("|") and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
            header = [o.strip() for o in d.strip("|").split("|")]
            if ten_cot in header:
                idx = header.index(ten_cot)
                return [r[idx] for r in dong_bang(nd)
                        if len(r) == len(header) and r[idx].strip()]
    return []


def kiem_email(goc, so):
    """Phép 12. Trả list (tên, ok, chi tiết) để fixture gọi được cả hàm;
    đồng thời báo qua bao() khi chạy thật."""
    ket = []
    nk_p = so / "_thu_nhat_ky.ndjson"
    reg_p = so / "_thu_da_nap.json"
    thu_nd = doc(so / "THU.md")
    co_du_lieu_thu = bool(dong_bang(thu_nd))
    if not nk_p.is_file() and not reg_p.is_file() and not co_du_lieu_thu:
        print("  BỎ QUA  12. profile EMAIL chưa chạy (chưa có nhật ký, registry hay dòng THU)")
        return ket

    # 12a. đã chạy EMAIL thì nhật ký VÀ registry phải cùng tồn tại
    ket.append(("12a. nhật ký nạp và registry cùng tồn tại",
                nk_p.is_file() and reg_p.is_file(),
                f"nhật ký={'có' if nk_p.is_file() else 'MẤT'},"
                f" registry={'có' if reg_p.is_file() else 'MẤT'};"
                f" mất nhật ký: GIỮ NGUYÊN registry làm rào chống nạp trùng, CẤM dựng lại từ tập COMMITTED rỗng (X5 mục 4); mất registry thì dựng lại từ COMMITTED"))

    luot, hong = doc_nhat_ky(doc(nk_p))
    committed = khoa_committed(luot)
    ket.append(("12b. nhật ký không có dòng hỏng", not hong,
                f"dòng sai schema tại {hong[:5]}, parse một lượt, không crash"))

    # 12g. mô hình sự kiện TỪNG KHÓA: đúng chuỗi PREPARED rồi (tùy) COMMITTED;
    #      COMMITTED mồ côi, COMMITTED đứng trước, sự kiện lặp đều là hỏng
    sai_mo_hinh = sorted(k for k, m in luot.items()
                         if m["seq"] not in (["PREPARED"], ["PREPARED", "COMMITTED"]))
    ket.append(("12g. mỗi khóa đúng mô hình PREPARED rồi COMMITTED, không mồ côi,"
                " không lặp, không ngược thứ tự",
                not sai_mo_hinh,
                f"{sai_mo_hinh[:3]}: chuỗi sự kiện {[luot[k]['seq'] for k in sai_mo_hinh[:3]]}"))

    # 12h. mọi PREPARED phải mang payload phục hồi ĐẠT SCHEMA DỮ LIỆU (staging
    #      trong _so/_thu_staging, thao tác đủ trường và operation_id duy nhất,
    #      đính kèm khai sha256 và byte), kể cả khi lượt đã COMMITTED
    thieu_payload = sorted(k for k, m in luot.items()
                           if "PREPARED" in m["seq"] and not m["payload_ok"])
    ket.append(("12h. mọi PREPARED mang payload phục hồi đạt schema",
                not thieu_payload,
                "; ".join(f"{k}: {luot[k]['payload_loi'][:2]}" for k in thieu_payload[:3])
                + "; không phục hồi được nếu không đọc lại hộp thư"))

    ket.append(("12c. không lượt nạp nào DỞ DANG (PREPARED thiếu COMMITTED)",
                not (set(luot) - committed),
                f"{sorted(set(luot) - committed)[:3]}: chạy lại bước 2 từ payload"
                f" và staging, cấm đọc lại hộp thư"))

    reg, reg_ok = doc_registry(doc(reg_p))
    chi_tiet_12d = ((f"dạng sai (phải là danh sách chuỗi khóa); " if not reg_ok else "")
                    + f"thiếu {sorted(committed - reg)[:3]}, thừa {sorted(reg - committed)[:3]};"
                    + (" nhật ký MẤT hay RỖNG: xem 12a, GIỮ NGUYÊN registry làm rào"
                       " chống nạp trùng, KHÔNG phải chặn oan, cấm xóa"
                       if not luot and reg
                       else " thừa nghĩa là registry chặn mail chưa từng nạp"))
    ket.append(("12d. registry là DANH SÁCH CHUỖI và BẰNG ĐÚNG tập khóa COMMITTED",
                reg_ok and reg == committed, chi_tiet_12d))

    # 12e. hộp thư so CHÍNH XÁC sau chuẩn hóa, không substring. EMAIL đã chạy
    #      mà X0 chưa khai @NHIP.HOPTHU là LỆCH cấu hình, không phải BỎ QUA
    x0nd = "".join(doc(q) for q in sorted(goc.glob("X0_CAUHINH_*.md"))
                   if "TEMPLATE" not in q.name and "conflicted" not in q.name.lower()
                   and "xung đột" not in q.name.lower())
    hop_khai_tap = set()
    for m_h in re.finditer(r"@NHIP\.HOPTHU(?:_CU)?(?:\s*\(EMAIL\))?[^\n]*", x0nd):
        # nhận cả dạng hiển thị "Văn phòng <vp@cty.vn>" và danh sách hộp CŨ
        # sau đổi domain (@NHIP.HOPTHU_CU): nhật ký lịch sử không bị đá oan
        hop_khai_tap |= {e.lower() for e in
                         re.findall(r"[\w.+-]+@[\w.-]+", m_h.group(0))}
    if hop_khai_tap:
        sai_hop = sorted(h for h in hop_thu_cua(luot) if h not in hop_khai_tap)
        ket.append(("12e. mọi mail trong nhật ký thuộc ĐÚNG hộp thư khai báo",
                    not sai_hop,
                    f"hộp lạ {sai_hop[:3]} so với {sorted(hop_khai_tap)}"))
    else:
        ket.append(("12e. mọi mail trong nhật ký thuộc ĐÚNG hộp thư khai báo",
                    False, "EMAIL đã chạy mà X0 CHƯA khai @NHIP.HOPTHU,"
                    " không có chuẩn nào để so, khai ngay"))

    # 12f. khóa cuối (Message-ID hay fallback, không lọc bằng dấu @) không đứng
    #      ở hai luồng THU
    khoa_cuoi = cot_thu(thu_nd, "Message-ID cuối")
    trung = sorted({k for k in khoa_cuoi if khoa_cuoi.count(k) > 1})
    ket.append(("12f. không khóa nào đứng cuối ở HAI luồng THU", not trung, str(trung[:3])))

    # 12i. một Conversation-ID chỉ được nằm ở MỘT dòng THU
    conv = cot_thu(thu_nd, "Conversation-ID")
    conv_trung = sorted({c for c in conv if conv.count(c) > 1})
    ket.append(("12i. Conversation-ID duy nhất trong THU", not conv_trung,
                f"{conv_trung[:3]}: một luồng bị tách hai dòng, gộp lại"))

    # 12j. staging THẬT trên đĩa, hiểu vòng đời dọn: PREPARED chưa COMMITTED
    #      thì staging bắt buộc còn; COMMITTED đã dọn thì phải có mục manifest
    #      dọn hợp lệ; staging còn thì .eml hay body KHÔNG rỗng, đúng
    #      eml_sha256, đường dẫn resolve() vẫn nằm trong _thu_staging (chặn
    #      symlink), từng đính kèm đúng sha256 và byte
    goc_staging = (so / "_thu_staging").resolve()
    try:
        don = json.loads(doc(so / "_thu_don_staging.json") or "{}")
        if not isinstance(don, dict):
            don = {}
    except ValueError:
        don = {}
    loi_staging = []
    for k, m2 in sorted(luot.items()):
        if "PREPARED" not in m2["seq"] or not m2["payload_ok"]:
            continue  # payload hỏng đã lệch ở 12h, không kiểm chồng
        p = m2["payload"]
        d = (goc / p["staging"].replace("\\", "/").strip()).resolve()
        if d != goc_staging and goc_staging not in d.parents:
            loi_staging.append(f"{k}: staging resolve ra ngoài _thu_staging (symlink?)")
            continue
        if not d.is_dir():
            mv = don.get(k)
            hop_le = (isinstance(mv, dict)
                      and all(isinstance(mv.get(t), str) and mv.get(t)
                              for t in ("purged_at", "eml_final_path", "sha256"))
                      and isinstance(mv.get("attachment_final_paths"), list))
            if k in committed and hop_le:
                continue  # đã dọn đúng luật, có dấu vết
            loi_staging.append(
                f"{k}: staging vắng mà " +
                ("chưa COMMITTED" if k not in committed else "không có manifest dọn hợp lệ"))
            continue
        eml = [f for f in d.iterdir() if f.is_file()
               and (f.suffix.lower() == ".eml" or f.stem.lower() in ("body", "than_thu"))]
        if not eml:
            loi_staging.append(f"{k}: staging thiếu .eml hay body")
        elif all(f.stat().st_size == 0 for f in eml):
            loi_staging.append(f"{k}: .eml hay body RỖNG, không phục hồi được")
        elif not any(sha_file(f) == p["eml_sha256"] for f in eml):
            loi_staging.append(f"{k}: không file .eml hay body nào khớp eml_sha256")
        for dk in p.get("dinh_kem", []):
            if dk.get("de_ngoai"):
                continue  # vượt @NHIP.TRANDINHKEM, để ngoài staging theo X3E mục 2
            f = (d / dk["ten"]).resolve()
            if f != goc_staging and goc_staging not in f.parents:
                loi_staging.append(f"{k}: đính kèm {dk['ten']} trỏ ra ngoài staging")
            elif not f.is_file():
                loi_staging.append(f"{k}: thiếu đính kèm {dk['ten']}")
            elif f.stat().st_size != dk["bytes"] or sha_file(f) != dk["sha256"]:
                loi_staging.append(f"{k}: đính kèm {dk['ten']} sai sha256 hay byte")
    # 12j2. staging MỒ CÔI: thư mục không có khóa nào trong nhật ký (crash giữa
    #       lưu staging và append PREPARED, X3E mục 2); báo, người duyệt mới xóa.
    if goc_staging.is_dir():
        # khóa lấy từ CẢ nhật ký lẫn registry: nhật ký mất hay rỗng thì staging
        # của mail đã nạp không bị gọi mồ côi oan rồi bị xúi xóa
        reg_mc, _ = doc_registry(doc(reg_p))
        co_khoa = {hashlib.sha256(k.encode("utf-8")).hexdigest()
                   for k in set(luot) | set(reg_mc)}
        mo_coi = sorted(d.name for d in goc_staging.iterdir()
                        if d.is_dir() and d.name not in co_khoa)
        if mo_coi:
            loi_staging.append(
                f"{len(mo_coi)} thư mục staging mồ côi ({mo_coi[0][:12]}...): không khóa"
                f" nào trong nhật ký, trình người dùng duyệt rồi mới xóa (mức B)")
    ket.append(("12j. staging đúng vòng đời: còn thì đúng nội dung, vắng thì có manifest dọn",
                not loi_staging, "; ".join(loi_staging[:3])))

    # 12k. tập mục index BẰNG ĐÚNG tập "khoa|operation_id" của các mail đã
    #      COMMITTED (thừa hay thiếu đều lệch); sổ và mã dòng phải khớp payload
    idx_p = so / "_thu_ap_dung.json"
    idx, idx_ok = doc_index(doc(idx_p))
    loi_idx = []
    if not luot and reg:
        # nhật ký MẤT hay RỖNG (12a/12d đã lệch): index và registry là thứ CÒN
        # ĐÚNG, thứ mất là nhật ký; không liệt kê "thừa mục" kẻo xúi dọn nhầm
        loi_idx.append("nhật ký MẤT hay RỖNG: GIỮ NGUYÊN _thu_ap_dung.json và"
                       " registry, thứ phải khôi phục là nhật ký (xem 12a)")
        idx = {}
    elif not idx_ok:
        loi_idx.append("index không phải object của các mục {so, dong}")
    thao_tac_cua = {}
    for k in sorted(committed):
        if luot[k]["payload_ok"]:
            for t in luot[k]["payload"]["thao_tac"]:
                thao_tac_cua[f"{k}|{t['operation_id']}"] = t
    for kk in sorted(set(thao_tac_cua) - set(idx)):
        loi_idx.append(f"{kk}: COMMITTED nhưng vắng trong index")
    for kk in sorted(set(idx) - set(thao_tac_cua)):
        goc_k = kk.split("|", 1)[0]
        loi_idx.append(f"{kk}: index thừa mục " +
                       ("(mail không có trong nhật ký)" if goc_k not in luot
                        else "(không có trong thao tác payload)"))
    if idx_ok:
        for kk in sorted(set(idx) & set(thao_tac_cua)):
            t = thao_tac_cua[kk]
            if idx[kk]["so"] != t["so"] or idx[kk]["dong"] != t["dong"]:
                loi_idx.append(f"{kk}: index trỏ {idx[kk]['so']}/{idx[kk]['dong']}"
                               f" khác payload {t['so']}/{t['dong']}")
    ket.append(("12k. tập mục index bằng đúng tập thao tác COMMITTED và khớp payload",
                not loi_idx, "; ".join(loi_idx[:3])))

    # 12l. index trỏ tới mã dòng CÓ THẬT trong sổ đích, so ĐÚNG Ô của bảng
    #      (V-1 không được ăn theo V-10), có hash nội dung thì đối chiếu thêm
    loi_dong = []
    if idx_ok:
        o_cua = {}
        for kk, v in sorted(idx.items()):
            so_p = so / f"{v['so']}.md"
            if v["so"] not in SO_HOP_LE:
                loi_dong.append(f"{kk}: sổ đích {v['so']!r} không hợp lệ")
                continue
            if not so_p.is_file():
                loi_dong.append(f"{kk}: sổ {v['so']} không tồn tại")
                continue
            if v["so"] not in o_cua:
                o_cua[v["so"]] = dong_bang(doc(so_p))
            hang = [r for r in o_cua[v["so"]] if v["dong"] in [o.strip() for o in r]]
            if not hang:
                loi_dong.append(f"{kk}: mã dòng {v['dong']} không là Ô nào trong {v['so']}")
            elif isinstance(v.get("hash"), str) and v["hash"] and not any(
                    hashlib.sha256(("|".join(r)).encode("utf-8")).hexdigest() == v["hash"]
                    for r in hang):
                loi_dong.append(f"{kk}: hash nội dung dòng không khớp")
    ket.append(("12l. index trỏ tới mã dòng có thật trong sổ đích (so đúng ô)",
                not loi_dong, "; ".join(loi_dong[:3])))

    for ten, ok, chi_tiet in ket:
        bao(ten, ok, chi_tiet)
    return ket


def main(goc):
    goc = Path(goc)
    so = goc / "_so"

    # Tự vệ tham số (hội đồng vòng 5): truyền nhầm GỐC KHO thay vì 00_Index thì
    # dừng sớm kèm gợi ý, không phun "khôi phục mức C" oan trên hệ khỏe mạnh.
    if (not so.is_dir() and not list(goc.glob("X0_CAUHINH_*.md"))
            and (goc / "00_Index" / "_so").is_dir()):
        print(f"Thư mục truyền vào không có _so hay X0, nhưng CHỨA 00_Index hợp lệ."
              f" Có phải bạn định chạy: python kiem_van_hanh.py {goc / '00_Index'} ?")
        sys.exit(2)

    # 0. Sổ lõi phải TỒN TẠI trên đĩa: doc() nuốt file vắng thành chuỗi rỗng nên
    #    thiếu phép này thì xóa nhầm cả một sổ vẫn PASS im lặng (hội đồng v21).
    SO_LOI = ["VIEC.md", "DUKIEN.md", "TAILIEU.md", "QUYETDINH.md",
              "PLANNING.md", "BANG_DIEU_KHIEN.md", "X0_INDEX.md"]
    vang = [t for t in SO_LOI if not (so / t).is_file()]
    bao("0. sổ lõi và view tồn tại trên đĩa", not vang,
        f"vắng {vang}: SỔ mất thì khôi phục là mức C (version history kho mây,"
        f" NHATKY làm trục sự thật, cấm gõ lại từ trí nhớ); riêng hai VIEW"
        f" BANG_DIEU_KHIEN, X0_INDEX chỉ cần sinh lại, mức A")

    # 0b. Conflicted copy của file sổ do đồng bộ mây: chứa lượt ghi bị kẹt,
    #     phải hòa giải theo X5 mục 3 rồi chuyển _lich_su, không được để im.
    xung = sorted(f.name for vung in (so.glob("*"), goc.glob("*.md"))
                  for f in vung
                  if f.is_file() and ("conflicted" in f.name.lower()
                                      or "xung đột" in f.name.lower()
                                      or la_file_tam(f.name)))
    # hậu tố LẠ trên tên sổ chuẩn (khuôn OneDrive -<TênMáy>...): cũng là bản sao
    xung += sorted(f.name for f in so.glob("NHATKY_*.md")
                   if f.name not in {x.split("/")[-1] for x in xung}
                   and "TEMPLATE" not in f.name
                   and not re.fullmatch(r"NHATKY_\d{4}Q[1-4]\.md", f.name))
    xung += sorted(f.name for f in goc.glob("X0_CAUHINH_*.md")
                   if "TEMPLATE" not in f.name
                   and not re.fullmatch(r"X0_CAUHINH_[A-Z0-9]{3,4}\.md", f.name))
    xung = sorted(set(xung))
    bao("0b. không bản conflicted copy của sổ trong _so hay bộ X ở 00_Index", not xung,
        f"{xung[:3]}: dòng vắng ở bản chính chép sang rồi hòa giải mã"
        f" (X5 mục 3 bước 2), bản conflict chuyển _so/_lich_su")

    x0s = loc_ban_chinh(goc.glob("X0_CAUHINH_*.md"), r"X0_CAUHINH_[A-Z0-9]{3,4}\.md")
    co_template = any("TEMPLATE" in q.name for q in goc.glob("X0_CAUHINH_*.md"))
    if not x0s and co_template:
        print("  BỎ QUA  0c: chỉ thấy X0_CAUHINH_TEMPLATE, hệ chưa cài đặt;"
              " chạy \"cài đặt\" theo X9 trước")
    elif not x0s:
        ung_vien_tho = [q.name for q in goc.glob("X0_CAUHINH_*.md")
                        if "TEMPLATE" not in q.name]
        if ung_vien_tho:
            bao("0c. có bản X0 đang chạy", False,
                f"thấy {ung_vien_tho[:3]} nhưng tên KHÔNG đúng chuẩn"
                f" X0_CAUHINH_<MÃ 3-4 ký tự A-Z 0-9, không dấu>.md:"
                f" đổi tên file (mức B), không phải mất cấu hình")
        else:
            bao("0c. có bản X0 đang chạy", False,
                "không thấy X0_CAUHINH nào: mất file cấu hình, khôi phục mức C")
    else:
        bao("0c. đúng MỘT bản X0 đang chạy (không tính _TEMPLATE, conflicted)",
            len(x0s) == 1, f"thấy {[q.name for q in x0s]}: nhiều ứng viên thì hệ"
            f" không tự chọn, gộp về một bản rồi rà lại")
    instrs = sorted(goc.glob("INSTRUCTION_WORKOPS_v*.md"))
    yc = re.search(r"instruction_yeu_cau:\s*(v\d+)", doc(x0s[0])) if x0s else None
    iv = re.search(r"INSTRUCTION · WORKOPS · (v\d+)", doc(instrs[0])) if instrs else None
    if not x0s and co_template:
        print("  BỎ QUA  1: chưa cài đặt, chưa có X0 để so instruction_yeu_cau")
    else:
        bao("1. instruction_yeu_cau khớp bản INSTRUCTION",
            bool(yc and iv and yc.group(1) == iv.group(1)),
            f"X0={yc and yc.group(1)} INSTR={iv and iv.group(1)}")

    LOI_DOC.clear()
    rev = re.search(r"rev (\d+)", doc(x0s[0])) if x0s else None
    chua_cai = bool(rev and rev.group(1) == "0") or (not x0s and co_template)
    if chua_cai:
        print("  BỎ QUA  2, 3, 4, 8: X0 rev 0, hệ chưa cài đặt, chưa có lượt ghi nào")
    else:
        co_nk = loc_ban_chinh(so.glob("NHATKY_*.md"), r"NHATKY_\d{4}Q[1-4]\.md")
        chi_conflict = (not co_nk and any(
            "TEMPLATE" not in q.name for q in so.glob("NHATKY_*.md")))
        bao("0d. NHATKY tồn tại khi hệ đã cài (rev >= 1)", bool(co_nk),
            ("chỉ còn bản conflicted/xung đột, BẢN CHÍNH đã mất: khôi phục bản"
             " chính mức C từ version history TRƯỚC, rồi mới hòa giải theo 0b"
             if chi_conflict else
             "trục sự thật để cấp mã, hòa giải trùng và chốt sổ đã biến mất:"
             " khôi phục mức C từ version history, cấm cấp mã G mới khi chưa có lại"))
    if ((so / "_thu_nhat_ky.ndjson").is_file() or (so / "_thu_da_nap.json").is_file())             and not (so / "THU.md").is_file():
        bao("0e. THU.md tồn tại khi pipeline EMAIL có dấu vết", False,
            "nhật ký hay registry còn mà sổ THU vắng: khôi phục mức C")

    bdk_nd = doc(so / "BANG_DIEU_KHIEN.md")
    if bdk_nd:
        bao("1b. BANG_DIEU_KHIEN trong trần runtime 4.200 ký tự",
            len(bdk_nd) <= 4200,
            f"{len(bdk_nd)} ký tự: bảng phình làm thuế mở phiên tăng ngầm, dọn bớt"
            f" khối cũ hay chuyển chi tiết xuống sổ")
    idx_rt = doc(so / "X0_INDEX.md")
    if idx_rt:
        bao("1c. X0_INDEX trong trần runtime 2.400 ký tự",
            len(idx_rt) <= 2400,
            f"{len(idx_rt)} ký tự: view phình thì thuế mở phiên tăng ngầm,"
            f" rút gọn về đúng rev, kho, profile, dự án, vị trí mục")

    idx = doc(so / "X0_INDEX.md")
    if not chua_cai:
        if idx:
            rev_idx = re.search(r"x0_rev:\s*(\d+)", idx)
            bao("2. X0_INDEX đúng rev X0",
                bool(rev and rev_idx and rev.group(1) == rev_idx.group(1)),
                f"X0 rev={rev and rev.group(1)} index={rev_idx and rev_idx.group(1)}")
        else:
            print("  BỎ QUA  2. chưa có X0_INDEX")

    nk = "".join(doc(p) for p in loc_ban_chinh(so.glob("NHATKY_*.md"),
                                               r"NHATKY_\d{4}Q[1-4]\.md"))
    hang_nk = dong_bang(nk)
    ma_cot_dau = [re.sub(r"\*", "", h[0]).strip() for h in hang_nk if h]
    ma_g = [m for m in ma_cot_dau if re.fullmatch(MAU_G, m)]
    wm = watermark(ma_g)

    if not chua_cai:
        treo = [h[0] for h in hang_nk if any(o == "ĐANG GHI" for o in h)]
        bao("3a. không dòng NHATKY còn ĐANG GHI", not treo, str(treo))
        trung = sorted({m for m in ma_g if ma_g.count(m) > 1})
        bao("3b. không mã G trùng ở cột Mã ghi", not trung, str(trung))
        cu = [m for m in ma_g if cua_cua(m) is None]
        if cu:
            print(f"        LƯU Ý: {len(cu)} mã G định dạng cũ (không cửa), không tính"
                  f" watermark, cân nhắc di trú: {cu[-3:]}")
        if wm:
            print("        watermark từng cửa: " + " · ".join(f"{c}={m}" for c, m in sorted(wm.items())))

        # 3c (X4 dòng 19 nửa sau): lượt XONG phải để dấu mã G ở ít nhất một sổ,
        # trừ khi cột Chạm sổ nào ghi "không"
        ghi_lan = set()
        for t in ["VIEC.md", "DUKIEN.md", "TAILIEU.md", "QUYETDINH.md", "PLANNING.md"]:
            for r in dong_bang(doc(so / t)):
                if r:
                    ghi_lan |= set(re.findall(MAU_G, r[-1]))
        khong_dau = [h[0].strip("* ") for h in hang_nk
                     if any(o == "XONG" for o in h)
                     and re.fullmatch(MAU_G, h[0].strip("* "))
                     and "không" not in (h[5] if len(h) > 5 else "").lower()
                     and h[0].strip("* ") not in ghi_lan]
        bao("3c. lượt ghi XONG đều để dấu mã G ở ít nhất một sổ", not khong_dau,
            str(khong_dau[:5]))

        # 3d (X4 dòng 23): lượt NHATKY mức C phải khớp một plan mang đúng mã G đó
        plan_da_ghi = {m for r in dong_bang(doc(so / "PLANNING.md"))
                       if any(o == "ĐÃ GHI" for o in r)
                       for m in re.findall(MAU_G, r[-1])}
        c_khong_plan = [h[0].strip("* ") for h in hang_nk
                        if len(h) > 3 and h[3].strip() == "C"
                        and re.fullmatch(MAU_G, h[0].strip("* "))
                        and h[0].strip("* ") not in plan_da_ghi]
        bao("3d. lượt mức C đều có plan mang mã G tương ứng", not c_khong_plan,
            str(c_khong_plan[:5]))

        hang_pl = dong_bang(doc(so / "PLANNING.md"))
        thieu_g = [h[0] for h in hang_pl
                   if any(o == "ĐÃ GHI" for o in h) and not re.search(MAU_G, h[-1] or "")]
        cho_chot = [h[0] for h in hang_pl if any(o == "CHỜ CHỐT" for o in h)]
        bao("4. plan ĐÃ GHI đều có mã G ở cột Mã ghi", not thieu_g, str(thieu_g))
        print(f"        plan CHỜ CHỐT: {cho_chot or 'không'}")

    lech = []
    for p in sorted(so.glob("*.md")):
        lines = doc(p).splitlines()
        for i, d in enumerate(lines[:-1]):
            if d.startswith("|") and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
                so_cot = d.count("|") - 1
                if lines[i + 1].count("|") - 1 != so_cot:
                    lech.append((p.name, "dòng kẻ"))
                j = i + 2
                while j < len(lines) and lines[j].startswith("|"):
                    if lines[j].count("|") - 1 != so_cot:
                        lech.append((p.name, f"dòng dữ liệu {j + 1}"))
                    j += 1
    bao("5. schema bảng: header, dòng kẻ, từng dòng dữ liệu cùng số cột",
        not lech, str(lech[:5]))

    vuot = []
    for p in sorted(so.glob("*.md")):
        n = len(dong_bang(doc(p)))
        if n > 500 or p.stat().st_size > 1_000_000:
            vuot.append((p.name, n, p.stat().st_size))
    bao("6. không sổ nào vượt ngưỡng 500 dòng / 1 MB", not vuot, str(vuot))

    trung_ma = []
    for ten, cot, mau in [("VIEC.md", 1, r"V-[A-Z0-9]+-\d+"), ("DUKIEN.md", 1, r"D-\d+"),
                          ("TAILIEU.md", 1, r"T-\d+"), ("QUYETDINH.md", 0, r"Q-\d+"),
                          ("PLANNING.md", 0, r"P-\d{8}-\d{2}")]:
        ds = [h[cot] for h in dong_bang(doc(so / ten)) if len(h) > cot and re.fullmatch(mau, h[cot])]
        t = sorted({m for m in ds if ds.count(m) > 1})
        if t:
            trung_ma.append((ten, t))
    bao("7. không mã trùng ở cột Mã của các sổ", not trung_ma, str(trung_ma))

    if not chua_cai:
        bdk = doc(so / "BANG_DIEU_KHIEN.md")
        g_bdk = re.search(r"sinh_boi:\s*(" + MAU_G + r")", bdk)
        if not ma_g:
            print("  BỎ QUA  8. chưa có lượt ghi nào trong NHATKY")
        else:
            gb = g_bdk.group(1) if g_bdk else None
            c = cua_cua(gb) if gb else None
            bao("8. BANG_DIEU_KHIEN sinh từ watermark của cửa nó",
                bool(gb and c and wm.get(c) == gb),
                f"bảng={gb} watermark {c}={wm.get(c) if c else 'không'}")
            khac = [f"{k}={v}" for k, v in sorted(wm.items()) if k != c and v[2:10] > (gb or '')[2:10]]
            if khac:
                print(f"        LƯU Ý: cửa khác có lượt ghi ngày mới hơn bảng ({'; '.join(khac)}), cân nhắc sinh lại")

    try:
        args_thuong, loc_ho = tach_tham_so(sys.argv[1:])
    except ValueError as e:
        bao("9-11. chế độ --ho giải được đúng một họ tài liệu", False, str(e))
        args_thuong, loc_ho = [], None
    if len(args_thuong) > 1:
        kho_arg = Path(args_thuong[1])
        if not kho_arg.is_dir():
            # ổ ngoài chưa cắm hay gõ sai: không quan sát, KHÔNG ghi đè cache
            # mốc ổn định bằng tập rỗng (hội đồng vòng 7, tự vệ vế ba)
            print(f"  BỎ QUA  9-11: gốc kho {kho_arg} không tồn tại hay chưa gắn;"
                  f" cache mốc ổn định giữ nguyên")
        elif kho_arg.resolve() == goc.resolve():
            # dán trùng đường 00_Index vào cả hai tham số: dừng sớm thay vì
            # phun "file khai Kho đã mất" oan (hội đồng vòng 6, tự vệ vế hai)
            print(f"  BỎ QUA  9-11: tham số <gốc kho> trùng với 00_Index;"
                  f" gốc kho là thư mục CHỨA 00_Index, ví dụ: {goc.parent}")
        else:
            quan_sat_kho(goc, so, kho_arg, loc_ho)
    elif loc_ho is not None:
        bao("9-11. chế độ --ho giải được đúng một họ tài liệu", False,
            "--ho cần cả <gốc kho> đứng trước")
    else:
        print("  BỎ QUA  9-11. không truyền <gốc kho>, không quan sát file nghiệp vụ")

    # 12 (profile EMAIL): đối chiếu nhật ký nạp, registry, THU, hộp thư khai báo
    kiem_email(goc, so)

    # 0f. File KHÔNG ĐỌC ĐƯỢC trong lượt chạy (khóa Office, sai encoding...):
    #     một dòng LỆCH đích danh thay vì chết traceback giữa báo cáo (v24).
    #     Đặt cuối để gom đủ mọi phép; các phép trên đã xử file lỗi như rỗng.
    if LOI_DOC:
        bao("0f. mọi file cần đọc đều đọc được", False,
            f"{sorted(set(LOI_DOC))[:5]}: file bị khóa hay sai encoding được các phép trên"
            f" coi như RỖNG, kết quả liên quan tới chúng chưa tin được; đóng"
            f" ứng dụng đang giữ file hay sửa encoding rồi rà lại")

    print()
    if loi:
        print(f"KẾT QUẢ: {len(loi)} lệch. Xuất vào báo cáo RA_SOAT, chưa sửa gì.")
        sys.exit(1)
    print("KẾT QUẢ: hệ sạch theo các phép kiểm máy.")


if __name__ == "__main__":
    try:
        _thuong, _ = tach_tham_so(sys.argv[1:])
    except ValueError as _e:
        print(f"LỖI CÁCH DÙNG: {_e}")
        print(CACH_CHAY)
        sys.exit(2)
    if not _thuong:
        print(CACH_CHAY)
        sys.exit(2)
    main(_thuong[0])
