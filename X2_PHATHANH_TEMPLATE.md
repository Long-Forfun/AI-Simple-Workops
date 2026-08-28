```
X2 · PHÁT HÀNH · <MÃ> · v06 · <YYYYMMDD>
Đọc TOÀN BỘ cùng X1 khi SOAN_RA, hoặc SUA_FILE mà bản sửa sẽ gửi ra ngoài.
Phát hành là việc mức C; trao đổi thường lệ đi vòng rút gọn, điều kiện ở X5 mục 1.
Giá trị đọc từ X0 các mục C5 C6 C7 C8 C10.
```

# 1. Bảng kiểm trước khi phát hành

Chạy TRƯỚC khi tài liệu rời công ty. Cấm thay bằng câu "đã kiểm". Cách in: dòng
TRƯỢT hay cần người dùng quyết in đầy đủ kèm chứng minh; các dòng ĐẠT gom thành
một khối ngắn, mỗi dòng một câu chứng minh tối thiểu. Gấp đến đâu cũng không bỏ
dòng nào, chỉ được in gọn.

Bước 1, xác định: tên chuẩn và vN · phạm vi, một giá trị trong tập đóng X0 C5 · gửi
cho ai · mức kiểm theo X0 C10. Không xác định được phạm vi thì dừng, hỏi.

Bước 2, bảng kiểm:

```
1   số kỹ thuật, số tiền, mốc, tỷ lệ đều có dòng ở DUKIEN
    liệt kê <số> = <mã dữ kiện> | <nguồn>. Số dẫn xuất ghi công thức
2   phạm vi tài liệu nằm trong danh sách phạm vi của mọi dữ kiện dùng
3   chỉ chứa dữ kiện của đúng công ty này
4   vai các bên đúng theo X0 C6
5   số kỹ thuật khớp nguồn thẩm quyền X0 C7, kèm đơn vị hoặc loại số đo
6   mọi dữ kiện dùng đạt MỨC NGUỒN tối thiểu của phạm vi theo X0 C7, hoặc đi theo
    ngoại lệ nguồn chỉ định của C7 với đủ bốn hàng rào; liệt kê dữ kiện nào mức
    nào, nguồn chỉ định nào. Hồ sơ nhà nước dùng nguồn dưới A: in cảnh báo "dưới
    chuẩn mặc định, theo nguồn chỉ định <mã>", người dùng xác nhận riêng dòng này
7   thuật ngữ bắt buộc và cấm theo X0 C8 và X1
8   không ký tự cấm, không làm tròn ngoài khai báo X0 C8
9   mục lục khớp 1:1 file thực tế
10  file gốc đính kèm còn nguyên vẹn, so lại sha256
11  giấy tờ viện dẫn còn hiệu lực tại ngày gửi
12  bản này khớp bản đã duyệt nội bộ
13+ dòng kiểm riêng của công ty theo X0 C10
```

Bước 3: một dấu sai là không phát hành, ghi VIEC. Đủ thì trình người dùng duyệt.
AI không tự gửi.

Bước 4, sau khi người dùng xác nhận đã gửi: TAILIEU đổi trạng thái kèm ngày và cho
ai, dán danh sách số đã dùng · bản nộp vào `01_Phap_ly\_NOP_YYYYMMDD\` rồi khóa ·
nháp cũ vào `_lich_su\` · VIEC cập nhật.

# 2. Mức áp dụng

Theo X0 C10 mục @KIEM.MUC. Dòng 1 và 3 không bao giờ được bỏ với đầu ra rời công ty.

Mức THƯỜNG LỆ, chỉ cho đầu ra đạt điều kiện ngoại lệ thường lệ ở X5 mục 1:
in dòng 3 · 4 · 7 · 8, kèm một câu xác nhận "không chứa cam kết, điều khoản". Có
nhắc tới số liệu hay tên định danh kỹ thuật ĐÃ CÓ SỔ: in thêm dòng 1 và 2. Xuất
hiện số liệu chưa có sổ, cam kết hay điều khoản: hết thường lệ, chạy ĐẦY ĐỦ.
NGOẠI LỆ HẬU CẦN: giờ hẹn, địa điểm, thông tin liên hệ CỦA CHÍNH trao đổi đó
do người dùng vừa đưa trong phiên KHÔNG tính là số liệu nghiệp vụ, không cần
dòng DUKIEN, không thoát thường lệ; số kỹ thuật, tiền, tỷ lệ, mốc cam kết
luôn tính là số liệu nghiệp vụ (một ngoại lệ duy nhất: NGOẠI LỆ SỰ CỐ dưới
đây). Phép thử: mốc do chính trao đổi này đặt cho việc GẶP, GỌI, HẸN là HẬU
CẦN; mốc giao hàng, gửi tài liệu ĐÃ HỨA, nghĩa vụ hợp đồng, tiến độ, hiệu
lực là CAM KẾT. NGOẠI LỆ SỰ CỐ: thông báo sự cố đang diễn ra (phần mềm, vận
hành) gửi được NGAY với giờ phát hiện và dự kiến khắc phục của chính sự cố;
DUKIEN ghi bù trong cùng phiên, mức nguồn B, nguồn "vận hành sự cố <ngày>".

Phát hành PHẦN MỀM cho khách: bảng kiểm chạy trên BỘ TÀI LIỆU PHÁT HÀNH đi
kèm (release note, hướng dẫn, phiên bản); gói build ghi TAILIEU: nằm trong kho
thì "Ở đâu" dạng Kho kèm sha256; chỉ tồn tại trong repo thì dạng Repo trỏ tag
release, ô sha256 bỏ trống theo C1, sha256 của gói ghi vào ô "Căn cứ trạng thái" của chính dòng đó, dạng
"sha256 gói <giá trị>".
Dòng 1-2 áp cho số liệu trong tài liệu đi kèm, không áp lên binary.

# 3. Phát hiện tài liệu đã gửi bị sai

Dừng ngay · ghi VIEC mức gấp: sai gì, bản nào, gửi ai ngày nào · trình phương án cho
người dùng chọn · CẤM tự đính chính, tự sửa, tự đổi trạng thái bản đó. Bản đã ra
ngoài bất biến kể cả khi sai, sửa bằng văn bản mới.
