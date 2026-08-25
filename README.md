# WORKOPS · bộ khởi tạo hệ vận hành công ty bằng AI · v24

Bộ mẫu dựng hệ vận hành cho MỘT công ty mới, từ zero, chạy trên Claude
(Project + phiên Cowork): luật thường trực, bộ cấu hình X0 tới X5, năm sổ lõi,
và hai script kiểm bằng máy. Repo này là BỘ MẪU. Vận hành hằng ngày diễn ra ở
KHO CÔNG TY của bạn (ổ máy đơn hoặc thư mục mây đồng bộ), không diễn ra ở repo.

Từ mở phiên đầu tới làm việc được: BA câu bắt buộc cộng MỘT câu chọn profile.
Phần còn lại AI hỏi đúng lúc cần, điền dần. Việc tay duy nhất là dán INSTRUCTION
vào Project instructions; mọi thứ khác copy nguyên trạng hoặc để AI tự dựng.

## Dùng cho công ty mới: ba bước

Việc tay duy nhất phải làm ĐÚNG là bước 2, dán INSTRUCTION. Còn lại đưa file
về nguyên trạng và để AI tự làm ở phiên đầu.

```
1  Đưa bộ về thành <gốc>\00_Index\ của công ty. Kho là ổ máy đơn hoặc thư mục
   mây đồng bộ như Dropbox:

     git clone https://github.com/Long-Forfun/AI-Simple-Workops.git "<gốc>\00_Index"

   hoặc bấm Code, Download ZIP, giải nén rồi đổi tên thư mục thành 00_Index.
   NGUYÊN TRẠNG: không chọn lọc file, không đổi tên gì.

2  Tạo Claude Project cho công ty. Dán NGUYÊN VĂN nội dung file
   INSTRUCTION_WORKOPS_v11.md vào Project instructions. Không sửa chữ nào.

3  Mở phiên Cowork, gắn folder <gốc> vào phiên, gõ: "cài đặt". AI đọc X9, hỏi
   BỐN câu (mã và tên công ty · kho ở đâu · dự án đầu tiên · chọn profile,
   không rõ thì LITE), rồi tự làm phần còn lại: đổi tên các file _TEMPLATE
   theo mã công ty, điền X0, dựng cây folder, sinh view, chạy thử một vòng
   mức A và một vòng mức C. TỪ ĐÂY LÀM VIỆC ĐƯỢC.
```

Tùy chọn: nếu sẽ dùng phiên CHAT (không chạm được kho) thì đưa X0 tới X5 và
X9 vào tài liệu của Project để CHAT có luật mà đọc. Dùng Cowork thuần thì bỏ
qua được. Cập nhật bộ về sau: git pull ngay trong 00_Index.

Muốn hiểu bộ trước khi dùng: đọc [DOC_TRUOC.md](DOC_TRUOC.md) (tổng quan, 1
trang) rồi [X9_CAIDAT.md](X9_CAIDAT.md) (kịch bản phiên đầu). Không cần đọc
X0 tới X5 trước, AI route tới đúng mục đúng lúc.

## Trong repo có gì

| File | Vai |
|---|---|
| [DOC_TRUOC.md](DOC_TRUOC.md) | Tổng quan bộ, đọc trước |
| [INSTRUCTION_WORKOPS_v11.md](INSTRUCTION_WORKOPS_v11.md) | Luật thường trực, dán nguyên văn vào Project instructions |
| [X0_CAUHINH_TEMPLATE.md](X0_CAUHINH_TEMPLATE.md) | Nguồn duy nhất mọi tham số công ty; phiên đầu điền, rev 0 nghĩa là chưa cài |
| [X1_CAM_TEMPLATE.md](X1_CAM_TEMPLATE.md) | Luật cấm: ký tự, động từ, từ theo phạm vi |
| [X2_PHATHANH_TEMPLATE.md](X2_PHATHANH_TEMPLATE.md) | Luật phát hành đầu ra rời công ty |
| [X3_CUAVAO_TEMPLATE.md](X3_CUAVAO_TEMPLATE.md) | Luật cửa vào: mail, file đến, chống nạp trùng |
| [X4_RASOAT_TEMPLATE.md](X4_RASOAT_TEMPLATE.md) | Luật rà soát sổ lệch thực tế |
| [X5_HESO_TEMPLATE.md](X5_HESO_TEMPLATE.md) | Mức tác động A B C, vòng đời tài liệu, hệ sổ |
| [X9_CAIDAT.md](X9_CAIDAT.md) | Kịch bản cài đặt, chạy đúng một lần ở phiên đầu |
| [_so/](_so) | Năm sổ lõi rỗng (VIEC, DUKIEN, TAILIEU, QUYETDINH, NHATKY) + PLANNING (mức C) + THU (chỉ khi bật EMAIL) + hai view máy sinh |
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
