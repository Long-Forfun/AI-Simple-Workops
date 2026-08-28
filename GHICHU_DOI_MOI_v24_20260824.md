# GHI CHÚ ĐỔI MỚI · STARTER · 20260824

File này cho người đánh giá. Không phải luật, không cần copy vào bộ chạy.
Các vòng xếp mới nhất ở trên; vòng 9 (v10) từng qua thêm một lượt team agent
nội bộ tự rà, tự dựng case, tự đóng vai người dùng.


Các mục vòng 1 tới 45 đã chuyển sang `GHICHU_LICHSU_v24_20260824.md` để file này
không phình mãi - X9 mục 3c chép GHICHU vào kho MỌI công ty mỗi lượt nâng cấp.
Lịch sử không mất, chỉ đổi chỗ.

## Vòng 79: rubric vòng chấm 04 - 93/100, vá nốt các khoản còn lại

Giám khảo chấm bản vòng 46 (b3f8834): 93/100 (95 · 96 · 91 · 93). Lần đầu
CẢ BA mục chạy-thật (cài được, vận hành tuần, thuế phiên) cùng tối đa, chín
vá vòng 03 giữ trọn, 10/10 mutant seed 45 trong mẫu chết. Khoản trừ dồn vào
hai vùng mới mở - và vòng 78 (sau ảnh chấm) đã vá sẵn phần lớn tầng CON
NGƯỜI, giám khảo tự ghi nhận "working tree đang vá đúng hướng". Phần còn
lại, vá trong vòng này:

1. X9 CÂU 3 KHAI 5/8 TRƯỜNG: kênh cài đặt hỏi thiếu (thiếu nhánh tự deploy,
   CSDL, phụ trách - ba trường vào schema sau khi X9 viết câu hỏi), nên
   người dùng trả lời ĐÚNG câu hỏi xong vẫn ăn 7d đỏ. Kênh hỏi nay khớp đủ
   TÁM trường; luật-grep phép 12 siết theo bản mới.

2. NEO BÀN GIAO: @NHIP.BANGIAO tự hứa "rà một lượt việc đang mở và plan treo
   sang người mới" mà không máy nào nhắc - người cũ nghỉ, việc trôi vô chủ.
   Nay khai tên ở C9 mà VIEC còn việc ĐANG MỞ gán tên đó thì in LƯU Ý (chỉ
   nhắc - việc ĐÚNG là của người cũ tới khi rà xong). Bug lượt đầu: regex
   không neo đầu dòng nên vớ nhầm câu văn xuôi C6 nhắc "@NHIP.BANGIAO" -
   ca đầu-ra bắt được trước khi lên bản.

3. BA MUTANT NGOÀI MẪU: lưới mềm 7g (tính năng vòng 76) tắt được mà bộ vẫn
   xanh - thêm ca đầu-ra "LƯU Ý 7g" theo khuôn chụp stdout của 13b; lách gõ
   Mức "c" thường (comment 3g tự khai từ lâu) - ca I3 ghim; vế CSDL của 7d
   đã được ca vòng 78 giết sẵn.

4. HIỂU ĐƯỢC: xác câu cũ "án khác," (vá vòng 61 để sót) trong đoạn Đóng dự
   án của X0 C2 - viết lại trọn đoạn, câu đứt biến mất.

Tái đo: m6 <- 11, n6 <- 13, bàn giao <- 11 - 3/3 CHẾT. Fixture 104 ca.
BẤT BIẾN I1 7, I2 33, I3 77(nt)/76. NHẬT KÝ RUBRIC: 95 · 96 · 91 · 93.
BACKLOG: (e) sổ CSV (đang CẤM).

## Vòng 78: trường thứ tám - NGƯỜI PHỤ TRÁCH VẬN HÀNH (vế TỔ CHỨC)

Phạm vi phần mềm sau vòng 77 phủ HẠ TẦNG (repo, môi trường, host, nhánh tự
deploy) và DỮ LIỆU (CSDL chạy thật) - nhưng "phạm vi TỔ CHỨC" còn một vế
chưa trả lời: CON NGƯỜI. Lượt mức C mà không biết hỏi AI thì "plan và cái
gật TRƯỚC" của X5 mục 1 là cái gật của không ai cả.

Trường thứ tám của @DUAN.PHANMEM: "phụ trách vận hành <tên - người GẬT lượt
mức C, hay 'chưa rõ'>". Máy giữ hai tầng: 7d ĐÒI trường (ca I3 khai đủ bảy
trường kia mà thiếu phụ trách -> 7d kêu); giá trị đích danh được 7g nhắc
THẲNG TÊN trong thông điệp mức C - "cần plan và cái gật TRƯỚC của chị Trân"
- người dùng biết đi xin ai, không chỉ biết mình sai (lab xác nhận tên chảy
vào thông điệp).

Đo đột biến lộ thêm một lỗ đối xứng: "7d bỏ đòi CSDL" cũng đang SỐNG - ca
vòng 77 khai "CSDL chua ro" nên gỡ mục CSDL khỏi danh sách đòi không ca nào
thấy. Thêm ca khai-đủ-trừ-CSDL; lượt đầu ca này tự dính bẫy của chính nó
(tên fixture "He thieu db" chứa chữ db nên pattern CSDL tự khớp) - đo lại
2/2 mutant CHẾT.

X0 giữ trần 20000: trường mới trả chỗ bằng cắt chữ thừa cùng khối C2 (hai
lượt). Trần kiem_van_hanh 185000 -> 195000 (file dev; trần THẬT là 13b/13c
trên đầu ra, cả hai xanh). BẤT BIẾN I1 7, I2 33, I3 76(nt)/75. Đang chờ
rubric vòng chấm 04. BACKLOG: (e) sổ CSV (đang CẤM).

## Vòng 77: rubric vòng chấm 03 - 91/100, vá cả chín khoản

Giám khảo chấm bản vòng 44, seed đột biến 44 chiếu thẳng vào VÙNG MÃ MỚI chưa
kịp có fixture: 91/100 (01: 95 · 02: 96). Điểm tụt KHÔNG phải thoái lui - cả
sáu vá vòng 42-44 tái xác minh GIỮ - mà là giá của mã mới chưa ghim. Chín
khoản, vá hết:

LƯỚI TỰ GIỮ (bốn mutant sống, mỗi con có hành vi lệch chứng minh):
· m02: kho lành fuzz KHÔNG có dòng PLANNING đi qua 3g - mutant đọc lệch cột
  báo oan mà mọi ca vẫn xanh. Kho lành nay có plan ĐÃ GHI (ngày 2098 để
  không hỏng theo thời gian thật) - lane PLANNING được quan sát HAI CHIỀU.
· m03: lane THU vòng 43 chỉ ghim SAI TỪ VỰNG; trạng thái RỖNG - luật hội
  đồng vòng 18 - bị mutant nuốt im. Ca I3 rỗng thêm.
· m07: kiem_payload nhận thao_tac RỖNG khi lật or->and - mail nạp không tạo
  dòng sổ nào vẫn ĐẠT. Ca trực tiếp; fixture 102 ca.
· m09: nhánh thử lại NFC/NFD của phép 9 (đĩa macOS/Dropbox) không fixture
  nào phủ - mutant báo MẤT oan. Ca I2 file NFD trên đĩa, sổ ghi NFC.

PHẠM VI PHẦN MỀM (ba lỗ chạm sản xuất):
· ĐA HOST: "chạy thật app... va api..." chỉ neo host ĐẦU - deploy lên host
  thứ hai lọt cả 7g cứng lẫn lưới mềm. Nay bắt trọn vế rồi nhặt MỌI token
  dạng domain; ca I3 deploy-host-thứ-hai ghim.
· TRƯỜNG THỨ BẢY của @DUAN.PHANMEM - CSDL/kho dữ liệu chạy thật (tên đích
  danh hay "CSDL chưa rõ"): update bảng giá trên CSDL khách là mức C theo X5
  mục 1 mà máy không có neo nào nếu không hỏi tên. 7d đòi trường, giá trị
  nạp vào neo 7g; ca I3 ghim. Đây là câu trả lời trực tiếp cho điều kiện
  "nắm rõ phạm vi tổ chức phần mềm": phạm vi nay gồm cả TẦNG DỮ LIỆU.
· Lưới mềm mở sang NEO CHỮ: "push ban moi len prod" (động từ lạ + chữ suông)
  trước im tuyệt đối, nay LƯU Ý tự soát.

KHÔNG BÁO OAN (mâu thuẫn hai luật): X5 m3 b3 bắt nối mã G vào Ghi lần của
MỌI dòng chạm tới - kể cả dòng QUYETDINH bị đánh ĐÃ THAY - trong khi sha 13n
gồm ô Ghi lần, nên làm đúng CẢ HAI luật ăn lệch "SỬA TẠI CHỖ" oan. Sha nay
chỉ lấy NĂM Ô ĐẦU (đúng lời sổ tự khai "nội dung bất biến"); ca I2 lượt-sau-
nối-Ghi-lần dựng đủ nhân chứng (dòng NHATKY + watermark bảng).

TÁI ĐO: 6/6 mutant CHẾT (m02 <- 13+15, m03/m09/đa-host/13n <- 13, m07 <- 11).
Lab neo CSDL 4/4 hành vi đúng (bản đầu regex nuốt "chạy thật" vào tên - lab
bắt trước khi lên bản). Trần X0 giữ 20000: trường mới trả chỗ bằng cắt chữ
thừa trong chính khối C2.

BẤT BIẾN I1 7, I2 33, I3 74(nt)/73. NHẬT KÝ RUBRIC: 95 · 96 · 91 (giá của mã
mới - cả chín khoản đã vá trong vòng này). BACKLOG: (e) sổ CSV (đang CẤM).

## Vòng 76: lưới MỀM cho động từ thứ N+1 của 7g

Hai vòng rubric liền, mục PHẠM VI PHẦN MỀM đều mất điểm theo cùng một khuôn:
giám khảo tìm ra một ĐỘNG TỪ đời thực chưa vào danh sách của 7g (vòng 01:
gop; vòng 02: phat hanh, dua len, squash). Danh sách động từ là cuộc rượt
đuổi không có vạch đích - vá từng từ là đúng nhưng chưa đủ, vì từ thứ N+1
luôn lọt trong IM LẶNG TUYỆT ĐỐI.

Lưới mềm mới nằm ngay sau 7g: câu mức A/B nhắc ĐÍCH DANH host chạy thật đã
khai ở X0 C2 mà máy KHÔNG nhận ra động từ sản xuất nào thì in LƯU Ý tự soát -
"nếu lượt đó CÓ chạm thật thì đổi mức C; chỉ nhắc tới thì thôi". KHÔNG kết
tội: họp, xem, bàn về prod là hợp lệ, nên đây là LƯU Ý chứ không phải LỆCH -
đổi lớp im-lặng-tuyệt-đối lấy lớp tự-soát mà không đẻ thêm lớp báo oan.

Lab 5 ca: động từ lạ + host -> LƯU Ý · chỉ họp bàn về host -> LƯU Ý · động
từ đã biết + host mức B -> LỆCH (7g cứng giữ nguyên) · mức C -> im · câu
không liên quan -> im. Nhân tiện "hotfix" và "sửa nóng" vào thẳng danh sách
cứng - ca hotfix chuyển từ LƯU Ý thành LỆCH đúng bậc.

BẤT BIẾN không đổi: I1 7, I2 31, I3 71(nt)/70. Đang chờ rubric vòng chấm 03
(bản vòng 44). BACKLOG: (e) sổ CSV (đang CẤM chuyển - trạng thái an toàn).

## Vòng 75: backlog (a) - nội dung QUYETDINH thành thứ MÁY GIỮ (phép 13n)

QUYETDINH tự khai "Không xóa dòng, không sửa NỘI DUNG quyết định" từ ngày
đầu, mà cả hai lệnh cấm đều chỉ là lời: sửa ô "Chọn gì" tại chỗ hay xóa trọn
dòng đều im. Đây là mục backlog nặng nhất còn lại vì nó đòi ĐỔI SCHEMA - phải
có chỗ LƯU dấu vân nội dung.

Thiết kế theo đúng khuôn _moc_ghi đã chạy tốt: NEO NGOÀI `00_Index\_moc_qd.txt`
(chỉ-thêm, một dòng "Q-mã sha12"), sha lấy trên PHẦN BẤT BIẾN của dòng (Mã ·
Ngày · Chọn gì · Vì sao · Đánh đổi · Ghi lần) - hai ô quản trị Trạng
thái/Thay bởi đổi theo luật ĐÃ THAY nên KHÔNG vào sha, luật thay-quyết-định
không bị phạt. Phép 13n: có neo mà sha lệch = SỬA TẠI CHỖ (mức C); có neo mà
dòng biến mất = XÓA DÒNG (mức C); chưa có neo = LƯU Ý kèm dòng neo IN SẴN để
dán (mức A) - kho lập trước nâng cấp không bị phạt vì làm đúng luật thời
điểm cũ, và công thức sha sống trong MÁY chứ không chiếm chỗ trong X5 (13n in
sẵn, người dùng không thể tính sai). Tombstone xóa pháp lý miễn.

Bốn ca ghim: I3 sửa-tại-chỗ · I3 xóa-dòng (lượt đo đầu mutant "bỏ nhánh xóa"
SỐNG - thêm ca này mới chết, lại đúng bài mỗi nhánh một ca) · I2 đổi hai ô
quản trị theo ĐÃ THAY không được kêu · đột biến hash-cả-ô-quản-trị bị I2 bắt.
Đo 3/3 mutant vùng 13n CHẾT.

TRẢ NỢ TRẦN có bù: X5 +265 ký tự cho luật neo, cân bằng nâng trần X5
20000->20300 kèm HẠ X1 3200->2900 (X1 thực dùng ~1.900) - tổng trần luật
KHÔNG tăng; 9b/BENCHMARK khai lại cùng lượt; route đo lại bằng
--sinh-benchmark (X5 mục 3: 1339->1392). Hội đồng 23 hai giám khảo còn lại
đã bị dừng bởi người dùng - coi như hủy, không phóng lại.

BẤT BIẾN I1 7, I2 31, I3 71(nt)/70. BACKLOG còn: (e) sổ CSV (đang CẤM chuyển,
chưa có bản rà đọc định dạng đó).

## Vòng 74: rubric vòng chấm 02 - 96/100, vá cả ba khoản trừ mới

Giám khảo độc lập chấm lại bản vòng 41 bằng cùng rubric: 96/100 (+1 so vòng
01; cả ba bản vá vòng 01 xác nhận CHẾT bằng ca chạy thật). Ba khoản trừ mới:

1. LANE THU CỦA 3G CHƯA GHIM: kho lành của fuzz không có dòng THU dữ liệu
   nên đột biến "đọc cột 8 thành cột 9" sống - lưới đúng mà chưa từng được
   quan sát HAI CHIỀU ở lane này. Bài học phụ đắt hơn bài học chính: lượt vá
   đầu tôi nhét dòng THU vào kho lành và MỌI ca fuzz chết - vì dòng THU làm
   cổng phép 12 coi EMAIL "đã chạy" và đòi nhật ký + registry + @NHIP.HOPTHU.
   Cổng đúng, chỗ đặt sai. Bản cuối: hai ca tự dựng MÔI TRƯỜNG EMAIL TỐI
   THIỂU (nhật ký rỗng + registry rỗng + khai hộp thư) - một I3 trạng thái
   sai từ vựng, một I2 dòng THU hợp lệ không được kêu. Chính ca I2 giết
   mutant: bản đột biến đọc ô "Chờ từ" rỗng và tố oan THU.

2. kiem_payload LANE METADATA: vá vòng 41 chỉ ghim operation_id sai kiểu,
   conv_id=123 vẫn để ngỏ. Ca "metadata nguồn sai kiểu bị từ chối" thêm vào
   cạnh ca schema; fixture 100 -> 101.

