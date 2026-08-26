```
X3 · CỬA VÀO · <MÃ> · v15 · <YYYYMMDD>
Đọc khi CUA_VAO: mail, file đến, người dùng đưa trực tiếp. Nhịp và bộ thực thi đọc
từ X0 C9. Nạp mục có nguồn rõ vào sổ là mức A; dữ kiện có phạm vi ra ngoài là mức B.
Mục 5b CHỈ đọc khi dán chat hay export.
```

# 1. Bốn cửa, không cửa nào bỏ qua sổ

Mail · folder chia sẻ bên ngoài · người dùng đưa trực tiếp · phát sinh trong phiên.

HÀNH ĐỘNG NGƯỜI DÙNG ĐÃ LÀM là SỰ KIỆN ĐẦU VÀO, không phải việc chờ AI cho
phép: người dùng đã sửa, gửi, nhận hay di chuyển file thì AI kiểm chứng (đọc
file, mail, mtime) và GHI NHẬN mức A, không xin phép hồi tố, không coi là vi
phạm vòng đời. Thiếu thông tin nhưng chưa ảnh hưởng bước tiếp theo: ghi "CHƯA
XÁC NHẬN" vào ô căn cứ, KHÔNG hỏi. Chỉ hỏi khi không xác định được file nào,
gửi cho ai, hoặc trạng thái đó đổi hành động sắp làm.

# 2. Bộ thực thi

Một công việc chỉ có MỘT bộ thực thi, khai ở X0 C9. Giám sát chỉ cảnh báo, cấm tự
quét, cấm sinh dữ liệu thứ hai, cấm nạp sổ. Nhịp giữ bằng bộ đếm trong
BANG_DIEU_KHIEN, không bằng trí nhớ. Phát hiện hai bộ cùng đọc một nguồn: ghi VIEC
để bỏ một, không tự chọn.

# 3. Hai chặng

```
CHẶNG 1  đọc, phân loại, rút dữ kiện, lập danh sách file cần tải, ghi _INBOX
         (tọa độ ở X0 C1 @DUONG.INBOX)
CHẶNG 2  chỉ phiên chạm được kho: tải về đúng folder, đổi tên chuẩn, ghi sổ,
         chuyển _da_nap
```

Chặng 1, mỗi mail hoặc file: gắn mã thư theo X0 C9 mục @MATHU, luồng mới cấp mã kế
tiếp · xác định dự án và khối · soi việc trong VIEC, chưa có thì đề xuất mở · rút dữ
kiện kèm mức nguồn theo X0 C7, nguồn bằng mã thư · quyết đích từng file đính kèm, tên
đã chuẩn hóa · nói rõ người dùng cần làm gì.

Mỗi mục `_INBOX` là MỘT FILE riêng:

```yaml
event_id:   <YYYYMMDD-HHMM>-<mã ngắn>     # KHÓA DUY NHẤT chống nạp trùng
source_id:  <mã thư, hoặc "phien-chat">   # chỉ để liên kết nguồn, KHÔNG làm khóa
loai:       VIEC | DUKIEN | TAILIEU | QUYETDINH | QUET_MAIL
du_an:      <mã>   khoi: <mã>
noi_dung:   <dán nguyên dòng sẽ thêm vào sổ>
can_tai:    [{tu, den, co: GOC}]
```

Ghi `_INBOX` hỏng: in nguyên khối cho người dùng dán tay, báo "chưa ghi được", cấm
im lặng.

