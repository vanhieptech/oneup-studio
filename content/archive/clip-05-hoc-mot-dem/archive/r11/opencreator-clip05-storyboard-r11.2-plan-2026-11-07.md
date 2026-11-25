---
title: "Clip05 r11.2 — storyboard FILE KẾ HOẠCH"
date: 2026-11-07
type: storyboard-plan
status: draft-planning-only-no-images
source: opencreator-clip05-spec-r11.2-draft-2026-11-07.json
tags: [clip05, storyboard, planning-only]
---

Không phải storyboardPNG/contactsheet đã render/kiểm mắt. Mọi tọa độ là dự kiến1080×1920, x/y/w/h. BVP local, logo05-pair-plus xuyênsuốt. Không assets mới/doodle/ảnhAI. Giâyước chưa voice.

Safe-zone chữ/hero x60–1020,y150–1460. Caption plate [80,1490,920,280]; logo[60,80,100,70]. Không prop/body quantrọng xuốngcaption. Kiểm va chạm chínhthức chưa chạy. Mỗi EN chunk là segment riêng không chồng, chưa timing.

| Beat / timeước | Frame đầu→giữa→cuối / reveal | BBoxdựkiến | Lời/ENđồngbộ | Cầnkiểm |
|---|---|---|---|---|
| b01 [0, 6.67] | Đầu sách mở/frame0hookEN; giữa cutmặt0.8s; cuối trởlạisách2s. ChưaFood/Rent. | hero/book[170,770,740,530]; chibi face[650,260,290,330]; bubble[100,180,530,400] | Copy nguyên text/captions từJSON b01; khônggõlạichữ | Đầu/giữa/cuốikhôngche/cắtvật; font/contrast; speechcues CHƯA KIỂM |
| b02 [6.67, 11.67] | Đầu giữsách; giữa panelReading as lifestyle; cuối panelcùngsách/khôngphe. | hero/book[170,770,740,530]; chibi face[650,260,290,330]; bubble[100,180,530,400] | Copy nguyên text/captions từJSON b02; khônggõlạichữ | Đầu/giữa/cuốikhôngche/cắtvật; font/contrast; speechcues CHƯA KIỂM |
| b03 [11.67, 17.5] | Đầu10thẻngang; giữa2thẻdi chuyển; cuối2nhómutility. Khôngđánhmức8thẻcònlại. | diagram[90,320,900,1000]; headers[100,230,880,80]; noface/nobubble | Copy nguyên text/captions từJSON b03; khônggõlạichữ | Đầu/giữa/cuốikhôngche/cắtvật; font/contrast; speechcues CHƯA KIỂM |
| b04 [17.5, 20.56] | Đầumặttò mò; giữtrangsách; cuối taychuẩnbịchứchưađóng. | hero/book[170,770,740,530]; chibi face[650,260,290,330]; bubble[100,180,530,400] | Copy nguyên text/captions từJSON b04; khônggõlạichữ | Đầu/giữa/cuốikhôngche/cắtvật; font/contrast; speechcues CHƯA KIỂM |
| b05 [20.56, 28.34] | Đầubìakhép; giữphầnkểFoodtrongbubble; cuối mởtrang nhưng chưa revealRent trước b06. | hero/book[170,770,740,530]; chibi face[650,260,290,330]; bubble[100,180,530,400] | Copy nguyên text/captions từJSON b05; khônggõlạichữ | Đầu/giữa/cuốikhôngche/cắtvật; font/contrast; speechcues CHƯA KIỂM |
| b06 [28.34, 35.84] | Đầuhai cột; giữa đúngtiềnthuênhà mớihiệnRentnguồn; cuối đúngbổsung mới thêmRentvàophầnkể. | diagram[90,320,900,1000]; headers[100,230,880,80]; noface/nobubble | Copy nguyên text/captions từJSON b06; khônggõlạichữ | Đầu/giữa/cuốikhôngche/cắtvật; font/contrast; speechcues CHƯA KIỂM |
| b07 [35.84, 41.67] | ĐầuvềThầy; giữa commentComplete/Missing; cuối khungdịchđểloophook, khôngcuttrước hếtlời. | chibi face[650,250,290,330]; comment[120,700,780,500]; book[100,1190,600,220] | Copy nguyên text/captions từJSON b07; khônggõlạichữ | Đầu/giữa/cuốikhôngche/cắtvật; font/contrast; speechcues CHƯA KIỂM |

## Nguồn trang giả định (không phải chứng cứ hay lời khuyên tài chính)

Cùng cuốn sách mock từhook. Trang nguồn minh họa có hai dòng EN “Record food expenses” và “Record rent”; phần tựkể ban đầu chỉ “Food expenses”. Khi đốichiếu mới lộ “Rent”, rồi bổsung. Nhãn “Editorial illustration” trên panel; không logo/tácgiảHTB trên cuốnmock. Không giả trang nguồn là trích nguyênvăn cẩm nang. Đây chỉ là payloadhưcấu giúp nhìn thấy thao tácF5, không khẳng định cách ghi chitiêu này tốiưu.

## Cover riêng, không lấy framevideo

{
  "direction": "a",
  "theme": "dark",
  "series": "Read + Learn",
  "ep": "05",
  "hero": [
    "REREAD",
    "SELF-TEST"
  ],
  "strike": 0,
  "accent": 1,
  "expression": "confused",
  "action": "thinking",
  "emote": "question",
  "tilt": -5,
  "template": "video-engine/src/composition/Cover.tsx",
  "rendered": false,
  "note": "EN hero2words. Vocabulary planned; schema compatibility unvalidated. No frame-grab. No doodle strike animation; template old/new design only."
}

TemplateA slots dựkiến: series/ep[100,290,880,150]; old/newhero[100,500,880,300]; chibi[400,850,560,650]; logo cósẵn. Không tựsửa template. Coverkhôngảnh; chưakiểmtrafields expression/action cóđúngschema. TikTok coverriêng; bảnReels/Shorts/Threads khungđầu cover≤0.5s chỉsaukhidựngđượcduyệt.

## Endcard

Ước[41.67, 44.67]; các dòng safety/credit/license copy từspec; bbox[70,250,940,1120]. Chưađođộđọc, khôngbáo3sđủ. Fullcredit cũngphảicópost. Bấtkỳkéođộdài nào phải phục vụđọcchứkhôngpaddingđạttrầngiây.

## Gate trước sảnxuất

- Phải cóReviewer/Deep/Social kiểm đúngfilemới, đọcto/ngườilạ, HiệpChốt đúngversion.
- Phải chuyển specplanning sang schemaengine, timing theo giọng, mỗi cảnh≤8s; không cho planningJSON này vào build.
- Chỉsauquyềnrender mới cóstill/contactsheet và2vòngkiểmmắt; hiệnchưalàm.
- Không tạo nétvẽdoodle; propsbook/sheet/pen/words/sign sẵncó, không nhânvậtgiả/stock/ngườithật.
