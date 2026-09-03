```
X0 · CẤU HÌNH · <MÃ> · v13 · rev 0 · <YYYYMMDD>
instruction_yeu_cau: v11
TEMPLATE. rev 0 nghĩa là chưa cài đặt. Phiên đầu chạy X9 để điền, xong đặt rev: 1.
Mọi tham số của công ty nằm ở đây, không ở đâu khác. X1 tới X5 là luật và TRỎ về các
mục của file này; cần giá trị thì đọc tại đây ngay lúc dùng, không chép đi đâu.
Ô CHƯA ĐIỀN của X0 viết bằng ĐÚNG MỘT khuôn `<điền: ...>` hay `<chưa điền>` hay
`<N>`; chỗ nào khác trong X0 dùng dấu ngoặc nhọn thì KHÔNG được mang ba khuôn đó
(rà 0i đọc theo khuôn này để biết mục nào còn trống).
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
@CTY.MA          <điền, 3-4 ký tự A-Z hay số, KHÔNG dấu tiếng Việt>
@CTY.TEN         <điền>
@CTY.VAITRO      <điền, công ty đóng vai gì trong công việc chính>

@KHO.CHINH       <điền: kho đặt ở đâu, ví dụ thư mục Dropbox / ổ máy đơn>
                 CUA1 = <điền: đường dẫn gốc trên máy 1> · thiết bị <điền: tên>
                 <thêm cửa thứ hai, thứ ba... nếu kho mây có nhiều máy cùng vào>
                 Kho Ổ MÁY ĐƠN: backup cùng ổ, phải sao lưu ra thiết bị khác
@KHO.LUAT_CUA    <điền ràng buộc riêng từng cửa nếu có: giới hạn dung lượng ghi,
                 không xóa được, tải theo yêu cầu phải quét hai lượt... hoặc "không có">
@KHO.SAOLUU      <điền: thư mục NGOÀI gốc kho (ổ khác, máy khác, hay tài
                 khoản mây khác) và nhịp sao; hoặc "chưa có". Bản backup
                 hằng ngày của X5 mục 7 nằm TRONG _so nên một lượt
                 rollback đám mây trọn _so xóa sạch cả chúng cùng lúc -
                 đây là bản duy nhất sống sót cảnh đó>
@KHO.CUA_NGUNG   <điền: cửa đã thu hồi - CUAn · thiết bị · ngày · căn cứ
                 Q-<mã>; hoặc "chưa có". Mã G cũ của cửa đó nằm trong
                 NHATKY chỉ-thêm nên KHÔNG xóa được: gỡ hẳn dòng cửa
                 khỏi trên mà không khai xuống đây thì rà 7b tố "cửa ma"
                 vĩnh viễn. Thu hồi cửa là mức C, kèm QUYETDINH>
@KHO.CU          <điền: kho đã ngừng, chỉ tra lịch sử, hoặc "không có">
@DUONG.SO        <điền: gốc kho>\00_Index\_so\
@DUONG.INBOX     <điền: gốc kho>\00_Index\_so\_inbox\ · mục đã nạp chuyển
                 vào _da_nap\ con của chính folder này
@DUONG.LUAT      <điền: gốc kho>\00_Index\
@DUONG.PROJECT   Claude Project "<điền: tên>", thư viện đọc, không phải sổ
@DUONG.DRIVE     <chưa điền, chỉ khai khi dùng tầng chia sẻ mây riêng>
```

