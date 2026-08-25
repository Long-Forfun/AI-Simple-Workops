```
X5 · MỨC TÁC ĐỘNG, VÒNG ĐỜI, HỆ SỔ · <MÃ> · v21 · <YYYYMMDD>
Mục 1 đọc trước MỌI việc đổi trạng thái. Các mục sau đọc khi SUA_FILE
hoặc sắp ghi sổ (mục 3). Dự án, folder, tên file đọc từ X0 C2 C3 C4; mức nâng ở X0 C13.
```

# 1. Mức tác động và vòng đời

Ba mức A B C khai ở INSTRUCTION mục 5. Danh mục chi tiết:

```
C  đầu ra rời công ty (trừ thường lệ dưới đây) · chạm bản đã gửi, đã nộp, đã ký,
   file gốc ngoài · sửa X0 nhóm khóa C11, X1 tới X5, INSTRUCTION (ngoại lệ duy
   nhất theo X0 C11: chỉ THÊM lệnh hay từ cấm để siết chặt là B; gỡ, nới vẫn C)
   · đổi vai các bên, nguồn thẩm quyền · cấu trúc folder, đổi tên hay di chuyển
   hàng loạt · xóa thứ ĐÃ vào sổ hay đã phát hành
B  sửa tài liệu nội bộ đã có sổ · tạo tài liệu nội bộ mới đáng vào sổ · thêm hay
   sửa DỮ KIỆN có phạm vi ra ngoài · mở dự án, khối mới · update ngược X0 ngoài
   nhóm khóa · THÊM lệnh cấm siết chặt theo ngoại lệ C11 · dọn hay xóa nháp
   CHƯA vào sổ
A  mở việc, cập nhật bước, hạn, trạng thái việc · dữ kiện thuần nội bộ có nguồn
   rõ · nạp CUA_VAO đã có nguồn theo X3 · tạo nháp, ghi chú chưa vào sổ · đổi tên
   MỘT file nội bộ chưa phát hành cho đúng chuẩn X0 C4
```

Vòng đời theo mức:

```
A  LÀM, GHI ngay, báo một dòng kèm trace
B  BÁO một câu, đồng ý, LÀM, GHI, báo một dòng
C  PLAN (mục 2), GẬT mới chạm file, LÀM đúng phạm vi, phát sinh bổ sung plan
   trước; VÒNG sửa bao nhiêu lần cũng được, cập nhật plan, KHÔNG ghi sổ, bản
   trung gian đặt v<NN>-nhap<M> không vào TAILIEU; CHỐT mới GHI (mục 3)
```

GHI MỐC, cho plan C có vòng duyệt nhiều bước (soạn, gửi sếp, sửa, gửi đối tác,
sửa, trình ký): MỘT plan bao trùm cả chu kỳ. Mỗi lần bản thật sự được gửi đi là
một GHI MỐC: ghi một dòng NHATKY như mức B, TAILIEU đánh dấu bản vừa gửi là ẢNH
CHỤP (ĐÃ GỬI DUYỆT, không sửa đè), việc tiếp theo làm trên vN+1, plan giữ nguyên
ĐANG LÀM, KHÔNG chốt, KHÔNG đóng. Chỉ phải quay lại xin
gật khi thay đổi một trong: mục tiêu · người nhận hay phạm vi · cam kết · nguồn
thẩm quyền · số liệu chưa có sổ · loại phát hành · hành động khó phục hồi. Phát
sinh vẫn trong mục tiêu cũ: tự cập nhật plan rồi làm tiếp. Plan chỉ CHỐT khi chu
kỳ kết thúc (ký, nộp, phát hành, hoặc người dùng dừng).

Các luật kèm theo:

