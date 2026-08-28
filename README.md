# WORKOPS · bộ khởi tạo hệ vận hành công ty bằng AI · v24

Bộ mẫu giúp MỘT công ty giao việc giấy tờ, sổ sách, mail cho Claude làm;
Claude tự ghi chép có kiểm soát. Công ty có PHẦN MỀM cũng dùng được (xem
mục "Công ty có phần mềm" bên dưới). Bên trong: luật thường
trực, bộ cấu hình X0 tới X5, năm sổ lõi, hai script kiểm bằng máy. Repo này
là BỘ MẪU; vận hành hằng ngày diễn ra ở KHO CÔNG TY của bạn (ổ máy đơn hoặc
thư mục mây đồng bộ như Dropbox; kho ổ đơn nhớ sao lưu ra thiết bị khác).

Việc tay duy nhất phải làm ĐÚNG là dán INSTRUCTION vào Project instructions.
Mọi thứ khác: copy nguyên trạng hoặc để AI tự dựng. Mọi sổ sách là file văn bản
thường (markdown) nằm trong kho CỦA BẠN, mở được bằng Notepad; ngừng dùng
WORKOPS lúc nào cũng được, không mất gì, không bị nhốt.

## Cài đặt: bốn bước (bước 3 tùy chọn)

Cowork là loại phiên làm việc của Claude ĐỌC GHI ĐƯỢC file trên máy bạn
(claude.ai/code hoặc app Claude cho máy tính). Việc cài đặt làm trên MÁY
TÍNH, không làm được từ điện thoại. Trong ví dụ dưới, <gốc> là thư mục gốc
công ty do bạn chọn, kiểu D:\CongTyABC hay thư mục Dropbox của công ty.

```
1  Đưa bộ về thành <gốc>\00_Index\ của công ty:

     git clone https://github.com/Long-Forfun/AI-Simple-Workops.git "<gốc>\00_Index"

   Không có git: bấm nút Code màu xanh trên trang GitHub, Download ZIP, giải
   nén. LƯU Ý: giải nén ra thư mục AI-Simple-Workops-main; đổi tên CHÍNH thư
   mục đó (thư mục chứa file README.md này) thành 00_Index rồi chuyển vào
   <gốc>. NGUYÊN TRẠNG: không chọn lọc file, không đổi tên file nào.
   Máy Mac: đường dẫn dùng dấu / thay cho \.
   Dùng git clone: sau khi cài xong, AI xóa thư mục 00_Index\.git giúp bạn.
   Kho đang chạy không nối với GitHub nữa, vì thư mục _so (sổ sách của công
   ty bạn) nằm trong đó.

2  Vào claude.ai, mục Projects, bấm New Project, đặt tên công ty. Mở phần
   Instructions của Project, dán NGUYÊN VĂN toàn bộ nội dung file
   INSTRUCTION_WORKOPS_v11.md (mở file bằng Notepad, bấm Ctrl+A rồi
   Ctrl+C; máy Mac dùng TextEdit, phím là Cmd+A, Cmd+C).
   Không sửa chữ nào.

3  (tùy chọn, chỉ khi sẽ chat trên web/điện thoại không chạm kho) Đưa X0,
   X1, X2, X5 - và X3E nếu bật profile EMAIL - vào tài liệu của Project để
   phiên CHAT có luật mà đọc. ĐỪNG đưa X9 (chỉ đọc một lần lúc cài) và X4
   (chỉ đọc khi rà file): hai file đó ăn thêm gần một phần năm bộ nhớ mỗi
   phiên chat mà không dùng tới. Chỉ dùng Cowork thì bỏ qua cả bước này.

4  Mở phiên Cowork trên máy tính (claude.ai/code, hoặc app Claude chọn chế
   độ Cowork), bấm nút gắn thư mục và chọn folder <gốc>. QUAN TRỌNG: gắn
   folder GỐC (thư mục CHỨA 00_Index), không phải chính 00_Index. Gõ:
   "cài đặt".
   AI hỏi BỐN câu (mã, tên công ty và vai trò · kho ở đâu · dự án đầu tiên · chọn
   profile, không rõ thì trả lời LITE), rồi tự làm phần còn lại: đổi tên
   file theo mã, điền X0, dựng cây folder, chạy thử. TỪ ĐÂY LÀM VIỆC ĐƯỢC.
   Kho đã có sẵn đống file? Nói với AI, nó nạp hàng loạt theo X9 mục 3b.
```

## Ngày thường của bạn

