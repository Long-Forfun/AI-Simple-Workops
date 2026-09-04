# WORKOPS · bộ khởi tạo hệ vận hành công ty bằng AI · v24

Bộ mẫu giúp MỘT công ty giao việc giấy tờ, sổ sách, mail cho Claude làm;
Claude tự ghi chép có kiểm soát. Công ty có PHẦN MỀM: xem
mục "Công ty có phần mềm" bên dưới. Bên trong: luật thường
trực, cấu hình X0 tới X5, năm sổ lõi, ba script máy. Repo này là BỘ
MẪU; vận hành hằng ngày ở KHO CÔNG TY của bạn (ổ máy đơn hay thư mục mây
như Dropbox; ổ đơn nhớ sao lưu ra thiết bị khác).

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
   ty bạn) nằm trong đó. 00_Index = ngăn LUẬT + SỔ của bộ; đừng bỏ file
   công ty vào đây (tài liệu để ở các folder nghiệp vụ 01_, 03_...).

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
đồng bộ quan sát   (nâng cao) cho AI cập nhật sổ theo bản mới nhất trên kho
```

Excel đang dùng (công nợ, chấm công): giữ nguyên, sổ chỉ trỏ file. Giấy ký
chỉ có scan: bạn đọc số, AI ghi. Kênh chat (Zalo, Messenger): export chat
ra .txt hay dán CẢ ĐOẠN vào phiên, AI tự tách từng tin và xử
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
ĐANG GHI    lượt ghi sổ bỏ dở; nói "chốt sổ" là AI vét lại
plan C treo việc rủi ro đã trình mà bạn chưa gõ "chốt"
LECH        máy thấy sổ lệch thực tế; dán nguyên dòng đó cho AI xử
```

Cập nhật bộ về sau: tải bản mới về MỘT THƯ MỤC KHÁC (clone hay ZIP đều được),
rồi nói với AI trong phiên Cowork "cập nhật bộ luật, bản mới ở <đường dẫn>".
AI tự đối chiếu, áp phần luật và nhắc nếu cần dán lại INSTRUCTION. Nói rõ với
AI: đọc X9 mục 3c trong THƯ MỤC BẢN MỚI, không đọc bản trong kho.
ĐỪNG chạy `git pull` hay `git stash` trong 00_Index hay thư mục CHA: sổ
của bạn nằm đó, stash làm mất dòng sổ. Lỡ stash mà sổ trống: gõ ngay
`git stash pop` ở đúng thư mục đó rồi nói AI "rà file".

Muốn hiểu bộ trước khi dùng: đọc [DOC_TRUOC.md](DOC_TRUOC.md) (tổng quan, 1
trang) rồi [X9_CAIDAT.md](X9_CAIDAT.md) (kịch bản phiên đầu). Không cần đọc
X0 tới X5, AI tự tìm tới đúng mục đúng lúc.

## Công ty có phần mềm

Khai MỘT dòng ở X0 C2: `<MÃ PM>  <tên> · repo <URL> · mô tả tới <ngày>:
<phần mềm làm gì>`. Hết. Mô tả là bản chụp để trả lời nhanh khỏi mở repo
mỗi lần; hỏi thứ cần chính xác thì AI đọc thẳng repo rồi cập nhật lại mô
tả kèm ngày mới. Không bắt bạn khai tính năng, môi trường, hạ tầng ra sổ.

Ba luật đi kèm, để kho khỏi loạn: repo là NGUỒN SỰ THẬT của code (code
không chép vào kho) · secret không vào kho, không vào sổ · lượt ghi chạm
CHẠY THẬT là mức C, đội kỹ thuật đã làm rồi thì ghi mức B kèm chữ "xác
nhận". Bộ KHÔNG deploy, migration, sửa CSDL hay đổi quyền hộ - chỉ ghi
nhận và mở việc chuyển đội kỹ thuật.

## Trong repo có gì

| File | Vai |
|---|---|
| [DOC_TRUOC.md](DOC_TRUOC.md) | Tổng quan bộ, đọc trước |
| [INSTRUCTION_WORKOPS_v11.md](INSTRUCTION_WORKOPS_v11.md) | Luật thường trực, dán nguyên văn vào Project instructions |
| [X0_CAUHINH_TEMPLATE.md](X0_CAUHINH_TEMPLATE.md) | Tham số công ty; rev 0 = chưa cài |
| [X1_CAM_TEMPLATE.md](X1_CAM_TEMPLATE.md) | Luật cấm theo phạm vi |
| [X2_PHATHANH_TEMPLATE.md](X2_PHATHANH_TEMPLATE.md) | Luật phát hành ra ngoài |
| [X3_CUAVAO_TEMPLATE.md](X3_CUAVAO_TEMPLATE.md) | Luật cửa vào: file đến, hai chặng, bảng chờ duyệt |
| [X3E_EMAIL_TEMPLATE.md](X3E_EMAIL_TEMPLATE.md) | Pipeline mail, chỉ khi bật EMAIL |
| [X4_RASOAT_TEMPLATE.md](X4_RASOAT_TEMPLATE.md) | Luật rà soát, các câu tắt |
| [X5_HESO_TEMPLATE.md](X5_HESO_TEMPLATE.md) | Mức tác động A B C, vòng đời tài liệu, hệ sổ |
| [X9_CAIDAT.md](X9_CAIDAT.md) | Cài đặt; kho có sẵn (3b); nâng cấp (3c) |
| [_so/](_so) | Năm sổ lõi rỗng + PLANNING (mức C) + THU (khi bật EMAIL) + hai view máy sinh |
| [bao_cao.py](bao_cao.py) | Máy sinh bảng điều khiển + báo cáo quản lý |
| [kiem_van_hanh.py](kiem_van_hanh.py) | Kiểm máy hệ sổ công ty ĐANG CHẠY |
| [kiem_tra_bo.py](kiem_tra_bo.py) | Test hồi quy BỘ MẪU cho người bảo trì; PASS hết mới đóng gói |
| [BENCHMARK_TOKEN.md](BENCHMARK_TOKEN.md) | Benchmark token tĩnh của bộ |
| [GHICHU_DOI_MOI_v24_20260824.md](GHICHU_DOI_MOI_v24_20260824.md) | Nhật ký đổi mới |
| [WORKOPS_STARTER_v24_20260824_GOP.md](WORKOPS_STARTER_v24_20260824_GOP.md) | Bản gộp mọi file, nạp một lần cho AI đánh giá |

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

Python 3, không thư viện ngoài, chạy trên Windows, macOS, Linux.

Kiểm bộ mẫu (ở gốc repo, cho người bảo trì, sửa bộ xong phải PASS hết):

```bash
python kiem_tra_bo.py .
```

Nghi sổ lệch: nói AI "rà file" là đủ - AI chạy máy kiểm và DỊCH kết quả
thành việc cần làm. Tự chạy tay (tùy chọn, ra bảng kỹ thuật):

```bash
python kiem_van_hanh.py "<gốc kho>/00_Index" "<gốc kho>"
```
