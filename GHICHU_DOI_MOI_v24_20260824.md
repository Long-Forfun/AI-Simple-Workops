# GHI CHÚ ĐỔI MỚI · STARTER · 20260824

File này cho người đánh giá. Không phải luật, không cần copy vào bộ chạy.
Các vòng xếp mới nhất ở trên; vòng 9 (v10) từng qua thêm một lượt team agent
nội bộ tự rà, tự dựng case, tự đóng vai người dùng.

## Vòng 33: dọn backlog tự khai (ba mục hành-động-được cuối)

Không chờ vòng chấm mới: ba mục backlog mà các giám khảo còn trừ điểm thật
và ĐỀU vá được, vá luôn:

1. CHAT DÁN TAY thành luật (X3 mục 5b): kênh Zalo, Messenger đi lối bán thủ
   công qua cửa "người dùng đưa trực tiếp" - dán cả đoạn chat hay export, AI
   tách từng tin theo khuôn giờ-tên, xử như mục đến ở chặng 1 (nguồn D, nâng
   B khi có xác nhận văn bản), ảnh chat như nguồn scan, không cấp luồng THU,
   theo dõi bằng VIEC. Vùng TRỐNG tần suất cao nhất với thị trường VN thành
   MỘT PHẦN có đường chính thức; README và X0 C9 trỏ về mục 5b.
2. X3E tách mục 1c PHỤC HỒI SỰ CỐ, gate "chỉ đọc khi rà 24-31 báo lệch" -
   cùng khuôn gate đã chứng minh ở X5 mục 1b; route CUA_VAO mail trong
   BENCHMARK và phép 2c đo trừ mục 1c.
3. kiem_van_hanh v29: heuristic bản sao CÙNG TIỀN TỐ cho file nghiệp vụ
   (khuôn OneDrive -<TênMáy>): ứng viên đề xuất _INBOX mà cùng thư mục có
   file làm tiền tố tên nó, đuôi -XXXX không phải vN, chuyển sang cảnh báo
   NGHI BẢN SAO thay vì mời vào sổ mức A.

Bảng route dán lại từ --sinh-benchmark trong cùng commit (quy ước vòng 8).
Watchlist trần: X0 ~15,99k/16.000 · X5 16,996/17.000 · X3E ~11,1k/12.000 ·
X3 ~4,24k/4.500. Backlog còn lại sau vòng này: KHÔNG - ba mục tự khai đã
[ĐÍNH CHÍNH vòng 35: câu "KHÔNG" này khai sót - mốc chống dán lặp chat
của giám khảo KHÔNG MISS vòng 9 khi đó còn treo, vá ở vòng 35]
dọn hết; phần chưa làm còn lại đều là đánh đổi có chủ đích đã ghi nhận
user-facing (không pipeline chat tự động, không phân quyền).

## Vòng 45: phạm vi tổ chức phần mềm thành thứ MÁY GIỮ

Yêu cầu nghiệp vụ gốc của người dùng có hai vế: hội đồng chấm tới 99/100, VÀ
"công ty có dự án phần mềm cần nắm rõ phạm vi tổ chức các phần mềm để các vận
hành liên quan nó chính xác hơn". Vế thứ hai đã có mặt từ vòng 24-37 và trải
đủ năm chặng - README mục riêng, X9 mục 1 câu 3, X0 C2 @DUAN.PHANMEM năm
trường, X5 mục 1b bảng mức repo, X2 phát hành phần mềm - nhưng RÀ LẠI vòng này
phát hiện cả chuỗi đó chỉ được giữ bằng MỘT luật ghim yếu. Nghĩa là nó tồn tại
nhờ lời khai, không nhờ máy. Đúng thứ mà chính bộ này cấm.

1. SÁU LUẬT GHIM giữ trọn chuỗi (phép 12 lên 73 luật): README phải có mục
   riêng KÈM LÝ DO ("khai đủ thì các vận hành liên quan mới chính xác") · X9
   phải hỏi phạm vi tổ chức ngay phiên cài đặt khi dự án là phần mềm, kèm nơi
   giữ secret · X0 C2 phải khai đủ NĂM trường · phải giữ luật "repo là NGUỒN
   SỰ THẬT của code, code KHÔNG chép vào kho" · X5 mục 1b phải còn gate, bảng
   mức repo, luật SECRET và dữ liệu khách · X2 phải còn bảng kiểm phát hành
   phần mềm. Gỡ bất kỳ mắt xích nào là bộ FAIL, không đóng gói được.

2. PHÉP 7d CƯỠNG CHẾ NỘI DUNG, không chỉ sự có mặt của chữ. Dự án phần mềm
   khai thiếu trường nào thì rà nêu ĐÍCH DANH trường đó, kèm hậu quả vận hành
   cụ thể: không rõ repo thì code có thể bị chép vào kho; không rõ đâu là môi
   trường CHẠY THẬT thì deploy đáng lẽ mức C bị hạ nhầm xuống A theo X5 mục
   1b; không rõ nơi giữ secret thì secret rơi vào sổ hay _INBOX. Kèm 7d2: dòng
   TAILIEU dùng dạng "Repo" mà công ty chưa khai phần mềm nào là lệch.
   Đây là chỗ vế thứ hai của yêu cầu chuyển từ TÀI LIỆU sang VẬN HÀNH: trước
   đây khai thiếu vẫn chạy, nay khai thiếu là rà đỏ.

3. NHẬN CẢ BẢN CÓ DẤU LẪN KHÔNG DẤU. Bàn thử bắt được bản vá đầu tiên của
   chính vòng này báo oan một công ty khai ĐỦ nhưng gõ "chay that" thay vì
   "chạy thật" - đúng lớp lỗi phạt-người-làm-đúng, lần này bị chặn TRƯỚC khi
   commit thay vì sau ba vòng. Nay mọi khuôn nhận cả hai kiểu gõ.

4. Ca I3 cho 7d vào phép 13 trong CÙNG lượt vá, đúng quy tắc vòng 44 vừa dựng
   thành máy. Phép 14b làm đúng việc của nó hai lần trong vòng này: báo 7d
   chưa có ca, rồi báo ca đầu tiên tôi viết KHÔNG kích hoạt được phép (khối
   tiếp nối nuốt nhầm dòng định nghĩa cú pháp nên đủ từ khóa oan).

Trạng thái: 21 phép của kiem_tra_bo, 37 phép của kiem_van_hanh, 91 fixture, 73
luật ghim, phép 13 với 7 ca I1 + 4 ca I2 + 13 ca I3, phép 14 và 14b điểm danh
hai chiều.

## Vòng 44: quy tắc tự viết ba vòng liền, nay thành MÁY

Điểm THÔNG MINH vòng 15b: 7,8/10 (vòng 13: 9,0). Tất định ĐẠT tuyệt đối - ép
qua PYTHONHASHSEED, bốn locale kể cả tr_TR (bẫy chữ I), đường dẫn có dấu,
junction: mọi lượt chạy giống nhau từng byte. Điểm tụt vì vòng 43 mở một bề
mặt lời khai rất lớn (phép 13, 14, "lưới của lưới") mà bề mặt đó yếu hơn lời
khai, cộng hai defect vận hành mới.

HAI DEFECT NẶNG, đều do CHÍNH bản vá vòng 43 gây ra:
1. 3c mù TRỌN DÒNG. Vòng 43 thêm `if "đã xóa theo Q-" in cham: continue` để
   thôi phạt người thi hành lệnh xóa pháp lý - nhưng X5 mục 7b chỉ dặn GỠ TÊN
   SỔ đó khỏi ô, nghĩa là phép đã tự loại đúng sổ bị xóa rồi, cái continue vừa
   thừa vừa MỞ LẠI ĐÚNG LỖ VÒNG 41 ĐÃ ĐÓNG: ghi đè ô "Ghi lần" của sổ CÒN LẠI
   đi im hoàn toàn, và chỉ cần gõ chuỗi đó vào ô là được, mã Q- không cần có
   thật. Nay chỉ bỏ qua khi ô thay TRỌN, và mã Q- phải có ở QUYETDINH.
2. 00_Index chỉ lọc ở TẦNG ĐẦU. Một bản sao lưu 00_Index lồng trong kho - thao
   tác sao lưu bình thường - đẩy trọn 14 file LUẬT của chính bộ thành ứng viên
   vào TAILIEU; qua junction thì thành 93 và đệ quy tới khi MAX_PATH cắt, tức
   chỉ giới hạn Windows chặn chứ không phải thiết kế. Nay lọc MỌI TẦNG như
   "_so" đã làm, và không đi xuyên junction hay symlink.

PHÉP 14b - quy tắc thành máy. Ba vòng liền bộ tự viết một quy tắc rồi không
thi hành ngay trong lượt đó: vòng 40 "mỗi bản vá phải đi kèm lưới của chính
nó", vòng 41 "phép kiểm mới nguy hiểm ngang một luật mới", vòng 43 "phép mới
phải kèm một ca I1 và một ca I2 của chính nó". Hậu quả đo được: 27/36 phép của
kiem_van_hanh xóa trọn được mà bộ vẫn in "sạch, đóng gói được" - gồm 8b mà mục
Vòng 43 nêu đích danh là đã vá, và 0k, 7c, 8c, 3d do CHÍNH vòng 43 đẻ ra.
Nay kiem_van_hanh mang DANH BẠ PHEP_VH (dữ liệu, không phải nhãn) và phép 14b
đối chiếu danh bạ đó với tập phép mà phép 13 THẬT SỰ ép được trạng thái vi
phạm. Phép mới không kèm ca của chính nó thì 14b đỏ NGAY LƯỢT VÁ ĐÓ. Nó chứng
minh giá trị ngay lần chạy đầu: nêu đích danh 3d chưa có ca nào canh, và ca
đó đã được thêm trong cùng lượt. MIEN_TRU còn 20 phép, phải rỗng dần - đó là
danh sách nợ công khai, không còn là vùng mù im lặng.

LƯỚI CỦA LƯỚI, khâu tiếp: tắt vế I2 hay I3 của phép 13 trước đây vẫn "sạch"
(CA MỒI chỉ canh vế I1) - nay SỐ CA là khẳng định (7/4/12) nên tắt vế nào cũng
đỏ · hong.pop() mù từng nuốt được thông điệp "KHO LÀNH đã lệch sẵn", nay có
điều kiện · thu3 nay cũng kiểm kho lành trước khi ép, hết ca đúng-một-cách-rỗng
· "68 luật" vẫn là NHÃN và đếm thật là 67, nay là khẳng định · phép 13c đo
trần đầu ra trên kho ĐANG LỆCH (kho toàn PASS là ca dễ nhất, mà RA_SOAT chỉ
chạy khi kho CÓ vấn đề: đo được 3.832 ký tự, vượt trần cũ 60 phần trăm).

BA CA CỦA PHÉP 13 SAI BẢN CHẤT, nay sửa: hai ca I1 không hề mất dấu mã G (cắt
byte cuối dòng trong khi mã nằm ô đầu - thực chất là hỏng schema do phép 5
bắt; và bản conflicted chỉ THÊM file, không xóa gì) nay đổi tên cho đúng bản
chất; một ca I2 khai "chuyển việc ĐÃ XONG sang _lich_su" mà dữ liệu là ĐANG
LÀM - lưới đang KHẲNG ĐỊNH rằng đem việc dở dang vào lịch sử là đúng luật, nay
sửa thành XONG.

Khâu nhỏ: 8c đọc ĐÚNG dòng watermark (một dòng văn xuôi mang chuỗi "CUA2=" là
đủ đánh lừa nó) · tên phép 2c khai đúng dung sai thật (0 cho dòng CỘNG, 2%
trên 5.000, 10% còn lại) thay vì "10%".

BACKLOG: (a) hash QUYETDINH · (b) phép 5 đối chiếu số cột với X5 mục 4 · (c)
khuôn bản sao (đã hạ mức) · (d) tách bản LUẬT thuần khỏi bản gộp, ĐƯỜNG GĂNG ·
(e) chuyển sổ sang CSV/SQLite còn CẤM chứ chưa có bản rà · (f) MIEN_TRU của
phép 14b còn 20 phép chưa ai canh · (g) loc_ban_chinh tất định nhờ sorted mà
không phép nào ghim - đổi hệ file thì im lặng đổi hành vi · (h) phép 7c chưa
soi PLANNING và DUKIEN, phép 9b bỏ qua hai trần script.

## Vòng 43: hội đồng vòng 15 - lưới phải có lưới của chính nó

Điểm vòng 15: TOKEN 9,4 (13: 9,3) · ĐƠN GIẢN 8,9 (8,8) · KHÔNG MISS 8,5 (14:
8,0) · KHÔNG SAI 7,1 (6,8) · VẬN HÀNH 6,5 (7,0). Năm giám khảo XÁC NHẬN mọi
phát hiện cũ đã đóng, không cái nào tái phát. Đo được: mutation score vùng cũ
52 lên 74 phần trăm; tỉ lệ trạng thái mất dấu đi im 14,2 xuống 4,1 phần trăm
(358 ca đột biến, 21 họ); 14/14 số route khớp tuyệt đối; pipeline EMAIL 0/14 im.

BA DEFECT NẶNG, đều là lớp lỗi PHẠT NGƯỜI LÀM ĐÚNG, lần thứ ba và thứ tư:
1. 3f phạt MỌI plan mức C đang mở (VẬN HÀNH). Ô "Mã ghi" trống ở PLANNING là
   THIẾT KẾ - X5 mục 2 cho bốn trạng thái chưa chốt, X5 mục 3 đặt điểm ghi mức
   C ở "khi chốt" - và phép 4 cách đó mười dòng chỉ đòi mã G cho plan ĐÃ GHI.
   Phép do chính vòng 41 viết đã đỏ lưới trên mọi việc rủi ro suốt hai vòng.
2. 3d mù _so\_lich_su\ (KHÔNG MISS). X5 mục 5 BẮT chuyển plan ĐÃ GHI quá 30
   ngày vào đó; làm đúng thì 3d lệch vĩnh viễn. Đúng lớp lỗi vòng 41 vừa đóng
   cho 3c và 3e, tái phát lần thứ tư ở phép thứ ba cùng họ.
3. Làm ĐÚNG X5 mục 7b đẻ 3c lệch vĩnh viễn (VẬN HÀNH): lệnh xóa pháp lý gỡ
   dòng một sổ, mà lối thoát 7b lại gate ở "mất dấu ở MỌI sổ" nên không dùng
   được. Nay 7b cấp lối cho ca mất dấu MỘT sổ, và 3c nhận dấu "đã xóa theo Q-".

LƯỚI PHẢI CÓ LƯỚI CỦA CHÍNH NÓ (KHÔNG SAI, phát hiện sâu nhất chiến dịch):
xóa trọn phép 13 - sản phẩm đầu bảng của vòng 42 - mà bộ vẫn in "sạch, đóng
gói được", dòng của nó chỉ lặng lẽ biến mất. Cùng lớp: xóa 3f, 7b, 8b, 1a khỏi
kiem_van_hanh cũng "sạch"; "88 ca" và "67 luật" là NHÃN chứ không phải khẳng
định; và vế I2 của phép 13 đúng một cách VÒNG TRÒN vì kho lành dựng C12 bằng
CHÍNH hàm mà rà 0i sẽ chấm - nên con bug NẶNG của vòng 40 tái nhập được mà
phép 13 im. Vá: phép 14 ĐIỂM DANH (thiếu phép nào là lệch) · bất biến I3 (mỗi
phép phải kêu ĐÚNG TÊN mình trên một trạng thái mẫu) · CA MỒI tự tố cáo nếu vế
I1 bị tắt · số ca và số luật thành khẳng định · fixture ghim trên CHÍNH
template, và kho lành dựng C12 bằng bản quét ĐỘC LẬP.

NEO NGOÀI _so (KHÔNG MISS, kịch bản thảm họa chưa ai nghĩ tới): mọi nhân chứng
- NHATKY, sáu sổ, hai view - đều nằm TRONG _so, nên một lần khôi phục nhầm hay
rollback đám mây TRỌN thư mục đó xóa sạch bằng chứng cùng lúc: kho đã ghi 500
lượt trông y hệt kho vừa cài và máy in "hệ sạch". Nay X5 mục 3 bước 6 nối mã G
vào 00_Index\_moc_ghi.txt (ngoài _so), và phép 0k lấy nó làm nhân chứng cuối.

PHÉP MỚI: 0k (neo ngoài _so) · 7c (liên kết trỏ mã không tồn tại - X4 dòng 12
hứa máy dò từ lâu mà máy chưa cài) · 8c (bảng khai lane watermark cho MỌI cửa;
lane rụng thì cửa đó mất mốc và lượt sau cấp lại mã đã dùng) · 9b (bảng trần
khớp NGAN_SACH) · 13b (trần ĐẦU RA của kiem_van_hanh - bảng này DÁN VÀO phiên
RA_SOAT nên là context thật, đã phình 16,9 phần trăm mà không ai giữ) · 14
(điểm danh). Mở rộng: 3e soi cả X0_INDEX · 0j soi xuống _so một tầng · 7b đọc
thêm PLANNING, ô Phiên và dòng watermark · 8b đòi nhãn watermark · muc_con_trong
thôi ép tham số của profile CHƯA BẬT vào C12 (8/34 mục với công ty LITE).

THÔNG ĐIỆP THÔI NÓI TIẾNG MÁY (ĐƠN GIẢN): hết phun cú pháp Python vào mắt
người dùng; "version history" nay có lối đi được cho kho Ổ MÁY ĐƠN - cấu hình
README khai là được hỗ trợ mà với nó version history KHÔNG TỒN TẠI, nên chỉ
dẫn cũ là bất khả thi; 3f thôi gợi ý "gỡ dòng đó", chính là thao tác nó sinh ra
để chặn; lệnh cho AI tách khỏi câu người dùng đọc bằng nhãn [AI: ...]; X4 cấm
dán nguyên đầu ra của máy cho người dùng.

TOKEN: 2c bắt MỌI lần xuất hiện của nhãn (một số stale nấp ở dòng thứ hai
cùng nhãn) và dung sai 0 cho dòng thuế thường trực · bảng thuế nay tự cân ·
cắt bỏ X9 và X4 khai đúng công của nó (~4193 token, 19,2 phần trăm, không phải
"gần 3.000") · thêm lối CHAT HOI/BAN không nạp X3.

Watchlist trần (nâng X5 20.000, kiem_van_hanh 104.000, kiem_tra_bo 100.000 -
hai script ngoài mọi route, chỉ vào bản gộp): bản gộp là mục cần xử SỚM, nhịp
phình 17.310 ký tự mỗi vòng nên chỉ còn khoảng hai vòng nữa là chạm trần.

BACKLOG cập nhật: (a) hash nội dung QUYETDINH · (b) phép 5 đối chiếu số cột
với schema X5 mục 4 · (c) khuôn bản sao " (n)" - hội đồng vòng 15 đo lại thấy
0b ĐÃ bắt, hạ mức · (d) TÁCH BẢN LUẬT THUẦN khỏi bản gộp, nay lên đường găng ·
(e) chuyển sổ sang CSV/SQLite: vòng này mới CẤM chuyển khi lưới chưa theo kịp,
chưa viết bản rà đọc được định dạng đó · (f) phép 13 mới phủ 10/32 phép, chưa
phủ 0, 0f, 2, 8b - bốn phép mà hội đồng đo được là "người canh DUY NHẤT" của
một trạng thái.