Mỗi lần làm việc: mở phiên Cowork, gắn folder gốc (PHIÊN NÀO CŨNG PHẢI GẮN,
quên gắn thì AI không thấy kho và hệ có vẻ "hỏng"), rồi cứ nói việc bằng tiếng
người. Vài câu tắt đáng nhớ:

```
điểm danh   xem bàn làm việc: việc quá hạn, chờ ai, mail đọng
quét mail   xử thư trong phiên, ra bảng chờ duyệt      (khi bật EMAIL)
rà file     nghi sổ lệch thực tế: kiểm toàn bộ, chỉ báo cáo chưa sửa;
            xem bảng xong muốn sửa mục nào thì nói, AI trình cách rồi làm
chốt sổ     kết phiên an toàn, vét các lượt ghi dở
đồng bộ quan sát   (nâng cao) sau khi quét kho, cho AI tự cập nhật sổ để
            biết file nào là bản mới nhất, bản nào đã cũ
```

Kênh chat (Zalo, Messenger) chưa có lối quét tự động như mail, nhưng
có lối bán thủ công: dán CẢ ĐOẠN chat vào phiên, AI tự tách từng tin và xử
như mục đến ở cửa vào (X3 mục 5b); tin nhắn chưa xác nhận tính là nguồn miệng.

Khi AI trình plan cho việc rủi ro: đọc rồi gõ "chốt" hoặc "ok" nếu đồng ý.
Chỉ vậy. Mã số, rev, trace, mức nguồn là việc của AI, bạn không cần hiểu.

Khi AI báo chữ lạ:

```
rev lệch    bản luật dán trong Project cũ hơn bộ trong kho. Mở file
            INSTRUCTION mới nhất, dán đè lại vào Project instructions
XUNG ĐỘT    hai bản file cùng số hiệu khác nội dung. AI sẽ hỏi, bạn chọn bản đúng
CHƯA KIỂM   thông tin chưa có giấy tờ xác nhận. Dùng nội bộ được,
            chỉ bị chặn khi đưa ra ngoài công ty
```

Cập nhật bộ về sau: tải bản mới về MỘT THƯ MỤC KHÁC (clone hay ZIP đều được),
rồi nói với AI trong phiên Cowork "cập nhật bộ luật, bản mới ở <đường dẫn>".
AI tự đối chiếu, áp phần luật và nhắc nếu cần dán lại INSTRUCTION. Nói rõ với
AI: đọc X9 mục 3c trong THƯ MỤC BẢN MỚI, không đọc bản trong kho.
ĐỪNG chạy `git pull` trong 00_Index, và cả ở thư mục CHA của nó: sổ của bạn nằm
trong đó, git sẽ dừng và lời khuyên `git stash` mà git in ra sẽ làm mất dòng sổ
khỏi thư mục làm việc. Lỡ chạy `git stash` rồi thấy sổ trống: gõ ngay
`git stash pop` ở đúng thư mục đó là dòng quay về, rồi nói với AI "rà file" để
đối chiếu. Đừng gõ thêm lệnh git nào khác trước khi làm việc này.

Muốn hiểu bộ trước khi dùng: đọc [DOC_TRUOC.md](DOC_TRUOC.md) (tổng quan, 1
trang) rồi [X9_CAIDAT.md](X9_CAIDAT.md) (kịch bản phiên đầu). Không cần đọc
X0 tới X5, AI tự tìm tới đúng mục đúng lúc.

## Công ty có phần mềm

Bộ xử được trọn vòng vận hành phần mềm, với điều kiện KHAI RÕ PHẠM VI TỔ
CHỨC của từng phần mềm ngay từ đầu - AI hỏi ở phiên cài đặt (X9 mục 1 câu
3), giá trị nằm ở X0 C2 @DUAN.PHANMEM, mỗi phần mềm một dòng:

```
repo ở đâu · thành phần chính · môi trường (dev, staging, prod ở đâu)
· nơi chạy thật · nơi giữ secret
```

Máy CƯỠNG CHẾ việc khai này: rà 7d báo lệch và nêu đích danh trường còn
thiếu, và báo cả khi công ty làm phần mềm mà chưa khai dòng nào. Khai đủ thì các vận hành liên quan mới chính xác: repo là nguồn sự thật
của code (không chép vào kho), secret không vào kho hay sổ, và mọi thao
tác chạm môi trường CHẠY THẬT đều là việc rủi ro cần bạn duyệt - việc trên
dev, staging là việc nhẹ AI tự làm. Chi tiết mức duyệt từng thao tác: X5
mục 1b; phát hành bản build có bảng kiểm riêng (X2); dump, log mang dữ
liệu khách có phạm vi riêng. Mục nào chưa rõ cứ trả lời "chưa rõ, hỏi
đội kỹ thuật".

