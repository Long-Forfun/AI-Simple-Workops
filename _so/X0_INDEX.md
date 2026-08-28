# X0_INDEX · <MÃ> · view máy sinh của X0

```yaml
may_sinh: true · sinh_boi: <mã G> · x0_rev: 0 · instruction: <vN>
kho: <đường gốc> · cửa phiên này: <CUA1...> · profile: <LITE hay danh sách bật>
du_an: <mã các dự án đang chạy>
```

Vị trí mục trong X0 (để mở đúng đoạn, không mở cả file):

```
C0 profile · C1 kho · C2 dự án · C3 folder khối · C4 tên file · C5 phạm vi
C6 các bên · C7 nguồn · C8 thuật ngữ · C9 nhịp · C10 kiểm · C11 nhóm khóa
C12 còn thiếu · C13 nâng mức · C14 bản đồ tham chiếu
```

Còn thiếu (chép từ C12): <danh sách hoặc "không">

Lượt CÀI ĐẶT chưa có mã G nào: ghi `sinh_boi: cai dat`.
Luật: sinh lại mỗi khi X0 tăng rev, không sửa tay. Giá trị đưa vào bất kỳ đầu ra
nào phải đọc từ X0 đúng mục, không lấy từ view này.
