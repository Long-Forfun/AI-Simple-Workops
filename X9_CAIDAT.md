```
X9 · CÀI ĐẶT TỪ ZERO · v09
Chạy đúng một lần cho mỗi công ty mới, ở PHIÊN ĐẦU TIÊN. Không chứa dữ liệu công ty nào.
Nguyên tắc: vào việc được sau BA câu bắt buộc cộng MỘT câu chọn profile.
Phần còn lại điền dần đúng lúc cần.
```

# 0. Bộ khởi tạo gồm gì

```
INSTRUCTION_WORKOPS      dán vào Project instructions, dùng nguyên văn, không sửa
X0_CAUHINH_TEMPLATE      phiên đầu AI đổi tên thành X0_CAUHINH_<MÃ> rồi điền
X1..X5, X3E TEMPLATE     luật, trỏ về X0, không phải điền; AI đổi tên theo mã
                         cùng lượt (X3E chỉ được nạp khi bật EMAIL)
X9 file này              đọc ở phiên đầu, xong thì thôi
_so\                     NĂM sổ lõi rỗng + PLANNING (mức C) + THU (chỉ khi
                         bật EMAIL) + hai view máy sinh, copy nguyên
```

Người dùng làm trước: đưa bộ về `<gốc>\00_Index\` (clone hay giải nén nguyên
trạng, không đổi tên gì) · dán INSTRUCTION vào Project instructions · mở phiên
Cowork đầu. Mọi việc còn lại là của AI.

# 1. Phiên đầu tiên: ba câu bắt buộc, một câu profile

AI nhận diện X0 còn `rev 0` thì tự chuyển sang chế độ CÀI ĐẶT: điền giá trị ban
đầu không tính là sửa nhóm khóa, không plan, không QUYETDINH (ngoại lệ 1 của X0
C11, hết hiệu lực từ rev 1). Hỏi BA câu bắt buộc:

```
1  Mã công ty (3-4 ký tự A-Z hay số, không dấu) và tên đầy đủ? Công ty đóng vai gì trong công
   việc chính?
2  Kho đặt ở đâu? (đường dẫn gốc, AI thử đọc để kiểm. Ai nữa dùng kho - trợ
   lý? Mỗi người một cửa CUA2, CUA3 ở X0 C1, LITE vẫn được)
3  Dự án đầu tiên tên gì, mã gì? (dự án CTY cho việc chung tự thêm sẵn; dự án
   là PHẦN MỀM thì hỏi đủ TÁM trường phạm vi tổ chức theo X0 C2
   @DUAN.PHANMEM: repo · thành phần · môi trường · nơi chạy thật · nơi giữ
   secret · nhánh tự deploy · CSDL chạy thật · người phụ trách vận hành -
   hỏi thiếu là 7d đỏ ngay sau khi người dùng trả lời đúng câu hỏi)
```

Câu 4, chọn profile (X0 C0), người dùng không rõ thì mặc định LITE:

```
4  Công ty có cần: phát hành chính thức hay hồ sơ nhà nước (REGULATED)? kho
   nhiều máy cùng ghi (PARALLEL)? tác vụ tự động không người (AUTOMATED)? mail
   là kênh nghiệp vụ chính (EMAIL, dùng sổ THU)? Không cái nào thì LITE. Bật
   thêm sau được, là việc mức B
