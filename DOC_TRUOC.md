# BỘ KHỞI TẠO WORKOPS · v24 · 20260824 · đọc file này trước

Bộ này dựng hệ vận hành cho MỘT công ty mới, từ zero. Bốn bước, người dùng làm 1 tới
3, AI làm bước 4. Thời gian từ mở phiên đầu tới làm việc được: ba câu bắt buộc, một câu profile.

```
1  Tạo folder gốc công ty trên kho (máy đơn hoặc thư mục mây đồng bộ). Copy cả bộ
   này vào <gốc>\00_Index\. Đổi <MÃ> trong tên file thành mã công ty
2  Tạo Claude Project cho công ty. Dán NGUYÊN VĂN file INSTRUCTION_WORKOPS_v11.md
   vào Project instructions. Không sửa chữ nào
3  Đưa X0 tới X5 và X9 vào tài liệu của Project. Gắn folder gốc vào phiên Cowork
4  Mở phiên đầu tiên, gõ: "cài đặt". AI đọc X9, hỏi BỐN câu (ba câu chạy được,
   câu bốn chọn profile), điền X0, dựng cây folder mặc định, sinh X0_INDEX và
   bảng điều khiển, chạy thử một vòng mức A và một vòng mức C
```

Từ đó về sau: mọi phiên chạy theo INSTRUCTION. Nguyên tắc vận hành:

```
Luật ở INSTRUCTION và X1 tới X5 · tham số ở X0, nguồn duy nhất, không chép đi đâu
· trạng thái ở _so · việc nhẹ AI tự làm tự ghi, việc đáng kể hỏi một câu, việc rủi
ro mới cần plan và chốt · truy vết đầy đủ ở mọi mức, dồn về một dòng Trace cuối
```

Hệ sổ, gọi cho đúng: NĂM sổ lõi (VIEC, DUKIEN, TAILIEU, QUYETDINH, NHATKY) ·
PLANNING chỉ mở cho việc mức C · THU chỉ tồn tại khi bật profile EMAIL ·
X0_INDEX và BANG_DIEU_KHIEN là VIEW máy sinh, không phải sổ. Hệ lõi không
phình quá năm sổ.

Tham số nào chưa điền thì AI dừng và hỏi đúng lúc cần, trả lời xong tự update ngược
vào X0. Không sửa INSTRUCTION theo từng công ty; thứ gì riêng của công ty đều
xuống X0.

Hai script đi kèm, cần Python 3, không cần thư viện ngoài:

```
kiem_tra_bo.py    cho NGƯỜI BẢO TRÌ BỘ MẪU: test hồi quy (đủ file kể cả benchmark
                  và script, phiên bản khớp, tham chiếu, ký tự cấm, schema, ngân
                  sách token, bản gộp _GOP); PASS hết mới được đóng gói
kiem_van_hanh.py  cho CÔNG TY ĐANG CHẠY: kiểm máy hệ sổ (rev khớp, mã trùng,
                  NHATKY treo, plan không mã, bảng cũ, sổ vượt ngưỡng); RA_SOAT
                  chạy nó trước, AI chỉ xử phần cần phán đoán nghiệp vụ
```
