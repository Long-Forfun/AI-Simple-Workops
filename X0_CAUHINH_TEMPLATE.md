```
X0 · CẤU HÌNH · <MÃ> · v13 · rev 0 · <YYYYMMDD>
instruction_yeu_cau: v11
TEMPLATE. rev 0 nghĩa là chưa cài đặt. Phiên đầu chạy X9 để điền, xong đặt rev: 1.
Mọi tham số của công ty nằm ở đây, không ở đâu khác. X1 tới X5 là luật và TRỎ về các
mục của file này; cần giá trị thì đọc tại đây ngay lúc dùng, không chép đi đâu.
Đổi giá trị: sửa đúng mục, tăng rev, ghi ngày cạnh dòng đổi. Thuộc C11 thì thêm
QUYETDINH và là việc mức C. Mỗi lần tăng rev: sinh lại view `_so\X0_INDEX.md`
(rev, kho, profile, dự án, vị trí mục, mục còn thiếu) để mở phiên không phải mở
cả file này.
```

# C0. Profile

Khối luật gắn nhãn profile chỉ áp khi bật ở đây. Không bật thì AI bỏ qua khối đó,
không đọc, không hỏi.

```
@PROFILE   CORE luôn bật: việc, tài liệu, quyết định, mức A B C, ghi sổ
  [ ] REGULATED   nguồn chỉ định, phạm vi chi tiết, phát hành chính thức, hồ
                  sơ nhà nước (thang mức nguồn A-D là CORE theo C7; tập phạm vi
                  tối thiểu của C5 là CORE; REGULATED kích hoạt phần CHI TIẾT
                  của C5, C7 và X2 đầy đủ)
  [ ] PARALLEL    kho nhiều cửa, nhiều phiên cùng ghi (luật cửa ở C1, kiểm trùng
                  mã ở X5 mục 3 bước 2)
  [ ] AUTOMATED   tác vụ hẹn giờ, giám sát (C9, X3 nhịp, luật phiên không
                  người ở X5 mục 1)
  [ ] EMAIL       mail là kênh nghiệp vụ chính: sổ mã thư THU, Message-ID chống
                  nạp trùng, cột chờ phản hồi, chống lặp digest, quy trình tải
                  đính kèm (X3E, sổ _so\THU.md)
  LITE = chỉ CORE, không bật gì thêm
```

Công ty nhỏ làm nội bộ chọn LITE là đủ; bật thêm profile khi việc thật xuất hiện
(mức B, không phải nhóm khóa).

# C1. Công ty và kho

Kho là MỘT bản dữ liệu duy nhất. Một kho có thể có nhiều cửa vào (nhiều máy cùng
đồng bộ một thư mục mây); các cửa không phải các kho riêng, không rà "hai máy cùng
giữ bản cuối" giữa các cửa của cùng một kho.

```
@CTY.MA          <điền, 3-4 ký tự viết hoa>
@CTY.TEN         <điền>
@CTY.VAITRO      <điền, công ty đóng vai gì trong công việc chính>

@KHO.CHINH       <điền: kho đặt ở đâu, ví dụ thư mục Dropbox / ổ máy đơn>
                 CUA1 = <đường dẫn gốc trên máy 1> · thiết bị <tên>
                 <thêm CUA2... nếu kho mây có nhiều máy cùng vào>
@KHO.LUAT_CUA    <điền ràng buộc riêng từng cửa nếu có: giới hạn dung lượng ghi,
                 không xóa được, tải theo yêu cầu phải quét hai lượt... hoặc "không có">
@KHO.CU          <kho đã ngừng, chỉ tra lịch sử, hoặc "không có">
@DUONG.SO        <gốc kho>\00_Index\_so\
@DUONG.INBOX     <gốc kho>\00_Index\_so\_inbox\ · mục đã nạp chuyển
                 vào _da_nap\ con của chính folder này
@DUONG.LUAT      <gốc kho>\00_Index\
@DUONG.PROJECT   Claude Project "<tên>", thư viện đọc, không phải sổ
@DUONG.DRIVE     <chưa điền, chỉ khai khi dùng tầng chia sẻ mây riêng>
```