3. 7g THIẾU ĐỘNG TỪ: "phat hanh ban 2.1 len <host>", "dua ban v2 len main",
   "squash branch feature vao main" - ba cách gõ đời thực chạm chạy thật mà
   lọt mức thấp. Thêm phát hành / đưa bản / đưa lên / squash / release /
   go-live vào danh sách động từ, và đưa/squash/rebase vào neo nhánh. KHÔNG
   thêm "ship": tiếng Việt thương mại "ship hàng" quá phổ biến, thêm vào là
   đổi một lỗ MISS lấy một lớp BÁO OAN. Hai ca I3 phủ cả hai lane neo.

TÁI ĐO cả ba mutant: 3/3 BẮT (3g-THU <- 13, metadata <- 11, 7g <- 13).
Khuyến nghị m10 (dòng in "LƯU Ý cửa khác" đa cửa) ghi nhận, chưa ghim - là
dòng nhắc, không phải phép.

BẤT BIẾN I1 7, I2 30, I3 69(nt)/68. NHẬT KÝ RUBRIC: 01 = 95 · 02 = 96 (bản
vòng 41). BACKLOG: (a) hash QUYETDINH · (c) khuôn bản sao · (e) sổ CSV.

## Vòng 73: phép 0r - vòng đời _inbox sang _da_nap (backlog j)

X3 chặng 2 dặn: nạp xong CHUYỂN _INBOX sang _da_nap, tên gốc vào ô Căn cứ
trạng thái; tải hụt thì KHÔNG chuyển và ghi VIEC. Hai lỗ của lời dặn đó chưa
từng có máy giữ:

· File nằm CẢ _inbox lẫn _da_nap - bản CHÉP sót thay vì CHUYỂN. Phiên sau
  thấy file còn trong _inbox thì nạp LẠI, dòng sổ nhân đôi, và phép 7 sẽ tố
  mã trùng ở đúng chỗ người dùng không hiểu vì sao.

· File trong _da_nap mà tên không để lại DẤU VẾT ở bất kỳ sổ nào (sáu sổ +
  NHATKY các quý + _lich_su): "đã nạp" khi ấy là lời khai suông - thứ đúng
  chiến dịch này đi diệt, lần này ở tầng dữ liệu thay vì tầng luật.

Ba ca ghim: hai I3 (mỗi lỗ một ca) + một I2 (file đã nạp có tên gốc ở Căn cứ
trạng thái TAILIEU - đúng khuôn X3 - không được kêu). Trả chỗ nhãn mới bằng
cắt thông điệp 0j, 1a; trần đầu ra GIỮ NGUYÊN. I2 29, I3 66(nt)/65.

BACKLOG còn: (a) hash nội dung QUYETDINH (đổi schema) · (c) khuôn bản sao ·
(e) sổ CSV. Đang chờ: hội đồng 23 (MISS, VẬN HÀNH) và rubric vòng chấm 02.

## Vòng 72: lần chấm RUBRIC CỐ ĐỊNH đầu tiên - 95/100, vá cả ba khoản trừ

Từ vòng này có HAI thước tách bạch: điểm đối kháng /10 (la bàn tìm lỗi, chĩa
vào mã mới nhất, NÊN thấp) và RUBRIC CỐ ĐỊNH /100 chấm CẢ BỘ - 10 mục, trọng
số ghim, giám khảo độc lập chấm bằng bằng chứng chạy thật, ca đặt tên để vòng
sau lặp lại được. Lần chấm đầu trên bản vòng 70: 95/100 (ĐÚNG 15/15 · KHÔNG
BÁO OAN 15/15 · KHÔNG MISS 15/15 · LƯỚI TỰ GIỮ 7/10 · PHẠM VI PHẦN MỀM 8/10 ·
CÀI ĐƯỢC 10/10 · VẬN HÀNH TUẦN GIẢ LẬP 10/10 · THUẾ PHIÊN 5/5 · HIỂU ĐƯỢC 5/5
· LỜI KHAI = MÁY 5/5). Ba khoản trừ, vá hết trong vòng này:

1. 7g LỌT MERGE KHÔNG DẤU (trừ 2 ở PHẠM VI PHẦN MỀM): neo merge-vào-nhánh
   chỉ nhận "merge|gộp" CÓ dấu trong khi danh sách động từ của chính phép này
   cố ý nhận "gop nhanh" không dấu từ vòng 19. "Gop nhanh feature vao main
   sau review" - kiểu gõ phổ biến nhất - lọt mức B ở đúng lượt merge vào
   nhánh tự deploy. Neo mới nhận g[ộo]p và đẩy lên/day len; ca I3 ghim.

2. Đột biến m08 SỐNG (trừ ở LƯỚI TỰ GIỮ): lật `len(r) > 11` thành `<=` là bộ
   đếm "hết hạn" chết hẳn - đúng kịch bản chứng-thư-hết-hạn-mà-bàn-sạch của
   hội đồng vòng 18 - mà không phép nào của kiem_tra_bo kêu. Ca I3 mới: dòng
   TAILIEU hết hạn 2020-01-01 (quá khứ vĩnh viễn, không hỏng theo thời gian
   thật) trên bảng "bàn sạch" thì 8e PHẢI đỏ.

3. Đột biến m05 SỐNG: operation_id SAI KIỂU (số 123) qua được kiem_payload
   khi lật isinstance->and, vì fixture 12h chỉ thử THIẾU trường. Thêm ca sai
   kiểu; fixture quan sát 99 -> 100 ca, số khai sửa cùng lượt.

TÁI ĐO cả ba mutant sau vá: 3/3 BẮT (m05 <- phép 11, m08 <- phép 13, neo 7g
lùi về có dấu <- phép 13). Ghi chú "sdfish trong .gitignore" của giám khảo
KHÔNG tái hiện trên repo - không nhận.

BẤT BIẾN I1 7, I2 28, I3 64(nt)/63. NHẬT KÝ RUBRIC: vòng chấm 01 (bản vòng
70) = 95/100; trần khả dĩ sau vá ước ~99 theo chính giám khảo. BACKLOG: (j)
vòng đời _inbox · (a) hash QUYETDINH · (c) khuôn bản sao · (e) sổ CSV.

## Vòng 71: trả nốt bốn món MISS của hội đồng vòng 22

Không chờ hội đồng vòng 23 về đủ: bốn mục backlog mà giám khảo vòng 22 đã
chứng minh bằng ca chạy thật, vá hết trong một vòng.

1. Phép 3h - Ô NGÀY TRÔNG NHƯ NGÀY MÀ MÁY KHÔNG ĐỌC ĐƯỢC. `30/06/2026` hay
   `2026-13-01` làm ngay() trả None và dòng rơi LẶNG LẼ khỏi cả ba bộ đếm
   quá hạn / rà lại / hết hạn - hợp đồng trễ 60 ngày mà bảng vẫn "bàn sạch".
   Chỉ soi đúng BA CỘT bộ đếm đọc để không tố oan chữ tự do; ô mang ngày ISO
   hợp lệ kèm ghi chú thì tha (ca I2 ghim).

2. Phép 10d vá HAI LỖI. Một: strip("/") xong mới hỏi endswith("/") - nhánh
   nhận diện THƯ MỤC là mã chết, bộ hồ sơ ĐÃ NỘP (X0 C1 bắt bỏ trống sha) bị
   đòi sha oan. Hai: so mốc bằng chuỗi TUYỆT ĐỐI trong khi 10a so bo_dau -
   `ĐÃ KÝ (bản scan 19/8)` được 10a coi là mốc nhưng 10d cho qua, thiếu sha ở
   đúng bản đã ký mà sổ vẫn xanh. Hai phép cùng đọc một ô nay cùng luật.

3. Phép 0q - JUNCTION/SYMLINK TRỎ RA NGOÀI KHO. `mklink /J 99_Goc D:\ngoai`
   không cần admin, không phải symlink (is_symlink trả False), cho file ngoài
   kho qua hết 9/10a/10b/10d - trong khi sao lưu kho và git KHÔNG mang chúng:
   "bản gốc bất biến" nằm ở chỗ không ai giữ. Đi os.walk không theo link, hỏi
   cả is_junction lẫn is_symlink, chỉ tố link trỏ RA NGOÀI.

4. Phép 9d - TÊN KHAI LỆCH HOA-THƯỜNG VỚI ĐĨA. NTFS cho qua nên phép 9 im,
   nhưng đồng bộ sang Linux, git checkout hay rsync coi là MẤT FILE hàng
   loạt. resolve() trả đúng casing trên Windows; so sau khi NFC hai vế để
   không dẫm lưới NFD. Ca I3 chỉ đăng ký trên NTFS - trên POSIX khai sai hoa
   thường nghĩa là mất file thật và phép 9 đã bắt sẵn - nên SỐ CA I3 khai
   THEO NỀN (62 nt / 61 posix), lần đầu con số này có điều kiện.

Trần đầu ra GIỮ NGUYÊN cả vòng: trả chỗ cho ba nhãn mới bằng cắt gọn thông
điệp 0g, 0h, 0k và mười nhãn - tổng bảng CẬN XẤU đúng 5.200/5.200. Token đầu
ra kho lành 806 -> 824, khai lại ở BENCHMARK theo số đo thật. Dọn nốt hai
SyntaxWarning docstring của chính kiem_tra_bo.

BẤT BIẾN I1 7, I2 28, I3 62(nt)/61. BACKLOG còn: (j) vòng đời _inbox ·
(a) hash nội dung QUYETDINH · (c) khuôn bản sao · (e) sổ CSV.

## Vòng 70: một máy fence duy nhất, và tach_o mở dần từng ngăn

Giám khảo báo-oan của hội đồng vòng 23 chấm 3/10 - thấp là ĐÚNG, vì đề bài
chĩa thẳng vào ba bản vá mới nhất của vòng 69 và cả bốn phát hiện đều tái hiện
được bằng ca chạy thật trước khi vá:

1. 5e đếm KÝ TỰ fence còn ngoai_fence chạy máy trạng thái - hai bộ đọc một thứ
   bằng hai luật, và chúng lệch thật: khối ``` có ruột là một dòng ~~~ bị 5e tố
   "thiếu dòng đóng", trong khi lời tố lại chính là lời 5b khuyên người dùng
   làm. Nghe lời máy sửa thì dòng hỏng thật phía sau tàng hình.

2. ngoai_fence thiếu ba luật CommonMark 4.5: fence ĐÓNG phải dài KHÔNG KÉM
   fence mở, dòng đóng không được mang info string, info string của fence nháy
   không được chứa nháy. Thiếu vế độ dài thì khối BỐN NHÁY - cách duy nhất hợp
   chuẩn để dán ví dụ chứa ``` - bị dòng ``` bên trong cắt sớm, ruột ví dụ lòi
   ra thành dòng thật và ăn lệch "mã trùng" chỉ thẳng vào dòng sổ THẬT.

   Vá gốc cho cả 1 lẫn 2: MỘT máy trạng thái `_quet_fence` theo CommonMark cho
   cả ngoai_fence LẪN 5e. Từ nay không còn hai bộ đọc fence.

3. tach_o vòng 69 được-ăn-cả-ngã-về-không: dòng vừa mang `\|` thoát vừa trỏ
   thư mục kết thúc `\` thì tách trọn GFM hụt một ô, tách trọn THÔ dôi một ô.
   Nay mở DẦN từng ngăn nghi ngờ tới khi đủ cột; chọn tổ hợp thì ưu tiên ngăn
   có ô đứng trước TRÔNG NHƯ ĐƯỜNG DẪN (chỉ dòng trỏ BỘ HỒ SƠ mới được kết
   thúc bằng `\` theo X0 C1), hoà thì lấy phía sau; chặn nổ tổ hợp ở 12 ngăn.

4. Phát hiện thứ tư (5b tố bảng lồng trong mục danh sách) KHÔNG nhận toàn
   phần: giám khảo đề nghị miễn, nhưng miễn là để một dòng sổ THẬT đặt ở đó
   mất im lặng - đúng cái giá vòng 66 đã trả. Giữ 5b kêu, chỉ sửa LỜI KHUYÊN:
   bọc fence đứng TRƯỚC, "kéo về sát lề" chỉ dành cho dòng sổ thật, vì kéo một
   dòng ví dụ ra lề là nạp mã ma vào sổ. Ca I3 ghim quyết định này.

ĐO ĐỘT BIẾN vùng mã mới: lượt đầu 6/10 - bốn mutant sống là bốn luật
CommonMark chưa có ca ghim (đóng-mang-info, mở-nhay-trong-info, điểm ưu tiên
đường dẫn, hoà-lấy-phía-sau). Thêm bốn ca I2 nhắm từng con: 10/10, không con
nào sống. Bài học đứng vững từ vòng 69: mỗi nhánh logic phải có ca RIÊNG chứng
minh nó cần tồn tại, không thì nó chỉ là lời hứa.

Trần kiem_tra_bo.py nâng 165000 -> 180000: file dev ngoài mọi route, không
phải thuế phiên; cái phình là 12 ca bất biến mới. Trần ĐẦU RA giữ nguyên.

BẤT BIẾN I1 7, I2 26, I3 58. BACKLOG: ngày không ISO làm câm bộ đếm · junction
99_Goc · đường dẫn lệch hoa thường · 10d khớp 7 chuỗi cứng · (j) vòng đời
_inbox · (a) hash nội dung QUYETDINH · (c) khuôn bản sao · (e) sổ CSV.

## Vòng 69: bốn hồi quy do CHÍNH BẢN VÁ CỦA TÔI đẻ ra

Hội đồng vòng 22 cho KHÔNG MISS 6,5 (lên từ 6,0) và xác nhận 8/8 bản vá vòng
66-67 đứng vững. Bốn lỗ còn lại đều mang một chữ ký: bản vá chống BÁO OAN của
tôi đẻ ra lớp hỏng mới.

1. FENCE MỞ MÀ KHÔNG ĐÓNG NUỐT TRỌN PHẦN ĐUÔI SỔ. `ngoai_fence` bật cờ rồi
   không bao giờ tắt, nên mọi dòng còn lại thành rỗng với 3f, 3g, 5, 5b, 5d, 6,
   7, 7b, 7f và bộ đếm quá hạn - trong khi Markdown vẫn render và người vẫn đọc
   thấy. Trước vòng 66 hỏng này KHÔNG TỒN TẠI: tôi đổi một lớp BÁO OAN lấy một
   lớp TÀNG HÌNH, mà tàng hình nguy hơn, và sổ chỉ-thêm nên số dòng bị nuốt
   tăng dần theo thời gian. Phép 5e đếm dấu fence, số LẺ là LỆCH.

2. `~~~` LÀ FENCE HỢP LỆ NGANG ```. Người đọc kỹ luật rồi chọn `~~~` vì ví dụ
   của họ CÓ chứa backtick - và ăn ba lệch, kèm chẩn đoán 7b xúi khai thêm một
   dự án ma vào X0 C2. Bản vá đẩy người dùng đi làm bẩn cấu hình. Nay
   `ngoai_fence` chỉ ĐÓNG bằng đúng ký tự đã MỞ.