```

Xong bốn câu: đổi tên các file _TEMPLATE theo mã công ty, dựng _so\_inbox\
và _da_nap\ con của nó (X0 C1 @DUONG.INBOX), điền X0 C0 C1 C2, đặt
rev 1, dựng cây folder mặc định theo X0 C3, sinh X0_INDEX và BANG_DIEU_KHIEN đầu tiên in "bàn sạch".
Kho vừa clone bằng git: XÓA `00_Index\.git` (Windows: object của git là file
CHỈ ĐỌC nên `rmtree` hỏng giữa chừng và để lại `.git` cụt; dùng `rmdir /s /q`,
rà 0g là lưới cuối nếu sót). `.git` ở THƯ MỤC CHA thì KHÔNG xóa (repo
cha có thể là dự án khác): CHUYỂN kho ra ngoài vùng git - `_so\` là sổ
SỐNG (mục 3c). Xóa luôn GHICHU_*, WORKOPS_*_GOP.md, BENCHMARK_TOKEN.md
khỏi kho: tài liệu của bộ mẫu, không dùng vận hành. Có tài liệu Project
(README bước 3)? Thay TEMPLATE bằng bản ĐÃ ĐIỀN sau cài và mỗi lần rev
tăng - để bản cũ là CHAT chạy luật STALE. Quét X0 một lượt, đưa MỌI
mục còn dấu chưa điền vào C12 thành danh sách thật, kể cả nhóm C chưa hỏi
(tham số của profile CHƯA bật thì KHÔNG vào C12; bật profile sau, mức B, thì
cùng lượt đó thêm chúng vào C12): C12
trống sau khi cài là SAI (rà 0i bắt).
TỪ ĐÂY LÀM VIỆC ĐƯỢC.

Khối việc không hỏi trước: sinh khi có việc đầu tiên, thêm dòng @FOLDER.KHOI (mức A; mở folder chức năng mới là B).

# 2. Nhóm hỏi tiếp theo, đúng lúc cần

**Nhóm B, bắt buộc TRƯỚC khi soạn TÀI LIỆU CHÍNH THỨC đầu tiên gửi ra ngoài
(có số liệu, cam kết, điều khoản, hay là văn bản chính thức). Đụng loại đó mà
nhóm này trống thì dừng, hỏi, rồi mới soạn (riêng thông báo SỰ CỐ đang diễn
ra theo NGOẠI LỆ SỰ CỐ của X2: gửi được ngay cả khi nhóm B còn trống). NGOẠI LỆ THƯỜNG LỆ: mail, tin công
việc không cam kết không số liệu chạy được NGAY với mặc định ngầm hiểu, không
hỏi: ngôn ngữ theo luồng thư hay người nhận · giọng chuyên nghiệp, ngắn gọn ·
từ cấm theo danh mục mặc định X1 · người nhận và phạm vi lấy từ chính thư đó.
CHỈ hỏi khi có hai lựa chọn khác nhau đáng kể (thư đầu tiên cho đối tác mới
chưa rõ dùng tiếng gì). Xuất hiện số liệu hay cam kết là hết thường lệ, dừng
và hỏi đủ nhóm B:**

```
5  Đầu ra chia mấy phạm vi? Phạm vi nào cấm nhắc từ nào? Phạm vi nào bắt buộc
   khai gì?
6  Các bên liên quan: tên, vai, tỷ lệ nếu có, và VĂN BẢN KÝ nào xác lập vai đó?
   Bên nào chưa có văn bản thì ghi CHƯA KIỂM và cấm đưa ra ngoài
```

**Nhóm C, điền dần, hỏi khi cần (7, 8 có mặc định ở X0 C7, C8):**

```
7  Loại dữ kiện nào lấy từ nguồn nào là nguồn thắng? Mức nguồn tối thiểu từng
   phạm vi giữ mặc định X0 C7 hay chỉnh?
8  Thuật ngữ bắt buộc dùng, thuật ngữ cấm? Quy tắc hình thức văn bản?
9   Nhịp: quét mail bằng gì, ai giữ, bao lâu nhắc? Ngưỡng rà lại dữ kiện?
10  Dòng kiểm riêng nào cần cộng vào bảng kiểm phát hành?
11  Mục nào của X0 khóa thêm ngoài mặc định C11? Loại việc nào cần nâng mức (C13)?
```

Câu nào người dùng chưa trả lời được: ghi `<chưa điền>`, đưa vào X0 C12, không đoán,
không bịa.

# 3. Chạy thử

Bảng điều khiển MÁY sinh: `python bao_cao.py <00_Index> --bang`; không
`--bang` là báo cáo.

Sau khi cài xong, chạy thử HAI vòng nhỏ để chứng minh hệ chạy được ở cả hai đầu:

```
1  một việc mức A: mở một việc con vào VIEC, tự ghi, cấp mã G, báo một dòng kèm trace
2  một việc mức C thu nhỏ: mở plan, làm một việc con, người dùng chốt, ghi theo
   trình tự X5 mục 3