```
THƯỜNG LỆ   trao đổi rời công ty (mail, tin công việc) không chứa cam kết, điều
            khoản, không phải tài liệu chính thức hay biểu mẫu nhà nước: bỏ plan,
            trình bản xem trước kèm bảng kiểm THƯỜNG LỆ của X2; người dùng xác
            nhận gửi là chốt; ghi như mức B. Số liệu và tên định danh kỹ thuật
            chỉ được xuất hiện khi đã có dòng DUKIEN đúng phạm vi, khi có thì
            bảng kiểm thêm dòng 1 và 2; số chưa có sổ, cam kết, điều khoản xuất
            hiện là hết thường lệ, nâng lên C đầy đủ. X1, X2 vẫn luôn đọc
NHÁP        note, nháp mặc định KHÔNG vào TAILIEU (tạo là A, dọn là B); chỉ vào
            TAILIEU khi người dùng cần tìm lại về sau (mức B), từ đó xóa là C
LÔ          lô nhiều mục độc lập: tách theo mức, phần A làm và ghi luôn, phần B
            gom một câu hỏi, phần C một plan
KIỂM BẢN    "đã cũ" định nghĩa TẤT ĐỊNH: họ tài liệu CHƯA được quét trong
            PHIÊN hiện tại. Lần đầu chạm một họ trong phiên (sửa hay dùng):
            tự quét đúng HỌ đó (không quét cả kho), kết quả rõ thì tự đồng
            bộ vai như câu tắt "đồng bộ quan sát" của X4, không hỏi; người
            dùng tự sửa file rồi mở việc khác cũng không lọt lưới.
            Trước khi ghi: kiểm bản mới nhất của file sẽ chạm, MỘT lần cho mỗi
            file trong một lượt trả lời. KHÁC nghĩa là: có sha256 trong TAILIEU
            thì so sha256; không có thì mtime VÀ dung lượng cùng đổi; đồng bộ mây
            đổi mtime suông không tính, nghi ngờ thì mở đối chiếu nội dung.
            Khác thật: dừng, hỏi, tức tự nâng một mức
CHỐT        người dùng gõ "chốt", "ok", hoặc xác nhận không sửa nữa. Việc C người dùng đã lệnh
            "làm luôn" và hoàn tất TRỌN trong cùng lượt, kết quả đã trình:
            coi là CHỐT, plan sang ĐÃ GHI, không treo. Nhiều plan
            CHỜ CHỐT: lệnh chốt phải nêu mã, không nêu thì hỏi kèm danh sách.
            Bỏ sang việc khác: plan giữ CHỜ CHỐT, không ghi, phiên sau nhắc
KHÔNG NGƯỜI (profile AUTOMATED) phiên hẹn giờ, không ai trả lời: A làm và ghi
            như thường; B và C chỉ CHUẨN BỊ, xếp bảng chờ duyệt, mở dòng VIEC
            hạn phiên sau; ngoài dòng đó không ghi sổ, không gửi, không update
            ngược X0. Người dùng về duyệt một lượt
```

# 2. Planning, chỉ việc mức C

Mở plan ở `_so\PLANNING.md` TRƯỚC khi chạm file. Mã `P-<YYYYMMDD>-<NN>`.

```
| Mã plan | Ngày | Dự án | Loại | Việc | Đọc gì | Sẽ tạo hoặc sửa file | Sẽ đổi dòng nào
| Rủi ro | Trạng thái | Mã ghi |
```

Trạng thái `MỚI` `ĐANG LÀM` `CHỜ CHỐT` `ĐÃ GHI` `HỦY`. Cột "Sẽ đổi dòng nào" ghi
mã cụ thể, không để trống. Plan ĐANG LÀM quá 7 ngày: lên bàn làm việc.

# 3. Ghi sổ, trình tự DUY NHẤT

Điểm ghi: A ngay sau khi làm · B sau khi đồng ý và làm xong · C khi chốt.