3. `tach_o` BÁO OAN Ô KẾT THÚC BẰNG `\` - khuôn mà X0 C1 BẮT BUỘC cho dòng trỏ
   BỘ HỒ SƠ. Bảng gõ SÁT dấu | (khuôn GFM hợp lệ, thứ markdownlint --fix sinh
   ra) làm nó thành `\|` và hai ô dính làm một. Người dùng làm ĐÚNG HAI luật
   của bộ cùng lúc và ăn hai lệch, trong đó chẩn đoán của phép 9 dẫn thẳng sang
   thao tác SAI. Lần thứ MƯỜI BA của lớp phạt-người-làm-đúng, lần thứ TƯ do
   chính bản vá chống báo oan đẻ ra.

   Cái khó thật: theo ĐÚNG GFM thì `\|` LÀ dấu thoát, không luật cú pháp nào
   phân biệt được "ô kết thúc bằng \ rồi tới dấu ngăn" với "dấu | thoát nằm
   giữa ô". Thứ DUY NHẤT phân biệt được là SỐ CỘT của header. Nên `tach_o` nay
   nhận thêm tham số số cột: tách theo luật GFM trước, chỉ khi kết quả LỆCH số
   cột mà tách THÔ lại KHỚP thì mới dùng bản thô. Lần vá đầu của tôi ở vòng này
   dùng một biểu thức lookahead và KHÔNG chạy - ca I2 mới thêm bắt được ngay,
   đó là lý do mỗi bản vá phải kèm ca riêng chứ không phải kèm lời hứa.

4. `goc_dai` VÁ NỬA VỜI: vòng 67 dùng nó ở `quet_ho` và `quet_secret`, nhưng
   phép 9, 10a, 10b, 10d vẫn `kho / rel`. Cùng MỘT lượt chạy: tầng quan sát
   THẤY file, phép 9 tuyên nó ĐÃ MẤT - hai lời khai ngược nhau trong một báo
   cáo.

Kèm: docstring `goc_dai` có escape hỏng, mỗi lượt biên dịch in SyntaxWarning.

TRẦN ĐẦU RA KHÔNG NỚI. Thêm phép 5e thì trả chỗ bằng cách viết nhãn ngắn lại
(mười một nhãn, 8c, 8d, 0g, 0k, 9, 8, 7b, 6, 1a, 4, 10a), không phải bằng cách
dời vạch 5.200 - đó là thứ người dùng TRẢ mỗi phiên RA_SOAT.

BẤT BIẾN I2 nay 16 ca, I3 56 ca. BACKLOG còn: ngày không ISO làm câm bộ đếm ·
junction ở 99_Goc · đường dẫn lệch hoa thường · (j) vòng đời _inbox và _da_nap ·
(a) hash nội dung QUYETDINH · (c) khuôn bản sao · (e) sổ chuyển sang CSV.

## Vòng 68: lưới đúng mà thông điệp làm nó vô dụng

Vòng TỰ DÒ, không chờ hội đồng: đo trước năm vùng mà giám khảo vòng 21 liệt là
chưa ai soi. Bốn vùng xử đúng sẵn và ghi lại đây để khỏi đo lại - BOM UTF-8 ở
đầu sổ (im, đúng: BOM nằm trước tiêu đề, không chạm dòng bảng) · dòng kẻ dùng
dấu hai chấm căn lề `|:---|---:|` của GFM (im, đúng) · hai khối CÙNG TÊN trong
một sổ (phép 7 bắt qua mã trùng) · khoảng trắng không ngắt U+00A0 cạnh giá trị
(str.strip của Python vốn cắt nó nên giá trị về đúng, không lệch - ĐÚNG hành
vi, ghi ra để vòng sau đừng "sửa cho đều").

MỘT PHÁT HIỆN THẬT, và nó thuộc lớp lỗi tinh vi nhất từ trước tới nay: ký tự
ZERO-WIDTH trong ô Trạng thái BỊ 3g bắt - lưới hoạt động đúng - nhưng thông
điệp in ra là `ô XONG`. Người dùng nhìn thấy ĐÚNG CHỮ XONG, đối chiếu với từ
vựng X5 thấy khớp hoàn toàn, và kết luận MÁY HỎNG. Lưới đúng mà thông điệp làm
nó thành vô dụng, và người dùng không có cách nào tự thấy vấn đề - sát ngay lớp
phạt-người-làm-đúng dù về mặt kỹ thuật thì phép này không hề sai.

U+200B, U+FEFF, các dấu định hướng sinh ra khi dán từ web, Word hay Excel. Nay
khi bỏ ký tự vô hình đi mà giá trị KHỚP từ vựng, thông điệp nói thẳng: "Trạng
thái XONG kèm KÝ TỰ VÔ HÌNH (U+200B)". Giá trị SAI THẬT thì vẫn báo như cũ,
không nhét thêm chữ gây nhiễu.

BACKLOG còn: (j) vòng đời _inbox và _da_nap · (a) hash nội dung QUYETDINH -
cần thêm chỗ LƯU hash, tức đổi schema, nên không phải việc vá một dòng · (c)
khuôn bản sao · (e) bản rà cho sổ chuyển sang CSV.

## Vòng 67: hai bảng khác thứ tự cột trong một sổ

Mục cuối của hội đồng vòng 21. X5 cho phép một sổ có nhiều khối `## <KHỐI>`,
mỗi khối một bảng - đó là cách bộ DẶN tách dự án. Nhưng không phép nào đòi các
bảng đó CÙNG MỘT thứ tự cột, trong khi `dem_qua_han`, `3g`, `7f`, `10d` và
`13m` đều đọc theo VỊ TRÍ CỨNG.

Giám khảo dựng VIEC.md có khối thứ hai đủ 10 cột nhưng đảo `Hạn` với `Chờ ai
từ`, trong đó một việc nộp hồ sơ dự thầu quá hạn 58 ngày. Mọi dòng CÙNG SỐ ô
nên phép 5 xanh, và bộ đếm quá hạn đọc nhầm ô - bảng giữ "bàn sạch", hồ sơ thầu
trễ hạn biến mất khỏi mọi mặt phẳng. Đúng hậu quả 8e sinh ra để chặn.

Phép 5d đòi mọi header trong CÙNG một sổ giống hệt nhau, và ca ĐÚNG LUẬT đi
kèm là chính ca của giám khảo: khối thứ hai dùng ĐÚNG header chuẩn phải giữ im.

Đây là mục thứ tám và cuối cùng của vòng 21 - toàn bộ danh sách hội đồng đó đã
đóng, mỗi mục kèm ca của chính nó và ít nhất một ca chứng minh không báo oan.

BACKLOG còn: (j) vòng đời _inbox và _da_nap · (a) hash nội dung QUYETDINH ·
(c) khuôn bản sao · (e) bản rà cho sổ chuyển sang CSV.

## Vòng 66: sáu lỗ của hội đồng vòng 21, hai trong đó là lời tôi tự hứa

Hội đồng vòng 21: KHÔNG MISS 6,0 (lên từ 4,0). Cả TÁM vá vòng 62-63 đứng vững
dưới tấn công trực diện, không cái nào lách được - kể cả hai chỗ rất dễ tự đẻ
báo oan là miễn-trừ-theo-đường-dẫn của quét secret và đòi-đúng-số-cột của dòng
thân bỏ pipe.

LỚP "PHẠT NGƯỜI DÙNG VÌ LÀM ĐÚNG", LẦN THỨ MƯỜI HAI, DO CHÍNH BẢN VÁ VÒNG 62
CỦA TÔI ĐẺ RA. Phép 5b in ra lời khuyên "muốn dán ví dụ bảng thì bọc trong ```
để phép này bỏ qua đúng cách". Người dùng làm ĐÚNG NGUYÊN VĂN câu đó và ăn BA
dòng lệch: 5b biết fence, `dong_bang` thì KHÔNG. Một việc VÍ DỤ "V-999" chui
vào bộ đếm quá hạn, 3f tố "dòng vào sổ ngoài lượt ghi", 7b tố dự án ma - và 3f
dặn "TUYỆT ĐỐI không gỡ dòng sổ", tức lối thoát duy nhất bị chính lưới cấm. Nay
`dong_bang`, phép 5 và 5b DÙNG CHUNG một hàm tách fence và một hàm tách ô, để
ba chỗ đọc bảng không lệch nhau lần nữa. Cùng hàm đó xử `\|` thoát - cách DUY
NHẤT hợp lệ theo GFM để viết dấu | trong ô, mà trước đây làm 3g và 5 tố oan.

LỜI KHAI VƯỢT CÁI MÁY LÀM, LẦN THỨ HAI TRONG BỘ: docstring của `chuan_hoa_ho`
viết nguyên văn "...và phép 9 báo oan khi sổ ghi NFC mà đĩa giữ NFD (hội đồng
vòng 17)". Vòng 17 chỉ vá `chuan_hoa_ho`, KHÔNG vá phép 9. Hậu quả kép: dòng bị
coi là mất file rồi `continue`, tức 10a và 10b cũng thôi kiểm sha bản ĐÃ NỘP -
mất lưới toàn vẹn ngay trên hồ sơ đã nộp thầu.

WATERMARK SO NN THEO CHUỖI: "99" > "100". Hai chiều cùng sai, và chiều thứ hai
là báo oan tệ nhất từ trước tới nay: kho LÀM ĐÚNG (lane khai -100) bị 8 và 8d
tố, và lời dặn của chúng là "sinh lại bảng" - tức kéo lane về -99, ĐÚNG THAO
TÁC gây ra "lượt sau cấp lại mã ĐÃ DÙNG" mà 8d tồn tại để chặn. Bộ vừa tố người
làm đúng vừa dạy họ làm hỏng. Vòng 58 nới MAU_G cho NN vượt hai chữ số mà quên
chỗ SO SÁNH.

MỘT CÂU TRỎ CHÉO TẮT TRỌN BỐN PHÉP: `_x0nd.find("# C3.")` trả vị trí ĐẦU TIÊN,
nên một dòng văn xuôi trong C1 như "Folder khối của kho: xem # C3. bên dưới" -
đúng tinh thần C14 - làm lát cắt C2 RỖNG. Cả ba nhánh của 7b bọc `if ... and
_da_khai` nên phép TỰ TẮT, kéo theo 7d, 7d2 và vế dự án của 2b. Nay có hàm
`cat_muc` neo `^# Cn. ` theo dòng.

Ô sha256 BỎ TRỐNG là lối tắt hợp lệ ra khỏi 10a và 10b - AI cũng chỉ cần bỏ
trống một ô là hết bị tố. Phép 10d đòi sha ở mốc chính thức và file 99_Goc,
KHÔNG đòi ở bản nháp hay dòng trỏ thư mục.

MAX_PATH LÀM CẢ KHO CON TÀNG HÌNH: `Path.rglob` nuốt OSError nên dừng đi xuống
ở chỗ vượt 260 ký tự, im lặng tuyệt đối. Đường dẫn gói thầu tiếng Việt vượt 260
là chuyện thường. Nay duyệt qua tiền tố đường dẫn dài; bàn thử bắt được secret
sau một đường 356 ký tự (và chính lệnh TẠO thư mục cũng cần tiền tố đó - bằng
chứng giới hạn này có thật trên nền đang chạy).

MAU_SECRET đòi dấu `:`/`=` NGAY sau từ khóa, nên `AWS_SECRET_ACCESS_KEY=` -
khóa AWS phổ biến nhất thế giới - `SECRET_KEY=` của Django, `TOKEN_GITHUB=`
đều trượt. Vá vòng 63 mở đúng đường cho deploy_prod.py vào lưới, nhưng lưới
không bắt được thứ nằm TRONG nó.

Bàn thử 8/8, gồm năm ca ĐÚNG LUẬT: ví dụ bảng trong fence, ô có `\|` thoát,
lane khai đúng ở NN 100, "Nơi giữ secret: 1Password", file NFD trên đĩa.

BACKLOG còn: hai bảng khác THỨ TỰ CỘT trong một sổ (dem_qua_han đọc theo vị
trí cứng) · (j) vòng đời _inbox và _da_nap · (a) hash QUYETDINH · (c) khuôn bản
sao · (e) bản rà cho sổ CSV.

## Vòng 65: MIEN_TRU từ 16 xuống 3, và ba mục còn lại có lý do THẬT

Backlog (i). Chú thích của MIEN_TRU tự khai "phải RỖNG DẦN: mỗi mục là một phép
chưa ai canh". Vòng 50 đưa nó từ 16 xuống 8 bằng cách nối tập phủ của phép 15.
Sáu mục còn lại đều DỰNG ĐƯỢC ca, chỉ là chưa ai viết: 3b (mã G trùng), 1b và
1c (hai view vượt trần runtime), 0c (nhiều bản X0 đang chạy), 0e (THU.md vắng
khi pipeline EMAIL đã có dấu vết). Năm ca mới, đo lại bằng đục ruột: 5/5 bị bắt
- hội đồng vòng 17 đo vùng miễn trừ cũ là 8/8 LỌT.

BA MỤC CÒN LẠI KHÔNG PHẢI NỢ ĐỌNG, và lý do ghi ngay tại chỗ để vòng sau đừng
ép một ca giả rồi tưởng đã canh:
  0f và 10c  cần KHÓA FILE ở tầng hệ điều hành nên ca phụ thuộc nền tảng -
             dựng được trên Windows thì hỏng trên CI Linux. Và bộ CỐ Ý phân
             biệt "chưa kiểm được" với "bị sửa"; ép chúng bắn là phá phân biệt
             đó.
  11.        chỉ so nội dung SAU khi file đạt luật ổn định HAI LƯỢT QUÉT, mà
             bộ fuzz chạy rà soát một lượt. Ràng buộc của thiết kế.

Tôi đã thử viết ca cho 11. và nó KHÔNG chạy được đúng như lý do trên - ghi lại
việc thử đó ở đây thay vì lặng lẽ để danh sách dài thêm một dòng không giải
thích.

BACKLOG còn: (j) vòng đời _inbox và _da_nap · (a) hash nội dung QUYETDINH ·
(c) khuôn bản sao · (e) bản rà cho sổ chuyển sang CSV.

## Vòng 64: 0j xuống lưu trữ, và chỉ lưu trữ

Mục cuối tôi tự hoãn ở vòng 63. 0j whitelist TRỌN ba thư mục `_lich_su`,
`_inbox`, `_thu_staging`, nên file lạ nấp ở đó không ai nhặt - mà `_lich_su`
chính là chỗ hồ sơ nằm LÂU NHẤT.

CHỈ mở `_lich_su`, và đây là phần đáng nói: `_inbox` theo định nghĩa chứa file
ĐỐI TÁC GỬI đủ mọi định dạng, `_thu_staging` chứa nguyên văn thư cùng đính kèm
do pipeline X3E sinh. Soi "file lạ" ở hai chỗ đó là báo oan HÀNG LOẠT - đúng
lớp lỗi đã tái phát mười một lần, và hai lần gần nhất do chính bản vá chống báo
oan đẻ ra. Vá đúng ở đây là vá HẸP. 0b thì đã xuống cả ba từ vòng 63, và điều
đó an toàn vì nó chỉ tìm bản conflicted chứ không phán xét file lành.

Bàn thử 7/7, trong đó bốn ca ĐÚNG LUẬT: sổ lưu trữ đúng tên, NHATKY quý cũ,
thư mục `backup_<ngày>`, và file đối tác đủ loại trong `_inbox`.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(a) hash QUYETDINH · (c) khuôn bản sao · (e) bản rà cho sổ CSV.

## Vòng 63: bốn mục cuối của hội đồng vòng 20

KHAI TRÙNG MỘT @KEY - "dòng sau đè dòng trước" IM LẶNG. Mọi hàm đọc X0 đều
`re.search` MỘT LẦN, nên bản khai trùng được giải theo "dòng nào regex gặp
trước" và không ai biết có mâu thuẫn. Hai dòng `CUA1 =` trỏ hai gốc là kịch bản
CHIA ĐÔI KHO: hai máy cùng cấp mã CUA1-NN, watermark một lane, sổ hai nơi. Hai
`@CTY.MA` thì tên file X0/X1/X5 và mã G hết quy về một công ty. Trùng khóa sinh
ra rất tự nhiên khi người dùng "chép dòng cũ xuống rồi sửa" - đúng như X9
hướng dẫn. Phép 0i3, và chỉ đếm dòng khớp `^@KEY ` nên các dòng NỐI thụt lề
dưới cùng một khóa (X0 mẫu có @NHIP.HOPTHU ba dòng) không bị tính.

0b KHÔNG XUỐNG `_lich_su`, `_inbox`, `_thu_staging`. Dropbox đẻ
`_lich_su\NHATKY_2026Q2 (Long's conflicted copy).md` chứa MỘT lượt mức C không
có ở bản chính; `loc_ban_chinh` lọc bản conflicted khỏi lượt gộp, nên lượt ký
phụ lục đó tồn tại trên đĩa, bị bỏ qua, và bộ tuyên bố sạch. Đúng vùng mù mà
vòng 58 đã vá cho lưới secret nhưng bỏ quên cho 0b. Nay rglob, và báo ĐƯỜNG DẪN
chứ không chỉ TÊN để người dùng biết nó nằm đâu.