Cột "Ở đâu" của sổ TAILIEU chỉ nhận: "Kho <đường dẫn tương đối từ gốc kho>" ·
"KhoCu <đường dẫn tương đối từ @KHO.CU>" (chỉ khi @KHO.CU khác "không có"; kho
cũ chỉ tra lịch sử nên máy không kiểm tồn tại hay sha) ·
"Project <đường dẫn doc>" · "Drive <ID folder>" · "Repo <mã PM> <đường dẫn
trong repo>@<commit hay tag>" (chỉ cho dòng thuộc dự án @DUAN.PHANMEM, ô
sha256 bỏ trống vì repo tự giữ lịch sử). Ngoài năm dạng đó là cấm.
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
           (dev, staging, prod) · nơi chạy thật · nơi giữ secret
           (vault, secret manager, hay "chưa rõ") · nhánh tự deploy chạy thật
           (nhánh merge vào là ra production, hay "không có auto-deploy")
           · CSDL chạy thật (tên ĐÍCH DANH máy neo mức C, hay "CSDL chưa rõ")
           · phụ trách vận hành <tên - người GẬT lượt mức C, hay "chưa rõ">
  Repo là NGUỒN SỰ THẬT của code: code KHÔNG chép vào kho, KHÔNG qua
  _INBOX; kho chỉ giữ hồ sơ, quyết định, tài liệu phát hành. Chạm code vẫn
  ghi VIEC, QUYETDINH, cột Liên kết trỏ commit hay PR. Một phần mềm nhiều
  repo: mỗi repo một vế cùng dòng. Đặc tả sống cùng code trong repo,
  TAILIEU trỏ dạng "Repo" (C1). Mức từng thao tác repo, SECRET, dữ liệu
  khách trong dump và log, bàn giao source thuê ngoài: X5 mục 1b (chỉ nạp
  khi có dự án phần mềm).
  Ví dụ dòng đã điền: APP  Ứng dụng đặt hàng · repo github.com/cty/app
  · web + máy chủ · dev máy đội, chạy thật app.cty.vn · secret ở
  GitHub Actions · nhánh tự deploy main. Mục nào chưa rõ: trả lời
  "chưa rõ, hỏi đội kỹ thuật", AI ghi dấu chưa điền vào C12.
  Nhánh tự deploy là dữ kiện X5 mục 1b CẦN để xử lượt merge: merge vào đúng
  nhánh đó là chạm CHẠY THẬT nên mức C, dù câu ghi không nhắc chữ nào về
  production. Không có auto-deploy thì khai "không có auto-deploy"
```

Đóng dự án: đổi sang NGỪNG (mức B), việc đang mở chuyển HỦY hay bàn giao
dự án khác; sổ giữ nguyên để tra lịch sử, bàn làm việc và digest lọc bỏ.
Còn nghĩa vụ sau thanh lý (bảo hành, bảo lãnh): khai
"NGỪNG (bảo hành tới YYYY-MM-DD)" và GIỮ các việc đó mở - rà thôi tố tới
ngày ấy, sau ngày ấy tố lại.
Dự án mới: thêm dòng ở đây (mức B), dựng folder con trong các folder chức năng cần
dùng, rồi mới mở việc đầu tiên.

# C3. Folder và khối

```
@FOLDER.CHUCNANG   cây mặc định, X9 dựng sẵn, thêm bớt khi công ty đã có cây riêng
  00_Index   01_Phap_ly   02_Ky_thuat   03_Thuong_mai   04_Trao_doi   05_Mau
  06_Ke_toan_Nhan_su   07_Hanh_chinh   98_Tai_nguyen   99_Goc   99_Luu_tru

@FOLDER.KHOI       khối việc sinh KHI CÓ VIỆC ĐẦU TIÊN của khối, không bắt khai trước
  <MÃ KHỐI>  <mô tả>  <folder thật>  <dự án>

@FOLDER.CON        dùng khi cần (mức A), tên KHÔNG bắt đầu bằng _: 01_Phap_ly 02_Ky_thuat 03_Thuong_mai
                   04_Trao_doi 05_Mau 06_Ke_toan_Nhan_su 07_Hanh_chinh 99_Goc
                   bản nộp: 01_Phap_ly\_NOP_YYYYMMDD\ rồi khóa
