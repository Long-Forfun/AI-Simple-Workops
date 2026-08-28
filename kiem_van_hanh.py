#!/usr/bin/env python3
# kiem_van_hanh.py · kiểm máy hệ WORKOPS đang chạy · v36 · 20260828
# v36, theo hội đồng vòng 14 (hai defect NẶNG do CHÍNH vòng 40 sinh): 0d và
# 3e nhìn cả _so\_lich_su\ - tách NHATKY quý cũ vào đó là ĐÚNG X5 mục 7 và
# bị phép 6 cưỡng bức, mà 3e lại tuyên "mất cả file quý, cấm cấp mã G" ·
# lech_c12 bỏ dòng ĐỊNH NGHĨA CÚ PHÁP của template (@DUAN.<MÃ DA>...) nên
# 0i hết bẫy vĩnh viễn không lối ra · 0g hết chốt theo pha rev 0 (kho vừa
# clone là lúc .git chắc chắn còn) · 0j bắt cả THƯ MỤC lạ · 1a đúng MỘT bản
# INSTRUCTION và chọn bản v LỚN NHẤT · 3c đòi dấu ở ĐÚNG các sổ đã khai
# chạm · 3f mọi dòng sổ phải mang mã G · 8b bảng đủ sáu bộ đếm · 0k mốc
# version của bộ khớp nhau (nâng cấp sót DOC_TRUOC thì kho tự khai bản cũ).
# v35, theo hội đồng vòng 13 (ba giám khảo cùng dựng lại được cảnh MẤT SỔ mà
# máy in "hệ sạch"): dấu vết đã-từng-ghi quét MỌI sổ và view trong _so (v34
# bỏ sót THU và BANG_DIEU_KHIEN, hai nơi mã G đậu theo X5 mục 3-4) · 0g dò
# .git ở CẢ THƯ MỤC CHA (clone vào chính gốc kho thì git stash vẫn nuốt sổ)
# · 0h rev 0 không còn tự nhận "chưa ghi" khi sổ đã mang mã G · 0i C12 phải
# khai đúng tập mục còn <chưa điền> (chống lách ngoại lệ C11) · 0j file lạ
# trong 00_Index (vùng bị loại khỏi quan sát nghiệp vụ) · 3e chiều NGƯỢC của
# 3c: mã G đậu ở sổ phải có dòng NHATKY, bắt mất TRỌN file quý · phép 8 tách
# hai chiều lệch, hết dẫn người dùng sinh lại bảng đè mất bằng chứng cuối.
# v34, theo PILOT vận hành thật: 0d hết báo động giả ngay sau khi cài (kho
# vừa cài chưa ghi lần nào thì NHATKY CHƯA sinh là đúng luật X5 mục 3, cũ
# báo 'trục sự thật đã biến mất, cấm cấp mã G') · 0g mới: 00_Index còn là
# bản làm việc git thì sổ sống nằm trong vùng git quản, git pull sẽ đụng.
# v33, theo hội đồng vòng 12: 12l so mã Q của tombstone ĐÚNG Ô trong
# QUYETDINH (qua dong_bang, hết so chuỗi con toàn văn) - Q là tiền tố của
# mã thật, hay Q chỉ được nhắc trong ghi chú của dòng khác, hết miễn oan.
# v32, theo hội đồng vòng 11: 12l miễn-hash đòi khuôn TRỌN "[đã xóa theo
# Q-<mã>]" (có ngoặc đóng, chuỗi lửng hết được miễn oan) VÀ mã Q phải có
# dòng trong QUYETDINH.md (tombstone mang Q ma bị bắt) · tự vệ vế SÁU: thư
# mục đầu tồn tại nhưng không có dấu vết cài đặt nào (_so, X0, INSTRUCTION)
# là LỖI CÁCH DÙNG exit 2, hết 4 LỆCH "khôi phục mức C" oan.
# v31, theo hội đồng vòng 10: nhãn "tiền tố gây nghi" TẤT ĐỊNH (chọn tiền tố
# DÀI nhất qua sorted, hết dao động theo hash seed) · 12l siết miễn-hash về
# đúng khuôn "[đã xóa theo Q-" và thông điệp lệch gợi kiểm tombstone sai
# khuôn · tự vệ tham số ĐẦU: đường dẫn không tồn tại hay flag lạ là LỖI CÁCH
# DÙNG exit 2, hết 4 LỆCH "khôi phục mức C" oan trên thư mục ma.
# v30, theo hội đồng vòng 9: heuristic cùng-tiền-tố lên tầng module
# (loc_nghi_ban_sao) để fixture ghim; cảnh báo NGHI nêu đích danh file tiền
# tố và có lối ra cho file thật (so nội dung theo X5 mục 4, không phải mục
# 3); 12l miễn so hash cho dòng tombstone "[đã xóa theo Q-" (xóa pháp lý
# đúng luật hết lệch oan ở index có ô hash); thông điệp BỎ QUA phép 1, 2-8
# hết nói "chưa cài đặt" khi thật ra X0 chỉ sai tên; tự vệ vế bốn nói thêm
# lối đặt lại quan sát khi kho rỗng có chủ đích.
# v29: heuristic bản sao CÙNG TIỀN TỐ cho file nghiệp vụ (khuôn OneDrive
# -<TênMáy>): ứng viên đề xuất _INBOX mà cùng thư mục có file làm tiền tố
# tên nó, đuôi -XXXX không phải vN, thì chuyển sang cảnh báo NGHI BẢN SAO
# thay vì mời vào sổ mức A - khép nốt lỗ vòng 6 tự khai.
# v28, theo hội đồng vòng 8: tự vệ tham số vế BỐN - kho tồn tại nhưng quét
# ra 0 file trong khi cache đang giữ >0 mục (mây chưa đồng bộ, ổ rỗng) thì
# cảnh báo và GIỮ cache, hết ghi đè mốc ổn định bằng tập rỗng · 0b chỉ flag
# bản X0 tên lạ khi BẢN CHUẨN cũng tồn tại (bản lạc); không có bản chuẩn
# thì nhường 0c xử "đổi tên", hết hai thông điệp trái chiều · nhánh 0c
# "chưa cài" chỉ kích hoạt khi TEMPLATE là file X0 duy nhất.
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
import itertools
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
# NN >= 2 chữ số và NEO CUỐI: bản cũ chốt \d{2} không neo nên "-101" bị
# cắt thành "-10", làm phép 8 và 8d tố ngược VĨNH VIỄN ở kho vượt 99 lượt
# một cửa một ngày - và phiên sau đọc watermark "-99" rồi cấp lại "-100",
# sinh mã TRÙNG THẬT (hội đồng vòng 19). X5 mục 3 không đặt trần 99.
MAU_G = r"G-\d{8}(?:-[A-Z0-9]+)?-\d{2,}(?!\d)"
# DANH BẠ PHÉP: DỮ LIỆU, không phải nhãn. Phép 14b của kiem_tra_bo đối
# chiếu danh bạ này với tập phép mà phép 13 THẬT SỰ ép được trạng thái vi
# phạm. Hội đồng vòng 15b: 27/36 phép xóa trọn được mà bộ vẫn in "sạch",
# gồm cả 8b mà vòng 43 khai đã vá, và 0k, 7c, 8c, 3d do vòng 43 tự đẻ ra.
PHEP_VH = ["0.", "0b.", "0c.", "0d.", "0e.", "0f.", "0g.", "0h.", "0i.",
           "0j.", "0k.", "1.", "1a.", "1b.", "1c.", "2.", "3a.", "3b.",
           "3c.", "3d.", "3e.", "3f.", "4.", "5.", "6.", "7.", "7b.",
           "0i2.", "0k2.", "3g.", "7c.", "7d.", "7d2.", "7e.", "7e2.", "7f.",
           "1d.", "7b2.", "7e3.", "7e4.", "7g.", "8.", "8b.", "8d.", "8c.",
           "8e.", "11b.", "0m.", "0n.", "13m.", "13n.", "7h.", "5b.", "0p.",
           "0i3.", "2b.", "10d.", "5d.", "5e.", "3h.", "0q.", "9d.", "0r.",
           "9.", "10a.", "10b.",
           "10c.", "11."]
BIET_MAT_SO = re.compile(
    r"(VIEC|DUKIEN|TAILIEU|QUYETDINH|PLANNING|THU|BANG_DIEU_KHIEN|X0_INDEX)\.md"
    r"|NHATKY_(\d{4}Q[1-4]|TEMPLATE)\.md|_thu_.*|_quan_sat_.*|_moc_ghi\.txt")
BIET_MAT_00 = re.compile(
    r"X[0-9]E?_[A-Z0-9_]+\.md|INSTRUCTION_WORKOPS_v\d+\.md|README\.md"
    r"|GHICHU_(DOI_MOI|LICHSU)_v.*\.md|DOC_TRUOC\.md|BENCHMARK_TOKEN\.md"
    r"|WORKOPS_.*_GOP\.md|kiem_\w+\.py|\.gitignore|_moc_(ghi|qd)\.txt")


def loc_dau_vet_ghi(so, doc_ham=None):
    """Mọi nơi mã G ĐẬU LẠI theo X5 mục 3-4, không phải chỉ 5 sổ lõi.
    THU.md có cột "Ghi lần"; BANG_DIEU_KHIEN và X0_INDEX mang sinh_boi và
    watermark sinh ở bước 6 của MỌI lượt ghi (kho vừa cài in "bàn sạch" nên
    KHÔNG mang mã G). Hai file máy _thu_* nằm trong .gitignore nên không
    được là bằng chứng DUY NHẤT. Hội đồng vòng 13: v34 quét thiếu ở đây làm
    máy in "hệ sạch" khi NHATKY đã mất."""
    d = doc_ham or (lambda p: p.read_text(encoding="utf-8") if p.is_file() else "")
    ra = sorted(q.name for q in list(so.glob("*.md")) + list((so / "_lich_su").glob("*.md"))
                if "TEMPLATE" not in q.name and re.search(MAU_G, d(q)))
    if (so / "_thu_nhat_ky.ndjson").is_file() or (so / "_thu_da_nap.json").is_file():
        ra.append("nhật ký EMAIL")
    return ra


def tim_vung_git(goc, them=None):
    """Thư mục gần nhất (kho hay TỔ TIÊN của nó) đang là bản làm việc git.
    Bắt cả .git thư mục lẫn .git FILE (worktree, submodule). Hội đồng vòng
    13: v34 chỉ soi đúng một tầng, clone vào chính gốc kho thì git stash
    vẫn nuốt dòng sổ mà lưới im. `them`: đường thứ hai để soi - hội đồng vòng
    17 chuyển _so thành JUNCTION sang thư mục Dropbox nằm trong một repo, gốc
    kho vẫn sạch nên 0g mù trọn; phải resolve TỪ ĐÍCH THẬT của _so đi ngược
    lên mới thấy .git đang quản sổ."""
    ra = []
    for goc_i in ([goc] if them is None else [goc, them]):
        try:
            g = Path(goc_i).resolve()
        except OSError:
            continue
        ra += [g, *g.parents]
    return next((d for d in ra if (d / ".git").exists()), None)


# Dòng ĐỊNH NGHĨA CÚ PHÁP ("@DUAN.<MÃ DA>", "@NGUON.<LOẠI>") là văn phạm của
# template, không phải ô giá trị: không đời nào điền được nên không tính là
# mục trống. Mốc "(cú pháp)" đánh tay cho khuôn tên file và lời hướng dẫn.
# Hội đồng vòng 14: thiếu vế này thì 0i là BẪY VĨNH VIỄN không lối ra hợp lệ.
SO_CO_GHI_LAN = ["VIEC.md", "DUKIEN.md", "TAILIEU.md", "QUYETDINH.md",
                 "PLANNING.md", "THU.md"]
MAU_LEGEND = re.compile(r"@[A-Z][A-Z0-9._]*<")
# X5 mục 1b cấm secret nằm trong kho đồng bộ, trong sổ và trong _INBOX.
# Hội đồng vòng 16 cắm chuỗi kết nối prod vào DUKIEN và prod.env vào kho:
# cả hai "hệ sạch", và bộ quan sát còn MỜI prod.env vào sổ mức A. Chính
# vòng 45 lấy hậu quả đó làm lý do dựng 7d mà không ai canh nó.
# Sau dấu phân cách phải là GIÁ TRỊ kiểu bí mật: >=12 ký tự LIỀN và có ít nhất
# một chữ số. Bản cũ chỉ đòi "\S" nên tố luôn "Loại secret: API key cổng thanh
# toán" - đúng cách viết mà X5 mục 1b DẶN dùng (hội đồng vòng 17, 3/7 báo oan).
MAU_SECRET = re.compile(
    r"(?i)(api[_-]?key|secret|password|passwd|token|private[_-]?key"
    r"|m[ậa]t\s*kh[ẩa]u|matkhau|m[ãa]\s*pin|kh[óo]a\s*api"
    r"|kh[óo]a\s*b[íi]\s*m[ậa]t|m[ãa]\s*kh[óo]a)"
    # cho HẬU TỐ giữa từ khóa và dấu phân cách: AWS_SECRET_ACCESS_KEY=,
    # SECRET_KEY= (Django), TOKEN_GITHUB=, api_key_prod= đều trượt khuôn cũ
    # vì nó đòi dấu :/= NGAY sau từ khóa (hội đồng vòng 21)
    r"[A-Za-z0-9_.-]{0,24}"
    r"\s*[:=]\s*(?=\S*\d)\S{12,}"
    r"|\b(sk|pk|ghp|xox[abpr])_[A-Za-z0-9_]{16,}"
    r"|[a-z+]+://[^\s/@]+:[^\s/@]+@"
    r"|BEGIN [A-Z ]*PRIVATE KEY")
MAU_FILE_SECRET = re.compile(r"(?i)\.env(\.|$)|(^|[/\\])id_rsa|\.pem$|\.p12$")
# file MẪU khai cấu hình là cách làm ĐÚNG (giá trị là <điền>), không phải
# secret: không loại nó ra thì lưới phạt đúng người làm đúng (vòng 17)
MAU_FILE_MAU = re.compile(r"(?i)\.(example|sample|template|mau|dist)$")
DUOI_VAN_BAN = (".env", ".txt", ".md", ".json", ".yml", ".yaml", ".ini",
                ".cfg", ".conf", ".sql", ".log", ".ndjson", ".csv", "")
# dump và log CỦA CHẠY THẬT mang dữ liệu khách: X5 mục 1 xếp mức C và cấm
# kéo vào kho đồng bộ. Chỉ tính khi tên hay đường dẫn mang NEO chạy thật,
# để dump của staging hay của máy dev không bị đá oan.
MAU_DUMP_PROD = re.compile(
    r"(?i)(^|[/\\_.-])(prod|production|live)([/\\_.-]|$)")
MAU_DUOI_DUMP = re.compile(r"(?i)\.(sql|dump|bak|mdf|bacpac)$")
MAU_TRONG = re.compile(r"<(?:chưa )?điền|<N>")


def muc_con_trong(nd):
    """Tập @KEY của X0 còn dấu chưa điền. MỘT nguồn duy nhất cho cả rà 0i lẫn
    bước 'quét X0 đưa mọi mục trống vào C12' của X9 mục 1: hai bên tính khác
    nhau thì kho cài đúng vẫn bị 0i tố (hội đồng vòng 14)."""
    mo = nd.index("# C12.") if "# C12." in nd else len(nd)
    than = nd[:mo] + (nd[nd.index("# C13."):] if "# C13." in nd else "")
    dong = than.splitlines()
    moc = [(i, m.group(1)) for i, m in
           ((i, re.match(r"\s*(@[A-Z][A-Z0-9._]*)\s", d)) for i, d in enumerate(dong)) if m]
    # X0 C0: "không bật thì AI bỏ qua khối đó, không đọc, không hỏi" - ép tham số
    # của profile chưa bật vào C12 là bắt công ty LITE ôm thứ nó không bao giờ
    # được hỏi (8/34 mục với bộ hiện tại, hội đồng vòng 15)
    bat = set(re.findall(r"\[x\]\s+(REGULATED|PARALLEL|AUTOMATED|EMAIL)", nd))
    ra = set()
    for vt, (i, khoa) in enumerate(moc):
        het = len(dong)
        for j in range(i + 1, len(dong)):
            if re.match(r"# C\d+\.", dong[j]) or (vt + 1 < len(moc) and j == moc[vt + 1][0]):
                het = j
                break
        khoi = "\n".join(dong[i:het])
        nhan_pf = set(re.findall(r"\((?:profile )?(REGULATED|PARALLEL|AUTOMATED|EMAIL)\)",
                                 khoi))
        if nhan_pf and not (nhan_pf & bat):
            continue
        if (MAU_TRONG.search(khoi) and "chỉ khai khi" not in khoi
                and "(cú pháp)" not in khoi and not MAU_LEGEND.search(khoi)):
            ra.add(khoa)
    return ra


def lech_c12(nd):
    """Tập mục lệch giữa C12 và tập THẬT còn dấu chưa điền của template.
    Dấu chưa điền gồm MỌI khuôn mẫu: <chưa điền>, <điền...>, <N>. Hội đồng
    vòng 13 (VẬN HÀNH) đếm được 29 mục còn trống sau khi cài mà C12 chỉ khai
    2, nên ngoại lệ C11 (2) phủ đúng 2/29. Quét theo DÒNG: mục nhiều dòng thì
    dấu trống ở dòng nối vẫn thuộc về @KEY gần nhất phía trên. Mục tự khai là
    tùy chọn ("chỉ khai khi") không tính. Dòng C12 đã ĐÁNH DẤU [x] là mục đã
    điền, giữ lại làm bằng chứng nhưng không còn là mục trống."""
    if "# C12." not in nd:
        return []
    c12 = nd[nd.index("# C12."):]
    c12 = c12[:c12.index("# C13.")] if "# C13." in c12 else c12
    that = muc_con_trong(nd)
    khai = set()
    for dong in c12.splitlines():
        if dong.strip().startswith(("[x]", "[X]")):
            continue  # đã điền, dòng giữ làm bằng chứng
        khai |= set(re.findall(r"@[A-Z][A-Z0-9._]*", dong))
    return sorted((that - khai) | (khai - that))
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


BAN_CU = ("bản cũ của file (kho mây: chuột phải file, chọn Version history;"
          " kho ổ máy đơn: lấy từ bản sao lưu ở thiết bị khác - không có thì"
          " nói với AI, nó dựng lại từ các sổ còn nguyên và đánh dấu CHƯA KIỂM)")
# hội đồng vòng 15: "version history" là tiếng Anh không giải nghĩa, và với
# kho Ổ MÁY ĐƠN - cấu hình README khai là được hỗ trợ - nó KHÔNG TỒN TẠI,
# nên chỉ dẫn cũ là bất khả thi. Câu này luôn có ít nhất một lối đi được.


def bang_moi_hon(gb, c, wm):
    """Bảng MỚI hơn mọi dòng NHATKY của cửa mình: NHATKY đã mất dòng, nên
    sinh lại bảng là XÓA BẰNG CHỨNG CUỐI. Tách hàm để fixture ghim được
    CHIỀU của lời dặn: cờ này không đổi phán quyết (phán quyết là
    wm.get(c) == gb) mà chọn giữa HAI lời dặn TRÁI NGƯỢC, nên đảo nó vẫn
    lọt mọi lưới cũ - hội đồng vòng 15 đảo được cả hai chiều."""
    def _khoa(m):
        return (m[2:10], int(m.split("-")[-1])) if re.fullmatch(MAU_G, m or "") \
            else ("", -1)
    return bool(gb and c and _khoa(gb) > _khoa(wm.get(c) or ""))


def _liet_cap(x, khuon="{0} {1}"):
    """Cặp (đối tượng, chi tiết) thành CÂU cho người đọc. _liet một mình không
    đủ vì str(tuple) vẫn phun ngoặc đơn và nháy - hội đồng vòng 16 đo được
    13/18 phép còn rò, đúng tập phép nằm trong MIEN_TRU của phép 14b."""
    return ", ".join(khuon.format(*t) for t in x) if x else "không có"


def _liet(x):
    """Liệt kê cho NGƯỜI đọc, không phải repr của Python: hội đồng vòng 15
    bắt được cả ngoặc vuông, nháy đơn và dấu escape lọt vào mắt người dùng."""
    return ", ".join(str(t)[:-1] + " (thư mục)" if str(t).endswith("\\")
                     else str(t) for t in x) if x else "không có"


def bao(ten, ok, chi_tiet=""):
    print(f"  {'PASS' if ok else 'LECH'}  {ten}" + (f": {chi_tiet}" if chi_tiet and not ok else ""))
    if not ok:
        loi.append(ten)


LOI_DOC = []
# số mục quan sát được mà chưa vào sổ (X4 dòng 2). KHÔNG phải lệch - đó là
# lời mời, không phải vi phạm - nhưng cũng KHÔNG được kết là "hệ sạch":
# phiên AI đọc dòng KẾT QUẢ sẽ ghi NHATKY "sổ khớp thực tế" trong khi hồ sơ
# đang nằm ngoài sổ, và vòng rà quý sau đếm từ chính dòng đó (vòng 17)
CHO_VAO_SO = []  # (đường dẫn, lý do) các file KHÔNG ĐỌC ĐƯỢC trong lượt chạy;
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


def goc_dai(kho):
    """Gốc kho ở dạng duyệt được đường dẫn DÀI. Trên Windows, `Path.rglob`
    nuốt OSError khi đường vượt MAX_PATH (260 ký tự) nên nó DỪNG ĐI XUỐNG ở
    đúng chỗ đó - im lặng tuyệt đối, cả một nhánh kho tàng hình cùng secret và
    dump khách nằm trong (hội đồng vòng 21). Kho thầu tiếng Việt vượt 260 ký
    tự là chuyện thường. Tiền tố đường dẫn dài gỡ giới hạn đó; nền khác trả
    nguyên gốc."""
    import os as _os_gd
    try:
        p = Path(kho).resolve()
        if _os_gd.name == "nt" and not str(p).startswith("\\\\"):
            return Path("\\\\?\\" + str(p))
        return p
    except OSError:
        return Path(kho)


def cat_muc(nd, n):
    """Nội dung mục "# Cn." của X0, cắt theo DÒNG chứ không theo `str.find`.

    `find("# C3.")` trả vị trí ĐẦU TIÊN của chuỗi đó ở BẤT KỲ đâu, nên một câu
    trỏ chéo trong mục trước - "Folder khối của kho: xem # C3. bên dưới", đúng
    tinh thần C14 - làm lát cắt RỖNG. Mà cả ba nhánh của 7b bọc `if ... and
    _da_khai`, nên phép TỰ TẮT không kêu, kéo theo 7d, 7d2 và vế dự án của 2b
    (hội đồng vòng 21). Trả "" khi thiếu mục - phép 0i2 lo phần báo thiếu."""
    m = re.search(rf"^# C{n}\. ", nd, re.M)
    if not m:
        return ""
    ke = re.search(r"^# C\d+\. ", nd[m.end():], re.M)
    return nd[m.start():m.end() + ke.start()] if ke else nd[m.start():]