Bài học vòng này: quy tắc vòng 41 tự viết - "phép kiểm mới nguy hiểm ngang một
luật mới" - vẫn chưa thành máy, nên 3f ra đời với một báo động giả phủ trọn
nhánh mức C mà không ai thấy suốt hai vòng. Từ vòng sau, mỗi phép kiểm mới
phải kèm ít nhất MỘT ca I1 và MỘT ca I2 của chính nó trong phép 13, trước khi
commit.

## Vòng 42: phép 13 FUZZ - lưới thường trực cho lớp lỗi đã tái phát ba vòng

Ba vòng liên tiếp (38, 40, 41) đều đẻ ra cùng MỘT lớp lỗi khi đang vá lớp lỗi
đó: phép kiểm mới quay ra PHẠT NGƯỜI DÙNG VÌ LÀM ĐÚNG. Mỗi lần đều phải có
giám khảo chạy tay cả buổi mới thấy. Vòng này biến phát hiện đó thành MÁY.

Phép 13 khẳng định HAI bất biến đối xứng, đo bằng cách ép trạng thái thật trên
một kho lành dựng từ chính bộ mẫu:
  I1  mọi trạng thái làm MẤT dấu mã G phải sinh ÍT NHẤT MỘT lệch
  I2  mọi trạng thái ĐÚNG LUẬT không được sinh lệch nào
Vế I2 là vế mà ba vòng vừa rồi vi phạm; hội đồng vòng 14 đề nghị đúng cặp này.

Sáu ca I1 (xóa trọn file NHATKY quý · xóa dòng NHATKY · xóa ô Ghi lần · xóa
trọn dòng sổ · cắt cụt dòng ở mức byte · bản conflicted rụng dòng) và bốn ca I2
(tách NHATKY quý cũ vào _lich_su theo X5 mục 7 · chuyển dòng VIEC đã xong sang
_lich_su theo X5 mục 5 · điền lần đầu rồi đánh dấu [x] ở C12 theo C11 ngoại lệ
2 · lượt hai nối thêm mã vào ô Ghi lần theo X5 mục 3 bước 3).

Phép 13 gọi TRỌN main() của kiem_van_hanh, không gọi hàm helper: hội đồng vòng
14 đo được 12/25 đột biến lọt vì fixture chỉ khẳng định giá trị trả về của hàm
mà không ai kẹp CHỖ GỌI.
[ĐÍNH CHÍNH vòng 43, ĐO LẠI ở vòng 44: câu "tắt một phép ở chỗ gọi là phép
 13 kêu ngay" KHAI QUÁ NET - và bản đính chính của vòng 43 CŨNG khai quá net.
 Đo trọn 36 mã phép của kiem_van_hanh (49 nếu kể 12a-12l), tắt từng phép một:
 vế I1 và I2 của vòng 42 bắt 3 (3c, 3e, 5), KHÔNG phải 4/32; 0b bị chính bản
 mở rộng "0j soi xuống _so" của vòng 43 che mất. I3 của vòng 43 thêm 0h, 0i,
 0j, 1a, 3f, 7b, thành 9/36. Vòng 44 thêm phép 14b nên con số này không còn
 là lời khai nữa mà là thứ MÁY tự đối chiếu mỗi lượt chạy.]

Kiểm chứng bằng hai đột biến, chạy thật trên bản sao:
- gỡ đúng bản vá _lich_su của vòng 41 (một dòng) thì phép 13 FAIL với
  "I2 chuyển dòng VIEC đã xong sang _lich_su: ĐÚNG LUẬT mà bị báo 3c" - tức
  lưới này TỰ BẮT được defect NẶNG mà giám khảo VẬN HÀNH phải chạy trọn một
  pilot mới tìm ra.
- tắt cả 0d lẫn 3e thì phép 13 FAIL với "I1 xóa trọn file NHATKY quý: mất dấu
  mã G mà KHÔNG phép nào kêu" và "I1 xóa dòng NHATKY".
Hai chiều đều bắt, và trên bộ hiện tại phép 13 PASS.

BACKLOG: mục (e) ĐÓNG. Còn (a) ô chốt hash cho nội dung QUYETDINH, (b) phép 5
đối chiếu số cột với schema X5 mục 4, (c) khuôn bản sao " (n)" bị bỏ im lặng
(bản vá đã soạn, chưa áp), (d) tách bản LUẬT thuần khỏi bản gộp.

## Vòng 41: hội đồng vòng 14 - vá chính bản vá vòng 40

Điểm vòng 14: KHÔNG MISS 8,0 · VẬN HÀNH 7,0 · KHÔNG SAI 6,8. Ba giám khảo
XÁC NHẬN mọi đầu vá vòng 40 chạy thật (0d, 0g, 0h, 3e, 0i, 0j, 1e, phép 8 hai
chiều đều dựng lại được và đều bắt). Nhưng vòng 40 tái phạm ĐÚNG lớp lỗi nó
đang chữa: đẻ ra BÁO ĐỘNG GIẢ trên đường đi của mọi công ty. Mutation score
của vùng vừa vá đo được 52% (12/25 đột biến lọt).

BÁO ĐỘNG GIẢ do vòng 40 sinh, nay đóng:
1. 0i BẪY VĨNH VIỄN (NẶNG, 3 giám khảo cùng bắt). Phép mới đếm cả dòng ĐỊNH
   NGHĨA CÚ PHÁP của template (`@DUAN.<MÃ DA>`, `@NGUON.<LOẠI>`), cả văn xuôi
   mang dấu ngoặc, cả ô ĐÃ điền (`@TEN.PROJECT`), lại bỏ sót C13 mà X9 câu 11
   hỏi đích danh. Kho cài ĐÚNG X9 bị tố "lách ngoại lệ C11" ngay lệnh rà đầu
   tiên, và ba lối ra đều hỏng - máy chỉ chấp nhận một C12 mà luật gọi là vi
   phạm. Nay: X0 khai LUẬT VIẾT DẤU (ô chưa điền dùng đúng một khuôn), template
   tuân đúng luật đó, và phép quét tách thành hàm dùng chung `muc_con_trong()`
   để AI cài đặt với rà 0i không thể tính ra hai tập khác nhau. Đo lại: 44 ô
   trống trên template, kho cài từ zero SẠCH.
2. 0i mù ô xuống dòng (VỪA-NẶNG). Quét theo DÒNG nên 20/32 khóa tàng hình, gồm
   cả nhóm khóa và sáu tham số EMAIL. Nay quét theo KHỐI THAM SỐ.