```
1  cấp mã G-<YYYYMMDD>-<CỬA>-<NN>, CỬA là cửa vào kho của phiên theo X0 C1 (kho
   một cửa thì luôn là CUA1): hai phiên khác cửa không thể trùng mã. Số NN đọc
   NHATKY ngay trước khi cấp; sang quý chưa có file thì tạo NHATKY_<năm>Q<quý>
   mới từ template trong cùng lượt (mức A), NN đọc ở file của quý mang ngày
   cấp mã. Thao tác A cùng lượt trả lời gộp một mã. Cột Phiên
   của NHATKY ghi ĐỊNH DANH LƯỢT = <CỬA>.<giờ phút>.<hậu tố ngẫu nhiên 3-4 ký
   tự>; cặp (mã G, định danh lượt) dùng để HÒA GIẢI XUNG ĐỘT, không phải khóa
   nguyên tử; mã G chỉ là số hiển thị
2  MỞ dòng NHATKY, Trạng thái ĐANG GHI, "Chạm sổ nào" ghi mã cụ thể (C chép từ
   plan); lượt tạo DÒNG MỚI ở sổ khác thì ô "Làm gì" ghi kèm giá trị chính
   của dòng đó, đủ để tái lập khi đứt lượt. MỌI profile đọc LẠI sổ ngay sau
   khi mở: hai dòng cùng mã G thì
   dòng nằm SAU trong file đổi mã sang số kế tiếp kèm ghi chú "đổi từ <mã> do
   trùng"; hai dòng hệt vị trí thì so định danh lượt, nhỏ hơn theo thứ tự chữ
   đứng, lớn hơn đổi mã: quy tắc tất định, hai phiên cùng áp nên không lặp. Mã G
   chỉ được điền vào các sổ SAU khi đã đứng vững ở NHATKY, nên trùng bị giam
   trong NHATKY và tự phục hồi tại đó. Đây là HÒA GIẢI SAU XUNG ĐỘT, không phải
   khóa nguyên tử; file thường qua đồng bộ mây KHÔNG có khóa nguyên tử, PARALLEL
   phải tuyên bố giới hạn này và khuyến nghị mỗi cửa một phiên ghi tại một thời
   điểm. Rà 12 của X4 là lưới cuối
3  ghi sổ, mỗi dòng chạm tới mang mã G ở cột "Ghi lần"
4  update ngược X0 nếu có, sinh lại X0_INDEX khi rev tăng
5  NHATKY sang XONG; mức C: plan sang ĐÃ GHI, điền mã G
6  sinh lại BANG_DIEU_KHIEN thì header ghi sinh_boi = mã lượt vừa xong của CHÍNH
   cửa mình, kèm dòng watermark: mã cuối của TỪNG cửa (giữa các cửa không có thứ
   tự thời gian tin được, "mới nhất" chỉ có nghĩa trong một cửa). Bảng có thêm:
   khối "Tài liệu đang hoạt động" (tên, vN hiện hành, trạng thái, ở đâu, của các
   tài liệu đang trong chu kỳ) và một dòng nhắc lấy từ X0 C12 khi còn mục thiếu
   chặn phát hành. Sinh xong, COWORK NHẮC người dùng tải BANG_DIEU_KHIEN và X0_INDEX
   lên tài liệu Project (@DUONG.PROJECT ở X0 C1): nền tảng KHÔNG cho phiên tự
   ghi vào Project; CHAT chỉ đọc được bản người dùng đã tải, luôn kèm nhãn
   ngày của bảng và coi bản đó có thể cũ hơn kho
```

NHATKY chỉ-thêm với MỘT ngoại lệ: sửa ô Trạng thái dòng mình vừa mở (và đổi mã
dòng mình khi trùng theo bước 2). Thấy bản "conflicted copy" của MỘT SỔ trong
_so: DỪNG lượt ghi; dòng có ở bản conflict mà vắng ở bản chính thì chép sang
bản chính rồi hòa giải mã theo bước 2, bản conflict chuyển _so\_lich_su\,
ghi một dòng NHATKY (mức B). Plan là dự kiến, NHATKY là thực ghi, sổ là kết
quả, khớp qua mã G.

# 4. Sổ nào giữ gì

