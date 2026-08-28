# GHI CHÚ ĐỔI MỚI · STARTER · 20260824

File này cho người đánh giá. Không phải luật, không cần copy vào bộ chạy.
Các vòng xếp mới nhất ở trên; vòng 9 (v10) từng qua thêm một lượt team agent
nội bộ tự rà, tự dựng case, tự đóng vai người dùng.


Các mục vòng 1 tới 35 đã chuyển sang `GHICHU_LICHSU_v24_20260824.md` để file này
không phình mãi - X9 mục 3c chép GHICHU vào kho MỌI công ty mỗi lượt nâng cấp.
Lịch sử không mất, chỉ đổi chỗ.

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

Trạng thái: 24 phép của kiem_tra_bo, 38 phép của kiem_van_hanh (vòng 47 đếm lại: dòng này từng khai 21 và 37, SAI), 91 fixture, 73
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