3. 3c mù `_so\_lich_su\` (NẶNG). X5 mục 5 bắt chuyển việc XONG quá 30 ngày vào
   lịch sử, phép 6 CƯỠNG BỨC khi sổ vượt 500 dòng - mà 3c không đọc thư mục đó,
   nên mỗi dòng lưu trữ ĐÚNG LUẬT đẻ một mã lệch không bao giờ dọn được, tích
   lũy từ ngày thứ 31. 3e cũng mù y hệt với NHATKY quý cũ. Nay cả hai đọc
   `_lich_su`, và X5 mục 5 nói rõ chuyển lịch sử không được làm mất dấu mã G.
4b. 0g ở PHA vừa clone: hai giám khảo vòng 14 chốt NGƯỢC nhau (một đòi cảnh
   báo ngay vì .git chắc chắn còn, một khen vì không đá người dùng ở bước 1
   của README). Chỗ gặp: kho CHƯA cài thì in LƯU Ý (chưa có sổ nào để mất, và
   bước cài của X9 sẽ xóa .git); kho ĐÃ cài mà còn .git mới là LỆCH.
4. 8b suýt lặp lại lớp lỗi ngay khi vừa viết: bảng "bàn sạch" là dạng RÚT GỌN
   mà INSTRUCTION mục 2 khai tường minh, đòi đủ sáu bộ đếm ở đó là báo oan. Bắt
   được ở chính lượt tự kiểm trước khi commit.

LỖ CÒN LẠI, nay đóng: 0g hết chốt theo pha rev 0 (kho vừa clone là lúc .git
chắc chắn còn) · 0j bắt cả THƯ MỤC lạ · 1a đúng MỘT bản INSTRUCTION, chọn bản
v lớn nhất · 3c đòi dấu ở ĐÚNG các sổ đã khai chạm, không phải "ít nhất một"
(X5 hứa "3c lệch mãi" mà thực tế im) · 3f MỚI: mọi dòng sổ phải mang mã G, xóa
hay dán dòng ngoài lượt ghi hết đi im · 3a xét trọn mọi dòng, không bỏ dòng
đầu · 7b MỚI: từ vựng sổ phải khai ở X0 (cửa ma sinh lane watermark giả; dự án
NGỪNG còn việc mở làm việc VÔ HÌNH) · 8b MỚI: bảng đủ bộ đếm · X9 mục 4 hết
dạy XÓA dòng C12 trong khi C11 cấm · nâng cấp chở thêm DOC_TRUOC, BENCHMARK,
GHICHU, bản gộp, và đọc mục 3c CỦA BẢN MỚI · DOC_TRUOC mang MỐC VÒNG VÁ nên
@NHIP.BANMOI mới có gì để so, kèm @NHIP.BANMOI.DAKIEM · 1e hết báo oan
`_quan_sat_bo.txt` và hết áp lên KHO CÔNG TY.

LƯỚI: 60 lên 67 luật ghim, thêm bảy luật CHỐNG ĐỘT BIẾN mà hội đồng chứng minh
được là lưới cũ cho qua (nhóm (b) của nâng cấp bị rút còn một file vẫn "sạch";
thân CHỐT CHỐNG LÁCH bị đảo ngược vẫn "sạch"). Mốc vòng vá ở DOC_TRUOC phải
khớp vòng mới nhất của GHICHU - lưới tự bắt nếu quên tăng.

Watchlist trần (nâng X0 18.500 lên 20.000 và bản gộp 340k lên 400k, cả hai đều
có gate đã khai: X0 đọc theo mục, bản gộp không nạp vào phiên nào; X9 7.500 lên
8.500 vì nay đứng ngoài MỌI route): X5 18.021/19.000 (94,8%) · README
8.463/9.000 (94,0%) · X3_CUAVAO 92,5% · X3E 92,3% · X9 92,3% · X0 92,4%.

BACKLOG, cập nhật thẳng: (a) QUYETDINH sửa nội dung không ai bắt - nay hẹp hơn
vì 3f bắt được XÓA dòng, còn SỬA ô thì vẫn hở, cần ô chốt hash · (b) phép 5
chưa đối chiếu số cột với schema X5 mục 4 - cùng họ với 7b, vá một lượt · (d)
bản gộp nên tách bản LUẬT thuần ~30k cho người đánh giá · (e) BỘ FUZZ: giám
khảo KHÔNG MISS đã tự viết và chạy 400 lượt, đo được 14,2% trạng thái mất mã G
đi im; giám khảo VẬN HÀNH đề nghị thêm vế đối xứng "mọi trạng thái ĐÚNG LUẬT
không được sinh LỆCH nào" - chính vế đó là thứ vòng 40 và 41 vi phạm hai lần.
Hai vế này là ưu tiên cao nhất cho vòng sau. Mục (c) khuôn bản sao đã có bản vá
soạn sẵn, chưa áp.

Bài học vòng này, đắt hơn vòng trước: vòng 40 tự viết "mỗi bản vá phải đi kèm
lưới của chính nó" rồi KHÔNG làm - và đúng chỗ đó thủng. Một phép kiểm mới
nguy hiểm ngang một luật mới: nó có thể phạt người dùng vì làm đúng. Từ vòng
này, phép mới nào cũng phải trả lời được hai câu: bắt được cái sai nào, và
KHÔNG bắt oan cái đúng nào.

## Vòng 40: hội đồng vòng 13 chấm PILOT - vá chính bản vá vòng 38

Điểm vòng 13: TOKEN 9,3 · THÔNG MINH 9,0 · ĐƠN GIẢN 8,8 · KHÔNG MISS 8,6 ·
KHÔNG SAI 7,6 · VẬN HÀNH 6,8. Điểm TỤT MẠNH so với 96,8 đọc-tĩnh, và tụt
đúng lý do đáng mừng: sáu giám khảo lần này CHẠY hệ thay vì đọc, mỗi người
một đường chưa ai đi (LITE không phần mềm, kho có sẵn file, bàn giao, hai
phiên cùng cửa, mất mát, mutation). Ba defect NẶNG là do CHÍNH bản vá vòng
38 sinh ra: vá một BÁO ĐỘNG GIẢ bằng cách đổi lấy ba lời BÁO SẠCH GIẢ.

MÁY (kiem_van_hanh v35), tất cả đều dựng lại được trước khi vá:
1. 0d quét thiếu (NẶNG, 3 giám khảo độc lập). v34 chỉ soi 5 sổ lõi, bỏ
   THU.md và BANG_DIEU_KHIEN - hai nơi mã G ĐẬU theo đúng X5 mục 3-4. Kho
   mất NHATKY mà bảng còn `sinh_boi: G-...` in "hệ sạch". Nay
   loc_dau_vet_ghi quét MỌI sổ và view trong _so.
2. 0g mù thư mục CHA (NẶNG, 3 giám khảo). `(goc/".git").exists()` chỉ soi
   một tầng; clone vào chính `<gốc>` thì `git stash` vẫn nuốt trọn sổ mà
   lưới im. Nay tim_vung_git dò kho VÀ mọi tổ tiên, bắt cả .git dạng file
   (worktree, submodule).
3. 0h MỚI (NẶNG). Cờ `rev 0` một mình tắt 0d, 2, 3, 4, 8: X0 bị đồng bộ mây
   trả về bản cũ thì máy KHẲNG ĐỊNH "chưa có lượt ghi nào" trong khi NHATKY
   nằm ngay đó. Nay có dấu vết ghi thì cấm tự nhận "chưa cài".
4. 3e MỚI (NẶNG). 3c chỉ đi MỘT chiều NHATKY sang sổ. Mất TRỌN một file quý,
   hay hai phiên cùng cửa ghi đè cả file NHATKY, đều không phép nào thấy.
   3e đi chiều ngược: mã G đậu ở sổ hay bảng phải có dòng NHATKY.
5. Phép 8 tách hai chiều lệch. Bảng MỚI HƠN mọi dòng NHATKY nghĩa là NHATKY
   mất dòng; câu cũ xui người dùng "sinh lại bảng", tức xóa nốt bằng chứng
   cuối cùng. Nay hai chiều nói hai câu khác nhau.
6. 0i, 0j MỚI. 0i: C12 phải khai ĐÚNG tập mục còn dấu chưa điền (chống lách
   ngoại lệ C11 bằng cách thêm bớt dòng C12). 0j: file lạ trong 00_Index -
   vùng bị loại khỏi quan sát nghiệp vụ nên tài liệu lỡ lưu vào đây KHÔNG
   phép nào nhặt, mà `git status` từng là lưới cuối thì vòng 38 vừa gỡ.
   3a bắt thêm dòng CỤT (đứt lượt ghi ở mức byte, ô Trạng thái mất chữ).

LUẬT:
7. Ngoại lệ C11 (2) phủ 2/29 mục (NẶNG, VẬN HÀNH đếm được). Neo cũ đòi
   ĐỒNG THỜI `<chưa điền>` VÀ có dòng ở C12, trong khi template viết
   `<điền...>`, `<N>`, và nhóm C không bao giờ được đưa vào C12. Nay neo là
   "CHƯA TỪNG mang giá trị, còn bất kỳ dấu chưa điền nào"; X9 mục 1 bắt
   buộc quét X0 đưa MỌI mục trống vào C12 khi cài (pilot mới liệt 27 mục);
   dòng C12 khi điền thì ĐÁNH DẤU `[x]` chứ không xóa, vì dấu đó là bằng
   chứng duy nhất phân biệt điền-lần-đầu với đổi-giá-trị. Thêm CHỐT CHỐNG
   LÁCH: C11 và C12 tự nằm trong nhóm khóa, đưa mục đã điền trở lại C12 là
   mức C.
8. Nâng cấp không chở lưới (NẶNG). X9 3c chỉ bảo chép `_TEMPLATE`, mà
   kiem_van_hanh, kiem_tra_bo, INSTRUCTION, README đều KHÔNG mang
   `_TEMPLATE`: mọi công ty cài trước vòng 38 nâng cấp đúng luật vẫn vĩnh
   viễn không có 0g và vẫn dính 0d báo động giả. Vá vòng 38 không có đường
   giao hàng. Nay 3c chép HAI nhóm, nhóm (b) đè thẳng năm file đó.
9. Một cửa MỘT phiên đang ghi là luật CORE, không riêng PARALLEL (công ty
   LITE mở hai tab là ca thường nhất). Ô "Ghi lần" khai rõ là danh sách
   CHỈ-THÊM (ghi đè làm lượt cũ mất dấu, 3c lệch kinh niên mỗi tuần).
   @VANHANH.NGUOI có thật ở C6 (thủ tục bàn giao đang trỏ tới một tham số
   không tồn tại). @NHIP.BANMOI có thật ở C9 (sau khi gỡ .git thì KHÔNG ai
   sở hữu việc biết bộ đã cũ). Lượt ghi ĐẦU TIÊN của kho hết bị nhắc vòng
   quý oan. X9 3b nói rõ phải quét HAI lần và tên gốc vào ô có thật.
   README có lối thoát `git stash pop` bằng tiếng người.

LƯỚI: phép 1e MỚI - phép BÙ của phép 1, bắt file THỪA (lưới là allow-list
nên rác vô hình theo cấu trúc: lọt hai commit liên tiếp, vòng 37 và 38).
Dung sai 2c siết theo bậc (2% cho số trên 5.000: 10% trên dòng CHAT che tới
2.000 token). Phép 10 hết mù tham chiếu bị xuống dòng. Luật ghim 52 lên 60,
gồm ba luật CHỐNG ĐỘT BIẾN mà hội đồng chứng minh được là lưới cũ cho qua:
README không được khuyên ngược, mức ĐIỀN LẦN ĐẦU phải khớp cả ba nơi, số
ngoại lệ C11 phải bằng số liệt kê. Fixture 82 lên 88: ba quyết định của 0d,
0g, 0i lên tầng module nên fixture kẹp thẳng - vùng rà soát trước đây có
mutation score 0% vì main() không hàm nào gọi được.

TOKEN: X9 và X4 KHÔNG nạp vào phiên CHAT nữa (X9 đọc một lần khi cài, X4
chỉ khi RA_SOAT mà pilot đo được RA_SOAT thực tế trả 0 token vì chạy
script): CHAT 20.314 xuống 17.335, cắt 14,7%. BENCHMARK khai thẳng ĐỘ BẤT
ĐỊNH của hệ số ký-tự/3 (đối chứng T5 cho 2,1x, là TRẦN TRÊN) và thôi gọi số
pilot là "đo được" - cái đo được là file nào thật sự đọc, không phải token.
Cả 14 số route dán lại từ máy trong cùng commit.

Watchlist trần (nâng X0 16.500 lên 18.500, X9 6.500 lên 7.500, X5 18.000
lên 19.000, X3E 12.000 lên 13.000 - mọi mục nâng đều có gate đã khai và đã
được do_route trừ): X9 7.407/7.500 (98,8%) · X5 17.812/19.000 (93,7%) · X0
17.707/18.500 (95,7%) · X3E 11.995/13.000 (92,3%) · README 8.398/9.000
(93,3%) · _GOP 91,9%.

BACKLOG CÒN LẠI, khai thẳng (không vá vòng này, đều có địa chỉ rõ):
(a) QUYETDINH tự khai "không sửa nội dung" nhưng KHÔNG có cưỡng chế nào -
    sửa tay ô "Đánh đổi" không phép nào bắt; cần ô chốt hash mỗi dòng, là
    đổi schema sổ nên để riêng một vòng.
(b) Phép 5 chỉ kiểm bảng nhất quán NỘI BỘ, chưa đối chiếu số cột với schema
    X5 mục 4, nên schema sổ trôi âm thầm được.
(c) File trúng khuôn bản sao " (n)" bị bỏ IM LẶNG khi quét kho, trong khi
    khuôn OneDrive được in đích danh - kho có sẵn file thì bản " (1)" có
    thể là bản mới hơn mà vô hình.
(d) _GOP 102k token, 71% là hai script và GHICHU; nên tách bản LUẬT thuần
    ~30k cho người đánh giá.
(e) Chưa có bộ sinh trạng thái đứt gãy (fuzz) khẳng định bất biến "mọi
    trạng thái mất mã G phải sinh ít nhất một LỆCH".

Lượt kiểm chứng đầu-cuối của chính vòng 40 (clone từ link công khai, cài từ
zero, chạy máy) bắt thêm một lỗi trong chính phép 1e vừa viết: nó chỉ đọc
được dòng .gitignore không có đường dẫn, nên báo oan `_so/_quan_sat_truoc.json`
- cache mà kiem_van_hanh vừa tự sinh - với MỌI người dùng chạy rà trước khi tự
kiểm. Đã vá bằng khuôn fnmatch đọc trọn .gitignore, và giữ đối chứng: thả một
file lạ vào bộ thì 1e vẫn bắt.

Bài học vòng này: đọc-tĩnh bão hòa ở 96,8 là thật, nhưng con số đó đo cái
BỘ ĐÃ ĐƯỢC ĐỌC, không đo cái bộ CHẠY. Một buổi chạy ra nhiều defect hơn
mười hai vòng đọc. Và bản vá viết vội ở vòng 38 tự nó sinh ba lỗ NẶNG -
bằng chứng đắt giá rằng mỗi bản vá phải đi kèm lưới của chính nó.

## Vòng 39: PILOT EMAIL - luật tả bằng văn xuôi, máy đòi schema

Pilot tiếp phần chưa ai đi: thực thi X3E mục 1 BẰNG TAY, chỉ theo CHỮ trong
luật, cố ý không đọc kiem_van_hanh.py, rồi để máy chấm. Kết quả: máy TỪ CHỐI
sản phẩm của người thực thi đúng luật.

1. GỐC (VỪA-nặng). X3E tả payload PREPARED bằng văn xuôi tiếng Việt ("convId,
   người gửi, thời điểm UTC, tiêu đề, đường dẫn staging, sha256 của .eml...")
   trong khi kiem_payload đòi một SCHEMA JSON chính xác không được khai ở
   đâu trong bộ: conv_id, nguoi_gui, thoi_diem, tieu_de, eml_sha256, staging,
   dinh_kem, thao_tac. Năm trên bảy tên trường tôi suy ra từ luật đều SAI, và
   trớ trêu nhất: tên khóa DUY NHẤT mà luật có ghi nguyên văn - `convId` - lại
   chính là tên máy không nhận (`conv_id`). Đường dẫn staging cũng lửng: luật
   nói "tương đối, nằm trong _so\_thu_staging", máy đòi chuỗi bắt đầu đúng
   `_so/_thu_staging/<sha256(khóa)>` tính từ GỐC KHO. Hậu quả dây chuyền: 12h
   từ chối payload, nên 12k coi cả ba mục index là "thừa" - ba dòng LỆCH cho
   một lượt nạp làm ĐÚNG luật.
2. VÁ: X3E thêm mục 1b "Schema file máy sinh, tên trường ĐÚNG NGUYÊN VĂN" -
   khai trọn ba file máy sinh (nhật ký ndjson, index, registry) dưới dạng
   JSON mẫu; văn xuôi mục 1 trỏ về đó và bỏ tên `convId` sai. Trần X3E giữ
   nguyên 12.000 bằng BÙ: cắt hai đoạn văn xuôi nay đã trùng schema (11.995).
3. MÁY GIỮ LỜI: hai fixture mới (bộ 82 ca) dựng payload ĐÚNG THEO SCHEMA khai
   trong X3E rồi gọi thẳng kiem_payload - phải trả RỖNG; và payload dùng tên
   cũ `convId`, `thoi_diem_utc` - phải bị từ chối đúng hai lỗi. Từ nay schema
   trong luật không thể trôi khỏi schema máy thực thi mà không ai biết. Thêm
   luật ghim 52: X3E phải chứa nguyên văn cả bảy tên trường.
4. KIỂM CHỨNG SAU VÁ: chạy lại pilot EMAIL với schema mục 1b - nạp một công
   văn trọn bốn bước (staging, PREPARED, áp ba thao tác THU/VIEC/TAILIEU kèm
   index, COMMITTED, registry dựng từ COMMITTED) - kho qua SẠCH toàn bộ
   12a-12l. Trước vá: 2 lệch; sau vá: 0.

Ghi thêm hai quan sát của pilot (không trừ điểm, là bằng chứng lưới chạy
đúng): (a) tôi quên sinh lại BANG_DIEU_KHIEN sau lượt ghi thứ hai - rà 8 bắt
ngay bằng watermark, đúng vai lưới an toàn cho lỗi THAO TÁC của người vận
hành; (b) đường "điền lần đầu C9 khi đụng <chưa điền>" vá ở vòng 38 chạy trơn
trong pilot này: điền @NHIP.* là mức B, rev 2 lên 3, xóa dòng khỏi C12, không
phải mở plan C.

Trạng thái sau 39 vòng vá: bốn gate token, 82 fixture, 52 luật ghim, 13 số
BENCHMARK máy giữ, 4 defect trạng-thái do pilot bắt.

## Vòng 38: vá theo PILOT VẬN HÀNH THẬT (nguồn phát hiện mới)

Hội đồng vòng 12 nhất trí 6/6: điểm đọc-tĩnh bão hòa quanh 96,8, nguồn phát
hiện còn lại là PILOT thật. Vòng này CHẠY pilot đó thay vì chấm tiếp: dựng một
công ty giả lập có dự án PHẦN MỀM (REGULATED + EMAIL), clone bộ như người dùng
thật, chạy X9 cài từ zero, vòng thử mức A, rồi dựng bản phát hành mới ở
upstream và nâng cấp. Ba defect lộ ra - không vòng đọc-tĩnh nào trong 12 vòng
thấy được, vì cả ba chỉ tồn tại ở TRẠNG THÁI, không ở chữ:

1. BÁO ĐỘNG GIẢ NGAY SAU KHI CÀI (VỪA). Cài đúng X9 xong, lệnh kiểm đầu tiên
   mà README bảo chạy in "trục sự thật đã biến mất: khôi phục mức C, cấm cấp
   mã G mới" - trong khi kho vừa cài chưa ghi lần nào, NHATKY quý CHỈ sinh ở
   lượt ghi đầu theo đúng X5 mục 3 bước 1. Hệ tự khóa mình ngay sau khi cài.
   Vá: 0d chỉ báo khi CÓ dấu vết đã từng ghi (mã G còn ở sổ, hay nhật ký
   EMAIL) mà NHATKY vắng; kho vừa cài in một dòng BỎ QUA nói rõ vì sao. Thông
   điệp lệch thật nay nêu đích danh sổ còn mang dấu.
2. MÂU THUẪN Ở ĐƯỜNG ĐI CỦA MỌI CÔNG TY MỚI (VỪA-nặng). X9 mục 2 và 4 dạy điền
   nhóm B (C5 tới C8) giữa chừng rồi "làm tiếp"; nhưng C5 tới C8 đều thuộc nhóm
   khóa C11, mà ngoại lệ chỉ sống ở rev 0 - "từ rev 1 luật này hiệu lực". Đọc
   chặt thì mỗi câu trả lời nhóm B là một plan C kèm QUYETDINH (phá lời hứa
   "vào việc được sau bốn câu"); đọc lỏng thì AI lặng lẽ phá C11. Không văn bản
   nào gỡ. Vá: C11 thêm ngoại lệ (2) ĐIỀN LẦN ĐẦU một mục đang nằm ở C12 là
   mức B, tăng rev, xóa dòng khỏi C12, không plan không QUYETDINH - đó là phần
   cài đặt HOÃN LẠI, không phải đổi giá trị đang có hiệu lực; ĐỔI giá trị ĐÃ
   điền vẫn C kèm QUYETDINH. Đồng bộ INSTRUCTION mục 6 và X5 mục 1 (hết "ngoại
   lệ duy nhất").
3. NÂNG CẤP BỘ LÀM MẤT DÒNG SỔ (NẶNG, dựng lại được). `git pull` - đúng lệnh
   X9 mục 3c và README dặn - DỪNG trên kho đang chạy vì `_so\` là sổ sống mà
   git đang quản; người dùng làm theo lời khuyên `git stash` mà chính git in
   ra thì dòng VIEC BIẾN MẤT khỏi bản làm việc. Pilot dựng lại nguyên vẹn chuỗi
   này. Lưới cũ có bắt hậu quả (rà 3c, 2, 8 cùng lệch) nhưng không ai chặn
   trước. Vá: X9 mục 1 thêm bước XÓA `00_Index\.git` khi cài; mục 3c viết lại,
   CẤM pull/stash/checkout trong kho, nâng cấp là tải bản mới ra THƯ MỤC KHÁC
   rồi chép _TEMPLATE vào; README nói bằng tiếng người kèm lối thoát
   `git stash pop`; rà 0g MỚI của kiem_van_hanh v34 chặn ngay trạng thái đó.
   Trần X9 giữ nguyên 6.500 bằng BÙ (cắt hai chỗ diễn đạt trùng), không nâng.
   [ĐÍNH CHÍNH vòng 40, theo hội đồng vòng 13 - BA lời khai trên sai:
    (a) "README kèm lối thoát git stash pop" - README KHÔNG có câu đó, lối
    thoát chỉ nằm ở X9 mục 3c, file người dùng không đọc; vá ở vòng 40.
    (b) "đồng bộ INSTRUCTION" - sót mục 5, chỗ đó vẫn viết "ngoại lệ duy
    nhất" trong khi mục 6 đã nói "ba ngoại lệ"; vá ở vòng 40.
    (c) "trần X9 giữ nguyên bằng BÙ" - đúng về TRẦN nhưng bù THIẾU: file
    phình +6%, còn đúng 14 ký tự headroom, và vòng 38 là vòng đầu tiên
    trong 10 vòng KHÔNG có dòng Watchlist trần, tắt đèn đúng lúc cần nhất.
    Ngoài ra vòng 38 để lọt assets/ (669 KB, ảnh của dự án khác) vào chính
    commit của mình - tái phát lớp lỗi .codex_audit_mutant của vòng 37 -
    và không dán lại 9/13 số route sau khi sửa X0, X5, X9, INSTRUCTION.]
4. README VÀO LƯỚI. File người dùng đọc ĐẦU TIÊN lại đứng ngoài mọi phép kiểm
   (không ký tự cấm, không tham chiếu chéo, không _GOP) - lỗi ở đó hại nhất mà
   được bảo vệ ít nhất. Nay README nằm trong FILE_BAT_BUOC, qua sạch cả bốn
   phép ngay lần đầu. Phép 12 lên 51 luật (thêm luật điền-lần-đầu và luật
   kho-không-phải-bản-làm-việc-git).

BENCHMARK có mục "Phiên thật đã đo" đầu tiên: cài đặt ~11,8k token thật, 6 lượt
đọc file, không đọc thừa, không sai; RA_SOAT thực tế trả 0 token đọc X4 vì
script tự đủ nghĩa. Cột "phiên thật" hết trống - bắt đầu có số.

Trạng thái sau 12 vòng chấm - 38 vòng vá: bốn gate token, 80 fixture, 51 luật
ghim, 13 số BENCHMARK máy giữ, 3 defect trạng-thái do pilot bắt. Bài học ghi
lại: đọc-tĩnh bão hòa ở 96,8 là thật, và cách vượt qua nó cũng là thật - chạy
hệ, đừng đọc thêm.

## Vòng 37: khâu theo hội đồng vòng 12 (96,8/100)

Điểm vòng 12: KHÔNG MISS 9,9 · ĐƠN GIẢN 9,9 · TOKEN 9,8 · VẬN HÀNH 9,6 ·
KHÔNG SAI 9,5 · THÔNG MINH 9,4. Mọi phát hiện đều THẤP, hội tụ về một rổ
việc nhỏ trên chính đường nối vòng 36; plateau đọc-tĩnh giữ nguyên. Vá:

1. 12l so mã Q ĐÚNG Ô (kiem_van_hanh v33): BỐN giám khảo cùng chứng minh
   bằng chạy thật rằng vế "Q phải có dòng trong QUYETDINH" mới chỉ là so
   chuỗi con toàn văn - Q là TIỀN TỐ của mã thật (Q-2026 ăn theo
   Q-20260826-01) và Q chỉ được nhắc trong ghi chú của dòng khác ("cân
   nhắc, không ban hành") đều được miễn hash oan. Nay so đúng Ô qua
   dong_bang; hai fixture ghim đúng hai ca lọt, bộ 80 ca.
2. X3 5b khâu bốn khe chat còn lại: mốc chống dán lặp thêm NGÀY (chat
   nhiều ngày hết mù ngày); nhánh khối-không-chứa-tin-mốc chốt biên "tin
   CÙNG phút mốc coi như ĐÃ NẠP, nghi sót thì dán lại cả khối chứa tin
   mốc"; chặng 2 gặp trùng event_id tin chat thì SO NỘI DUNG trước khi bỏ
   qua (khử đụng khóa xuyên khối cùng phút-cùng-NN); từ hai kênh chat trở
   lên mỗi kênh một dòng VIEC + mã kênh -chat-<kênh>-<NN>; ngày lấy theo
   header GẦN NHẤT phía trên (export nhiều ngày); header X3 nhắc gate 5b
   theo đúng quy ước header X5. Luật ghim 934/936 ghim thêm "Bước tiếp
   theo", "VỊ TRÍ", "SO NỘI DUNG".
3. Số LITE vào lưới 2c: nhãn thứ 13 "CUA_VAO thường của LITE" ~1025 token
   máy đo - hết số tay đứng ngoài lưới trong BENCHMARK.
4. Nâng trần theo quy ước: X3 5.500 (phần tăng nằm TRỌN trong 5b gated,
   route thường không đổi ~2554) · X5 18.000 chủ động (headroom 98,1% là
   nợ được giám khảo ĐƠN GIẢN đòi xử trước khi phát nổ). BENCHMARK rewrap
   các dòng gãy giữa câu; số CHAT dán lại từ máy trong cùng commit.

Watchlist trần: X3 ~5,09k/5.500 (92,5%) · X5 17,16k/18.000 (95,3%) · X0
96,9% · X3E 92,8%. Trạng thái sau 12 vòng chấm - 37 vòng vá: bốn gate
token, 80 fixture, 49 luật ghim, 13 số BENCHMARK máy giữ. Hội đồng nhất
trí 6/6: nguồn phát hiện còn lại là PILOT vận hành thật 2-4 tuần, điền
cột "phiên thật" của BENCHMARK; điểm đọc-tĩnh 96,8 đã sát trần phương
pháp.

## Vòng 36: vá theo hội đồng vòng 11 (96/100, plateau xác nhận)

Điểm vòng 11: KHÔNG MISS 9,8 · ĐƠN GIẢN 9,8 · TOKEN 9,7 · KHÔNG SAI 9,5 ·
THÔNG MINH 9,5 · VẬN HÀNH 9,3 (trừ đúng: defect VỪA event_id là do vòng 35
sinh). BỐN giám khảo độc lập cùng bắt một defect - hội tụ chưa từng có. CẢ
SÁU giám khảo cùng kết luận: điểm đọc-tĩnh đã bão hòa quanh 96, các vòng
sau chỉ dao động quanh nhiễu; nguồn phát hiện duy nhất còn lại là PILOT
vận hành thật 2-4 tuần. Vá:

1. event_id tin chat: <YYYYMMDD-HHMM>-chat-<NN> (NN thứ tự tin trong khối
   dán - hai tin cùng phút hết trùng khóa, chặng 2 hết nuốt tin im lặng);
   ngày lấy theo header ngày trong đoạn dán, thiếu mới rơi về ngày phiên;
   mốc chống dán lặp về MỘT nhà (ô "Bước tiếp theo" của dòng VIEC theo dõi
   chat - cột có thật, bền phiên); "SAU mốc" chốt nghĩa theo VỊ TRÍ trong
   khối. Luật ghim phép 12 (49 luật).
2. Mục 5b lên GATE "CHỈ đọc khi người dùng dán chat hay export" (tiền lệ
   gate thứ tư): route CUA_VAO thường về ~2554 (LITE không dán chat khỏi
   trả thuế 5b); trần X3 nâng 5.000 KÈM GATE theo quy ước - thoát cảnh
   99,8% mà không thành thuế chung.
3. kiem_van_hanh v32: 12l đòi khuôn TRỌN "[đã xóa theo Q-<mã>]" (chuỗi
   lửng hết được miễn oan) VÀ mã Q phải có dòng trong QUYETDINH (Q ma bị
   bắt) - hai fixture mới, bộ 78 ca; tự vệ vế SÁU (thư mục tồn tại nhưng
   không dấu vết cài đặt = LỖI CÁCH DÙNG exit 2).
4. Khâu chữ: CỘNG thuế thường trực vào lưới 2c (khớp phép làm tròn của
   phép 9 - hết nit 1 token); số LITE cập nhật; cột ma cuối "ghi chú
   TAILIEU" về ô "Căn cứ trạng thái" có thật; C4 rewrap; 1d khớp _thu_
   theo path segment.

Watchlist trần: X3 ~4,7k/5.000 (94%) · X5 17,16k/17.500 (98,1%) · X0
~15,99k/16.500 (96,9%) · X3E 92,8%. Trạng thái sau 12 vòng chấm - 36 vòng
vá: bốn gate token (1b, 7b, 1c, 5b), 78 fixture, 49 luật ghim, 12 số
BENCHMARK máy giữ. Hội đồng khuyến nghị nhất trí: bước kế tiếp là PILOT
thật, điền cột "phiên thật" của BENCHMARK.

## Vòng 35: khâu theo hội đồng vòng 10 (96/100)

Điểm vòng 10: ĐƠN GIẢN 9,8 · KHÔNG MISS 9,7 · VẬN HÀNH 9,7 · TOKEN 9,6 ·
KHÔNG SAI 9,4 · THÔNG MINH 9,4. Mọi phát hiện đều THẤP trừ một khoản quản
trị đích đáng: vòng 33 khai "backlog rỗng" trong khi mốc chống dán lặp chat
còn treo - vòng này vá món đó VÀ đính chính lời khai cũ ngay trong GHICHU.

1. CHAT 5b khâu kín: CHỐNG DÁN LẶP bằng mốc "đã nạp tới tin <giờ> <người
   gửi>" ghi vào VIEC/bảng chờ, lượt sau chỉ xử tin SAU mốc; event_id tin
   chat <YYYYMMDD-HHMM>-chat (ngày theo ngữ cảnh phiên); không tách được
   khuôn giờ-tên thì cả khối là MỘT mục nguồn D; luật ghim vào phép 12.
2. kiem_van_hanh v31: nhãn "tiền tố gây nghi" TẤT ĐỊNH (sorted, chọn dài
   nhất - 3 giám khảo cùng bắt dao động theo hash seed) + fixture đa-tiền-
   tố; 12l siết miễn-hash về đúng khuôn "[đã xóa theo Q-" và thông điệp
   lệch gợi kiểm tombstone; tự vệ tham số ĐẦU (thư mục ma, flag lạ = LỖI
   CÁCH DÙNG exit 2, hết 4 LỆCH oan).
3. Gate 7b về chuẩn hai-lưới như 1c (phép 12 ghim heading + vế gate; 47
   luật); phép 10 phủ cả tham chiếu "X9 mục n"; phép 1d loại dòng "!" và
   đuôi sau khoảng trắng (hết khe tự phá); hồi quy C4 dấu ":" dính nghĩa
   sửa lại (kèm khai ngưỡng hậu tố ~5 ký tự cho khớp máy); X5 header nhắc
   cả gate 7b; header kiem_tra_bo đếm đúng 76 ca; CỘNG ~2214 khớp máy;
   trần X0 nâng chủ động 16.500 theo quy ước (headroom 99,8% là nợ đã
   được giám khảo ĐƠN GIẢN đòi xử trước khi phát nổ); bảng route dán lại
   từ máy đo trong cùng commit.

Watchlist trần: X0 ~15,99k/16.500 (96,9%) · X5 17,16k/17.500 (98,1%) · X3
~4,49k/4.500 (99,8% - ứng viên nâng-kèm-gate vòng sau nếu 5b cần thêm) ·
X3E ~92,8%. Khuyến nghị chiến lược của hội đồng (ĐƠN GIẢN vòng 10): bộ đã
bão hòa điểm đọc-tĩnh; nguồn phát hiện kế tiếp là PILOT vận hành thật 2-4
tuần trên kho công ty thật, đo số lần AI hỏi thừa và ghi sai thực tế.

## Vòng 34: vá theo hội đồng vòng 9 (94,8/100)

Điểm vòng 9 (thang hiệu chỉnh: chỉ trừ defect có hành động sửa; đánh đổi
được giám khảo công nhận đúng thì không trừ): ĐƠN GIẢN 9,7 · KHÔNG MISS 9,7
· VẬN HÀNH 9,5 · TOKEN 9,5 · THÔNG MINH 9,3 · KHÔNG SAI 9,2. Không còn
phát hiện CAO; các giám khảo đồng thanh "lỗi còn lại là lỗi KHÂU, không còn
lỗi THIẾT KẾ". Vá trọn 16 mục hội tụ:

1. MÁY GIỮ LỜI VÒNG 33 (VỪA duy nhất): heuristic cùng-tiền-tố lên tầng
   module (loc_nghi_ban_sao) + 2 fixture ghim (ca dương -DESKTOP kèm tên
   tiền tố, ca âm -v02); phép 12 ghim 2 luật mới (45 luật: chat 5b, gate
   1c); phép 10 phủ hậu tố chữ (mục 5b, 1b, 1c, 7b được kiểm thật, hết mù
   "\d+"); fixture 12l-tombstone-hash. Bộ fixture lên 75 ca.
2. X5 tách mục 7b "Xóa theo yêu cầu pháp lý" GATE "chỉ đọc khi có Q-<mã>"
   (tiền lệ gate thứ ba): SUA_FILE ~5665 xuống ~5221; sáu tham chiếu mục 7
   đổi 7b (X1, X5 x3, QUYETDINH, NHATKY template); trần X5 17.500 kèm gate.
   12l MIỄN so hash cho dòng tombstone (xóa đúng luật hết lệch oan ở index
   có ô hash); X5 7b khai vế "máy miễn hash".
3. Khâu chữ vòng 9: "nâng lên B" (4 giám khảo cùng bắt) · ô Mã thư của tin
   chat = "phien-chat" · X5 mục 4 trỏ đích danh X3E mục 1c · README "xử
   như mục đến ở cửa vào" (hết liên tưởng pipeline mail) · C4 khai giá
   khuôn cùng-tiền-tố (kèm cắt bù X0: nén ghi chú ổ đơn) · X9 mục 3c thêm
   câu gỡ kẹt pull một-lần cho bản cài cũ · thông điệp NGHI BẢN SAO nêu
   đích danh tiền tố + lối ra file thật + trỏ đúng X5 mục 4 · BỎ QUA phép
   1, 2-8 hết nói "chưa cài" khi X0 chỉ sai tên · tự vệ vế bốn nói lối đặt
   lại quan sát · phép 1d lọc dòng comment · 2c giữ thêm số INSTRUCTION
   (~1884), bảng route dán lại từ máy đo. kiem_van_hanh lên v30.

Watchlist trần: X5 17,13k/17.500 · X0 15,97k/16.000 · X3E ~92,8% · X3
~94,9%. Quy ước bổ sung: vN ở header các template đứng yên trong cùng bản
phát hành bộ, chỉ nhích khi đóng gói bản mới - nâng cấp đi lối diff nội
dung theo X9 mục 3c.

## Vòng 32: vá theo hội đồng vòng 8 (đợt chốt)

Vòng 8 về 4/6 giám khảo (hai giám khảo đứt giữa chừng vì giới hạn phiên):
VẬN HÀNH 9,0 · TOKEN 9,2 · KHÔNG MISS 9,6 · ĐƠN GIẢN 9,6; giám khảo KHÔNG
SAI kịp ghi nhận một phát hiện trước khi đứt (X9 thiếu vế secret - trùng
với hai giám khảo khác). Vá:

1. FILE MÁY SINH HẾT BỊ ĐÓNG GÓI (VỪA của vòng 8, chứng minh bằng clone
   thật): _so/_quan_sat_truoc.json từng bị commit vào bộ mẫu khiến git pull
   - đường nâng cấp duy nhất được tài liệu hóa - abort vì cache local bẩn.
   Gỡ khỏi index, .gitignore che cả họ (_quan_sat_truoc, _thu_*, staging),
   phép 1d mới của kiem_tra_bo giữ vĩnh viễn qua .gitignore (tất định,
   không phụ thuộc git).
2. kiem_van_hanh v28: tự vệ tham số vế BỐN (kho tồn tại nhưng quét 0 file
   trong khi cache >0 mục: cảnh báo, GIỮ cache - hết ghi đè mốc ổn định
   bằng tập rỗng); 0b chỉ flag bản X0 tên lạ khi BẢN CHUẨN cũng tồn tại,
   không có bản chuẩn thì nhường 0c khuyên "đổi tên" - hết hai thông điệp
   trái chiều; nhánh 0c "chưa cài" chỉ khi TEMPLATE là file X0 duy nhất.
3. X9 mục 1 câu 3 thêm vế "nơi giữ secret" (3 giám khảo cùng chỉ - khớp
   trọn ba đầu README, X0 C2, X9); ví dụ X0 C2 hết ngắt dòng giữa câu
   (net 0 ký tự, X0 giữ 15.993/16.000); README mục phần mềm: đoạn hai tách
   thành câu tiếng người + con trỏ X5 mục 1b (bớt chuỗi jargon git), intro
   trỏ xuống mục; GHICHU vòng 31 sửa câu "bù tương đương" thành "bù MỘT
   PHẦN, kín headroom" cho khớp diff thật (giám khảo TOKEN đối chiếu git);
   BENCHMARK: đoạn văn hết lặp số SUA_FILE (thành tham chiếu bảng), toàn
   bộ bảng route dán lại từ --sinh-benchmark (xóa trôi 2-4%).

Watchlist trần: X0 15.993/16.000 (99,9%) · X5 16.996/17.000 (99,9%) · X3E
~92% · X9 ~92,5%. Backlog tự khai giữ nguyên: pipeline chat bán thủ công
(vùng TRỐNG tần suất cao nhất còn lại với thị trường VN) · heuristic
cùng-tiền-tố OneDrive cho file nghiệp vụ · gate phục hồi X3E khi chạm ~95%.

## Vòng 31: vá theo hội đồng vòng 7 (20260825, điểm vòng 7: 91,2/100)

Điểm vòng 7: THÔNG MINH 8,5 · VẬN HÀNH 9,0 · KHÔNG SAI 9,0 · TOKEN 9,1 ·
KHÔNG MISS 9,5 · ĐƠN GIẢN 9,6. Giám khảo THÔNG MINH tuyên bố "hệ đã hội tụ:
lỗi còn lại là lỗi KHÂU, không còn lỗi THIẾT KẾ"; ĐƠN GIẢN tuyên bố bão hòa.
Vá:

1. XÓA PHÁP LÝ khớp trọn lưới máy (VỪA cuối, hai giám khảo cùng chỉ): dòng
   TAILIEU, THU là ĐÍCH INDEX thì giữ khung và mã dòng, chỉ trung hòa ô dữ
   liệu (12k, 12l tự khớp); dòng NHATKY mất dấu Ghi lần thì ô "Chạm sổ nào"
   thay "không, đã xóa theo Q-<mã>" (đi lối "không" sẵn của phép 3c); VIEC,
   DUKIEN, PLANNING, staging + manifest lý do Q, cache quan sát đều có cách
   xử; fixture 73 "kho sau XÓA PHÁP LÝ đúng luật phải sạch" ghim hồi quy.
2. kiem_van_hanh v27: loc_ban_chinh lên tầng module, ba hành vi bộ lọc bản
   sao được fixture ghim (73 ca); regex mã X0 khớp luật 3-4 ký tự A-Z 0-9
   (luật ghi rõ KHÔNG dấu ở X0 C1 và X9 câu 1, hết cáo buộc oan mã có dấu);
   0c nhánh "tên không đúng chuẩn: đổi tên file"; tự vệ tham số vế ba (gốc
   kho không tồn tại: bỏ qua quan sát, KHÔNG ghi đè cache mốc ổn định).
3. Giới hạn nói ra ở nơi người dùng đọc (KHÔNG MISS: "ghi nhận đúng nhưng
   sai chỗ"): kênh chat Zalo chưa có pipeline (README Ngày thường + X0 C9);
   bộ mặc định MỘT người vận hành toàn quyền chốt C (X0 C6); giá của khuôn
   bản sao khai tại luật tên file C4 (" (n)", "(bản sao)" bị máy coi là bản
   sao đồng bộ).
4. README thêm mục "CÔNG TY CÓ PHẦN MỀM": khai rõ PHẠM VI TỔ CHỨC từng phần
   mềm (repo, thành phần, môi trường, nơi chạy thật, nơi giữ secret) ngay từ
   phiên cài đặt để các vận hành liên quan chính xác; trỏ X9 mục 1 câu 3, X0
   C2 @DUAN.PHANMEM, X5 mục 1b, X2 phát hành build.
5. Máy giữ thêm hai số con của BENCHMARK (mục 1b ~421, X5 mục 3 ~1058) qua
   phép 2c; số mục 3 cập nhật (~950 đã trôi 11%). Trần X0, X5 GIỮ NGUYÊN
   theo quy ước nâng-trần-kèm-bù: phần thêm được bù MỘT PHẦN bằng cắt chữ
   trong hai file đó, phần còn lại ăn hết headroom (X0 15.993/16.000, X5
   16.996/17.000 - thử lửa một phần; bài kiểm net-zero còn ở phía trước).

Watchlist trần: X0 99,9% · X5 99,9% · X3E ~92% · X9 ~92%. Hai file trụ đã
kín trần thật sự: vòng sau muốn thêm chữ vào X0 hay X5 là phải cắt trước.

## Vòng 30: vá theo hội đồng vòng 6 (20260825, điểm vòng 6: 89/100)

Điểm vòng 6: VẬN HÀNH 8,5 · THÔNG MINH 8,5 · KHÔNG SAI 8,5 · TOKEN 9,0 ·
KHÔNG MISS 9,4 · ĐƠN GIẢN 9,5. Hội đồng không còn phát hiện CAO nào; giám
khảo KHÔNG MISS vẽ bản đồ độ phủ tổng thể: 8/11 nhóm PHỦ chắc, xác suất công
ty nhỏ VN gặp tình huống TRỐNG trong 12 tháng ước 8-12% (persona đích ~5%).
Vá:

1. kiem_van_hanh v26: nhận dạng bản sao đồng bộ về MỘT nguồn ba tầng -
   MAU_TAM học khuôn " (1)", " copy", " copy 2", "(bản sao)" nên bản sao
   file nghiệp vụ hết được ĐỀ XUẤT vào sổ mức A; NHATKY và X0 chọn bản
   chính theo TÊN CHUẨN (NHATKY_<năm>Q<quý>, X0_CAUHINH_<MÃ>) nên khuôn
   OneDrive -<TênMáy> và mọi hậu tố lạ bị 0b flag thay vì gây lệch giả
   "trùng mã G" · tự vệ tham số vế hai (gốc kho trùng 00_Index dừng sớm).
2. XÓA PHÁP LÝ khâu nốt: dòng TAILIEU, THU trỏ file đã xóa thì XÓA DÒNG
   trong chính plan C (hai sổ đó không phải chỉ-thêm; "CHỈ-THÊM" định danh
   rõ NHATKY, QUYETDINH, nhật ký thư); tầng quét thêm "MỌI file theo con
   trỏ sổ, kể cả 01_Phap_ly/_NOP, 99_Archive, file digest"; ô tên đính kèm
   mang dữ liệu cá nhân cũng trung hòa; danh mục C của X5 mục 1 trỏ thủ
   tục mục 7 (phiên NOI_BO cũng thấy đường).
3. Schema @DUAN.PHANMEM thêm ô "nơi giữ secret" (con trỏ SECRET của X5 1b
   hết trỏ vào ô không tồn tại), ví dụ đã điền cập nhật; C14 hàng X5 thêm
   C5; "tự khai" RA_NGOAI được định nghĩa một vế (chữ phải NẰM trong danh
   sách của chính dữ kiện, luật bao trùm không dùng cho lối người nhận
   mới); X3E MAIL MÁY "một dòng ở phần 5" khớp khuôn digest; BENCHMARK
   NOI_BO ghi chú "+mục 1b ~421 khi phần mềm", SUA_FILE hai số; header
   kiem_tra_bo đếm đúng 69 ca; README rewrap dòng dài cuối; DOC_TRUOC
   "X9 mục 1 câu 3".

QUY ƯỚC MỚI cho người bảo trì (đề xuất giám khảo TOKEN): nâng trần một file
phải kèm (a) gate để phần nâng không thành thuế chung, hoặc (b) cắt tương
đương ở file khác cùng route. Phép 9 giữ trần; quy ước này giữ chính cái trần.

Còn ghi nhận, chưa vá (đều NHẸ): kênh chat Zalo chưa có pipeline luồng kiểu
THU · phân quyền nhiều người dùng "ai được chốt C" · X3E mục 1 tách gate
phục hồi khi chạm ~95% trần · khuôn bản sao OneDrive cho FILE NGHIỆP VỤ
(ngoài sổ) cần heuristic cùng-tiền-tố, để vòng sau cân nhắc.

## Vòng 29: khâu đường nối theo hội đồng vòng 5 (20260825, điểm vòng 5: 84,5/100)

Điểm vòng 5: KHÔNG SAI 7,5 · THÔNG MINH 8,0 · VẬN HÀNH 8,0 · TOKEN 8,6 ·
KHÔNG MISS 9,2 · ĐƠN GIẢN 9,4. Bài học hội tụ từ ba giám khảo: mỗi vòng THÊM
tính năng lại sinh đường nối mới; vòng này CHỈ KHÂU, không mở gì mới.

1. kiem_van_hanh v25: ghi_cache bọc lỗi GHI (cache bị khóa chỉ in lưu ý, báo
   cáo chạy trọn) · truyền nhầm gốc kho được tự nhận, dừng sớm kèm gợi ý ·
   10a/10b có nhánh KHÔNG KIỂM ĐƯỢC khi file bị khóa (hết cáo buộc "bị sửa"
   oan cho bản ĐÃ KÝ đang mở) · bộ lọc bản chính và 0b nhận khuôn bản sao
   đồng bộ " (1)", " - Copy", "(bản sao)".
2. XÓA PHÁP LÝ khâu kín: là ngoại lệ DUY NHẤT của X1 "cờ GỐC KHÔNG SỬA" và
   luật cốt lõi 3 (phải có Q-<mã>); tầng quét thêm 99_Goc, _Summary,
   _inbox/_da_nap, manifest dọn; đính kèm mail đã COMMITTED trung hòa bằng
   cờ de_ngoai "đã xóa theo Q-<mã>" (12j tự nhận); nhắc thay bản đã tải lên
   Project; "MỘT ngoại lệ" của NHATKY và QUYETDINH thành HAI, khai ở cả X5
   lẫn hai template sổ.
3. HOPTHU_CU đồng bộ chữ luật với máy: X4 rà 28 và X3E mục 1 nhận hộp cũ là
   lịch sử hợp lệ; C14 đủ cạnh; fixture DƯƠNG hộp cũ (bộ 69 ca).
4. Tách X5 mục 1b "Phần mềm và repo" GATE theo @DUAN.PHANMEM: bảng REPO,
   SECRET, dữ liệu khách, bàn giao source dồn về một chỗ; công ty không phần
   mềm hết trả thuế repo trên mọi việc đổi trạng thái (NOI_BO ~1628); X0 C2
   còn con trỏ; khối ẢNH CHỤP trùng luật GHI MỐC rút gọn; trần X5 lên 17.000
   với gate.
5. NGOẠI LỆ SỰ CỐ nối đủ ba đầu: X2 "luôn tính" có vế trừ; X5 THƯỜNG LỆ
   trỏ; X9 nhóm B trống vẫn gửi được thông báo sự cố. Phép thử HẬU CẦN vs
   CAM KẾT hết mơ hồ chữ "gửi". RA_NGOAI có lối cho người nhận mới (điều
   kiện dữ kiện tự khai RA_NGOAI + mở việc mức B khai phạm vi). MAIL MÁY
   "đính kèm cần lưu" có phép thử; khuôn DIGEST có ô dòng mail máy.
6. Máy giữ lời: phép 12 ghim 6 luật vòng 28 (43 luật); phép 2c phủ thêm hai
   số CHAT; cảnh báo kho Ổ MÁY ĐƠN (backup cùng ổ) ở X0 C1 và README; UX
   vòng 5 (câu mở tách chủ ngữ, vai trò trong câu 1, rewrap DOC_TRUOC, tín
   hiệu phần mềm ở cả hai cửa ngõ).

Watchlist trần: X0 ~15,4k/16.000 · X5 ~16,3k/17.000 · X9 ~6,0k/6.500.

## Vòng 28: vá theo hội đồng vòng 4 (20260825, điểm vòng 4: 85/100)

Điểm vòng 4: VẬN HÀNH 7,5 · KHÔNG SAI 8,0 · THÔNG MINH 8,5 · TOKEN 8,7 ·
KHÔNG MISS 9,0 · ĐƠN GIẢN 9,3. Vá:

1. kiem_van_hanh v24, CHỐNG CHẾT GIỮA BÁO CÁO (CAO của vòng 4, đã chạy thật):
   doc() và sha_file() bắt UnicodeDecodeError, OSError, gom vào phép 0f "file
   không đọc được" kèm chỉ dẫn, hết traceback vì file Office đang mở hay sổ
   sai encoding; file tạm ~$ không hash. Bộ lọc bản chính (TEMPLATE,
   conflicted, xung đột) dùng CHUNG cho X0 và NHATKY: chỉ còn bản xung đột
   thì 0d LỆCH "bản chính mất" thay vì PASS tự mâu thuẫn với 0b; 12k khi
   nhật ký mất hay rỗng đổi chẩn đoán GIỮ index; basename áp cho cả đính kèm
   de_ngoai; 12e nhận dạng hiển thị "Tên <mail@dom>".
2. ĐỔI HỘP THƯ có đường: @NHIP.HOPTHU_CU giữ danh sách hộp cũ (đổi hộp là
   mức C kèm QUYETDINH), 12e chấp nhận hộp lịch sử, nhật ký cũ hết bị đá oan.
3. MAIL MÁY có lối thoát nghiệp vụ (2 giám khảo cùng chỉ): hóa đơn, bản ký
   DocuSign, thông báo giao dịch, thư có đính kèm cần lưu THOÁT luật gom, đi
   pipeline như thư thường; chỉ thư thuần thông báo mới gom một dòng digest.
4. de_ngoai dữ-liệu-khách siết về đúng ý: chỉ DUMP, LOG, EXPORT hàng loạt từ
   hệ thống phần mềm; hợp đồng, CV có thông tin cá nhân vẫn theo 99_Goc.
5. Bảng REPO chuyển từ X0 C2 về X5 mục 1 (gom luật mức về một chỗ, X0 nhẹ
   bớt, công ty không phần mềm khỏi kéo khối này khi mở C2); thêm migration
   dev/staging = A, lệnh "rollback đi" giữa sự cố là gật plan; danh mục B
   "dọn nháp" khai rõ không áp trong repo.
6. RA_NGOAI thành phạm vi BAO TRÙM có luật quan hệ với phạm vi chi tiết và
   luật từ cấm (hết chặn oan hay lách lưới); X2 thêm NGOẠI LỆ SỰ CỐ (thông
   báo sự cố gửi ngay, DUKIEN ghi bù cùng phiên) và phép thử HẬU CẦN vs CAM
   KẾT; gói build hết đá luật bốn dạng (trong kho dạng Kho kèm sha, trong
   repo dạng Repo, sha vào ghi chú); XÓA THEO YÊU CẦU PHÁP LÝ có thủ tục
   xuyên tầng ở X5 mục 7; nghiệm thu source thuê ngoài vào 99_Goc.
7. BENCHMARK: các số route sinh lại sau khi X5 phình (phép 2c tự bắt trôi
   đúng như thiết kế); đoạn runtime-max hết dùng trần cũ; README câu mở
   tiếng người kèm tín hiệu "công ty có phần mềm cũng dùng được"; GHICHU
   header hết đếm tay số vòng; kiem_tra_bo header lên v21.

Watchlist trần: X0 ~15,6k/16.000 (97%) · X9 ~5,9k/6.500 · X3E ~10,8k/12.000.

## Vòng 27: vá theo hội đồng vòng 3 (20260825, điểm vòng 3: 80/100)

Điểm vòng 3: VẬN HÀNH 7,5 · THÔNG MINH 7,5 · KHÔNG SAI 7,5 · KHÔNG MISS 8,0 ·
TOKEN 8,5 · ĐƠN GIẢN 9,0. Ba giám khảo chạy thật và cùng bắt hai lỗi CAO do
vòng 26 sinh: de_ngoai bị schema 12h đánh hỏng, và "ba dạng" chưa thành "bốn
dạng" ở ba đầu luật. Vá:

1. kiem_van_hanh v23: glob NHATKY loại _TEMPLATE (template nằm trong _so theo
   cài chuẩn che phép 0d, xóa trục sự thật vẫn "hệ sạch" — kịch bản đinh của
   giám khảo vận hành) · kiem_payload miễn sha256/bytes cho đính kèm de_ngoai
   (đòi ten + ly_do), máy hết đá luật X3E; hai fixture mới (de_ngoai hợp lệ
   phải sạch, thiếu ly_do phải lệch), bộ fixture lên 68 ca · 12d và 12j2 xử
   nhật ký RỖNG như nhật ký vắng (hết lách qua nhánh "GIỮ registry"), khóa
   staging lấy từ cả registry · 0c phân biệt "chưa cài, chỉ thấy template"
   (bỏ qua êm — hết 3 LỆCH oan trên bộ mới clone) với "mất X0" và "nhiều
   ứng viên" · 12e loại cả bản conflicted.
2. BENCHMARK thành lời thật: bỏ tuyên bố "sinh lại tự động" treo; thêm phép
   2c so SỐ route với số đo thật (dung sai 10%, đo bằng cùng quy tắc mục),
   chế độ --sinh-benchmark in số mới; toàn bộ bảng route cập nhật theo số đo
   20260825; dòng CHAT tách hai con số (không EMAIL ~15.800, có EMAIL ~19.100).
3. "Bốn dạng" đồng bộ ba đầu: X1 mục 5, C14 hàng X1, header TAILIEU (kèm chú
   dạng Repo chỉ cho dự án @DUAN.PHANMEM).
4. Khép các khe phán đoán vòng 3: rollback môi trường chạy thật = C, xóa
   nhánh đã merge = A chưa merge = C (C2) · phép thử thẩm quyền cho xác nhận
   trong phiên + ngoại lệ VAI, TỶ LỆ chỉ theo văn bản ký (C7) · người dùng
   TỰ dán secret: nhắc một câu rồi làm tiếp, cấm chép giá trị vào sổ; lộ RA
   NGOÀI mới là VIEC mức gấp (C2) · thủ tục bàn giao CHUNG là mức B ở C9
   (CORE), phần thư mới nằm X3E · C5 có RA_NGOAI mặc định, LITE khỏi dừng
   hỏi phạm vi (gỡ vênh C0 "kích hoạt C5" với X2) · trigger vòng quý đặt
   ngay tại điểm tạo NHATKY quý mới trong X5.
5. Phần mềm nốt hai lỗ vòng 3: phát hành PHẦN MỀM chạy bảng kiểm trên BỘ TÀI
   LIỆU PHÁT HÀNH, build vào TAILIEU kèm sha256 và tag repo (X2) · đính kèm
   là dữ liệu khách hay dữ liệu cá nhân xử như de_ngoai, không kéo vào kho
   đồng bộ; MAIL MÁY (no-reply, bot, CI/CD) không cấp luồng, gom một dòng
   digest, bot công ty không tính "thư của mình" (X3E mục 2).
6. UX vòng 3: phím Mac là Cmd không phải Ctrl · DOC_TRUOC hết câu "AI làm
   bước 4" nói quá · "đồng bộ quan sát" tả bằng tiếng người · C14 hàng X3,
   X4 thêm C1; X4 rà 29 chú de_ngoai.

Watchlist trần cho vòng sau: X0 ~15,3k/16.000 · X9 ~5,9k/6.500 · X3E
~10,3k/12.000. Chưa vá, ghi nhận: nghiệm thu source thuê ngoài vào 99_Goc ·
con trỏ Repo@commit chết chưa có phép dò máy · lối khẩn cho truyền thông sự
cố production.

## Vòng 26: vá theo hội đồng vòng 2 (20260825, điểm vòng 2: 77,5/100)

Hội đồng chấm lại sau vòng 24-25: VẬN HÀNH 7,0 (tụt vì bản vá backup tự sinh
lỗi) · KHÔNG SAI 7,5 · KHÔNG MISS 7,5 · THÔNG MINH 8,0 · ĐƠN GIẢN 8,0 · TOKEN
8,5. Ba giám khảo chạy thật kịch bản đứt gãy và bắt được lỗi do chính vòng vá
trước sinh ra. Vá:

1. BACKUP HỎNG KÉP (3 giám khảo cùng bắt): đường dẫn chứa byte backspace 0x08
   (escape bị nuốt khi soạn) VÀ sao đệ quy _so vào con của _so. Sửa: chỉ sao
   năm sổ lõi + PLANNING + THU, loại _lich_su, _thu_staging, _inbox; phép
   kiểm 4 thêm CẢ DẢI control char để lớp lỗi này máy tự chặn từ nay.
2. CHỌN X0 TẤT ĐỊNH: sau git pull, X0_CAUHINH_TEMPLATE đứng trước bản mã theo
   bảng chữ nên kiem_van_hanh đọc nhầm rev 0, báo "chưa cài" trên hệ đang
   chạy. Sửa: glob loại _TEMPLATE và conflicted, nhiều ứng viên là LỆCH (0c);
   12e cũng lọc template và nhận dòng mang nhãn (EMAIL) đúng khuôn, fixture
   sửa theo (fixture cũ che đúng lỗi này). kiem_van_hanh lên v22.
3. TRỤC SỰ THẬT PHẢI TỒN TẠI: 0d đòi NHATKY khi rev >= 1, 0e đòi THU khi
   pipeline EMAIL có dấu vết; 0b quét conflicted cả bộ X ở gốc; thông điệp
   phép 0 tách VIEW (sinh lại mức A) khỏi SỔ (khôi phục mức C); 12d khi nhật
   ký mất đổi chẩn đoán "GIỮ registry", hết xúi xóa.
4. BANNER ĐANG GHI có nguồn số: bảng giữ bộ đếm cho banner, bảng cũ hơn lượt
   ghi gần nhất thì số ĐANG GHI đọc lại từ NHATKY trước khi tin.
5. ĐÍNH KÈM QUÁ LỚN hết đá pipeline: payload khai cờ de_ngoai kèm lý do,
   12j bỏ qua mục mang cờ; luật viết cả hai đầu (X3E mục 1 và 2).
6. PHẦN MỀM sâu thêm theo goal: SECRET không vào kho, sổ, phiên (lộ = VIEC
   mức gấp); TAILIEU trỏ được vào repo (dạng "Ở đâu" thứ tư); bản đồ mức
   thao tác repo (merge vào nhánh CI/CD deploy chạy thật = C, dev/staging =
   A, danh mục folder-C không áp trong repo); dump, log mang dữ liệu khách
   theo phạm vi C5; ví dụ đã điền và lối "chưa rõ" cho người không kỹ thuật.
7. Xác nhận BẰNG CHỮ của người dùng có thẩm quyền trong phiên = mức B (hết
   đường cụt "sếp nói trực tiếp vẫn là nguồn D"); thủ tục BÀN GIAO chuyển
   thành luật ở X3E mục 2 (X0 chỉ giữ giá trị); vòng quý có trigger tất định
   (lượt tạo NHATKY quý mới); C14 thêm hàng X3E, X5 thêm C11 C12; C0 và
   INSTRUCTION hết tàn dư "thang A-D thuộc REGULATED"; phiên CHAT bật EMAIL
   đưa thêm X3E vào Project (ba tài liệu cùng sửa); README định nghĩa Cowork,
   nói rõ cần máy tính, ví dụ <gốc>, TextEdit cho Mac, câu tắt thứ năm.
8. Trần theo vai đọc: X0 lên 16.000 (đọc theo mục, thuế là X0_INDEX), X4 lên
   5.500 (chỉ đọc khi RA_SOAT); phép kiểm 10 phủ cả tham chiếu "X3E mục n".

## Vòng 25: tách X3E, phạm vi phần mềm, vét nốt danh sách treo (20260825)

1. TÁCH X3E_EMAIL: X3 mục 6 (71% file, kín trần 11.488/11.500) thành file
   riêng X3E_EMAIL_TEMPLATE.md, X3 giữ stub trỏ sang. X3 xuống ~3.4k/4.500,
   X3E ~9.2k/12.000: hết bom trần, công ty LITE trên nền nạp cả file bớt
   ~2.700 token mỗi lượt CUA_VAO, EMAIL có chỗ vá. Phép kiểm 12 đọc gộp
   X3 cộng X3E; mô tả _thu_* trong X5 mục 4 nén còn bốn dòng trỏ X3E.
2. PHẠM VI TỔ CHỨC PHẦN MỀM (X0 C2 @DUAN.PHANMEM): công ty có dự án phần
   mềm khai repo, thành phần, môi trường, nơi chạy thật cho TỪNG phần mềm.
   Repo là nguồn sự thật của code, code không chép vào kho, không qua
   _INBOX; kho giữ hồ sơ và quyết định; deploy môi trường chạy thật là mức
   C (vào danh mục C của X5). X9 câu 3 hỏi thêm khi dự án là phần mềm.
3. Vét danh sách treo của vòng 24: trả lời INLINE tính là phần vừa viết
   (X3E mục 2) · đính kèm vượt @NHIP.TRANDINHKEM không kéo vào staging ·
   staging mồ côi có luật (X3E) và phép dò 12j2 (kiem_van_hanh) · nguồn
   scan không đọc được: cờ CHƯA ĐỌC ĐƯỢC, cấm rút dữ kiện (X0 C7) · bàn
   giao người dùng @NHIP.BANGIAO · dự án có trạng thái NGỪNG kèm thủ tục
   đóng (X0 C2).

## Vòng 24: hội đồng 6 lăng kính chấm độc lập (20260825)

Sáu giám khảo AI độc lập, mỗi người một lăng kính, đọc trọn bộ không nhiễm
nhận định của nhau: VẬN HÀNH 7,5 · TOKEN 7,5 · THÔNG MINH 7,5 · KHÔNG SAI 6,5
· KHÔNG MISS 6,5 · ĐƠN GIẢN 6,0. Trung bình 6,9/10. Vá theo phát hiện, ưu
tiên cái được nhiều lăng kính cùng chỉ:

1. LUẬT BẤT KHẢ THI (Không sai, CAO): X5 mục 3 bước 6 lệnh "COWORK đồng bộ
   view lên tài liệu Project", nền tảng không cho phiên ghi vào Project. Sửa:
   COWORK NHẮC người dùng tải, CHAT coi bản Project có thể cũ hơn kho.
2. VÊNH PROFILE (Không sai, CAO): luật cốt lõi 1 đòi mức nguồn "mọi lúc"
   nhưng DUKIEN ở LITE ghi "không áp dụng"; C9 gắn nhãn AUTOMATED/EMAIL trong
   khi X3, X4 (CORE) bắt đọc ngưỡng ở đó. Sửa: thang A-D và các ngưỡng nhịp
   là CORE; REGULATED chỉ giữ nguồn chỉ định và phạm vi chi tiết.
3. _INBOX VÔ GIA CƯ (Không sai + Không miss): dùng khắp X3, X4 mà không khai
   tọa độ. Thêm @DUONG.INBOX ở X0 C1, X9 dựng khi cài.
4. VẬN HÀNH: conflicted copy của CHÍNH file sổ có luật hòa giải (X5) và phép
   dò 0b; phép 0 đòi sổ lõi tồn tại (trước đây mất sổ PASS im lặng); banner
   đếm lượt ĐANG GHI; chốt sổ cấm đoán nội dung, lượt mở dòng ghi kèm giá trị
   chính; mất RIÊNG nhật ký thư thì GIỮ registry, thông điệp 12a/12d hết chỉ
   sai hướng; backup _so mỗi ngày 7 bản. kiem_van_hanh lên v21.
5. THÔNG MINH: luật gom MỘT lượt hỏi đưa vào INSTRUCTION (trước nằm ở X9 là
   file "đọc xong thì thôi"); vòng quý có chỗ đếm (mỗi lần rà ghi một dòng
   NHATKY); ngoại lệ HẬU CẦN cho giờ hẹn, địa chỉ trong X2; "làm luôn" hoàn
   tất trọn lượt được tính là CHỐT; @NHIP.TAIKHOAN nhận alias.
6. TOKEN: route NOI_BO chốt một mối (X5 mục 1 + mục 3 khi ghi sổ, ba nơi hết
   vênh); cắt lặp C11 ở INSTRUCTION; BENCHMARK thêm ghi chú trung thực về
   phiên CHAT nạp cả bộ. Còn treo: tách X3 mục 6 thành X3E (X3 dư 12 ký tự).
7. KHÔNG MISS: X9 thêm mục 3b kho CÓ SẴN file và 3c NÂNG CẤP BỘ khi git pull;
   NHATKY sang quý mới tự tạo từ template; hòa giải trùng mã G chạy MỌI
   profile (trước khóa sau nhãn PARALLEL); đánh số câu X9 hết trùng "câu 4".
8. ĐƠN GIẢN: README thêm "Ngày thường của bạn" (câu tắt, gắn folder mỗi
   phiên, chốt/ok), bảng "AI báo chữ lạ" (rev lệch, XUNG ĐỘT, CHƯA KIỂM),
   bẫy ZIP lồng thư mục, ghi chú Mac, "dữ liệu là của bạn"; bốn bước khớp
   DOC_TRUOC; TAILIEU trong X5 mục 4 sửa đúng thứ tự cột template; lệnh chạy
   script trong X4 đúng cú pháp và đủ tham số.

Trần X9 nâng 5.400 lên 6.500 (đọc một lần mỗi công ty, không phải thuế thường
trực). Chưa vá, ghi nhận cho vòng sau: tách X3E_EMAIL (gỡ bom trần X3, bớt
~2.700 token/lượt CUA_VAO cho LITE trên nền nạp cả file) · trả lời inline
trong trích dẫn cho CHỜ TÔI · nguồn scan không đọc được chữ · thủ tục bàn
giao người dùng · trạng thái dự án NGỪNG · staging mồ côi.

## Vá 20260825: phát hành qua git, chạy được trên Windows, cài đặt gọn

Không đổi luật vận hành, không đổi INSTRUCTION, không đổi X1 tới X5. Hai phần:

Phần một, ba lỗi lộ ra khi đưa bộ lên GitHub và chạy phép kiểm trên Windows:

1. Console Windows mặc định cp1252 không in được tiếng Việt, cả hai script
   crash ngay dòng in đầu tiên. Sửa: ép stdout, stderr sang UTF-8 khi mở, lỗi
   ký tự thì thay thế chứ không dừng phép kiểm.
2. Phép 12j so containment staging bằng chuỗi có "/", nhưng resolve() trên
   Windows trả "\" nên BỘ SẠCH cũng bị báo "resolve ra ngoài _thu_staging"
   oan, kéo fixture 66 ca FAIL. Sửa: so bằng pathlib (goc_staging in
   d.parents), áp cho cả kiểm đính kèm. kiem_van_hanh lên v20.
3. Docstring bao_phu chứa "\ " gây SyntaxWarning mỗi lần import. Chuyển raw
   string.

Phần hai, rà phản biện THỦ TỤC cài đặt (đổi X9 mục 0 và DOC_TRUOC, không đổi
luật): thủ tục cũ bắt người dùng làm ba việc thừa mà máy hay AI làm được.

1. Chọn lọc file để copy vào 00_Index: thừa, kiem_van_hanh loại hẳn 00_Index
   khỏi vùng quét nghiệp vụ nên file của người bảo trì nằm đó vô hại. Giờ:
   clone hay giải nén NGUYÊN TRẠNG thành 00_Index, còn được git pull khi bộ
   có bản mới.
2. Đổi tên file _TEMPLATE theo mã công ty trước khi cài: ngược quy trình, mã
   công ty là CÂU HỎI SỐ MỘT của phiên cài đặt; script cũng glob
   X0_CAUHINH_*.md nên tên nào máy cũng đọc. Giờ: AI đổi tên trong phiên cài
   đặt, sau khi biết mã.
3. Đưa X0 tới X5, X9 vào tài liệu Project là bước bắt buộc: chỉ phiên CHAT
   (không chạm kho) mới cần. Giờ là bước tùy chọn.

Việc tay còn đúng MỘT bước phải làm chính xác: dán NGUYÊN VĂN INSTRUCTION vào
Project instructions (AI không tạo hay sửa Project được). README.md là cửa vào
cho người tới từ link git, ba bước từ clone tới gõ "cài đặt".

## Vòng 23: v23 sang v24, khóa nốt chế độ --ho (vòng đánh giá 22, 9,6/10)

Lại chỉ sửa công cụ, không đổi luật, không đổi INSTRUCTION, không đổi X0 tới X5.

1. Hồi quy do chính v23 tạo ra. v23 thu hẹp danh sách dòng TAILIEU theo họ
   TRƯỚC khi tính phạm vi bao phủ, nên một dòng trỏ THƯ MỤC như `Kho 01_A/`
   biến mất khỏi phép tính và `01_A/BC_v02.docx` bị đề xuất _INBOX oan dù cả
   bộ hồ sơ đã có dòng trong sổ. v24 tách hai việc: phạm vi ĐÃ VÀO SỔ luôn
   tính trên TOÀN BỘ TAILIEU, còn phần kiểm file mất, sha và bất biến mới thu
   về đúng họ đang quét.
2. Cache đời cũ không được mang theo bằng chứng ổn định sai. Bản trước v19
   chỉ ghi MỘT mốc chung toàn kho; nếu mốc đó đã quá năm phút thì mọi file
   trong cache lập tức được coi là ổn định, kể cả file thật ra vừa đổi nội
   dung. v24 nhận diện cache thiếu `"v": 2`, vẫn nạp nội dung để so sha nhưng
   ĐÓNG DẤU LẠI mốc bằng thời điểm chạy, kèm một dòng lưu ý. Lần chạy đầu sau
   nâng cấp phải chờ đủ khoảng ổn định, từ lần sau trở đi mốc riêng từng file
   hoạt động bình thường.

Fixture lên 66 ca: một dòng `Kho 01_A/` phải bao phủ `01_A/BC_v02.docx` trong
chế độ --ho, và cache đời cũ không nhận ổn định ngay. Cả hai ca đều được chạy
ngược trên v23 để xác nhận là bắt được lỗi thật, không phải test tự thỏa mãn.

## Vòng 22: v22 sang v23, sửa lỗi thực thi của chế độ --ho (vòng đánh giá 21, 9,5/10)

Vòng này KHÔNG đổi luật, không đổi INSTRUCTION, không đổi X0 tới X5. Chỉ sửa
công cụ: vòng đánh giá 21 chạy thật chế độ --ho của v22 và bắt được bốn lỗi mà
bộ tự kiểm khi đó không thấy, vì hai fixture mới chỉ kiểm hàm khớp tên.

Lỗi đã sửa:

1. Selector mơ hồ. v22 hiểu --ho theo ba nghĩa lẫn nhau nên: truyền
   `01_A/BC_v01.docx` chỉ nhận đúng v01, bỏ sót v02 CÙNG HỌ; truyền thư mục
   `01_A` lại nhận cả họ KHAC; truyền tên `BC.docx` kéo cả họ BC ở dự án khác.
   v23 chỉ nhận ĐÚNG một đường dẫn tương đối tới MỘT FILE, từ file đó suy khóa
   (thư mục, họ đã chuẩn hóa), rồi quét mọi phiên bản cùng họ trong ĐÚNG thư
   mục đó. Thư mục, tên họ trơ, file không có thật, đường dẫn ra ngoài kho đều
   bị từ chối kèm câu nhắc cách dùng.
2. Cache giữ mốc thời gian TOÀN KHO nên luật ổn định bị phá: file vừa đổi nội
   dung, quét lần đầu ra KHÔNG XÁC ĐỊNH, quét lại ngay lập tức đã thành HIỆN
   HÀNH. v23 đổi cache sang MỐC RIÊNG TỪNG FILE, "luc" là lần đầu quan sát
   thấy đúng nội dung đang có; file giữ nguyên nội dung thì mốc giữ nguyên,
   file đổi nội dung thì mốc đặt lại. Ổn định = cùng nội dung VÀ đã giữ nội
   dung đó tối thiểu năm phút, đúng cả ở chế độ quét cả kho lẫn chế độ --ho.
3. Hợp nhất cache chỉ `update`, không loại mục cũ, nên file đã xóa khỏi một họ
   vẫn nằm lại trong cache. v23 THAY đúng tập cache của họ đang quét, các họ
   khác giữ nguyên.
4. --ho vẫn duyệt cả cây kho rồi mới lọc. v23 duyệt ĐÚNG thư mục của họ bằng
   iterdir, không rglob. Ở chế độ này phần đối chiếu TAILIEU cũng chỉ soi các
   dòng sổ thuộc đúng họ đó, và nhãn phép kiểm mang thêm phạm vi để không
   đọc nhầm thành đã kiểm cả kho.

Hai lỗi cách dùng thành LỆCH thay vì im lặng: --ho không khớp file nào (trước
đây PASS như thể mọi thứ sạch), và thiếu giá trị sau --ho (trước đây rơi về
quét cả kho).

Fixture: bỏ hai ca kiểm hàm khớp tên, thêm tám ca kiểm hành vi thật, tổng 64
ca. quet_ho và quan_sat_kho nhận tham số bay_gio để tiêm THỜI GIAN GIẢ, nhờ
vậy kiểm được cả mốc "ngay lập tức" lẫn mốc "sau năm phút" mà không phải chờ
thật. Nhãn số ca lấy từ chính danh sách fixture, hết lệch khi thêm bớt.

Không đụng tới X3, nên trần 11.500 ký tự vẫn còn nguyên khoảng trống ít ỏi cũ;
khuyến nghị của vòng đánh giá 21 về việc rút gọn hoặc tách phần kỹ thuật của
X3 giữ nguyên cho vòng sau.

## Vòng 21: v21 sang v22, đóng lớp thực thi (vòng đánh giá 20, 9,5/10, CORE và đặc tả EMAIL khóa được)

Bốn việc lớp thực thi, không kiến trúc mới:

1. @NHIP.TRANGTHAI có schema BẮT BUỘC tối thiểu: {"status": "OK"|"FAILED",
   "mailbox", "last_success_utc"}; chỉ lần quét thành công mới cập nhật
   last_success_utc; file thiếu, sai định dạng hay lần cuối FAILED đều coi
   là DỮ LIỆU CŨ.
2. Khóa digest đã gửi có nơi lưu BỀN: X0 C9 thêm @NHIP.DAUGUI, chỉ ghi khóa
   SAU khi kênh báo xác nhận gửi thành công, máy khởi động lại vẫn nhớ.
3. kiem_van_hanh v17 có chế độ --ho <đường dẫn hay họ file>: quét đúng MỘT
   họ tài liệu phục vụ X5 KIỂM BẢN, kết quả HỢP NHẤT vào cache thay vì ghi
   đè cache toàn kho, mốc ổn định toàn kho giữ nguyên. Hai fixture mới cho
   khop_ho (chế độ đường dẫn, chế độ họ tên), tổng 58 ca.
4. Câu chữ: "đang chờ AI" trong khuôn digest đổi thành "đang chờ BÊN NÀO"
   để khỏi hiểu nhầm là chờ hệ AI. X3 chạm trần nên RÚT GỌN câu cũ thay vì
   nâng trần (11.488/11.500 ký tự), đúng khuyến nghị. Luật then chốt lên 37.

## Vòng 20: v20 sang v21, vá hẹp digest và nguồn thời gian quét (vòng đánh giá 19, 9,3/10)

Ba điểm logic cộng một lỗi chữ, không kiến trúc mới:

1. Khuôn digest đủ thông tin hành động: dòng đầu đếm CẦN TÔI và CHỜ ĐỐI TÁC
   QUÁ HẠN; mỗi thư CẦN TÔI đủ mã luồng, người gửi, tiêu đề, ý chính, tôi
   cần làm gì, hạn, file; mục CHỜ ĐỐI TÁC nêu đang chờ ai, chờ việc gì, từ
   ngày nào; THEO DÕI riêng và ngắn; cuối tin giờ quét thật, giờ tạo tin,
   tình trạng DỮ LIỆU MỚI hay CŨ.
2. Cảnh báo dữ liệu cũ hết bị chống-lặp nuốt: chỉ GIÁ TRỊ giờ trình bày nằm
   ngoài hash; tình trạng MỚI/CŨ, tập việc quá hạn và thay đổi trạng thái
   thư PHẢI nằm trong hash, nên chuyển MỚI sang CŨ gửi cảnh báo đúng MỘT
   lần dù không có mail mới.
3. Hai khái niệm được định nghĩa tất định: X0 C9 thêm @NHIP.TRANGTHAI trỏ
   tới nguồn chứa thời điểm quét thành công cuối (X3 đọc giờ quét thật từ
   đây); X5 "đã cũ" = họ tài liệu CHƯA được quét trong PHIÊN hiện tại, lần
   đầu chạm trong phiên thì tự quét đúng họ.
4. Lỗi chữ: ghi chú đổi mới hết nói "Mười vòng". kiem_tra_bo v17 khai rõ
   phạm vi phép kiểm 12 (kiểm luật có mặt, không thay được nghiệm thu hành
   vi ở bộ email thật); benchmark gọi rõ "giảm 70%" là số của view mẫu rỗng,
   kèm mức tối đa runtime theo trần đã enforce. Luật then chốt lên 35.

## Vòng 19: v19 sang v20, bản vá nhỏ khóa EMAIL (vòng đánh giá 18, 9,2/10, CORE khóa được)

Đúng phạm vi bản vá được đề nghị, không kiến trúc mới:

1. Digest có KHUÔN BẮT BUỘC trong X3 mục 6, đúng thứ tự: đếm thư cần tôi xử
   lý và việc quá hạn · từng thư kèm ý chính, TÔI CẦN LÀM GÌ, hạn, file ·
   theo dõi để riêng · cuối tin là giờ quét THẬT với giờ tạo bản tin và cảnh
   báo dữ liệu cũ. Hệ đúng dữ liệu giờ bắt buộc phải NÓI cũng dễ đọc.
2. X0 C9 thêm @NHIP.TENGOI (EMAIL): tên, cách xưng hô, bí danh người dùng để
   máy nhận "thư chào đích danh mình"; bộ email TỰ lấy từ tên tài khoản khi
   cài, chỉ hỏi khi không lấy được. X3 trỏ về tham số này.
3. Đồng bộ bản hiện hành hết phụ thuộc người gọi: X5 KIỂM BẢN thêm luật
   trước khi SỬA hay DÙNG một họ tài liệu mà lần quan sát đã cũ thì tự quét
   đúng HỌ đó (không cả kho), kết quả rõ thì tự đồng bộ vai, không hỏi.
4. Mail thường lệ hết bị hỏi ngôn ngữ giọng điệu: X9 mặc định ngầm hiểu
   (ngôn ngữ theo luồng thư hay người nhận, giọng chuyên nghiệp ngắn gọn, từ
   cấm X1), chỉ hỏi khi có hai lựa chọn khác nhau đáng kể.
5. Trần token khép nốt: kiem_van_hanh v16 áp trần runtime 2.400 ký tự cho
   X0_INDEX (BANG_DIEU_KHIEN đã có 4.200 từ v19); X3 nâng trần 11.500 vì
   khuôn digest và @NHIP.TENGOI; sửa hai lỗi trình bày: X9 hết ghi "bảy sổ
   rỗng" (đúng cấu trúc năm sổ lõi cộng sổ phụ theo vai trò), ngày ở đầu
   INSTRUCTION và ghi chú đổi mới về đúng 20260824. Luật then chốt lên 32.

## Vòng 18: v18 sang v19, bảy điểm để khóa bản (vòng đánh giá 17, 8,3/10 "có thể pilot")

Đúng yêu cầu "chỉ tập trung bảy điểm, không thêm kiến trúc mới":

1. Profile EMAIL hết mâu thuẫn với AUTOMATED: INSTRUCTION (lên v11) liệt kê đủ
   REGULATED, PARALLEL, AUTOMATED, EMAIL và khai luật "một mục phục vụ nhiều
   profile, bật MỘT trong số đó là phải đọc"; X0 C9 đổi nhãn thành "AUTOMATED
   và EMAIL", @NHIP.HOPTHU và @NHIP.TAIKHOAN gắn nhãn (EMAIL) từng dòng.
2. CHỜ TÔI lên NĂM điều kiện: thêm "yêu cầu đọc từ phần người gửi vừa viết
   (cắt lịch sử trích dẫn, chữ ký, câu xã giao please find/see)" và "yêu cầu
   nhắm vào mình, thư chào đích danh người khác không tính dù mình ở To".
   Đây là hai lỗi đã lộ ở hệ email thật (ca PIP breakdown).
3. Khép kín bộ quan sát: X4 thêm câu tắt thứ năm "đồng bộ quan sát": kết quả
   ổn định không xung đột thì TỰ ghi vai HIỆN HÀNH/CŨ vào TAILIEU mức A; chỉ
   hỏi khi XUNG ĐỘT hay KHÔNG XÁC ĐỊNH. RA_SOAT thuần vẫn chỉ báo cáo.
4. BẤT BIẾN viết rõ hai nghĩa: NỘI DUNG (byte) file đã gửi không sửa đè;
   TRẠNG THÁI nghiệp vụ của dòng TAILIEU vẫn tiến lên khi có bằng chứng.
5. X9: mail thường lệ đầu tiên chạy với cấu hình tối thiểu (người nhận và
   phạm vi, ngôn ngữ, giọng, từ cấm mặc định), không phải trả lời cả nhóm B;
   số liệu hay cam kết xuất hiện là dừng hỏi đủ.
6. Digest chống lặp bằng KHÓA NỘI DUNG (mốc mail cuối + hash phần nghiệp vụ,
   giờ trình bày không vào hash): sáng gửi rồi, chiều có mail mới thì khóa
   đổi, không chặn oan; tên file digest mang ngày giờ, không ghi đè.
7. Đóng gói tự kiểm độc lập: ZIP chứa sẵn bản _GOP; kiem_tra_bo v15 thêm
   --gop <file> và mặc định im lặng với chi tiết fixture (LECH của tình
   huống âm là chủ ý), --verbose xem đủ. Trần X3 nâng 10.500 lên 11.000 ký
   tự vì mục 6 dày thêm hai luật. kiem_van_hanh v15 áp trần runtime 4.200 ký
   tự cho BANG_DIEU_KHIEN. DOC_TRUOC nói rõ hệ sổ: NĂM sổ lõi, PLANNING mức
   C, THU theo profile EMAIL, hai view máy sinh, hệ lõi không phình.

## Vòng 17: v17 sang v18, vòng đời staging và đối chiếu index chính xác (vòng đánh giá 16)

Vòng đánh giá 16 chấm 9,6/10, tuyên bố CORE/LITE đủ chốt; EMAIL còn một mâu
thuẫn vòng đời staging và hai PASS giả. Năm điểm, sửa hết:

1. Mâu thuẫn dọn-staging với 12j giải bằng MANIFEST DỌN _so\_thu_don_staging.json
   (máy sinh, ghi TRƯỚC khi xóa): mỗi khóa một mục purged_at, eml_final_path,
   attachment_final_paths, sha256. 12j giờ hiểu vòng đời: PREPARED chưa
   COMMITTED thì staging bắt buộc còn; COMMITTED đã dọn có manifest hợp lệ thì
   staging vắng là PASS; vắng mà thiếu một trong hai điều là lệch.
2. Khe ../_so/_thu_staging đóng: containment bằng normpath thay cho lstrip,
   cấm tuyệt đối, cấm ".." sau chuẩn hóa; lúc rà 12j còn resolve() đường dẫn
   thật và bắt buộc nằm dưới _thu_staging, chặn cả symlink thoát ra.
3. Tên đính kèm phải là BASENAME thuần (không /, \, ".."), file sau resolve()
   phải còn trong staging: ten "../../../secret.txt" hết đường lách.
4. Index đối chiếu CHÍNH XÁC: tập mục index bằng ĐÚNG tập "khoa|operation_id"
   của các mail đã COMMITTED (thừa mục ngoài payload cũng lệch); sổ và mã dòng
   trong index phải khớp thao tác payload; 12l so mã dòng theo ĐÚNG Ô bảng
   (V-1 không ăn theo V-10), mục index có "hash" thì đối chiếu thêm sha256
   nội dung dòng.
5. Payload đủ dữ liệu phục hồi thật: bắt buộc metadata nguồn conv_id,
   nguoi_gui, thoi_diem UTC, tieu_de và eml_sha256; .eml hay body không được
   rỗng và phải khớp eml_sha256; thư mục staging tên sha256(khóa), mỗi mail
   một thư mục, hai mail hết đường dùng chung.

Fixture email lên 40 kịch bản, tổng 56 ca (có ca PASS chủ động: staging đã dọn
đúng luật); luật then chốt lên 28. CORE không đổi.

## Vòng 16: v16 sang v17, kiểm dữ liệu thật và đóng khe ghi đồng thời (vòng đánh giá 15)

Vòng đánh giá 15 chấm 9,5/10: CORE đủ mức chốt, EMAIL là release candidate cần
kiểm staging/index thật và đóng khe "ghi sổ xong nhưng chưa ghi index". Năm điểm:

1. kiem_payload kiểm DỮ LIỆU chứ không chỉ tên trường: staging phải là đường
   dẫn tương đối nằm BÊN TRONG _so\_thu_staging (chặn tuyệt đối, chặn chấm
   chấm thoát ra); mỗi thao tác đủ operation_id (chuỗi, DUY NHẤT trong một
   mail), sổ đích thuộc THU VIEC DUKIEN TAILIEU QUYETDINH, mã dòng, nội dung
   dòng; đính kèm khai đủ ten, sha256, bytes. Thiếu @NHIP.HOPTHU khi EMAIL đã
   chạy: 12e LỆCH cấu hình, hết BỎ QUA.
2. Khe sinh dòng đôi đóng ở X3 bước 2: ĐỐI CHIẾU trước ghi sau. Chưa có trong
   index thì TÌM mã dòng trong sổ đích trước; thấy rồi (lần trước chết sau khi
   ghi sổ, trước khi ghi index) thì CHỈ bổ sung index; chưa thấy mới ghi dòng,
   đọc lại xác minh, rồi bổ sung index.
3. Ba phép máy mới cộng ba dòng X4 (29 tới 31): 12j staging thật trên đĩa
   (thư mục tồn tại, có .eml hay body, từng đính kèm đúng sha256 và byte);
   12k index đủ hai chiều (thao tác COMMITTED phải có trong index, index không
   trỏ mail không có trong nhật ký); 12l index trỏ mã dòng CÓ THẬT trong sổ.
4. Khóa một dạng: trường "khoa" DUY NHẤT, gặp "msgId" kiểu cũ là dòng hỏng chờ
   một lượt migration riêng, không đọc lẫn hai dạng. Khóa fallback serialize
   CỐ ĐỊNH: FB-<sha256(convId + thời điểm UTC + tiêu đề chuẩn hóa + 200 ký tự
   đầu thân)>.
5. Staging hết tăng vô hạn: DỌN STAGING là việc mức A khi đủ BỐN điều (đã
   COMMITTED, đích và sha xác minh, .eml bằng chứng đã chuyển 04_Trao_doi,
   qua thời gian đệm X0 C9 @NHIP.DEMSTAGING mặc định 30 ngày).

Fixture email lên 29 kịch bản, tổng 45 ca, luật then chốt lên 24. Không đụng
INSTRUCTION, X1, X2; X0 chỉ thêm @NHIP.DEMSTAGING.

## Vòng 15: v15 sang v16, chốt lớp bảo đảm dữ liệu email theo vòng đánh giá 14

Vòng đánh giá 14 chấm 9,4/10: CORE gần mức chốt, EMAIL còn hở lớp phục hồi dữ
liệu. Năm điểm, sửa hết:

1. Payload phục hồi THẬT: X3 mục 6 bước 1 thành "STAGING trước, PREPARED sau".
   Nguyên văn thư (.eml hay body đầy đủ) cùng mọi đính kèm lưu vào
   `_so\_thu_staging\<khóa an toàn>\` TRƯỚC khi append PREPARED; payload mang
   đường dẫn staging cộng danh sách THAO TÁC ghi sổ đã chuẩn hóa (operation_id,
   sổ đích, nội dung dòng). Tên với dung lượng đính kèm suông không còn được
   tính là payload phục hồi; staging hụt thì không được append PREPARED.
2. `source_msg_id` có nơi lưu thật: index máy sinh `_so\_thu_ap_dung.json`,
   mỗi thao tác đã áp một dòng "source_msg_id + operation_id" trỏ "sổ + mã
   dòng". Sổ người đọc không phải mang thêm cột khóa máy; mất index thì dựng
   lại bằng đối chiếu payload với sổ. Đăng ký ở X5 mục 4 cùng _thu_staging.
3. Schema sự kiện cứng: mỗi dòng nhật ký phải là JSON object có "ev" chỉ nhận
   PREPARED hoặc COMMITTED, "khoa" là CHUỖI, "hop_thu" bắt buộc ở cả hai loại;
   mỗi mail đúng HAI sự kiện, PREPARED đứng TRƯỚC COMMITTED; lượt phục hồi
   không append PREPARED mới. Khắc ở X3 mục 6, máy giữ ở kiem_van_hanh.
4. kiem_van_hanh v12: parse theo TỪNG KHÓA giữ thứ tự và số lần xuất hiện.
   Bảy PASS giả bị đóng: PREPARED thiếu payload nhưng đã COMMITTED (12h),
   COMMITTED mồ côi, COMMITTED đứng trước PREPARED, sự kiện lặp (12g),
   ev gõ sai kiểu "TYPO" thành dòng hỏng chứ không thành COMMITTED (12b),
   sự kiện thiếu hop_thu thành dòng hỏng (12b), hai dòng THU cùng
   Conversation-ID (12i), registry dạng `{}` (12d). Hai ca crash hết crash:
   registry là danh sách chứa object, msgId là array; đều thành LỆCH.
   Registry bắt buộc là DANH SÁCH CHUỖI khóa.
5. kiem_tra_bo v12: fixture email từ 9 lên 18 kịch bản, tổng 34 ca, vẫn gọi
   toàn bộ kiem_email(); danh mục luật then chốt từ 15 lên 20 (thêm staging
   trước PREPARED, index áp thao tác, mô hình hai sự kiện, Conversation-ID
   duy nhất, registry danh sách chuỗi).

Không đụng INSTRUCTION, X0, X1, X2, X4, X9; CORE giữ nguyên như bản 9,7 điểm.

## Vòng 14: v14 sang v15, làm lại máy kiểm email theo vòng đánh giá 13

```
1  Nhật ký email nâng thành NHẬT KÝ SỰ KIỆN: PREPARED mang payload phục hồi đủ
   dựng lại THU, VIEC, TAILIEU và tải lại đính kèm mà không đọc lại hộp thư;
   ghi sổ idempotent theo source_msg_id; COMMITTED khi sổ và đính kèm đủ;
   registry CHỈ dựng từ COMMITTED. Hết luôn hai câu mâu thuẫn trong X3: khóa
   fallback chỉ còn một dạng mạnh, đính kèm nằm gọn trong bước 2 trước COMMITTED