```
VIEC.md       dự án · mã · việc · bước tiếp theo · ai làm · chờ ai từ · hạn
              · trạng thái · liên kết · ghi lần
DUKIEN.md     dự án · mã · dữ kiện · giá trị · hiệu lực từ · phạm vi được phép
              · nguồn · MỨC NGUỒN A B C D theo X0 C7 (schema CỐ ĐỊNH mọi
              profile, ô này LUÔN ghi A tới D; thang là CORE, REGULATED chỉ
              thêm nguồn chỉ định và phạm vi chi tiết) · trạng thái · rà lại trước · ghi lần
TAILIEU.md    dự án · mã · tên · vN · ngày · ở đâu · VAI PHIÊN BẢN (HIỆN HÀNH,
              CŨ, XUNG ĐỘT, KHÔNG XÁC ĐỊNH) · trạng thái nghiệp vụ · QUAN SÁT
              LÚC · CĂN CỨ TRẠNG THÁI (mail, lời người dùng, quét kho, biên
              nhận...) · nguồn · hết hạn · cờ · sha256 · ghi lần
QUYETDINH.md  mã Q- · ngày · chọn gì · vì sao · đánh đổi · TRẠNG THÁI (HIỆN HÀNH
              hay ĐÃ THAY) · thay bởi · ghi lần. Không xóa, không sửa NỘI DUNG;
              dòng cũ chỉ được cập nhật hai ô quản trị Trạng thái và Thay bởi
NHATKY_<quý>  mã ghi · ngày · phiên · mức · làm gì · chạm sổ nào · file ra
              · trạng thái · chờ ai
PLANNING.md   mục 2, chỉ mức C
BANG_DIEU_KHIEN.md  view máy sinh: số liệu dẫn xuất, tóm tắt, mã trỏ; cấm chép
              nguyên dòng sổ, cấm dùng làm căn cứ sửa sổ, không là nguồn sự thật
X0_INDEX.md   view máy sinh của X0: rev, kho, profile, dự án, vị trí mục, mục còn
              thiếu. Sinh lại mỗi khi X0 tăng rev, không sửa tay; giá trị đưa vào
              đầu ra phải đọc từ X0 đúng mục, không lấy từ view
_quan_sat_truoc.json  cache máy sinh của bộ quan sát (giữ luật ổn định hai lần
              quét), không phải sổ, không sửa tay, mất thì tự dựng lại
_thu_da_nap.json  (profile EMAIL) registry máy sinh, DANH SÁCH CHUỖI khóa đã
              nạp, chống nạp trùng khi quét lại; mất thì dựng lại từ _thu_nhat_ky
_thu_nhat_ky.ndjson  (profile EMAIL) nhật ký SỰ KIỆN append-only, máy sinh,
              NGUỒN SỰ THẬT: mỗi mail đúng hai sự kiện, PREPARED (kèm payload
              phục hồi: đường dẫn staging cộng danh sách thao tác ghi sổ chuẩn
              hóa) đứng TRƯỚC COMMITTED; registry chỉ dựng từ COMMITTED; mất cả
              nhật ký lẫn registry thì lần quét đầu chỉ đề xuất, không tự nạp;
              mất RIÊNG nhật ký khi registry còn: GIỮ registry làm rào chống
              nạp trùng, CẤM dựng lại từ tập COMMITTED rỗng, ghi QUYETDINH
_thu_ap_dung.json  (profile EMAIL) index máy sinh cho ghi idempotent: mỗi thao
              tác đã áp một dòng "khóa + operation_id" trỏ "sổ + mã dòng"; sổ
              người đọc không mang cột khóa máy; mất thì dựng lại bằng đối
              chiếu payload với sổ
_thu_staging\ (profile EMAIL) vùng bền vững máy sinh giữ nguyên văn thư và
              đính kèm, mỗi mail một thư mục tên sha256(khóa), lưu TRƯỚC khi
              append PREPARED; dọn mức A theo bốn điều kiện X3 mục 6
              (COMMITTED, đích và sha xác minh, .eml bằng chứng đã chuyển,
              qua đệm @NHIP.DEMSTAGING)
_thu_don_staging.json  (profile EMAIL) manifest dọn máy sinh, ghi TRƯỚC khi
              xóa staging: mỗi khóa một mục purged_at, eml_final_path,
              attachment_final_paths, sha256; là căn cứ để staging vắng của
              mail đã COMMITTED không bị coi là lệch
_quan_sat_bo.txt  danh sách đường dẫn công ty muốn loại khỏi bộ quan sát (một
              dòng một mục), người dùng sửa tay được, mặc định không có
```

Phân định: hành động có người và hạn vào VIEC · số, điều khoản, mốc vào DUKIEN ·
file vào TAILIEU · quyết định vào QUYETDINH. Một thứ không nằm hai sổ, mã cấp
một lần.

SUY BẢN HIỆN HÀNH. Máy được tự xác định "bản hiện hành QUAN SÁT ĐƯỢC tới thời
điểm T", không bao giờ tự gọi là "bản cuối". Trong một họ tài liệu (cùng tên bỏ
hậu tố vN):

```
1  bỏ file tạm, autosave, conflict copy (~$, .tmp, "conflicted copy"...)
2  chỉ nhận file ổn định qua hai lần quan sát liên tiếp
3  vN cao hơn là ứng viên hiện hành
4  cùng vN, cùng sha256 là một bản
5  cùng vN, khác sha256: đánh XUNG ĐỘT, cấm tự chọn
6  bản mới thành HIỆN HÀNH, bản trước thành CŨ, không xóa dòng
7  ghi Quan sát lúc và Căn cứ trạng thái = "quét kho <ngày giờ>"
8  IM LẶNG của người dùng chỉ giữ nguyên trạng thái nghiệp vụ: không bao giờ suy
   ra đã duyệt, đã gửi, đã phát hành hay việc đã XONG từ im lặng
```

Vai phiên bản là quan sát của máy, đổi tự do theo bằng chứng quét (mức A);
trạng thái NGHIỆP VỤ chỉ đổi khi có căn cứ: mail, biên nhận, lời người dùng.