```

# C4. Tên file

```
@TEN.MAY       (cú pháp) <KHOI>_<YYYYMMDD>_<LOAI>_<DoiTac>_<MoTa>_v<NN>.ext
@TEN.PROJECT   Ten_vNN_YYYYMMDD.md
@TEN.NHAP      (cú pháp) bản trung gian chưa chốt: v<NN>-nhap<M>, không vào TAILIEU
@TEN.LOAI      CV TT PA BG DT HD PL MOU BB BC SL GP MAU MAIL HDON BL BBBG, thêm bớt: A
```

Không dấu, không khoảng trắng. Cấm final, copy, moi_nhat, ban_cuoi
và khuôn " (n)", "(bản sao)"; tên hậu tố "-<chữ/số>" cạnh file cùng tiền
tố cũng bị máy NGHI bản sao (khuôn OneDrive, hậu tố từ ~5 ký tự).
Nội bộ: DoiTac là NA. Bản ký thêm `_SIGNED`, bất biến. Trạng thái ở TAILIEU, không vào tên file.
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
  tiết, TRỪ người nhận chưa thuộc phạm vi nào: dùng RA_NGOAI với điều kiện
  mọi dữ kiện trong đầu ra TỰ KHAI RA_NGOAI (chữ RA_NGOAI phải NẰM trong
  danh sách phạm vi của CHÍNH dữ kiện; luật bao trùm "tự thỏa" không dùng
  cho lối này), và mở việc mức B đề xuất khai phạm vi mới; từ cấm áp cho
  RA_NGOAI là HỢP của mọi dòng @PHAMVI.CAM cộng X1

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

@VANHANH.NGUOI  <điền: tên người vận hành hiện tại, chức danh, cửa hay dùng>
                KHÔNG thuộc nhóm khóa: đổi là mức B; @NHIP.BANGIAO đổi nó
                khi bàn giao.
```

Mặc định MỘT người vận hành chốt mức C; nhiều người thì tự quy ước ai chốt
- hệ ghi vết theo cửa, không phân quyền. Vai đổi khi có văn bản ký mới: dòng
TAILIEU ĐÃ KÝ (có sha256) với bên đó là ĐỦ, AI cập nhật vai ở C6 mức B
cùng lượt, không cần QUYETDINH. Cách gọi trong hội thoại không đổi vai.
Gỡ lệnh cấm: không xóa dòng, gạch và ghi "gỡ ngày, căn cứ mã".

# C7. Nguồn thẩm quyền và mức nguồn (CORE: thang A-D và mức tối thiểu áp MỌI
profile; riêng nguồn chỉ định và phạm vi chi tiết: profile REGULATED)

```
@NGUON.LOAI      <điền: loại dữ kiện> lấy từ <điền: tài liệu, bản, ngày>
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
  văn bản nội bộ (bảng giá, chính sách) người vận hành xác nhận trong
  phiên: B, không cần QUYETDINH
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
mức nguồn thấp hơn tối thiểu, đầu ra ghi kèm "theo tên nguồn, bản và ngày". Mức
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
@HINHTHUC.KYTUCAM    em-dash · en-dash · dấu xấp xỉ · mũi tên (mặc định)
@HINHTHUC.SO         giữ số như nguồn, không tự làm tròn
@HINHTHUC.VANPHONG   không có
@HINHTHUC.FONT       không có
@HINHTHUC.QUANHE     dùng sự kiện kèm ngày · động từ cấm: không có
```

# C9. Nhịp và bộ thực thi (các ngưỡng @NHIP.RALAI, HETHAN, CHODOITAC, INBOX,
MUIGIO và @MATHU là CORE, mọi profile đọc khi X3, X4 trỏ tới; dòng gắn nhãn
AUTOMATED, EMAIL chỉ đọc khi bật profile đó)

