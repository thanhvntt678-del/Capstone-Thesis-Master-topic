# -*- coding: utf-8 -*-
LESSON_0101 = {
    'lesson_id': '0101',
    'cefr': 'A0 / Pre-A1',
    'domain': 'Transport',
    'en_title': 'Recognising and Responding to a Misunderstanding or Problem Involving Taxi & Ride Services',
    'vi_title': 'Giao tiếp nền tảng: taxi & ride services — a misunderstanding or problem involving taxi & ride services',
    'intro_en': (
        "Ms Lan and Mr Desmond are colleagues who often share rides and run into small misunderstandings "
        "and problems with taxis and ride-hailing apps. Across many everyday moments -- a driver heading "
        "to the wrong address, the app showing the wrong pickup point, a fare higher than the quoted "
        "price, a driver taking a much longer route, the wrong car being matched to a ride, a driver "
        "cancelling at the last minute, a long wait with no driver assigned, a payment method failing in "
        "the app, a mistaken destination entered by accident, a driver not recognising the pickup spot, a "
        "shared-ride mix-up with another passenger, luggage space being too small, an unexpected surge "
        "price, the wrong number of passengers being allowed, a driver arriving at the wrong entrance, GPS "
        "leading to the wrong building, a tip amount charged incorrectly, a promo code not being applied, "
        "a car seat request not being fulfilled, a driver running late without any notice, the wrong car "
        "colour or model shown in the app, a ride being cancelled after the driver was already near, being "
        "matched with a driver who is too far away, confusion over which exit to meet the driver at, a "
        "driver asking for cash when the app says card, a receipt not being sent after the ride, a "
        "misunderstanding about how many stops are allowed, a driver taking a phone call in a way that "
        "feels distracting, a mismatched name on the app, the wrong drop-off point being selected, a "
        "driver unfamiliar with the area causing a detour, a rating-system issue after a bad experience, "
        "the air conditioning not working during the ride, the app crashing mid-booking, a misunderstanding "
        "about splitting the fare, explaining why staying polite during a ride problem matters, and "
        "finally why clear communication with a driver matters so much for everyday conversation -- one of "
        "them explains a misunderstanding or problem, and the other responds helpfully each time."
    ),
    'intro_vi': (
        "Chị Lan và anh Desmond là đồng nghiệp, thường đi chung xe và gặp những hiểu lầm hay vấn đề nhỏ "
        "với taxi và ứng dụng đặt xe. Qua nhiều khoảnh khắc đời thường -- tài xế chạy tới sai địa chỉ, "
        "ứng dụng hiện sai điểm đón, giá cước cao hơn báo giá, tài xế chạy đường vòng xa hơn nhiều, xe "
        "ghép nhầm cho chuyến đi, tài xế hủy chuyến vào phút chót, chờ lâu mà chưa có tài xế nhận, phương "
        "thức thanh toán bị lỗi trên ứng dụng, nhập nhầm điểm đến, tài xế không nhận ra điểm đón, nhầm "
        "lẫn với hành khách khác trong chuyến đi ghép, khoang hành lý quá nhỏ, giá cước tăng đột ngột, "
        "sai số lượng hành khách được phép, tài xế tới sai cổng, GPS dẫn tới sai tòa nhà, tiền tip bị "
        "tính sai, mã giảm giá không được áp dụng, yêu cầu ghế trẻ em không được đáp ứng, tài xế trễ mà "
        "không báo trước, sai màu hoặc đời xe hiện trên ứng dụng, chuyến đi bị hủy khi tài xế đã gần tới, "
        "được ghép với tài xế ở quá xa, nhầm lẫn về cổng nào để gặp tài xế, tài xế đòi tiền mặt trong khi "
        "ứng dụng ghi thanh toán thẻ, không nhận được hóa đơn sau chuyến đi, hiểu lầm về số điểm dừng "
        "được phép, tài xế nghe điện thoại theo cách khiến người ngồi thấy mất tập trung, tên trên ứng "
        "dụng không khớp, chọn nhầm điểm trả khách, tài xế không quen khu vực khiến phải đi vòng, vấn đề "
        "về hệ thống đánh giá sau một trải nghiệm không tốt, điều hòa không hoạt động trong chuyến đi, "
        "ứng dụng bị treo giữa lúc đặt xe, hiểu lầm về việc chia tiền cước, giải thích vì sao giữ thái độ "
        "lịch sự khi có vấn đề trong chuyến đi lại quan trọng, và cuối cùng là vì sao giao tiếp rõ ràng "
        "với tài xế lại quan trọng đến vậy cho giao tiếp hằng ngày -- một người giải thích một hiểu lầm "
        "hoặc vấn đề, và người kia luôn đáp lại một cách giúp đỡ mỗi lần."
    ),
    'turns': [
        # 1 driver heading to wrong address
        ("Ms Lan", "Excuse me, I think the driver is heading to the wrong address.", "Xin lỗi, tôi nghĩ tài xế đang chạy tới sai địa chỉ."),
        ("Mr Desmond", "Let me message the driver and correct it right away.", "Để tôi nhắn cho tài xế và sửa lại ngay."),
        ("Ms Lan", "Thank you, I do not want to be late.", "Cảm ơn anh, tôi không muốn bị trễ."),
        # 2 app showing wrong pickup point
        ("Mr Desmond", "The app is showing the wrong pickup point for us.", "Ứng dụng đang hiện sai điểm đón của mình."),
        ("Ms Lan", "Let me drop a new pin at our real location.", "Để tôi cắm lại vị trí đúng trên bản đồ."),
        ("Mr Desmond", "Good, hopefully the driver sees it in time.", "Tốt, mong tài xế thấy kịp lúc."),
        # 3 fare higher than the quoted price
        ("Ms Lan", "This fare looks higher than the price we were quoted.", "Giá cước này có vẻ cao hơn báo giá ban đầu."),
        ("Mr Desmond", "Let me check the breakdown to see what changed.", "Để tôi xem chi tiết để biết cái gì đã thay đổi."),
        ("Ms Lan", "Ah, it seems traffic added an extra charge.", "À, hình như kẹt xe làm phát sinh thêm phí."),
        # 4 driver taking a longer route
        ("Mr Desmond", "I think our driver is taking a much longer route.", "Tôi nghĩ tài xế đang chạy đường vòng xa hơn nhiều."),
        ("Ms Lan", "Let me check the map and ask him about it politely.", "Để tôi xem bản đồ và hỏi anh ấy một cách lịch sự."),
        ("Mr Desmond", "There must be roadwork ahead, that explains it.", "Chắc là có đoạn đang sửa đường phía trước, vậy là hợp lý rồi."),
        # 5 wrong car matched to a ride
        ("Ms Lan", "This does not look like the car that was matched to us.", "Xe này có vẻ không phải xe được ghép cho mình."),
        ("Mr Desmond", "Let me check the plate number against the app.", "Để tôi kiểm tra biển số so với ứng dụng."),
        ("Ms Lan", "You are right, this is a different car entirely.", "Anh nói đúng, đây hoàn toàn là xe khác."),
        # 6 driver cancelling at the last minute
        ("Mr Desmond", "Our driver just cancelled on us at the last minute.", "Tài xế của mình vừa hủy chuyến vào phút chót."),
        ("Ms Lan", "That is frustrating, let me book another one now.", "Bực thật, để tôi đặt chuyến khác ngay."),
        ("Mr Desmond", "Thanks, I hope this one shows up on time.", "Cảm ơn chị, mong chuyến này tới đúng giờ."),
        # 7 long wait with no driver assigned
        ("Ms Lan", "We have been waiting a while with no driver assigned yet.", "Mình đã chờ khá lâu mà chưa có tài xế nhận chuyến."),
        ("Mr Desmond", "Let me try switching to a different service option.", "Để tôi thử đổi sang loại dịch vụ khác."),
        ("Ms Lan", "Good idea, that might get us a faster match.", "Ý hay, vậy có thể tìm được xe nhanh hơn."),
        # 8 payment method failing in the app
        ("Mr Desmond", "My payment method keeps failing in the app.", "Phương thức thanh toán của tôi cứ bị lỗi trên ứng dụng."),
        ("Ms Lan", "Let us try mine instead for this ride.", "Mình thử dùng thẻ của tôi cho chuyến này đi."),
        ("Mr Desmond", "Thanks, I will fix mine when we get home.", "Cảm ơn chị, tôi sẽ sửa lại khi về nhà."),
        # 9 mistaken destination entered
        ("Ms Lan", "I think I entered the wrong destination by mistake.", "Tôi nghĩ mình đã nhập nhầm điểm đến rồi."),
        ("Mr Desmond", "No problem, let us correct it before we start moving.", "Không sao, mình sửa lại trước khi xe chạy."),
        ("Ms Lan", "Thank you for catching that so quickly.", "Cảm ơn anh đã phát hiện nhanh vậy."),
        # 10 driver not recognising the pickup spot
        ("Mr Desmond", "The driver does not seem to recognise our pickup spot.", "Tài xế có vẻ không nhận ra điểm đón của mình."),
        ("Ms Lan", "Let me describe a nearby landmark to help him.", "Để tôi mô tả một địa điểm gần đó để giúp anh ấy."),
        ("Mr Desmond", "Good call, that should make it clear.", "Cách hay đấy, vậy chắc sẽ rõ hơn."),
        # 11 shared-ride mix-up with another passenger
        ("Ms Lan", "I think this shared ride has us mixed up with another passenger.", "Tôi nghĩ chuyến ghép này bị nhầm mình với hành khách khác."),
        ("Mr Desmond", "Let me confirm our names with the driver directly.", "Để tôi xác nhận tên của mình trực tiếp với tài xế."),
        ("Ms Lan", "Thank you, better to sort that out early.", "Cảm ơn anh, sửa sớm vẫn hơn."),
        # 12 luggage space too small
        ("Mr Desmond", "This car does not really have room for our luggage.", "Xe này không đủ chỗ cho hành lý của mình."),
        ("Ms Lan", "Let me ask if we can rearrange the back seat.", "Để tôi hỏi xem có thể sắp xếp lại ghế sau không."),
        ("Mr Desmond", "That worked, it all fits now.", "Được rồi, giờ vừa hết cả."),
        # 13 unexpected surge price
        ("Ms Lan", "The price suddenly went up right before we booked.", "Giá cước bỗng tăng ngay trước khi mình đặt xe."),
        ("Mr Desmond", "Let us wait a few minutes, it might settle down.", "Mình chờ vài phút xem, có thể giá sẽ hạ lại."),
        ("Ms Lan", "You are right, it dropped back to normal.", "Anh nói đúng, giá đã trở lại bình thường rồi."),
        # 14 wrong number of passengers allowed
        ("Mr Desmond", "This car type only allows fewer passengers than we have.", "Loại xe này chỉ cho phép ít hành khách hơn số người mình có."),
        ("Ms Lan", "Let me upgrade to a bigger car option.", "Để tôi nâng cấp lên loại xe lớn hơn."),
        ("Mr Desmond", "Thanks, that solves the problem for everyone.", "Cảm ơn chị, vậy là giải quyết được cho mọi người."),
        # 15 driver arriving at the wrong entrance
        ("Ms Lan", "The driver arrived at the wrong entrance of the building.", "Tài xế đã tới sai cổng của tòa nhà."),
        ("Mr Desmond", "Let me guide him to the correct side by message.", "Để tôi nhắn hướng dẫn anh ấy tới đúng phía."),
        ("Ms Lan", "Thank you, we should not keep him waiting.", "Cảm ơn anh, mình không nên để anh ấy chờ lâu."),
        # 16 GPS leading to the wrong building
        ("Mr Desmond", "The GPS seems to be leading us to the wrong building.", "GPS có vẻ đang dẫn mình tới sai tòa nhà."),
        ("Ms Lan", "Let me check the address again on my phone.", "Để tôi kiểm tra lại địa chỉ trên điện thoại."),
        ("Mr Desmond", "Ah, we typed the street number wrong earlier.", "À, mình đã gõ sai số nhà từ đầu."),
        # 17 tip amount charged incorrectly
        ("Ms Lan", "I think the tip amount was charged incorrectly.", "Tôi nghĩ tiền tip bị tính sai rồi."),
        ("Mr Desmond", "Let me check the receipt and report it.", "Để tôi kiểm tra hóa đơn và báo lại."),
        ("Ms Lan", "Thank you, that extra amount should not be there.", "Cảm ơn anh, khoản thừa đó không nên có."),
        # 18 promo code not applied
        ("Mr Desmond", "This promo code does not seem to have been applied.", "Mã giảm giá này có vẻ chưa được áp dụng."),
        ("Ms Lan", "Let me check if it was entered before booking.", "Để tôi kiểm tra xem đã nhập trước khi đặt xe chưa."),
        ("Mr Desmond", "Ah, I think I entered it one step too late.", "À, hình như tôi nhập trễ mất một bước rồi."),
        # 19 car seat request not fulfilled
        ("Ms Lan", "I requested a car seat, but the driver does not have one.", "Tôi đã yêu cầu ghế trẻ em, nhưng tài xế không có."),
        ("Mr Desmond", "Let me cancel and book a driver who has one.", "Để tôi hủy và đặt tài xế nào có sẵn ghế đó."),
        ("Ms Lan", "Thank you, that is important for our little one.", "Cảm ơn anh, việc đó quan trọng cho bé nhà mình."),
        # 20 driver running late without any notice
        ("Mr Desmond", "Our driver is running quite late without any notice.", "Tài xế của mình trễ khá lâu mà không báo gì."),
        ("Ms Lan", "Let me send a message asking for an update.", "Để tôi nhắn hỏi xem tình hình thế nào."),
        ("Mr Desmond", "Good, at least we will know what is happening.", "Tốt, ít ra mình sẽ biết chuyện gì đang xảy ra."),
        # 21 wrong car colour or model shown in the app
        ("Ms Lan", "The app showed a different car colour than what arrived.", "Ứng dụng hiện màu xe khác với xe tới thực tế."),
        ("Mr Desmond", "Let me double-check the plate to be sure it is right.", "Để tôi kiểm tra lại biển số cho chắc."),
        ("Ms Lan", "It matches, the colour must have just updated late.", "Khớp rồi, chắc màu xe chỉ cập nhật trễ thôi."),
        # 22 ride cancelled after the driver was already near
        ("Mr Desmond", "The ride got cancelled even though the driver was already close.", "Chuyến đi bị hủy dù tài xế đã gần tới rồi."),
        ("Ms Lan", "That is odd, let me try booking again right away.", "Lạ thật, để tôi thử đặt lại ngay."),
        ("Mr Desmond", "Thanks, hopefully the next one goes smoothly.", "Cảm ơn chị, mong chuyến sau suôn sẻ hơn."),
        # 23 matched with a driver too far away
        ("Ms Lan", "We were matched with a driver who is quite far away.", "Mình được ghép với tài xế ở khá xa."),
        ("Mr Desmond", "Let me cancel and search again for someone closer.", "Để tôi hủy và tìm lại tài xế gần hơn."),
        ("Ms Lan", "Good thinking, that should save us some time.", "Nghĩ hay đấy, vậy sẽ tiết kiệm thời gian hơn."),
        # 24 confusion over which exit to meet the driver
        ("Mr Desmond", "I am not sure which exit we are meant to meet the driver at.", "Tôi không chắc mình phải gặp tài xế ở lối ra nào."),
        ("Ms Lan", "Let me call him to confirm the exact spot.", "Để tôi gọi anh ấy để xác nhận đúng chỗ."),
        ("Mr Desmond", "Thanks, that clears up the confusion.", "Cảm ơn chị, vậy hết nhầm lẫn rồi."),
        # 25 driver asking for cash when app says card
        ("Ms Lan", "The driver is asking for cash, but the app says card only.", "Tài xế đang đòi tiền mặt, nhưng ứng dụng ghi chỉ nhận thẻ."),
        ("Mr Desmond", "Let me show him the payment screen to clarify.", "Để tôi cho anh ấy xem màn hình thanh toán để làm rõ."),
        ("Ms Lan", "Thank you, that should settle the confusion.", "Cảm ơn anh, vậy sẽ giải quyết được nhầm lẫn."),
        # 26 receipt not sent after the ride
        ("Mr Desmond", "I never received a receipt after that last ride.", "Tôi chưa nhận được hóa đơn sau chuyến đi vừa rồi."),
        ("Ms Lan", "Let me check your email for it, it might be delayed.", "Để tôi kiểm tra email của anh xem, có thể bị chậm thôi."),
        ("Mr Desmond", "Found it, it just arrived a bit late.", "Tìm thấy rồi, nó tới hơi trễ thôi."),
        # 27 misunderstanding about how many stops are allowed
        ("Ms Lan", "I thought we could add an extra stop, but the app says otherwise.", "Tôi tưởng mình có thể thêm điểm dừng, nhưng ứng dụng ghi khác."),
        ("Mr Desmond", "Let me check the ride settings for that option.", "Để tôi kiểm tra cài đặt chuyến đi xem có tùy chọn đó không."),
        ("Ms Lan", "Ah, we need to book it as a separate feature.", "À, mình cần đặt riêng tính năng đó."),
        # 28 driver taking a phone call in a distracting way
        ("Mr Desmond", "I am a little uneasy that the driver is on his phone while driving.", "Tôi hơi lo vì tài xế đang nghe điện thoại lúc lái xe."),
        ("Ms Lan", "Let me kindly ask him to focus on the road.", "Để tôi nhẹ nhàng nhờ anh ấy tập trung lái xe."),
        ("Mr Desmond", "Thank you, safety matters more than anything else.", "Cảm ơn chị, an toàn quan trọng hơn hết."),
        # 29 mismatched name on the app
        ("Ms Lan", "The name on the app does not match the driver in front of us.", "Tên trên ứng dụng không khớp với tài xế trước mặt mình."),
        ("Mr Desmond", "Let me double-check his ID before we get in.", "Để tôi kiểm tra lại giấy tờ của anh ấy trước khi lên xe."),
        ("Ms Lan", "Good idea, it is always safer to confirm first.", "Ý hay, xác nhận trước vẫn an toàn hơn."),
        # 30 wrong drop-off point selected
        ("Mr Desmond", "I think we selected the wrong drop-off point by mistake.", "Tôi nghĩ mình chọn nhầm điểm trả khách rồi."),
        ("Ms Lan", "Let me update it before we get too close.", "Để tôi cập nhật lại trước khi tới gần điểm đó."),
        ("Mr Desmond", "Thanks, good thing we noticed in time.", "Cảm ơn chị, may là mình nhận ra kịp lúc."),
        # 31 driver unfamiliar with the area causing a detour
        ("Ms Lan", "The driver does not seem familiar with this area at all.", "Tài xế có vẻ không quen khu vực này chút nào."),
        ("Mr Desmond", "Let me guide him with directions from my phone.", "Để tôi hướng dẫn đường bằng điện thoại của tôi."),
        ("Ms Lan", "Thank you, that should get us back on track.", "Cảm ơn anh, vậy sẽ giúp đi đúng đường lại."),
        # 32 rating-system issue after a bad experience
        ("Mr Desmond", "I tried to leave feedback about that ride, but the rating did not save.", "Tôi thử để lại đánh giá cho chuyến đó, nhưng điểm không lưu được."),
        ("Ms Lan", "Let me report that through the help section for you.", "Để tôi báo lỗi đó qua mục trợ giúp giúp anh."),
        ("Mr Desmond", "Thank you, I really wanted that feedback recorded.", "Cảm ơn chị, tôi thật sự muốn đánh giá đó được ghi lại."),
        # 33 air conditioning not working during the ride
        ("Ms Lan", "The air conditioning does not seem to be working in here.", "Điều hòa có vẻ không hoạt động trong xe này."),
        ("Mr Desmond", "Let me ask the driver to check the settings.", "Để tôi nhờ tài xế kiểm tra lại cài đặt."),
        ("Ms Lan", "Better already, thank you for asking him.", "Đỡ hơn rồi, cảm ơn anh đã hỏi giúp."),
        # 34 app crashing mid-booking
        ("Mr Desmond", "The app just crashed while I was booking our ride.", "Ứng dụng vừa bị treo lúc tôi đang đặt xe."),
        ("Ms Lan", "Let me restart it and try booking again.", "Để tôi khởi động lại và thử đặt lần nữa."),
        ("Mr Desmond", "Thanks, it went through fine this time.", "Cảm ơn chị, lần này thì được rồi."),
        # 35 misunderstanding about splitting the fare
        ("Ms Lan", "I thought the fare would split evenly, but it did not.", "Tôi tưởng tiền cước sẽ chia đều, nhưng lại không phải vậy."),
        ("Mr Desmond", "Let me check the split settings before we finish paying.", "Để tôi kiểm tra cài đặt chia tiền trước khi thanh toán xong."),
        ("Ms Lan", "Ah, I see, we needed to select it manually.", "À, ra là vậy, mình cần chọn thủ công."),
        # 36 explaining why staying polite during a ride problem matters
        ("Mr Desmond", "Why does staying polite during a ride problem matter so much?", "Vì sao giữ thái độ lịch sự khi có vấn đề trong chuyến đi lại quan trọng vậy?"),
        ("Ms Lan", "It keeps things calm so the driver can actually help us.", "Nó giúp mọi thứ bình tĩnh để tài xế có thể thật sự giúp mình."),
        ("Mr Desmond", "That makes sense, I will remember that next time.", "Nghe hợp lý đấy, tôi sẽ nhớ điều đó cho lần sau."),
    ],
}