Cột "Ở đâu" của sổ TAILIEU chỉ nhận: "Kho <đường dẫn tương đối từ gốc kho>" ·
"Project <đường dẫn doc>" · "Drive <ID folder>" · "Repo <mã PM> <đường dẫn
trong repo>@<commit hay tag>" (chỉ cho dòng thuộc dự án @DUAN.PHANMEM, ô
sha256 bỏ trống vì repo tự giữ lịch sử). Ngoài bốn dạng đó là cấm.
Trỏ tới MỘT FILE thì ghi tới tận tên file; trỏ tới cả BỘ HỒ SƠ thì ghi đường dẫn
thư mục kết thúc bằng dấu \ và bỏ trống ô sha256 (bộ quan sát chỉ đối chiếu sha
cho dòng trỏ file).

# C2. Dự án

Một công ty có nhiều dự án. Mọi việc, dữ kiện, tài liệu gắn đúng một dự án.

```
@DUAN.<MÃ DA>    <tên dự án>          đang chạy | NGỪNG
@DUAN.CTY        việc của công ty, không thuộc dự án nào    luôn có

@DUAN.PHANMEM    dự án PHẦN MỀM khai thêm PHẠM VI TỔ CHỨC, mỗi phần mềm một dòng:
  <MÃ PM>  <tên> · repo <URL hay đường dẫn> · thành phần chính · môi trường
           (dev, staging, prod ở đâu) · nơi chạy thật
  Repo là NGUỒN SỰ THẬT của code và lịch sử sửa: code KHÔNG chép vào kho,
  KHÔNG đi qua _INBOX; kho chỉ giữ hồ sơ, quyết định, tài liệu phát hành.
  Việc chạm code vẫn ghi VIEC, QUYETDINH như thường, cột Liên kết trỏ
  commit hay PR. MỨC cho từng thao tác repo: bảng REPO ở X5 mục 1. Một phần mềm nhiều
  repo: mỗi repo một vế trên cùng dòng. Đặc tả, tài liệu sống cùng code nằm
  trong repo, TAILIEU trỏ dạng "Repo" theo C1.
  SECRET (API key, mật khẩu, chuỗi kết nối, .env): KHÔNG nằm trong kho đồng
  bộ, KHÔNG vào sổ hay _INBOX, KHÔNG dán vào phiên; nơi giữ khai ở dòng
  phần mềm (vault, secret manager). Lộ secret RA NGOÀI công ty: VIEC mức
  gấp, thu hồi trước, ghi sau. Người dùng TỰ dán secret vào phiên: nhắc một
  câu về rủi ro rồi xử tiếp việc chính; sổ chỉ mô tả LOẠI secret và hệ liên
  quan, CẤM chép giá trị secret vào bất kỳ sổ hay file nào của kho. Phần mềm giữ dữ liệu khách hàng: dump, log mang dữ liệu
  đó coi là đầu ra có phạm vi theo C5, không kéo về kho tùy tiện.
  Bản BÀN GIAO source từ thuê ngoài là FILE GỐC NGOÀI: vào 99_Goc, cờ GỐC,
  sha256 (luật "code không chép vào kho" chỉ áp cho repo của CHÍNH công ty).
  Ví dụ một dòng đã điền: APP  Ứng dụng đặt hàng · repo github.com/cty/app
  · web + máy chủ · dev máy đội kỹ thuật, chạy thật app.cty.vn. Mục nào
  chưa rõ: trả lời "chưa rõ, hỏi đội kỹ thuật", AI ghi <chưa điền> vào C12
```

Đóng dự án: đổi sang NGỪNG (mức B), việc đang mở chuyển HỦY hay bàn giao dự
án khác, sổ giữ nguyên tra lịch sử, bàn làm việc và digest lọc bỏ.
Dự án mới: thêm dòng ở đây (mức B), dựng folder con trong các folder chức năng cần
dùng, rồi mới mở việc đầu tiên.

