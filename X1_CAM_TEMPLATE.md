```
X1 · CẤM · <MÃ> · v04 · <YYYYMMDD>
Luật cấm. GIÁ TRỊ cấm (từ nào, bên nào, ký tự nào) nằm ở X0, file này trỏ tới và nói
trúng thì làm gì. Đọc toàn bộ khi SOAN_RA, mục 3 và 4 khi NOI_BO.
Sửa file này là việc mức C. Giá trị cấm nằm ở X0: THÊM lệnh cấm mới (siết chặt) là
mức B theo ngoại lệ X0 C11; GỠ hay NỚI lệnh cấm là mức C kèm QUYETDINH.
```

# 1. Lệnh cấm nêu tên

Danh sách tại X0 C6 mục @BEN.CAM. Soạn bất cứ thứ gì rời công ty: đối chiếu từng
lệnh, trúng là DỪNG, báo người dùng, không tự lách bằng cách viết khác đi.

# 2. Từ cấm và điều bắt buộc theo phạm vi

Danh sách tại X0 C5 mục @PHAMVI.CAM và @PHAMVI.BATBUOC. Trước khi phát hành: quét
sạch từ cấm của đúng phạm vi tài liệu, IN kết quả quét; điều bắt buộc thiếu một dòng
là không phát hành.

# 3. Ký tự và số

Quy tắc tại X0 C8 mục @HINHTHUC.KYTUCAM và @HINHTHUC.SO. Áp cho cả tài liệu nội bộ.
Cấm chung trong tên file, mọi công ty: dấu tiếng Việt · khoảng trắng · final · copy
· moi_nhat · ban_cuoi.

# 4. Động từ cấm khi mô tả quan hệ các bên

Danh sách tại X0 C8 mục @HINHTHUC.QUANHE. Thay bằng sự kiện kèm ngày, áp cho mọi bên.

# 5. Hành vi cấm với file và sổ, dùng chung mọi công ty

```
Sửa hoặc xóa file đã ký, đã nộp, file gốc bên ngoài (cờ GỐC KHÔNG SỬA;
ngoại lệ duy nhất: XÓA PHÁP LÝ theo X5 mục 7, phải có Q-<mã>)
Ghi cột "Ở đâu" của TAILIEU ngoài bốn dạng khai ở X0 C1
Chép giá trị của X0 sang file khác rồi làm việc trên bản chép (X0_INDEX là view
máy sinh hợp lệ, nhưng giá trị đưa vào đầu ra phải đọc từ X0 đúng mục)
Chép nguyên dòng sổ vào BANG_DIEU_KHIEN, hoặc dùng BANG_DIEU_KHIEN làm căn cứ sửa
sổ. Bảng chỉ được chứa số liệu dẫn xuất, tóm tắt và mã trỏ về sổ
Đánh dấu đã nạp cho thứ chưa tải được
Làm việc mức C mà không có plan, hoặc ghi sổ mức C khi plan chưa CHỐT
Ghi mức A, B khi chưa kiểm bản mới nhất của file sẽ chạm
Hạ mức tác động của việc thuộc danh mục C
```