def _quet_fence(nd):
    """Máy trạng thái fence theo CommonMark 4.5, dùng CHUNG cho `ngoai_fence`
    và phép 5e. Trả (danh sách (dòng, đang-trong-khối), số dòng MỞ còn treo).

    Ba luật mà bản vòng 38 thiếu:
      · fence ĐÓNG phải cùng KÝ TỰ và DÀI KHÔNG KÉM fence mở - thiếu vế độ dài
        thì khối bốn nháy (cách DUY NHẤT hợp chuẩn để dán ví dụ chứa ```) bị
        dòng ``` bên trong đóng sớm, ruột ví dụ lòi ra thành dòng bảng thật;
      · dòng ĐÓNG không được mang info string;
      · fence mở bằng dấu nháy thì info string không được chứa dấu nháy.

    Vòng 38 để 5e đếm ký tự còn ngoai_fence chạy máy trạng thái - hai bộ đọc
    một thứ bằng hai luật thì sớm muộn cũng lệch, và chúng lệch thật: khối ```
    có ruột là một dòng ~~~ bị 5e tố thiếu dòng đóng (hội đồng vòng 23)."""
    ra, mo, dai, n_mo = [], None, 0, 0
    for _i, d in enumerate(nd.splitlines(), 1):
        m = re.match(r"[ ]{0,3}(`{3,}|~{3,})(.*)$", d)
        if m:
            ky, n, duoi = m.group(1)[0], len(m.group(1)), m.group(2)
            if mo is None:
                if not (ky == "`" and "`" in duoi):
                    mo, dai, n_mo = ky, n, _i
                    ra.append((d, True))
                    continue
            elif ky == mo and n >= dai and not duoi.strip():
                mo = None
                ra.append((d, True))
                continue
        ra.append((d, mo is not None))
    return ra, (n_mo if mo is not None else 0)


def ngoai_fence(nd):
    """Các dòng NẰM NGOÀI mọi khối fence. Dùng CHUNG với phép 5b và phép 5e:
    vòng 62 dựng 5b biết fence mà quên dạy dong_bang, nên người dùng làm ĐÚNG
    lời khuyên của chính 5b ("bọc ví dụ trong ```") thì ăn ba dòng lệch - lớp
    phạt-người-làm-đúng lần thứ mười hai (hội đồng vòng 21)."""
    return ["" if trong else d for d, trong in _quet_fence(nd)[0]]


def tach_o(d, so_cot=None):
    """Tách ô của một dòng bảng. `\\|` là cách DUY NHẤT hợp lệ theo GFM để viết
    dấu | trong ô; tách thô làm dòng đó lệch ô và bị 3g, 5 tố oan (vòng 21)."""
    # Theo đúng GFM thì `\|` LÀ dấu thoát; không luật cú pháp nào phân biệt
    # được "ô kết thúc bằng \ rồi tới dấu ngăn" với "dấu | thoát giữa ô". Thứ
    # duy nhất phân biệt được là SỐ CỘT. X0 C1 BẮT BUỘC dòng trỏ BỘ HỒ SƠ kết
    # thúc bằng `\`, mà bảng gõ SÁT dấu | là khuôn GFM hợp lệ - người dùng làm
    # đúng HAI luật cùng lúc không được ăn lệch (hội đồng vòng 22).
    loi = d.strip().strip("|")
    ra = [o.replace("\\|", "|").strip() for o in re.split(r"(?<!\\)\|", loi)]
    if so_cot is None or len(ra) == so_cot:
        return ra
    # Đổi TRỌN dòng sang tách thô (bản vòng 38) thì dòng vừa mang `\|` thoát
    # VỪA trỏ thư mục ăn oan cả hai bản: GFM hụt một ô, thô dôi một ô. Nên mở
    # DẦN từng ngăn nghi ngờ cho tới khi đủ cột (hội đồng vòng 23).
    _chac = [_m.start() for _m in re.finditer(r"(?<!\\)\|", loi)]
    _mo_ho = [_m.start() + 1 for _m in re.finditer(r"\\\|", loi)]
    _k = so_cot - 1 - len(_chac)
    if not 1 <= _k <= len(_mo_ho) or len(_mo_ho) > 12:
        return ra                       # chặn nổ tổ hợp trên dòng rác

    def _cat_tai(_chon):
        _tr, _thu = 0, []
        for _v in sorted(_chac + list(_chon)):
            _thu.append(loi[_tr:_v])
            _tr = _v + 1
        _thu.append(loi[_tr:])
        return _thu

    # Ngăn nào là THẬT thì ô đứng trước nó kết thúc bằng `\`, mà theo X0 C1 chỉ
    # dòng trỏ BỘ HỒ SƠ mới được vậy - nên ưu tiên tổ hợp có nhiều ô-trước
    # TRÔNG NHƯ ĐƯỜNG DẪN nhất. Hoà thì lấy tổ hợp ở phía SAU.
    _tot, _diem_tot = None, -1
    for _chon in itertools.combinations(_mo_ho, _k):
        _thu = _cat_tai(_chon)
        _diem = sum(1 for _o in _thu[:-1]
                    if _o.endswith("\\") and re.search(r"[\\/]", _o[:-1]))
        if _diem >= _diem_tot:
            _tot, _diem_tot = _thu, _diem
    return [o.replace("\\|", "|").strip() for o in _tot]


def dong_bang(nd):
    """Các dòng dữ liệu bảng (bỏ header và dòng kẻ), mỗi dòng là list ô.

    Nhận tối đa BA khoảng trắng đầu dòng theo đúng GFM: bản cũ lọc bằng
    `d.startswith("|")` nên một dấu cách thừa - thứ Prettier, bản dán từ Word,
    hay một lượt AI "thụt cho đẹp" sinh ra - làm dòng đó biến mất khỏi 3f, 3g,
    5, 6, 7, 7b, 7b2, 7e, 7f, 7g và dem_qua_han cùng lúc, trong khi Markdown
    vẫn render nó và người vẫn đọc thấy (hội đồng vòng 19). Thụt SÂU hơn ba là
    khối code, không phải bảng - phép 5b báo riêng chỗ đó."""
    lines = [d.strip() if re.match(r"^[ \t]{1,3}\|", d) else d
             for d in ngoai_fence(nd)]
    headers, so_cot = set(), {}
    for i, d in enumerate(lines[:-1]):
        if d.startswith("|") and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
            _h = tuple(tach_o(d))
            headers.add(_h)
            so_cot[i] = len(_h)
    ket, _dang_mo = [], 0
    for i, d in enumerate(lines):
        if i in so_cot:                       # dòng header
            _dang_mo = so_cot[i]
            continue
        if not d.strip() or d.lstrip().startswith("#"):
            _dang_mo = 0                      # ra khỏi thân bảng
            continue
        if re.match(r"^\|[\s:|-]+\|$", d):
            continue                          # dòng kẻ
        if d.startswith("|"):
            r = tach_o(d, _dang_mo or None)
        elif _dang_mo:
            # GFM cho bỏ dấu | ĐẦU và CUỐI ở dòng THÂN. Không nhận thì 11 phép
            # cùng mù, y hệt lớp thụt lề của vòng 58 - Prettier và
            # markdownlint --fix đều sinh ra dạng này (hội đồng vòng 20).
            # ĐÒI ĐÚNG SỐ CỘT: nhận rộng hơn thì rác đứng trước dấu | đầu bị
            # đọc thành một ô, cả dòng lệch một ô, và 3g tố oan - bản vá chống
            # báo oan suýt tự đẻ ra báo oan.
            r = tach_o(d, _dang_mo)
            if len(r) != _dang_mo:
                continue
        else:
            continue
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
        # so NN theo SỐ, không theo chuỗi: "99" > "100" làm kho vượt 99 lượt
        # một cửa một ngày vừa lọt lưới (lane lùi được tuyên sạch) vừa bị tố
        # oan (kho khai ĐÚNG bị bảo "sinh lại bảng", tức kéo lane về -99 -
        # đúng thao tác gây cấp lại mã ĐÃ DÙNG). Vòng 58 nới MAU_G cho NN vượt
        # hai chữ số mà quên chỗ SO SÁNH này (hội đồng vòng 21).
        k = (m[2:10], int(m.split("-")[-1]))
        if c not in wm or k > (wm[c][2:10], int(wm[c].split("-")[-1])):
            wm[c] = m
    return wm


def la_file_tam(ten):
    return bool(MAU_TAM.search(ten))


def loc_nghi_ban_sao(de_xuat, tat_ca_stem):
    """Heuristic bản sao CÙNG TIỀN TỐ (khuôn OneDrive -<TênMáy>): ứng viên mà
    cùng thư mục có file khác làm TIỀN TỐ tên nó, đuôi -XXXX không phải vN.
    Trả (de_xuat_giữ, [(rel, tiền_tố_gây_nghi)]). Tầng module để fixture ghim."""
    giu, nghi = [], []
    for rel in de_xuat:
        tm2, stem = str(Path(rel).parent), Path(rel).stem
        goc_nghi = None
        for goc_stem in sorted(tat_ca_stem.get(tm2, ()), key=len, reverse=True):
            duoi = stem[len(goc_stem):]
            if (goc_stem and stem != goc_stem and stem.startswith(goc_stem)
                    and re.fullmatch(r"-[A-Za-z0-9][A-Za-z0-9-]{3,}", duoi)
                    and not re.fullmatch(r"-v\d+", duoi, re.I)):
                goc_nghi = goc_stem
                break
        (nghi.append((rel, goc_nghi)) if goc_nghi else giu.append(rel))
    return giu, nghi


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
    # NFD (macOS, iCloud, Dropbox) và NFC là CÙNG một họ: không chuẩn hóa thì
    # "Hồ_sơ_v01.docx" tách làm hai họ, phép 11 hết đường kêu XUNG ĐỘT và phép
    # 9 báo oan khi sổ ghi NFC mà đĩa giữ NFD (hội đồng vòng 17)
    import unicodedata as _ud
    goc = _ud.normalize("NFC", goc)
    goc = re.sub(r"[-_ ().]+", "_", goc).strip("_").lower()
    return goc + ("." + _ud.normalize("NFC", duoi).lower() if duoi else "")


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


# ký tự VÔ HÌNH hay sinh ra khi dán từ web, Word, Excel: zero-width, khoảng
# trắng không ngắt, dấu định hướng. Mắt không thấy, máy thấy khác hoàn toàn.
MAU_VO_HINH = re.compile(r"[\u200b-\u200f\u202a-\u202e\u2060\ufeff\xa0]")


def ta_vo_hinh(gt, hop_le):
    """Nếu bỏ ký tự vô hình đi thì giá trị KHỚP từ vựng, trả câu giải thích.

    Không có câu này thì thông điệp in ra "ô XONG" trong khi từ vựng cũng có
    "XONG": người dùng đối chiếu thấy khớp và kết luận MÁY HỎNG. Lưới đúng mà
    thông điệp làm nó thành vô dụng."""
    sach = MAU_VO_HINH.sub("", gt)
    if sach != gt and sach in hop_le:
        ma = ", ".join(sorted({f"U+{ord(c):04X}"
                               for c in gt if MAU_VO_HINH.match(c)}))
        return f"{sach} kèm KÝ TỰ VÔ HÌNH ({ma})"
    return None


def bo_dau(s):
    """Chữ thường, BỎ DẤU. Hội đồng vòng 16: ô "Chạm sổ nào" gõ "khong" thay
    vì "không" làm 3c báo LỆCH vĩnh viễn trên lượt tra cứu ĐÚNG LUẬT, và làm
    lối thoát XÓA PHÁP LÝ của X5 mục 7b không dùng được. Đúng lớp lỗi mà vòng
    45 vừa đóng cho 7d - và chính fixture của bộ cũng gõ "khong"."""
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", s.lower())
                   if unicodedata.category(c) != "Mn").replace("đ", "d")


def _la_lien_ket(p):
    """True cho symlink VÀ junction. Path.is_symlink() trả FALSE cho junction
    (reparse tag MOUNT_POINT chứ không phải SYMLINK), nên chốt chặn của vòng
    44 là no-op đúng trên nền tảng mà lỗi được báo: hội đồng vòng 16 dựng
    junction tự trỏ và quét ra 20 file, đệ quy chỉ dừng bằng MAX_PATH."""
    import stat as _stat
    try:
        return bool(p.lstat().st_file_attributes
                    & _stat.FILE_ATTRIBUTE_REPARSE_POINT)
    except (OSError, AttributeError):
        try:
            return p.is_symlink()
        except OSError:
            return False


def dem_qua_han(so, x0nd, hom_nay=None):
    """Đếm các mục QUÁ NGƯỠNG theo ngày, đọc ngưỡng từ X0 C9.

    Trả dict {"quá hạn", "rà lại", "hết hạn", "_INBOX"} -> list mã. Đây là bốn
    con số mà bảng điều khiển khai và banner mở phiên in ra, nhưng trước vòng
    51 không ai đối chiếu chúng với sổ: hội đồng vòng 18 dựng được kho có
    chứng thư số hết hạn 59 ngày mà bảng vẫn ghi "bàn sạch" (X4 dòng 8, 9, 11,
    14, 15). hom_nay: tiêm ngày giả cho fixture, đúng khuôn bay_gio của
    quet_ho - không có nó thì ca thử hỏng dần theo thời gian thật."""
    import datetime
    hom_nay = hom_nay or datetime.date.today()

    def ngay(o):
        m = re.search(r"(\d{4})-(\d{2})-(\d{2})", o or "")
        try:
            return datetime.date(*map(int, m.groups())) if m else None
        except ValueError:
            return None

    def nguong(ten, mac_dinh):
        """Đọc trong ĐÚNG KHỐI của @NHIP.<ten>. Bản cũ dùng `\\D*` khớp cả
        xuống dòng, nên mục còn <N> thì con trỏ chạy sang mục KẾ và lấy chữ số
        đầu tiên gặp được: @NHIP.INBOX từng lấy 30 của @NHIP.DEMSTAGING và
        @NHIP.RALAI lấy số 3 từ chữ "X3, X4" ở tiêu đề mục (hội đồng vòng 19).
        Biên bản nghiệm thu nằm _INBOX 18 ngày mà bộ im vì ngưỡng thành 30."""
        m = re.search(rf"@NHIP\.{ten}\b([^\n]*(?:\n(?![ \t]*(?:@|# C))[^\n]*)*)",
                      x0nd or "")
        so = re.search(r"(\d+)", m.group(1)) if m else None
        return int(so.group(1)) if so else mac_dinh

    ra = {"quá hạn": [], "rà lại": [], "hết hạn": [], "_INBOX": [],
          "plan C treo": [], "chờ đối tác": []}
    for r in dong_bang(doc(so / "VIEC.md")):
        if len(r) > 7 and r[7].strip() not in ("XONG", "HỦY"):
            h = ngay(r[6])
            if h and h < hom_nay:
                ra["quá hạn"].append(r[1].strip())
    for r in dong_bang(doc(so / "DUKIEN.md")):
        if len(r) > 9 and r[8].strip() not in ("HẾT HIỆU LỰC", "HỦY"):
            h = ngay(r[9])
            if h and h < hom_nay:
                ra["rà lại"].append(r[1].strip())
    _canh = nguong("HETHAN", 30)
    # dòng KHÔNG CÒN SỐNG thì thôi đếm: hợp đồng đã gia hạn bằng phụ lục, giấy
    # đã hết hiệu lực, hồ sơ đã trả. Không có các trạng thái này thì lối thoát
    # DUY NHẤT của người dùng là ghi đè ô Hết hạn của một bản ĐÃ KÝ - tức bộ
    # dẫn thẳng tới thao tác làm sai lệch sổ (hội đồng vòng 19).
    _thoi_dem = ("HẾT HIỆU LỰC", "ĐÃ GIA HẠN", "ĐÃ THAY", "TRẢ HỒ SƠ", "HỦY")
    for r in dong_bang(doc(so / "TAILIEU.md")):
        if len(r) > 11 and "[đã xóa theo Q-" not in "|".join(r):
            if len(r) > 7 and r[7].strip().upper() in _thoi_dem:
                continue
            h = ngay(r[11])
            if h and (h - hom_nay).days <= _canh:
                ra["hết hạn"].append(r[1].strip())
    # HAI BỘ ĐẾM banner X5 khai mà trước vòng 92 không máy nào đếm: plan C
    # treo và chờ đối tác quá ngưỡng - bảng khai 0 mà sổ đầy, 8e vẫn xanh
    # (giám khảo rubric 06, đúng lớp lỗi hội đồng vòng 18, nay đủ 6/6)
    for r in dong_bang(doc(so / "PLANNING.md")):
        if len(r) > 9 and r[9].strip() in ("MỚI", "ĐANG LÀM", "CHỜ CHỐT"):
            ra["plan C treo"].append(r[0].strip())
    _cdt = nguong("CHODOITAC", 5)
    for r in dong_bang(doc(so / "VIEC.md")):
        if len(r) > 7 and r[7].strip() == "CHỜ ĐỐI TÁC":
            h = ngay(r[5] if len(r) > 5 else "")
            if h and (hom_nay - h).days > _cdt:
                ra["chờ đối tác"].append(r[1].strip())
    _ib = nguong("INBOX", 3)
    thu = so / "_inbox"
    if thu.is_dir():
        for f in sorted(thu.glob("*")):
            if not f.is_file():
                continue
            d = ngay(re.sub(r"^(\d{4})(\d{2})(\d{2})", r"\1-\2-\3", f.name))
            if d and (hom_nay - d).days > _ib:
                ra["_INBOX"].append(f.name)
    return ra


# khuôn Windows/Chrome đặt khi tải lại file CÙNG TÊN: "BC (1).docx".
# Đây là tập CON của MAU_TAM: mọi file khớp nó vốn bị loại lặng lẽ.
MAU_BAN_SAO_N = re.compile(r"^(?P<goc>.+?) (?:\((?P<n>\d+)\)|- ?[Cc]opy"
                           r"(?: \d+)?|\(bản sao\))(?P<duoi>\.[^.]+)$")


def doc_saoluu(x0nd):
    """Giá trị @KHO.SAOLUU: trả (đường dẫn hay None, có_khai_chua_co)."""
    m = re.search(r"@KHO\.SAOLUU\s+(.+)", x0nd or "")
    if not m:
        return None, False
    v = m.group(1).strip()
    if re.search(r"(?i)ch[ưu]a c[óo]|<", v):
        return None, True
    d = re.match(r"([A-Za-z]:[\\/][^·,;]*|[\\/][^·,;]*)", v)
    return (d.group(1).strip() if d else None), False


def quet_ban_sao_n(kho):
    """File khuôn " (n)" mà nội dung KHÁC bản gốc cùng tên.

    Trả (khac_noi_dung, mo_coi). Bộ quan sát loại mọi file khớp MAU_TAM một
    cách LẶNG LẼ, nên bản thứ hai và thứ ba của một tài liệu - thứ Windows và
    Chrome tự đặt tên mỗi lần tải lại đính kèm cùng tên - biến mất khỏi mọi
    đầu ra, và người dùng được chỉ vào BẢN CŨ NHẤT (hội đồng vòng 18).
    TRÙNG sha thì im: đó mới là bản sao đồng bộ thật."""
    khac, mo_coi = [], []
    for f in sorted(kho.rglob("*")):
        try:
            if not f.is_file():
                continue
        except OSError:
            continue
        m = MAU_BAN_SAO_N.match(f.name)
        if not m:
            continue
        rel = str(f.relative_to(kho)).replace("\\", "/")
        if any(seg == t or seg.startswith((t + " ", t + "_", t + "-", t + "."))
               for seg in rel.split("/")
               for t in THU_MUC_HE_THONG + (".git", "__pycache__")):
            continue
        goc_f = f.with_name(m.group("goc") + m.group("duoi"))
        if not goc_f.is_file():
            mo_coi.append(rel)
        elif sha_file(f) != sha_file(goc_f):
            khac.append((rel, goc_f.name))
    return khac, mo_coi