2  kiem_email viết lại và bị fixture gọi CẢ HÀM trên 9 kịch bản: bộ sạch PASS
   hết; mất registry, mất nhật ký, dòng rác, dòng "42", lượt dở dang, registry
   thừa mã, hộp thư giả kiểu substring, khóa fallback không dấu @ trùng hai
   luồng: TỪNG CA đều phải bị bắt, không ca nào crash
3  X4 dòng rà email 24 tới 28 viết lại theo mô hình mới
4  Fixture tổng lên 25 ca, luật then chốt lên 15
```

## Vòng 13: v13 sang v14, vá vòng đánh giá 12

```
1  BỎ lọc tiền tố "9": 98_Assets và 99_Goc là vùng nghiệp vụ phải quét (chính X4
   đòi kiểm sha 99_Goc), chỉ loại đích danh 99_Archive; công ty muốn loại thêm
   thì khai _quan_sat_bo.txt. Fixture chứng minh cả ba nhánh
2  Benchmark tách đúng route: CUA_VAO thường chỉ X3 mục 1 tới 5, CUA_VAO EMAIL
   mới cộng mục 6, hết cách trình bày gây hiểu nạp email hai lần
3  Email commit/recovery: THỨ TỰ GHI AN TOÀN nhật ký trước, registry sau, THU
   cuối; nhật ký là nguồn sự thật, thiếu đâu bổ sung đó, không nạp lại từ hộp
   thư; dòng trùng do chạy lại vô hại. Fallback thiếu Message-ID nâng thành
   (Conversation-ID, thời điểm tới giây, sha256 tiêu đề + 200 ký tự đầu thân)