```

# 3b. Kho CÓ SẴN file, không từ zero

Công ty đã có đống file trước khi cài: KHÔNG đi từng mục _INBOX. Chạy
kiem_van_hanh HAI lần cách nhau ít nhất 5 phút rồi mới đọc khối ĐỀ XUẤT _INBOX:
lần quét đầu luôn trả rỗng theo luật ổn định, "hệ sạch" ở lần đầu KHÔNG có nghĩa
kho không có file. Lấy danh sách file chưa vào sổ, nạp TAILIEU hàng loạt theo khối
bằng MỘT plan mức C; chỉ đổi tên về chuẩn X0 C4 với file CHƯA phát hành (căn
cứ nhận diện: lời người dùng hay dấu vết _SIGNED, _NOP; KHÔNG suy từ tên
suông), file cũ giữ tên, tên gốc ghi vào ô "Căn cứ trạng thái" của chính dòng đó. DUKIEN và VIEC không nạp đón trước, chỉ mở
khi đụng việc thật.

# 3c. Nâng cấp bộ khi repo mẫu ra bản mới

Nâng cấp thì đọc mục 3c CỦA BẢN MỚI vừa tải về, KHÔNG đọc bản trong kho: thủ
tục nâng cấp có thể đã đổi giữa hai bản.

CẤM `git pull`, `git stash`, `git checkout` ở BẤT KỲ đâu trong bản làm việc git
chứa kho, kể cả chạy từ thư mục cha: `_so\` là sổ SỐNG, pull dừng vì local
changes và `git stash` mà git khuyên làm DÒNG SỔ biến mất khỏi bản làm việc.

Đúng: tải bản mới ra THƯ MỤC KHÁC ngoài kho, rồi chép sang `00_Index` HAI nhóm.
(a) file _TEMPLATE mới: để CẠNH bộ mang mã, là nguồn luật để diff. (b) chép ĐÈ
thẳng: INSTRUCTION_WORKOPS_v*.md, README.md, X9_CAIDAT.md, DOC_TRUOC.md,
bao_cao.py, kiem_van_hanh.py,
kiem_tra_bo.py - nhóm này không mang mã công ty, không chứa dữ liệu công ty, bản
mới thay bản cũ là xong (bản v* cũ của INSTRUCTION và GHICHU xóa đi, chỉ giữ
MỘT). Bỏ nhóm (b) thì LƯỚI RÀ của kho đứng yên ở bản cũ và mọi phép kiểm mới
không bao giờ tới. DOC_TRUOC.md là MỐC VERSION mà @NHIP.BANMOI đọc: bỏ nó thì
kho vĩnh viễn tự khai bản cũ và mỗi vòng quý lại nâng cấp lại một lần nữa.

Chép xong: file _TEMPLATE rev 0 mới nằm CẠNH bộ đã
mang mã: chúng là NGUỒN LUẬT, không phải bộ chạy. AI diff template mới với bản
mang mã, áp phần LUẬT sang bản mã bằng MỘT plan mức C, QUYETDINH ghi version;
X0 đã điền giữ nguyên giá trị, chỉ đối chiếu schema mục. instruction_yeu_cau
tăng: NHẮC người dùng dán lại INSTRUCTION vào Project instructions TRƯỚC khi
làm việc tiếp. File _TEMPLATE để nguyên trong 00_Index, không tính là "hai
bản bộ X" của rà 18. Lỡ giữ .git (rà 0g nhắc): xóa nó, sổ trên đĩa nguyên vẹn. Trót `git stash` mất
dòng sổ: `git stash pop`, rồi rà 3c và 2 đối chiếu.

# 4. Luật hỏi lại, áp mãi mãi về sau

```
Giữa chừng đụng tới tham số còn dấu chưa điền (`<chưa điền>`, `<điền...>`, `<N>`,
hay để trống):
  DỪNG việc đang làm ở điểm đó · GOM mọi tham số và dữ kiện còn thiếu CỦA CÙNG
  VIỆC ĐÓ vào MỘT lượt hỏi duy nhất, kèm vì sao cần, không hỏi nhỏ giọt từng câu
  · trả lời xong update ngược X0 (tăng rev, ĐÁNH DẤU dòng C12 thành `[x] <mục> -
  điền lần đầu rev <N> ngày <YYYYMMDD>`, KHÔNG xóa dòng, theo X0 C11 ngoại lệ
  (2)) · rồi mới làm
  tiếp. CẤM đoán, cấm lấy giá trị tạm.

Dữ kiện nghiệp vụ (số, mốc, điều khoản) thiếu thì KHÔNG hỏi để điền vào X0.
X0 chỉ giữ tham số vận hành. Dữ kiện vào sổ DUKIEN theo cửa vào X3, có nguồn và
mức nguồn.

Câu người dùng trả lời miệng trong phiên là căn cứ đủ cho THAM SỐ VẬN HÀNH,
nhưng với VAI CÁC BÊN thì vẫn cần văn bản ký, chưa có thì CHƯA KIỂM.
```