## Trong repo có gì

| File | Vai |
|---|---|
| [DOC_TRUOC.md](DOC_TRUOC.md) | Tổng quan bộ, đọc trước |
| [INSTRUCTION_WORKOPS_v11.md](INSTRUCTION_WORKOPS_v11.md) | Luật thường trực, dán nguyên văn vào Project instructions |
| [X0_CAUHINH_TEMPLATE.md](X0_CAUHINH_TEMPLATE.md) | Nguồn duy nhất mọi tham số công ty; phiên đầu điền, rev 0 nghĩa là chưa cài |
| [X1_CAM_TEMPLATE.md](X1_CAM_TEMPLATE.md) | Luật cấm: ký tự, động từ, từ theo phạm vi |
| [X2_PHATHANH_TEMPLATE.md](X2_PHATHANH_TEMPLATE.md) | Luật phát hành đầu ra rời công ty |
| [X3_CUAVAO_TEMPLATE.md](X3_CUAVAO_TEMPLATE.md) | Luật cửa vào: file đến, hai chặng, bảng chờ duyệt |
| [X3E_EMAIL_TEMPLATE.md](X3E_EMAIL_TEMPLATE.md) | Pipeline mail đầy đủ, chỉ nạp khi bật profile EMAIL |
| [X4_RASOAT_TEMPLATE.md](X4_RASOAT_TEMPLATE.md) | Luật rà soát sổ lệch thực tế, các câu tắt |
| [X5_HESO_TEMPLATE.md](X5_HESO_TEMPLATE.md) | Mức tác động A B C, vòng đời tài liệu, hệ sổ |
| [X9_CAIDAT.md](X9_CAIDAT.md) | Kịch bản cài đặt phiên đầu; kho có sẵn (3b); nâng cấp bộ (3c) |
| [_so/](_so) | Năm sổ lõi rỗng (VIEC, DUKIEN, TAILIEU, QUYETDINH, NHATKY) + PLANNING (mức C) + THU (chỉ dùng khi bật EMAIL) + hai view máy sinh |
| [kiem_van_hanh.py](kiem_van_hanh.py) | Kiểm máy hệ sổ của công ty ĐANG CHẠY; RA_SOAT chạy nó trước |
| [kiem_tra_bo.py](kiem_tra_bo.py) | Test hồi quy BỘ MẪU cho người bảo trì; PASS hết mới đóng gói |
| [BENCHMARK_TOKEN.md](BENCHMARK_TOKEN.md) | Benchmark token tĩnh của bộ |
| [GHICHU_DOI_MOI_v24_20260824.md](GHICHU_DOI_MOI_v24_20260824.md) | Nhật ký các vòng đổi mới, cho người đánh giá |
| [WORKOPS_STARTER_v24_20260824_GOP.md](WORKOPS_STARTER_v24_20260824_GOP.md) | Bản gộp nguyên văn mọi file, nạp một lần cho AI đánh giá |

## Nguyên tắc vận hành

```
Luật ở INSTRUCTION và X1 tới X5 · tham số ở X0, nguồn duy nhất, không chép đi đâu
· trạng thái ở _so · việc nhẹ AI tự làm tự ghi, việc đáng kể hỏi một câu, việc rủi
ro mới cần plan và chốt · truy vết đầy đủ ở mọi mức, dồn về một dòng Trace cuối
```

Profile bật theo nhu cầu thật, mặc định LITE: REGULATED (phát hành chính thức,
hồ sơ nhà nước) · PARALLEL (kho nhiều máy cùng ghi) · AUTOMATED (tác vụ hẹn
giờ) · EMAIL (mail là kênh nghiệp vụ chính, mở sổ THU). Bật thêm sau được.

## Hai script kiểm

Cần Python 3, không thư viện ngoài, chạy được trên Windows, macOS, Linux.

Kiểm bộ mẫu (chạy ở gốc repo, cho người bảo trì, sửa bộ xong phải PASS hết):

```bash
python kiem_tra_bo.py .
```

Kiểm kho công ty đang chạy (chạy định kỳ hoặc khi nghi sổ lệch thực tế):

```bash
python kiem_van_hanh.py "<gốc kho>/00_Index" "<gốc kho>"
```