# C3. Folder và khối

Tầng ngoài là CHỨC NĂNG, tầng trong là DỰ ÁN hoặc hồ sơ của dự án.

```
@FOLDER.CHUCNANG   cây mặc định, X9 dựng sẵn, thêm bớt khi công ty đã có cây riêng
  00_Index   01_Phap_ly   02_Ky_thuat   03_Thuong_mai   04_Trao_doi   05_Mau
  98_Assets  99_Goc       99_Archive

@FOLDER.KHOI       khối việc sinh KHI CÓ VIỆC ĐẦU TIÊN của khối, không bắt khai trước
  <MÃ KHỐI>  <mô tả>  <folder thật>  <dự án>

@FOLDER.CON        dùng khi cần, đúng tên: 01_Phap_ly 02_Ky_thuat 03_Thuong_mai
                   04_Trao_doi 05_Mau 99_Goc _lich_su
                   bản nộp: 01_Phap_ly\_NOP_YYYYMMDD\ rồi khóa
```

Dự án mới cần chức năng đã có thì mở folder con, không mở folder chức năng mới.

# C4. Tên file

```
@TEN.MAY       <KHOI>_<YYYYMMDD>_<LOAI>_<DoiTac>_<MoTa>_v<NN>.ext
@TEN.PROJECT   <Ten>_v<N>_<YYYYMMDD>.md
@TEN.NHAP      bản trung gian chưa chốt: v<NN>-nhap<M>, không vào TAILIEU
@TEN.LOAI      CV TT PA BG DT HD PL MOU BB BC SL GP MAU MAIL <thêm bớt khi cài>
```

Không dấu, không khoảng trắng. Cấm final, copy, moi_nhat, ban_cuoi. Nội bộ DoiTac là
NA. Bản ký thêm `_SIGNED`, bất biến. Trạng thái ở TAILIEU, không vào tên file.
Không đổi tên file cũ đã phát hành. Đổi tên hàng loạt là mức C, phải có QUYETDINH.

# C5. Phạm vi

```
@PHAMVI.TAP      tập đóng, đầu ra mang đúng một giá trị
  <MÃ PHẠM VI>   <cho loại tài liệu nào, gửi ai>
  NOI_BO         trong công ty                              luôn có
  RA_NGOAI       mọi đầu ra rời công ty khi chưa khai phạm vi chi tiết
                 (LITE dùng ngay giá trị này, khỏi dừng hỏi)   luôn có
  RA_NGOAI là phạm vi BAO TRÙM: dữ kiện khai phạm vi chi tiết nào cũng tự
  thỏa RA_NGOAI; đầu ra mang phạm vi chi tiết KHÔNG dùng được dữ kiện chỉ
  khai RA_NGOAI. Đã khai phạm vi chi tiết: đầu ra mới phải mang phạm vi chi
  tiết; từ cấm áp cho RA_NGOAI là HỢP của mọi dòng @PHAMVI.CAM cộng X1

@PHAMVI.CAM      <điền: phạm vi nào cấm từ nào. Trúng một từ là dừng>
@PHAMVI.BATBUOC  <điền: phạm vi nào bắt buộc khai gì, hậu quả nếu thiếu>
```

# C6. Các bên

```
@BEN.VAI   tên · vai, tỷ lệ nếu có · văn bản ký xác lập
  <điền từng bên. Chưa có văn bản ký thì ghi CHƯA KIỂM>

@BEN.DAUMOI  đầu mối liên hệ từng bên: tên, chức danh, kênh
  <điền dần. KHÔNG thuộc nhóm khóa: thêm sửa là mức B>

@BEN.CAM   <điền các lệnh cấm nêu tên: cấm đưa bên nào, số nào ra phạm vi nào>
```

Vai chỉ đổi khi có văn bản ký mới. Cách gọi trong hội thoại không làm đổi vai.
Gỡ một lệnh cấm: không xóa dòng, gạch và ghi "gỡ ngày, căn cứ mã", chỉ gỡ khi dữ kiện
gốc đổi trạng thái.