4  Máy rà email: kiem_van_hanh phép 12 (registry đủ so nhật ký, Message-ID cuối
   không đứng ở hai luồng THU, mail thuộc đúng hộp khai báo), X4 thêm dòng rà
   24 tới 26; nhật ký nạp thêm trường hop_thu để rà được sai hộp
5  Fixture lên 18 ca, luật then chốt lên 13
```

## Vòng 12: v12 sang v13, vá 2 lỗi vận hành vòng đánh giá 11

```
1  Dòng TAILIEU trỏ THƯ MỤC (kết thúc bằng dấu chéo) bao phủ mọi file con: hồ sơ
   nhiều tài liệu hết bị đề xuất _INBOX thừa liên tục; luật khớp: trùng đường
   dẫn file, hoặc nằm trong thư mục sổ đã trỏ
2  Bỏ loại theo đuôi trên toàn kho: script và config NGHIỆP VỤ ngoài 00_Index
   được quan sát như tài liệu thường; chỉ loại vùng hệ thống, rác thật, và danh
   sách đường dẫn công ty tự khai ở _so/_quan_sat_bo.txt
3  Email: thêm nhật ký nạp APPEND-ONLY _thu_nhat_ky.ndjson làm nguồn dựng lại
   registry; mất cả hai thì lần quét đầu chỉ xuất danh sách ứng viên chờ duyệt,
   không tự nạp