```
@NHIP.BANMOI     <điền: nơi phát hành bộ (URL repo hay thư mục) và chu kỳ
                 kiểm, mặc định mỗi quý>. Kho chạy KHÔNG có .git (X9 mục 1)
                 nên không tự biết có bản mới; người giữ nhịp mở nơi phát
                 hành, so số VÒNG VÁ ở DÒNG ĐẦU file DOC_TRUOC.md của nơi
                 phát hành với @NHIP.BANMOI.DAKIEM dưới đây,
                 mới hơn thì nâng cấp theo X9 mục 3c
@NHIP.BANMOI.DAKIEM  <điền: YYYYMMDD lần kiểm cuối và số vòng vá của bản
                 đang chạy; cập nhật ngay sau mỗi lượt kiểm, mức A>
@NHIP.QUETMAIL   <điền nhịp, ngưỡng nhắc>
                 Quét tự động chỉ có cho EMAIL; chat (Zalo...) đi lối bán
                 thủ công X3 mục 5b: dán cả đoạn, AI tách tin, nguồn D
@NHIP.HOPTHU     (EMAIL) <điền HỘP THƯ NGHIỆP VỤ của CHÍNH công ty này. Một công ty một
                 hộp thư quét; bộ quét CHỈ đọc hộp này, hộp thư của công ty khác
                 trên cùng máy tuyệt đối không vào pipeline>
@NHIP.HOPTHU_CU  (EMAIL) <điền: các hộp thư CŨ sau khi đổi domain hay đổi hộp,
                 hoặc "chưa có"; đổi @NHIP.HOPTHU là mức C kèm QUYETDINH,
                 hộp cũ chuyển xuống đây để nhật ký lịch sử không bị đá oan>
@NHIP.TAIKHOAN   (EMAIL) <điền các địa chỉ NGƯỜI DÙNG dùng để gửi, CỘNG các
                 alias hay hộp nhóm mà thư nhắm tới người dùng vẫn đến (info@,
                 sales@...); dùng nhận diện "thư của mình", "mình ở To" X3E>
@NHIP.TENGOI     (EMAIL) <điền: tên, cách xưng hô, bí danh của người dùng trong thư
                 (Long, anh Long, Mr. Long...); bộ email TỰ điền từ tên tài
                 khoản khi cài đặt, chỉ hỏi khi không tự lấy được>
@NHIP.BOCHINH    (EMAIL) <điền: thứ DUY NHẤT đọc mail và sinh dữ liệu thô>
@NHIP.GIAMSAT    <điền hoặc "không có". Giám sát chỉ cảnh báo, cấm tự quét, cấm nạp sổ>
@NHIP.RALAI      dữ kiện đổi nhanh 30 ngày · còn lại 180 ngày
@NHIP.HETHAN     cảnh báo trước 30 và 7 ngày
@NHIP.CHODOITAC  nhắc đòi sau 5 ngày
@NHIP.INBOX      chưa nạp cảnh báo sau 3 ngày
@NHIP.DEMSTAGING (profile EMAIL) thời gian đệm trước khi dọn staging đã
                 COMMITTED và xác minh, mặc định 30 ngày
@NHIP.TRANDINHKEM (EMAIL) trần dung lượng đính kèm kéo vào staging, mặc
                 định 50 MB; vượt trần xử theo X3E mục 2
@NHIP.BANGIAO    <điền: tên người cũ, người mới, ngày bàn giao, hoặc "chưa có">
                 Thủ tục chung (mức B): đổi @VANHANH.NGUOI ở C6, rà một lượt
                 việc đang mở và plan treo sang người mới; phần rà luồng THƯ
                 khi bật EMAIL theo X3E mục 2 khối BÀN GIAO
@NHIP.TRANGTHAI  (EMAIL) <điền: nguồn chứa thời điểm quét thành công cuối của bộ
                 quét (file status máy sinh); digest đọc giờ quét THẬT từ
                 đây, không lấy giờ chạy báo cáo>. Schema tối thiểu BẮT BUỘC:
                 {"status": "OK"|"FAILED", "mailbox": "...",
                 "last_success_utc": "...Z"}; CHỈ lần quét thành công mới
                 được cập nhật last_success_utc; file thiếu, sai định dạng
                 hay lần cuối FAILED đều coi là DỮ LIỆU CŨ
@NHIP.DAUGUI     (EMAIL) <điền: nơi lưu BỀN khóa digest đã gửi thành công (file máy
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
lượt riêng, tăng rev, ghi QUYETDINH. BA ngoại lệ tường minh: (1) chế độ CÀI ĐẶT khi
rev 0, điền giá trị ban đầu theo X9 không coi là sửa nhóm khóa, từ rev 1 luật này
hiệu lực; (2) ĐIỀN LẦN ĐẦU một mục CHƯA TỪNG mang giá trị công ty - còn bất kỳ dấu
chưa điền nào của template (`<chưa điền>`, `<điền...>`, `<N>`, hay ô để trống), dù
đã có dòng ở C12 hay chưa - theo X9 mục 2 và mục 4: mức B, tăng rev, ĐÁNH DẤU dòng
ở C12 thành `[x] <mục> - điền lần đầu rev <N> ngày <YYYYMMDD>` (KHÔNG xóa dòng: dấu
này là bằng chứng duy nhất phân biệt điền-lần-đầu với đổi-giá-trị; dòng đã đánh dấu
`[x]` KHÔNG còn là mục trống với rà 0i, mục chỉ quay lại C12 khi giá trị bị gỡ và
việc gỡ đó là mức C kèm QUYETDINH), KHÔNG plan C
không QUYETDINH - đó là phần cài đặt hoãn lại chứ không phải đổi giá trị đang có
hiệu lực; ĐỔI một giá trị ĐÃ điền vẫn là mức C kèm QUYETDINH; (3) THÊM một lệnh cấm
hay từ cấm mới vào C5, C6, C8 (thuần siết chặt hơn) là mức B; GỠ hay NỚI bất kỳ lệnh
cấm nào vẫn là mức C kèm QUYETDINH.

CHỐT CHỐNG LÁCH: đưa một mục ĐÃ điền trở lại C12, hay ghi dấu chưa điền đè lên giá
trị đang có hiệu lực, CHÍNH LÀ đổi giá trị đã điền - mức C kèm QUYETDINH, và không
mở lại được ngoại lệ (2). Bản thân hai danh sách C11 và C12 cũng thuộc nhóm khóa:
THÊM mục vào C11 (siết chặt) là mức B; BỚT mục khỏi C11, hay thêm dòng C12 cho một
mục đã điền, là mức C kèm QUYETDINH. Dòng `<thêm bớt khi cài đặt>` chỉ có hiệu lực
ở rev 0. Người dùng vừa trả lời chính câu hỏi đó trong cùng lượt thì lời trả lời LÀ
câu đồng ý của mức B: ghi thẳng, gộp mọi mục điền cùng lượt vào MỘT dòng báo.
Ngoại lệ lời-trả-lời-miệng này KHÔNG áp cho C6 phần VAI và TỶ LỆ: theo X9 mục 4,
vai các bên vẫn cần văn bản ký, chưa có thì ghi CHƯA KIỂM dù mức duyệt đã là B.

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
@MUC.NANG   <điền: ví dụ "dữ kiện khối tài chính: A nâng lên B", hoặc "không có">
```