# C7. Nguồn thẩm quyền và mức nguồn (CORE: thang A-D và mức tối thiểu áp MỌI
profile; riêng nguồn chỉ định và phạm vi chi tiết: profile REGULATED)

```
@NGUON.<LOẠI>    <loại dữ kiện> lấy từ <tài liệu + bản + ngày>
@NGUON.CONLAI    chưa khai, mặc định CHƯA KIỂM
```

Mức nguồn của một dữ kiện, ghi ở cột "Mức nguồn" của DUKIEN:

```
A  văn bản ký, văn bản chính thức có số
B  mail hoặc biên bản xác nhận của bên có thẩm quyền
C  tài liệu làm việc: draft, bảng tính đối tác, ghi chú họp có file
D  nói miệng, tin nhắn chưa xác nhận
```

Mức nguồn TỐI THIỂU theo phạm vi của đầu ra:

```
@NGUON.MUC_TOI_THIEU
  hồ sơ nộp cơ quan nhà nước       A
  đầu ra rời công ty khác          B    <chỉnh khi cài nếu công ty cần chặt hơn>
  NOI_BO                           A tới D đều được, nhưng phải ghi kèm mức
```

Ngoại lệ NGUỒN CHỈ ĐỊNH, có bốn hàng rào:

```
1  mỗi nguồn chỉ định khai theo LOẠI DỮ KIỆN + PHẠM VI được dùng, không khai trần
   theo loại: @NGUON.<LOẠI> ... dùng cho phạm vi <danh sách>
2  khai mới hay đổi nguồn chỉ định là sửa C7, thuộc nhóm khóa: mức C, có QUYETDINH
3  nguồn mức D không bao giờ làm nguồn chỉ định cho đầu ra rời công ty
4  hồ sơ nộp cơ quan nhà nước dùng nguồn dưới mức A: bảng kiểm X2 dòng 6 phải IN
   CẢNH BÁO "dưới chuẩn mặc định, theo nguồn chỉ định <mã>" và người dùng xác nhận
   riêng dòng đó
```

Đạt cả bốn thì dữ kiện lấy đúng từ nguồn chỉ định được dùng cho phạm vi đã khai dù
mức nguồn thấp hơn tối thiểu, đầu ra ghi kèm "theo <tên nguồn> <bản, ngày>". Mức
tối thiểu áp cho mọi dữ kiện KHÔNG có nguồn chỉ định.

Xác nhận BẰNG CHỮ của người dùng ngay trong phiên: ghi mức B, nguồn "xác
nhận trong phiên <ngày>". Phép thử thẩm quyền: người dùng chỉ có thẩm quyền
với dữ kiện thuộc vai của CHÍNH công ty mình theo C6; dữ kiện thuộc bên khác,
dù diễn đạt kiểu gì, tối đa là D. NGOẠI LỆ: VAI và TỶ LỆ các bên không đi
đường này, chỉ đổi theo văn bản ký (C6, luật cốt lõi 2).
Nguồn là ảnh chụp, scan KHÔNG đọc được chữ: TAILIEU nhận file kèm cờ CHƯA
ĐỌC ĐƯỢC, CẤM rút dữ kiện từ đó cho tới khi có bản đọc được hay người dùng
đọc tay và xác nhận từng số. Số đo kèm đơn vị hoặc loại số đo. Hai nguồn cãi nhau: DUKIEN ghi MÂU THUẪN, cấm tự
chọn. Bản mới thay bản cũ chỉ khi có mail, biên bản, hay xác nhận trong phiên của
bên có thẩm quyền (tức từ mức B).

# C8. Thuật ngữ và hình thức

```
@TUNGU.DUNG          <điền>
@TUNGU.CAM           <điền>
@HINHTHUC.KYTUCAM    <điền, gợi ý: em-dash · en-dash · dấu xấp xỉ · mũi tên>
@HINHTHUC.SO         <điền quy tắc làm tròn>
@HINHTHUC.VANPHONG   <điền>
@HINHTHUC.FONT       <điền>
@HINHTHUC.QUANHE     dùng sự kiện kèm ngày · động từ cấm: <điền>
```

