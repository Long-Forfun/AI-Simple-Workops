# WORKOPS · bộ khởi tạo trợ lý hồ sơ công ty bằng AI · v24

Bộ mẫu giúp MỘT công ty dùng Claude làm trợ lý giữ hồ sơ: lưu file theo
phiên bản, biết bản nào mới nhất và nằm ở đâu, biết file nào chứa thông tin
gì, trả lời có dẫn nguồn và không đoán khi chưa có căn cứ. Kèm sổ việc và
sổ quyết định để theo dõi việc đang chờ và lý do đã chốt. Người vẫn là
chính; AI ghi chép có kiểm soát và hỏi lại khi chưa chắc.

Mọi sổ là file văn bản (markdown) nằm trong kho CỦA BẠN, mở được bằng
Notepad; ngừng dùng lúc nào cũng được, không mất gì. Repo này là BỘ MẪU;
vận hành hằng ngày ở kho công ty (ổ máy đơn hay thư mục mây như Dropbox;
ổ đơn nhớ sao lưu ra thiết bị khác).

## Cài đặt: bốn bước (bước 3 tùy chọn)

Làm trên MÁY TÍNH. Cowork là loại phiên Claude đọc ghi được file trên máy
(claude.ai/code hoặc app Claude). `<gốc>` là thư mục gốc công ty bạn chọn,
kiểu D:\CongTyABC hay thư mục Dropbox của công ty.

```
1  Đưa bộ về thành <gốc>\00_Index\ của công ty:

     git clone https://github.com/Long-Forfun/AI-Simple-Workops.git "<gốc>\00_Index"

   Không có git: nút Code trên GitHub, Download ZIP, giải nén, đổi tên thư
   mục vừa giải nén thành 00_Index rồi đặt vào <gốc>. Nguyên trạng: không
   bỏ bớt, không đổi tên file nào. Máy Mac dùng dấu / thay cho \.
   00_Index là ngăn LUẬT + SỔ của bộ; tài liệu công ty để ở các folder
   nghiệp vụ (01_, 03_...), không bỏ vào đây.

2  Trên claude.ai tạo Project, đặt tên công ty. Dán NGUYÊN VĂN nội dung
   INSTRUCTION_WORKOPS_v11.md vào Instructions của Project (mở bằng Notepad,
   Ctrl+A, Ctrl+C; Mac: TextEdit, Cmd+A, Cmd+C). Không sửa chữ nào. Đây là
   việc tay duy nhất phải làm đúng.

3  (tùy chọn, chỉ khi sẽ chat trên web/điện thoại không chạm kho) Đưa X0,
   X1, X2, X5 - và X3E nếu bật EMAIL - vào tài liệu Project. ĐỪNG đưa X9
   (chỉ đọc lúc cài) và X4 (chỉ đọc khi rà file). Chỉ dùng Cowork thì bỏ qua.

4  Mở phiên Cowork, gắn folder <gốc> (thư mục CHỨA 00_Index, không phải
   chính 00_Index), gõ "cài đặt". AI hỏi bốn câu: mã và tên công ty · kho
   ở đâu, ai nữa dùng kho · dự án đầu tiên (có phần mềm thì hỏi repo) ·
   profile (không rõ thì LITE). Rồi AI tự đổi tên file theo mã, điền X0,
   dựng cây folder, xóa 00_Index\.git và các file chỉ dành cho người bảo
   trì bộ (GHICHU, bản gộp, BENCHMARK), chạy thử. Từ đây làm việc được.
   Kho đã có sẵn file: nói với AI, nó nạp hàng loạt theo X9 mục 3b.
```

## Ngày thường

Mỗi lần làm việc: mở Cowork, gắn lại folder gốc (quên gắn thì AI không
thấy kho), rồi nói việc bằng tiếng người. Năm câu tắt:

```
điểm danh          bàn làm việc: quá hạn, chờ đối tác, chờ bạn chốt, tài
                   liệu sắp đến hạn; bảng do máy sinh, AI chỉ dịch
rà file            nghi sổ lệch thực tế: kiểm toàn bộ, chỉ báo cáo, chưa sửa
chốt sổ            kết phiên an toàn, vét các lượt ghi dở
quét mail          xử thư trong phiên, ra bảng chờ duyệt (khi bật EMAIL)
đồng bộ quan sát   cập nhật sổ theo bản file mới nhất trên kho
```

Hỏi thông tin: AI trả lời từ sổ và file, nói rõ lấy ở file nào, bản nào;
chưa có giấy tờ xác nhận thì nói "chưa kiểm", không đoán.

Việc rủi ro AI trình plan: đọc rồi gõ "chốt" hay "ok". Chỉ vậy. Mã số, rev,
mức nguồn là việc của AI. Ghi nhầm (sai mã, sai ngày): nói AI sửa; nhật ký
không xóa dòng cũ mà thêm dòng "đính chính".

Excel đang dùng (công nợ, chấm công): giữ nguyên, sổ chỉ trỏ tới file. Giấy
ký chỉ có bản scan: bạn đọc số, AI ghi. Chat Zalo, Messenger: export ra .txt
hay dán cả đoạn vào phiên, AI tách từng tin (X3 mục 5b); tin chưa xác nhận
tính là nguồn miệng. Hai người cùng dùng kho: mỗi người một cửa (CUA1,
CUA2), khai lúc cài.

Khi AI báo chữ lạ:

```
rev lệch    INSTRUCTION trong Project cũ hơn bộ trong kho: dán đè bản mới
XUNG ĐỘT    hai bản file cùng số hiệu khác nội dung: AI hỏi, bạn chọn bản đúng
CHƯA KIỂM   chưa có giấy tờ xác nhận: dùng nội bộ được, không đưa ra ngoài
ĐANG GHI    lượt ghi sổ bỏ dở: nói "chốt sổ" là AI vét lại
plan C treo việc rủi ro đã trình mà bạn chưa gõ "chốt"
LECH        máy thấy sổ lệch thực tế: dán nguyên dòng đó cho AI xử
```

## Cập nhật bộ

Tải bản mới về MỘT THƯ MỤC KHÁC (clone hay ZIP), rồi nói với AI "cập nhật
bộ luật, bản mới ở <đường dẫn>, đọc X9 mục 3c trong THƯ MỤC BẢN MỚI". AI
chép đè script và luật chung, đối chiếu luật với bản đã điền của công ty,
nhắc nếu cần dán lại INSTRUCTION vào Project.

ĐỪNG chạy `git pull` hay `git stash` trong 00_Index hay thư mục CHA: sổ
của bạn nằm đó, stash làm mất dòng sổ. Lỡ stash mà sổ trống: gõ ngay
`git stash pop` ở đúng thư mục đó rồi nói AI "rà file".

## Công ty có phần mềm

Khai MỘT dòng ở X0 C2: `<MÃ PM>  <tên> · repo <URL> · mô tả tới <ngày>:
<phần mềm làm gì>`. Mô tả là bản chụp để trả lời nhanh khỏi mở repo mỗi
lần; hỏi thứ cần chính xác thì AI đọc thẳng repo rồi cập nhật lại mô tả
kèm ngày mới.

Ba luật để kho khỏi loạn: repo là NGUỒN SỰ THẬT của code (code không chép
vào kho) · secret không vào kho, không vào sổ · lượt ghi chạm CHẠY THẬT là
mức C, đội kỹ thuật đã làm rồi thì ghi mức B kèm chữ "xác nhận". Bộ không
deploy, không sửa CSDL, không đổi quyền hộ; chỉ ghi nhận và mở việc.

## Trong repo có gì