# C14. Bản đồ tham chiếu, file nào đọc mục nào

Để soát tay khi nghi lệch. Không phải bản chép, chỉ là mục lục.

```
X1  đọc C1 (năm dạng "Ở đâu") · C5 (từ cấm theo phạm vi) · C6 (lệnh cấm nêu
    tên) · C8 (ký tự, số, động từ)
X2  đọc C5 · C6 · C7 · C8 · C10
X3  đọc C1 (@DUONG.INBOX) · C7 (mức nguồn khi rút dữ kiện) · C9
X3E đọc C9 (@NHIP.HOPTHU, TAIKHOAN, TENGOI, DEMSTAGING, TRANDINHKEM,
    TRANGTHAI, DAUGUI, BANGIAO, HOPTHU_CU; chỉ khi bật EMAIL)
X4  đọc C1 (@DUONG.INBOX) · C9 (các ngưỡng rà, @NHIP.HOPTHU, HOPTHU_CU)
X5  đọc C0 · C1 (danh sách cửa cho mã G, @DUONG.PROJECT) · C2 · C3 · C4 ·
    C5 (phạm vi dump, log ở mục 1b) · C11 (ngoại lệ siết chặt) · C12 (dòng
    nhắc của bảng) · C13
```

Rev hiện tại: **0, chưa cài đặt**.
