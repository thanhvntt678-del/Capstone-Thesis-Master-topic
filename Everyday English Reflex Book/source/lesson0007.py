# -*- coding: utf-8 -*-
LESSON_0007 = {
    'lesson_id': '0007',
    'cefr': 'A0 / Pre-A1',
    'domain': 'Shopping',
    'en_title': 'Recognising and Responding to the First Practical Exchange About Shopping & Payments',
    'vi_title': 'Giao tiếp nền tảng: shopping & payments — the first practical exchange about shopping & payments',
    'intro_en': (
        "Ms Lan is a regular customer at Mr Thomas's small shop. Across many everyday moments -- "
        "paying for bread, choosing a size, asking the price, paying by card, getting change, asking "
        "for a receipt, a faded price tag, buying in bulk, a discount coupon, opening hours, packing "
        "bags, weighing fruit, buying a gift, choosing between two items, a return policy, a loyalty "
        "card, buying stamps, paying for delivery, rounding up for charity, a shopping list, asking "
        "for a bigger bag, checking stock, comparing prices, a mobile payment app, a refund, an "
        "exchange, holiday store hours, exact change, rounding to a note, two items together, a sale, "
        "a discounted price, and holding an item until tomorrow -- Thomas repeatedly helps Lan through "
        "a shopping and payment exchange, and she responds naturally each time."
    ),
    'intro_vi': (
        "Chị Lan là khách quen của cửa hàng nhỏ do anh Thomas quản lý. Qua nhiều khoảnh khắc đời "
        "thường -- trả tiền mua bánh mì, chọn cỡ, hỏi giá, thanh toán bằng thẻ, nhận tiền thối, xin "
        "hóa đơn, một tấm nhãn giá bị mờ, mua số lượng lớn, một phiếu giảm giá, giờ mở cửa, đóng gói "
        "túi hàng, cân trái cây, mua quà, chọn giữa hai món, chính sách đổi trả, thẻ khách hàng thân "
        "thiết, mua tem thư, trả phí giao hàng, làm tròn tiền để làm từ thiện, một danh sách mua sắm, "
        "xin túi to hơn, kiểm tra hàng còn không, so sánh giá, thanh toán qua ứng dụng điện thoại, xin "
        "hoàn tiền, đổi hàng, giờ mở cửa ngày lễ, trả đúng số tiền, làm tròn theo tờ tiền, tính gộp hai "
        "món, một đợt giảm giá, giá sau khi giảm, và giữ hàng lại đến ngày mai -- anh Thomas liên tục "
        "giúp chị Lan hoàn tất một lượt mua sắm và thanh toán, và chị luôn đáp lại một cách tự nhiên."
    ),
    'turns': [
        # 1 buying bread
        ("Mr Thomas", "Good morning, Lan. That will be three dollars, please.", "Chào buổi sáng, chị Lan. Tổng cộng là ba đô la."),
        ("Ms Lan", "Here you are, Thomas.", "Đây anh Thomas."),
        ("Mr Thomas", "Perfect, and here is your change.", "Tuyệt, đây là tiền thối của chị."),
        # 2 choosing a size
        ("Ms Lan", "Do you have this in a larger size, Thomas?", "Anh có cỡ lớn hơn của món này không, anh Thomas?"),
        ("Mr Thomas", "Yes, let me check in the back.", "Có chứ, để tôi kiểm tra ở phía sau."),
        ("Ms Lan", "Thank you, I will wait here.", "Cảm ơn anh, tôi đợi ở đây."),
        # 3 asking the price
        ("Ms Lan", "How much is this jacket, Thomas?", "Cái áo khoác này giá bao nhiêu vậy, anh Thomas?"),
        ("Mr Thomas", "It is forty-five dollars.", "Giá bốn mươi lăm đô la."),
        ("Ms Lan", "That sounds fair. I will take it.", "Vậy hợp lý đấy. Tôi lấy cái này."),
        # 4 paying by card
        ("Mr Thomas", "Would you like to pay by card or cash, Lan?", "Chị muốn trả bằng thẻ hay tiền mặt vậy, chị Lan?"),
        ("Ms Lan", "By card, please.", "Bằng thẻ nhé, cảm ơn anh."),
        ("Mr Thomas", "Sure, just tap here.", "Được, chị chạm vào đây thôi."),
        # 5 getting change
        ("Mr Thomas", "Here is your change, Lan. Five dollars back.", "Đây là tiền thối của chị, chị Lan. Năm đô la nhé."),
        ("Ms Lan", "Thank you, let me count it.", "Cảm ơn anh, để tôi đếm lại."),
        ("Mr Thomas", "Take your time.", "Chị cứ từ từ."),
        # 6 asking for a receipt
        ("Ms Lan", "Could I have a receipt, please, Thomas?", "Cho tôi xin hóa đơn được không, anh Thomas?"),
        ("Mr Thomas", "Of course, here you are.", "Được chứ, đây chị."),
        ("Ms Lan", "That is very helpful, thank you.", "Vậy hữu ích lắm, cảm ơn anh."),
        # 7 faded price tag
        ("Ms Lan", "This price tag looks a bit faded, Thomas.", "Nhãn giá này trông hơi mờ, anh Thomas."),
        ("Mr Thomas", "Let me check the system for you.", "Để tôi kiểm tra trong hệ thống cho chị."),
        ("Ms Lan", "Thank you, that would help.", "Cảm ơn anh, vậy sẽ giúp ích lắm."),
        # 8 buying in bulk
        ("Mr Thomas", "Would you like to buy in bulk today, Lan?", "Hôm nay chị có muốn mua số lượng lớn không, chị Lan?"),
        ("Ms Lan", "Yes, I will take five of these.", "Có chứ, tôi lấy năm cái này."),
        ("Mr Thomas", "Great, I will pack them for you.", "Tuyệt, tôi sẽ đóng gói giúp chị."),
        # 9 discount coupon
        ("Ms Lan", "I have a coupon for this item, Thomas.", "Tôi có phiếu giảm giá cho món này, anh Thomas."),
        ("Mr Thomas", "Let me apply that for you now.", "Để tôi áp dụng ngay cho chị."),
        ("Ms Lan", "Thank you, that saves a little.", "Cảm ơn anh, vậy tiết kiệm được chút ít."),
        # 10 opening hours
        ("Ms Lan", "What time do you open tomorrow, Thomas?", "Ngày mai anh mở cửa lúc mấy giờ vậy, anh Thomas?"),
        ("Mr Thomas", "We open at eight in the morning.", "Bọn tôi mở cửa lúc tám giờ sáng."),
        ("Ms Lan", "Perfect, I will come early then.", "Tuyệt, vậy tôi sẽ đến sớm."),
        # 11 packing bags
        ("Mr Thomas", "Would you like a bag for these, Lan?", "Chị có muốn túi đựng mấy món này không, chị Lan?"),
        ("Ms Lan", "Yes, please. One bag is enough.", "Có chứ, một túi là đủ rồi."),
        ("Mr Thomas", "Here you go, all packed.", "Đây chị, đóng gói xong rồi."),
        # 12 weighing fruit
        ("Ms Lan", "Could you weigh these apples for me, Thomas?", "Anh cân giúp tôi mấy quả táo này được không, anh Thomas?"),
        ("Mr Thomas", "Of course, that comes to two dollars.", "Được chứ, tổng cộng là hai đô la."),
        ("Ms Lan", "Sounds good, I will take them.", "Được đấy, tôi lấy mấy quả này."),
        # 13 buying a gift
        ("Ms Lan", "I am looking for a small gift, Thomas.", "Tôi đang tìm một món quà nhỏ, anh Thomas."),
        ("Mr Thomas", "This candle is very popular right now.", "Cây nến này đang bán chạy lắm."),
        ("Ms Lan", "Perfect, I will take it.", "Tuyệt, tôi lấy cái này."),
        # 14 choosing between two items
        ("Mr Thomas", "Would you prefer the blue one or the red one, Lan?", "Chị thích cái màu xanh hay màu đỏ hơn, chị Lan?"),
        ("Ms Lan", "I think I will choose the blue one.", "Tôi nghĩ tôi sẽ chọn cái màu xanh."),
        ("Mr Thomas", "Good choice, it suits you well.", "Chọn hay đấy, hợp với chị lắm."),
        # 15 return policy
        ("Ms Lan", "What is your return policy, Thomas?", "Chính sách đổi trả của anh thế nào vậy, anh Thomas?"),
        ("Mr Thomas", "You can return it within a week with the receipt.", "Chị có thể đổi trả trong vòng một tuần nếu có hóa đơn."),
        ("Ms Lan", "That is good to know, thank you.", "Vậy tốt quá, cảm ơn anh đã cho biết."),
        # 16 loyalty card
        ("Mr Thomas", "Do you have a loyalty card with us, Lan?", "Chị có thẻ khách hàng thân thiết của bọn tôi không, chị Lan?"),
        ("Ms Lan", "Yes, here it is.", "Có chứ, đây ạ."),
        ("Mr Thomas", "Great, that gives you extra points today.", "Tuyệt, vậy chị được cộng thêm điểm hôm nay."),
        # 17 buying stamps
        ("Ms Lan", "Could I buy some stamps here, Thomas?", "Tôi mua tem thư ở đây được không, anh Thomas?"),
        ("Mr Thomas", "Yes, how many would you like?", "Được chứ, chị muốn mua mấy con vậy?"),
        ("Ms Lan", "Five stamps, please.", "Năm con tem nhé, cảm ơn anh."),
        # 18 paying for delivery
        ("Mr Thomas", "Would you like this delivered to your home, Lan?", "Chị có muốn giao món này đến nhà không, chị Lan?"),
        ("Ms Lan", "Yes, please. How much extra is that?", "Có chứ. Vậy tốn thêm bao nhiêu vậy?"),
        ("Mr Thomas", "Just two dollars for delivery.", "Chỉ thêm hai đô la tiền giao hàng thôi."),
        # 19 rounding up for charity
        ("Mr Thomas", "Would you like to round up for charity today, Lan?", "Hôm nay chị có muốn làm tròn tiền để ủng hộ từ thiện không, chị Lan?"),
        ("Ms Lan", "Yes, of course. That is a nice idea.", "Có chứ. Ý hay đấy."),
        ("Mr Thomas", "Thank you for supporting it.", "Cảm ơn chị đã ủng hộ."),
        # 20 shopping list
        ("Ms Lan", "I have a shopping list here, Thomas. Can you help me find everything?", "Tôi có danh sách mua sắm đây, anh Thomas. Anh giúp tôi tìm hết được không?"),
        ("Mr Thomas", "Of course, let us go through it together.", "Được chứ, mình cùng xem qua nhé."),
        ("Ms Lan", "Thank you, that would save time.", "Cảm ơn anh, vậy tiết kiệm thời gian lắm."),
        # 21 asking for a bag
        ("Ms Lan", "Could I have a bigger bag, please, Thomas?", "Cho tôi xin túi to hơn được không, anh Thomas?"),
        ("Mr Thomas", "Sure, here is a larger one.", "Được, đây là túi to hơn."),
        ("Ms Lan", "Perfect, that fits everything now.", "Tuyệt, giờ vừa hết mọi thứ rồi."),
        # 22 checking stock
        ("Ms Lan", "Do you still have this in stock, Thomas?", "Anh còn hàng món này không, anh Thomas?"),
        ("Mr Thomas", "Let me check for you right now.", "Để tôi kiểm tra ngay cho chị."),
        ("Ms Lan", "Thank you, I will wait.", "Cảm ơn anh, tôi đợi được."),
        # 23 comparing prices
        ("Ms Lan", "Which one is cheaper, Thomas?", "Cái nào rẻ hơn vậy, anh Thomas?"),
        ("Mr Thomas", "This one is two dollars less.", "Cái này rẻ hơn hai đô la."),
        ("Ms Lan", "I will take that one then.", "Vậy tôi lấy cái đó."),
        # 24 mobile payment app
        ("Mr Thomas", "You can also pay with your phone, Lan.", "Chị cũng có thể thanh toán bằng điện thoại đấy, chị Lan."),
        ("Ms Lan", "Oh, that is convenient. Let me try it.", "Ồ, tiện quá. Để tôi thử xem."),
        ("Mr Thomas", "Just scan this code here.", "Chị quét mã này là được."),
        # 25 refund
        ("Ms Lan", "I would like to return this and get a refund, Thomas.", "Tôi muốn trả lại món này và xin hoàn tiền, anh Thomas."),
        ("Mr Thomas", "No problem, do you have the receipt?", "Không sao đâu, chị có hóa đơn không?"),
        ("Ms Lan", "Of course, here it is.", "Có chứ, đây ạ."),
        # 26 exchange
        ("Ms Lan", "Could I exchange this for a different colour, Thomas?", "Tôi đổi món này sang màu khác được không, anh Thomas?"),
        ("Mr Thomas", "Of course, which colour would you like?", "Được chứ, chị muốn màu nào?"),
        ("Ms Lan", "The green one, please.", "Màu xanh lá nhé, cảm ơn anh."),
        # 27 holiday store hours
        ("Ms Lan", "Are you open on the holiday, Thomas?", "Ngày lễ anh có mở cửa không, anh Thomas?"),
        ("Mr Thomas", "Yes, but only until noon.", "Có, nhưng chỉ mở đến trưa thôi."),
        ("Ms Lan", "Good to know, thank you for telling me.", "Tốt quá, cảm ơn anh đã cho tôi biết."),
        # 28 exact change
        ("Ms Lan", "I think I have the exact change, Thomas.", "Tôi nghĩ tôi có đúng số tiền lẻ đấy, anh Thomas."),
        ("Mr Thomas", "Perfect, that makes it easy.", "Tuyệt, vậy dễ dàng hơn nhiều."),
        ("Ms Lan", "Great, here you are.", "Tuyệt, đây anh."),
        # 29 rounding to a note
        ("Mr Thomas", "I do not have small change right now, Lan.", "Hiện tôi không có tiền lẻ, chị Lan."),
        ("Ms Lan", "That is fine, just round it up.", "Không sao đâu, làm tròn lên đi."),
        ("Mr Thomas", "I appreciate your patience.", "Cảm ơn chị đã kiên nhẫn."),
        # 30 two items together
        ("Ms Lan", "Could you total these two items together, Thomas?", "Anh tính gộp hai món này lại giúp tôi được không, anh Thomas?"),
        ("Mr Thomas", "Sure, that comes to twelve dollars.", "Được, tổng cộng là mười hai đô la."),
        ("Ms Lan", "Here you go.", "Đây anh."),
        # 31 buying on sale
        ("Mr Thomas", "This item is on sale today, Lan.", "Món này hôm nay đang giảm giá đấy, chị Lan."),
        ("Ms Lan", "Oh wonderful, how much is it now?", "Ồ tuyệt quá, giờ giá bao nhiêu vậy?"),
        ("Mr Thomas", "It is now just six dollars.", "Giờ chỉ còn sáu đô la thôi."),
        # 32 price after discount
        ("Ms Lan", "What is the price after the discount, Thomas?", "Giá sau khi giảm là bao nhiêu vậy, anh Thomas?"),
        ("Mr Thomas", "It comes to eight dollars now.", "Giờ còn tám đô la thôi."),
        ("Ms Lan", "That is a good deal.", "Vậy hời quá."),
        # 33 hold an item
        ("Ms Lan", "Could you hold this item for me until tomorrow, Thomas?", "Anh giữ giúp tôi món này đến mai được không, anh Thomas?"),
        ("Mr Thomas", "Of course, I will keep it behind the counter.", "Được chứ, tôi sẽ để sau quầy giúp chị."),
        ("Ms Lan", "Thank you, I will come back for it.", "Cảm ơn anh, tôi sẽ quay lại lấy."),
        # 34 regular customer wrap-up
        ("Mr Thomas", "Thank you for shopping with us again, Lan.", "Cảm ơn chị đã mua sắm ở đây lần nữa, chị Lan."),
        ("Ms Lan", "It is always a pleasure, Thomas.", "Lúc nào cũng vui khi đến đây, anh Thomas."),
        ("Mr Thomas", "See you next time.", "Hẹn gặp lại chị lần sau."),
        ("Ms Lan", "See you soon, Thomas.", "Hẹn gặp lại sớm, anh Thomas."),
        # 35 expiry date
        ("Ms Lan", "Could you check the expiry date on this, Thomas?", "Anh kiểm tra giúp tôi hạn sử dụng của món này được không, anh Thomas?"),
        ("Mr Thomas", "Of course, it is good until next month.", "Được chứ, còn hạn đến tháng sau."),
        ("Ms Lan", "Great, I will buy it then.", "Tốt quá, vậy tôi mua món này."),
        # 36 umbrella in the rain
        ("Mr Thomas", "It is raining outside, Lan. Do you need an umbrella?", "Trời đang mưa ngoài kia, chị Lan. Chị có cần dù không?"),
        ("Ms Lan", "Yes, actually. I forgot mine today.", "Có chứ. Hôm nay tôi quên mang dù rồi."),
        ("Mr Thomas", "Here is a good one.", "Đây là một cây dù tốt."),
        # 37 gift wrapping
        ("Ms Lan", "Could you wrap this as a gift, Thomas?", "Anh gói giúp tôi món này thành quà được không, anh Thomas?"),
        ("Mr Thomas", "Of course, just give me a moment.", "Được chứ, chờ tôi một chút."),
        ("Ms Lan", "Thank you, that looks lovely.", "Cảm ơn anh, trông đẹp quá."),
        # 38 special order
        ("Ms Lan", "Could you order this in for me, Thomas?", "Anh đặt hàng giúp tôi món này được không, anh Thomas?"),
        ("Mr Thomas", "Yes, it should arrive next week.", "Được chứ, chắc tuần sau hàng sẽ về."),
        ("Ms Lan", "Wonderful, I will come back then.", "Tuyệt quá, vậy tôi sẽ quay lại lúc đó."),
        # 39 deposit
        ("Mr Thomas", "Would you like to pay a small deposit today, Lan?", "Hôm nay chị có muốn đặt cọc một ít không, chị Lan?"),
        ("Ms Lan", "Yes, that sounds fair.", "Có chứ, vậy hợp lý đấy."),
        ("Mr Thomas", "Great, I will note it down.", "Tuyệt, tôi sẽ ghi lại ngay."),
        # 40 second-hand item
        ("Ms Lan", "Is this item second-hand, Thomas?", "Món này là đồ cũ à, anh Thomas?"),
        ("Mr Thomas", "Yes, but it is in excellent condition.", "Vâng, nhưng còn rất tốt."),
        ("Ms Lan", "Good, the price is very reasonable too.", "Tốt, giá cũng hợp lý nữa."),
        # 41 warranty
        ("Ms Lan", "Does this come with a warranty, Thomas?", "Món này có bảo hành không, anh Thomas?"),
        ("Mr Thomas", "Yes, for one full year.", "Có chứ, bảo hành trọn một năm."),
        ("Ms Lan", "That gives me peace of mind.", "Vậy tôi yên tâm hơn nhiều."),
        # 42 flowers
        ("Ms Lan", "Could I get a small bunch of flowers, Thomas?", "Cho tôi mua một bó hoa nhỏ được không, anh Thomas?"),
        ("Mr Thomas", "Of course, any colour in particular?", "Được chứ, chị thích màu nào không?"),
        ("Ms Lan", "Yellow ones, please.", "Màu vàng nhé, cảm ơn anh."),
        # 43 trying an item on
        ("Ms Lan", "Could I try this on before I buy it, Thomas?", "Tôi mặc thử trước khi mua được không, anh Thomas?"),
        ("Mr Thomas", "Of course, the fitting room is over there.", "Được chứ, phòng thử đồ ở đằng kia."),
        ("Ms Lan", "Thank you, I will be quick.", "Cảm ơn anh, tôi thử nhanh thôi."),
    ],
}
