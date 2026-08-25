# WORKOPS · bộ khởi tạo hệ vận hành công ty bằng AI · v24

Bộ mẫu dựng hệ vận hành cho MỘT công ty mới, từ zero, chạy trên Claude
(Project + phiên Cowork): luật thường trực, bộ cấu hình X0 tới X5, năm sổ lõi,
và hai script kiểm bằng máy. Repo này là BỘ MẪU. Vận hành hằng ngày diễn ra ở
KHO CÔNG TY của bạn (ổ máy đơn hoặc thư mục mây đồng bộ), không diễn ra ở repo.

Từ mở phiên đầu tới làm việc được: BA câu bắt buộc cộng MỘT câu chọn profile.
Phần còn lại AI hỏi đúng lúc cần, điền dần.

## Dùng cho công ty mới: sáu bước

Người dùng làm bước 1 tới 5, AI làm bước 6.

```
1  Lấy bộ về máy:
     git clone https://github.com/Long-Forfun/AI-Simple-Workops.git
   hoặc bấm Code, Download ZIP rồi giải nén.

2  Tạo folder gốc công ty trên kho (máy đơn hoặc thư mục mây như Dropbox).
   Copy BỘ CHẠY vào <gốc>\00_Index\ :
     INSTRUCTION_WORKOPS_v11.md · DOC_TRUOC.md · X0 tới X5 · X9_CAIDAT.md
     · cả thư mục _so\ · kiem_van_hanh.py
   Bốn thứ còn lại (GHICHU_DOI_MOI, BENCHMARK_TOKEN, *_GOP.md, kiem_tra_bo.py)
   là hồ sơ của người bảo trì bộ mẫu, không cần copy; copy thừa cũng không hại.

3  Đổi hậu tố _TEMPLATE trong tên file X0 tới X5 thành mã công ty (3-4 ký tự
   viết hoa). Ví dụ mã ABC: X0_CAUHINH_TEMPLATE.md thành X0_CAUHINH_ABC.md.

4  Tạo Claude Project cho công ty. Dán NGUYÊN VĂN nội dung file
   INSTRUCTION_WORKOPS_v11.md vào Project instructions. Không sửa chữ nào.

5  Đưa X0 tới X5 và X9 vào tài liệu của Project. Mở phiên Cowork, gắn folder
   gốc công ty vào phiên.

6  Ở phiên đầu tiên, gõ: "cài đặt". AI đọc X9, hỏi BỐN câu (mã và tên công ty
   · kho đặt ở đâu · dự án đầu tiên · chọn profile, không rõ thì LITE), điền
   X0, dựng cây folder mặc định, sinh X0_INDEX và bảng điều khiển, chạy thử
   một vòng mức A và một vòng mức C. TỪ ĐÂY LÀM VIỆC ĐƯỢC.
```

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