```
VIEC     MỚI · ĐANG LÀM · CHỜ ĐỐI TÁC · CHỜ DUYỆT · TREO · XONG · HỦY
DUKIEN   CHƯA KIỂM · ĐÃ KIỂM · MÂU THUẪN · ĐÃ THAY · HẾT HẠN
TAILIEU  NHÁP · CHỜ DUYỆT NỘI BỘ · ĐÃ GỬI DUYỆT · ĐÃ DUYỆT NỘI BỘ ·
         ĐÃ PHÁT HÀNH · ĐÃ NỘP · TRẢ HỒ SƠ · ĐÃ CẤP · ĐÃ KÝ
         Gửi sếp hay đối tác GÓP Ý là ĐÃ GỬI DUYỆT: đúng FILE đã gửi là ẢNH
         CHỤP bằng chứng, KHÔNG sửa đè; công việc tiếp tục trên bản vN+1 mới,
         plan không đóng. BẤT BIẾN nghĩa là NỘI DUNG (byte) của chính file đã
         gửi không được sửa đè, áp từ ĐÃ GỬI DUYỆT trở đi; còn TRẠNG THÁI
         NGHIỆP VỤ của dòng TAILIEU vẫn được TIẾN LÊN khi có bằng chứng
         (ĐÃ GỬI DUYỆT sang ĐÃ DUYỆT NỘI BỘ khi có câu xác nhận rõ). Khác
         nhau ở chỗ ĐÃ GỬI DUYỆT thì chu kỳ còn mở, còn ĐÃ PHÁT HÀNH, ĐÃ
         NỘP, ĐÃ KÝ, ĐÃ CẤP là mốc chính thức, sửa gì cũng bằng văn bản mới
         theo luật cốt lõi 3
```

Việc chưa xong đủ bước, người, hạn. Cái gì đổi ghi vào đâu: số mới vào DUKIEN kèm
nguồn, mức nguồn, phạm vi · số thay: dòng cũ ghi "thay bởi mã", không xóa · file
mới hay sửa: TAILIEU tăng vN · gửi, nộp, ký, cấp: TAILIEU đổi trạng thái kèm
ngày, cho ai · chốt phương án: QUYETDINH · file gốc ngoài: 99_Goc, cờ GỐC, sha256
· thiếu nguồn hay hai nguồn cãi: CHƯA KIỂM, MÂU THUẪN · bỏ không làm: HỦY kèm lý
do, không XONG.

# 5. Đọc sổ và chuyển lịch sử

Đọc đúng mục theo dự án và khối (`sed -n '/^## <KHỐI>/,/^## /p'`, `grep '^| V-'`),
không mở cả file. BANG_DIEU_KHIEN và X0_INDEX đọc cả file vì chúng phải ngắn.
Chuyển `_so\_lich_su\`: việc XONG, HỦY quá 30 ngày · dữ kiện ĐÃ THAY · tài liệu
đã thay không còn viện dẫn · plan ĐÃ GHI quá 30 ngày. QUYETDINH chia theo năm,
NHATKY theo quý.

# 6. Folder và tên file

Cây theo X0 C3, tên theo X0 C4; tầng ngoài chức năng, tầng trong dự án; chức năng
đã có thì mở folder con, không mở folder chức năng mới. Bản cuối một tài liệu chỉ
nằm một kho. Đổi tên hàng loạt là mức C kèm QUYETDINH. Tài liệu gốc dài: gốc
nguyên vẹn ở 99_Goc, thêm _Summary có bảng tra ngược, TAILIEU trỏ Summary.

# 7. Ngưỡng lưu trữ và chuyển đổi

COWORK sao _so\ vào _so\_lich_suackup_<YYYYMMDD>\ tối đa một lần mỗi ngày,
trước lượt ghi đầu tiên của ngày, giữ 7 bản gần nhất (mức A, không vào sổ).

Chạm MỘT trong ba là xử lý: sổ vượt 500 dòng dữ liệu · file vượt 1 MB · đọc, tìm
thường dùng chậm rõ rệt. Bước 1: tách theo khối hoặc năm vào `_so\_lich_su\`.
Vẫn vượt: chuyển phần dữ liệu sang CSV hoặc SQLite theo đặc tả tối thiểu, chi
tiết hóa bằng một plan mức C khi chạm ngưỡng thật:

```
1  file dữ liệu mới là NGUỒN SỰ THẬT; sổ Markdown còn header, luật đọc, con trỏ
2  mã V D T Q và mã G vẫn cấp theo mục 3, NHATKY vẫn Markdown, vẫn mở dòng TRƯỚC
3  đứt giữa lượt ghi: "chốt sổ" của X4 đối chiếu NHATKY với file dữ liệu
4  dòng thay thế đánh dấu như luật hiện tại, không xóa; backup bản theo ngày vào
   _so\_lich_su\ trước lượt ghi có đổi cấu trúc
5  BANG_DIEU_KHIEN sinh từ nguồn sự thật mới, cách đọc của người dùng không đổi
```