def quet_secret(kho):
    """Quét secret ĐỘC LẬP với quet_ho. Trả (list file secret, list dump prod).

    KHÔNG dùng lại vòng lặp của quet_ho vì vòng đó loại dotfile và chịu bo_them
    TRƯỚC khi lưới secret nhìn thấy gì: `.env` - tên file secret phổ biến nhất -
    chưa bao giờ tới được 7e2, và một dòng trong _quan_sat_bo.txt tắt được hẳn
    lưới cho cả một thư mục (hội đồng vòng 18). Danh sách loại trừ của công ty
    là để bớt ồn khi quan sát TÀI LIỆU, không phải để tự miễn luật X5 mục 1b."""
    bo, dump = [], []
    _goc_d = goc_dai(kho)
    for f in sorted(_goc_d.rglob("*")):
        try:
            if not f.is_file():
                continue
        except OSError:
            continue
        rel = str(f.relative_to(_goc_d)).replace("\\", "/")
        if any(seg == t or seg.startswith((t + " ", t + "_", t + "-",
                                           t + ".", t + "("))
               for seg in rel.split("/") for t in (".git", "__pycache__")):
            continue
        # KHÔNG loại trọn 00_Index nữa: _so, _lich_su, _inbox, _thu_staging và
        # các bản backup đều nằm trong đó, và đó là chỗ secret THẬT rơi vào -
        # lối _thu_staging còn là lối TỰ ĐỘNG, không ai phải làm gì sai (hội
        # đồng vòng 19). Chỉ bỏ đúng FILE CỦA BỘ: chính tài liệu bộ trích
        # `sk_live_...` làm ví dụ nên quét chúng là tự báo oan mình.
        # miễn theo ĐƯỜNG DẪN, không theo tên: chỉ file CON TRỰC TIẾP của
        # 00_Index mới là file của bộ. So theo tên thì mọi README.md, mọi
        # .gitignore, mọi X?_*.md và MỌI .py ở bất kỳ đâu trong kho thành vùng
        # miễn dịch - mà README của repo và script deploy là hai chỗ secret hay
        # nằm nhất đời thật (hội đồng vòng 20, lỗi của bản vá vòng 58).
        _phan = rel.split("/")
        if len(_phan) == 2 and _phan[0] == "00_Index" and (
                BIET_MAT_00.fullmatch(f.name) or f.suffix.lower() == ".py"):
            continue
        if MAU_FILE_MAU.search(f.name):
            continue           # file MẪU khai cấu hình là cách làm ĐÚNG
        if MAU_FILE_SECRET.search(rel):
            bo.append(rel)
            continue
        if MAU_DUOI_DUMP.search(rel) and MAU_DUMP_PROD.search(rel):
            dump.append(rel)
            continue
        try:
            # file VĂN BẢN đọc tới 2 MB: file bàn giao môi trường 300 KB từng
            # lọt trọn vì trần cứng 256 KB (hội đồng vòng 19)
            _tran = (2 * 1024 * 1024
                     if f.suffix.lower() in DUOI_VAN_BAN else 256 * 1024)
            if f.stat().st_size > _tran:
                continue
            if MAU_SECRET.search(f.read_text(encoding="utf-8", errors="ignore")):
                bo.append(rel + " (giá trị trong ruột file)")
        except OSError:
            continue
    return sorted(bo), sorted(dump)


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
        nguon = sorted(goc_dai(kho).rglob("*"))
    for f in nguon:
        if not f.is_file() or f.suffix.lower() in DUOI_BO or f.name.startswith("."):
            continue
        try:
            rel = str(f.relative_to(kho)).replace("\\", "/")
        except ValueError:
            rel = str(f.relative_to(goc_dai(kho))).replace("\\", "/")
        # BỎ lọc tiền tố "9" (v10): 98_Assets và 99_Goc là vùng NGHIỆP VỤ phải
        # quét (X4 kiểm sha 99_Goc); chỉ loại đích danh kho lưu trữ 99_Archive
        if rel.startswith(("_", ".")) or "/_" in rel:
            continue
        if rel.split("/")[0] == "99_Archive":
            continue
        if ".git" in rel.split("/"):
            continue  # checkout repo trong kho: X0 C2 nói code KHÔNG chép vào
            # kho, và .git/HEAD từng được MỜI vào TAILIEU (hội đồng vòng 16)
        # khớp cả BẢN SAO: "00_Index - Copy", "00_Index (1)",
        # "00_Index_20260828". `_so` vốn được lọc bằng startswith("_") nên
        # bản sao của nó vẫn bị lọc; 00_Index thì không, và mỗi bản sao đẩy
        # trọn 14 FILE LUẬT thành ứng viên chờ vào TAILIEU (vòng 16)
        if any(seg == t or seg.startswith((t + " ", t + "_", t + "-",
                                           t + ".", t + "("))
               for seg in rel.split("/") for t in THU_MUC_HE_THONG):
            continue  # 00_Index là vùng luật và sổ, không phải tài liệu nghiệp
            # vụ - lọc ở MỌI TẦNG như "_so", không riêng tầng đầu: một bản sao
            # lưu 00_Index lồng trong kho đẩy trọn 14 file LUẬT thành ứng viên
            # vào TAILIEU, qua junction thì thành 93 (hội đồng vòng 15b)
        if _la_lien_ket(f) or any(
                _la_lien_ket(kho / "/".join(rel.split("/")[:i + 1]))
                for i in range(len(rel.split("/")) - 1)):
            continue  # junction hay symlink: nội dung thật đã quét ở đường
            # CHÍNH của nó; đi xuyên vào đây là đếm đúp và đệ quy tới khi
            # MAX_PATH cắt - giới hạn của Windows, không phải thiết kế
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
    # 0q. Không junction/symlink nào trong kho trỏ RA NGOÀI kho. Junction
    #     Windows tạo được KHÔNG cần admin và KHÔNG phải symlink (is_symlink
    #     trả False), nên `mklink /J 99_Goc D:\\ngoai` cho file ngoài kho qua
    #     hết 9/10a/10b/10d - trong khi sao lưu kho và git không mang chúng
    #     theo: "bản gốc bất biến" nằm ở chỗ không ai giữ (backlog vòng 22).
    def _la_lienket(_p):
        try:
            if _p.is_symlink():
                return True
            _ij = getattr(_p, "is_junction", None)
            return bool(_ij and _ij())
        except OSError:
            return False

    _lk_ngoai = []
    try:
        _goc0q = Path(kho).resolve()
        import os as _os0q
        for _day, _thu_mucs, _ in _os0q.walk(kho):
            for _t in list(_thu_mucs):
                _p = Path(_day) / _t
                if _la_lienket(_p):
                    _thu_mucs.remove(_t)     # không đi VÀO link: tránh vòng lặp
                    try:
                        _dich = _p.resolve()
                    except OSError:
                        _dich = None
                    if _dich is None or not str(_dich).startswith(str(_goc0q)):
                        _lk_ngoai.append(_p.name)
    except OSError:
        pass
    bao("0q. không link trỏ ra ngoài kho", not _lk_ngoai,
        f"{_liet(_lk_ngoai[:4])}: file sau link vẫn qua 9/10a/10b nhưng sao"
        f" lưu kho và git KHÔNG mang chúng - bản gốc nằm ở chỗ không ai giữ."
        f" Chuyển dữ liệu THẬT vào kho rồi gỡ link, mức C")

    khoa_ho = None
    if loc_ho is not None:
        try:
            khoa_ho = giai_ho(kho, loc_ho)
        except ValueError as e:
            bao("9-11. --ho giải đúng một họ tài liệu", False, str(e))
            return
    pv = f" [họ {khoa_ho[0]}/{khoa_ho[1]}]" if khoa_ho else ""
    lan_dau = not any(khoa_ho_cua(k) == khoa_ho for k in truoc) if khoa_ho else not truoc
    bo_them = tuple(l.strip().replace("\\", "/") for l in
                    doc(so / "_quan_sat_bo.txt").splitlines() if l.strip())
    nhom, moi = quet_ho(kho, truoc, bo_them, khoa_ho, bay_gio)
    if khoa_ho:
        if not moi:
            bao("9-11. --ho giải đúng một họ tài liệu", False,
                f"không file nào thuộc họ '{khoa_ho[1]}' trong '{khoa_ho[0]}'")
            return
        # THAY đúng họ đang quét: bỏ mọi mục cũ của họ này rồi thêm tập hiện tại
        gop = {k: v for k, v in truoc.items() if khoa_ho_cua(k) != khoa_ho}
        gop.update(moi)
        ghi_cache(cache, luc_kho, gop)
        print(f"        chế độ --ho{pv}: {len(moi)} file cùng họ, cache thay đúng họ này")
    else:
        if not moi and truoc:
            # kho tồn tại nhưng quét ra 0 file trong khi cache đang giữ mục:
            # nghi mây chưa đồng bộ hay sai đường - cảnh báo, GIỮ cache
            bao("9-11. kho quan sát có file", False,
                f"quét ra 0 file nghiệp vụ trong khi lần trước thấy"
                f" {len(truoc)}: kho chưa đồng bộ, ổ rỗng hay sai đường?"
                f" cache mốc ổn định giữ nguyên; kho thật sự đã rỗng có chủ"
                f" đích thì xóa _quan_sat_truoc.json để đặt lại quan sát")
            return
        ghi_cache(cache, bay_gio, moi)

    hang = dong_bang(doc(so / "TAILIEU.md"))
    # "KhoCu " là kho đã NGỪNG (X0 C1 @KHO.CU): chỉ tra lịch sử, có thể
    # offline, nên phép 9, 10a, 10b không soi - startswith("Kho ") có dấu cách
    # nên tự loại "KhoCu " rồi, ghi ra đây để vòng sau đừng nới nhầm
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
    _lech_hoa = []
    for h in dong_kho:
        rel = h[5][4:].strip("` ").replace("\\", "/").strip("/")
        # gốc DÀI: vòng 67 thêm goc_dai cho quet_ho và quet_secret mà quên đây,
        # nên cùng một lượt chạy tầng quan sát THẤY file còn phép 9 tuyên nó
        # ĐÃ MẤT - hai lời khai ngược nhau trong một báo cáo (vòng 22)
        _goc9 = goc_dai(kho)
        duong = _goc9 / rel
        if not duong.exists():
            # NFD (đĩa macOS, iCloud, Dropbox) và NFC là CÙNG MỘT tên. Không
            # thử lại thì dòng bị coi là MẤT FILE rồi `continue`, tức 10a và
            # 10b cũng thôi kiểm sha bản ĐÃ NỘP đó - mất lưới toàn vẹn ngay
            # trên hồ sơ đã nộp thầu. Docstring của chuan_hoa_ho từ vòng 17 đã
            # KHAI là phép 9 được vá chỗ này, mà nó chưa từng được vá.
            import unicodedata as _ud9
            for _dang in ("NFC", "NFD"):
                _thu = _goc9 / _ud9.normalize(_dang, rel)
                if _thu.exists():
                    duong = _thu
                    break
        if not duong.exists():
            mat.append((h[1], rel))
            continue
        # 9d. Tên THẬT trên đĩa khác HOA-THƯỜNG với tên khai: NTFS cho qua
        #     nên phép 9 im, nhưng đồng bộ sang Linux hay git checkout là
        #     "mất file" hàng loạt (backlog vòng 22). resolve() trả đúng
        #     casing trên Windows; so sau khi NFC hai vế để không dẫm lưới NFD.
        try:
            import unicodedata as _ud9d
            _that9 = str(duong.resolve()).replace("\\", "/")
            _duoi9 = _that9[-len(rel):] if len(_that9) >= len(rel) else _that9
            _a9 = _ud9d.normalize("NFC", _duoi9)
            _b9 = _ud9d.normalize("NFC", rel)
            if _a9.lower() == _b9.lower() and _a9 != _b9:
                _lech_hoa.append(f"{h[1].strip()}: sổ {rel[-30:]} / đĩa"
                                 f" {_duoi9[-30:]}")
        except OSError:
            pass
        sha_so = next((o for o in h if re.fullmatch(r"[0-9a-f]{12,64}", o)), None)
        if sha_so and duong.is_file():
            sha_that = (moi.get(rel) or {}).get("sha") or sha_file(duong)
            if not sha_that:
                # file bị khóa hay không đọc được (đã vào LOI_DOC): CHƯA KIỂM
                # ĐƯỢC, không phải "bị sửa" - hết cáo buộc oan bản ĐÃ KÝ đang mở
                khong_kiem.append((h[1], rel))
            elif not sha_that.startswith(sha_so[:12]):
                # so BỎ DẤU và cho phép chú thích kèm sau: "Đã ký",
                # "da ky", "ĐÃ KÝ (ban scan 19/8)" đều là MỐC CHÍNH THỨC.
                # So chuỗi tuyệt đối làm bốn cách viết đời thực tụt thao tác
                # mức C xuống mức A hay biến mất hẳn (hội đồng vòng 18)
                _o_kd = [bo_dau(o) for o in h]
                (sua_bat_bien if any(bo_dau(t) in o for t in BAT_BIEN
                                     for o in _o_kd) else lech_sha).append(h[1])
    # 10d. Ô sha256 BỎ TRỐNG là lối tắt hợp lệ ra khỏi 10a và 10b: không có
    #      sha thì cả dòng bị bỏ qua, nên bản ĐÃ KÝ / ĐÃ NỘP / ĐÃ CẤP mất trọn
    #      lưới toàn vẹn mà sổ vẫn xanh - AI cũng chỉ cần bỏ trống một ô là hết
    #      bị 10a tố. X4 dòng 5 liệt việc này mà chưa phép nào canh (vòng 21).
    #      CHỈ đòi ở dòng đã tới điểm đóng sha: mốc chính thức, hay file trong
    #      99_Goc. Bản NHÁP chưa tới điểm đó thì không phạt.
    _thieu_sha = []
    for h in dong_kho:
        # hỏi THƯ MỤC trên chuỗi CHƯA strip("/"): bản cũ strip xong mới hỏi
        # endswith("/") nên nhánh này là mã chết, và bộ hồ sơ ĐÃ NỘP (X0 C1
        # bắt bỏ trống sha) bị đòi sha oan (backlog vòng 22)
        _tho_h = h[5].strip().strip("`").replace("\\", "/")
        if _tho_h.endswith("/") or "[đã xóa theo Q-" in "|".join(h):
            continue          # dòng trỏ THƯ MỤC: X0 C1 bắt bỏ trống ô sha
        _rel_h = _tho_h[4:].strip("/ ")
        # cùng LUẬT ĐỌC MỐC với 10a (bo_dau + chú thích kèm): so tuyệt đối thì
        # "Da ky" hay "ĐÃ KÝ (bản scan 19/8)" được 10a coi là mốc nhưng 10d
        # cho qua - thiếu sha ở đúng bản đã ký mà sổ vẫn xanh (vòng 22)
        if not (any(bo_dau(t) in bo_dau(o) for t in BAT_BIEN for o in h)
                or _rel_h.lower().startswith("99_goc/")):
            continue
        if not any(re.fullmatch(r"[0-9a-f]{12,64}", o) for o in h):
            _thieu_sha.append((h[1] if len(h) > 1 else "?").strip())
    bao("10d. mốc chính thức, 99_Goc có sha256" + pv, not _thieu_sha,
        f"{_liet(_thieu_sha[:5])}: thiếu sha thì 10a và 10b BỎ QUA trọn dòng,"
        f" tức bản đã ký hay đã nộp không còn lưới toàn vẹn nào (X4 dòng 5)."
        f" Chạy lại lượt ghi để đóng sha, mức A")
    bao("9d. tên khai đúng hoa thường với đĩa" + pv, not _lech_hoa,
        f"{_liet(_lech_hoa[:3])}: NTFS cho qua nhưng đồng bộ Linux, git hay"
        f" rsync coi là MẤT FILE. Sửa sổ theo tên thật trên đĩa, mức A")
    bao("9. file khai 'Kho' còn trên kho" + pv, not mat,
        f"{mat[:5]}"
        + (": tài liệu nằm ở KHO CŨ thì khai dạng \"KhoCu <đường dẫn từ"
           " @KHO.CU>\" (X0 C1) - dạng đó không bị kiểm tồn tại vì kho cũ chỉ"
           " tra lịch sử và có thể offline; ĐỪNG chép file sang kho mới, X5"
           " mục 6 bắt bản cuối chỉ nằm MỘT kho" if mat else ""))
    bao("10a. mốc chính thức không sửa tại chỗ" + pv, not sua_bat_bien, str(sua_bat_bien))
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
    # heuristic bản sao CÙNG TIỀN TỐ (khuôn OneDrive -<TênMáy> trên file nghiệp
    # vụ): ứng viên mà cùng thư mục có file khác làm TIỀN TỐ của tên nó, phần
    # đuôi dạng -XXXX không phải vN, thì nghi bản sao - cảnh báo thay vì mời vào
    # sổ mức A (hội đồng vòng 6-8)
    tat_ca_stem = {}
    for (tm2, _), kq2 in nhom.items():
        for it2 in kq2["items"]:
            tat_ca_stem.setdefault(tm2, set()).add(Path(it2["ten"]).stem)
    de_xuat, nghi_ban_sao = loc_nghi_ban_sao(de_xuat, tat_ca_stem)
    if nghi_ban_sao:
        print("        NGHI BẢN SAO ĐỒNG BỘ (không mời vào sổ mức A): đúng bản"
              " sao thì so nội dung theo SUY BẢN HIỆN HÀNH (X5 mục 4) rồi chuyển"
              " _lich_su; là FILE THẬT khác nội dung thì cứ ghi TAILIEU như thường:")
        for d, goc_ng in nghi_ban_sao[:10]:
            print(f"          - {d} (tiền tố gây nghi: {goc_ng})")
    bao("11. không họ nào cùng vN khác nội dung" + pv, not xung_dot,
        str(xung_dot[:3]))
    if lan_dau:
        print(f"        LƯU Ý: lần quét ĐẦU của phạm vi này, chưa file nào đạt luật ổn"
              f" định; chạy lại sau tối thiểu {KHOANG_ON_DINH // 60} phút để nhận bản hiện hành")
    elif cho_on_dinh:
        print(f"        {cho_on_dinh} file mới đổi hay chưa giữ nguyên nội dung đủ"
              f" {KHOANG_ON_DINH // 60} phút, chờ lần quét sau")
    # KHÔNG mời file secret vào sổ, và bắt nó dù nó CHƯA thành ứng viên: file
    # phải qua hai lượt quét mới đủ luật ổn định, mà secret nằm chờ trong kho
    # giữa hai lượt đó vẫn là secret trong kho (hội đồng vòng 16). X5 mục 1b
    # cấm secret ở kho đồng bộ, ở sổ và ở _INBOX.
    # soi cả TÊN lẫn RUỘT: file bàn giao môi trường là chỗ tự nhiên nhất một
    # shop nhỏ viết chuỗi kết nối prod, mà bản cũ chỉ dò tên nên im (vòng 17).
    # File MẪU (.example...) là cách khai ĐÚNG, không tính.
    _secret_kho, _dump_kho = quet_secret(kho)
    _bo_moi = {_x.split(" (")[0] for _x in _secret_kho} | set(_dump_kho)
    de_xuat = [d for d in de_xuat if d not in _bo_moi]
    if _secret_kho:
        bao("7e2. file secret không ở kho đồng bộ", False,
            f"{_liet(_secret_kho[:5])}: KHÔNG mời vào sổ. Thu hồi và xoay khóa"
            f" TRƯỚC, chuyển ra khỏi kho sau; nơi giữ secret khai ở X0 C2. Mức C")
    if _dump_kho:
        bao("7e4. dump của chạy thật không ở kho",
            False, f"{_liet(_dump_kho[:5])}: dump chạy thật mang dữ liệu KHÁCH"
            f" HÀNG và kho là thư mục đồng bộ, file đã đi ra mọi máy công ty."
            f" Chuyển ra ngoài kho; cần phân tích thì lấy bản đã che. Mức C")
    # 11b. File khuôn " (n)" KHÁC nội dung bản gốc là TÀI LIỆU THẬT bị khuôn
    #      tên che, không phải bản sao đồng bộ. Bộ quan sát loại chúng lặng lẽ
    #      nên người dùng được chỉ vào BẢN CŨ NHẤT trong khi hai bản mới hơn
    #      không xuất hiện một dòng nào (hội đồng vòng 18: chênh 86 triệu đi
    #      vào DUKIEN mức nguồn A rồi ra hóa đơn).
    _bs_khac, _bs_mo = quet_ban_sao_n(kho)
    bao("11b. file khuôn \" (n)\" khác bản gốc",
        not _bs_khac,
        f"{_liet([f'{a} (khác {b})' for a, b in _bs_khac[:4]])}: khuôn này là"
        f" thứ Windows và Chrome tự đặt khi tải lại file CÙNG TÊN, nên đây rất"
        f" có thể là BẢN MỚI đối tác gửi lại chứ không phải bản sao. So nội"
        f" dung rồi đổi tên chuẩn theo X0 C4 và nạp TAILIEU; trùng nội dung"
        f" thì xóa bản thừa. Mức A")
    if _bs_mo:
        print(f"        LƯU Ý: {_liet(_bs_mo[:5])} mang khuôn \" (n)\" mà"
              f" KHÔNG có bản gốc cùng tên - bộ quan sát bỏ qua chúng, nên"
              f" chúng sẽ không bao giờ được mời vào sổ. Đổi tên chuẩn nếu là"
              f" tài liệu thật")
    if de_xuat:
        CHO_VAO_SO.append(len(de_xuat))
        print("        ĐỀ XUẤT _INBOX (bản hiện hành quan sát được, chưa vào sổ, ghi mức A):")
        for d in de_xuat[:15]:
            print(f"          - {d}")
        if len(de_xuat) > 15:
            print(f"          ... còn {len(de_xuat) - 15} mục nữa chưa vào sổ;"
                  f" nạp hàng loạt theo X9 mục 3b")


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


def cot_thu(nd, ten_cot, thieu=None):
    """Giá trị một cột của bảng THU theo TÊN cột trong header, không đoán vị trí.

    `thieu`: giá trị trả về khi KHÔNG tìm thấy tên cột; mặc định [] giữ tương
    thích. Gọi với một giá trị khác cho biết header đã đổi tên - đổi
    "Conversation-ID" thành "Conversation ID" là 12f và 12i cùng tắt IM LẶNG,
    hai dòng THU cùng một luồng hết trùng, và mỗi thư trong một hội thoại được
    cấp một mã #L- mới (hội đồng vòng 19)."""
    lines = nd.splitlines()
    for i, d in enumerate(lines[:-1]):
        if d.startswith("|") and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
            header = [o.strip() for o in d.strip("|").split("|")]
            if ten_cot not in header:
                return [] if thieu is None else thieu
            if True:
                idx = header.index(ten_cot)
                # GIỮ ô rỗng: lọc nó ra là mở lối thoát cho 12f và 12i -
                # bỏ trống Conversation-ID thì hai dòng cùng luồng hết trùng,
                # và mỗi thư trong một hội thoại được cấp một mã #L- mới
                # (hội đồng vòng 18)
                return [r[idx] for r in dong_bang(nd)
                        if len(r) == len(header)]
    return [] if thieu is None else thieu