4  Fixture lên 16 ca (bao phủ thư mục, script nghiệp vụ được quét, schema THU);
   phép 12 giữ 11 luật; benchmark sinh lại với số hiện tại
```

## Vòng 11: v11 sang v12, vá 3 lỗi thực thi vòng đánh giá 10 và nâng spec EMAIL

```
1  Luật 5 phút ENFORCE THẬT: cache non hơn 5 phút không được dùng làm bằng chứng
   ổn định (trước chỉ in cảnh báo nhưng vẫn công nhận HIỆN HÀNH)
2  Bộ quan sát loại hẳn 00_Index, file .py .ps1 .bat .json khỏi vùng quét nghiệp
   vụ; hết cảnh đề xuất đưa chính file luật và script vào _INBOX
3  Chuẩn hóa họ đổi cụm phân cách về MỘT dấu "_" thay vì xóa sạch: AB_C_v01 và
   A_BC_v02 là hai họ khác nhau, (v3) -v03 _v02 vẫn về một họ
4  Spec EMAIL nâng theo góp ý: THU thêm cột Conversation-ID làm khóa luồng ·
   registry _thu_da_nap.json giữ TẬP mọi Message-ID đã nạp, quét lại toàn hộp
   không nạp trùng · CHỜ ĐỐI TÁC cũng cần bằng chứng mong phản hồi, thư thông
   báo không treo chờ ai · digest trùng ngày chỉ chặn khi lần trước THÀNH CÔNG