# C9. Nhịp và bộ thực thi (các ngưỡng @NHIP.RALAI, HETHAN, CHODOITAC, INBOX,
MUIGIO và @MATHU là CORE, mọi profile đọc khi X3, X4 trỏ tới; dòng gắn nhãn
AUTOMATED, EMAIL chỉ đọc khi bật profile đó)

```
@NHIP.QUETMAIL   <điền nhịp, ngưỡng nhắc>
@NHIP.HOPTHU     (EMAIL) <điền HỘP THƯ NGHIỆP VỤ của CHÍNH công ty này. Một công ty một
                 hộp thư quét; bộ quét CHỈ đọc hộp này, hộp thư của công ty khác
                 trên cùng máy tuyệt đối không vào pipeline>
@NHIP.HOPTHU_CU  (EMAIL) <các hộp thư CŨ sau khi đổi domain hay đổi hộp,
                 hoặc "chưa có"; đổi @NHIP.HOPTHU là mức C kèm QUYETDINH,
                 hộp cũ chuyển xuống đây để nhật ký lịch sử không bị đá oan>
@NHIP.TAIKHOAN   (EMAIL) <điền các địa chỉ NGƯỜI DÙNG dùng để gửi, CỘNG các
                 alias hay hộp nhóm mà thư nhắm tới người dùng vẫn đến (info@,
                 sales@...); dùng nhận diện "thư của mình", "mình ở To" X3E>
@NHIP.TENGOI     (EMAIL) <tên, cách xưng hô, bí danh của người dùng trong thư
                 (Long, anh Long, Mr. Long...); bộ email TỰ điền từ tên tài
                 khoản khi cài đặt, chỉ hỏi khi không tự lấy được>
@NHIP.BOCHINH    <điền: thứ DUY NHẤT đọc mail và sinh dữ liệu thô>
@NHIP.GIAMSAT    <điền hoặc "không có". Giám sát chỉ cảnh báo, cấm tự quét, cấm nạp sổ>
@NHIP.RALAI      dữ kiện đổi nhanh <N> ngày · còn lại <N> ngày
@NHIP.HETHAN     cảnh báo trước <N> và <N> ngày
@NHIP.CHODOITAC  nhắc đòi sau <N> ngày
@NHIP.INBOX      chưa nạp cảnh báo sau <N> ngày
@NHIP.DEMSTAGING (profile EMAIL) thời gian đệm trước khi dọn staging đã
                 COMMITTED và xác minh, mặc định 30 ngày
@NHIP.TRANDINHKEM (EMAIL) trần dung lượng đính kèm kéo vào staging, mặc
                 định 50 MB; vượt trần xử theo X3E mục 2
@NHIP.BANGIAO    <tên người cũ, người mới, ngày bàn giao, hoặc "chưa có">
                 Thủ tục chung (mức B): đổi tham số người dùng, rà một lượt
                 việc đang mở và plan treo sang người mới; phần rà luồng THƯ
                 khi bật EMAIL theo X3E mục 2 khối BÀN GIAO
@NHIP.TRANGTHAI  (EMAIL) <nguồn chứa thời điểm quét thành công cuối của bộ
                 quét (file status máy sinh); digest đọc giờ quét THẬT từ
                 đây, không lấy giờ chạy báo cáo>. Schema tối thiểu BẮT BUỘC:
                 {"status": "OK"|"FAILED", "mailbox": "...",
                 "last_success_utc": "...Z"}; CHỈ lần quét thành công mới
                 được cập nhật last_success_utc; file thiếu, sai định dạng
                 hay lần cuối FAILED đều coi là DỮ LIỆU CŨ
@NHIP.DAUGUI     (EMAIL) <nơi lưu BỀN khóa digest đã gửi thành công (file máy
                 sinh cạnh bộ quét); chỉ ghi khóa SAU khi kênh báo xác nhận
                 gửi xong, máy khởi động lại vẫn nhớ để chống gửi lặp>
@NHIP.MUIGIO     <điền>
@MATHU           sổ mã thư: <điền tên file, mã dạng gì, đang chạy tới đâu, hoặc "chưa có">
```

