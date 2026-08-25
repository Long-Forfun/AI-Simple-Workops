```
X3E · EMAIL · <MÃ> · v01 · <YYYYMMDD>
Chỉ đọc khi X0 C0 bật profile EMAIL; là phần đầy đủ của X3 mục 6, giá trị đọc
từ X0 C9. Không bật EMAIL thì file này không được nạp, không tính thuế context.
```

# 1. Pipeline mail


```
MỘT HỘP THƯ bộ quét chỉ đọc đúng hộp thư khai ở X0 C9 @NHIP.HOPTHU. Máy có
            nhiều hộp thư nhiều công ty: mỗi công ty một hộp, một pipeline,
            một bộ sổ riêng; mail hộp khác lọt vào là lệch, rà và loại
SỔ THƯ      _so\THU.md: một dòng một LUỒNG, mã #L-<NNN>, luồng nhận diện bằng
            Conversation-ID (tiêu đề đổi khi Re/Fw, không làm khóa); một
            Conversation-ID chỉ được nằm ở MỘT dòng THU. KHÓA của
            một mail là Message-ID; thiếu Message-ID thì khóa thay thế DUY
            NHẤT serialize CỐ ĐỊNH: FB-<sha256(convId + thời điểm UTC tới giây
            + tiêu đề chuẩn hóa + 200 ký tự đầu thân thư)>, không có dạng
            khóa nào khác.
            Chống nạp trùng bằng REGISTRY _so\_thu_da_nap.json (máy sinh, là
            DANH SÁCH CHUỖI khóa, không dạng nào khác): khóa nằm trong registry
            thì bỏ qua kể cả khi quét lại toàn hộp
NHẬT KÝ SỰ  _so\_thu_nhat_ky.ndjson, append-only, NGUỒN SỰ THẬT. Mỗi dòng một
KIỆN        JSON object: "ev" CHỈ nhận PREPARED hoặc COMMITTED, khóa nằm ở
            trường "khoa" DUY NHẤT và là CHUỖI ("msgId" kiểu cũ chỉ được nạp
            qua một lượt migration riêng, không đọc lẫn hai dạng), "hop_thu"
            bắt buộc ở cả hai loại; sai một điều là dòng hỏng.
            Mỗi mail đúng HAI sự kiện, PREPARED đứng TRƯỚC COMMITTED; lượt
            phục hồi không append PREPARED mới, dùng lại payload cũ.
            Thứ tự ghi an toàn bốn bước:
            1  STAGING trước, PREPARED sau: lưu nguyên văn thư (.eml hay body
               đầy đủ, KHÔNG rỗng) cùng MỌI đính kèm vào thư mục
               _so\_thu_staging\<sha256(khóa)>\ (mỗi mail MỘT thư mục riêng,
               tên bằng đúng sha256 của khóa, không dùng chung), rồi mới
               append PREPARED có PAYLOAD PHỤC HỒI: convId, người gửi, thời
               điểm UTC, tiêu đề, đường dẫn staging (đường dẫn TƯƠNG ĐỐI, sau
               chuẩn hóa PHẢI còn nằm bên trong _so\_thu_staging\, cấm tuyệt
               đối, cấm chấm chấm, cấm symlink thoát ra), sha256 của file
               .eml hay body, danh sách đính kèm kèm sha256 và byte của TỪNG
               file (tên đính kèm là BASENAME thuần, không dấu phân cách
               đường dẫn, không chấm chấm), danh sách THAO TÁC ghi sổ đã
               chuẩn hóa: mỗi thao tác đủ operation_id (DUY NHẤT trong một
               mail), sổ đích (THU VIEC DUKIEN TAILIEU QUYETDINH), mã dòng,
               nội dung dòng.
               Phục hồi = staging cộng thao tác, KHÔNG đọc lại hộp thư; tên và
               dung lượng đính kèm suông KHÔNG phải payload phục hồi; staging
               hụt thì không được append PREPARED
            2  áp từng thao tác, ĐỐI CHIẾU trước ghi sau để không có khe sinh
               dòng đôi: "khoa + operation_id" đã có trong INDEX
               _so\_thu_ap_dung.json (máy sinh) thì bỏ qua; CHƯA có trong
               index thì trước tiên TÌM mã dòng của thao tác trong sổ đích,
               thấy rồi (lần trước chết sau khi ghi sổ, trước khi ghi index)
               thì CHỈ bổ sung index; chưa thấy mới ghi dòng, đọc lại xác
               minh, rồi bổ sung index trỏ "sổ + mã dòng" khớp ĐÚNG thao tác
               trong payload. Sau khi mail COMMITTED: tập mục index của mail
               bằng ĐÚNG tập thao tác payload, không thừa không thiếu. Chạy
               lại bao nhiêu lần cũng không sinh dòng trùng; sổ người đọc
               không phải mang thêm cột khóa máy
            3  append COMMITTED khi mọi thao tác và đính kèm đã đủ
            4  registry CHỈ dựng từ các sự kiện COMMITTED
            Chết giữa chừng: PREPARED không có COMMITTED là lượt DỞ DANG, phục
            hồi bằng cách chạy lại bước 2 từ payload và staging, cấm đọc lại
            hộp thư. COMMITTED không có PREPARED, hay đứng trước PREPARED, là
            nhật ký hỏng, rà ngay. Mất registry: dựng lại từ COMMITTED. Mất
            index: dựng lại bằng cách đối chiếu thao tác trong payload với sổ.
            Mất CẢ nhật ký lẫn registry: lần quét đầu chỉ xuất danh sách
            ỨNG VIÊN chờ duyệt, không tự nạp.
            DỌN STAGING là việc mức A, tự làm khi đủ BỐN điều: mail đã
            COMMITTED · file đích và sha256 đã xác minh · .eml cần làm bằng
            chứng đã chuyển sang 04_Trao_doi hay vùng lưu chính · đã qua thời
            gian đệm X0 C9 @NHIP.DEMSTAGING. Thiếu một điều thì giữ nguyên.
            TRƯỚC khi xóa phải ghi MANIFEST DỌN _so\_thu_don_staging.json
            (máy sinh): mỗi khóa một mục gồm purged_at, eml_final_path,
            attachment_final_paths, sha256; nhờ đó staging vắng của mail đã
            COMMITTED có manifest hợp lệ là BÌNH THƯỜNG, còn staging vắng khi
            lượt chưa COMMITTED hay không có manifest là lệch
TRẠNG THÁI  CHỜ TÔI chỉ khi đủ NĂM điều: thư cuối không phải của mình · mình ở
            To (không phải chỉ CC) · thư có câu hỏi hay yêu cầu hành động thật,
            không phải thư thông báo · yêu cầu đọc từ PHẦN NGƯỜI GỬI VỪA VIẾT
            (cắt lịch sử trích dẫn, chữ ký; câu xã giao "please find/see" không
            phải yêu cầu) · yêu cầu NHẮM VÀO MÌNH: thư chào đích danh người
            khác (Hi Mark, Dear Vincent) mà thân thư không gọi mình thì không
            tính dù mình ở To. Thiếu một điều thì là THEO DÕI. Thư cuối
            của mình gửi đi: CHỜ ĐỐI TÁC, quá @NHIP.CHODOITAC lên bàn làm việc.
            CHỜ ĐỐI TÁC cũng cần BẰNG CHỨNG mong phản hồi: thư mình gửi có
            câu hỏi hay yêu cầu thật; thư mình gửi chỉ để thông báo hay gửi
            file thì KHÔNG chờ ai, chuyển THEO DÕI hay ĐÃ ĐÓNG, khỏi nhắc oan.
            Người dùng nói bỏ luồng: BỎ QUA, không nhắc lại. Việc đã xử lý qua
            họp hay kênh khác theo lời người dùng: ĐÃ ĐÓNG, căn cứ ghi lời nói.
            MỌI tài khoản mail của người dùng khai ở X0 C9 @NHIP.TAIKHOAN, thư
            từ bất kỳ tài khoản nào trong đó đều tính là "của mình"; tên và
            bí danh để nhận "thư chào đích danh MÌNH" đọc từ X0 C9
            @NHIP.TENGOI, bộ email TỰ lấy từ tên tài khoản khi cài, chỉ hỏi
            khi không lấy được
DIGEST      KHUÔN BẮT BUỘC, đúng thứ tự: 1 dòng đầu đếm CHỜ TÔI và CHỜ ĐỐI
            TÁC QUÁ HẠN · 2 CHỜ TÔI, mỗi thư đủ: mã luồng, người gửi, tiêu
            đề, ý chính một câu, TÔI CẦN LÀM GÌ, hạn nếu có, file liên quan
            · 3 CHỜ ĐỐI TÁC: đang chờ BÊN NÀO, chờ VIỆC GÌ, từ NGÀY nào · 4 CHỈ
            THEO DÕI để riêng, trình bày ngắn · 5 cuối tin: giờ quét THẬT
            (đọc từ nguồn X0 C9 @NHIP.TRANGTHAI, không lấy giờ chạy báo
            cáo), giờ tạo bản tin, tình trạng DỮ LIỆU MỚI hay CŨ.
            Chống gửi lặp bằng khóa NỘI DUNG: chỉ GIÁ TRỊ giờ trình bày nằm
            ngoài hash; tình trạng DỮ LIỆU MỚI/CŨ, tập việc quá hạn, thay
            đổi trạng thái thư PHẢI nằm trong hash, nên chuyển sang CŨ được
            gửi cảnh báo đúng MỘT lần dù không có mail mới.
            Khóa đã gửi lưu BỀN ở X0 C9 @NHIP.DAUGUI, ghi SAU khi kênh báo
            xác nhận; trùng khóa bản đã gửi TRỌN VẸN thì bỏ qua; có mail mới
            thì khóa đổi, bản sau trong ngày gửi bình thường; chạy lại sau
            lần lỗi là hợp lệ. Tên file digest mang ngày GIỜ chạy, không ghi
            đè bản đã phát hành
ĐÍNH KÈM    đính kèm nằm ở staging từ bước 1; bước 2 chép về chỗ xếp, tính
            sha256, trỏ vào cột Đính kèm của THU, rồi mới được
            append COMMITTED; "đã nạp" nghĩa là CÓ sự kiện COMMITTED, không có
            cách đánh dấu nào khác. Hai file cùng tên cùng ngày phân biệt bằng
            sha, không được bỏ bản sau; chép hụt thì KHÔNG COMMITTED, ghi VIEC
            kèm lý do, lượt nạp giữ trạng thái dở dang chờ chạy lại bước 2
GỬI KÈM FILE thư mình gửi đi có đính kèm bản làm việc: file đó thành ẢNH CHỤP
            ĐÃ GỬI DUYỆT theo X5; thư phản hồi chỉ nâng thành ĐÃ DUYỆT NỘI BỘ
            khi có câu xác nhận rõ, không suy từ im lặng
AN TOÀN     token và bí mật của kênh báo (Telegram...) để NGOÀI kho đồng bộ,
            script đọc từ chỗ hệ điều hành giữ bí mật; digest sinh lỗi thì tuyệt
            đối không gửi lại bản cũ, báo lỗi thay vì báo DONE
```

# 2. Luật bổ sung

```
TRẢ LỜI     nội dung người gửi viết XEN TRONG phần trích dẫn (trả lời inline,
INLINE      "[xem trả lời bên dưới từng mục]") vẫn tính là PHẦN NGƯỜI GỬI VỪA
            VIẾT khi xét năm điều CHỜ TÔI; chỉ phần trích dẫn nguyên văn không
            có chữ mới mới bị cắt
ĐÍNH KÈM    đính kèm vượt trần @NHIP.TRANDINHKEM (X0 C9): KHÔNG kéo vào
QUÁ LỚN     staging hay kho đồng bộ; ghi dòng TAILIEU trỏ nguồn (link, mã thư)
            kèm sha256 nếu lấy được, mở VIEC "tải tay" cho người dùng; mail đó
            vẫn COMMITTED với ghi chú đính kèm để ngoài
STAGING     thư mục trong _thu_staging không có khóa nào trong nhật ký (crash
MỒ CÔI      giữa lưu staging và append PREPARED): rà thấy thì báo, người dùng
            duyệt rồi mới xóa (mức B); không tự coi là rác
```