5  Fixture lên 14 ca (thêm: AB_C không trộn A_BC, 00_Index và script bị loại);
   phép 12 giữ 9 luật nghiệp vụ
6  Ngoài bundle: bộ email SẢN XUẤT của công ty mẫu đã được vá cùng ngày theo
   cùng spec (cửa sổ 24h theo giờ chạy, CHỜ TÔI ba điều kiện, một công ty một
   hộp thư, Message-ID vào dữ liệu quét, chặn gửi digest cũ, token ra ngoài kho)
```

## Vòng 10: v10 sang v11, vá vòng đánh giá 9 và thêm profile EMAIL

```
1  Ngoại lệ "thêm lệnh cấm là B" giờ nằm ở CẢ BA nơi cùng câu chữ: X0 C11,
   INSTRUCTION mục 5 (lên v10), X5 mục 1; hết chuyện AI đọc file nào ra mức đó
2  Họ tài liệu CHUẨN HÓA bỏ mọi ký tự phân cách: (v3), -v03, _v02 về cùng một
   họ; fixture kiểm cả tính cùng-họ chứ không chỉ lấy được số, hết PASS giả
3  Bộ quan sát quét MỌI file thường (kmz, kml, csv, dwg, eml, zip...), chỉ loại
   danh sách đuôi rác; hash đủ mọi cỡ file, file lớn chỉ cảnh báo chậm
4  Hai lần quét cách nhau dưới 5 phút tính là một lần quan sát, giữ mốc cũ
5  Phép 3c đọc đúng CỘT Ghi lần, 3d chỉ nhận plan có trạng thái ĐÃ GHI
6  Cột Ở đâu phân biệt trỏ FILE (tới tên file, có sha) với trỏ BỘ HỒ SƠ (kết
   thúc bằng dấu chéo, không sha)
7  Profile EMAIL (X0 C0, X3 mục 6, sổ THU.md): Message-ID làm khóa chống trùng,
   trạng thái CHỜ TÔI (đủ ba điều kiện: không phải thư mình, mình ở To, có yêu
   cầu thật) · CHỜ ĐỐI TÁC · THEO DÕI · ĐÃ ĐÓNG · BỎ QUA (nói một lần, không
   nhắc lại), mọi tài khoản người dùng khai @NHIP.TAIKHOAN, đính kèm liên kết
   bằng sha256, thư gửi kèm file thành ảnh chụp ĐÃ GỬI DUYỆT, digest chống lặp
   theo ngày chạy và cấm gửi lại bản cũ khi sinh lỗi, token để ngoài kho đồng
   bộ. Chỉ nạp khi quét mail, không tăng thuế bộ lõi. Nguyên tắc gốc, học từ
   ca thật hai công ty chung một máy: MỘT CÔNG TY MỘT HỘP THƯ QUÉT
   (@NHIP.HOPTHU), hộp thư công ty khác trên cùng máy không được vào pipeline
```

## Vòng 9: v09 sang v10, code làm đúng điều tài liệu tuyên bố

```
1  Gỡ mâu thuẫn "gửi duyệt": đúng FILE đã gửi là ẢNH CHỤP bằng chứng không sửa
   đè, việc tiếp tục trên vN+1, plan không đóng; ĐÃ PHÁT HÀNH, NỘP, KÝ, CẤP là
   mốc chính thức theo luật cốt lõi 3. X2 với X5 hết đá nhau
2  Luật "ổn định qua hai lần quan sát" CHẠY THẬT: cache _so/_quan_sat_truoc.json
   (máy sinh), lần quét đầu không công nhận gì, lần hai cùng nội dung mới nhận
3  sha256 thật thay cho dung lượng file; file quá 200MB ghi chú riêng
4  File không có vN chọn theo mtime sau khi ổn định; mtime không phân định được
   thì KHÔNG XÁC ĐỊNH, không bao giờ chọn theo thứ tự tên
5  File mới độc lập (chưa có bản cũ) vẫn được đề xuất _INBOX
6  Khóa nhận dạng họ tài liệu = thư mục tương đối + họ tên: hai dự án trùng tên
   file không lẫn nhau; đối chiếu sổ theo đường dẫn tương đối
7  Fixture nâng lên 11 ca, phủ đúng 6 ca vòng 8 yêu cầu, chạy trên hàm thật kể
   cả quét kho hai lượt trong thư mục tạm
```

Lượt TEAM AGENT nội bộ trên v10: 15 agent, ba hướng (kiểm toán nhất quán toàn bộ
luật, kiểm thử đối kháng chạy script thật, đóng vai giám đốc không rành kỹ thuật
diễn một tuần làm việc), mỗi phát hiện qua một agent phản biện cố bẻ. 12 phát
hiện, 4 bị bẻ gãy có bằng chứng, 8 đứng vững và ĐÃ VÁ HẾT trong chính bản này:

```
1  Mâu thuẫn X1 với nhóm khóa C11 về thêm giá trị cấm: khắc ngoại lệ tường minh,
   THÊM lệnh cấm (siết chặt) là mức B, GỠ hay NỚI là mức C kèm QUYETDINH
2  X4 hứa quá khả năng script: thêm phép 3c (lượt XONG phải để dấu mã G ở ít
   nhất một sổ) và 3d (lượt mức C phải khớp plan), phủ đủ dòng rà 19 và 23
3  Tuple bất biến của script thiếu ĐÃ DUYỆT NỘI BỘ và TRẢ HỒ SƠ: đã thêm, kèm
   ca fixture giữ code khớp luật
4  Cache quan sát hỏng làm crash: tự phục hồi, coi như lần quét đầu
5  Mã G định dạng cũ (không cửa) cướp watermark: loại khỏi watermark, báo riêng
   "cân nhắc di trú"
6  Regex vN sót dạng -v03 và (v03): đã nới, kèm hai ca fixture chống nhận nhầm
7  Phiên CHAT không có đường đọc sổ (mức CAO): X5 bước 6 quy định COWORK đồng bộ
   BANG_DIEU_KHIEN và X0_INDEX lên tài liệu Project mỗi lần sinh lại, bảng thêm
   khối "Tài liệu đang hoạt động"; CHAT đọc bản Project kèm nhãn ngày
8  Kịch bản gửi gấp dồn ma sát: X9 gom mọi câu thiếu của cùng việc vào một lượt
   hỏi, bảng điều khiển nhắc mục C12 còn thiếu chặn phát hành, X2 cho in gọn
   dòng ĐẠT nhưng cấm bỏ dòng
```

Tám vòng trước: v02 theo phản biện độc lập trên v01; v03 vá 5 điểm vòng 2; v04 vá 10
mục stress-test; v05 vá vòng 3 thêm test hồi quy; v06 tối ưu token và máy hóa;
v07 sửa regression vòng 5; v08 vá 3 điểm vòng 6 (9,1/10); v09 thêm state engine
quan sát file và vòng duyệt nhiều bước theo vòng 7 (8,9/10 vì thiếu hai năng lực
nghiệp vụ này).

## Vòng 8: v08 sang v09, state engine quan sát file và vòng duyệt

Nguyên tắc mới, chữ của người đánh giá: "tự nhận bản hiện hành theo bằng chứng,
không tự nhận bản cuối theo sự im lặng". Không đụng INSTRUCTION (thuế thường trực
giữ nguyên), chỉ sửa X3, X5, TAILIEU và hai script.

```
1  TAILIEU thêm ba cột: VAI PHIÊN BẢN (HIỆN HÀNH, CŨ, XUNG ĐỘT, KHÔNG XÁC ĐỊNH)
   · QUAN SÁT LÚC · CĂN CỨ TRẠNG THÁI. Vai là quan sát của máy, đổi tự do theo
   bằng chứng quét (mức A); trạng thái nghiệp vụ chỉ đổi khi có căn cứ
2  Trạng thái nghiệp vụ tách vòng duyệt khỏi phát hành: NHÁP · CHỜ DUYỆT NỘI BỘ
   · ĐÃ GỬI DUYỆT · ĐÃ DUYỆT NỘI BỘ · ĐÃ PHÁT HÀNH · ĐÃ NỘP · TRẢ HỒ SƠ · ĐÃ
   CẤP · ĐÃ KÝ. Bản gửi sếp hay đối tác góp ý SỬA TIẾP ĐƯỢC; bất biến chỉ áp
   cho ĐÃ PHÁT HÀNH, ĐÃ NỘP, ĐÃ KÝ, ĐÃ CẤP
3  SUY BẢN HIỆN HÀNH (X5 mục 4): tám quy tắc, gồm bỏ file tạm, vN cao hơn là
   ứng viên, cùng vN khác hash là XUNG ĐỘT cấm tự chọn, và im lặng KHÔNG BAO GIỜ
   suy ra đã duyệt, đã gửi hay đã xong
4  GHI MỐC (X5 mục 1): một plan C bao trùm cả chu kỳ soạn, gửi sếp, sửa, gửi đối
   tác, trình ký; mỗi lần gửi là một dòng NHATKY + TAILIEU cập nhật, plan KHÔNG
   đóng; chỉ xin gật lại khi đổi mục tiêu, người nhận, cam kết, nguồn, số chưa
   có sổ, loại phát hành hay hành động khó phục hồi
5  X3: hành động người dùng ĐÃ LÀM là sự kiện đầu vào, AI kiểm chứng và ghi mức
   A hồi tố, không xin phép; thiếu thông tin chưa ảnh hưởng bước tiếp thì ghi
   CHƯA XÁC NHẬN, không hỏi
