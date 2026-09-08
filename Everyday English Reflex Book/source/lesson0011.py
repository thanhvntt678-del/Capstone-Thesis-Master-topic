# -*- coding: utf-8 -*-
LESSON_0011 = {
    'lesson_id': '0011',
    'cefr': 'A0 / Pre-A1',
    'domain': 'Transport',
    'en_title': 'Recognising and Responding to the First Practical Exchange About Taxi & Ride Services',
    'vi_title': 'Giao tiếp nền tảng: taxi & ride services — the first practical exchange about taxi & ride services',
    'intro_en': (
        "Mr Henry is a taxi driver whom Ms Lan books regularly. Across many everyday moments -- a "
        "phone booking, an app request, confirming the pickup, the arrival time, getting in, giving the "
        "destination, the fare, a receipt, a shared ride, splitting the fare, a chosen route, traffic, "
        "a quick stop, paying by card, a cancelled ride, rebooking, surge pricing, a late-night ride, an "
        "airport pickup, waiting a few minutes, a new address, a rating, a forgotten umbrella, booking "
        "for a colleague, a child seat, luggage space, a late driver, a quieter ride, confirming the "
        "car, a promo code, a bigger car for a group, a tip, a rainy day, and finally becoming a regular "
        "passenger -- Lan repeatedly needs a taxi or ride service, and Henry responds and helps "
        "naturally each time."
    ),
    'intro_vi': (
        "Anh Henry là tài xế taxi mà chị Lan thường xuyên đặt xe. Qua nhiều khoảnh khắc đời thường -- "
        "một cuộc gọi đặt xe, một yêu cầu qua ứng dụng, xác nhận điểm đón, thời gian đến, lên xe, cho "
        "biết điểm đến, giá cước, một hóa đơn, một chuyến đi chung, chia tiền cước, một tuyến đường "
        "được chọn, kẹt xe, một điểm dừng nhanh, thanh toán bằng thẻ, một chuyến đi bị hủy, đặt lại "
        "chuyến, giá tăng theo giờ cao điểm, một chuyến đi khuya, đón ở sân bay, đợi vài phút, một địa "
        "chỉ mới, một lượt đánh giá, một chiếc ô bị bỏ quên, đặt xe giúp đồng nghiệp, ghế cho trẻ em, "
        "chỗ để hành lý, tài xế đến trễ, một chuyến đi yên tĩnh hơn, xác nhận xe, một mã giảm giá, một "
        "chiếc xe lớn hơn cho nhóm, tiền boa, một ngày mưa, và cuối cùng trở thành khách quen -- chị Lan "
        "liên tục cần một chuyến taxi hoặc dịch vụ đặt xe, và anh Henry luôn đáp lại và giúp đỡ một "
        "cách tự nhiên."
    ),
    'turns': [
        # 1 phone booking
        ("Ms Lan", "Hello, Henry. Could you pick me up in ten minutes?", "Chào anh Henry. Anh đón tôi trong mười phút nữa được không?"),
        ("Mr Henry", "Of course, Lan. I will be right there.", "Được chứ, chị Lan. Tôi đến ngay đây."),
        ("Ms Lan", "Thank you, that means a lot right now.", "Cảm ơn anh, giờ tôi cần lắm đấy."),
        # 2 app request
        ("Mr Henry", "Lan, I saw your ride request on the app.", "Chị Lan, tôi thấy yêu cầu đặt xe của chị trên ứng dụng."),
        ("Ms Lan", "Yes, that is me. Thank you for accepting.", "Vâng, đúng là tôi đấy. Cảm ơn anh đã nhận chuyến."),
        ("Mr Henry", "My pleasure, see you soon.", "Không có gì, hẹn gặp chị sớm nhé."),
        # 3 pickup location
        ("Ms Lan", "Henry, are you outside my building now?", "Anh Henry, anh đang ở ngoài tòa nhà của tôi rồi à?"),
        ("Mr Henry", "Yes, I am parked right at the entrance.", "Vâng, tôi đang đậu ngay lối vào đấy."),
        ("Ms Lan", "Perfect, I am coming down now.", "Tuyệt, tôi xuống ngay đây."),
        # 4 arrival time
        ("Mr Henry", "Lan, I should arrive in about five minutes.", "Chị Lan, khoảng năm phút nữa tôi sẽ đến."),
        ("Ms Lan", "Thank you, that works well for me.", "Cảm ơn anh, vậy hợp với tôi lắm."),
        ("Mr Henry", "Great, see you shortly.", "Tốt, hẹn gặp chị lát nữa."),
        # 5 getting in
        ("Mr Henry", "Good morning, Lan. Please get in.", "Chào buổi sáng, chị Lan. Mời chị lên xe."),
        ("Ms Lan", "Good morning, Henry. Thank you.", "Chào buổi sáng, anh Henry. Cảm ơn anh."),
        ("Mr Henry", "Where would you like to go today?", "Hôm nay chị muốn đi đâu vậy?"),
        # 6 destination
        ("Ms Lan", "Henry, could you take me to the airport, please?", "Anh Henry, anh chở tôi ra sân bay được không?"),
        ("Mr Henry", "Of course, I know the fastest way there.", "Được chứ, tôi biết đường nhanh nhất đến đó."),
        ("Ms Lan", "That is great news, thank you.", "Tin tốt quá, cảm ơn anh."),
        # 7 fare
        ("Mr Henry", "Lan, the fare to the airport is about fifteen dollars.", "Chị Lan, giá cước ra sân bay khoảng mười lăm đô la."),
        ("Ms Lan", "That sounds reasonable, thank you.", "Vậy hợp lý đấy, cảm ơn anh."),
        ("Mr Henry", "I will start the meter now.", "Tôi bật đồng hồ tính tiền ngay đây."),
        # 8 receipt
        ("Ms Lan", "Henry, could I have a receipt at the end?", "Anh Henry, cuối chuyến cho tôi xin hóa đơn được không?"),
        ("Mr Henry", "Of course, I will print one for you.", "Được chứ, tôi sẽ in cho chị."),
        ("Ms Lan", "That sounds fair, thank you.", "Nghe hợp lý đấy, cảm ơn anh."),
        # 9 shared ride
        ("Mr Henry", "Lan, would you mind sharing this ride with another passenger?", "Chị Lan, chị có phiền đi chung chuyến này với khách khác không?"),
        ("Ms Lan", "Not at all, that is fine with me.", "Không phiền đâu, được mà."),
        ("Mr Henry", "Glad that works for you.", "Tôi mừng vì hợp với chị."),
        # 10 splitting fare
        ("Ms Lan", "Henry, could we split the fare between us?", "Anh Henry, mình chia tiền cước được không?"),
        ("Mr Henry", "Of course, I can divide it on the app.", "Được chứ, tôi chia trên ứng dụng cho."),
        ("Ms Lan", "That sounds good, thank you.", "Nghe ổn đấy, cảm ơn anh."),
        # 11 route
        ("Mr Henry", "Lan, would you like me to take the highway?", "Chị Lan, chị có muốn tôi đi đường cao tốc không?"),
        ("Ms Lan", "Yes, please. That should be faster.", "Có chứ, vậy sẽ nhanh hơn."),
        ("Mr Henry", "Good choice, less traffic that way.", "Chọn hay đấy, đường đó ít kẹt xe hơn."),
        # 12 traffic
        ("Ms Lan", "Henry, is the traffic bad today?", "Anh Henry, hôm nay kẹt xe lắm không?"),
        ("Mr Henry", "Yes, a little heavier than usual.", "Có, hơi đông hơn bình thường một chút."),
        ("Ms Lan", "No worries, we still have time.", "Không sao đâu, mình vẫn còn thời gian."),
        # 13 quick stop
        ("Ms Lan", "Henry, could we stop at the pharmacy for a moment?", "Anh Henry, mình ghé hiệu thuốc một lát được không?"),
        ("Mr Henry", "Sure, that is not a problem.", "Được chứ, không vấn đề gì đâu."),
        ("Ms Lan", "Thank you, I will hurry back.", "Cảm ơn anh, tôi sẽ quay lại nhanh."),
        # 14 paying by card
        ("Mr Henry", "Lan, would you like to pay by card today?", "Chị Lan, hôm nay chị muốn trả bằng thẻ không?"),
        ("Ms Lan", "Yes, please. That is easier for me.", "Có chứ, vậy tiện cho tôi hơn."),
        ("Mr Henry", "No problem, just tap here.", "Được thôi, chị chạm vào đây."),
        # 15 cancelling
        ("Ms Lan", "Henry, I am sorry, but I need to cancel this ride.", "Anh Henry, tôi xin lỗi, nhưng tôi cần hủy chuyến này."),
        ("Mr Henry", "That is fine, Lan. No trouble at all.", "Không sao đâu, chị Lan. Không phiền gì cả."),
        ("Ms Lan", "Thank you for understanding, Henry.", "Cảm ơn anh đã thông cảm, anh Henry."),
        # 16 rebooking
        ("Mr Henry", "Lan, would you like to rebook for later today?", "Chị Lan, chị có muốn đặt lại chuyến vào lát nữa không?"),
        ("Ms Lan", "Yes, please. Around six o'clock.", "Có chứ, khoảng sáu giờ nhé."),
        ("Mr Henry", "Perfect, I will see you then.", "Tuyệt, hẹn gặp chị lúc đó."),
        # 17 surge pricing
        ("Ms Lan", "Henry, is the price higher right now?", "Anh Henry, giờ giá cao hơn à?"),
        ("Mr Henry", "Yes, it is a busy time of day.", "Vâng, giờ này đang cao điểm."),
        ("Ms Lan", "I understand, thank you for telling me.", "Tôi hiểu rồi, cảm ơn anh đã cho biết."),
        # 18 late-night ride
        ("Mr Henry", "Lan, are you sure you want a ride this late?", "Chị Lan, chị chắc là muốn đi xe muộn thế này chứ?"),
        ("Ms Lan", "Yes, I need to get home safely.", "Vâng, tôi cần về nhà an toàn."),
        ("Mr Henry", "Of course, I will drive carefully.", "Được chứ, tôi sẽ lái cẩn thận."),
        # 19 airport pickup
        ("Ms Lan", "Henry, could you pick me up from the airport tomorrow?", "Anh Henry, mai anh đón tôi ở sân bay được không?"),
        ("Mr Henry", "Of course, just send me your flight number.", "Được chứ, chị gửi tôi số chuyến bay nhé."),
        ("Ms Lan", "Thank you, I will do that now.", "Cảm ơn anh, tôi gửi ngay đây."),
        # 20 asking to wait
        ("Ms Lan", "Henry, could you wait a few minutes for me?", "Anh Henry, anh đợi tôi vài phút được không?"),
        ("Mr Henry", "Sure, take your time.", "Được chứ, chị cứ từ từ."),
        ("Ms Lan", "Thank you, I will not be long.", "Cảm ơn anh, tôi sẽ không lâu đâu."),
        # 21 new address
        ("Mr Henry", "Lan, I do not recognise this address.", "Chị Lan, tôi không quen địa chỉ này."),
        ("Ms Lan", "Let me send you the exact location.", "Để tôi gửi vị trí chính xác cho anh."),
        ("Mr Henry", "Thank you, that will help.", "Cảm ơn chị, vậy sẽ giúp ích lắm."),
        # 22 rating
        ("Ms Lan", "Henry, thank you for a smooth ride today.", "Anh Henry, cảm ơn anh vì chuyến đi êm ả hôm nay."),
        ("Mr Henry", "You are welcome, I will give you a five star rating too.", "Không có gì, tôi cũng sẽ đánh giá năm sao cho chị."),
        ("Ms Lan", "Thank you, that is kind of you.", "Cảm ơn anh, anh tốt bụng quá."),
        # 23 forgotten umbrella
        ("Mr Henry", "Lan, I think you left your umbrella in the car.", "Chị Lan, hình như chị để quên ô trên xe rồi."),
        ("Ms Lan", "Oh no, thank you for noticing.", "Ôi không, cảm ơn anh đã để ý."),
        ("Mr Henry", "I will bring it back to you.", "Tôi sẽ mang trả lại cho chị."),
        # 24 booking for someone else
        ("Ms Lan", "Henry, could you pick up my colleague instead today?", "Anh Henry, hôm nay anh đón đồng nghiệp tôi thay được không?"),
        ("Mr Henry", "Of course, just send me the address.", "Được chứ, chị gửi địa chỉ cho tôi nhé."),
        ("Ms Lan", "Thank you, that is very helpful of you.", "Cảm ơn anh, anh giúp ích nhiều lắm."),
        # 25 child seat
        ("Ms Lan", "Henry, do you have a child seat available?", "Anh Henry, anh có ghế cho trẻ em không?"),
        ("Mr Henry", "Yes, I can bring one for you.", "Có chứ, tôi mang một cái cho chị."),
        ("Ms Lan", "Thank you, that is very helpful.", "Cảm ơn anh, vậy hữu ích lắm."),
        # 26 luggage
        ("Ms Lan", "Henry, is there enough space for two suitcases?", "Anh Henry, đủ chỗ cho hai cái vali không?"),
        ("Mr Henry", "Yes, the trunk is quite large.", "Đủ chứ, cốp xe khá rộng."),
        ("Ms Lan", "That works out well, thank you.", "Vậy ổn quá, cảm ơn anh."),
        # 27 driver late
        ("Mr Henry", "Lan, I am sorry, I will be a few minutes late.", "Chị Lan, tôi xin lỗi, tôi sẽ đến trễ vài phút."),
        ("Ms Lan", "That is okay, thank you for letting me know.", "Không sao đâu, cảm ơn anh đã báo trước."),
        ("Mr Henry", "Thank you for your patience, Lan.", "Cảm ơn chị đã kiên nhẫn, chị Lan."),
        # 28 quieter ride
        ("Ms Lan", "Henry, would you mind turning the music down a little?", "Anh Henry, anh vặn nhỏ nhạc lại một chút được không?"),
        ("Mr Henry", "Sure, I do not mind at all.", "Được chứ, tôi không phiền đâu."),
        ("Ms Lan", "Thank you, I need to make a call.", "Cảm ơn anh, tôi cần gọi điện thoại."),
        # 29 confirming car
        ("Mr Henry", "Lan, I am driving a white car today.", "Chị Lan, hôm nay tôi lái xe màu trắng."),
        ("Ms Lan", "Thank you, I will look out for it.", "Cảm ơn anh, tôi sẽ để ý tìm."),
        ("Mr Henry", "See you in a moment.", "Hẹn gặp chị chút nữa."),
        # 30 promo code
        ("Ms Lan", "Henry, does this promo code work on the app?", "Anh Henry, mã giảm giá này dùng được trên ứng dụng không?"),
        ("Mr Henry", "Yes, it should apply automatically.", "Có chứ, nó sẽ tự động áp dụng."),
        ("Ms Lan", "Great, thank you for checking.", "Tuyệt, cảm ơn anh đã kiểm tra."),
        # 31 bigger car
        ("Ms Lan", "Henry, do you have a bigger car for four people?", "Anh Henry, anh có xe lớn hơn cho bốn người không?"),
        ("Mr Henry", "Yes, I can arrange one for you.", "Có chứ, tôi sắp xếp cho chị."),
        ("Ms Lan", "That is very reassuring, thank you.", "Vậy tôi yên tâm hơn nhiều, cảm ơn anh."),
        # 32 tipping
        ("Ms Lan", "Henry, please keep the change as a tip.", "Anh Henry, anh giữ tiền thối làm tiền boa nhé."),
        ("Mr Henry", "Thank you so much, Lan. That is very generous.", "Cảm ơn chị nhiều lắm. Chị hào phóng quá."),
        ("Ms Lan", "You are welcome, you drove very well.", "Không có gì, anh lái xe rất tốt."),
        # 33 rainy day
        ("Mr Henry", "Lan, prices are a bit higher because of the rain.", "Chị Lan, giá hơi cao hơn vì trời mưa."),
        ("Ms Lan", "That makes sense, thank you for explaining.", "Vậy hợp lý mà, cảm ơn anh đã giải thích."),
        ("Mr Henry", "I appreciate your understanding, Lan.", "Cảm ơn chị đã thông cảm, chị Lan."),
        # 34 regular customer
        ("Mr Henry", "Lan, you are one of my favourite regular passengers.", "Chị Lan, chị là một trong những khách quen tôi thích nhất."),
        ("Ms Lan", "Thank you, Henry. You are always so reliable.", "Cảm ơn anh, anh Henry. Anh lúc nào cũng đáng tin cậy."),
        ("Mr Henry", "I look forward to our next ride.", "Tôi mong đến chuyến đi tiếp theo của mình."),
        ("Ms Lan", "Me too, see you soon.", "Tôi cũng vậy, hẹn gặp lại sớm."),
        # 35 asking about payment methods
        ("Ms Lan", "Henry, do you accept mobile payment too?", "Anh Henry, anh có nhận thanh toán qua điện thoại không?"),
        ("Mr Henry", "Yes, most apps work fine with me.", "Có chứ, hầu hết ứng dụng đều dùng được."),
        ("Ms Lan", "Great, I will use that this time.", "Tuyệt, lần này tôi sẽ dùng cách đó."),
        # 36 window down
        ("Mr Henry", "Lan, would you like the window open?", "Chị Lan, chị có muốn mở cửa sổ không?"),
        ("Ms Lan", "Yes, please. It is a bit warm in here.", "Có chứ, trong này hơi nóng."),
        ("Mr Henry", "No problem, I will open it now.", "Không sao đâu, tôi mở ngay đây."),
        # 37 recommending a route change
        ("Ms Lan", "Henry, is there a shorter way through downtown?", "Anh Henry, có đường ngắn hơn qua trung tâm không?"),
        ("Mr Henry", "Yes, I know a quieter side street.", "Có chứ, tôi biết một con đường nhỏ vắng hơn."),
        ("Ms Lan", "Let us try that way then.", "Vậy mình đi đường đó nhé."),
        # 38 asking about parking at destination
        ("Ms Lan", "Henry, is there somewhere to stop right outside?", "Anh Henry, có chỗ dừng ngay trước cửa không?"),
        ("Mr Henry", "Yes, there is space just by the entrance.", "Có chứ, có chỗ ngay cạnh lối vào."),
        ("Ms Lan", "Wonderful, that saves us a walk.", "Tuyệt vời, vậy đỡ phải đi bộ."),
    ],
}