X0_INDEX LẠC HẬU: phép 2 chỉ đối chiếu `x0_rev`. Sửa X0 mà KHÔNG tăng rev là
đường đi thường ngày - thêm dự án, bật profile đều là sửa nội dung - nên view
mà INSTRUCTION bắt phiên đọc TRƯỚC có thể khai `profile: LITE` cho một công ty
REGULATED: phiên chạy không nghi thức mức C, không plan cho thay đổi chạy thật,
dự án thứ hai VÔ HÌNH. Phép 2b so theo TẬP profile và TẬP mã dự án.
Bản đầu của tôi so VÔ ĐIỀU KIỆN và báo oan ngay trên KHO LÀNH của phép 13 -
view tối giản ở đó không có dòng `profile:` lẫn `du_an:`, và bốn phép cùng đỏ
theo. Lại suýt là một bản vá chống báo oan tự đẻ báo oan. Nay CHỈ so trường mà
view THỰC SỰ khai; ca của giám khảo vẫn bị bắt trọn vì view của họ khai đủ, chỉ
là khai SAI. Và ngay sau đó 2b bắt được một lỗi trong chính script cài thử của
tôi: view liệt kê dự án CTY mà X0 không khai.

14e SIẾT LẦN HAI: giám khảo lách được bằng `[] == []`, `x or True`, `all([])`.
Nay chặn cả BoolOp `or`, so hai hằng rỗng, và `all(<hằng rỗng>)`. Đo lại: 4/4
cách lách đều bị bắt.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(a) hash QUYETDINH · (c) khuôn bản sao · (e) bản rà cho sổ CSV · 0j vẫn chưa
xuống trong ba thư mục máy sinh (0b đã xuống; 0j cần whitelist riêng cho
`_lich_su` nên để lượt sau).

## Vòng 62: lời hứa tôi viết mà không dựng, và hai lỗ của chính bản vá cũ

Hội đồng vòng 20: KHÔNG MISS 4,0 (lên từ 3,0). Phần đáng giá nhất của báo cáo
không phải điểm mà là dòng KIỂM CHỨNG: 21/21 vá vòng 58-59 được xác nhận CÒN
KÍN, không cái nào lách lại được, và KHÔNG cái nào đẻ ra báo oan - kể cả các ca
đúng luật khó ("mật khẩu VPN giữ ở 1Password", "ĐÃ GIA HẠN", lượt thứ 101 trong
ngày, tách 618 dòng sang _lich_su). Quyết định CỐ Ý cho phép 6 không đọc
_lich_su cũng được xác nhận là đúng.