6  kiem_van_hanh v4: truyền thêm <gốc kho> thì đối chiếu TAILIEU với file thật
   (mất file, sha lệch, bản bất biến bị sửa tại chỗ, họ tài liệu cùng vN khác
   nhau) và ĐỀ XUẤT sự kiện _INBOX cho bản hiện hành chưa vào sổ. Chỉ báo cáo
7  kiem_tra_bo v4: fixture hồi quy 4 ca cho suy bản hiện hành (import thẳng hàm
   thật), phép kiểm 12 giữ 6 luật nghiệp vụ then chốt khỏi rơi khi rút gọn,
   phép 2b chặn metadata version trôi giữa BENCHMARK và DOC_TRUOC
```

## Vòng 7: v07 sang v08, vá 3 điểm vòng đánh giá 6

```
1  kiem_tra_bo v3: GHICHU_DOI_MOI_v* (pattern, đúng một file), BENCHMARK_TOKEN.md
   và chính hai script vào danh mục bắt buộc; tất cả phải có mặt VÀ nằm nguyên
   văn trong _GOP. Script và GHICHU miễn kiểm ký tự cấm với tham chiếu chéo, vì
   script giữ danh sách ký tự cấm làm mẫu dò còn GHICHU trích nguyên văn vòng cũ
2  "Mới nhất" theo WATERMARK TỪNG CỬA: giữa các cửa của kho mây không có thứ tự
   thời gian tin được, nên kiem_van_hanh v3 chỉ so BANG_DIEU_KHIEN với watermark
   của CHÍNH cửa sinh ra nó; cửa khác có lượt ngày mới hơn thì in LƯU Ý, không
   phán LỆCH. BANG_DIEU_KHIEN header thêm dòng watermark từng cửa (X5 mục 3
   bước 6)
3  Hạ lời "khóa thật" xuống đúng bản chất: ĐỊNH DANH LƯỢT (<CỬA>.<giờ phút>.<hậu
   tố ngẫu nhiên>) cộng QUY TẮC HÒA GIẢI XUNG ĐỘT tất định; nói thẳng đây là hòa
   giải sau xung đột, không phải khóa nguyên tử, và PARALLEL phải tuyên bố giới
   hạn đó khi quảng bá
```

## Vòng 6: v06 sang v07, sửa regression theo vòng đánh giá 5

```
1  kiem_van_hanh.py v2: parse đúng CỘT của dòng dữ liệu bảng thay vì đếm chuỗi
   toàn văn (hết báo sai "ĐANG GHI" từ câu hướng dẫn, hết đếm mã G nhắc lại trong
   cột Làm gì); mã mới nhất xếp theo ngày và số, không theo vị trí; X0 rev 0 trả
   BỎ QUA "chưa cài đặt" thay vì LỆCH; schema kiểm cả từng dòng dữ liệu; thêm mã
   Q và P vào kiểm trùng
2  Tham chiếu X5 mục 2 sang mục 3 ở X4, X9, NHATKY mẫu (regression khi chuyển nội
   dung từ INSTRUCTION về X5). kiem_tra_bo thêm phép kiểm 10: mọi tham chiếu
   "X<k> mục <n>" và "INSTRUCTION mục <n>" phải trỏ tới mục có thật, để loại lỗi
   này khỏi tái diễn
3  kiem_tra_bo v2: thiếu bản gộp _GOP là FAIL, chỉ bỏ qua khi truyền cờ
   --skip-gop tường minh; hết chuyện "PASS hết" mà một phép bị âm thầm bỏ qua
4  X9 thống nhất: ba câu bắt buộc cộng một câu profile; _so là bảy sổ cộng một
   view X0_INDEX
5  Schema DUKIEN CỐ ĐỊNH mọi profile: LITE ghi "không áp dụng" ở ô Mức nguồn,
   khỏi migration khi bật REGULATED sau
6  Mã đồng thời cùng một cửa: khóa thật là cặp (mã G, định danh phiên ghi ở cột
   Phiên), mã G chỉ là số hiển thị; quy tắc phục hồi tất định "dòng nằm sau đổi
   mã"; mã chỉ điền vào các sổ SAU khi đứng vững ở NHATKY nên trùng bị giam trong
   NHATKY; nói thẳng file thường không có khóa nguyên tử, PARALLEL khuyến nghị
   mỗi cửa một phiên ghi một thời điểm
7  Benchmark sửa lời: "giảm 71% theo benchmark tĩnh, chờ số phiên thật", không
   tuyên bố kết quả runtime khi cột phiên thật còn trống
```

## Vòng 5: v05 sang v06, tối ưu token và máy hóa

```
1  INSTRUCTION rút từ 15,4K ký tự xuống dưới 8K (xấp xỉ 2.600 token, trước xấp xỉ
   5.100): chỉ giữ luật gốc, router, A B C rút gọn, 9 luật cốt lõi, trace, mở và
   đóng phiên. Toàn bộ danh mục mức chi tiết, thường lệ, nháp, kiểm bản, chốt,
   phiên không người dồn về X5 mục 1; router thêm dòng "mọi việc đổi trạng thái
   đọc X5 mục 1", tức chi tiết chỉ tốn token khi thật sự đổi trạng thái
2  X0_INDEX: view máy sinh của X0 (rev, kho, profile, dự án, vị trí mục, mục còn
   thiếu, trần 1.500 ký tự). Mở phiên đọc view này thay vì mở cả X0; giá trị đưa
   vào đầu ra vẫn phải đọc X0 đúng mục. Sinh lại mỗi khi rev tăng
3  PROFILE ở X0 C0: CORE luôn bật · REGULATED (mức nguồn, phát hành, hồ sơ nhà
   nước) · PARALLEL (nhiều cửa kho, kiểm trùng mã) · AUTOMATED (phiên không
   người, nhịp mail) · LITE = chỉ CORE. Khối luật gắn nhãn chỉ áp khi bật; công
   ty nhỏ không phải mang luật mình không dùng. X9 thêm câu 4 chọn profile
4  MÁY HÓA: thêm kiem_van_hanh.py chạy trên 00_Index của công ty thật, kiểm 8
   nhóm không cần suy luận (rev khớp, X0_INDEX đúng rev, NHATKY treo, mã G trùng,
   plan ĐÃ GHI thiếu mã, schema bảng, sổ vượt ngưỡng, bảng điều khiển cũ). X4
   route RA_SOAT chạy script trước, AI chỉ xử phần cần phán đoán
5  TOKEN BUDGET enforce bằng máy: kiem_tra_bo.py thêm phép kiểm 9, mỗi file có
   trần ký tự (INSTRUCTION 8K, X0_INDEX 1,5K, BANG_DIEU_KHIEN 1,2K...), vượt là
   FAIL không được đóng gói; in luôn thuế thường trực ước lượng
6  BENCHMARK_TOKEN.md: bảng đo bằng máy chi phí context theo từng loại yêu cầu,
   trước và sau v06, kèm cột trống để ghi số đo phiên chạy thật
```

Thuế thường trực đo được (ký tự / 3): xem BENCHMARK_TOKEN.md sinh kèm bộ.

## Vòng 4: v04 sang v05, vá theo vòng đánh giá 3

```
1  KHÓA GHI ĐỒNG THỜI: mã ghi đổi sang G-<YYYYMMDD>-<CỬA>-<NN>; hai phiên ở hai
   cửa kho khác nhau không thể trùng mã theo cấu tạo, miễn nhiễm trễ đồng bộ mây.
   Trong cùng một cửa: đọc NHATKY ngay trước khi cấp, cộng luật kiểm LẠI sau khi
   mở dòng: thấy trùng thì đổi mã dòng MÌNH kèm ghi chú. Rà 12 là lưới cuối.
   Không dùng file khóa vì kho mây đồng bộ trễ làm khóa không tin được
2  HÀNG RÀO NGUỒN CHỈ ĐỊNH (X0 C7): khai theo loại dữ kiện + phạm vi, không khai
   trần · khai hay đổi là sửa C7 nhóm khóa, mức C có QUYETDINH · mức D không bao
   giờ làm nguồn chỉ định cho đầu ra ngoài · hồ sơ nhà nước dùng nguồn dưới A
   phải in cảnh báo ở dòng kiểm 6 và người dùng xác nhận riêng dòng đó
3  NGOẠI LỆ CÀI ĐẶT rev 0 (INSTRUCTION mục 1, X0 C11, X9): điền giá trị ban đầu
   không coi là sửa nhóm khóa; C11 hiệu lực từ rev 1
4  Ngày sinh bảng vào thẳng mẫu hai dòng mở phiên: "· bảng <YYYY-MM-DD>"
5  QUYETDINH nói chính xác: không xóa, không sửa NỘI DUNG; dòng cũ chỉ được cập
   nhật hai ô quản trị Trạng thái và Thay bởi
6  Đặc tả tối thiểu chuyển Markdown sang CSV/SQLite (X5 mục 7): nguồn sự thật sau
   chuyển, mã vẫn cấp qua NHATKY Markdown mở dòng trước, phục hồi bằng "chốt sổ",
   backup trước lượt ghi đổi cấu trúc, BANG_DIEU_KHIEN sinh từ nguồn mới
7  BỘ TEST HỒI QUY kiem_tra_bo.py: tám phép kiểm chạy máy (đủ file, phiên bản
   khớp, tham chiếu X0 Cn tồn tại, ký tự cấm, số cột bảng, bộ trạng thái, dạng mã
   G, bản gộp _GOP khớp nguyên văn). Chạy sạch mới được đóng gói
```

Instruction lên v08; X0 X2 X5 lên v05; X9 lên v03; NHATKY và QUYETDINH mẫu sửa
lời; X1 X3 X4 và các sổ mẫu còn lại không đổi.

## Vòng 3: v03 sang v04, vá theo stress-test

```
H1  Thường lệ với số liệu ĐÃ CÓ SỔ: được phép xuất hiện, khi có thì bảng kiểm
    THƯỜNG LỆ thêm dòng 1 và 2; số chưa có sổ vẫn đá về C đầy đủ
H2  Nguồn chỉ định (X0 C7): dữ kiện lấy từ nguồn đã khai là nguồn thắng được dùng
    cho phạm vi tương ứng dù mức nguồn dưới tối thiểu, ghi kèm nguồn. Gỡ thế bí
    "hồ sơ nhà nước đòi mức A nhưng nguồn thẩm quyền hợp lệ là mail kỹ thuật mức B"
H3  Phiên không có người (INSTRUCTION mục 6): A làm và ghi; B và C chỉ chuẩn bị,
    xếp bảng chờ duyệt, mở VIEC hạn phiên sau; người dùng duyệt một lượt khi về
V1  Lô lẫn mức: tách theo mức, phần A đi trước, B gom một câu, C một plan
V2  Ranh giới nháp: tạo nháp là A, dọn nháp chưa vào sổ là B, xóa thứ đã vào sổ
    hay đã phát hành mới là C; note chỉ vào TAILIEU khi cần tìm lại về sau
V3  Nhóm khóa C6 thu về vai, tỷ lệ, lệnh cấm nêu tên; đầu mối liên hệ tách ra
    @BEN.DAUMOI, sửa là mức B
V4  Trong một lượt trả lời kiểm bản mới nhất MỘT lần cho mỗi file
V5  BANG_DIEU_KHIEN sinh lại ngay khi cũ hơn lượt ghi gần nhất hoặc chứa mốc đã
    qua, không đợi ngưỡng 7 ngày; hai dòng mở phiên luôn in ngày bảng
V6  Nhiều plan CHỜ CHỐT thì lệnh chốt phải nêu mã, không nêu thì hỏi kèm danh sách
#14 X5 mục 2: đọc NHATKY ngay trước khi cấp mã G, chặn hai phiên cấp trùng
```

Instruction lên v07; X0 X2 X5 lên v04; X1 X3 X4 X9 và bảy sổ mẫu không đổi.

## Vòng 2: v02 sang v03, vá 5 điểm

```
1  NGOẠI LỆ THƯỜNG LỆ trong mức C (INSTRUCTION mục 5, X2 mức THƯỜNG LỆ): trao đổi
   thường lệ ra ngoài không chứa số liệu mới, cam kết, điều khoản thì không mở plan,
   chỉ trình bản xem trước kèm bảng kiểm rút gọn 3·4·7·8, người dùng xác nhận gửi là
   chốt. Chọn đường ngoại lệ thay vì thêm mức C1 C2 để giữ hệ ba mức; xuất hiện số
   liệu hay cam kết giữa chừng thì tự nâng về C đầy đủ. X1 và X2 vẫn luôn được đọc
2  Plan C treo không chặn việc không liên quan (INSTRUCTION mục 2): treo hiện trên
   dòng trạng thái; chỉ bắt xử lý trước khi yêu cầu mới chạm cùng tài liệu, dữ kiện
   hay dòng sổ. Treo quá ngưỡng thì lên bàn làm việc
3  Định nghĩa BẢN KHÁC khi kiểm trước ghi (INSTRUCTION mục 5, X5 mục 2): có sha256
   trong TAILIEU thì so sha256; không có thì mtime VÀ dung lượng cùng đổi; đồng bộ
   mây đổi mtime suông không tính, nghi ngờ thì đối chiếu nội dung. Tránh báo động
   giả của kho mây
4  BANG_DIEU_KHIEN nói rõ (X1 mục 5, X5 mục 3): ĐƯỢC chứa số liệu dẫn xuất, tóm tắt,
   mã trỏ; CẤM chép nguyên dòng sổ và cấm dùng bảng làm căn cứ cập nhật sổ
5  Ngưỡng lưu trữ đa tiêu chí (X5 mục 7): 500 dòng HOẶC 1 MB HOẶC đọc tìm chậm rõ
   rệt, chạm một trong ba là xử lý
```

Instruction lên v06; X0 X1 X2 X5 lên v03; X3 X4 và bảy sổ mẫu không đổi, giữ v02.

## Vòng 1: v01 sang v02

Nguyên tắc chung được thêm thành
LUẬT SỐ KHÔNG: kiểm soát tỷ lệ với rủi ro; việc thường chạy nhanh, phê duyệt nặng
chỉ dành cho việc rủi ro; truy vết giữ nguyên đầy đủ ở mọi mức.

## Đổi lớn

```
1  BỎ CƠ CHẾ NƯỚNG. v01 chép giá trị X0 sang X1 tới X5 kèm dấu [@MÃ] và hệ x0_rev
   để giữ đồng bộ; thực chạy đã ghi nhận hai lần lệch nội dung dù cùng rev, và một
   lần đổi mục không nướng vẫn phải cập nhật header cả năm file. v02: X1 tới X5 là
   luật thuần, TRỎ về mục X0, đọc giá trị tại chỗ lúc dùng. Xóa được [@MÃ], x0_rev,
   luật nướng lại 3b, và các dòng rà lệch nướng.

2  MỨC TÁC ĐỘNG A B C (INSTRUCTION mục 5). Phân cấp PHÊ DUYỆT, không phân cấp truy
   vết: A tự làm tự ghi báo một dòng · B hỏi một câu rồi làm và ghi · C mới cần plan,
   gật, chốt. Danh mục C cứng cho mọi công ty (đầu ra rời công ty, bản đã phát hành,
   nhóm khóa, xóa và di chuyển hàng loạt). Công ty chỉ được NÂNG mức ở X0 C13, cấm hạ.
   Điều kiện an toàn của A B: kiểm bản mới nhất của file trước khi ghi, vì người dùng
   có thể sửa tay song song; lệch thì tự nâng mức.

3  CHỐT chỉ bắt buộc ở mức C. Lệnh trực tiếp ("sửa đi", "làm luôn") được định nghĩa
   là gật. Plan không chốt thì giữ CHỜ CHỐT, không thành plan treo giả.

4  TRACE ẨN (INSTRUCTION mục 8). Thân trả lời nói tiếng người; mã P G V D T dồn về
   một dòng Trace cuối. Người dùng chỉ cần biết bốn khái niệm: Việc, Tài liệu,
   Dữ kiện, Quyết định.

5  MỞ PHIÊN còn HAI dòng, bàn sạch còn một; "điểm danh" mới bung đủ. Giữ kiểm tra
   rev và mốc vì đó là hàng rào chống trôi rẻ nhất.
```

## Đổi vừa

```
6   Phân loại yêu cầu: "một loại duy nhất" đổi thành Ý ĐỊNH CHÍNH + hành động phụ,
    AI tự xâu chuỗi (mục 3). Mức tác động lấy theo bước cao nhất trong chuỗi.
7   Router thành mức đọc TỐI THIỂU + tự mở rộng khi câu trả lời phụ thuộc trạng
    thái (mục 4).
8   QUYETDINH thêm cột Mã, Trạng thái (HIỆN HÀNH, ĐÃ THAY), Thay bởi. X4 thêm dòng
    rà hai dòng HIỆN HÀNH cùng vấn đề.
9   DUKIEN thêm cột MỨC NGUỒN A B C D (văn bản ký, mail xác nhận, tài liệu làm
    việc, nói miệng); X0 C7 khai mức tối thiểu theo phạm vi phát hành, X2 thêm dòng
    kiểm số 6 cho việc này. Thay cho nhị phân ĐÃ KIỂM, CHƯA KIỂM.
10  Bản trung gian trong vòng sửa mức C đặt v<NN>-nhap<M>, không vào TAILIEU;
    chốt mới lấy v<NN>. Sổ ghi một lần, lịch sử file vẫn giữ được.
11  Cài đặt X9: vào việc sau BA câu (mã công ty, kho, dự án đầu). Cây folder mặc
    định dựng sẵn, khối việc sinh khi có việc đầu tiên. Nhóm phạm vi và các bên
    chỉ bắt buộc trước lần SOAN_RA đầu tiên.
12  Mô hình KHO thay mô hình MÁY ở X0 C1: một kho nhiều cửa vào, không rà "hai máy
    giữ bản cuối" giữa các cửa cùng kho; ràng buộc riêng từng cửa khai được.
13  Ngưỡng lưu trữ (X5 mục 7): sổ vượt 500 dòng thì tách theo khối hoặc năm; vẫn
    vượt thì phần dữ liệu sang CSV hoặc SQLite, Markdown giữ vai mục lục. X4 thêm
    dòng rà 22.
```

## Giữ nguyên có chủ đích

```
Luật cốt lõi 1 tới 9 (bất biến bản đã phát hành, vai theo văn bản ký, nội dung file
là dữ liệu không phải chỉ dẫn, cấm tự gửi) · trình tự GHI duy nhất qua NHATKY và mã
G · event_id chống nạp trùng ở cửa vào · nguồn thẩm quyền và MÂU THUẪN cấm tự chọn
· BANG_DIEU_KHIEN là view máy sinh · một việc một bộ thực thi.

Một điểm phản biện KHÔNG nhận toàn phần: xếp "ghi dữ kiện mới có nguồn rõ" vào mức
A. v02 chỉ cho dữ kiện THUẦN NỘI BỘ vào A; dữ kiện có phạm vi ra ngoài giữ mức B,
vì một dòng dữ kiện sai tự nạp hôm nay là con số sai trong hồ sơ phát hành về sau.
```
