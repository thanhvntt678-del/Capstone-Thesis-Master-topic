# -*- coding: utf-8 -*-
LESSON_0025 = {
    'lesson_id': '0025',
    'cefr': 'A0 / Pre-A1',
    'domain': 'Shopping',
    'en_title': 'Recognising and Responding to a Routine Everyday Need Involving Shopping and Payments',
    'vi_title': 'Giao tiếp nền tảng: shopping & payments — a routine everyday need involving shopping & payments',
    'intro_en': (
        "Ms Lan and Mr Nathan work near the same market and often run into each other during ordinary "
        "shopping errands. Across many everyday moments -- buying groceries, paying by cash, paying by "
        "card, asking for a receipt, checking change, asking the price, a sale discount, waiting in a "
        "queue, forgetting a wallet, a contactless payment, splitting a bill, asking for a bag, returning "
        "an item, exchanging a size, asking about a warranty, a loyalty card, paying with a mobile app, a "
        "forgotten PIN, an expired card, buying a subscription, paying a utility bill at a counter, "
        "buying a bus ticket, buying stamps at the post office, using a coupon, checking store hours, "
        "asking about delivery, a payment declined, a bag charge, buying a phone top-up card, needing "
        "small change, leaving a tip, paying for parking, a self-checkout machine, asking for cash back, "
        "an ATM withdrawal, asking about instalment payment, a missing price tag, and finally why "
        "routine shopping and payment moments matter so much -- one of them runs into a small everyday "
        "need, and the other responds helpfully each time."
    ),
    'intro_vi': (
        "Chị Lan và anh Nathan làm việc gần cùng một khu chợ và thường gặp nhau trong những việc mua sắm "
        "đời thường. Qua nhiều khoảnh khắc đời thường -- mua thực phẩm, trả tiền mặt, trả bằng thẻ, xin "
        "hóa đơn, kiểm tra tiền thối, hỏi giá, giảm giá khuyến mãi, xếp hàng chờ, quên ví, thanh toán "
        "chạm thẻ, chia tiền hóa đơn, xin túi đựng, trả lại hàng, đổi size, hỏi về bảo hành, thẻ tích "
        "điểm, thanh toán bằng ứng dụng di động, quên mã PIN, thẻ hết hạn, mua gói đăng ký, trả hóa đơn "
        "tiện ích tại quầy, mua vé xe buýt, mua tem tại bưu điện, dùng phiếu giảm giá, xem giờ mở cửa của "
        "cửa hàng, hỏi về giao hàng, thanh toán bị từ chối, phí túi đựng, mua thẻ nạp điện thoại, cần "
        "tiền lẻ, để lại tiền boa, trả tiền đỗ xe, máy tự thanh toán, xin rút tiền mặt, rút tiền tại máy "
        "ATM, hỏi về trả góp, thiếu bảng giá, và cuối cùng là vì sao những khoảnh khắc mua sắm và thanh "
        "toán đời thường lại quan trọng đến vậy -- một người gặp phải một nhu cầu nhỏ hằng ngày, và "
        "người kia luôn đáp lại giúp đỡ mỗi lần."
    ),
    'turns': [
        # 1 buying groceries
        ("Mr Nathan", "Lan, are you here to buy groceries too?", "Chị Lan, chị cũng đến mua đồ ăn à?"),
        ("Ms Lan", "Yes, just picking up a few things for dinner.", "Vâng, tôi ghé mua vài thứ nấu bữa tối."),
        ("Mr Nathan", "Same here, the market is quite busy today.", "Tôi cũng vậy, chợ hôm nay đông quá."),
        # 2 paying by cash
        ("Ms Lan", "I will pay for this in cash, please.", "Cho tôi trả bằng tiền mặt nhé."),
        ("Mr Nathan", "Sure, that comes to fifty thousand dong.", "Được chứ, tổng cộng năm mươi nghìn đồng."),
        ("Ms Lan", "Here you go, exact change.", "Đây, đúng số tiền luôn."),
        # 3 paying by card
        ("Mr Nathan", "Could I pay by card instead of cash?", "Tôi trả bằng thẻ thay vì tiền mặt được không?"),
        ("Ms Lan", "Of course, just tap it on the machine.", "Được chứ, anh chạm thẻ vào máy là được."),
        ("Mr Nathan", "Done, thank you for your patience.", "Xong rồi, cảm ơn chị đã kiên nhẫn."),
        # 4 asking for a receipt
        ("Ms Lan", "Could I get a receipt for this purchase?", "Cho tôi xin hóa đơn cho lần mua này được không?"),
        ("Mr Nathan", "Sure, here is your receipt.", "Được chứ, đây là hóa đơn của chị."),
        ("Ms Lan", "Thanks, I need it for my records.", "Cảm ơn anh, tôi cần nó để lưu lại."),
        # 5 checking change
        ("Mr Nathan", "I think you gave me the wrong change.", "Tôi nghĩ chị thối tiền nhầm rồi."),
        ("Ms Lan", "Let me check that again for you.", "Để tôi kiểm tra lại giúp anh."),
        ("Mr Nathan", "Ah, you are right, it was correct after all.", "À, chị nói đúng, hóa ra là đúng rồi."),
        # 6 asking the price
        ("Ms Lan", "Excuse me, how much does this cost?", "Xin lỗi, cái này giá bao nhiêu vậy?"),
        ("Mr Nathan", "That one is thirty thousand dong.", "Cái đó giá ba mươi nghìn đồng."),
        ("Ms Lan", "Thank you, I will take two of them.", "Cảm ơn anh, tôi lấy hai cái nhé."),
        # 7 sale discount
        ("Mr Nathan", "Is there a discount on this item today?", "Hôm nay món này có giảm giá không?"),
        ("Ms Lan", "Yes, it is twenty percent off until Sunday.", "Có chứ, giảm hai mươi phần trăm đến hết chủ nhật."),
        ("Mr Nathan", "Great, I will grab a few then.", "Tuyệt, vậy tôi lấy vài cái luôn."),
        # 8 waiting in a queue
        ("Ms Lan", "This queue is longer than usual today.", "Hàng chờ hôm nay dài hơn thường lệ."),
        ("Mr Nathan", "Yes, everyone seems to be shopping this morning.", "Vâng, sáng nay hình như ai cũng đi mua sắm."),
        ("Ms Lan", "I suppose we just wait our turn.", "Chắc mình cứ chờ đến lượt thôi."),
        # 9 forgetting a wallet
        ("Mr Nathan", "Oh no, I think I forgot my wallet.", "Ôi không, hình như tôi quên ví rồi."),
        ("Ms Lan", "Do not worry, I can lend you some money.", "Đừng lo, tôi cho anh mượn tiền được."),
        ("Mr Nathan", "Thank you so much, I will pay you back.", "Cảm ơn chị nhiều lắm, tôi sẽ trả lại sau."),
        # 10 contactless payment
        ("Ms Lan", "Does this shop accept contactless payment?", "Cửa hàng này có nhận thanh toán chạm thẻ không?"),
        ("Mr Nathan", "Yes, just hold your card near the reader.", "Có chứ, chị chỉ cần để thẻ gần đầu đọc."),
        ("Ms Lan", "Easy enough, thank you.", "Vậy dễ quá, cảm ơn anh."),
        # 11 splitting a bill
        ("Mr Nathan", "Shall we split this bill between us?", "Mình chia đôi hóa đơn này nhé?"),
        ("Ms Lan", "Sure, that sounds fair to me.", "Được chứ, vậy công bằng đấy."),
        ("Mr Nathan", "Great, I will pay my half now.", "Tuyệt, tôi trả phần của tôi ngay đây."),
        # 12 asking for a bag
        ("Ms Lan", "Could I get a bag for these items, please?", "Cho tôi xin một cái túi đựng mấy món này được không?"),
        ("Mr Nathan", "Of course, here is a bag for you.", "Được chứ, đây là túi cho chị."),
        ("Ms Lan", "Thank you, that makes it easier to carry.", "Cảm ơn anh, vậy mang dễ hơn nhiều."),
        # 13 returning an item
        ("Mr Nathan", "I would like to return this, it does not fit.", "Tôi muốn trả lại cái này, nó không vừa."),
        ("Ms Lan", "That is fine, do you still have the receipt?", "Không sao, anh có hóa đơn không?"),
        ("Mr Nathan", "Yes, right here.", "Có, đây rồi."),
        # 14 exchanging a size
        ("Ms Lan", "Could I exchange this for a larger size?", "Tôi đổi cái này sang size lớn hơn được không?"),
        ("Mr Nathan", "Sure, let me check what we have in stock.", "Được chứ, để tôi xem còn hàng không."),
        ("Ms Lan", "Thanks, I will just wait right here.", "Cảm ơn anh, tôi đợi ở đây."),
        # 15 asking about a warranty
        ("Mr Nathan", "Does this product come with a warranty?", "Sản phẩm này có bảo hành không?"),
        ("Ms Lan", "Yes, it comes with a one-year warranty.", "Có chứ, bảo hành một năm."),
        ("Mr Nathan", "That is useful to know, thanks.", "Tốt quá, cảm ơn chị."),
        # 16 loyalty card
        ("Ms Lan", "Do you have a loyalty card with this shop?", "Anh có thẻ tích điểm ở cửa hàng này không?"),
        ("Mr Nathan", "Not yet, how do I sign up for one?", "Chưa có, làm sao để đăng ký một cái vậy?"),
        ("Ms Lan", "Just ask at the counter, it is quick.", "Anh cứ hỏi ở quầy, nhanh lắm."),
        # 17 mobile app payment
        ("Mr Nathan", "Can I pay using a mobile payment app here?", "Ở đây tôi trả bằng ứng dụng thanh toán di động được không?"),
        ("Ms Lan", "Yes, just scan this code at the counter.", "Được chứ, anh quét mã này ở quầy là được."),
        ("Mr Nathan", "Perfect, that is very convenient.", "Tuyệt, vậy tiện quá."),
        # 18 forgotten PIN
        ("Ms Lan", "Oh dear, I cannot remember my card PIN.", "Ôi trời, tôi không nhớ mã PIN của thẻ nữa."),
        ("Mr Nathan", "Take your time, there is no rush.", "Chị cứ từ từ, không vội đâu."),
        ("Ms Lan", "Got it, I remember it now.", "Nhớ ra rồi, tôi nhớ được rồi."),
        # 19 expired card
        ("Mr Nathan", "It seems this card has expired.", "Hình như thẻ này hết hạn rồi."),
        ("Ms Lan", "Oh, I did not realise, let me use another one.", "Ồ, tôi không để ý, để tôi dùng thẻ khác."),
        ("Mr Nathan", "No problem, take your time.", "Không sao đâu, chị cứ từ từ."),
        # 20 buying a subscription
        ("Ms Lan", "I would like to buy a monthly subscription, please.", "Tôi muốn mua gói đăng ký hàng tháng."),
        ("Mr Nathan", "Sure, which plan would you like to choose?", "Được chứ, chị muốn chọn gói nào?"),
        ("Ms Lan", "The basic plan should be enough for me.", "Gói cơ bản là đủ cho tôi rồi."),
        # 21 paying a utility bill at a counter
        ("Mr Nathan", "Can I pay my electricity bill here?", "Tôi trả tiền điện ở đây được không?"),
        ("Ms Lan", "Yes, just give me the bill number.", "Được chứ, anh đưa tôi mã hóa đơn."),
        ("Mr Nathan", "Here it is, thank you.", "Đây rồi, cảm ơn chị."),
        # 22 buying a bus ticket
        ("Ms Lan", "One ticket to the city centre, please.", "Cho tôi một vé đến trung tâm thành phố."),
        ("Mr Nathan", "That will be fifteen thousand dong.", "Vé đó giá mười lăm nghìn đồng."),
        ("Ms Lan", "Here you go, thank you.", "Đây, cảm ơn anh."),
        # 23 buying stamps at the post office
        ("Mr Nathan", "Could I buy a few stamps, please?", "Cho tôi mua vài con tem được không?"),
        ("Ms Lan", "Sure, how many would you like?", "Được chứ, anh muốn mua bao nhiêu?"),
        ("Mr Nathan", "Five should be enough for now.", "Năm con là đủ cho bây giờ rồi."),
        # 24 using a coupon
        ("Ms Lan", "Can I use this coupon on my purchase today?", "Hôm nay tôi dùng phiếu giảm giá này được không?"),
        ("Mr Nathan", "Yes, that will bring the price down nicely.", "Được chứ, vậy giá sẽ giảm xuống đáng kể."),
        ("Ms Lan", "Wonderful, thank you for checking.", "Tuyệt quá, cảm ơn anh đã kiểm tra."),
        # 25 checking store hours
        ("Mr Nathan", "What time does this shop close tonight?", "Tối nay cửa hàng đóng cửa lúc mấy giờ?"),
        ("Ms Lan", "It closes at nine in the evening.", "Đóng cửa lúc chín giờ tối."),
        ("Mr Nathan", "Good, I have plenty of time then.", "Tốt, vậy tôi còn nhiều thời gian."),
        # 26 asking about delivery
        ("Ms Lan", "Does this store offer home delivery?", "Cửa hàng này có giao hàng tận nhà không?"),
        ("Mr Nathan", "Yes, delivery is available within the city.", "Có chứ, giao hàng trong nội thành."),
        ("Ms Lan", "Perfect, I will arrange that then.", "Tuyệt, vậy tôi sắp xếp giao hàng nhé."),
        # 27 payment declined
        ("Mr Nathan", "It looks like the payment did not go through.", "Hình như thanh toán không thành công."),
        ("Ms Lan", "Let us try again, maybe it was a glitch.", "Mình thử lại xem, chắc do lỗi thôi."),
        ("Mr Nathan", "It worked this time, thank you for waiting.", "Lần này được rồi, cảm ơn chị đã chờ."),
        # 28 bag charge
        ("Ms Lan", "Is there a small charge for the bag?", "Túi đựng có tính thêm phí không?"),
        ("Mr Nathan", "Yes, just a small fee, is that alright?", "Có, một khoản phí nhỏ thôi, được không ạ?"),
        ("Ms Lan", "That is fine, I will take one.", "Được thôi, cho tôi một cái."),
        # 29 buying a phone top-up card
        ("Mr Nathan", "Could I buy a phone top-up card, please?", "Cho tôi mua một thẻ nạp điện thoại được không?"),
        ("Ms Lan", "Sure, which network and amount do you need?", "Được chứ, anh cần mạng nào và mệnh giá bao nhiêu?"),
        ("Mr Nathan", "A fifty thousand dong top-up will do.", "Thẻ năm mươi nghìn đồng là được rồi."),
        # 30 needing small change
        ("Ms Lan", "Do you happen to have change for a large note?", "Anh có tình cờ có tiền lẻ đổi tờ lớn không?"),
        ("Mr Nathan", "Let me check what I have in the drawer.", "Để tôi xem trong ngăn kéo có gì."),
        ("Ms Lan", "Thanks so much, that is a big help.", "Cảm ơn anh, tôi cảm kích lắm."),
        # 31 leaving a tip
        ("Mr Nathan", "Should we leave a tip for the delivery driver?", "Mình có nên để lại tiền boa cho người giao hàng không?"),
        ("Ms Lan", "That would be a nice gesture, yes.", "Vậy sẽ là một cử chỉ đẹp đấy, nên làm."),
        ("Mr Nathan", "I will add a little extra then.", "Vậy tôi thêm một chút nữa."),
        # 32 paying for parking
        ("Ms Lan", "How much is the parking fee here?", "Phí đỗ xe ở đây bao nhiêu vậy?"),
        ("Mr Nathan", "It is five thousand dong per hour.", "Là năm nghìn đồng mỗi giờ."),
        ("Ms Lan", "That seems reasonable, thank you.", "Nghe hợp lý đấy, cảm ơn anh."),
        # 33 self-checkout machine
        ("Mr Nathan", "Have you used the self-checkout machine before?", "Chị dùng máy tự thanh toán bao giờ chưa?"),
        ("Ms Lan", "Not yet, could you show me how it works?", "Chưa, anh chỉ tôi cách dùng được không?"),
        ("Mr Nathan", "Sure, it is actually quite simple.", "Được chứ, thật ra khá đơn giản thôi."),
        # 34 asking for cash back
        ("Ms Lan", "Could I get some cash back with this payment?", "Cho tôi rút thêm tiền mặt cùng lúc thanh toán được không?"),
        ("Mr Nathan", "Sure, how much would you like?", "Được chứ, chị muốn rút bao nhiêu?"),
        ("Ms Lan", "Two hundred thousand dong, please.", "Cho tôi hai trăm nghìn đồng."),
        # 35 ATM withdrawal
        ("Mr Nathan", "I need to withdraw some cash from the ATM.", "Tôi cần rút tiền mặt ở máy ATM."),
        ("Ms Lan", "There is one just around the corner.", "Có một cái ngay góc phố kia."),
        ("Mr Nathan", "Thanks, I will head there now.", "Cảm ơn chị, tôi đi ngay đây."),
        # 36 asking about instalment payment
        ("Ms Lan", "Does this store offer instalment payment plans?", "Cửa hàng này có hình thức trả góp không?"),
        ("Mr Nathan", "Yes, you can pay over three months.", "Có chứ, chị có thể trả trong ba tháng."),
        ("Ms Lan", "That makes it much easier for me.", "Vậy sẽ dễ dàng hơn nhiều cho tôi."),
        # 37 missing price tag
        ("Mr Nathan", "This item does not seem to have a price tag.", "Món này hình như không có bảng giá."),
        ("Ms Lan", "Let me check the price for you at the counter.", "Để tôi kiểm tra giá giúp anh ở quầy."),
        ("Mr Nathan", "Thank you, I appreciate you checking.", "Cảm ơn chị đã kiểm tra giúp."),
        # 38 closing - why these moments matter
        ("Ms Lan", "These small shopping errands really add up during the week.", "Những việc mua sắm nhỏ này thật ra cộng lại cũng nhiều trong tuần."),
        ("Mr Nathan", "They do, and it helps to have things go smoothly.", "Đúng vậy, và mọi thứ suôn sẻ thì đỡ mệt hơn nhiều."),
        ("Ms Lan", "That is why a little patience always helps.", "Vì vậy mà một chút kiên nhẫn luôn có ích."),
        ("Mr Nathan", "Well said, and a friendly face makes it easier too.", "Chị nói đúng, có một gương mặt thân thiện cũng dễ chịu hơn."),
    ],
}