| File | Vai |
|---|---|
| [DOC_TRUOC.md](DOC_TRUOC.md) | Tổng quan một trang, đọc trước |
| [INSTRUCTION_WORKOPS_v11.md](INSTRUCTION_WORKOPS_v11.md) | Luật thường trực, dán nguyên văn vào Project |
| [X0_CAUHINH_TEMPLATE.md](X0_CAUHINH_TEMPLATE.md) | Tham số công ty, nguồn duy nhất; rev 0 = chưa cài |
| [X1_CAM_TEMPLATE.md](X1_CAM_TEMPLATE.md) | Luật cấm theo phạm vi |
| [X2_PHATHANH_TEMPLATE.md](X2_PHATHANH_TEMPLATE.md) | Luật gửi tài liệu ra ngoài |
| [X3_CUAVAO_TEMPLATE.md](X3_CUAVAO_TEMPLATE.md) | Luật cửa vào: file đến, chat dán, bảng chờ duyệt |
| [X3E_EMAIL_TEMPLATE.md](X3E_EMAIL_TEMPLATE.md) | Luồng mail, chỉ khi bật EMAIL |
| [X4_RASOAT_TEMPLATE.md](X4_RASOAT_TEMPLATE.md) | Luật rà soát và năm câu tắt |
| [X5_HESO_TEMPLATE.md](X5_HESO_TEMPLATE.md) | Mức A B C, cách ghi sổ, vòng đời tài liệu |
| [X9_CAIDAT.md](X9_CAIDAT.md) | Cài đặt, nạp kho có sẵn (3b), nâng cấp bộ (3c) |
| [_so/](_so) | Sổ mẫu rỗng: năm sổ lõi VIEC, DUKIEN, TAILIEU, QUYETDINH, NHATKY · PLANNING (việc mức C) · THU (khi bật EMAIL) · hai bảng máy sinh X0_INDEX, BANG_DIEU_KHIEN |
| [bao_cao.py](bao_cao.py) | Sinh bảng điều khiển và báo cáo quản lý từ sổ |
| [kiem_van_hanh.py](kiem_van_hanh.py) | Rà kho công ty đang chạy: sổ có khớp file thật |
| [kiem_tra_bo.py](kiem_tra_bo.py) | Test bộ mẫu cho người bảo trì |
| [BENCHMARK_TOKEN.md](BENCHMARK_TOKEN.md) | Đo chi phí token của bộ |
| [GHICHU_DOI_MOI_v24_20260824.md](GHICHU_DOI_MOI_v24_20260824.md), [GHICHU_LICHSU_v24_20260824.md](GHICHU_LICHSU_v24_20260824.md) | Nhật ký các vòng sửa bộ |
| [WORKOPS_STARTER_v24_20260824_GOP.md](WORKOPS_STARTER_v24_20260824_GOP.md) | Bản gộp mọi file, nạp một lần cho AI đánh giá |
| [.github/workflows/kiem.yml](.github/workflows/kiem.yml) | Tự chạy kiem_tra_bo mỗi lần đẩy lên GitHub |

## Nguyên tắc

```
Luật ở INSTRUCTION và X1 tới X5 · tham số ở X0, nguồn duy nhất · trạng thái ở
_so · việc nhẹ AI tự làm tự ghi, việc đáng kể hỏi một câu, việc rủi ro cần
plan và chốt · mọi lượt ghi để dấu vết trong NHATKY
```

Profile, mặc định LITE, bật thêm sau được: REGULATED (hồ sơ nhà nước, phát
hành chính thức) · PARALLEL (nhiều phiên ghi cùng lúc) · AUTOMATED (tác vụ
hẹn giờ) · EMAIL (mail là kênh chính, mở sổ THU).

## Ba script

Python 3, không thư viện ngoài, chạy trên Windows, macOS, Linux. Người dùng
không phải chạy tay: nói "điểm danh" hay "rà file", AI chạy và dịch kết quả.

```bash
python bao_cao.py "<gốc kho>/00_Index"                     # báo cáo quản lý
python bao_cao.py "<gốc kho>/00_Index" --bang              # ghi lại bảng điều khiển
python kiem_van_hanh.py "<gốc kho>/00_Index" "<gốc kho>"   # rà kho đang chạy
python kiem_tra_bo.py .                                    # test bộ mẫu, ở gốc repo
```

Sửa bộ mẫu xong, `kiem_tra_bo.py` phải PASS hết mới đóng gói; CI chạy lại
nó trên mỗi lần đẩy.