def kiem_email(goc, so):
    """Phép 12. Trả list (tên, ok, chi tiết) để fixture gọi được cả hàm;
    đồng thời báo qua bao() khi chạy thật."""
    ket = []
    nk_p = so / "_thu_nhat_ky.ndjson"
    reg_p = so / "_thu_da_nap.json"
    thu_nd = doc(so / "THU.md")
    co_du_lieu_thu = bool(dong_bang(thu_nd))
    if not nk_p.is_file() and not reg_p.is_file() and not co_du_lieu_thu:
        print("  BỎ QUA  12. profile EMAIL chưa chạy")
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
    _CO_MAT = object()
    conv = cot_thu(thu_nd, "Conversation-ID", _CO_MAT)
    if conv is _CO_MAT:
        ket.append(("12i2. header THU còn đủ tên cột then chốt", False,
                    "không thấy cột 'Conversation-ID': đổi tên cột là 12f và"
                    " 12i cùng tắt IM LẶNG, mỗi thư trong một hội thoại được"
                    " cấp một mã #L- mới. Trả tên cột về đúng X5 mục 4"))
        conv = []
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
                # MỞ FILE BẰNG CHỨNG RA XEM. Bản cũ chỉ kiểm manifest là chuỗi
                # RỖNG HAY KHÔNG, nên một lượt dọn hỏng (đích chưa mkdir, đồng
                # bộ mây chưa lên, đường dẫn gõ sai) xóa sạch nguyên văn thư mà
                # 12j vẫn PASS - kho hết bằng chứng và không ai biết cho tới
                # lúc ra tòa (hội đồng vòng 18). X3E chỉ cho dọn KHI file đã
                # thật sự nằm ở vùng lưu chính.
                def _giai(_d):
                    """Đường dẫn bằng chứng tính từ GỐC KHO; nhận cả quy ước
                    tính từ 00_Index để không báo oan kho đặt khác."""
                    _r = str(_d).replace("\\", "/").strip()
                    for _n in (goc.parent / _r, goc / _r):
                        if _n.is_file():
                            return _n
                    return None

                _thieu_bc = []
                _fe = _giai(mv["eml_final_path"])
                if _fe is None:
                    _thieu_bc.append(f"eml_final_path {mv['eml_final_path']}"
                                     f" KHÔNG có trên kho")
                elif sha_file(_fe) != mv["sha256"]:
                    _thieu_bc.append("nguyên văn thư ở vùng lưu chính KHÁC"
                                     " sha256 mà manifest khai")
                for _dk in mv.get("attachment_final_paths") or []:
                    if not isinstance(_dk, str) or _giai(_dk) is None:
                        _thieu_bc.append(f"đính kèm {str(_dk)[:40]} KHÔNG có"
                                         f" trên kho")
                if not _thieu_bc:
                    continue  # đã dọn đúng luật, bằng chứng có thật
                loi_staging.append(
                    f"{k}: manifest dọn khai đã chuyển bằng chứng nhưng "
                    + "; ".join(_thieu_bc[:2])
                    + ". Staging đã xóa nên nguyên văn thư CHỈ CÒN ở nơi"
                      " manifest trỏ; khôi phục từ hộp thư, mức C")
                continue
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

    # 12n. Đính kèm của mail ĐÃ COMMITTED phải để lại DẤU Ở SỔ. X3E mục ĐÍNH
    #      KÈM: chép về chỗ xếp, tính sha256, trỏ vào cột Đính kèm của THU,
    #      RỒI MỚI được append COMMITTED; mục để ngoài theo mục 2 thì phải có
    #      dòng TAILIEU trỏ nguồn VÀ một VIEC tải tay. Trước vòng 54 không phép
    #      nào nối dinh_kem của payload với nội dung sổ, nên hợp đồng đã ký số
    #      được coi là "đã nạp" trong khi file chỉ nằm trong staging chờ bị dọn
    #      - và registry chặn nạp lại, tức mất IM LẶNG (hội đồng vòng 18).
    _tl_nd = doc(so / "TAILIEU.md")
    _vc_nd = doc(so / "VIEC.md")
    _loi_dk = []
    for _k in sorted(committed):
        if not luot[_k]["payload_ok"]:
            continue
        for _dk in luot[_k]["payload"].get("dinh_kem", []):
            _ten = str(_dk.get("ten") or "").strip()
            if not _ten:
                continue
            _sha12 = str(_dk.get("sha256") or "")[:12]
            _co = lambda _nd: (_ten in _nd) or bool(_sha12 and _sha12 in _nd)
            if _dk.get("de_ngoai"):
                # X3E mục 2: để ngoài thì phải có nguồn ở TAILIEU VÀ việc tải tay
                if not _co(_tl_nd) or not _co(_vc_nd):
                    _loi_dk.append(f"{_ten[:28]} khai de_ngoai mà thiếu dòng "
                                   + ("TAILIEU trỏ nguồn"
                                      if not _co(_tl_nd) else "VIEC tải tay"))
            elif not (_co(thu_nd) or _co(_tl_nd)):
                _loi_dk.append(f"{_ten[:28]} đã COMMITTED mà không có ở THU"
                               f" lẫn TAILIEU")
    ket.append(("12n. đính kèm của mail đã COMMITTED để lại dấu ở sổ",
                not _loi_dk, "; ".join(_loi_dk[:3])
                + ". Registry đã chặn nạp lại nên đây là MẤT IM LẶNG: chép về"
                  " chỗ xếp và trỏ vào cột Đính kèm của THU (X3E mục ĐÍNH KÈM),"
                  " mục để ngoài thì thêm dòng TAILIEU trỏ nguồn và một VIEC"
                  " tải tay (X3E mục 2)"))

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
                # đọc CẢ _lich_su: phép 6 BẮT tách sổ khi vượt 500 dòng, tách
                # xong theo đúng X5 mục 7 mà 12l chỉ đọc sổ sống thì người làm
                # ĐÚNG lãnh 400 dòng lệch vĩnh viễn, và lối thoát duy nhất họ
                # nghĩ ra là xóa _thu_ap_dung.json - tự phá rào chống nạp
                # trùng. 3c, 3d, 3e, 7 đã học điều này từ vòng 41 (vòng 18)
                o_cua[v["so"]] = dong_bang(doc(so_p)) + [
                    r for q in sorted((so / "_lich_su").glob(v["so"] + "*.md"))
                    for r in dong_bang(doc(q))]
            hang = [r for r in o_cua[v["so"]] if v["dong"] in [o.strip() for o in r]]
            if not hang:
                loi_dong.append(f"{kk}: mã dòng {v['dong']} không là Ô nào trong {v['so']}")
            elif (isinstance(v.get("hash"), str) and v["hash"]
                  and not any(
                      (m9 := re.search(r"\[đã xóa theo (Q-[A-Za-z0-9-]+)\]",
                                       "|".join(r)))
                      and any(m9.group(1) == o.strip()
                              for rq in dong_bang(doc(so / "QUYETDINH.md"))
                              for o in rq)
                      for r in hang)
                  and not any(
                    hashlib.sha256(("|".join(r)).encode("utf-8")).hexdigest() == v["hash"]
                    for r in hang)):
                # dòng tombstone xóa pháp lý (X5 mục 7b) được miễn so hash:
                # nội dung đã trung hòa có chủ đích, mã dòng vẫn đứng
                loi_dong.append(f"{kk}: hash nội dung dòng không khớp (nếu là dòng"
                                f" xóa pháp lý: kiểm tombstone đúng khuôn"
                                f" [đã xóa theo Q-<mã>])")
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
        f"vắng {_liet(vang)}: SỔ mất thì khôi phục là mức C (lấy lại từ {BAN_CU};"
        f" NHATKY làm trục sự thật, cấm gõ lại từ trí nhớ); riêng hai VIEW"
        f" BANG_DIEU_KHIEN, X0_INDEX chỉ cần sinh lại, mức A")

    # 0b. Conflicted copy của file sổ do đồng bộ mây: chứa lượt ghi bị kẹt,
    #     phải hòa giải theo X5 mục 3 rồi chuyển _lich_su, không được để im.
    # rglob trên _so: bản conflicted nấp trong _lich_su, _inbox hay
    # _thu_staging từng lọt trọn - loc_ban_chinh lọc nó khỏi lượt gộp NHATKY
    # nên một lượt ghi mức C tồn tại trên đĩa mà bộ tuyên bố sạch (vòng 20).
    # Báo ĐƯỜNG DẪN tương đối, không chỉ tên, để người dùng biết nó nằm đâu.
    xung = sorted(
        str(f.relative_to(so)).replace("\\", "/") if vung is so else f.name
        for vung in (so, goc)
        for f in (vung.rglob("*") if vung is so else vung.glob("*.md"))
        if f.is_file() and ("conflicted" in f.name.lower()
                            or "xung đột" in f.name.lower()
                            or la_file_tam(f.name)))
    # hậu tố LẠ trên tên sổ chuẩn (khuôn OneDrive -<TênMáy>...): cũng là bản sao
    xung += sorted(f.name for f in so.glob("NHATKY_*.md")
                   if f.name not in {x.split("/")[-1] for x in xung}
                   and "TEMPLATE" not in f.name
                   and not re.fullmatch(r"NHATKY_\d{4}Q[1-4]\.md", f.name))
    co_x0_chuan = any(re.fullmatch(r"X0_CAUHINH_[A-Z0-9]{3,4}\.md", f.name)
                      for f in goc.glob("X0_CAUHINH_*.md"))
    # bản X0 tên lạ CHỈ là "bản lạc" khi bản chuẩn cũng tồn tại; không có
    # bản chuẩn thì đó là bản duy nhất đặt sai tên - nhường 0c khuyên đổi tên
    xung += sorted(f.name for f in goc.glob("X0_CAUHINH_*.md")
                   if "TEMPLATE" not in f.name and co_x0_chuan
                   and not re.fullmatch(r"X0_CAUHINH_[A-Z0-9]{3,4}\.md", f.name))
    xung = sorted(set(xung))
    bao("0b. không bản conflicted copy", not xung,
        f"{_liet(xung[:3])}: dòng vắng ở bản chính chép sang rồi hòa giải mã"
        f" (X5 mục 3 bước 2), bản conflict chuyển _so/_lich_su")

    x0s = loc_ban_chinh(goc.glob("X0_CAUHINH_*.md"), r"X0_CAUHINH_[A-Z0-9]{3,4}\.md")
    co_template = any("TEMPLATE" in q.name for q in goc.glob("X0_CAUHINH_*.md"))
    ung_vien_tho = [q.name for q in goc.glob("X0_CAUHINH_*.md")
                    if "TEMPLATE" not in q.name]
    if not x0s and co_template and not ung_vien_tho:
        print("  BỎ QUA  0c: chỉ thấy X0_CAUHINH_TEMPLATE, hệ chưa cài đặt;"
              " chạy \"cài đặt\" theo X9 trước")
    elif not x0s:
        if ung_vien_tho:
            bao("0c. có bản X0 đang chạy", False,
                f"thấy {_liet(ung_vien_tho[:3])} nhưng tên KHÔNG đúng chuẩn"
                f" X0_CAUHINH_<MÃ 3-4 ký tự A-Z 0-9, không dấu>.md:"
                f" đổi tên file (mức B), không phải mất cấu hình")
        else:
            bao("0c. có bản X0 đang chạy", False,
                "không thấy X0_CAUHINH nào: mất file cấu hình, khôi phục mức C")
    else:
        bao("0c. đúng một bản X0",
            len(x0s) == 1, f"thấy {[q.name for q in x0s]}: nhiều ứng viên thì hệ"
            f" không tự chọn, gộp về một bản rồi rà lại")
    instrs = sorted(goc.glob("INSTRUCTION_WORKOPS_v*.md"),
                    key=lambda q: int(re.search(r"_v(\d+)\.md", q.name).group(1))
                    if re.search(r"_v(\d+)\.md", q.name) else 0, reverse=True)
    if len(instrs) > 1:
        bao("1a. đúng MỘT INSTRUCTION trong 00_Index", False,
            f"{[q.name for q in instrs][:4]}: X9 mục 3c dặn XÓA bản v* cũ, chỉ"
            f" giữ MỘT - hai bản thì phép 1 so nhầm và AI nạp nhầm luật; đang"
            f" lấy bản v lớn nhất để so")
    yc = re.search(r"instruction_yeu_cau:\s*(v\d+)", doc(x0s[0])) if x0s else None
    iv = re.search(r"INSTRUCTION · WORKOPS · (v\d+)", doc(instrs[0])) if instrs else None
    if not x0s and co_template:
        print("  BỎ QUA  1: " + ("X0 tên chưa chuẩn, đổi tên theo 0c rồi chạy lại"
              if ung_vien_tho else "chưa cài đặt, chưa có X0 để so instruction_yeu_cau"))
    else:
        bao("1. instruction_yeu_cau khớp INSTRUCTION",
            bool(yc and iv and yc.group(1) == iv.group(1)),
            f"X0={yc and yc.group(1)} INSTR={iv and iv.group(1)}")

    LOI_DOC.clear()
    rev = re.search(r"rev (\d+)", doc(x0s[0])) if x0s else None
    dau_vet_ghi = loc_dau_vet_ghi(so, doc)
    # rev 0 là LỜI KHAI của X0, không phải sự thật của sổ: X0 bị đồng bộ mây trả
    # về bản cũ thì cờ này tắt một lượt cả 0d, 2, 3, 4, 8. Có dấu vết ghi thì
    # KHÔNG cho phép tự nhận "chưa cài đặt" nữa (hội đồng vòng 13).
    chua_cai = ((bool(rev and rev.group(1) == "0") or (not x0s and co_template))
                and not dau_vet_ghi)
    if rev and rev.group(1) == "0" and dau_vet_ghi:
        bao("0h. rev X0 khớp trạng thái sổ đã ghi", False,
            f"X0 còn rev 0 (CHƯA cài) mà sổ đã mang dấu mã G"
            f" ({_liet(dau_vet_ghi[:3])}): X0 bị khôi phục nhầm bản cũ hay mất dòng"
            f" rev. Phục hồi rev đúng, mức C, từ {BAN_CU} TRƯỚC khi ghi tiếp."
            f" [AI: cấm cấp mã G mới khi chưa có lại]")
    if chua_cai:
        print("  BỎ QUA  2, 3, 4, 8: " + ("X0 tên chưa chuẩn (xem 0c), chưa đọc được rev"
              if not x0s and ung_vien_tho else "X0 rev 0, hệ chưa cài đặt, chưa có lượt ghi nào"))
    else:
        # quý cũ ĐÃ TÁCH vào _so\_lich_su\ theo X5 mục 7 (phép 6 cưỡng bức khi
        # sổ vượt 500 dòng) vẫn là NHATKY hợp lệ: một tầng, không đệ quy vào
        # backup_* kẻo 3b báo trùng mã oan (hội đồng vòng 14)
        co_nk = loc_ban_chinh(list(so.glob("NHATKY_*.md"))
                              + list((so / "_lich_su").glob("NHATKY_*.md")),
                              r"NHATKY_\d{4}Q[1-4]\.md")
        chi_conflict = (not co_nk and any(
            "TEMPLATE" not in q.name for q in so.glob("NHATKY_*.md")))
        # KHO VỪA CÀI, CHƯA GHI LẦN NÀO: NHATKY chưa sinh là ĐÚNG luật (X5 mục
        # 3 bước 1 tạo file quý ở lượt ghi ĐẦU). Chỉ khi có DẤU VẾT đã từng ghi
        # mà NHATKY vắng thì mới là mất trục sự thật (PILOT vòng 38: bản cũ dọa
        # "cấm cấp mã G" ngay sau khi cài đúng X9, hệ tự khóa mình). Tập dấu vết
        # tính ở loc_dau_vet_ghi, phủ MỌI sổ và view (hội đồng vòng 13).
        if not co_nk and not chi_conflict and not dau_vet_ghi:
            print("  BỎ QUA  0d: hệ đã cài nhưng CHƯA ghi lần nào; NHATKY quý sinh"
                  " ở lượt ghi đầu theo X5 mục 3 bước 1, chưa có là đúng")
        else:
            bao("0d. NHATKY tồn tại khi đã ghi", bool(co_nk),
                ("chỉ còn bản conflicted/xung đột, BẢN CHÍNH đã mất: khôi phục bản"
                 f" chính mức C từ {BAN_CU} TRƯỚC, rồi mới hòa giải theo 0b"
                 if chi_conflict else
                 f"còn dấu mã G ở ({_liet(dau_vet_ghi[:3])}) mà NHATKY vắng: trục sự thật"
                 " để cấp mã, hòa giải trùng và chốt sổ đã biến mất; khôi phục mức C"
                 f" từ {BAN_CU}. [AI: cấm cấp mã G mới khi chưa có lại]"))
    # 0g. Kho ĐANG CHẠY không được nằm TRONG bất kỳ bản làm việc git nào, kể
    #     cả khi .git ở thư mục CHA: git pull và git stash chạy từ gốc repo vẫn
    #     đụng _so. Hội đồng vòng 13 dựng lại được cảnh mất trọn sổ ở ca cha.
    # KHÔNG chốt theo chua_cai: kho vừa clone, X0 còn rev 0, là đúng khoảnh khắc
    # .git chắc chắn còn và cần cảnh báo nhất (hội đồng vòng 14)
    vung_git = tim_vung_git(goc, so)
    if vung_git is not None and chua_cai:
        # kho VỪA CLONE, chưa cài: chưa có sổ nào để mất, nên đây là LỜI NHẮC
        # chứ không phải lệch - đá người dùng ở bước 1 của README là báo động
        # giả. Cài xong (X9 mục 1 xóa .git) thì im; còn .git sau khi cài mới
        # là LỆCH thật. Hai giám khảo vòng 14 chốt ngược nhau, đây là chỗ gặp.
        print(f"  LƯU Ý  0g: còn thư mục ẩn .git ở {vung_git}. Chưa hại gì vì kho"
              f" chưa có sổ; bước cài đặt của X9 mục 1 sẽ xóa nó. Sau khi cài mà"
              f" còn thì thành LỆCH: git pull hay git stash sẽ nuốt dòng sổ")
    elif vung_git is not None:
        bao("0g. kho chạy không nằm trong bản git", False,
            f"thấy thư mục ẩn .git ở {vung_git} (thư mục này hay THƯ MỤC CHA"
            f" của kho): sổ công ty đang nằm trong vùng git quản. Nói với AI"
            f" \"xóa .git giúp tôi\" - sổ trên đĩa không suy suyển gì; tự làm"
            f" thì bật Hidden items trong File Explorer rồi xóa. TUYỆT ĐỐI"
            f" đừng gõ git pull hay git stash ở đây; lỡ gõ mà sổ trống thì git"
            f" stash pop lấy lại ngay. Nâng cấp bộ theo X9 mục 3c")

    # 13n. QUYETDINH tự khai "Không xóa dòng, không sửa NỘI DUNG quyết định"
    #      mà chưa máy nào giữ - sửa ô "Chọn gì" tại chỗ hay xóa trọn dòng
    #      đều im (backlog a). Neo ngoài _moc_qd.txt theo đúng khuôn _moc_ghi;
    #      sha chỉ lấy PHẦN BẤT BIẾN, hai ô quản trị đổi theo luật ĐÃ THAY
    #      không vào sha. Dòng chưa neo chỉ LƯU Ý - kho lập trước nâng cấp
    #      không bị phạt vì làm đúng luật của thời điểm cũ.
    _qd_neo_p = goc / "_moc_qd.txt"
    _qd_rows = {}
    for _r in dong_bang(doc(so / "QUYETDINH.md")):
        if len(_r) >= 8 and _r[0].strip().startswith("Q-") \
                and "[đã xóa theo Q-" not in "|".join(_r):
            import unicodedata as _ud13n
            # KHÔNG gồm ô Ghi lần: X5 mục 3 bước 3 bắt nối mã G vào Ghi
            # lần của MỌI dòng chạm tới - kể cả dòng bị đánh ĐÃ THAY - nên
            # gồm nó vào sha là phạt người làm đúng HAI luật cùng lúc (giám
            # khảo rubric 03). "Nội dung bất biến" = năm ô đầu, đúng lời sổ.
            _loi_qd = _ud13n.normalize(
                "NFC", "|".join(o.strip() for o in
                                (_r[0], _r[1], _r[2], _r[3], _r[4])))
            _qd_rows[_r[0].strip()] = hashlib.sha256(
                _loi_qd.encode("utf-8")).hexdigest()[:12]
    _neo_qd = {}
    if _qd_neo_p.is_file():
        for _d in doc(_qd_neo_p).splitlines():
            _m = re.match(r"\s*(Q-\S+)\s+([0-9a-f]{12})\s*$", _d)
            if _m:
                _neo_qd[_m.group(1)] = _m.group(2)
    _loi13n = []
    for _ma, _sha in sorted(_neo_qd.items()):
        if _ma not in _qd_rows:
            _loi13n.append(f"{_ma}: neo còn mà DÒNG BIẾN MẤT (sổ cấm xóa dòng)")
        elif _qd_rows[_ma] != _sha:
            _loi13n.append(f"{_ma}: nội dung quyết định bị SỬA TẠI CHỖ (sha"
                           f" lệch neo; muốn đổi thì thêm dòng mới + ĐÃ THAY)")
    bao("13n. QUYETDINH khớp neo _moc_qd", not _loi13n,
        f"{_liet(_loi13n[:3])}. Khôi phục dòng theo {BAN_CU}, mức C")
    _chua_neo = sorted(m for m in _qd_rows if m not in _neo_qd)
    if _chua_neo:
        # in SẴN dòng neo để dán nguyên văn: máy tính sha nên công thức không
        # cần chiếm chỗ trong X5, và người dùng không thể tính sai
        _dan = "; ".join(f"{m} {_qd_rows[m]}" for m in _chua_neo[:4])
        print(f"        LƯU Ý  13n: {len(_chua_neo)} dòng chưa neo - dán các"
              f" dòng sau vào _moc_qd.txt (mức A): {_dan}")

    # 0k. NEO NGOÀI _so: mọi nhân chứng (NHATKY, sáu sổ, hai view) đều nằm
    #     TRONG _so, nên một lần khôi phục nhầm hay rollback đám mây TRỌN thư
    #     mục đó xóa sạch bằng chứng cùng lúc: kho đã ghi 500 lượt trông y hệt
    #     kho vừa cài và máy in "hệ sạch". _moc_ghi.txt nằm ngoài _so nên sống
    #     sót (hội đồng vòng 15).
    _moc_p = goc / "_moc_ghi.txt"
    if not chua_cai:
        if not _moc_p.is_file() or not re.search(MAU_G, doc(_moc_p)):
            bao("0k2. neo ngoài _so tồn tại khi đã ghi",
                not dau_vet_ghi,
                "chưa có 00_Index\\_moc_ghi.txt (hay nó rỗng). Đây là nhân chứng"
                " DUY NHẤT nằm ngoài _so: thiếu nó thì một lần khôi phục nhầm"
                " trọn thư mục _so xóa sạch bằng chứng cùng lúc, và kho đã ghi"
                " 500 lượt trông y hệt kho vừa cài. Nối mọi mã G đã có vào đó"
                " theo X5 mục 3 bước 6. [AI: không cấp mã mới trước khi nối]")
        else:
            _moc = set(re.findall(MAU_G, doc(_moc_p)))
            _mat = sorted(_moc - set(re.findall(MAU_G, doc(so / "NHATKY_2026Q3.md")
                                                + "".join(doc(q) for q in
                                                          list(so.glob("NHATKY_*.md"))
                                                          + list((so / "_lich_su")
                                                                 .glob("NHATKY_*.md"))))))
            bao("0k. mã G _moc_ghi.txt còn dòng NHATKY", not _mat,
                f"{_liet(_mat[:5])}: neo ngoài _so còn mã mà NHATKY không có:"
                f" _so đã bị LÙI hay khôi phục nhầm. Khôi phục mức C từ"
                f" {BAN_CU}. [AI: cấm cấp mã G mới khi chưa có lại]")

    # 0i. C12 phải khai ĐÚNG tập mục còn trống. Ngoại lệ C11 (2) cho phép "điền
    #     lần đầu" ở mức B dựa trên tư cách thành viên của C12, nên C12 trôi khỏi
    #     sự thật là mở cửa lách (hội đồng vòng 13).
    if not chua_cai and x0s:
        _mat_muc = [m for m in ("C1", "C2", "C7", "C12")
                    if not re.search(rf"^# {m}\. ", doc(x0s[0]), re.M)]
        bao("0i2. X0 còn đủ mục phép kiểm dùng", not _mat_muc,
            f"mất mục {_liet(_mat_muc)}: xóa mục là TẮT LUÔN phép canh chính mục"
            f" đó - mất C12 thì 0i im, mất C2 thì 7b im (hội đồng vòng 16)")
        # 0i3. Khai TRÙNG một @KEY: mọi hàm đọc X0 đều re.search MỘT LẦN nên
        #      bản trùng được giải theo "dòng nào gặp trước", không ai biết có
        #      mâu thuẫn. Hai dòng CUA1 trỏ hai gốc là CHIA ĐÔI KHO - hai máy
        #      cùng cấp mã một lane; hai @CTY.MA thì tên file và mã G hết quy
        #      về một công ty. Trùng khóa sinh ra rất tự nhiên khi người dùng
        #      "chép dòng cũ xuống rồi sửa" đúng như X9 hướng dẫn (vòng 20).
        #      Chỉ đếm dòng KHỚP "^@KEY " nên các dòng NỐI thụt lề dưới cùng
        #      một khóa (X0 mẫu có @NHIP.HOPTHU ba dòng) không bị tính.
        _gt_khoa = {}
        for _d0i3 in doc(x0s[0]).splitlines():
            _m0i3 = (re.match(r"(@[A-Z][A-Z0-9._]*)\s+(\S.*)$", _d0i3)
                     or re.match(r"\s+(CUA\d+)\s*=\s*(\S.*)$", _d0i3))
            if _m0i3:
                _gt_khoa.setdefault(_m0i3.group(1), set()).add(
                    _m0i3.group(2).strip())
        _trung_khoa = sorted(f"{_k}: {_liet(sorted(_v)[:2])}"
                             for _k, _v in _gt_khoa.items() if len(_v) > 1)
        bao("0i3. mỗi @KEY của X0 khai một giá trị", not _trung_khoa,
            f"{_liet(_trung_khoa[:3])}: mọi phép đọc X0 lấy dòng GẶP TRƯỚC nên"
            f" bản khai trùng đi im. Hai cửa cùng tên trỏ hai gốc là chia đôi"
            f" kho: hai máy cùng cấp mã một lane. Gộp về một dòng, mức B")

        _lc = lech_c12(doc(x0s[0]))
        if _lc:
            bao("0i. C12 khai đúng tập mục <chưa điền>", False,
                f"lệch {_liet(_lc[:5])}: mục biến khỏi C12 mà giá trị vẫn trống là lách"
                f" ngoại lệ C11 (2); ngược lại là mục đã điền còn kẹt ở C12."
                f" Đồng bộ C12 rồi sinh lại X0_INDEX")

    # 0j. File LẠ trong 00_Index: vùng luật bị loại khỏi quan sát nghiệp vụ
    #     (THU_MUC_HE_THONG), nên tài liệu lỡ lưu vào đây KHÔNG phép nào nhặt.
    #     Trước vòng 38, "git status" là lưới cuối; xóa .git thì mất nốt.
    _la = sorted(f.name + ("\\" if f.is_dir() else "") for f in goc.iterdir()
                 if not (f.is_dir() and f.name in ("_so", "__pycache__", ".git"))
                 and not (f.is_file() and BIET_MAT_00.fullmatch(f.name)))
    # _so\ cũng ngoài quan sát nghiệp vụ, đúng nguyên văn lý lẽ của chính 0j:
    # tài liệu để đây KHÔNG BAO GIỜ được nhặt (hội đồng vòng 15)
    _la += sorted("_so\\" + f.name + ("\\" if f.is_dir() else "")
                  for f in (so.iterdir() if so.is_dir() else [])
                  if not (f.is_dir() and f.name in ("_lich_su", "_inbox", "_thu_staging"))
                  and not (f.is_file() and BIET_MAT_SO.fullmatch(f.name)))
    # _lich_su cũng phải soi: file lạ nấp ở đó không ai nhặt, mà đây là chỗ hồ
    # sơ nằm LÂU NHẤT. CHỈ mở thư mục này - `_inbox` theo định nghĩa chứa file
    # ĐỐI TÁC GỬI đủ mọi định dạng, `_thu_staging` chứa nguyên văn thư và đính
    # kèm do pipeline X3E sinh; soi "file lạ" ở hai chỗ đó là báo oan hàng loạt
    # (0b đã xuống cả ba từ vòng 63 - nó chỉ tìm bản conflicted).
    _ls_ok = re.compile(
        r"NHATKY_\d{4}Q[1-4]\.md"
        r"|(VIEC|DUKIEN|TAILIEU|QUYETDINH|PLANNING|THU)[_A-Za-z0-9-]*\.md")
    _la += sorted("_so\\_lich_su\\" + f.name + ("\\" if f.is_dir() else "")
                  for f in ((so / "_lich_su").iterdir()
                            if (so / "_lich_su").is_dir() else [])
                  if not (f.is_dir() and f.name.startswith("backup_"))
                  and not (f.is_file() and _ls_ok.fullmatch(f.name)))
    if _la:
        bao("0j. không file lạ trong 00_Index", False,
            f"{_liet(_la[:5])}: 00_Index là vùng luật, bị loại khỏi quan sát nên"
            f" file ở đây KHÔNG BAO GIỜ được đề xuất vào TAILIEU. Tài liệu thì"
            f" chuyển ra vùng nghiệp vụ rồi nạp sổ; file phụ trợ khai vào"
            f" _so\\_quan_sat_bo.txt, để NGOÀI 00_Index")
    if ((so / "_thu_nhat_ky.ndjson").is_file() or (so / "_thu_da_nap.json").is_file())             and not (so / "THU.md").is_file():
        bao("0e. THU.md tồn tại khi EMAIL có vết", False,
            "nhật ký hay registry còn mà sổ THU vắng: khôi phục mức C")

    bdk_nd = doc(so / "BANG_DIEU_KHIEN.md")
    if bdk_nd:
        bao("1b. BANG_DIEU_KHIEN trong trần 4.200",
            len(bdk_nd) <= 4200,
            f"{len(bdk_nd)} ký tự: bảng phình làm thuế mở phiên tăng ngầm, dọn bớt"
            f" khối cũ hay chuyển chi tiết xuống sổ")
    idx_rt = doc(so / "X0_INDEX.md")
    if idx_rt:
        bao("1c. X0_INDEX trong trần 2.400",
            len(idx_rt) <= 2400,
            f"{len(idx_rt)} ký tự: view phình thì thuế mở phiên tăng ngầm,"
            f" rút gọn về đúng rev, kho, profile, dự án, vị trí mục")

    # 2b. X0_INDEX khớp X0 ở PROFILE và DỰ ÁN, không chỉ ở rev. Sửa X0 mà
    #     không tăng rev là đường đi thường ngày (thêm dự án, bật profile), nên
    #     view mà INSTRUCTION bắt phiên đọc TRƯỚC có thể khai "profile: LITE"
    #     cho một công ty REGULATED: phiên chạy không nghi thức mức C và dự án
    #     thứ hai vô hình (hội đồng vòng 20). So theo TẬP, không nguyên văn.
    if not chua_cai and x0s and idx_rt:
        _x0nd2 = doc(x0s[0])
        _pf_x0 = set(re.findall(
            r"\[x\]\s*(REGULATED|PARALLEL|AUTOMATED|EMAIL)", _x0nd2))
        # CHỈ so trường mà view CÓ KHAI: view tối giản (không dòng profile,
        # không dòng du_an) là hợp lệ, so vô điều kiện là báo oan mọi kho như
        # thế - bản đầu của phép này làm đúng vậy trên chính kho lành của
        # phép 13.
        _m_pf = re.search(r"profile:\s*(.+)", idx_rt)
        _pf_iv = set(re.findall(r"\b(REGULATED|PARALLEL|AUTOMATED|EMAIL)\b",
                                _m_pf.group(1) if _m_pf else ""))
        _c2b = cat_muc(_x0nd2, 2)
        _da_x0 = {m.group(1) for m in re.finditer(
            r"@DUAN\.([A-Z0-9]+)[^\n]*đang chạy", _c2b) if m.group(1) != "PHANMEM"}
        _m_da = re.search(r"du_an:\s*(.+)", idx_rt)
        _da_iv = set(re.findall(r"[A-Z0-9]{2,6}",
                                _m_da.group(1) if _m_da else ""))
        # CTY "luôn có" theo chính chữ của X0 C2 - nó không mang đuôi "đang
        # chạy" nên không vào _da_x0, mà view khai nó là ĐÚNG X5 mục 4: so
        # tuyệt đối là tố oan mọi view khai đủ (giám khảo rubric 05)
        _da_iv.discard("CTY")
        _lech2b = []
        if _m_pf and _pf_x0 != _pf_iv:
            _lech2b.append(f"profile: X0 bật {_liet(sorted(_pf_x0)) or 'LITE'},"
                           f" view khai {_liet(sorted(_pf_iv)) or 'LITE'}")
        if _m_da and _da_x0 and _da_x0 != _da_iv:
            _lech2b.append(f"dự án đang chạy: X0 có {_liet(sorted(_da_x0))},"
                           f" view khai {_liet(sorted(_da_iv)) or 'không'}")
        bao("2b. X0_INDEX khớp X0: profile, dự án", not _lech2b,
            f"{'; '.join(_lech2b)}: INSTRUCTION bắt phiên đọc view NÀY trước,"
            f" nên view lạc hậu là cả phiên chạy sai chế độ - công ty REGULATED"
            f" bị xử như LITE thì không nghi thức mức C, và dự án vắng ở view"
            f" thành vô hình. Sinh lại view theo X5 mục 3 bước 6")

    # 1d. X0 CỦA KHO ĐANG CHẠY. NGAN_SACH của kiem_tra_bo chỉ chấm bản
    #     TEMPLATE trong bộ mẫu; file mà phiên CHAT thật sự nạp nguyên vẹn là
    #     X0 mang mã công ty, và trước vòng 48 không phép nào đo nó - bơm lên
    #     49.591 ký tự vẫn "hệ sạch" (hội đồng vòng 17). Trần 22.000 là trần
    #     template 20.000 cộng 10% chỗ điền giá trị thật, nên kho vừa cài
    #     (18.969 LITE, 19.059 REGULATED+EMAIL) không bị kêu oan.
    if x0s:
        _n_x0 = len(doc(x0s[0]))
        bao("1d. X0 đang chạy trong trần 28.000", _n_x0 <= 28000,
            f"{_n_x0} ký tự: X0 là file phiên CHAT nạp NGUYÊN VẸN mỗi lượt, nên"
            f" nó phình là thuế thường trực phình theo. Chuyển phần liệt kê dài"
            f" xuống sổ, giữ X0 là nơi khai THAM SỐ")

    # D7 vòng 18: chua_cai và dau_vet_ghi đọc TRỌN từ trong _so, nên khi _so
    # bay thì cả hai rơi về "kho mới cài" - đầu ra có "CHƯA ghi lần nào" nằm
    # ngay cạnh dòng tố mất 5 mã G. Người dùng đang hoảng đọc câu đầu bảng,
    # kết luận không mất gì, rồi ghi tiếp - cấp lại chính những mã đã dùng.
    # Neo ngoài _so sinh ra đúng để trả lời câu này; chỉ là chưa ai hỏi nó.
    if chua_cai and _moc_p.is_file() and re.search(MAU_G, doc(_moc_p)):
        print("        CẢNH BÁO: kho trông như CHƯA ghi lần nào, nhưng neo"
              " ngoài _so còn mã G - nhiều khả năng _so vừa bị khôi phục nhầm"
              " hay rollback đám mây, xem dòng 0k. [AI: TUYỆT ĐỐI không cấp mã"
              " G mới trước khi dựng lại sổ]")

    # 0m. NƠI SAO LƯU NGOÀI KHO. Backup hằng ngày của X5 mục 7 nằm TRONG
    #     _so, nên lượt rollback đám mây trọn _so xóa sạch cả chúng - hội đồng
    #     vòng 18 dựng đúng cảnh đó và 7/7 bản chết cùng lượt. Lối khôi phục mà
    #     chính phép 0 chỉ ra ("bản sao lưu ở thiết bị khác") trước vòng 53
    #     không có thủ tục nào trong bộ tạo ra nó.
    if not chua_cai and x0s:
        _sl_d, _sl_chua = doc_saoluu(doc(x0s[0]))
        # chưa khai thì KHÔNG nhắc ở đây: @KHO.SAOLUU là mục trống của X0
        # C12 và phép 0i đã canh đúng việc đó. Nhắc thêm ở mỗi lượt RA_SOAT là
        # thuế vĩnh viễn trên trần đầu ra cho một nghĩa vụ đã có lưới.
        if not (_sl_chua or _sl_d is None):
            _slp = Path(_sl_d)
            if not _slp.is_dir():
                print(f"        LƯU Ý  0m: nơi sao lưu {_sl_d} không thấy;"
                      f" ổ ngoài chưa cắm? Không kết luận")
            else:
                import time as _t0m
                _moi_nhat = max((f.stat().st_mtime for f in _slp.rglob("*")
                                 if f.is_file()), default=0)
                _ngay = int((_t0m.time() - _moi_nhat) / 86400) if _moi_nhat else 9999
                bao("0m. nơi sao lưu ngoài kho còn cập nhật", _ngay <= 7,
                    f"{_sl_d}: bản mới nhất cách đây {_ngay} ngày - đây là bản"
                    f" DUY NHẤT sống sót một lượt rollback trọn _so. Sao lại, mức A")

    # 0n. Cache quan sát là chỗ luật ổn định hai lượt đặt trọn niềm tin, mà
    #     trước vòng 55 không phép nào nhìn nó. Mốc TƯƠNG LAI (đồng hồ máy sai,
    #     hay một lượt sinh lại cẩu thả) làm mọi file lập tức "đủ ổn định": bộ
    #     công nhận HIỆN HÀNH một file có thể đang ghi dở rồi đóng sha của nó
    #     vào TAILIEU làm mốc toàn vẹn. KHÔNG phải rào chống giả mạo có chủ ý -
    #     ai sửa được cache thì cũng sửa được sổ - mà là lưới cho hai ca THẬT
    #     hay xảy ra: cache hỏng cấu trúc, và mốc tương lai.
    _cache_p = so / "_quan_sat_truoc.json"
    if _cache_p.is_file():
        import time as _t0n
        _loi0n = []
        try:
            _cn = json.loads(doc(_cache_p) or "{}")
            _files0n = _cn.get("files") if isinstance(_cn, dict) else None
            if not isinstance(_files0n, dict):
                _loi0n.append("không phải object {files: {...}} của bản v2")
            else:
                _tuonglai = sorted(
                    k for k, v in _files0n.items()
                    if isinstance(v, dict)
                    and isinstance(v.get("luc"), (int, float))
                    and v["luc"] > _t0n.time() + 86400)
                if _tuonglai:
                    _loi0n.append(f"{len(_tuonglai)} mục mang mốc TƯƠNG LAI"
                                  f" ({_tuonglai[0][:40]}...)")
        except ValueError:
            _loi0n.append("không đọc được JSON")
        bao("0n. cache quan sát không mốc tương lai",
            not _loi0n, f"{'; '.join(_loi0n[:2])}: luật ổn định hai lượt dựa"
            f" trọn vào file này, mốc sai làm bộ công nhận HIỆN HÀNH một file"
            f" có thể đang ghi dở. Xóa {_cache_p.name} để đặt lại quan sát"
            f" (mất hai lượt chờ, không mất dữ liệu nào)")

    # 0r. Vòng đời _inbox -> _da_nap (X3 chặng 2): nạp xong phải CHUYỂN, tên
    #     gốc phải để lại dấu ở sổ. File nằm CẢ HAI nơi là bản chép sót -
    #     phiên sau nạp LẠI và dòng sổ nhân đôi; file _da_nap không dấu vết
    #     sổ nào là "đã nạp" bằng lời khai suông (backlog j, vòng 22).
    _ib0r = so / "_inbox"
    _dn0r = _ib0r / "_da_nap"
    _loi0r = []
    if _dn0r.is_dir():
        _hai_noi = [f.name for f in _ib0r.glob("*")
                    if f.is_file() and (_dn0r / f.name).is_file()]
        if _hai_noi:
            _loi0r.append(f"nằm CẢ hai nơi: {_liet(_hai_noi[:3])} (chép sót -"
                          f" phiên sau nạp LẠI, dòng sổ nhân đôi; xóa bản"
                          f" _inbox)")
        _van0r = "|".join(
            [doc(so / t) for t in ("TAILIEU.md", "DUKIEN.md", "VIEC.md",
                                   "THU.md", "QUYETDINH.md")]
            + [doc(f) for f in sorted(so.glob("NHATKY_*.md"))]
            + [doc(f) for f in sorted((so / "_lich_su").glob("*.md"))])
        _mo_coi = [f.name for f in sorted(_dn0r.glob("*"))
                   if f.is_file() and f.name not in _van0r]
        if _mo_coi:
            _loi0r.append(f"nạp MỒ CÔI: {_liet(_mo_coi[:3])} - không sổ nào"
                          f" mang tên gốc (X3 chặng 2 bắt ghi vào Căn cứ"
                          f" trạng thái); dựng lại lượt nạp")
    bao("0r. _inbox sang _da_nap sạch vòng đời", not _loi0r,
        "; ".join(_loi0r) + ". Mức A")

    # Neo BÀN GIAO (vế TỔ CHỨC): @NHIP.BANGIAO tự hứa "rà một lượt việc đang
    #     mở và plan treo sang người mới" mà không máy nào nhắc - người cũ đã
    #     nghỉ, việc vẫn gán tên họ và trôi vô chủ (giám khảo rubric 04). Chỉ
    #     LƯU Ý: việc ĐÚNG là của người cũ cho tới khi rà xong.
    if not chua_cai and x0s:
        # neo ĐẦU DÒNG: văn xuôi C6 cũng nhắc "@NHIP.BANGIAO đổi khi bàn
        # giao" và re.search không neo vớ nhầm câu đó thay vì dòng khai C9
        _mbg = re.search(r"^@NHIP\.BANGIAO\s+([^\n<]+)", doc(x0s[0]), re.M)
        _v_bg = (_mbg.group(1).strip() if _mbg else "")
        if _v_bg and not re.match(r"(?i)ch[ưu]a c[óo]", _v_bg):
            # cắt đuôi "cũ/mới": người điền xuôi khuôn "<tên người cũ,
            # người mới>" thành "An cũ, Bình mới" - giữ nguyên là câm cả hai
            # vế (giám khảo rubric 06)
            _ten_cu = re.sub(r"\s*\(?(c[ũu]|m[ớo]i)\)?$", "",
                             _v_bg.split(",")[0].strip())[:30]
            if _ten_cu:
                _viec_cu = [
                    (_r[1] or "?").strip()[:12]
                    for _r in dong_bang(doc(so / "VIEC.md"))
                    if len(_r) > 7 and _r[7].strip() not in ("XONG", "HỦY")
                    and bo_dau(_ten_cu) in bo_dau(_r[4] if len(_r) > 4 else "")]
                # người GẬT mức C đã nghỉ mà C2 vẫn ghi tên: 7g sẽ mãi
                # bảo đi xin cái gật của người cũ (giám khảo rubric 05)
                # tách C2 thành TỪNG KHỐI entry rồi tìm trong TRỌN khối:
                # bản regex một-dòng chết trên chính khuôn nhiều dòng của
                # template - fixture một-dòng "tái đo chết" mà không phủ
                # khuôn thật (giám khảo rubric 06)
                _c2bg = cat_muc(doc(x0s[0]), 2)
                _pm_bg = _c2bg[_c2bg.find("@DUAN.PHANMEM"):] \
                    if "@DUAN.PHANMEM" in _c2bg else ""
                _pm_cu, _kh_bg, _ma_bg = [], [], None
                for _dg in _pm_bg.splitlines():
                    _mkb = re.match(r"\s{2}([A-Z0-9]{2,6})\s", _dg)
                    if _mkb:
                        if _ma_bg and re.search(
                                r"(?:ph[ụu] tr[áa]ch|owner)[^·]*"
                                + re.escape(_ten_cu),
                                "\n".join(_kh_bg), re.I):
                            _pm_cu.append(_ma_bg)
                        _ma_bg, _kh_bg = _mkb.group(1), []
                    _kh_bg.append(_dg)
                if _ma_bg and re.search(
                        r"(?:ph[ụu] tr[áa]ch|owner)[^·]*" + re.escape(_ten_cu),
                        "\n".join(_kh_bg), re.I):
                    _pm_cu.append(_ma_bg)
                if _viec_cu or _pm_cu:
                    _vepm = (f"; phần mềm {_liet(_pm_cu[:2])} còn ghi"
                             f" {_ten_cu} ở vế phụ trách C2" if _pm_cu else "")
                    print(f"        LƯU Ý  bàn giao: {len(_viec_cu)} việc đang"
                          f" mở còn gán {_ten_cu} ({_liet(_viec_cu[:3])})"
                          f"{_vepm} - @NHIP.BANGIAO dặn rà sang người mới,"
                          f" mức B")

    # 0m2. Backup NGÀY của X5 mục 7 thành máy: ngày có lượt ghi (mã
    #      G-YYYYMMDD trong NHATKY) mà _lich_su thiếu backup_<ngày> thì mọi
    #      lượt rollback trọn _so của ngày đó không còn bản đỡ. Chỉ LƯU Ý -
    #      khuyến nghị của X5, không kết tội (giám khảo rubric 05).
    if not chua_cai:
        _ngay_ghi = set()
        for _f0m2 in sorted(so.glob("NHATKY_*.md")):
            _ngay_ghi |= set(re.findall(r"\bG-(\d{8})-", doc(_f0m2)))
        _thieu_bk = sorted(
            _ng for _ng in _ngay_ghi
            if not (so / "_lich_su" / f"backup_{_ng}").is_dir())
        if _thieu_bk:
            print(f"        LƯU Ý  0m2: {len(_thieu_bk)} ngày có lượt ghi mà"
                  f" thiếu backup_<ngày> ({_liet(_thieu_bk[:3])}) - X5 mục 7"
                  f" dặn backup ngày; tạo lại từ bản hiện tại, mức A")

    # 0p. Sổ lõi còn KHUNG, không chỉ còn TÊN. Đồng bộ mây hay một lượt AI
    #     ghi đè để lại file 0 byte thì phép 0 vẫn PASS vì nó chỉ hỏi
    #     is_file() - rồi phiên sau nối dòng vào file KHÔNG có header và cột
    #     mất nghĩa vĩnh viễn (hội đồng vòng 20).
    if not chua_cai:
        _mat_khung = []
        for _t0p in SO_CO_GHI_LAN:
            _p0p = so / _t0p
            if not _p0p.is_file():
                continue          # phép 0 lo phần VẮNG
            _nd0p = doc(_p0p)
            if not re.search(r"^\|[\s:|-]+\|$", _nd0p, re.M):
                _mat_khung.append(_t0p)
        for _t0p, _neo0p in (("BANG_DIEU_KHIEN.md", "may_sinh:"),
                             ("X0_INDEX.md", "may_sinh:")):
            _p0p = so / _t0p
            if _p0p.is_file() and _neo0p not in doc(_p0p):
                _mat_khung.append(_t0p)
        bao("0p. sổ lõi còn khung", not _mat_khung,
            f"{_liet(_mat_khung[:5])}: file còn trên đĩa nhưng mất header bảng"
            f" hay khối khai - rất có thể bị đồng bộ hay một lượt ghi đè cắt"
            f" cụt. Lượt sau nối dòng vào file không header là cột mất nghĩa"
            f" VĨNH VIỄN; khôi phục từ bản cũ, mức C")

    idx = doc(so / "X0_INDEX.md")
    if not chua_cai:
        if idx:
            rev_idx = re.search(r"x0_rev:\s*(\d+)", idx)
            bao("2. X0_INDEX đúng rev X0",
                bool(rev and rev_idx and rev.group(1) == rev_idx.group(1)),
                f"X0 rev={rev and rev.group(1)} index={rev_idx and rev_idx.group(1)}")
        else:
            print("  BỎ QUA  2. chưa có X0_INDEX")

    nk = "".join(doc(p) for p in loc_ban_chinh(
        list(so.glob("NHATKY_*.md")) + list((so / "_lich_su").glob("NHATKY_*.md")),
                                               r"NHATKY_\d{4}Q[1-4]\.md"))
    hang_nk = dong_bang(nk)
    ma_cot_dau = [re.sub(r"\*", "", h[0]).strip() for h in hang_nk if h]
    ma_g = [m for m in ma_cot_dau if re.fullmatch(MAU_G, m)]
    wm = watermark(ma_g)

    if not chua_cai:
        # dòng CỤT: đứt giữa lượt ghi ở mức byte (ổ đồng bộ cắt ngang) làm ô
        # Trạng thái mất chữ, so khớp "ĐANG GHI" trượt và "chốt sổ" tuyên bố
        # đóng phiên an toàn trong khi sổ đã mang mã của lượt dở (hội đồng 13)
        so_o_dau = max((len(h) for h in hang_nk), default=0)
        treo = [h[0] for h in hang_nk if any(o == "ĐANG GHI" for o in h)] + [
            (h[0] or "?") + " (dòng CỤT)" for h in hang_nk
            if not any(o == "ĐANG GHI" for o in h)
            and (len(h) < so_o_dau or not (h[7].strip() if len(h) > 7 else "x")
                 or any(o.strip().startswith("ĐANG") and
                        o.strip() != "ĐANG GHI" for o in h))]
        bao("3a. không dòng NHATKY cụt / ĐANG GHI", not treo, str(treo))
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
        ghi_lan, ghi_lan_theo_so = set(), {}
        # đọc CẢ _so\_lich_su\: dòng sổ chuyển lịch sử theo X5 mục 5 (việc XONG
        # quá 30 ngày) vẫn mang mã G. Không quét thì mỗi lượt ghi được lưu trữ
        # ĐÚNG LUẬT đẻ thêm một dòng 3c LỆCH vĩnh viễn (hội đồng vòng 14).
        for t in SO_CO_GHI_LAN:  # THU có cột "Ghi lần" (profile EMAIL): thiếu nó
                                 # thì lượt chỉ chạm THU bị 3c báo LỆCH oan
            nguon = [so / t] + sorted((so / "_lich_su").glob(t.replace(".md", "*.md")))
            for r in [r for p in nguon for r in dong_bang(doc(p))]:
                if r:
                    ma_r = set(re.findall(MAU_G, r[-1]))
                    ghi_lan |= ma_r
                    ghi_lan_theo_so.setdefault(t, set()).update(ma_r)
        # 3c đòi dấu ở ĐÚNG CÁC SỔ mà chính lượt đó khai ở ô "Chạm sổ nào",
        # không phải "ít nhất một sổ": ghi đè ô Ghi lần của MỘT sổ từng đi im
        # trong khi X5 mục 3 bước 3 hứa "3c lệch mãi" (hội đồng vòng 14)
        khong_dau = []
        for h in hang_nk:
            ma = h[0].strip("* ")
            cham = (h[5] if len(h) > 5 else "")
            if not (any(o == "XONG" for o in h) and re.fullmatch(MAU_G, ma)):
                continue
            _cham_kd = bo_dau(cham)
            if "khong" in _cham_kd and "da xoa theo q-" not in _cham_kd:
                continue  # khuôn chuẩn của X5 mục 7b là "không, đã xóa theo
                          # Q-<mã>" - chứa chữ "không", nên nhánh kiểm mã Q-
                          # dưới đây CHẾT đúng trên khuôn chuẩn (vòng 16)
            # X5 mục 7b dặn GỠ TÊN SỔ đó khỏi ô, nên `can` đã tự loại đúng sổ
            # bị xóa: bỏ TRỌN DÒNG là mù luôn các sổ CÒN LẠI mà lượt đó chạm.
            # Hội đồng vòng 15b: gõ chuỗi "đã xóa theo Q-" vào ô là đủ để ghi
            # đè ô Ghi lần của sổ còn lại đi im - đúng lỗ vòng 41 đã đóng, mở
            # lại bởi chính bản vá vòng 43. Mã Q- cũng phải CÓ THẬT.
            _mq = re.search(r"(?:đã|da) xóa theo (Q-[A-Za-z0-9-]+)", cham) \
                or re.search(r"da xoa theo (Q-[A-Za-z0-9-]+)", cham)
            if _mq and not any(_mq.group(1) == o.strip()
                               for rq in dong_bang(doc(so / "QUYETDINH.md"))
                               for o in rq):
                khong_dau.append(f"{ma} khai xóa theo {_mq.group(1)} mà QUYETDINH"
                                 f" không có mã đó")
                continue
            if "khong, da xoa theo q-" in _cham_kd:
                continue  # X5 mục 7b: mất dấu ở MỌI sổ, ô thay trọn
            can = {t for t in SO_CO_GHI_LAN if t.split(".")[0] in cham}
            thieu = sorted(t for t in (can or set()) if ma not in ghi_lan_theo_so.get(t, set()))
            if thieu or (not can and ma not in ghi_lan):
                khong_dau.append(f"{ma}{' thiếu ở ' + str(thieu) if thieu else ''}")
        bao("3c. lượt XONG để dấu mã G ở đúng sổ", not khong_dau,
            str(khong_dau[:5]))

        # 3f. Mọi DÒNG DỮ LIỆU của sổ phải mang ít nhất một mã G ở ô "Ghi lần":
        #     dòng vào sổ ngoài lượt ghi (sửa tay, dán nhầm) trước đây đi im.
        # đọc CẢ _lich_su: 3c, 3d, 3e, 7 và 12l đã học điều này từ vòng 41,
        # 3f thì chưa - dòng thiếu mã G sống nhăn trong file lưu trữ mà bộ vẫn
        # "hệ sạch", mà lưu trữ là nơi hồ sơ nằm LÂU NHẤT (hội đồng vòng 19).
        # PHÉP 6 thì CỐ Ý không đọc _lich_su: nó đếm ngưỡng 500 dòng, và tách
        # sang lưu trữ CHÍNH LÀ cách xử lý ngưỡng đó - cho nó đọc là đẻ ra báo
        # oan không lối thoát. Đừng "sửa cho đều".
        thieu_g_dong = []
        for t in SO_CO_GHI_LAN:
            _dong_t = [_x for _q in [so / t] + sorted(
                (so / "_lich_su").glob(t.replace(".md", "*.md")))
                for _x in dong_bang(doc(_q))]
            for r in _dong_t:
                # PLANNING chưa tới điểm ghi thì ô "Mã ghi" TRỐNG là ĐÚNG: X5 mục
                # 2 cho bốn trạng thái MỚI, ĐANG LÀM, CHỜ CHỐT, HỦY; X5 mục 3 đặt
                # điểm ghi mức C ở "khi chốt"; GHI MỐC giữ plan ĐANG LÀM cả chu
                # kỳ duyệt. Vế ĐÃ GHI đã có phép 4 canh, cách đây mười dòng.
                # Hội đồng vòng 15: thiếu vế này thì MỌI việc mức C đỏ lưới suốt
                # thời gian nó mở - lần thứ ba của lớp lỗi phạt-người-làm-đúng.
                if t == "PLANNING.md" and not any(o.strip() == "ĐÃ GHI" for o in r):
                    continue
                if r and any(o.strip() for o in r) and not re.search(MAU_G, r[-1] or ""):
                    thieu_g_dong.append(f"{t}:{(r[0] or '?').strip()[:20]}")
        bao("3f. mọi dòng sổ mang mã G ở ô Ghi lần", not thieu_g_dong,
            f"{_liet(thieu_g_dong[:5])}: dòng vào sổ NGOÀI lượt ghi (sửa tay hay"
            f" dán nhầm); dựng lại lượt ghi theo X5 mục 3. Dòng ĐÃ có mã mà máy"
            f" không thấy thì kiểm số cột trước (phép 5); TUYỆT ĐỐI không gỡ dòng"
            f" sổ để làm im phép này - xóa dòng chính là thứ phép này sinh ra để"
            f" chặn")

        # 3e. Chiều NGƯỢC của 3c: mã G đã đậu ở sổ hay bảng thì phải có dòng
        #     NHATKY. 3c chỉ đi từ NHATKY ra sổ nên MẤT TRỌN một file quý (mây
        #     rollback, restore lệch, git stash) không lay động phép nào.
        # X0_INDEX cũng mang sinh_boi: loc_dau_vet_ghi TÍNH nó là dấu vết cho
        # 0d, nên 3e không soi là bất đối xứng thuần (hội đồng vòng 15)
        dau_ngoai = (ghi_lan | set(re.findall(MAU_G, doc(so / "BANG_DIEU_KHIEN.md")))
                     | set(re.findall(MAU_G, doc(so / "X0_INDEX.md"))))
        mo_coi = sorted(dau_ngoai - set(ma_g))
        bao("3e. mã G ở sổ có dòng NHATKY", not mo_coi,
            f"{_liet(mo_coi[:5])}: sổ hay bảng mang mã mà NHATKY không có dòng."
            f" Kiểm _so\\_lich_su\\ TRƯỚC (quý cũ tách theo X5 mục 7 là hợp"
            f" lệ); thật sự mất thì dòng NHATKY hay CẢ FILE QUÝ đã bay: khôi"
            f" phục mức C từ {BAN_CU}. [AI: cấm cấp mã G mới]")

        # 3g. Ô Mức và Trạng thái là DỮ LIỆU ĐIỀU KHIỂN, không phải văn xuôi: 3d
        #     chỉ nhìn h[3] == "C" và 3c chỉ nhìn "XONG", nên gõ "c" hay "xong"
        #     là lách TRỌN kỷ luật mức C mà không phép nào kêu - 21/22 ca họ này
        #     đi im (hội đồng vòng 16). 7b đã canh từ vựng cửa và dự án; đây là
        #     vế còn lại của cùng ý tưởng.
        _tv = []
        for h in hang_nk:
            if len(h) > 3 and h[3].strip() and h[3].strip() not in ("A", "B", "C"):
                _tv.append(f"NHATKY {h[0].strip()[:20]}: Mức "
                           + (ta_vo_hinh(h[3].strip(), ("A", "B", "C"))
                              or h[3].strip()))
            if len(h) > 7 and h[7].strip() and h[7].strip() not in ("XONG", "ĐANG GHI"):
                _tv.append(f"NHATKY {h[0].strip()[:20]}: Trạng thái "
                           + (ta_vo_hinh(h[7].strip(), ("XONG", "ĐANG GHI"))
                              or h[7].strip()))
        for _t, _c, _hl in [
                ("VIEC.md", 7, ("MỚI", "ĐANG LÀM", "CHỜ ĐỐI TÁC", "CHỜ DUYỆT",
                                "TREO", "XONG", "HỦY")),
                ("DUKIEN.md", 7, ("A", "B", "C", "D")),
                ("PLANNING.md", 9, ("MỚI", "ĐANG LÀM", "CHỜ CHỐT", "ĐÃ GHI", "HỦY")),
                # THU cũng có từ vựng ĐÓNG mà 3g bỏ sót đúng nó: dòng gõ sai
                # rơi khỏi bộ đếm CHỜ TÔI của bảng và của digest, tức luồng
                # khách đang chờ trả lời biến mất (hội đồng vòng 18)
                ("THU.md", 8, ("CHỜ TÔI", "CHỜ ĐỐI TÁC", "THEO DÕI",
                               "ĐÃ ĐÓNG", "BỎ QUA"))]:
            for _r in [_x for _q in [so / _t] + sorted(
                    (so / "_lich_su").glob(_t.replace(".md", "*.md")))
                    for _x in dong_bang(doc(_q))]:
                if len(_r) <= _c:
                    continue
                _gt = _r[_c].strip()
                # ô Trạng thái RỖNG của THU cũng là lệch: dòng đó rơi khỏi bộ
                # đếm CHỜ TÔI của bảng và của digest, tức luồng khách đang chờ
                # trả lời biến mất khỏi mọi mặt phẳng (hội đồng vòng 18)
                if not _gt and _t != "THU.md":
                    continue
                if _gt not in _hl:
                    _tv.append(f"{_t}:{(_r[0] or '?').strip()[:12]} ô "
                               + (ta_vo_hinh(_gt, _hl) or _gt[:14] or "(rỗng)"))
        bao("3g. ô Mức, Trạng thái đúng từ vựng", not _tv,
            f"{_liet(_tv[:5])}: giá trị ngoài từ vựng làm chính dòng đó TÀNG HÌNH"
            f" với 3c, 3d và mọi bộ đếm của bảng. Sửa về đúng từ vựng X5 mục 2,"
            f" mục 4 và X0 C7; [AI: tuyệt đối không gỡ dòng]")

        # 3h. Ô ngày TRÔNG NHƯ NGÀY mà dem_qua_han KHÔNG đọc được: `30/06/2026`
        #     hay `2026-13-01` làm ngay() trả None và dòng rơi LẶNG LẼ khỏi cả
        #     ba bộ đếm quá hạn / rà lại / hết hạn - hợp đồng trễ 60 ngày mà
        #     bảng vẫn "bàn sạch". Chỉ soi đúng BA CỘT bộ đếm đọc, không đụng
        #     chữ tự do (backlog hội đồng vòng 22).
        import datetime as _dt3h

        def _iso_ok(_o):
            _m = re.search(r"(\d{4})-(\d{2})-(\d{2})", _o)
            if not _m:
                return False
            try:
                _dt3h.date(*map(int, _m.groups()))
                return True
            except ValueError:
                return False

        _ngay_mu = []
        for _t3, _c3 in (("VIEC.md", 6), ("DUKIEN.md", 9), ("TAILIEU.md", 11)):
            for _r in dong_bang(doc(so / _t3)):
                if len(_r) <= _c3 or not _r[_c3].strip():
                    continue
                _o = _r[_c3].strip()
                if _iso_ok(_o):
                    continue
                if re.search(r"\d{1,2}[/.]\d{1,2}[/.]\d{2,4}"
                             r"|\d{1,2}-\d{1,2}-\d{4}"
                             r"|\d{4}[/.]\d{1,2}[/.]\d{1,2}"
                             r"|\d{4}-\d{2}-\d{2}", _o):
                    _ngay_mu.append(f"{_t3}:{(_r[1] or '?').strip()[:12]}"
                                    f" ô {_o[:16]}")
        bao("3h. ô ngày đọc được theo ISO", not _ngay_mu,
            f"{_liet(_ngay_mu[:5])}: máy chỉ đọc YYYY-MM-DD nên dòng này rơi"
            f" LẶNG LẼ khỏi bộ đếm quá hạn / rà lại / hết hạn trong khi người"
            f" vẫn thấy ngày. Ghi lại theo ISO, mức A")

        # 3d (X4 dòng 23): lượt NHATKY mức C phải khớp một plan mang đúng mã G đó
        # X5 mục 5 BẮT chuyển plan ĐÃ GHI quá 30 ngày vào _lich_su: không đọc
        # thư mục đó thì 3d lệch vĩnh viễn - đúng lớp lỗi vòng 41 vừa đóng cho
        # 3c và 3e, tái phát lần thứ tư (hội đồng vòng 15)
        plan_da_ghi = {m for p_pl in [so / "PLANNING.md"]
                       + sorted((so / "_lich_su").glob("PLANNING*.md"))
                       for r in dong_bang(doc(p_pl))
                       if any(o == "ĐÃ GHI" for o in r)
                       for m in re.findall(MAU_G, r[-1])}
        c_khong_plan = [h[0].strip("* ") for h in hang_nk
                        if len(h) > 3 and h[3].strip() == "C"
                        and re.fullmatch(MAU_G, h[0].strip("* "))
                        and h[0].strip("* ") not in plan_da_ghi]
        bao("3d. lượt mức C đều có plan mang mã G", not c_khong_plan,
            str(c_khong_plan[:5]))

        hang_pl = dong_bang(doc(so / "PLANNING.md"))
        thieu_g = [h[0] for h in hang_pl
                   if any(o == "ĐÃ GHI" for o in h) and not re.search(MAU_G, h[-1] or "")]
        cho_chot = [h[0] for h in hang_pl if any(o == "CHỜ CHỐT" for o in h)]
        bao("4. plan ĐÃ GHI có mã G ở cột Mã ghi", not thieu_g, str(thieu_g))
        print(f"        plan CHỜ CHỐT: {cho_chot or 'không'}")

    lech = []
    for p in sorted(so.glob("*.md")):
        # CÙNG hàm tách ô và cùng luật fence với dong_bang: đếm bằng
        # d.count("|") thì ô chứa `\|` thoát (cách DUY NHẤT hợp lệ theo GFM để
        # viết dấu | trong ô) bị tính dôi một cột và phép 5 tố oan. Hai chỗ đọc
        # bảng bằng hai luật khác nhau thì sớm muộn cũng lệch (hội đồng vòng 21)
        lines = ngoai_fence(doc(p))
        for i, d in enumerate(lines[:-1]):
            if d.startswith("|") and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
                so_cot = len(tach_o(d))
                if len(tach_o(lines[i + 1], so_cot)) != so_cot:
                    lech.append((p.name, "dòng kẻ"))
                j = i + 2
                while j < len(lines) and lines[j].startswith("|"):
                    if len(tach_o(lines[j], so_cot)) != so_cot:
                        lech.append((p.name, f"dòng dữ liệu {j + 1}"))
                    j += 1
    bao("5. schema bảng: mọi dòng cùng số cột",
        not lech, str(lech[:5]))

    # 5e. Dấu fence trong sổ phải đóng ĐỦ CẶP. `ngoai_fence` bật cờ và không
    #     bao giờ tắt nếu thiếu dòng đóng, nên mọi dòng còn lại TÀNG HÌNH với
    #     3f, 3g, 5, 5b, 5d, 6, 7, 7b, 7f và bộ đếm quá hạn - trong khi
    #     Markdown vẫn render và người vẫn đọc thấy. Trước vòng 66 hỏng này
    #     KHÔNG TỒN TẠI: bản vá fence đổi một lớp BÁO OAN lấy một lớp TÀNG
    #     HÌNH, mà sổ chỉ-thêm nên số dòng bị nuốt tăng dần (vòng 22).
    _fence_le = []
    for p in sorted(so.glob("*.md")) + sorted((so / "_lich_su").glob("*.md")):
        _treo = _quet_fence(doc(p))[1]
        if _treo:
            _fence_le.append(f"{p.name} dòng {_treo}")
    bao("5e. dấu fence trong sổ đóng đủ cặp", not _fence_le,
        f"{_liet(_fence_le[:4])} mở khối mà chưa đóng: MỌI dòng phía sau TÀNG"
        f" HÌNH với 3f, 3g, 5, 6, 7, 7b, 7f và bộ đếm quá hạn, trong khi"
        f" Markdown vẫn hiện chúng. Thêm dòng đóng ĐÚNG dấu và dài không kém"
        f" dòng mở, mức A")

    # 5d. Mọi bảng trong CÙNG một sổ phải cùng thứ tự cột. X5 cho nhiều khối
    #     `## <KHỐI>` mỗi khối một bảng - đó là cách bộ dặn tách dự án - nhưng
    #     không ai đòi chúng cùng THỨ TỰ, trong khi dem_qua_han, 3g, 7f, 10d và
    #     13m đều đọc theo VỊ TRÍ CỨNG. Đảo hai cột ở khối thứ hai là mọi dòng
    #     vẫn cùng SỐ ô (phép 5 xanh) mà bộ đếm đọc nhầm ô: việc quá hạn 58
    #     ngày biến mất khỏi mọi mặt phẳng, bảng giữ "bàn sạch" (vòng 21).
    _lech_hdr = []
    for p in sorted(so.glob("*.md")) + sorted((so / "_lich_su").glob("*.md")):
        _lines = ngoai_fence(doc(p))
        _hdrs = []
        for _i, _d in enumerate(_lines[:-1]):
            if _d.startswith("|") and re.match(r"^\|[\s:|-]+\|$", _lines[_i + 1]):
                _hdrs.append(tuple(tach_o(_d)))
        if len(set(_hdrs)) > 1:
            _lech_hdr.append(f"{p.name}: {len(set(_hdrs))} thứ tự cột khác nhau")
    bao("5d. bảng trong một sổ cùng thứ tự cột", not _lech_hdr,
        f"{_liet(_lech_hdr[:4])}: các phép đọc sổ theo VỊ TRÍ cột, nên khối"
        f" đảo cột làm bộ đếm quá hạn và từ vựng đọc nhầm ô trong khi phép 5"
        f" vẫn xanh (mọi dòng cùng SỐ ô). Đưa các khối về cùng header; nếu đó"
        f" là bảng VÍ DỤ thì bọc nó trong ``` hay ~~~, mức A")

    # 5b. Dòng thụt SÂU (>=4 dấu cách hay tab) mà trông như dòng bảng: GFM coi
    #     đó là khối code, nên dong_bang KHÔNG đọc nó - và docstring của
    #     dong_bang từ vòng 58 hứa "phép 5b báo riêng chỗ đó" mà phép đó chưa
    #     từng được dựng. Đúng lớp LỜI KHAI VƯỢT CÁI MÁY LÀM mà chiến dịch này
    #     đi diệt, do chính vòng 58 phạm (hội đồng vòng 20).
    _thut_sau = []
    for p in sorted(so.glob("*.md")) + sorted((so / "_lich_su").glob("*.md")):
        for _n, _d in enumerate(ngoai_fence(doc(p)), 1):
            if re.match(r"^(?: {4,}|\t)", _d) and _d.count("|") >= 2:
                _thut_sau.append(f"{p.name}:{_n}")
    bao("5b. không dòng bảng nào bị thụt sâu", not _thut_sau,
        f"{_liet(_thut_sau[:5])}: thụt từ bốn dấu cách trở lên thì mọi phép"
        f" đọc sổ BỎ QUA dòng đó trong khi người và AI vẫn đọc thấy - kể cả khi"
        f" nó lồng trong một mục danh sách. Là VÍ DỤ thì bọc trong ``` hay ~~~"
        f" (5e canh chúng đóng đủ cặp); là dòng sổ THẬT thì mới kéo về sát lề"
        f" trái, vì kéo một dòng ví dụ ra lề là nạp mã ma vào sổ")

    vuot = []
    for p in sorted(so.glob("*.md")):
        n = len(dong_bang(doc(p)))
        if n > 500 or p.stat().st_size > 1_000_000:
            vuot.append((p.name, n, p.stat().st_size))
    bao("6. không sổ nào vượt 500 dòng / 1 MB", not vuot, str(vuot))

    trung_ma = []
    # khuôn mã phải phủ dạng có mã khối, ví dụ Q-DA2-001: khuôn cũ Q-\d+ bỏ sót
    # đúng dạng tự nhiên nhất nên BA sổ không có lưới mã trùng nào. Và đọc CẢ
    # _lich_su: X5 mục 5 BẮT lưu trữ khi sổ vượt 500 dòng, mà mã đã lưu trữ vẫn
    # là mã ĐÃ DÙNG - cấp lại nó làm mọi liên kết cũ trỏ nhầm (hội đồng vòng 16)
    # khuôn VIEC từng BẮT BUỘC đoạn khối trong khi ba sổ kia để tùy chọn, nên
    # V-001 trùng lọt ở sổ NÓNG NHẤT - nơi hai phiên hay cấp mã song song nhất -
    # và 7c cũng mù theo với mã ngắn. Bộ không có chỗ nào bắt mã mang đoạn khối
    for ten, cot, mau in [("VIEC.md", 1, r"V-(?:[A-Z0-9]+-)?\d+"),
                          ("DUKIEN.md", 1, r"D-(?:[A-Z0-9]+-)?\d+"),
                          ("TAILIEU.md", 1, r"T-(?:[A-Z0-9]+-)?\d+"),
                          ("QUYETDINH.md", 0, r"Q-(?:[A-Z0-9]+-)?\d+"),
                          ("PLANNING.md", 0, r"P-\d{8}-\d{2}")]:
        ds = [h[cot] for p_s in [so / ten]
              + sorted((so / "_lich_su").glob(ten.replace(".md", "*.md")))
              for h in dong_bang(doc(p_s)) if len(h) > cot and re.fullmatch(mau, h[cot])]
        t = sorted({m for m in ds if ds.count(m) > 1})
        if t:
            trung_ma.append((ten, t))
    bao("7. không mã trùng ở cột Mã của các sổ", not trung_ma, str(trung_ma))

    # 7c. LIÊN KẾT TREO: X4 dòng 12 khai tường minh "mã trùng, HOẶC liên kết
    #     trỏ mã không tồn tại" là phần DÒ ĐƯỢC BẰNG MÁY, mà phép 7 mới làm nửa
    #     đầu. Đây là lời hứa tài liệu chưa giữ (hội đồng vòng 15).
    if not chua_cai:
        _ma_that, _treo = set(), []
        # gom mã từ ĐÚNG Ô MÃ, không từ trọn dòng: gom trọn dòng thì chính ô
        # liên kết treo tự đưa mã của nó vào tập hợp lệ (bàn thử vòng 43)
        for _t, _c in [("VIEC.md", 1), ("DUKIEN.md", 1), ("TAILIEU.md", 1),
                       ("QUYETDINH.md", 0), ("PLANNING.md", 0)]:
            for _p in [so / _t] + sorted((so / "_lich_su").glob(_t.replace(".md", "*.md"))):
                for _r in dong_bang(doc(_p)):
                    if len(_r) > _c:
                        _ma_that |= set(re.findall(r"\b[VDTQP]-[A-Za-z0-9-]+\b", _r[_c]))
        # PLANNING ô "Việc" (thứ 5) và DUKIEN ô "Nguồn" (thứ 7) cũng là liên
        # kết: treo ở đó thì plan mức C đứng trên một mã việc gãy mà 3d vẫn
        # xanh - nó so mã G, không so mã việc (backlog (h), vòng 55)
        for _t, _cot in [("VIEC.md", -2), ("QUYETDINH.md", -2), ("THU.md", -2),
                         ("PLANNING.md", 4), ("DUKIEN.md", 6)]:
            for _r in dong_bang(doc(so / _t)):
                if len(_r) < abs(_cot) or "[đã xóa theo Q-" in "|".join(_r):
                    continue
                for _m in re.findall(r"\b[VDTQP]-[A-Za-z0-9-]+\b", _r[_cot]):
                    if _m not in _ma_that:
                        _treo.append(f"{_t}:{_m}")
        bao("7c. liên kết trong sổ trỏ mã có thật", not _treo,
            f"{_liet(_treo[:5])}: ô Liên kết, Thay bởi hay Việc liên quan trỏ mã"
            f" không tồn tại ở sổ nào; sửa mã hay gỡ tham chiếu")

    # 7d. PHẠM VI TỔ CHỨC PHẦN MỀM (X0 C2 @DUAN.PHANMEM). Dự án phần mềm
    #     khai THIẾU trường nào thì mọi vận hành liên quan trường đó chạy mù:
    #     không biết repo thì code có thể bị chép vào kho; không biết đâu là
    #     môi trường CHẠY THẬT thì deploy mức C bị hạ nhầm xuống A (X5 mục
    #     1b); không biết nơi giữ secret thì secret rơi vào sổ hay _INBOX.
    #     Đây là lý do bộ bắt khai ngay ở phiên cài đặt, X9 mục 1 câu 3.
    if not chua_cai and x0s:
        _x0c2 = doc(x0s[0])
        _c2 = cat_muc(_x0c2, 2)
        _pm = _c2[_c2.find("@DUAN.PHANMEM"):] if "@DUAN.PHANMEM" in _c2 else ""
        _dong_pm, _ma_pm, _thieu_pm = _pm.splitlines(), [], []
        _host_pm = []   # GIÁ TRỊ nơi chạy thật, để 7g đọc lại
        _nhanh_pm = []  # GIÁ TRỊ nhánh tự deploy, cũng để 7g đọc lại
        _db_pm = []     # tên ĐÍCH DANH CSDL chạy thật (rubric 03)
        _pt_pm = []     # tên NGƯỜI phụ trách vận hành - 7g nêu thẳng ai gật
        for _i, _dg in enumerate(_dong_pm):
            # KHÔNG đòi 2-6 ký tự HOA: không văn bản nào của bộ khai luật
            # đó, mà mã ngoài khuôn ngầm làm công ty khai ĐÚNG bị 7d và
            # 7d2 buộc tội, còn công ty khai THIẾU thì nhận đúng thông
            # điệp ấy - lời hứa của README sai cả hai chiều (vòng 16)
            _m = re.match(r"^  ([A-Za-z0-9][A-Za-z0-9_.-]{0,23})  +\S", _dg)
            if not _m:
                continue
            _khoi_pm = _dg
            for _kx in _dong_pm[_i + 1:]:
                # dòng NỐI của một khai báo thụt SÂU hơn (4 dấu cách trở lên);
                # dòng định nghĩa cú pháp của template chỉ thụt 2, nên không bị
                # gom nhầm vào khai báo thật rồi cho đủ từ khóa oan
                if not re.match(r"^ {3,}\S", _kx) or "<MÃ PM>" in _kx or "<tên>" in _kx:
                    break
                _khoi_pm += " " + _kx.strip()
            _ma_pm.append(_m.group(1))
            # GIÁ TRỊ nơi chạy thật: "chạy thật app.cty.vn" -> app.cty.vn.
            # Bỏ qua "chưa rõ" (đó là khai hợp lệ tạm thời, 7d đã lo).
            # bắt TRỌN vế sau "chạy thật" rồi nhặt MỌI token dạng domain:
            # re.search một host làm "app.tst.vn va api.tst.vn" chỉ neo host
            # đầu, deploy lên host thứ hai lọt cả 7g cứng lẫn lưới mềm
            # (giám khảo rubric vòng 03)
            _mh = re.search(r"(?:nơi\s+)?ch[ạa]y\s+th[ậa]t\s*:?\s*([^·\n]+)",
                            _khoi_pm)
            if _mh:
                _host_pm += [_h.rstrip(".,;·") for _h in re.findall(
                    r"[A-Za-z0-9][A-Za-z0-9_-]*(?:\.[A-Za-z0-9_-]+)+",
                    _mh.group(1))]
                # máy chủ NỘI BỘ không có dấu chấm ("VPS-01", "prod2"):
                # token đơn chỉ vào neo khi mang CHỮ SỐ hay dấu gạch - từ
                # tiếng Việt thường ("chưa rõ", "máy chủ") đứng ngoài
                # (giám khảo rubric 05)
                _host_pm += [_h for _h in re.findall(
                    r"(?<![\w.-])([A-Za-z][A-Za-z0-9-]{2,})(?![\w.])",
                    _mh.group(1))
                    if re.search(r"[0-9-]", _h)]
            _mpt = re.search(r"(?:ph[ụu] tr[áa]ch(?:\s+v[ậa]n h[àa]nh)?"
                             r"|owner|on-?call)\s*:?\s*([^·\n]+)",
                             _khoi_pm, re.I)
            if _mpt and not re.search(r"(?i)ch[ưu]a r[õo]", _mpt.group(1)):
                _ten_pt = _mpt.group(1).strip().rstrip(".,;·")
                if _ten_pt:
                    _pt_pm.append(_ten_pt[:30])
            _mdb = re.search(r"(?:csdl|c[ơo] s[ởo] d[ữu] li[ệe]u"
                             r"|kho d[ữu] li[ệe]u|database|\bdb\b)"
                             r"\s*(?:ch[ạa]y\s+th[ậa]t)?\s*:?\s*([^·\n]+)",
                             _khoi_pm, re.I)
            if _mdb and not re.search(r"(?i)ch[ưu]a r[õo]", _mdb.group(1)):
                _ten_db = _mdb.group(1).strip().rstrip(".,;·")
                if _ten_db:
                    _db_pm.append(_ten_db[:40])
            _mb = re.search(r"nh[áa]nh\s+t[ựu]\s+deploy[^·]*?"
                            r"(?:th[ậa]t\s+)?([A-Za-z0-9][\w./-]*)\s*(?:·|$)",
                            _khoi_pm)
            if _mb and not re.search(r"(?i)kh[ôo]ng c[óo]", _mb.group(0)):
                _nhanh_pm.append(_mb.group(1).rstrip(".,;"))
            # nhận CẢ bản có dấu lẫn không dấu: người Việt gõ cả hai kiểu, dò
            # mỗi bản có dấu là phạt oan công ty gõ "chay that" (bàn thử vòng 45)
            _can_pm = [("repo", r"repo\s*[:=]?\s*\S"),
                       ("thành phần chính",
                        r"thành phần|thanh phan|gồm|gom|\bweb\b|\bapi\b"
                        r"|máy chủ|may chu|mobile|\bapp\b"),
                       ("môi trường (dev, staging hay prod)",
                        r"dev|staging|prod|môi trường|moi truong"),
                       ("nơi chạy thật", r"chạy thật|chay that"),
                       ("nơi giữ secret", r"secret|bí mật|bi mat"),
                       # X5 mục 1b BẮT phân biệt "merge vào nhánh mà CI/CD tự
                       # deploy chạy thật là C", mà schema không có ô nào khai
                       # nhánh đó: luật gác đúng chỗ hiểm nhưng phụ thuộc một
                       # dữ kiện bộ không bao giờ hỏi, nên MỌI lượt merge rơi
                       # về mức A theo mặc định thực tế (hội đồng vòng 18)
                       ("nhánh tự deploy chạy thật",
                        r"nhánh tự deploy|nhanh tu deploy|auto-?deploy"),
                       # update bảng giá trên CSDL khách là mức C theo X5 mục
                       # 1 mà máy không có neo nào nếu không hỏi tên (rubric 03)
                       ("CSDL/kho dữ liệu chạy thật",
                        r"csdl|cơ sở dữ liệu|co so du lieu|kho dữ liệu"
                        r"|kho du lieu|database|\bdb\b"),
                       # lượt mức C mà không biết hỏi AI GẬT thì "plan và cái
                       # gật TRƯỚC" là cái gật của không ai cả (vế TỔ CHỨC
                       # của phạm vi phần mềm - hạ tầng và dữ liệu đã có neo)
                       ("người phụ trách vận hành",
                        r"phụ trách|phu trach|owner|chịu trách nhiệm"
                        r"|chiu trach nhiem|on-?call")]
            # Bỏ đoạn "repo ..." ra trước khi dò BỐN trường còn lại: khai
            # báo phân đoạn bằng dấu ·, mà dò từ khóa trên TRỌN dòng thì
            # trường này ăn ké chữ của trường kia - `repo git.cty.vn/app` một
            # mình từng thỏa luôn cả "thành phần chính" nên công ty bỏ trống
            # trường đó vẫn xanh (hội đồng vòng 16, mục cuối còn mở của họ)
            _ngoai_repo = " · ".join(
                _d for _d in _khoi_pm.split("·")
                if not re.match(r"\s*repo\b", _d, re.I))
            _hut = [_ten for _ten, _mau in _can_pm
                    if not re.search(_mau, _khoi_pm if _ten == "repo"
                                     else _ngoai_repo, re.I)]
            if _hut:
                _thieu_pm.append(f"{_m.group(1)} thiếu: {', '.join(_hut)}")
        # QUÊN KHAI HẲN: C2 có dự án đang chạy và sổ đầy dấu vết làm phần mềm
        # mà @DUAN.PHANMEM trống trơn - cả chuỗi mức duyệt repo của X5 mục 1b
        # không kích hoạt được, deploy chạy thật bị xử như việc nhẹ (vòng 16)
        if not _ma_pm:
            # chỉ dò DÒNG DỮ LIỆU: văn xuôi mẫu của sổ vốn đã nhắc "Repo"
            # (TAILIEU khai bốn dạng ô "Ở đâu"), dò trọn file là báo oan mọi
            # kho lành - bàn thử vòng 46 bắt được ngay lượt đầu
            _dau_pm = re.search(
                r"(?i)\brepo\b|\bdeploy\b|\bnhánh\b|\bbranch\b|\bcommit\b"
                r"|\bstaging\b|\bprod\b",
                " ".join("|".join(_r) for _t in SO_CO_GHI_LAN
                         for _r in dong_bang(doc(so / _t))))
            if _dau_pm:
                _thieu_pm.append("@DUAN.PHANMEM chưa khai dòng nào, trong khi sổ đã"
                                 " có dấu vết làm phần mềm")
        bao("7d. dự án phần mềm khai đủ phạm vi",
            not _thieu_pm,
            f"{' · '.join(_thieu_pm[:3])}. Thiếu trường nào thì vận hành liên quan"
            f" trường đó chạy mù: không rõ repo thì code có thể bị chép vào kho;"
            f" không rõ đâu là môi trường CHẠY THẬT thì deploy đáng lẽ mức C bị"
            f" hạ xuống A (X5 mục 1b); không rõ nơi giữ secret thì secret rơi"
            f" vào sổ hay _INBOX. CHƯA BIẾT CŨNG KHAI ĐƯỢC: gõ đúng tên trường"
            f" kèm chữ \"chưa rõ\" (ví dụ \"secret chưa rõ\") thì rà thôi đỏ, AI"
            f" đưa mục đó vào danh sách còn thiếu ở X0 C12 để hỏi lại sau; mức B")

        # dòng TAILIEU dạng "Repo" chỉ hợp lệ khi công ty CÓ khai phần mềm
        # 7d2 từng chỉ nổ khi C2 chưa khai phần mềm NÀO, nên công ty khai một
        # dự án rồi là cổng khóa vĩnh viễn ở trạng thái xanh: dòng "Repo KIOT"
        # trỏ mã KHÔNG có trong danh sách khai vẫn PASS. Nhận dự án phần mềm
        # thứ hai là chuyện tháng thứ ba, không phải ngoại lệ (vòng 17).
        _repo_mo_coi = []
        for _r in dong_bang(doc(so / "TAILIEU.md")):
            if len(_r) > 5 and _r[5].strip().startswith("Repo "):
                _pm_o = _r[5].strip()[5:].split()
                if not _ma_pm or (_pm_o and _pm_o[0] not in _ma_pm):
                    _repo_mo_coi.append((_r[1] if len(_r) > 1 else "?").strip()
                                        + (f" (Repo {_pm_o[0]})" if _pm_o else ""))
        if _repo_mo_coi:
            bao("7d2. Repo thuộc dự án có khai phần mềm",
                False, f"{_liet(_repo_mo_coi[:3])}: cột \"Ở đâu\" dạng Repo chỉ"
                f" cho dòng thuộc dự án ĐÃ khai @DUAN.PHANMEM (X0 C1)."
                f" Đang khai: {_liet(_ma_pm) or 'chưa dự án nào'}. Khai phạm vi"
                f" tổ chức của dự án đó trước, mức B")

        # 7g. GIÁ TRỊ khai ở @DUAN.PHANMEM phải ĐIỀU KHIỂN mức duyệt, không
        #     chỉ nằm đó cho đẹp. Đây là vế thi hành của X5 mục 1 MẶC ĐỊNH
        #     ĐÓNG: động từ sản xuất GIAO với neo chạy thật thì lượt đó là C.
        #     Trước 7g, ba thao tác hiểm nhất của công ty phần mềm - deploy
        #     prod, sửa dữ liệu khách trên CSDL thật, merge kích hoạt
        #     auto-deploy - đều ghi mức A mà bộ vẫn in "hệ sạch" (vòng 17).
        # tiếng VIỆT là ngôn ngữ chính của bộ: bản cũ chỉ liệt động từ tiếng
        # Anh nên sáu cách viết tự nhiên nhất đều lọt (hội đồng vòng 19)
        _dv = (r"(?i)\bdeploy\b|\bmigration\b|\brollback\b|\brestore\b"
               r"|\bdump\b|\bdrop\b|\btruncate\b|\bforce[- ]push\b"
               r"|\bupdate\b|\bdelete\b|\bmerge\b|xoay khóa|xoay khoa"
               r"|thu hồi secret|thu hoi secret|feature flag"
               r"|x[óo]a|xo[áa]|kh[ôo]i ph[ụu]c|ph[ụu]c h[ồo]i"
               r"|đ[ẩa]y b[ảa]n|day ban|đ[ẩa]y l[êe]n|day len"
               r"|tri[ểe]n khai|trien khai|c[ậa]p nh[ậa]t|cap nhat"
               r"|s[ửu]a d[ữu] li[ệe]u|sua du lieu|g[ộo]p nh[áa]nh|gop nhanh"
               r"|ph[áa]t h[àa]nh|phat hanh|đ[ưu]a b[ảa]n|dua ban"
               r"|đ[ưu]a l[êe]n|dua len|\bsquash\b|\brelease\b|go[- ]live"
               r"|\bhotfix\b|s[ửu]a n[óo]ng|sua nong"
               r"|l[ấa]y b[ảa]n sao|lay ban sao|b[ậa]t c[ờo]|t[ắa]t c[ờo]"
               r"|c[ấa]p quy[ềe]n|cap quyen|thu h[ồo]i quy[ềe]n")
        _neo = [r"ch[ạa]y\s+th[ậa]t", r"(?<![\w-])prod(uction)?(?![\w-])"] + [
            "(?<![\\w.-])" + re.escape(_h) for _h in _host_pm] + [
            re.escape(_d) for _d in _db_pm]
        # merge vào ĐÚNG nhánh tự deploy là chạm chạy thật, dù câu ghi không
        # nhắc chữ nào về production - đó là cả lý do trường này tồn tại
        # nhận cả KHÔNG DẤU: danh sách động từ _dv cố ý nhận "gop nhanh"
        # mà neo nhánh lại đòi "gộp" có dấu - kiểu gõ phổ biến nhất lọt mức
        # thấp ở đúng lượt merge vào nhánh tự deploy (giám khảo rubric 01)
        _neo += [r"(?:merge|g[ộo]p|đ[ẩa]y l[êe]n|day len|đ[ưu]a|dua"
                 r"|\bsquash\b|\brebase\b)[^·]*?(?<![\w.-])"
                 + re.escape(_b) + r"(?![\w.-])"
                 for _b in _nhanh_pm]
        _sx = []
        for _r in hang_nk:
            if len(_r) < 5:
                continue
            _lg, _muc = _r[4], _r[3].strip()
            if _muc == "C" or not re.search(_dv, _lg):
                continue
            if any(re.search(_n, _lg, re.I) for _n in _neo):
                _sx.append(f"{(_r[0] or '?').strip()[:22]} (mức {_muc or 'trống'})")
        bao("7g. chạm CHẠY THẬT phải ghi mức C", not _sx,
            f"{_liet(_sx[:4])}: ô \"Làm gì\" có động từ sản xuất GIAO với nơi"
            f" chạy thật khai ở X0 C2"
            f"{' (' + _liet(_host_pm[:2]) + ')' if _host_pm else ''} mà lượt"
            f" ghi KHÔNG ở mức C. X5 mục 1 MẶC ĐỊNH ĐÓNG: chạm chạy thật cần"
            f" plan và cái gật TRƯỚC"
            f"{' của ' + _liet(_pt_pm[:2]) if _pt_pm else ''}. Việc trên"
            f" staging hay đã có plan thì sửa ô Mức về C và nối mã plan;"
            f" [AI: không tự hạ mức]")
        # Lưới MỀM cho động từ chưa vào danh sách: hai vòng rubric liền phát
        # hiện lớp lỗ này bằng động từ MỚI (gop, phat hanh, squash...). Câu
        # mức A/B nhắc ĐÍCH DANH host/nhánh đã khai mà máy không nhận ra động
        # từ nào thì KHÔNG kết tội (họp, xem, bàn về prod là hợp lệ) - chỉ in
        # LƯU Ý tự soát, để động từ thứ N+1 không lọt trong im lặng tuyệt đối.
        # neo CHỮ (prod, chạy thật) cũng vào lưới mềm: "push ban moi len
        # prod" - động từ lạ + chữ suông - trước im tuyệt đối (rubric 03)
        _tu_soat = [f"{(_r[0] or '?').strip()[:22]}"
                    for _r in hang_nk
                    if len(_r) >= 5 and _r[3].strip() != "C"
                    and not re.search(_dv, _r[4])
                    and any(re.search(_n, _r[4], re.I) for _n in _neo)]
        if _tu_soat:
            print(f"        LƯU Ý  7g: {_liet(_tu_soat[:3])} mức A/B nhắc"
                  f" đích danh nơi chạy thật/nhánh tự deploy mà máy không"
                  f" nhận ra động từ sản xuất nào - nếu lượt đó CÓ chạm thật"
                  f" thì đổi mức C; chỉ nhắc tới thì thôi")

    # 7e. SECRET không được nằm trong sổ. X5 mục 1b cấm secret ở kho đồng bộ,
    #     ở sổ và ở _INBOX; trước vòng 46 không phép nào canh điều đó.
    if not chua_cai:
        _lo = []
        for _t in SO_CO_GHI_LAN:
            for _r in dong_bang(doc(so / _t)):
                for _o in _r:
                    if MAU_SECRET.search(_o or ""):
                        _ma_d = next((c.strip() for c in _r
                                      if re.match(r"[VDTQPG]-", c.strip())),
                                     (_r[0] or "?").strip())
                        _lo.append(f"{_t}:{_ma_d[:20]}")
                        break
        bao("7e. secret không lọt vào sổ", not _lo,
            f"{_liet(sorted(set(_lo))[:5])}: X5 mục 1b cấm secret nằm trong kho"
            f" đồng bộ, trong sổ và trong _INBOX. THU HỒI và xoay khóa TRƯỚC, gỡ"
            f" khỏi sổ sau; sổ chỉ mô tả LOẠI secret và hệ liên quan, không bao"
            f" giờ chứa giá trị. Việc mức C")

    # 7e3. _INBOX và NỘI DUNG file. X5 mục 1b cấm secret ở kho, ở sổ VÀ ở
    #      _INBOX; 7e soi ô sổ, 7e2 soi TÊN file ngoài 00_Index, còn hai lối
    #      tự nhiên nhất thì chưa ai soi: file .env đối tác gửi rơi vào _INBOX,
    #      và file bàn giao môi trường viết thẳng chuỗi kết nối prod trong RUỘT
    #      (hội đồng vòng 17: cả hai "hệ sạch", lối thứ hai còn được MỜI vào sổ)
    _lo_ib = []
    # rglob chứ không glob: .env nằm trong THƯ MỤC CON của _inbox từng lọt
    # trọn (hội đồng vòng 19)
    for _thu in (so / "_inbox",):
        if not _thu.is_dir():
            continue
        for _f in sorted(_thu.rglob("*")):
            if not _f.is_file() or MAU_FILE_MAU.search(_f.name):
                continue
            _rel_ib = _f.relative_to(so).as_posix()
            if MAU_FILE_SECRET.search(_f.name):
                _lo_ib.append(f"{_rel_ib} (tên file)")
                continue
            try:
                if _f.stat().st_size > 256 * 1024:
                    continue
                if MAU_SECRET.search(_f.read_text(encoding="utf-8",
                                                  errors="ignore")):
                    _lo_ib.append(f"{_rel_ib} (giá trị trong ruột file)")
            except OSError:
                pass
    bao("7e3. secret không ở _INBOX", not _lo_ib,
        f"{_liet(_lo_ib[:5])}: _INBOX vẫn là kho đồng bộ, file nằm đó đã đi ra"
        f" mọi máy của công ty. Xoay khóa TRƯỚC, chuyển ra ngoài kho sau. Mức C")

    # 7b2. XÓA PHÁP LÝ phải LAN. X5 mục 7b bắt thay ô dữ liệu của dòng
    #      TAILIEU VÀ THU trỏ file đã xóa bằng [đã xóa theo Q-<mã>]. Bỏ sót
    #      dòng THU thì công ty trả lời khách "đã xóa xong" trong khi sổ còn
    #      tên đối tác, tiêu đề luồng, Message-ID và sha256 của file (vòng 17).
    _ma_mo = set()
    for _t7 in SO_CO_GHI_LAN:
        for _r in dong_bang(doc(so / _t7)):
            if "[đã xóa theo Q-" in "|".join(_r):
                _mm = next((c.strip() for c in _r
                            if re.match(r"^[VDTQP]-[A-Za-z0-9-]+$", c.strip())), "")
                if _mm:
                    _ma_mo.add(_mm)
    _sot = []
    if _ma_mo:
        for _t7 in SO_CO_GHI_LAN:
            for _r in dong_bang(doc(so / _t7)):
                _van = "|".join(_r)
                if "[đã xóa theo Q-" in _van:
                    continue
                for _mm in _ma_mo:
                    if re.search(r"(?<![A-Za-z0-9-])" + re.escape(_mm)
                                 + r"(?![A-Za-z0-9-])", _van):
                        _sot.append(f"{_t7}:{(_r[0] or '?').strip()[:14]}"
                                    f" còn trỏ {_mm}")
                        break
    bao("7b2. xóa pháp lý lan mọi dòng trỏ nó",
        not _sot, f"{_liet(_sot[:4])}: dòng đó vẫn giữ dữ liệu của khách -"
        f" tên đối tác, tiêu đề luồng, Message-ID, sha256 - trong khi công ty"
        f" đã trả lời là đã xóa. Trung hòa NỐT theo X5 mục 7b, giữ khung dòng"
        f" và ô Ghi lần; cùng lượt ghi. Mức C")

    # 7f. Ô "Ở đâu" chỉ nhận NĂM DẠNG khai ở X0 C1. Đây KHÔNG phải lỗi trình
    #     bày: bộ quan sát lọc dòng bằng h[5].startswith("Kho "), nên gõ "kho "
    #     thường, "Kho:", hay bỏ hẳn tiền tố là TẮT LẶNG LẼ phép 9, 10a và 10b
    #     cho đúng tài liệu đó. Đo vòng 47: hợp đồng ĐÃ KÝ bị sửa đè tại chỗ -
    #     đúng thứ luật cốt lõi 3 sinh ra để bắt - đi im ở 4/5 cách gõ đời thực.
    _sai_khuon = []
    for _r in dong_bang(doc(so / "TAILIEU.md")):
        _o = (_r[5] if len(_r) > 5 else "").strip().strip("`").strip()
        if not _o or _o.startswith("[đã xóa theo Q-"):
            continue          # ô TRỐNG là dòng chưa đặt chỗ; tombstone là thứ
            # X5 mục 7b BẮT ghi vào đúng ô này khi tên file mang dữ liệu cá
            # nhân - 8e và 12k đã miễn nó, 7f quên (hội đồng vòng 19)
        # so bằng \s sau TÊN DẠNG: bản cũ để "Kho cũ E:\..." lách vào dạng
        # "Kho" rồi bị phép 9 tố mất file (hội đồng vòng 19)
        if not re.match(r"(Kho|KhoCu|Project|Drive|Repo)\s\S", _o):
            _sai_khuon.append(f"{(_r[1] if len(_r) > 1 else '?').strip()[:14]}:"
                              f" {_o[:30]}")
    bao("7f. ô \"Ở đâu\" thuộc các dạng X0 C1", not _sai_khuon,
        f"{_liet(_sai_khuon[:5])}: X0 C1 cho ĐÚNG năm dạng - Kho · KhoCu · Project ·"
        f" Drive · Repo. Sai khuôn thì phép 9, 10a, 10b BỎ QUA dòng này: tài"
        f" liệu trông như được theo dõi mà không có lưới toàn vẹn nào, hợp"
        f" đồng đã ký bị sửa đè vẫn im. Sửa về đúng khuôn, mức A")

    # 13m. QUYETDINH: ô "Thay bởi" và ô "Trạng thái" là một CẶP (X5 mục 4).
    #      Dòng tự khai người kế nhiệm mà vẫn đứng HIỆN HÀNH thì sổ có hai
    #      quyết định nói ngược nhau về cùng một việc, và phiên sau lấy dòng
    #      nào cũng "đúng sổ" - đúng thứ DUY NHẤT sổ này tồn tại để chặn (hội
    #      đồng vòng 19). Tất định cả hai chiều, không suy luận nội dung.
    if not chua_cai:
        _hang_qd = dong_bang(doc(so / "QUYETDINH.md"))
        _ma_qd = {(_r[0] or "").strip() for _r in _hang_qd}
        _cap_qd = []
        for _r in _hang_qd:
            if len(_r) < 7 or "[đã xóa theo Q-" in "|".join(_r):
                continue
            _tt, _tb = _r[5].strip().upper(), _r[6].strip()
            _co_tb = bool(re.fullmatch(r"Q-[A-Za-z0-9-]+", _tb)) and _tb in _ma_qd
            if _co_tb and _tt != "ĐÃ THAY":
                _cap_qd.append(f"{(_r[0] or '?').strip()} khai Thay bởi {_tb}"
                               f" mà Trạng thái là {_tt or '(rỗng)'}")
            elif _tt == "ĐÃ THAY" and not _co_tb:
                _cap_qd.append(f"{(_r[0] or '?').strip()} ĐÃ THAY mà ô Thay bởi"
                               f" không trỏ quyết định có thật")
        bao("13m. Trạng thái QUYETDINH khớp Thay bởi", not _cap_qd,
            f"{_liet(_cap_qd[:3])}: hai quyết định cùng HIỆN HÀNH về một việc"
            f" thì phiên sau lấy dòng nào cũng 'đúng sổ'. Đánh ĐÃ THAY cho dòng"
            f" cũ, mức A")

    # 7h. Profile AUTOMATED: lượt máy TỰ LÀM chỉ được mức A. X5 mục 1 khối
    #     KHÔNG NGƯỜI cấm B và C ghi sổ, gửi, hay update ngược X0 - và chính X5
    #     nói ô Phiên dạng <CỬA>.AUTO.<giờ phút> là dấu DUY NHẤT phân biệt việc
    #     máy với việc người. Dấu đó có, máy đọc được, mà trước vòng 59 không
    #     phép nào đọc: phiên hẹn giờ ban đêm phát hành công văn đòi tiền chủ
    #     đầu tư ở mức C vẫn "hệ sạch" (hội đồng vòng 19).
    if not chua_cai and x0s and re.search(r"\[x\]\s*AUTOMATED", doc(x0s[0])):
        _auto_sai = []
        for _r in hang_nk:
            if len(_r) < 5 or not re.match(r"^[A-Z0-9]+\.AUTO\.", _r[2].strip()):
                continue
            if _r[3].strip().upper() in ("B", "C"):
                _auto_sai.append(f"{(_r[0] or '?').strip()[:22]} mức"
                                 f" {_r[3].strip()}: {_r[4].strip()[:40]}")
        bao("7h. lượt phiên AUTOMATED chỉ ghi mức A", not _auto_sai,
            f"{_liet(_auto_sai[:3])}: X5 mục 1 KHÔNG NGƯỜI cho phiên hẹn giờ"
            f" mức B và C CHUẨN BỊ thôi - xếp bảng chờ duyệt và mở dòng VIEC"
            f" hạn phiên sau; ngoài dòng đó không ghi sổ, không gửi, không"
            f" update ngược X0. Lượt đã lỡ: ghi QUYETDINH và để người duyệt"
            f" xác nhận sau việc, mức C")

    # 7b. TỪ VỰNG của sổ phải nằm trong X0: cửa ma (gõ nhầm một ký tự là sinh
    #     một lane watermark mới) và dự án ĐÃ NGỪNG còn việc mở (X0 C2 bắt
    #     chuyển HỦY hay bàn giao TRƯỚC khi đóng, mà việc đó rơi khỏi bàn làm
    #     việc và digest nên thành VIỆC VÔ HÌNH) - hội đồng vòng 14.
    if x0s and not chua_cai:
        _x0nd = doc(x0s[0])
        _c1 = cat_muc(_x0nd, 1)
        _c2 = cat_muc(_x0nd, 2)
        _cua_khai = set(re.findall(r"\b(CUA\d+)\b", _c1))
        _da_khai = {m.group(1) for m in re.finditer(r"@DUAN\.([A-Z0-9]+)", _c2)
                    if m.group(1) != "PHANMEM"}
        _ngung = {m.group(1) for m in re.finditer(r"@DUAN\.([A-Z0-9]+)[^\n]*NGỪNG", _c2)}
        # NGỪNG (bảo hành tới <ngày>): dự án đã thanh lý mà nghĩa vụ còn chạy.
        # Không có lối này thì công ty phải chọn giữa hai lời khai SAI - chuyển
        # việc bảo hành sang HỦY, hay giữ dự án "đang chạy" cả năm sau khi xong
        # (hội đồng vòng 19). Hết hạn bảo hành thì 7b tố lại, vì lúc đó việc
        # còn mở mới thật sự là việc bị bỏ quên.
        import datetime as _dt62
        _bao_hanh = {}
        for _m62 in re.finditer(r"@DUAN\.([A-Z0-9]+)[^\n]*NGỪNG[^\n]*?"
                                r"b[ảa]o h[àa]nh[^\n]*?(\d{4})-(\d{2})-(\d{2})",
                                _c2):
            try:
                _bao_hanh[_m62.group(1)] = _dt62.date(
                    *map(int, _m62.group(2, 3, 4)))
            except ValueError:
                pass
        _hom_nay62 = _dt62.date.today()
        _ngung = {_d for _d in _ngung
                  if not (_d in _bao_hanh and _bao_hanh[_d] >= _hom_nay62)}
        _la_cua = {c for m in ma_g if (c := cua_cua(m)) and c not in _cua_khai}
        # ô "Phiên" (<CỬA>.<giờ phút>.<hậu tố>, X5 mục 3 bước 1) và dòng watermark
        # của bảng (bước 6) cũng mang tên cửa: gõ nhầm ở đó sinh đúng cái "lane
        # watermark giả" mà phép này lấy làm lý do tồn tại (hội đồng vòng 15)
        _la_cua |= {c for h in hang_nk if len(h) > 2
                    for c in re.findall(r"\b(CUA\d+)\b", h[2]) if c not in _cua_khai}
        _wm = re.search(r"watermark:\s*(.+)", bdk_nd or "")
        _la_cua |= {c for c in re.findall(r"\b(CUA\d+)\b", _wm.group(1) if _wm else "")
                    if c not in _cua_khai}
        _la_cua = sorted(_la_cua)
        _la_da, _mo_ngung = set(), []
        for _r in dong_bang(doc(so / "PLANNING.md")):  # cột Dự án là ô thứ ba
            if len(_r) > 2 and (_d := _r[2].strip()) and _da_khai and _d not in _da_khai \
                    and re.fullmatch(r"[A-Z0-9]{2,6}", _d):
                _la_da.add(f"PLANNING.md:{_d}")
        for _t in ["VIEC.md", "DUKIEN.md", "TAILIEU.md"]:
            for _r in dong_bang(doc(so / _t)):
                if not _r or not _r[0].strip():
                    continue
                _d = _r[0].strip()
                if _da_khai and _d not in _da_khai and re.fullmatch(r"[A-Z0-9]{2,6}", _d):
                    _la_da.add(f"{_t}:{_d}")
                if _t == "VIEC.md" and _d in _ngung and any(
                        o.strip() in ("MỚI", "ĐANG LÀM", "CHỜ ĐỐI TÁC", "CHỜ DUYỆT", "TREO")
                        for o in _r):
                    _mo_ngung.append(f"{_d}:{_r[1].strip() if len(_r) > 1 else '?'}")
        _loi7b = ([f"cửa không khai ở C1: {_la_cua}"] if _la_cua else []) \
            + ([f"dự án không khai ở C2: {_liet(sorted(_la_da)[:3])}"] if _la_da else []) \
            + ([f"dự án NGỪNG còn việc mở: {_liet(_mo_ngung[:3])}"] if _mo_ngung else [])
        bao("7b. từ vựng sổ (cửa, dự án) khai ở X0", not _loi7b,
            "; ".join(_loi7b) + " - cửa THU HỒI thì khai xuống @KHO.CUA_NGUNG"
            " (X0 C1), đừng gỡ trắng: mã G cũ nằm trong NHATKY chỉ-thêm nên"
            " không xóa được. Gõ nhầm một ký tự cũng sinh cửa ma và một lane"
            " watermark giả; dự án NGỪNG còn việc mở thì việc đó rơi khỏi bàn"
            " làm việc mà không ai đóng (X0 C2) - còn nghĩa vụ bảo hành thì"
            " khai \"NGỪNG (bảo hành tới YYYY-MM-DD)\", đừng chuyển việc sang"
            " HỦY cho im")

    if not chua_cai:
        bdk = doc(so / "BANG_DIEU_KHIEN.md")
        g_bdk = re.search(r"sinh_boi:\s*(" + MAU_G + r")", bdk)
        if not ma_g:
            print("  BỎ QUA  8. chưa có lượt ghi nào trong NHATKY")
        else:
            gb = g_bdk.group(1) if g_bdk else None
            c = cua_cua(gb) if gb else None
            # hai chiều lệch phải nói hai câu KHÁC nhau: bảng CŨ hơn thì sinh
            # lại là đúng; bảng MỚI hơn mọi dòng NHATKY của chính cửa mình thì
            # NHATKY đã mất dòng, sinh lại bảng là XÓA BẰNG CHỨNG CUỐI CÙNG
            # (hội đồng vòng 13: phép cũ dẫn thẳng người dùng tới thao tác đó)
            moi_hon = bang_moi_hon(gb, c, wm)
            if not gb or not c:
                bao("8. BANG_DIEU_KHIEN sinh từ watermark cửa nó", False,
                    "bảng chưa khai sinh_boi hay watermark mang mã G có cửa:"
                    " bảng sinh TRƯỚC lượt ghi đầu tiên thì ghi \"cai dat\"; bảng"
                    " sinh SAU một lượt ghi mà thiếu hai giá trị này là bảng sửa"
                    " tay, sinh lại theo X5 mục 3 bước 6")
            else:
             bao("8. BANG_DIEU_KHIEN sinh từ watermark cửa nó",
                bool(gb and c and wm.get(c) == gb),
                (f"bảng={gb} MỚI HƠN mọi dòng NHATKY của cửa {c}"
                 f" ({wm.get(c) or 'không có dòng nào'}): bảng chứng minh lượt ghi"
                 f" đó ĐÃ xong mà NHATKY không còn - dòng hay CẢ FILE QUÝ đã mất."
                 f" CẤM sinh lại bảng (sinh lại là xóa bằng chứng cuối); khôi"
                 f" phục NHATKY mức C từ {BAN_CU} TRƯỚC, rồi mới sinh lại"
                 if moi_hon else
                 f"bảng={gb} watermark {c}={wm.get(c) if c else 'không'}:"
                 f" bảng cũ hơn lượt ghi gần nhất, sinh lại bảng"))
            # 8b. Bảng là mặt phẳng DUY NHẤT làm việc quá hạn nổi lên; thiếu bộ
            #     đếm thì banner mở phiên in số bịa mà không phép nào biết.
            #     "bàn sạch" là dạng RÚT GỌN hợp lệ mà INSTRUCTION mục 2 khai
            #     tường minh (dòng hai còn "bàn sạch · mốc: <mốc>"): đòi đủ sáu
            #     nhãn ở đó là báo oan, đúng lớp lỗi vòng 38 và 40 đang chữa.
            # dòng watermark là bằng chứng DUY NHẤT về lượt ghi của cửa KHÁC
            # khi dòng NHATKY của cửa đó chưa đồng bộ về (hội đồng vòng 15)
            _nhan = ["mốc", "watermark"] if "bàn sạch" in bdk_nd else [
                "quá hạn", "chờ đối tác", "plan C treo", "ĐANG GHI", "mail", "mốc",
                "watermark"]
            _thieu_dem = [k for k in _nhan if k.lower() not in bdk_nd.lower()]
            bao("8b. BANG_DIEU_KHIEN mang đủ sáu bộ đếm",
                not _thieu_dem, f"thiếu nhãn {_thieu_dem}: bảng thiếu bộ đếm thì"
                f" banner mở phiên in số bịa; sinh lại theo X5 mục 3 bước 6")
            # 8e. Bộ đếm của bảng phải KHỚP SỔ, không chỉ có mặt tên. 8b chỉ
            #     đếm NHÃN, và ở dạng "bàn sạch" chỉ đòi hai nhãn - nên kho có
            #     chứng thư số hết hạn 59 ngày, việc quá hạn và dữ kiện quá mốc
            #     rà lại 119 ngày vẫn khai "bàn sạch" và bộ vẫn in "hệ sạch"
            #     (hội đồng vòng 18). Bảng là mặt phẳng DUY NHẤT banner mở phiên
            #     đọc, mà nó do AI tự sinh từ trí nhớ.
            _qh = dem_qua_han(so, doc(x0s[0]) if x0s else "")
            _tong_qh = sum(len(v) for v in _qh.values())
            _loi8e = []
            if "bàn sạch" in bdk_nd and _tong_qh:
                _loi8e.append("bảng khai \"bàn sạch\" mà sổ còn: "
                              + "; ".join(f"{k} {len(v)} ({_liet(v[:3])})"
                                          for k, v in _qh.items() if v))
            else:
                for _k, _v in _qh.items():
                    _m8 = re.search(re.escape(_k) + r"\D{0,12}?(\d+)", bdk_nd)
                    if _m8 and int(_m8.group(1)) != len(_v):
                        _loi8e.append(f"{_k}: bảng khai {_m8.group(1)},"
                                      f" sổ đếm {len(_v)} ({_liet(_v[:3])})")
                    elif not _m8 and _v:
                        # banner ĐẦY ĐỦ mà thiếu nhãn: chỉ so nhãn CÓ MẶT là
                        # ba bộ đếm hết hạn / rà lại / _INBOX vô hình - chứng
                        # thư +20 ngày mà "hệ sạch", vòng 18 tái hiện (giám
                        # khảo rubric 07)
                        _loi8e.append(f"bảng không mang nhãn \"{_k}\" mà sổ"
                                      f" đếm {len(_v)} ({_liet(_v[:3])})")
            # MỐC = hạn sớm nhất còn hiệu lực (X5 mục 3 bước 6) thành máy:
            # trước đây là lời hứa không ai đối chiếu (giám khảo rubric 07)
            import datetime as _dt8e
            _han_toi = []
            for _r8 in dong_bang(doc(so / "TAILIEU.md")):
                if len(_r8) > 11 and "[đã xóa theo Q-" not in "|".join(_r8) \
                        and (len(_r8) <= 7 or _r8[7].strip().upper()
                             not in ("HẾT HIỆU LỰC", "ĐÃ GIA HẠN", "ĐÃ THAY",
                                     "TRẢ HỒ SƠ", "HỦY")):
                    _m8h = re.search(r"(\d{4}-\d{2}-\d{2})", _r8[11])
                    if _m8h and _m8h.group(1) >= _dt8e.date.today().isoformat():
                        _han_toi.append(_m8h.group(1))
            if _han_toi and min(_han_toi) not in bdk_nd:
                _loi8e.append(f"mốc: hạn sớm nhất còn hiệu lực là"
                              f" {min(_han_toi)} mà bảng không nêu")
            bao("8e. bộ đếm của bảng khớp sổ",
                not _loi8e, f"{'; '.join(_loi8e[:3])}. Bảng là mặt phẳng DUY"
                f" NHẤT banner mở phiên đọc; khai sai là mọi phiên sau đọc sai."
                f" Sinh lại bảng theo X5 mục 3 bước 6, ngưỡng ở X0 C9")

            # 8c. Bảng phải khai lane watermark cho MỌI cửa có lượt ghi: X5 mục
            #     3 bước 6 đặt watermark làm chỗ DUY NHẤT giữ mã cuối của cửa
            #     KHÁC. Lane rụng thì cửa đó mất mốc cao nhất và lượt sau có thể
            #     cấp lại mã đã dùng - phép 8 chỉ đọc sinh_boi nên mù (vòng 15).
            # đọc ĐÚNG dòng watermark, không quét trọn bảng: một dòng văn
            # xuôi bất kỳ mang chuỗi "CUA2=" là đủ để lane rụng mà phép này im
            _wmd = re.search(r"watermark:\s*(.+)", bdk_nd or "")
            _wm_khai = set(re.findall(r"\b(CUA\d+)\s*=",
                                      _wmd.group(1) if _wmd else ""))
            _thieu_lane = sorted(cc for cc in wm if cc not in _wm_khai)
            bao("8c. bảng khai watermark mọi cửa có ghi",
                not _thieu_lane, f"thiếu lane {_liet(_thieu_lane)}: cửa đó mất mốc"
                f" cao nhất, lượt sau có thể cấp lại mã đã dùng. Sinh lại bảng"
                f" theo X5 mục 3 bước 6")
            _wm_gt = dict(re.findall(r"\b(CUA\d+)\s*=\s*(" + MAU_G + r")",
                                     _wmd.group(1) if _wmd else ""))
            _lane_sai = sorted(f"{c}: bảng={_wm_gt.get(c) or 'thiếu'} NHATKY={m}"
                               for c, m in wm.items() if _wm_gt.get(c) != m)
            bao("8d. watermark khớp mã cao nhất cửa đó",
                not _lane_sai, f"{_liet(_lane_sai[:3])}: lane LÙI hay khai sai thì"
                f" lượt sau cấp lại mã ĐÃ DÙNG; 8c chỉ đếm TÊN lane nên mù giá trị")
            khac = [f"{k}={v}" for k, v in sorted(wm.items()) if k != c and v[2:10] > (gb or '')[2:10]]
            if khac:
                print(f"        LƯU Ý: cửa khác có lượt ghi ngày mới hơn bảng ({'; '.join(khac)}), cân nhắc sinh lại")

    try:
        args_thuong, loc_ho = tach_tham_so(sys.argv[1:])
    except ValueError as e:
        bao("9-11. --ho giải đúng một họ tài liệu", False, str(e))
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
        bao("9-11. --ho giải đúng một họ tài liệu", False,
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
    if CHO_VAO_SO:
        print(f"KẾT QUẢ: sạch về ràng buộc, nhưng {sum(CHO_VAO_SO)} mục chờ vào"
              f" sổ (X4 dòng 2). CHƯA nói được \"sổ khớp thực tế\".")
        sys.exit(3)
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
    _g = Path(_thuong[0])
    if (not _thuong[0].startswith("--") and _g.is_dir()
            and not (_g / "_so").is_dir()
            and not list(_g.glob("X0_CAUHINH_*.md"))
            and not list(_g.glob("INSTRUCTION_WORKOPS_*.md"))
            and not (_g / "00_Index").is_dir()):
        # thư mục tồn tại nhưng KHÔNG dấu vết cài đặt nào: gõ nhầm đường,
        # đừng phun "khôi phục mức C" oan (tự vệ vế sáu, hội đồng vòng 11)
        print(f"LỖI CÁCH DÙNG: '{_thuong[0]}' không có _so, X0 hay INSTRUCTION -"
              f" có phải gõ nhầm đường 00_Index?")
        print(CACH_CHAY)
        sys.exit(2)
    if _thuong[0].startswith("--") or not Path(_thuong[0]).is_dir():
        # thư mục ma hay flag lạ ở vị trí đầu: LỖI CÁCH DÙNG, không phun
        # "khôi phục mức C" oan trên thư mục không tồn tại (hội đồng vòng 10)
        print(f"LỖI CÁCH DÙNG: '{_thuong[0]}' không phải thư mục 00_Index tồn tại")
        print(CACH_CHAY)
        sys.exit(2)
    main(_thuong[0])