LỜI KHAI VƯỢT CÁI MÁY LÀM - DO CHÍNH TÔI PHẠM Ở VÒNG 58. Docstring của
`dong_bang` viết nguyên văn rằng thụt sâu hơn ba dấu cách là khối code và "phép
5b báo riêng chỗ đó". TÔI CHƯA HỀ DỰNG PHÉP 5b NÀO. Vá vòng 58 vì thế chỉ dịch
vùng mù từ ">=1 dấu cách" sang ">=4 dấu cách" rồi ghi chú thích như đã bịt -
đúng lớp lỗi mà cả chiến dịch này đi diệt, và phép 15 không thấy vì nó chỉ soi
X4. Nay 5b được dựng THẬT, và nó bỏ qua đúng cách khi dòng nằm trong ``` fence.

DÒNG THÂN BẢNG BỎ DẤU `|` ĐẦU - tái phát Y HỆT lớp thụt lề, chỉ đổi ký tự gây
ra. GFM cho phép bỏ pipe đầu và cuối ở dòng thân; Markdown vẫn render, người vẫn
đọc thấy, và 11 phép cùng mù trở lại. Prettier, `markdownlint --fix`, bản dán từ
Word và một lượt AI "gọn lại bảng" đều sinh ra dạng này.
Bản vá đầu của tôi SUÝT tự đẻ ra báo oan: nhận mọi dòng có đủ số pipe thì dòng
`x| DA1 |...` mà bộ fuzz dùng để "xóa dòng" bị đọc thành dòng dữ liệu LỆCH MỘT
Ô, và 3g tố oan ngay một ca ĐÚNG LUẬT của phép 13. Ranh giới tin được là ĐÚNG
SỐ CỘT của header: dòng mất pipe do Prettier vẫn đủ ô, dòng có rác đứng trước
thì dôi ra một ô và bị loại. Bàn thử 5/5.

HAI LỖ CỦA CHÍNH BẢN VÁ VÒNG 58:
- Khi mở quet_secret ra quét cả cây 00_Index, tôi loại file của bộ bằng TÊN
  (`BIET_MAT_00.fullmatch(f.name) or f.suffix == ".py"`) chứ không bằng ĐƯỜNG
  DẪN. Hệ quả: mọi README.md, mọi .gitignore, mọi X?_*.md và MỌI file .py ở
  BẤT KỲ ĐÂU trong kho thành vùng miễn dịch. Giám khảo đặt chuỗi kết nối prod
  và sk_live_... vào 02_Ky_thuat\README.md, 02_Ky_thuat\deploy_prod.py,
  99_Goc\.gitignore - tất cả "hệ sạch"; cùng nội dung trong bangiao.txt thì
  7e2 kêu ngay. README của repo và script deploy là HAI CHỖ secret hay nằm
  nhất đời thật. Nay chỉ miễn file CON TRỰC TIẾP của 00_Index.
- Sổ lõi bị cắt còn 0 BYTE mà phép 0 vẫn PASS, vì nó chỉ hỏi is_file(). Phiên
  sau nối dòng vào file KHÔNG có header là cột mất nghĩa vĩnh viễn. Phép 0p đòi
  sổ còn KHUNG, không chỉ còn TÊN.

Bàn thử 7/7 cho hai mục trên, gồm hai ca đúng luật (.gitignore thường ở gốc kho,
README nghiệp vụ không có secret).

BACKLOG còn từ hội đồng vòng 20: 0b và 0j không xuống _lich_su, _inbox,
_thu_staging · X0_INDEX chỉ đối chiếu x0_rev, còn kho/profile/dự án thì không ·
X0 khai TRÙNG một @KEY thì "dòng sau đè dòng trước" im lặng · 14e còn lách được
bằng `[] == []`, `x or True`, `all([])`. Cùng (i), (j), (a), (c), (e) như cũ.

## Vòng 61: hai lối đi mà luật quên mở

Hai mục cuối của hội đồng vòng 19, cùng một hình dạng: nghiệp vụ có thật, luật
không có ô nào cho nó, nên người dùng phải chọn giữa ôm lệch vĩnh viễn và khai
sai sự thật.

(z4) NHATKY VƯỢT 500 DÒNG TRONG MỘT QUÝ. Phép 6 kêu, nhưng X5 mục 5 cố định
NHATKY theo QUÝ còn mục 7 bước 1 chỉ cho tách "theo khối hoặc năm" - không vế
nào áp được cho một quý. Tôi đo lại ba lối trên kho 519 dòng:
    chưa tách                             -> phép 6 kêu   (đúng)
    NHATKY_2026Q3_p2.md cạnh sổ sống      -> 0b, 0j, 3e   (bẫy)
    _lich_su/NHATKY_2026Q3.md CÙNG TÊN    -> SẠCH
Tức CƠ CHẾ ĐÃ CÓ SẴN và chạy đúng - loc_ban_chinh, 3c, 3d, 3e, 3f, 3g, 7, 12l
đều đọc `_lich_su`, còn phép 6 thì cố ý không. Thứ thiếu chỉ là một câu nói cho
người dùng biết, và họ đọc nó ở ĐẦU SỔ chứ không ở X5 (X5 cũng chỉ còn 24 ký tự
headroom). Ghi vào NHATKY_TEMPLATE, kèm luôn việc NN được phép vượt hai chữ số.

(z3) DỰ ÁN NGỪNG CÒN NGHĨA VỤ BẢO HÀNH. Thanh lý hợp đồng, dự án đóng, nhưng
bảo hành chạy tiếp 12 tháng. X0 C2 chỉ cho hai lối: chuyển việc sang HỦY, hay
bàn giao dự án khác - cả hai đều SAI SỰ THẬT, vì việc bảo hành vẫn còn và không
có dự án nào khác để giao. Lối duy nhất đi được là giữ dự án "đang chạy" suốt
thời gian bảo hành, tức bàn làm việc ôm một dự án đã xong cả năm.
Lối thứ ba, đúng sự thật và CÓ HẠN RÕ: khai `NGỪNG (bảo hành tới YYYY-MM-DD)`.
7b thôi tố tới ngày ấy, và tố LẠI sau ngày ấy - vì lúc đó nghĩa vụ đã hết, việc
còn mở mới thật sự là việc bị bỏ quên. Bàn thử 4/4, gồm ca hạn đã qua.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(a) hash QUYETDINH · (b) phép 5 đối chiếu số cột với X5 mục 4 · (c) khuôn bản
sao · (e) bản rà cho sổ CSV.

## Vòng 60: hai luật BẤT KHẢ THI

Hai mục còn lại của hội đồng vòng 19 thuộc loại nặng nhất về nghiệp vụ: không
phải "máy im" mà là "làm đúng thì máy chặn".

(z1) TRẦN 1d 22.000 BẤT KHẢ THI. Tôi đặt con số đó ở vòng 48 bằng phép tính
"trần template cộng 10%" mà CHƯA HỀ ĐO một kho REGULATED cài đúng - đúng thói
quen mà cả chiến dịch này đi diệt ở chỗ khác. Giám khảo đo: template rỗng đã
19.614 ký tự = 89% trần; trả lời TRỌN nhóm B của X9 mục 2 (phạm vi và từ cấm,
các bên và vai, nguồn thẩm quyền, thuật ngữ) là 22.497; cộng ~1.216 ký tự dấu
`[x] ... điền lần đầu` mà C11 CẤM xóa thì kho cài xong đúng luật nằm khoảng
23.700. Nghĩa là MỌI công ty REGULATED làm đúng đều nhận LỆCH vĩnh viễn ngay
phiên soạn tài liệu đầu tiên. Lời khuyên của chính phép ("chuyển phần liệt kê
dài xuống sổ") lại mâu thuẫn với C11 và C14: @BEN.VAI, @PHAMVI.CAM,
@NGUON.LOAI là nhóm khóa mà X1 và X2 phải đọc TẠI CHỖ, không chép đi đâu.
Trần mới 28.000, và phép 9c bắt tôi khai nó ở CẢ HAI nơi kèm lý do - đúng việc
9c sinh ra để làm.

(z2) @KHO.CU KHÔNG CÓ DẠNG "Ở ĐÂU" NÀO HỢP LỆ. X0 C1 dựng ô @KHO.CU cho kho đã
ngừng "chỉ tra lịch sử", nhưng cột "Ở đâu" chỉ nhận bốn dạng và cả ba lối người
dùng thử đều hỏng: `Kho ..\KhoCu\...` bị phép 9 tố mất file · `KhoCu E:\...`
bị 7f tố sai dạng · `Kho cũ E:\...` lọt 7f rồi vẫn bị 9 tố. Lối DUY NHẤT máy
chấp nhận là CHÉP file sang kho mới, mà làm vậy là phá X5 mục 6 "bản cuối một
tài liệu chỉ nằm một kho". Mọi công ty vừa chuyển kho hoặc ôm lệch vĩnh viễn
hoặc nhân đôi kho, và hồ sơ 5 năm không vào được sổ nào.
Dạng thứ NĂM `KhoCu <đường dẫn từ @KHO.CU>`; phép 9, 10a, 10b không soi nó vì
kho cũ có thể offline.

Một chỗ tôi KHÔNG vá dù giám khảo nêu: `Kho cũ E:\...` vẫn qua được 7f. Đó là
"Kho" cộng một đường dẫn tên "cũ ...", và 7f không có cách nào phân biệt nó với
một đường dẫn tương đối hợp lệ bắt đầu bằng chữ "cũ" - bắt 7f đoán là mở đường
cho báo oan. Phép 9 bắt đúng ca này; việc cần làm là thông điệp của 9 chỉ sang
dạng KhoCu, vì đó mới là chỗ người dùng thật sự đọc khi gặp nó.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(z3) dự án NGỪNG còn nghĩa vụ bảo hành 12 tháng: X0 C2 chỉ cho HỦY hay bàn giao
dự án khác, cả hai đều sai sự thật · (z4) NHATKY vượt 500 dòng trong MỘT quý
chưa có lối tách nào được luật mô tả · (a) (b) (c) (e) như cũ.

## Vòng 59: lưu trữ hết là vùng khuất, header hết tắt lưới trong im lặng

(z5) 3c, 3d, 3e, 7 và 12l đều đã học đọc `_so\_lich_su\` qua các vòng 41, 15 và
50 - nhưng 3f và 3g thì chưa. Dòng thiếu mã G, hay trạng thái ngoài từ vựng,
sống nhăn trong file lưu trữ mà bộ vẫn "hệ sạch". Lưu trữ là nơi hồ sơ nằm LÂU
NHẤT, tức chỗ sai sót sống dai nhất.

PHÉP 6 THÌ CỐ Ý KHÔNG ĐỌC `_lich_su`, và ghi rõ điều đó trong mã để vòng sau
đừng "sửa cho đều": nó đếm ngưỡng 500 dòng, mà tách sổ sang lưu trữ CHÍNH LÀ
cách xử lý ngưỡng đó. Cho nó đọc thì tách xong vẫn đỏ - tức đẻ ra đúng lớp báo
oan không lối thoát mà vòng 58 vừa diệt ở chỗ khác. Bàn thử có một ca riêng
cho việc này: chuyển 618 dòng sang lưu trữ thì phép 6 phải THÔI kêu.

(z6) `cot_thu` tra cột theo TÊN trong header, không thấy thì trả rỗng - IM
LẶNG. Đổi "Conversation-ID" thành "Conversation ID" (đúng một gạch nối) là 12f
và 12i cùng tắt: hai dòng THU cùng một luồng hết trùng, và mỗi thư trong một
hội thoại được cấp một mã #L- mới. Một thương lượng hợp đồng dài 30 thư nở ra
30 luồng, digest đếm 30 việc chờ, người dùng tắt digest. Nay 12i2 báo thẳng khi
tên cột không còn.

Bàn thử 5/5, gồm hai ca ĐÚNG LUẬT. Và một ghi chú về chính bàn thử: hai ca đầu
tôi dựng SAI - chép cả sổ sống sang lưu trữ nên phép 7 kêu mã trùng, kêu ĐÚNG,
vì X5 mục 5 nói tách là CHUYỂN dòng chứ không phải chép.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(z1) trần 1d 22.000 bất khả thi, cần tách X0 thành phần THAM SỐ và phần CHÚ
GIẢI · (z2) @KHO.CU không có dạng "Ở đâu" hợp lệ · (z3) dự án NGỪNG còn nghĩa
vụ bảo hành · (z4) NHATKY vượt 500 dòng trong MỘT quý không có lối tách nào
được luật mô tả · (a) (b) (c) (e) như cũ.

## Vòng 58: một dấu cách đầu dòng xóa sổ toàn bộ lưới

Hội đồng vòng 19: KHÔNG MISS 3,0 (dựng 62 kho, 33/48 kho hỏng lọt lưới) ·
VẬN HÀNH 7,8 (pilot 18 tình huống, lên từ 7,0). Hai con số ngược chiều nhau và
cả hai đều đúng: các vá vòng 47-52 phần lớn KÍN khi diễn nghiệp vụ bình thường,
nhưng nền móng đọc bảng thì thủng.

PHÁT HIỆN NẶNG NHẤT CẢ CHIẾN DỊCH. `dong_bang()` và phép 5 lọc dòng bảng bằng
`d.startswith("|")`. Dòng thụt MỘT DẤU CÁCH - Markdown vẫn render, người và AI
vẫn đọc thấy - biến mất khỏi 3f, 3g, 5, 6, 7, 7b, 7b2, 7e, 7f, 7g và
dem_qua_han CÙNG LÚC. Giám khảo dựng kho có trọn một lượt deploy môi trường
CHẠY THẬT ghi mức A, còn ĐANG GHI, không plan, cộng một dòng VIEC trạng thái
ngoài từ vựng và ô Ghi lần TRỐNG - cả hai dòng thụt đúng một dấu cách - và bộ
in "hệ sạch". Một lần Prettier, một lần dán từ Word, một lần AI thụt lề cho đẹp
là kho mất trắng lưới, mà người dùng TIN là sạch. Nay nhận tối đa ba khoảng
trắng theo đúng GFM rồi strip trước khi tách ô.

TOÀN BỘ CÂY 00_Index LÀ VÙNG MÙ CỦA MỌI PHÉP SECRET. quet_secret loại
THU_MUC_HE_THONG nên bỏ qua cả `_so`, `_lich_su`, `_inbox`, `_thu_staging` và
các bản backup - tức bỏ qua đúng chỗ secret THẬT rơi vào. Sáu kho lọt, trong đó
lối `_thu_staging` là lối TỰ ĐỘNG: khách MAIL file prod.env, pipeline X3E tự
lưu, COMMITTED, "hệ sạch" - không ai phải làm gì sai. Nay quét cả cây, chỉ bỏ
đúng FILE CỦA BỘ (chính tài liệu bộ trích `sk_live_...` làm ví dụ nên quét
chúng là tự báo oan mình), 7e3 đổi glob thành rglob, trần đọc file văn bản nới
256 KB lên 2 MB.

LƯỚI SECRET CHỈ BẮT NHÃN TIẾNG ANH, TRONG MỘT BỘ TIẾNG VIỆT CHO CÔNG TY VIỆT.
"Mật khẩu: Congtruong@2026x" im, "password: Congtruong@2026x" lệch. Mật khẩu
tới kho bằng chữ "mật khẩu". Cả ba lưới 7e, 7e2, 7e3 dùng chung khuôn nên cùng
mù. Giám khảo đã đo khuôn mới: bắt 6/7 ca xấu, 0/9 ca viết ĐÚNG cách X5 mục 1b
dặn, 0 ca bắt thêm khi quét trọn kho pilot cộng trọn bộ luật. Giữ nguyên ràng
buộc dấu `:`/`=` và giá trị >=12 ký tự có chữ số - đó mới là thứ chặn báo oan.

BÁO OAN LẦN THỨ CHÍN, MƯỜI VÀ MƯỜI MỘT - và lần thứ mười một là kiểu tệ nhất:
KHÔNG CÓ LỐI THOÁT HỢP LỆ.
- 7f tố ô "Ở đâu" mang tombstone `[đã xóa theo Q-...]`, trong khi X5 mục 7b BẮT
  thay ô đó khi chính tên file mang dữ liệu cá nhân. 7f đã miễn ô TRỐNG mà quên
  miễn tombstone, dù 8e và 12k đã miễn đúng chuỗi này.
- 3f tố dòng chuẩn chỉ vì có khoảng trắng sau dấu `|` cuối.
- 8e tố "hết hạn" cho hợp đồng ĐÃ GIA HẠN bằng phụ lục. Giám khảo thử MỌI lối
  thoát - đổi Trạng thái, ghi chú vào ô Cờ, ghi mũi tên ngày mới - đều vẫn đếm.
  Lối DUY NHẤT hết đếm là GHI ĐÈ ô Hết hạn của bản ĐÃ KÝ bằng một ngày mà bản
  ký không hề nói. Bộ dẫn người dùng THẲNG tới thao tác làm sai lệch sổ. Nay
  TAILIEU có từ vựng HẾT HIỆU LỰC và ĐÃ GIA HẠN, và bộ đếm thôi tính dòng đó.

MÃ G CHỈ NHẬN NN HAI CHỮ SỐ: `\d{2}` không neo cuối nên "-101" bị cắt thành
"-10". Kho vượt 99 lượt một cửa một ngày (AUTOMATED quét mail theo giờ, hay
ngày nạp hàng loạt theo X9 mục 3b) thì 8 và 8d tố ngược VĨNH VIỄN - sinh lại
bảng bao nhiêu lần cũng lệch. Và đúng như câu cảnh báo của chính 8d: phiên sau
đọc watermark "-99" rồi cấp lại "-100", sinh mã TRÙNG THẬT.

NGƯỠNG @NHIP ĐỌC XUYÊN QUA MỤC KHÁC: `\D*` khớp cả xuống dòng, nên mục còn <N>
thì con trỏ chạy sang mục kế lấy chữ số đầu tiên gặp được. @NHIP.INBOX lấy 30
của @NHIP.DEMSTAGING; @NHIP.RALAI lấy số 3 từ chữ "X3, X4" ở TIÊU ĐỀ mục. Đo
được: biên bản nghiệm thu nằm _INBOX 18 ngày mà bộ im. Nay đọc trong ĐÚNG KHỐI.

PHÉP MỚI: 7h (profile AUTOMATED: lượt máy tự làm chỉ được mức A - giám khảo
dựng phiên hẹn giờ ban đêm PHÁT HÀNH VÀ GỬI công văn giục thanh toán cho chủ
đầu tư ở mức C, exit 0, im lặng; X5 nói ô Phiên `.AUTO.` là dấu DUY NHẤT phân
biệt việc máy với việc người, dấu đó có mà không phép nào đọc) · 13m (QUYETDINH:
ô Thay bởi và ô Trạng thái là một CẶP - dòng tự khai người kế nhiệm mà vẫn đứng
HIỆN HÀNH thì sổ có hai quyết định nói ngược nhau về cùng một việc, đúng thứ
DUY NHẤT sổ này tồn tại để chặn).

14e SIẾT: giám khảo lách được bằng `not []` thay cho `True`. Nay chặn cả
`not <hằng rỗng>`, `len(<hằng rỗng>) == 0` và so sánh hai hằng.

ĐO ĐƯỢC: bàn thử 16/16, gồm sáu ca ĐÚNG LUẬT (mô tả LOẠI secret bằng tiếng
Việt, mật khẩu đã xoay, chuỗi QUYETDINH thay đúng cách, giấy đã gia hạn, mã G
ba chữ số khai đúng, phiên AUTO mức A).

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(z1) MỚI: trần 1d 22.000 BẤT KHẢ THI - template X0 rỗng đã 19.274 ký tự = 88%
trần, công ty REGULATED trả lời trọn nhóm B của X9 là 22.497 và còn ~1.216 ký
tự dấu C12 nữa; cần tách X0 thành phần THAM SỐ (tính trần) và phần CHÚ GIẢI
(không tính) · (z2) MỚI: @KHO.CU không có dạng "Ở đâu" nào hợp lệ, mọi công ty
vừa chuyển kho hoặc ôm LỆCH 9 vĩnh viễn hoặc nhân đôi kho · (z3) MỚI: dự án
NGỪNG còn nghĩa vụ bảo hành 12 tháng thì X0 C2 chỉ cho HỦY hay bàn giao, cả hai
đều sai sự thật · (z4) MỚI: NHATKY vượt 500 dòng trong MỘT quý không có lối
tách nào được luật mô tả · (z5) MỚI: 3f, 3g, 5, 6 chưa đọc `_lich_su` trong khi
3c, 3d, 3e, 7, 12l thì có · (z6) MỚI: cot_thu trả rỗng im lặng khi header đổi
tên · (a) (b) (c) (e) như cũ.

## Vòng 57: trục tất định thứ chín

Backlog (g). `loc_ban_chinh` chọn "bản chính" trong một tập file, và nó TẤT
ĐỊNH nhờ đúng một chữ `sorted` ở đầu hàm - tính chất mà không ai khẳng định.
Bỏ chữ đó đi thì kết quả theo thứ tự glob của hệ tệp, và trước vòng 57 bộ vẫn
xanh trọn.

Hậu quả nếu mất: cùng một kho, hai máy (hay hai lượt) chọn hai bản NHATKY khác
nhau làm bản chính, nên mã G cao nhất khác nhau, watermark khác nhau, và lượt
ghi sau cấp lại một mã ĐÃ DÙNG - đúng thứ hỏng nặng nhất mà cả nhóm phép 3 và 8
tồn tại để chặn.

Bộ đã đo tất định 8/8 trục ở các vòng trước (PYTHONHASHSEED, bốn locale kể cả
bẫy chữ I của tr_TR, NFC/NFD, mười lượt giống nhau từng byte). Đây là trục thứ
CHÍN và chưa ai đo: THỨ TỰ ĐẦU VÀO. Ca ghim đưa cùng một tập ba file vào theo
sáu hoán vị và đòi đúng MỘT kết quả. Đo lại bằng đột biến: bỏ `sorted` thì
phép 11 đỏ ngay.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(a) hash QUYETDINH · (b) phép 5 đối chiếu số cột với X5 mục 4 · (c) khuôn bản
sao · (e) bản rà cho sổ CSV.

## Vòng 56: cache quan sát vào lưới

Backlog (k). `_so/_quan_sat_truoc.json` là MÁY SINH và giữ mốc "lần đầu thấy
sha này". Luật ổn định hai lượt dựa TRỌN vào nó, mà trước vòng 56 không phép
nào nhìn nó: mốc TƯƠNG LAI làm mọi file lập tức "đủ ổn định", tức bộ công nhận
HIỆN HÀNH một file có thể đang được ghi hay đồng bộ dở, rồi đóng sha đó vào
TAILIEU làm mốc toàn vẹn.

Phép 0n, và NÓI THẲNG GIỚI HẠN của nó ngay trong chú thích: đây KHÔNG phải rào
chống giả mạo có chủ ý - ai sửa được cache thì cũng sửa được sổ. Nó bắt hai ca
THẬT hay xảy ra: cache hỏng cấu trúc (đồng bộ mây cắt ngang, sửa tay nhầm) và
mốc tương lai (đồng hồ máy sai, hay một lượt sinh lại cẩu thả). Khai đúng tầm
thì nó vẫn đáng có; khai quá lời thì lại đúng lớp "lời khai vượt cái máy làm"
mà chiến dịch này đi diệt.

Ca lành của phép này lúc đầu tôi dựng SAI - trỏ một file không có thật nên
chính bộ quan sát kêu, và ca mất nghĩa. Cache RỖNG mới là hình dạng đúng cho
kho chưa có file nghiệp vụ nào, tức kho lành của phép 13.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(a) hash QUYETDINH · (b) phép 5 đối chiếu số cột với X5 mục 4 · (c) khuôn bản
sao · (e) bản rà cho sổ CSV · (g) loc_ban_chinh tất định nhờ sorted mà không ai
ghim.

## Vòng 55: liên kết treo ở hai sổ còn lại

Backlog (h). 7c gom mã CÓ THẬT từ cả năm sổ, nhưng chỉ soi ô liên kết của VIEC,
QUYETDINH và THU. PLANNING có ô "Việc" trỏ mã việc, DUKIEN có ô "Nguồn" trỏ mã
tài liệu - treo ở hai chỗ đó thì không ai kêu.

Hậu quả cụ thể: plan mức C trỏ một mã việc gõ sai thì phép 3d (lượt mức C phải
có plan mang mã G tương ứng) VẪN XANH, vì 3d so mã G chứ không so mã việc. Cả
chuỗi duyệt mức C - thứ đắt nhất của bộ - đứng trên một liên kết gãy mà không
ai biết. Bàn thử 4/4, gồm hai ca không báo oan: PLANNING trỏ mã có thật, và
DUKIEN ô Nguồn ghi văn xuôi thường ("email đối tác") chứ không phải mã.

Kèm một ca I3 ghim riêng phần MỚI: 14b chỉ đòi 7c kêu ở ĐÂU ĐÓ, nên hai cột vừa
thêm có thể bị gỡ lại mà không lưới nào biết.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(k) cache _quan_sat_truoc.json giả mạo được · (a) hash QUYETDINH · (b) phép 5
đối chiếu số cột với X5 mục 4 · (c) khuôn bản sao · (e) bản rà cho sổ CSV ·
(g) loc_ban_chinh tất định nhờ sorted mà không ai ghim.

## Vòng 54: đính kèm hết biến mất im lặng

Backlog (y), mục cuối trong danh sách hội đồng vòng 18 giao.

Hai biến thể, cả hai từng "hệ sạch":
(a) HopDong_daky.pdf nằm trong staging, mail COMMITTED, nhưng chưa hề chép ra
    chỗ xếp và cột "Đính kèm" của THU để RỖNG. X3E mục ĐÍNH KÈM nói rõ trình
    tự: chép về chỗ xếp, tính sha256, trỏ vào cột Đính kèm của THU, RỒI MỚI
    được append COMMITTED.
(b) mọi đính kèm khai cờ `de_ngoai` với lý do "qua tran", không dòng TAILIEU
    nào trỏ nguồn, không VIEC "tải tay" nào - X3E mục 2 bắt buộc CẢ HAI.

12j chỉ kiểm sha và byte của file TRONG staging; kiem_payload với de_ngoai chỉ
đòi `ly_do` là chuỗi; không phép nào nối `dinh_kem` của payload với nội dung
THU, TAILIEU hay VIEC.

Hậu quả nặng vì nó IM LẶNG hai lần: hợp đồng đã ký số gửi qua mail được coi là
"đã nạp" (có COMMITTED, có trong registry) nên lượt quét sau BỎ QUA VĨNH VIỄN,
trong khi file chỉ nằm trong _thu_staging chờ bị dọn - hoặc chưa bao giờ rời
hộp thư và không việc nào nhắc tải. Sổ không có nó, digest không nhắc, registry
chặn nạp lại.

Phép 12n nối hai đầu đó: mail COMMITTED thì mỗi đính kèm thường phải có TÊN
hoặc 12 ký tự đầu sha256 xuất hiện ở THU hay TAILIEU; mục để ngoài phải có ở
TAILIEU (nguồn) VÀ ở VIEC (việc tải tay).

Và một điều đáng ghi: fixture "email bộ sạch PASS hết" - bàn nền của cả nhóm
phép 12 - THẬT RA CHƯA SẠCH theo X3E. Nó có mail COMMITTED mang đính kèm f.pdf
mà không sổ nào nhắc tới. Nó "sạch" suốt bấy lâu chỉ vì không ai kiểm. Nay
fixture ghi f.pdf vào TAILIEU đúng như luật đòi, cộng hai ca âm mới.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(k) cache _quan_sat_truoc.json giả mạo được · (a) (b) (c) (e) (g) (h) như cũ.

## Vòng 53: backup ra khỏi vùng nổ

Backlog (v). Hội đồng vòng 18 tạo 7 bản backup ĐÚNG X5 mục 7
(`_so\_lich_su\backup_<ngày>\`) rồi diễn OneDrive rollback trọn `_so` - đúng
kịch bản mà chú thích của phép 0k2 tự khai làm lý do tồn tại. 7/7 bản chết cùng
lượt. Máy bắt được mất sổ (phép 0 và 0k) và chỉ lối khôi phục "lấy từ bản sao
lưu ở thiết bị khác" - nhưng đo trong X0: chữ "sao lưu" xuất hiện ĐÚNG MỘT LẦN
và là câu văn xuôi, 0 tham số @, 0 dòng C12, 0 ngưỡng ở C9; trong kiem_van_hanh
chuỗi "backup_" xuất hiện đúng một lần và là để LOẠI TRỪ. Tức lối thoát mà
chính máy chỉ ra KHÔNG CÓ THỦ TỤC NÀO TRONG BỘ TẠO RA NÓ. Với kho ổ máy đơn -
cấu hình README khai là được hỗ trợ - đó là mất vĩnh viễn.

@KHO.SAOLUU vào X0 C1, một câu ở X5 mục 7, và phép 0m đọc lại giá trị đó.
Chống báo oan theo đúng khuôn 0g đã dùng cho .git ở kho vừa clone: thư mục khai
mà KHÔNG thấy thì chỉ NHẮC (ổ ngoài chưa cắm là chuyện thường, không kết luận);
CHỈ khi thư mục CÓ THẬT mà bản mới nhất quá 7 ngày mới là LỆCH - lúc đó mới
biết chắc người dùng đã dựng nơi sao lưu rồi bỏ bê. Bàn thử 4/4.

Và một quyết định NGƯỢC hướng thường thấy: dòng nhắc "chưa khai @KHO.SAOLUU"
đã bị BỎ, dù nó là thứ tự nhiên nhất để thêm. Lý do: nó in ở MỌI lượt RA_SOAT
cho tới khi người dùng khai, tức một khoản thuế vĩnh viễn trên trần đầu ra -
trong khi @KHO.SAOLUU vốn đã là mục trống của X0 C12 và phép 0i canh đúng việc
đó. Hai lưới cho một nghĩa vụ, cái thứ hai tốn chỗ mỗi phiên.

Hai trần trả nợ NGAY TRONG LƯỢT VAY, không nâng cái nào: X5 vượt 20.000 sáu ký
tự (rút gọn chính đoạn vừa thêm), và trần đầu ra 13c vượt 143 ký tự (bỏ dòng
nhắc ở trên). Cả hai đều là thứ người dùng thật sự gánh.

TÁCH LỊCH SỬ, backlog (s) - trả nợ trần của vòng 48. GHICHU phình một mục mỗi
vòng và vừa chạm trần lần thứ hai. Vòng 48 nâng 115.000 lên 130.000 và ghi
thẳng đó là NỢ, kèm câu "trần này KHÔNG được nâng lần nữa trước khi tách". Nay
giữ đúng lời: các mục vòng 1 tới 25 sang GHICHU_LICHSU, GHICHU 131.366 xuống
88.531 - đúng con số 37% đã đo ở vòng 48 - và bản gộp 239.489 xuống 196.653.
Chi phí thật của GHICHU không phải token phiên (nó ngoài mọi route) mà là X9
mục 3c CHÉP NÓ VÀO KHO MỌI CÔNG TY mỗi lượt nâng cấp. Trần HẠ về 100.000 chứ
không giữ chỗ vừa vay.

Nới allow-list cho file mới mà không thêm nghĩa vụ là mở một lỗ - xóa file lưu
trữ đi thì 25 vòng lịch sử biến mất mà không phép nào kêu. Phép 1f đòi ba thứ:
file tồn tại, GHICHU trỏ tới nó, và tập số vòng của HAI file gộp lại KHÔNG
THỦNG. Phép 14d bắt ngay lượt đầu vì tôi quên khai 1f vào danh bạ.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(k) cache _quan_sat_truoc.json giả mạo được · (y) đính kèm của mail đã COMMITTED
có thể không để lại dấu nào ở sổ · (a) (b) (c) (e) (g) (h) như cũ.

## Vòng 52: bản mới bị giấu, nhánh tự deploy, và manifest hết là tờ giấy

Ba mục backlog nặng nhất còn lại của hội đồng vòng 18.

(w) BỘ QUAN SÁT CHỈ NGƯỜI DÙNG VÀO BẢN CŨ NHẤT. Ba file cùng một biên bản
nghiệm thu trong 04_Trao_doi: bản gốc, "BienBanNghiemThu (1).docx" (1,720 tỷ),
"BienBanNghiemThu (2).docx" (đối tác đòi giảm 5%, còn 1,634 tỷ). Đầu ra: ĐỀ
XUẤT đúng BẢN GỐC, hai bản mới không xuất hiện MỘT DÒNG NÀO - chúng khớp
MAU_TAM nên bị loại lặng lẽ. Khuôn " (n)" là thứ Windows và Chrome tự đặt mỗi
lần tải lại đính kèm cùng tên, tức chuyện tuần nào cũng xảy ra khi đối tác gửi
bản sửa. Kế toán nạp bản 1,720 tỷ trong khi bản chốt là 1,634: chênh 86 triệu
vào DUKIEN mức nguồn A rồi ra hóa đơn. Mỉa mai: khuôn anh em `-<TênMáy>` của
OneDrive thì CÓ cảnh báo NGHI BẢN SAO từ vòng 6-8; riêng khuôn này thì im.
Phép 11b so sha với bản gốc cùng tên: TRÙNG thì im (bản sao đồng bộ thật, giữ
nguyên hành vi cũ), KHÁC thì báo. Bàn thử 4/4.

(n) X5 MỤC 1b BẮT PHÂN BIỆT "MERGE VÀO NHÁNH MÀ CI/CD TỰ DEPLOY CHẠY THẬT LÀ
C" - MÀ SCHEMA KHÔNG CÓ Ô NÀO KHAI NHÁNH ĐÓ. Trong pilot vòng 18, công ty khai
đủ 5/5 trường mà vẫn không có căn cứ nào trong X0 để trả lời "merge PR 210 vào
main là A hay C", nên lượt đó đi mức A và máy đồng ý. Merge PR là thao tác
nhiều lần nhất trong ngày của công ty phần mềm và là lối vào production phổ
biến nhất; luật gác đúng chỗ hiểm nhưng phụ thuộc một dữ kiện bộ KHÔNG BAO GIỜ
HỎI, nên mọi lượt merge rơi về mức A theo mặc định thực tế - ngược hẳn "không
dòng nào khớp thì lấy C" của X5 mục 1. Trường thứ SÁU của @DUAN.PHANMEM, và 7g
đọc nó: merge vào đúng nhánh đó mà ghi khác mức C là lệch, dù câu ghi không
nhắc chữ nào về production. Khai "không có auto-deploy" là hợp lệ và đúng hiện
trạng phần lớn shop nhỏ. Bàn thử 4/4.

(x) MANIFEST DỌN STAGING LÀ TỜ GIẤY. Mail đã COMMITTED, staging đã xóa,
manifest khai `eml_final_path: 04_Trao_doi/m1.eml` - mà file đó KHÔNG hề tồn
tại. Nguyên văn thư biến mất vĩnh viễn và 12j in PASS, vì nó chỉ kiểm manifest
là CHUỖI RỖNG HAY KHÔNG, không bao giờ `.is_file()`. X3E chỉ cho dọn khi .eml
đã chuyển sang vùng lưu chính; với profile REGULATED đây là nguyên văn thư của
một hợp đồng đã ký. Một lượt dọn hỏng (đích chưa mkdir, đồng bộ mây chưa lên,
đường dẫn gõ sai) xóa sạch bằng chứng mà bộ vẫn khai "hệ sạch" - kho hết bằng
chứng và không ai biết cho tới lúc ra tòa. Nay 12j MỞ FILE RA XEM: đủ đường
dẫn, đúng sha256, và từng đính kèm cũng phải có thật. Hai fixture cũ vốn đang
ghim đúng cái luật yếu đó nay phải đặt file thật xuống đĩa, cộng hai ca âm mới.

Trần kiem_tra_bo nâng 135.000 lên 150.000; gate không đổi: file này ngoài mọi
route và từ vòng 46 không còn trong bản gộp, nên nó không tốn token của phiên
nào. Trần ĐẦU RA (13b, 13c) - thứ người dùng thật sự gánh - KHÔNG nâng: bốn
phép mới đẩy kho cận xấu lên 5.246/5.200, trả nợ bằng cắt đuôi nhãn tám phép,
về 5.1xx.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(k) cache _quan_sat_truoc.json giả mạo được · (s) tách lịch sử GHICHU (giảm
37%) · (v) backup theo X5 mục 7 nằm TRONG _so nên chết cùng lượt rollback mà
0k2 lấy làm lý do tồn tại · (y) đính kèm của mail đã COMMITTED có thể không để
lại dấu nào ở sổ · (a) (b) (c) (e) (g) (h) như cũ.

## Vòng 51: tầng HẠN vào lưới - bảng hết khai "bàn sạch" hộ sổ

Backlog (t) và (u), hai mục nặng nhất còn lại của hội đồng vòng 18. Đo trên kho
pilot của giám khảo, ngày 28/8/2026:

  việc V-002 quá hạn 3 ngày · dữ kiện D-002 quá mốc rà lại 119 ngày · chứng
  thư số ký điện tử T-003 HẾT HẠN 59 ngày · mục _INBOX kẹt 9 ngày (ngưỡng
  công ty tự khai là 3)

và cùng lượt chạy đó: 35 PASS, 0 LỆCH, "hệ sạch", bảng ghi "bàn sạch".

Nguyên nhân: 8b chỉ đếm NHÃN có mặt, và ở dạng rút gọn "bàn sạch" chỉ đòi hai
nhãn - không một giá trị nào bị đối chiếu với sổ. Mà bảng là mặt phẳng DUY NHẤT
banner mở phiên đọc, và nó do AI tự sinh từ trí nhớ. X4 xếp chín dòng rà (7-11,
13-15, 21) vào nhóm "kiểm tay" trong khi cả chín đều là SO NGÀY trên đúng những
cột mà dong_bang đã parse sẵn cho 3g và 7c - 29% danh mục rà là số học tầm
thường mà vẫn giao cho trí nhớ con người.

PHÉP 8e: đếm bốn họ quá ngưỡng từ sổ (việc quá hạn · dữ kiện quá mốc rà lại ·
giấy tờ hết hạn hay sắp hết trong ngưỡng cảnh báo · mục _INBOX chưa nạp quá
ngưỡng), ngưỡng đọc từ X0 C9. Bảng khai "bàn sạch" mà sổ còn mục nào là LỆCH;
bảng khai số khác số thật cũng là LỆCH. Bàn thử 8/8: bắt cả bốn họ, và im với
bốn ca đúng luật gồm việc quá hạn nhưng ĐÃ XONG và mục _INBOX vừa ghi hôm nay.

TẤT ĐỊNH - một khoản nợ vòng này phải trả trước khi vay: hàm đếm nhận `hom_nay`
để fixture tiêm ngày giả, đúng khuôn `bay_gio` mà quet_ho đã dùng từ trước. Và
ngày trong fixture đổi từ 2026-12-31 sang 2099-12-31: giữ nguyên thì sang năm
sau nó thành QUÁ KHỨ và ca thử hỏng dần theo thời gian thật - loại nợ tất định
mà bộ đã đo 8/8 trục sạch ở các vòng trước, không nên tự đẻ lại.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(k) cache _quan_sat_truoc.json giả mạo được · (n) schema @DUAN.PHANMEM chưa có
ô khai nhánh CI/CD tự deploy · (s) tách lịch sử GHICHU (đo được giảm 37%) ·
(v) backup theo X5 mục 7 nằm TRONG _so nên chết cùng lượt rollback mà 0k2 lấy
làm lý do tồn tại; X0 không có tham số nào khai nơi sao lưu NGOÀI kho · (w)
file trùng tên khuôn " (n)" bị loại lặng lẽ, bộ chỉ người dùng vào bản CŨ NHẤT
trong khi hai bản mới hơn bị giấu · (x) manifest dọn staging không ai mở file
bằng chứng ra xem · (y) đính kèm của mail đã COMMITTED có thể không để lại dấu
nào ở sổ · (a) (b) (c) (e) (g) (h) như cũ.

## Vòng 50: hội đồng vòng 18 - lưới secret có lỗ to bằng chính thứ nó canh

Điểm vòng 18 (chấm bản vòng 47): KHÔNG MISS 6,0 · VẬN HÀNH 7,0. Giám khảo
KHÔNG SAI vòng 16 cũng về muộn, chấm bản vòng 45 được 7,4 và tự kiểm lại ở
HEAD: 5/6 phát hiện của họ đã đóng.

LƯỚI SECRET CÓ LỖ TO BẰNG CHÍNH THỨ NÓ CANH. Vòng 48 dựng 7e2 đọc tập `moi`
của quet_ho, mà quet_ho loại `f.name.startswith(".")` TRƯỚC đó - nên `.env`,
TÊN FILE SECRET PHỔ BIẾN NHẤT, chưa bao giờ tới được lưới, và mẫu `\.env(\.|$)`
là mã chết cho ca trần. Đối chứng: prod.pem và id_rsa cùng chỗ thì BỊ BẮT,
.env thì LỌT. Tệ hơn: `_so\_quan_sat_bo.txt` - file text NGƯỜI DÙNG SỬA TAY
ĐƯỢC - cũng lọc trước, nên thêm một dòng "02_Ky_thuat" là tắt hẳn lưới secret
cho cả thư mục, không để lại dấu vết nào. Một luật TUYỆT ĐỐI của X5 mục 1b bị
vô hiệu bằng một dòng text. Vá: hàm quet_secret quét ĐỘC LẬP, không qua lọc
dotfile và không chịu bo_them. Bàn thử 5/5, gồm hai ca đúng luật (.gitignore
thường, và _quan_sat_bo loại thư mục video - đúng mục đích X5 khai).

LỚP "PHẠT NGƯỜI DÙNG VÌ LÀM ĐÚNG", LẦN THỨ BẢY VÀ THỨ TÁM, trong cùng một vòng:
- Lần 7: phép 6 BẮT tách sổ THU khi vượt 500 dòng; tách xong theo đúng X5 mục 7
  thì 12l lệch 400 DÒNG VĨNH VIỄN, vì nó chỉ đọc sổ sống chứ không đọc
  `_so\_lich_su\`. Lối thoát duy nhất người dùng nghĩ ra là xóa
  _thu_ap_dung.json - tự tay phá rào chống nạp trùng của X3E. Phép 3c, 3d, 3e,
  7 đã học đọc _lich_su từ vòng 41; 12l là vế còn sót.
- Lần 8: nhân viên nghỉ, thu hồi máy, công ty gỡ cửa CUA2 khỏi X0 C1 ĐÚNG THỦ
  TỤC mức C (plan, QUYETDINH, rev mới) -> 7b tố "cửa ma" vĩnh viễn, không bao
  giờ tắt được vì mã G cũ nằm trong NHATKY chỉ-thêm. GIỮ NGUYÊN dòng cửa của
  một cái máy đã không còn thì "hệ sạch": bộ THƯỞNG lời khai sai, PHẠT lời khai
  đúng. Và thông điệp dạy sai - nói "gõ nhầm một ký tự", đẩy người dùng đi sửa
  NHATKY, đúng thứ 0k và 3e sinh ra để chặn. X0 C2 có "đang chạy | NGỪNG" cho
  dự án, C1 có @KHO.CU cho kho ngừng; chỉ CỬA là không có đường khai ngừng.
  Thêm @KHO.CUA_NGUNG, không phải sửa dòng mã nào.

VĂN XUÔI MẪU CỦA X0 TỰ KHAI HỘ MỘT CỬA - tôi bắt được cái này khi dựng ca thử
cho vế trên, và nó đáng ghi vì cùng lớp với defect của vòng 46: dòng hướng dẫn
C1 viết nguyên văn "<thêm CUA2... nếu kho mây có nhiều máy cùng vào>", mà 7b
gom cửa đã khai bằng regex trên TRỌN khối C1. Với MỌI công ty, CUA2 luôn được
coi là đã khai. Tức đúng cửa thứ hai - cửa dễ gõ nhầm nhất, và là cửa đầu tiên
sinh ra khi công ty thêm máy - là cửa DUY NHẤT lưới cửa-ma không bao giờ bắt.

MỐC CHÍNH THỨC MẤT LƯỚI CHỈ VÌ CÁCH VIẾT MỘT Ô. `any(t in h for t in BAT_BIEN)`
so chuỗi TUYỆT ĐỐI, nên sửa đè một hợp đồng ĐÃ KÝ: ô ghi "ĐÃ KÝ" thì 10a kêu
(mức C), còn "Đã ký", "da ky", "ĐÃ KÝ (ban scan 19/8)" thì 10a IM và chỉ còn
10b (mức A); thêm bỏ trống ô sha256 thì "hệ sạch". Bốn cách viết đời thực làm
thao tác chạm mốc chính thức tụt hạng hay biến mất. Nay so BỎ DẤU và cho phép
chú thích kèm sau.

MIEN_TRU RỖNG DẦN THẬT: 16 xuống 8. Nguyên nhân cấu trúc là 14b chỉ nhìn tập
phủ của PHÉP 13, trong khi từ vòng 47 bộ có thêm PHÉP 15 cũng ép trạng thái
thật - chỉ là tập phủ của nó không ai dùng. Nối hai tập thì tám phép NGHIỆP VỤ
NẶNG NHẤT (0, 1, 3a, 6, 7, 9, 10a, 10b) ra khỏi vùng miễn trừ mà không phải
viết thêm ca nào. Đo lại bằng đục ruột: 8/8 bị bắt, hội đồng vòng 17 đo 0/8.

CÁC VÁ CÒN LẠI: 3g phủ nốt sổ THU và coi ô Trạng thái RỖNG của THU là lệch
(dòng rỗng rơi khỏi bộ đếm CHỜ TÔI của bảng và digest, tức luồng khách đang
chờ trả lời biến mất) · cot_thu GIỮ ô rỗng, vì lọc nó ra là mở lối thoát cho
12f và 12i: bỏ trống Conversation-ID thì mỗi thư trong một hội thoại được cấp
một mã #L- mới · khi _so bị khôi phục nhầm mà neo ngoài _so còn mã G thì máy
in CẢNH BÁO thay vì để dòng "CHƯA ghi lần nào" nằm cạnh dòng tố mất 5 mã -
người dùng đang hoảng đọc câu đầu bảng rồi ghi tiếp là cấp lại mã đã dùng ·
7d hết cho trường này ăn ké chữ của trường kia (`repo git.cty.vn/app` một
mình từng thỏa luôn "thành phần chính"), nay bỏ đoạn repo ra trước khi dò bốn
trường còn lại - mục cuối còn mở của giám khảo KHÔNG SAI.

ĐO ĐƯỢC: 9/9 đột biến nhắm vào chính các lưới mới bị bắt · 8/8 phép vừa rời
MIEN_TRU thật sự có lưới · 6/6 đột biến nới ngưỡng bị bắt · 5/5 ca secret ·
4/4 ca 7d · 5/5 ca 3g trên THU · 3/3 ca cửa thu hồi.

BACKLOG còn: (i) phần hành vi của phép 14 · (j) vòng đời _inbox và _da_nap ·
(k) cache _quan_sat_truoc.json giả mạo được · (n) schema @DUAN.PHANMEM chưa có
ô khai nhánh CI/CD tự deploy · (s) tách lịch sử GHICHU (giảm 37%) · (t) MỚI:
toàn bộ tầng HẠN không ai thi hành - bảng khai "bàn sạch" trong lúc chứng thư
số đã hết hạn 59 ngày, việc quá hạn, dữ kiện quá mốc rà lại 119 ngày; X4 xếp
9 dòng rà (7-11, 13-15, 21) vào "kiểm tay" dù cả 9 đều là so ngày trên đúng
những cột dong_bang đã parse sẵn · (u) MỚI: @NHIP.INBOX là tham số chết, mục
_INBOX kẹt không mặt phẳng nào hiện · (v) MỚI: backup theo X5 mục 7 nằm TRONG
_so nên chết cùng lượt rollback mà 0k2 lấy làm lý do tồn tại; X0 không có
tham số nào khai nơi sao lưu ngoài kho · (w) MỚI: file trùng tên khuôn " (n)"
bị loại lặng lẽ, bộ chỉ người dùng vào bản CŨ NHẤT · (x) MỚI: manifest dọn
staging không ai mở file bằng chứng ra xem · (y) MỚI: đính kèm của mail đã
COMMITTED có thể không để lại dấu nào ở sổ · (a) (b) (c) (e) (g) (h) như cũ.

## Vòng 49: ngưỡng vào lưới, và máy hết nói hai điều trái nhau cùng lúc

(q) MỌI HẰNG NGƯỠNG ĐỨNG NGOÀI LƯỚI. Chỉ NGAN_SACH có phép 9b canh - khai ở
BENCHMARK, đối chiếu với hằng trong mã. Sáu ngưỡng RUNTIME thì không ai canh:
hội đồng vòng 17 nới `n > 500` thành `n > 500000`, `<= 4200` thành `<= 420000`,
trần đầu ra 2.700 thành 270.000, và CẢ SÁU con sống sót trọn bộ kiểm. Nới trần
là lối "vá" rẻ nhất khi bộ đỏ, và không có gì cản. Đối chứng của chính giám
khảo cho thấy khuôn 9b hiệu lực thật (nới một trần trong NGAN_SACH thì bị bắt
ngay), nên vòng này chỉ NHÂN RỘNG đúng khuôn đó: phép 9c, sáu ngưỡng runtime
khai ở BENCHMARK và đối chiếu với mã. Đo lại: 6/6 bị bắt, trước là 0/6.

(r) MÁY VỪA NÓI "HỆ SẠCH" VỪA NÓI "CÓ FILE NGOÀI SỔ". X4 dặn "Sạch thì một
dòng sổ khớp thực tế <ngày>", nhưng máy in ĐỀ XUẤT _INBOX rồi vẫn kết "hệ
sạch" với mã thoát 0. Phiên AI đọc dòng KẾT QUẢ, hay CI đọc mã thoát, sẽ ghi
NHATKY "sổ khớp thực tế" trong khi phụ lục hợp đồng đang nằm ngoài sổ - và
vòng rà quý sau đếm từ chính các dòng NHATKY đó nên sai theo. Nay ba trạng
thái, ba câu, ba mã thoát: 0 hệ sạch · 3 sạch về ràng buộc nhưng còn N mục chờ
vào sổ · 1 có lệch. Bàn thử 3/3. X4 nói rõ chỉ mã 0 mới được viết câu đó.

Kèm một lỗi của chính vòng này, bắt được nhờ danh mục trạng thái: bộ đếm mục
chờ vào sổ KHÔNG được đặt lại giữa hai lượt chạy trong CÙNG tiến trình, nên
mọi fixture chạy hai lượt đọc ra con số gấp đôi. Phép 15 đỏ ngay lượt đầu vì
nó ghim KẾT LUẬN chứ không ghim mỗi dòng ĐỀ XUẤT - ghim dòng ĐỀ XUẤT thì hoàn
nguyên "hệ sạch" vẫn xanh.

BACKLOG còn: (f) MIEN_TRU 16 phép chưa ai canh · (i) phần hành vi của phép 14 ·
(j) vòng đời _inbox và _da_nap · (k) cache _quan_sat_truoc.json giả mạo được ·
(n) schema @DUAN.PHANMEM chưa có ô khai nhánh CI/CD tự deploy · (s) tách mục
vòng <= 25 của GHICHU ra file lưu trữ, đo được giảm 43.029 ký tự tức 37% thứ
mọi công ty phải chép về kho · (a) (b) (c) (e) (g) (h) như cũ.

## Vòng 48: trả nợ backlog - secret vào kho bằng hai lối chưa ai soi

Vòng vá thuần backlog, không chờ hội đồng mới. Bốn mục nặng nhất của backlog
vòng 47 đã đóng, mỗi mục kèm ca của chính nó và một ca ĐÚNG LUẬT.

(m) SECRET VÀO KHO BẰNG HAI LỐI TỰ NHIÊN NHẤT, cả hai chưa ai soi. X5 mục 1b
cấm secret ở kho đồng bộ, ở sổ VÀ ở _INBOX; máy làm được hai phần ba - 7e soi
Ô SỔ, 7e2 soi TÊN FILE ngoài 00_Index. Còn lại:
  _so\_inbox\prod.env (file đối tác gửi mail rơi vào _INBOX)  -> IM
  02_Ky_thuat\bangiao_moitruong.md chứa DATABASE_URL prod và
  sk_live_... trong RUỘT, vì 7e2 chỉ dò TÊN                    -> IM, còn
                                                                 được MỜI vào sổ
File bàn giao môi trường là chỗ tự nhiên nhất một shop nhỏ viết chuỗi kết nối
prod. Nay 7e3 soi _INBOX (cả tên lẫn ruột) và 7e2 soi thêm RUỘT file kho.

(l) DUMP CSDL CHẠY THẬT MANG DỮ LIỆU KHÁCH kéo về kho: im, và bộ còn mời vào
sổ mức A. Kho nằm trên thư mục đồng bộ chung 12 người, tức CCCD khách đã đi ra
12 máy cá nhân. Phép 7e4, và CHỈ tính khi tên hay đường dẫn mang neo chạy thật
- dump của staging hay của máy dev không bị đá oan.

(o) XÓA PHÁP LÝ KHÔNG LAN. X5 mục 7b bắt trung hòa cả dòng TAILIEU VÀ dòng THU
trỏ file đã xóa. Bỏ sót THU thì công ty trả lời khách "đã xóa xong" trong khi
sổ còn tên đối tác, tiêu đề luồng, Message-ID và sha256 của file - một lượt
kiểm tra của khách hay cơ quan quản lý là vỡ, và chính lưới an toàn đã cấp giấy
"hệ sạch". Phép 7b2 lan tombstone tới mọi dòng trỏ mã đã xóa.

(p) TRẦN X0 CỦA KHO ĐANG CHẠY KHÔNG TỒN TẠI - cùng lớp "trần giả" của vòng 46.
NGAN_SACH chỉ chấm bản TEMPLATE trong bộ mẫu; file mà phiên CHAT nạp NGUYÊN VẸN
là X0 mang mã công ty, và không phép nào đo nó: bơm lên 49.591 ký tự (2,5 lần
trần khai) vẫn "hệ sạch". Không phải máy yếu - 1b và 1c kêu đúng khi bơm hai
view - mà thiếu đúng một phép. Phép 1d, trần 22.000 = trần template cộng 10%
chỗ điền giá trị thật, nên kho vừa cài (18.969 LITE, 19.059 REGULATED+EMAIL)
không bị kêu oan.

CHỐNG BÁO OAN, vì lớp lỗi này đã tái phát SÁU lần: file MẪU (.example, .sample,
.template, .mau, .dist) KHÔNG bị tính - `05_Mau\cauhinh.env.example` chứa
`DATABASE_URL=<điền>` là cách khai ĐÚNG. Bàn thử 9/9: bắt bốn ca thật, im với
năm ca đúng luật gồm cả file mẫu trong _INBOX, mô tả LOẠI secret theo nguyên
văn X5 1b, và dump của staging.

TRẦN ĐẦU RA: bốn phép mới đẩy đầu ra kho CẬN XẤU lên 5.325 ký tự, vượt trần
13c là 5.200. Tôi KHÔNG nâng trần: đó là số ký tự người dùng và phiên AI thật
sự gánh, nâng nó là chuyển chi phí sang họ. Trả nợ bằng cách CẮT ĐUÔI NHÃN của
tám phép (nhãn là thứ máy đọc; 29 dòng PASS đang chiếm 31% đầu ra), giữ nguyên
toàn bộ phần HƯỚNG DẪN trong các dòng LỆCH - đó mới là thứ người dùng không
rành máy tính cần. Về 5.16x ký tự, dưới trần, không nâng một trần nào.

BACKLOG còn: (f) MIEN_TRU 16 phép chưa ai canh · (i) phần hành vi của phép 14 ·
(n) schema @DUAN.PHANMEM chưa có ô khai nhánh CI/CD tự deploy · (q) mọi hằng
ngưỡng (2700, 5200, 4200, 500, 22000) đứng ngoài lưới, chỉ NGAN_SACH có 9b canh
· (j) vòng đời _inbox và _da_nap · (s) tách mục vòng <= 25 của GHICHU ra file lưu trữ: đo được giảm 43.029 ký tự, tức 37% thứ mọi công ty phải chép về kho theo X9 mục 3c · (k) cache _quan_sat_truoc.json giả mạo được
· (r) MỚI: "hệ sạch" và mã thoát 0 in ra ngay cả khi có ĐỀ XUẤT _INBOX, tức máy
vừa nói sạch vừa nói có file ngoài sổ · (a) (b) (c) (e) (g) (h) như cũ.

## Vòng 47: lời khai phần mềm thành thứ ĐIỀU KHIỂN mức duyệt, và lưới của lưới

Điểm vòng 17 (chấm bản vòng 46, bốn lăng kính về kịp): KHÔNG MISS 5,5 · VẬN
HÀNH 6,5 · THÔNG MINH 5,5 · ĐƠN GIẢN 7,5 · TOKEN 6,5. Vòng 16 các lăng kính
tương ứng là 7,6 · 7,8 · 7,6 · 9,0 · 9,1. ĐIỂM TỤT MẠNH, và tụt vì lý do TỐT:
vòng 17 giám khảo ĐO thay vì ĐỌC - dựng 101 kho hỏng, diễn 20 tình huống của
một công ty phần mềm 12 người trong hai tuần, sinh 69 đột biến mã nguồn, và
chạy tokenizer thật. Điểm cao ba vòng trước là điểm của việc đọc kỹ, không
phải điểm của bộ.

VÁ NẶNG NHẤT CHIẾN DỊCH - PHÉP 7g. Vòng 45 dựng @DUAN.PHANMEM với lý do khai
đủ thì vận hành mới chính xác. Pilot vòng 17 bác thẳng lý do đó: GIÁ TRỊ khai
KHÔNG ĐƯỢC ĐỌC LẠI Ở BẤT KỲ PHÉP NÀO. 7d chỉ dò xem chữ "chạy thật" có XUẤT
HIỆN trong X0 hay không. Đo trên kho thật, khai đủ năm trường rồi mà:

  deploy lên qlkh.bacha.vn (nơi chạy thật ĐÃ KHAI)   ghi mức A -> hệ sạch
  UPDATE trực tiếp CSDL chạy thật, 812 bản ghi       ghi mức A -> hệ sạch
  merge PR vào main mà CI/CD tự deploy chạy thật     ghi mức A -> hệ sạch

Ba thao tác hiểm nhất của một công ty phần mềm đi qua mức A "làm rồi báo một
dòng", không plan, không cái gật - và lưới an toàn cấp giấy "hệ sạch". Khai đủ
là THUẦN GIẤY TỜ. 7g đóng vòng: đọc GIÁ TRỊ nơi chạy thật, giao với động từ sản
xuất trong ô "Làm gì", đòi mức C theo X5 mục 1 MẶC ĐỊNH ĐÓNG. Bàn thử 7/7: bắt
cả ba ca trên, IM với deploy lên staging stg.qlkh.vn (host staging CHỨA tên dự
án, đúng bẫy chuỗi con), IM với deploy prod đã có plan mức C, IM với rollback
sự cố mức C, IM với việc thường. Từ vòng này, khai phạm vi tổ chức phần mềm
ĐỔI thứ máy làm - đó là điều kiện thứ hai của yêu cầu gốc, nay có máy giữ.

LỚP LỖI "PHẠT NGƯỜI DÙNG VÌ LÀM ĐÚNG", LẦN THỨ SÁU, ba chỗ cùng lúc:
1. Khuôn nhận dòng khai phần mềm là `^  ([A-Z0-9]{2,6})  +\S` - mã BẮT BUỘC
   2-6 ký tự HOA, một luật KHÔNG VĂN BẢN NÀO CỦA BỘ KHAI. Công ty đặt mã
   DATHANG hay webapp, khai ĐỦ cả năm trường, bị 7d VÀ 7d2 buộc tội và được
   bảo "khai phạm vi tổ chức trước" - đúng việc họ vừa làm; còn công ty khai
   THIẾU nhận CÙNG một thông điệp. README hứa "7d nêu đích danh trường còn
   thiếu nên không ai quên được": sai cả hai chiều.
2. 7e tố đúng dòng viết theo NGUYÊN VĂN X5 mục 1b. Luật dặn "sổ chỉ mô tả LOẠI
   secret và hệ liên quan"; viết "Loại secret: API key cổng thanh toán" thì bị
   tố lộ secret - ngay giữa lúc xử sự cố lộ khóa. Bài học người dùng rút ra sẽ
   là "đừng ghi gì về secret vào sổ", tức xóa luôn truy vết sự cố bảo mật. Nay
   sau dấu phân cách phải là GIÁ TRỊ (>=12 ký tự liền, có chữ số): 3/7 báo oan
   xuống 0/7, giữ nguyên 4/4 ca bắt thật.
3. Ô Trạng thái NHATKY RỖNG: 3a không thấy "ĐANG GHI", 3g bỏ qua ô rỗng, 3c
   chỉ soi dòng XONG - ba lưới đứng cạnh nhau, không lưới nào nhận. Cùng kho
   đó ghi "XONG" thì 3c kêu, ghi "-" thì 3g kêu; CHỈ giá trị rỗng lọt.

Ô "Ở ĐÂU" SAI KHUÔN TẮT LẶNG LẼ TOÀN BỘ LƯỚI TOÀN VẸN (hai giám khảo độc lập
cùng bắt). Bộ quan sát lọc dòng bằng h[5].startswith("Kho "), nên gõ "kho "
thường, "Kho:", hay bỏ tiền tố là phép 9, 10a, 10b BỎ QUA dòng đó. Đo: hợp
đồng ĐÃ KÝ bị sửa đè tại chỗ - đúng thứ luật cốt lõi 3 sinh ra để bắt - đi im
ở 4/5 cách gõ đời thực. Phép 7f đóng, và IM với cả bốn dạng hợp lệ lẫn dòng
trỏ thư mục có sha256 để trống.

PHÉP 15 - DANH MỤC TRẠNG THÁI HỎNG, thứ hai giám khảo vòng 16 gọi tên là bản
vá đáng giá nhất còn lại. Lưới đi từ PHÉP (13, 14, 14b, 14c) và lưới đi từ
TRẠNG THÁI phát hiện hai lớp lỗi khác nhau: phép 14 đi từ danh sách phép hiện
hữu nên theo định nghĩa không bao giờ hỏi được "bộ còn THIẾU phép nào". Phép
15 đi từ NGHĨA VỤ mà chính X4 khai là máy dò được, 16 ca, và 15b kẹp danh mục
vào lời khai đó nên thêm một dòng X4 mà quên ca là đỏ ngay. Đo giá trị riêng
của nó: đục ruột phép 3a thì CHỈ phép 15 bắt (3a nằm trong MIEN_TRU nên 14b mù).

LƯỚI CỦA LƯỚI. Giám khảo THÔNG MINH đo: kiem_tra_bo bắt 0/9 đột biến đục ruột
nhắm vào CHÍNH NÓ - phép 13, 14, 14b, 14c bảo vệ kiem_van_hanh mà không ai bảo
vệ chúng. Ba vá: 14d (danh bạ PHEP_BAT_BUOC đối chiếu mã nguồn - rút sáu phép
khỏi danh bạ rồi xóa thân hàm từng cho "đóng gói được"), 14e (cấm hằng True ở
vị trí điều kiện của kiem() và bao(), và thân hai hàm đó phải CÒN rẽ nhánh theo
tham số điều kiện; hằng False vẫn HỢP LỆ vì 7d2, 7e2, 10c cố ý dùng), và CA MỒI
cho vế I2 và vế I3. Chú thích cũ ngay trên chỗ ghim số ca khai "tắt I2, tắt I3
đều đỏ" - SAI, vì _dem đếm ca ĐĂNG KÝ chứ không đếm khẳng định ĐƯỢC THI HÀNH.
Lời khai sai NẰM TRONG chính cái lưới là thứ nguy hơn thiếu lưới: vòng sau tin nó.

ĐO SAU KHI VÁ: 9/9 đột biến nhắm vào chính các lưới mới đều bị bắt (trước vá
6/9; và lượt đo đầu tiên của tôi ra "8/8" là CON SỐ TỰ LỪA - tôi loại *_GOP.md
khỏi bản chép nên phép 9 đỏ ở mọi con, kể cả bản nguyên vẹn. Ghi lại đây vì
đó đúng lớp sai mà hội đồng bắt bộ suốt: đo mà không có đối chứng).

HỆ SỐ TOKEN: BENCHMARK tự nêu "việc còn lại duy nhất để đóng khoảng bất định"
là chạy một tokenizer sản xuất. Vòng 47 chạy - và bằng tokenizer CLAUDE, không
phải o200k_base như câu cũ chỉ định, vì bộ chạy trên Claude còn o200k là của
OpenAI và cho hệ số đẹp nhất (1,09x): chọn nó là tự chấm điểm dễ cho mình. Đo
độc lập hai lượt: thuế thường trực khai 2.316, đo THẬT 4.785 token, x2,07. Câu
"2,1x là TRẦN TRÊN chứ không phải đáp số" sai hai lần - 2,07x là số thật, và
X2_PHATHANH đo được 2,18x đã vượt qua cái trần đó. Nay khai đúng: các số token
trong BENCHMARK là ĐƠN VỊ SO SÁNH TƯƠNG ĐỐI giữa các route, không phải hóa
đơn; nhân khoảng 2,1 để ra token thật. Phép 2d giữ lời khai này, và BỎ QUA
sạch sẽ khi máy không có thư viện - bộ vẫn không phụ thuộc gói ngoài.

CÁC VÁ CÒN LẠI: DOC_TRUOC bước 3 dạy NGƯỢC README bước 3 (thêm X3, X4, X9 vào
Project), và phép 12 chỉ soi README nên cụm bị cấm sống yên trong file mà chính
nó dặn "đọc trước" - đo được 35,9% token mỗi phiên CHAT. Vá cả văn bản lẫn vế
cấm · bản sao vùng luật ("00_Index - Copy", "00_Index (1)", "00_Index_20260828"
- thứ Windows Explorer và OneDrive tự đẻ) đẩy trọn 14 FILE LUẬT thành ứng viên
chờ vào TAILIEU; nay lọc khớp cả bản sao · NFD và NFC là CÙNG một họ (file từ
macOS, iCloud): không chuẩn hóa thì phép 11 hết đường kêu XUNG ĐỘT và phép 9
báo oan; bộ đã biết lớp lỗi này vì bo_dau có normalize, chỉ quên đúng chỗ
chuan_hoa_ho · _so là JUNCTION sang thư mục nằm trong một repo thì 0g mù trọn,
nay soi từ ĐÍCH THẬT · khuôn mã VIEC bắt buộc đoạn khối trong khi ba sổ kia để
tùy chọn, nên V-001 trùng lọt ở sổ NÓNG NHẤT · 7d2 chỉ nổ khi CHƯA khai phần
mềm nào, nên dự án phần mềm THỨ HAI lọt trọn - nhận sản phẩm thứ hai là chuyện
tháng thứ ba, không phải ngoại lệ · @NHIP.BOCHINH gắn nhãn (EMAIL).

KHÔNG SỬA dù giám khảo đề nghị, vì kiểm lại thì lời khai của bộ đúng:
@MATHU (X0 dòng 248 khai THẲNG nó là CORE, mọi profile đọc) và @NHIP.QUETMAIL
(chú thích của chính nó nói quét TỰ ĐỘNG chỉ cho EMAIL, còn chat Zalo đi lối
bán thủ công X3 mục 5b - công ty LITE dùng lối chat VẪN cần nhịp này).

BACKLOG: (i) phép 14 chỉ chứng minh phép ĐÃ CHẠY - 14e đóng phần cấu trúc,
phần hành vi vẫn hở · (f) MIEN_TRU còn 16/46 phép chưa ai canh, giám khảo đo
8/8 đột biến vào vùng đó lọt · (l) MỚI: dump CSDL prod mang dữ liệu khách vào
kho vẫn im và còn được MỜI vào sổ mức A · (m) MỚI: secret trong _INBOX và
trong NỘI DUNG file chưa ai soi (7e2 chỉ dò TÊN file) · (n) MỚI: X5 1b bắt
phân biệt "nhánh CI/CD tự deploy" mà schema @DUAN.PHANMEM không có ô nào khai
nhánh · (o) MỚI: xóa pháp lý sót dòng THU trỏ tài liệu đã tombstone · (p) MỚI:
X0 của kho ĐANG CHẠY không có trần runtime (bơm lên 49.591 ký tự vẫn hệ sạch)
· (q) MỚI: mọi hằng ngưỡng (2700, 5200, 4200, 500) đứng ngoài lưới, chỉ
NGAN_SACH có 9b canh · (j) (k) (a) (b) (c) (e) (g) (h) như cũ.

Bài học vòng này: điểm ba vòng trước là điểm của việc ĐỌC KỸ. Vòng đầu tiên có
giám khảo chịu cài kho thật, diễn hai tuần, và chạy tokenizer thật thì điểm tụt
1,5 tới 2,6 mỗi lăng kính. Không phải bộ xấu đi - là lần đầu nó bị đo đúng.

## Vòng 46: hội đồng vòng 16 - trần giả, secret không lưới, junction no-op

Điểm vòng 16 (sáu lăng kính, chấm sau ba vòng vá 43-45): TOKEN 9,1 · ĐƠN GIẢN
9,0 · VẬN HÀNH 7,8 (vòng 15: 6,5, bước nhảy lớn nhất chiến dịch) · KHÔNG SAI
chưa về · KHÔNG MISS 7,6 · THÔNG MINH 7,6. Chỉ số đo được đều tiến: tỉ lệ trạng
thái mất dấu mã G đi im 4,1 xuống 1,9 phần trăm (389 ca, 55 họ); mutation score
ở MỨC PHÉP của kiem_van_hanh 0/36 lên 19/38; xóa hẳn một phép của kiem_tra_bo
bị bắt 22/24; tất định ĐẠT 8/8 trục (sáu PYTHONHASHSEED, bốn locale kể cả bẫy
chữ I của tr_TR, NFC/NFD, mười lượt giống nhau từng byte).

BỐN DEFECT NẶNG, cả bốn đều là LỜI KHAI VƯỢT CÁI MÁY LÀM:
1. TRẦN BẢN GỘP LÀ TRẦN GIẢ (TOKEN và ĐƠN GIẢN cùng bắt). Khai ở NGAN_SACH,
   soi gương sang BENCHMARK, phép 9b kiểm hai bản khai KHỚP NHAU - nhưng không
   ai đối chiếu với FILE. Bản gộp không nằm trong docs lẫn kem nên phép 9 rơi
   vào nd="" rồi `if nd` chặn luôn. Bơm 1.000.000 ký tự rác vào bản gộp mà bộ
   vẫn in "sạch, đóng gói được". Nó đã vượt trần từ vòng 44. Vá: phép 9 đọc
   THẲNG từ đĩa cho mọi khóa ngoài docs/kem, thiếu file cũng là LỆCH; và gỡ hai
   script khỏi bản gộp (49,8 phần trăm mà không ai đọc chúng ở đó) - 409.287
   xuống 205.410, trần hạ 400.000 xuống 260.000. Backlog (d) ĐÓNG.
2. LUẬT SECRET KHÔNG CÓ LƯỚI NÀO (VẬN HÀNH, pilot công ty phần mềm thật). Cắm
   chuỗi kết nối prod vào DUKIEN và prod.env vào kho: cả hai "hệ sạch", và bộ
   quan sát còn MỜI prod.env vào sổ mức A. X5 mục 1b cấm secret ở kho, ở sổ, ở
   _INBOX - máy làm đủ ba việc bị cấm rồi báo sạch. Mỉa mai nhất: chính vòng 45
   lấy hậu quả đó làm LÝ DO dựng 7d. Vá: phép 7e (secret trong ô sổ) và 7e2
   (file secret trong kho, soi THẲNG kho chứ không chờ file thành ứng viên).
3. CHỐT CHẶN JUNCTION CỦA VÒNG 44 LÀ NO-OP (THÔNG MINH và KHÔNG MISS cùng bắt).
   Path.is_symlink() trả FALSE cho junction Windows (reparse tag MOUNT_POINT),
   nên chốt chặn chưa bao giờ bắn đúng trên nền tảng mà lỗi được báo: junction
   tự trỏ đẻ 39 đường dẫn ma, đệ quy chỉ dừng bằng MAX_PATH. Vá: đọc thẳng cờ
   FILE_ATTRIBUTE_REPARSE_POINT.
4. Ô "Chạm sổ nào" gõ KHÔNG DẤU làm 3c báo oan VĨNH VIỄN, và chặn luôn lối
   thoát XÓA PHÁP LÝ của X5 mục 7b - trong khi chính fixture của bộ cũng gõ
   "khong". Đúng lớp lỗi phạt-người-làm-đúng mà vòng 45 vừa tuyên bố diệt cho
   7d. Vá: hàm bo_dau dùng cho mọi so khớp tiếng Việt trong ô sổ.

7d SAU KHI BỊ ÉP 10 BIẾN THỂ: chỉ kiểm 4/5 trường (bỏ "thành phần chính"), báo
oan khi gõ `repo:` hay `repo=`, và IM HOÀN TOÀN khi công ty quên khai hẳn -
đúng ca nguy hiểm nhất, vì cả chuỗi mức duyệt repo của X5 mục 1b không kích
hoạt được và deploy chạy thật bị xử như việc nhẹ. Cả ba đã vá; lời khai "cưỡng
chế NỘI DUNG" hạ xuống đúng thứ máy làm là dò bốn trường TRONG KHỐI khai báo.

X5 MỤC 1b LÀ DANH SÁCH ĐÓNG: lấy dump prod có dữ liệu khách, chạy SQL sửa dữ
liệu thật, restore, xoay secret, đổi feature flag, cấp quyền prod đều rơi ra
ngoài bảng và TỤT XUỐNG MỨC A, trong khi README hứa mọi thao tác chạm chạy thật
đều cần duyệt. Nay bảng có MẶC ĐỊNH ĐÓNG: không dòng nào khớp thì lấy C.

PHÉP MỚI: 7e, 7e2 (secret) · 8d (lane watermark khớp GIÁ TRỊ, 8c chỉ đếm tên) ·
3g (ô Mức và Trạng thái phải thuộc từ vựng X5 - gõ "c" thay "C" là lách trọn kỷ
luật mức C, 21/22 ca họ này từng đi im) · 0i2 (mục X0 biến mất là tắt luôn phép
canh chính mục đó) · 0k2 (neo ngoài _so thành NGHĨA VỤ, trước chỉ là LƯU Ý nên
kịch bản thảm họa vòng 43 vẫn đi im khi kho chưa từng tạo neo) · 13d (số token
đầu ra vào lưới) · 14c (DANH BẠ PHEP_VH đối chiếu với chính mã nguồn - vòng 45
đẻ ra 7d2 rồi quên khai nên 14b mù đúng phép mới nhất, tức quy tắc vòng 44 bị
phá ngay vòng sau). Phép 7 dùng khuôn mã đúng (Q-DA2-001 từng lọt vì khuôn cũ
là Q-\d+) và đọc cả _lich_su, cùng 3b.

SỐ LIỆU: dung sai 2c siết 10%/2% xuống 2%/0,5%, việc này lập tức phơi ra 9 số
route stale từ vòng 43 mà băng dung sai đang che; tất cả đã dán lại. Thuế
thường trực đứng yên tuyệt đối 2.316 token qua bốn vòng 43-46 dù thêm 13 phép
kiểm. Bốn gate token còn nguyên.

MIEN_TRU của 14b từ 20 xuống 16 (bốn mục thừa: phép 13 đã canh sẵn).

BACKLOG cập nhật: (d) ĐÓNG. Còn (a) hash QUYETDINH · (b) phép 5 đối chiếu số
cột với X5 mục 4 · (c) khuôn bản sao · (e) chuyển sổ sang CSV còn CẤM chứ chưa
có bản rà · (f) MIEN_TRU còn 16 phép chưa ai canh, nguy hiểm nhất là phép 0 (sổ
lõi tồn tại trên đĩa) - người canh DUY NHẤT của 12 ca mất trọn một sổ · (g)
loc_ban_chinh tất định nhờ sorted mà không ai ghim · (h) 7c chưa soi PLANNING
và DUKIEN · (i) MỚI: phép 14 chỉ chứng minh phép ĐÃ CHẠY, không chứng minh nó
CÒN BẮT ĐƯỢC GÌ - đục ruột một phép cho điều kiện luôn đúng thì 0/24 bị bắt ·
(j) MỚI: vòng đời _inbox và _da_nap chưa ai canh · (k) MỚI: cache
_quan_sat_truoc.json giả mạo được để lách luật ổn định hai lượt quét.

Bài học vòng này, thẳng thắn: bốn defect NẶNG đều là LỜI KHAI VƯỢT CÁI MÁY LÀM,
và ba trong bốn nằm trong bản vá của chính ba vòng liền trước. Hai giám khảo
độc lập cùng nói một câu đáng ghi: lưới đi từ PHÉP (phép 13, 14, 14b) và lưới
đi từ TRẠNG THÁI (bộ fuzz) phát hiện hai lớp lỗi khác nhau và KHÔNG thay nhau
được. Bộ đã có lưới thứ nhất; thứ còn thiếu là một danh mục TRẠNG THÁI HỎNG độc
lập với danh sách phép hiện hữu. Đó là bản vá đáng giá nhất còn lại.