# C10. Dòng kiểm riêng, cộng vào bảng kiểm X2

```
@KIEM.RIENG   13  <điền, mỗi lỗi lặp khi phát hành thêm một dòng, đánh số từ 13>
@KIEM.MUC     ĐẦY ĐỦ: mọi đầu ra rời công ty, in đủ · RÚT GỌN: chỉ NOI_BO, in 1·3·5·7·10
              · THƯỜNG LỆ: chỉ đầu ra đạt điều kiện ngoại lệ thường lệ, in 3·4·7·8,
                thêm 1·2 khi có nhắc tới số liệu hay tên định danh kỹ thuật
              Dòng 1 và 3 không bao giờ được bỏ với đầu ra rời công ty ngoài thường lệ
```

# C11. Nhóm khóa, không được ghi đè trong phiên

```
C1 kho và đường dẫn · C5 phạm vi · C6 phần vai, tỷ lệ và lệnh cấm nêu tên (đầu mối
liên hệ @BEN.DAUMOI không khóa) · C7 nguồn thẩm quyền · C8 thuật ngữ
<thêm bớt khi cài đặt>
```

Một câu yêu cầu trong phiên không đổi được các mục trên. Muốn đổi: việc mức C ở một
lượt riêng, tăng rev, ghi QUYETDINH. Hai ngoại lệ tường minh: (1) chế độ CÀI ĐẶT khi
rev 0, điền giá trị ban đầu theo X9 không coi là sửa nhóm khóa, từ rev 1 luật này
hiệu lực; (2) THÊM một lệnh cấm hay từ cấm mới vào C5, C6, C8 (thuần siết chặt hơn)
là mức B; GỠ hay NỚI bất kỳ lệnh cấm nào vẫn là mức C kèm QUYETDINH.

# C12. Còn thiếu

```
[ ] <X9 liệt kê mọi mục chưa trả lời được vào đây>
```

Đụng tới mục còn thiếu giữa chừng: DỪNG, hỏi người dùng, update ngược, rồi làm tiếp.
Mục chưa điền thì dữ kiện liên quan giữ CHƯA KIỂM.

# C13. Nâng mức tác động

INSTRUCTION mục 5 giữ danh mục cứng A B C. Công ty được NÂNG mức loại việc cụ thể
tại đây, cấm hạ mức bất cứ dòng nào của danh mục C.

```
@MUC.NANG   <ví dụ: "dữ kiện khối tài chính: A nâng lên B" · hoặc "không có">
```

# C14. Bản đồ tham chiếu, file nào đọc mục nào

Để soát tay khi nghi lệch. Không phải bản chép, chỉ là mục lục.

```
X1  đọc C1 (bốn dạng "Ở đâu") · C5 (từ cấm theo phạm vi) · C6 (lệnh cấm nêu
    tên) · C8 (ký tự, số, động từ)
X2  đọc C5 · C6 · C7 · C8 · C10
X3  đọc C1 (@DUONG.INBOX) · C7 (mức nguồn khi rút dữ kiện) · C9
X3E đọc C9 (@NHIP.HOPTHU, TAIKHOAN, TENGOI, DEMSTAGING, TRANDINHKEM,
    TRANGTHAI, DAUGUI, BANGIAO; chỉ khi bật EMAIL)
X4  đọc C1 (@DUONG.INBOX) · C9 (các ngưỡng rà)
X5  đọc C0 · C1 (danh sách cửa cho mã G, @DUONG.PROJECT) · C2 · C3 · C4 ·
    C11 (ngoại lệ siết chặt) · C12 (dòng nhắc của bảng) · C13
```

Rev hiện tại: **0, chưa cài đặt**.