Chặng 2: trùng `event_id` thì bỏ qua · đổi tên chuẩn ngay lúc tải, tên gốc vào ô "Căn
cứ trạng thái" của dòng TAILIEU · file gốc ngoài: bất biến, cờ GỐC, tính sha256 và byte ngay lúc nhận ·
mail là căn cứ dữ kiện thì lưu .eml hoặc .pdf vào `04_Trao_doi\` TRƯỚC rồi DUKIEN mới
trỏ tới · số đổi thì DUKIEN dòng cũ ghi thay bởi · chuyển `_INBOX` sang `_da_nap\` ·
cập nhật bộ đếm. Tải hụt: KHÔNG chuyển `_da_nap`, ghi VIEC kèm lý do.

# 4. Xếp chỗ

```
gửi để xem hoặc trả lời      04_Trao_doi\        bản gốc pháp lý, kỹ thuật   99_Goc\ + cờ
bản sẽ nộp                   01_Phap_ly\         bản vẽ, số liệu             02_Ky_thuat\
báo giá, hợp đồng            03_Thuong_mai\      mẫu dùng lại                05_Mau\
```

Một file một bản ở nơi đúng nhất, nơi khác chỉ tham chiếu. Folder ngoài sở hữu: chép
bản sao về kho ngay. Nói miệng: DUKIEN mức nguồn D, CHƯA KIỂM tới khi có văn bản.

# 5. Bảng chờ duyệt

`| Mail/File | Mã thư | Dự án | Khối | Việc | Trạng thái mới | Tải về đâu | Cần làm gì |`

Mục đã đủ nguồn và thuần nội bộ: nạp luôn theo mức A, báo một dòng. Mục là dữ kiện
phạm vi ra ngoài, hoặc mở việc lớn: đưa vào bảng, duyệt rồi mới ghi. Chưa duyệt mà
hết phiên: ghi VIEC hạn phiên sau, cấm chết theo phiên.

# 5b. Chat dán tay (CHỈ đọc khi người dùng dán chat hay export)

Kênh chat chưa có pipeline quét; xử BÁN THỦ CÔNG qua cửa "người dùng đưa
trực tiếp": người dùng dán CẢ ĐOẠN chat (hay export) vào phiên, AI tách
từng tin theo khuôn "giờ - tên người gửi", xử mỗi tin như một mục đến ở
chặng 1: rút việc, dữ kiện (nguồn D "tin nhắn chưa xác nhận", nâng lên B
khi có xác nhận văn bản), đề xuất qua bảng chờ duyệt mục 5, ô Mã thư ghi
"phien-chat". event_id tin chat: <YYYYMMDD-HHMM>-chat-<NN> (NN là số thứ
tự tin trong khối dán; ngày theo header ngày GẦN NHẤT phía trên tin trong
đoạn dán, thiếu mới rơi về ngày phiên); công ty theo dõi TỪ HAI kênh chat
trở lên: mỗi kênh MỘT dòng VIEC riêng, event_id thêm mã kênh
-chat-<kênh>-<NN>. CHỐNG DÁN LẶP: cuối lượt ghi mốc "đã nạp tới tin
<ngày> <giờ> <người gửi>" vào ô "Bước tiếp theo" của dòng VIEC theo dõi
chat (chưa có thì mở, mức A); SAU mốc nghĩa là sau VỊ TRÍ tin mốc trong
khối dán; khối không chứa tin mốc: so theo ngày rồi giờ, tin CÙNG phút
mốc coi như ĐÃ NẠP, nghi sót thì dán lại cả khối chứa tin mốc; chặng 2
gặp trùng event_id tin chat thì SO NỘI DUNG trước khi bỏ qua, khác nội
dung là tin mới: cấp NN kế tiếp. Không tách được khuôn giờ-tên: cả khối
là MỘT mục nguồn D. Ảnh chụp chat xử như nguồn scan theo X0 C7 (cờ CHƯA
ĐỌC ĐƯỢC khi không rút được chữ). KHÔNG cấp mã luồng THU (THU chỉ cho
EMAIL); theo dõi chờ phản hồi chat: dòng VIEC "CHỜ ĐỐI TÁC".

# 6. Mail là kênh nghiệp vụ chính (profile EMAIL)

Không bật EMAIL: bỏ qua, mail đi qua bốn cửa như file thường. Bật EMAIL: đọc
X3E_EMAIL_<MÃ>.md, luật đầy đủ của pipeline mail nằm trọn ở đó; khi đó mail
KHÔNG đi qua _INBOX và event_id (chống trùng bằng khóa và registry của X3E),
X3 chỉ còn áp mục 4 xếp chỗ và mục 5 bảng chờ duyệt cho mail.
