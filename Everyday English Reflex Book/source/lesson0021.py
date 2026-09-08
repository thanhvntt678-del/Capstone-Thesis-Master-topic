# -*- coding: utf-8 -*-
LESSON_0021 = {
    'lesson_id': '0021',
    'cefr': 'A0 / Pre-A1',
    'domain': 'Numbers and Time',
    'en_title': 'Recognising and Responding to a Phone Number',
    'vi_title': 'Giao tiếp nền tảng: numbers, dates & time — a phone number',
    'intro_en': (
        "Ms Lan and Mr George work in the same building and often need to exchange or confirm phone "
        "numbers for many different reasons. Across many everyday moments -- asking for a number, "
        "giving a number slowly, reading a number back to confirm, a wrong number, a missed call, an "
        "office extension, an area code, a country code for an overseas call, texting a number instead "
        "of saying it, saving a new contact, correcting a mistyped digit, a doctor's appointment line, "
        "a restaurant reservation number, a taxi booking number, a delivery driver's number, a customer "
        "service hotline, a landlord's maintenance number, an emergency contact number, leaving a "
        "number in a voicemail, a repeated digit spoken as 'double', exchanging numbers on a business "
        "card, an RSVP contact number, a school office number, a technical support line, a landline "
        "versus a mobile number, borrowing a phone after losing one, a messaging app number, a family "
        "member's updated number, a bank hotline, confirming an "
        "insurance number, a number written by hand that is hard to read, spelling digits over a noisy "
        "line, a number given with a country plus sign, a driver calling at the gate, an old number that "
        "no longer works, a number that changed after moving house, and finally why getting a number "
        "exactly right matters so much -- Mr George often needs a number from Ms Lan, or the other way "
        "around, and each time she responds clearly and makes sure it is correct."
    ),
    'intro_vi': (
        "Chị Lan và anh George làm việc trong cùng một tòa nhà và thường xuyên phải trao đổi hoặc xác "
        "nhận số điện thoại vì nhiều lý do khác nhau. Qua nhiều khoảnh khắc đời thường -- hỏi xin số "
        "điện thoại, đọc số chậm rãi, đọc lại số để xác nhận, gọi nhầm số, một cuộc gọi nhỡ, số máy lẻ "
        "văn phòng, mã vùng, mã quốc gia cho cuộc gọi ra nước ngoài, nhắn tin số thay vì đọc, lưu số liên "
        "hệ mới, sửa lại một chữ số gõ sai, đường dây hẹn khám bệnh, số đặt bàn nhà hàng, số đặt xe taxi, "
        "số của tài xế giao hàng, tổng đài chăm sóc khách hàng, số liên hệ bảo trì của chủ nhà, số liên "
        "hệ khẩn cấp, để lại số trong hộp thư thoại, một chữ số lặp lại được đọc là 'double', trao đổi số "
        "trên danh thiếp, số liên hệ để xác nhận tham dự, số văn phòng trường học, đường dây hỗ trợ kỹ "
        "thuật, số điện thoại bàn so với số di động, mượn điện thoại sau khi làm mất máy, số trên ứng "
        "dụng nhắn tin, số điện thoại mới của người thân, tổng đài ngân hàng, xác "
        "nhận số bảo hiểm, một số viết tay khó đọc, đọc từng chữ số qua đường truyền ồn, một số được cho "
        "kèm dấu cộng mã quốc gia, tài xế gọi ở cổng, một số cũ không còn dùng được nữa, một số đổi sau "
        "khi chuyển nhà, và cuối cùng là vì sao việc lấy đúng một con số lại quan trọng đến vậy -- anh "
        "George thường cần một số điện thoại từ chị Lan, hoặc ngược lại, và mỗi lần chị đều trả lời rõ "
        "ràng và đảm bảo con số đó chính xác."
    ),
    'turns': [
        # 1 asking for a number
        ("Mr George", "Lan, could I get your phone number?", "Chị Lan, cho tôi xin số điện thoại của chị được không?"),
        ("Ms Lan", "Sure, it is zero nine one, two three four, five six seven eight.", "Được chứ, số của tôi là không chín một, hai ba bốn, năm sáu bảy tám."),
        ("Mr George", "Noted, I appreciate it.", "Tôi ghi lại rồi, cảm ơn chị."),
        # 2 giving a number slowly
        ("Mr George", "Could you say that again, more slowly this time?", "Chị đọc lại lần nữa, chậm hơn được không?"),
        ("Ms Lan", "Of course. Zero... nine... one... two... three... four.", "Được chứ. Không... chín... một... hai... ba... bốn."),
        ("Mr George", "That is much easier to follow.", "Vậy dễ theo dõi hơn nhiều."),
        # 3 reading a number back to confirm
        ("Mr George", "Let me read it back to make sure I have it right.", "Để tôi đọc lại xem tôi ghi đúng chưa."),
        ("Ms Lan", "Please do, go ahead.", "Chị cứ đọc đi."),
        ("Mr George", "Zero nine one, two three four, five six seven eight.", "Không chín một, hai ba bốn, năm sáu bảy tám."),
        ("Ms Lan", "That is exactly right.", "Đúng y như vậy đấy."),
        # 4 wrong number
        ("Mr George", "Hello? Is this Ms Lan's number?", "Alo? Đây có phải số của chị Lan không?"),
        ("Ms Lan", "I am sorry, I think you have the wrong number.", "Xin lỗi, tôi nghĩ anh gọi nhầm số rồi."),
        ("Mr George", "Oh, my mistake, sorry to bother you.", "Ồ, xin lỗi, làm phiền chị rồi."),
        # 5 missed call
        ("Ms Lan", "George, I see a missed call from you.", "Anh George, tôi thấy có cuộc gọi nhỡ từ anh."),
        ("Mr George", "Yes, sorry, I called about the meeting.", "Vâng, xin lỗi, tôi gọi để hỏi về cuộc họp."),
        ("Ms Lan", "No problem, let me call you back now.", "Không sao, để tôi gọi lại cho anh ngay."),
        # 6 office extension
        ("Mr George", "What is your office extension, Lan?", "Số máy lẻ văn phòng của chị là gì vậy, chị Lan?"),
        ("Ms Lan", "My extension is two one five.", "Số máy lẻ của tôi là hai một năm."),
        ("Mr George", "Two one five, I will note that down.", "Hai một năm, tôi ghi lại nhé."),
        # 7 area code
        ("Mr George", "What area code do I need for this city?", "Muốn gọi vào thành phố này thì cần mã vùng nào?"),
        ("Ms Lan", "You will need the code zero two eight.", "Anh cần dùng mã không hai tám."),
        ("Mr George", "Thanks, that clears it up.", "Cảm ơn chị, giờ tôi hiểu rồi."),
        # 8 country code overseas
        ("Mr George", "How do I dial your number from overseas?", "Muốn gọi số của chị từ nước ngoài thì làm sao?"),
        ("Ms Lan", "Just add plus eight four before the number.", "Anh chỉ cần thêm dấu cộng tám bốn trước số điện thoại."),
        ("Mr George", "Plus eight four, understood.", "Cộng tám bốn, tôi hiểu rồi."),
        # 9 texting instead of saying
        ("Ms Lan", "It might be easier if I just text you the number.", "Chắc để tôi nhắn tin số điện thoại cho anh thì dễ hơn."),
        ("Mr George", "That would be great, thank you.", "Vậy thì tốt quá, cảm ơn chị."),
        ("Ms Lan", "Sending it right now.", "Tôi gửi ngay đây."),
        # 10 saving a contact
        ("Mr George", "I have saved your number under 'Lan, Front Desk'.", "Tôi lưu số của chị vào tên 'Lan, Lễ tân' rồi."),
        ("Ms Lan", "Perfect, you will find it easily then.", "Tốt quá, vậy anh sẽ dễ tìm thấy hơn."),
        ("Mr George", "Exactly, no more searching.", "Đúng vậy, khỏi phải tìm lại nữa."),
        # 11 correcting a mistyped digit
        ("Ms Lan", "Wait, I think you typed the last digit wrong.", "Khoan đã, hình như anh gõ sai chữ số cuối rồi."),
        ("Mr George", "Oh, you are right, let me fix it.", "Ồ, chị nói đúng, để tôi sửa lại."),
        ("Ms Lan", "It should end in eight, not nine.", "Số phải kết thúc bằng tám, không phải chín."),
        ("Mr George", "Fixed now, thank you for catching that.", "Sửa xong rồi, cảm ơn chị đã phát hiện ra."),
        # 12 doctor's appointment line
        ("Mr George", "What number do I call to book a doctor's appointment?", "Muốn đặt lịch khám bác sĩ thì gọi số nào?"),
        ("Ms Lan", "Call the clinic at zero two eight, three three three, four four four.", "Anh gọi phòng khám theo số không hai tám, ba ba ba, bốn bốn bốn."),
        ("Mr George", "Got it, I will call them today.", "Tôi ghi lại rồi, hôm nay tôi sẽ gọi."),
        # 13 restaurant reservation number
        ("Ms Lan", "Do you have the number for the restaurant reservation?", "Anh có số đặt bàn nhà hàng không?"),
        ("Mr George", "Yes, it is zero nine three, seven seven seven, eight eight eight.", "Có chứ, số là không chín ba, bảy bảy bảy, tám tám tám."),
        ("Ms Lan", "Thanks, I will book a table now.", "Cảm ơn anh, tôi đặt bàn ngay đây."),
        # 14 taxi booking number
        ("Mr George", "What is the number for the taxi service you use?", "Số của hãng taxi anh hay dùng là gì vậy?"),
        ("Ms Lan", "It is zero eight one, two two two, three three three.", "Là không tám một, hai hai hai, ba ba ba."),
        ("Mr George", "I will save that for next time.", "Tôi lưu lại để lần sau dùng."),
        # 15 delivery driver's number
        ("Ms Lan", "The delivery driver just sent his number to call at the gate.", "Tài xế giao hàng vừa gửi số để gọi khi đến cổng."),
        ("Mr George", "What is his number, in case I need it too?", "Số của anh ấy là gì, phòng khi tôi cũng cần?"),
        ("Ms Lan", "It is zero nine seven, one one one, two two two.", "Là không chín bảy, một một một, hai hai hai."),
        # 16 customer service hotline
        ("Mr George", "Do you know the customer service hotline for the bank?", "Chị có biết số tổng đài chăm sóc khách hàng của ngân hàng không?"),
        ("Ms Lan", "Yes, it is one nine hundred, five five five, six six six.", "Có chứ, là một chín trăm, năm năm năm, sáu sáu sáu."),
        ("Mr George", "Thank you, that will save me some searching.", "Cảm ơn chị, vậy đỡ phải tìm kiếm rồi."),
        # 17 landlord's maintenance number
        ("Ms Lan", "My landlord gave me a maintenance number for repairs.", "Chủ nhà tôi có đưa một số liên hệ bảo trì để sửa chữa."),
        ("Mr George", "That is useful, could you share it with me too?", "Hữu ích đấy, chị chia sẻ luôn cho tôi được không?"),
        ("Ms Lan", "Sure, it is zero two eight, wait, let me check again.", "Được chứ, là không hai tám, khoan, để tôi kiểm tra lại."),
        # 18 emergency contact number
        ("Mr George", "What number should I list as your emergency contact?", "Tôi nên ghi số nào làm liên hệ khẩn cấp của chị?"),
        ("Ms Lan", "Please use my mobile number, not the office line.", "Anh dùng số di động của tôi nhé, đừng dùng số văn phòng."),
        ("Mr George", "Understood, mobile number it is.", "Rõ rồi, vậy tôi ghi số di động."),
        # 19 leaving a number in voicemail
        ("Ms Lan", "I left George a voicemail with my number.", "Tôi để lại tin nhắn thoại cho anh George kèm số điện thoại."),
        ("Mr George", "I got it, and I wrote the number down carefully.", "Tôi nhận được rồi, và ghi lại số cẩn thận."),
        ("Ms Lan", "Good, I will wait for your call.", "Tốt quá, tôi sẽ đợi anh gọi lại."),
        # 20 double digit spoken
        ("Mr George", "How do I say the number if two digits repeat?", "Nếu hai chữ số giống nhau liền kề thì đọc sao?"),
        ("Ms Lan", "You can say 'double five' instead of 'five, five'.", "Anh có thể nói 'double five' thay vì 'năm, năm'."),
        ("Mr George", "That sounds quicker, I will try it.", "Nghe nhanh hơn đấy, tôi sẽ thử."),
        # 21 business card exchange
        ("Ms Lan", "Here is my business card with my number on it.", "Đây là danh thiếp của tôi, có số điện thoại trên đó."),
        ("Mr George", "Thank you, and here is mine as well.", "Cảm ơn chị, đây là danh thiếp của tôi luôn."),
        ("Ms Lan", "Now we both have each other's number.", "Vậy là hai ta đều có số của nhau rồi."),
        # 22 RSVP contact number
        ("Mr George", "The invitation asks for a contact number to RSVP.", "Thiệp mời yêu cầu một số điện thoại để xác nhận tham dự."),
        ("Ms Lan", "You can just put my number on the form.", "Anh cứ điền số của tôi vào đơn cũng được."),
        ("Mr George", "I will do that, thank you.", "Tôi sẽ làm vậy, cảm ơn chị."),
        # 23 school office number
        ("Ms Lan", "Do you have the school office number handy?", "Anh có sẵn số văn phòng trường học không?"),
        ("Mr George", "Yes, it is zero two eight... sorry, let me check my phone.", "Có chứ, là không hai tám... xin lỗi, để tôi kiểm tra điện thoại."),
        ("Ms Lan", "There is no hurry, check whenever you are ready.", "Anh cứ từ từ, không vội đâu."),
        # 24 technical support line
        ("Mr George", "The technical support line is busy again.", "Đường dây hỗ trợ kỹ thuật lại bận nữa rồi."),
        ("Ms Lan", "Try this alternate number instead, it usually works.", "Anh thử số dự phòng này xem, thường thì gọi được."),
        ("Mr George", "Good idea, let me try that one.", "Ý hay đấy, để tôi thử số đó."),
        # 25 landline versus mobile
        ("Ms Lan", "Should I give you my landline or my mobile number?", "Tôi nên cho anh số điện thoại bàn hay số di động?"),
        ("Mr George", "The mobile number would be more useful, thanks.", "Số di động sẽ hữu ích hơn, cảm ơn chị."),
        ("Ms Lan", "Understood, I will give you that one.", "Rõ rồi, tôi sẽ cho anh số đó."),
        # 26 borrowing a phone after losing one
        ("Mr George", "I lost my phone, could I borrow yours to call my number?", "Tôi làm mất điện thoại rồi, mượn máy của chị gọi số tôi được không?"),
        ("Ms Lan", "Sure, here is my phone.", "Được chứ, máy của tôi đây."),
        ("Mr George", "Thank you, this really helps.", "Cảm ơn chị, việc này giúp tôi nhiều lắm."),
        # 27 messaging app number
        ("Ms Lan", "Is this the same number you use on the messaging app?", "Đây có phải số anh dùng trên ứng dụng nhắn tin không?"),
        ("Mr George", "Yes, it is exactly the same number.", "Đúng vậy, chính là số này luôn."),
        ("Ms Lan", "Good, I will message you there then.", "Tốt, vậy tôi sẽ nhắn tin cho anh ở đó."),
        # 28 family member's updated number
        ("Mr George", "My brother changed his number, let me give you the new one.", "Em trai tôi đổi số rồi, để tôi cho chị số mới."),
        ("Ms Lan", "Please do, I will update it in my contacts.", "Anh cho tôi đi, tôi sẽ cập nhật trong danh bạ."),
        ("Mr George", "It is zero nine six, four four four, one one one.", "Là không chín sáu, bốn bốn bốn, một một một."),
        # 30 bank hotline
        ("Mr George", "I need to call the bank hotline about my card.", "Tôi cần gọi tổng đài ngân hàng về vấn đề thẻ của tôi."),
        ("Ms Lan", "The number is printed on the back of your card.", "Số điện thoại được in ở mặt sau thẻ của anh đấy."),
        ("Mr George", "Ah, I did not notice that, thank you.", "À, tôi không để ý, cảm ơn chị."),
        # 31 confirming an insurance number
        ("Ms Lan", "Can you confirm the number listed for my insurance file?", "Anh xác nhận giúp số được ghi trong hồ sơ bảo hiểm của tôi được không?"),
        ("Mr George", "Sure, it shows zero nine two, eight eight eight, nine nine nine.", "Được chứ, hồ sơ ghi không chín hai, tám tám tám, chín chín chín."),
        ("Ms Lan", "Yes, that is the right number.", "Vâng, đúng số đó rồi."),
        # 32 number written by hand hard to read
        ("Mr George", "I cannot quite read this handwritten number, can you check?", "Tôi không đọc rõ số viết tay này, chị xem giúp được không?"),
        ("Ms Lan", "Let me look... I believe this is a seven, not a one.", "Để tôi xem... tôi nghĩ đây là số bảy, không phải số một."),
        ("Mr George", "That makes much more sense now.", "Vậy hợp lý hơn nhiều rồi."),
        # 33 spelling digits over a noisy line
        ("Ms Lan", "The line is very noisy, could you say each digit clearly?", "Đường truyền ồn quá, anh đọc rõ từng chữ số được không?"),
        ("Mr George", "Sure. Zero, nine, four, then two, six, one.", "Được chứ. Không, chín, bốn, rồi hai, sáu, một."),
        ("Ms Lan", "Got it, thank you for repeating.", "Tôi nghe được rồi, cảm ơn anh đã đọc lại."),
        # 34 number given with plus sign
        ("Mr George", "My friend abroad gave me his number with a plus sign.", "Bạn tôi ở nước ngoài cho tôi số kèm dấu cộng."),
        ("Ms Lan", "That plus sign just means the country code, right?", "Dấu cộng đó nghĩa là mã quốc gia phải không?"),
        ("Mr George", "Exactly, plus one for his country.", "Đúng vậy, cộng một là mã nước của anh ấy."),
        # 35 driver calling at the gate
        ("Ms Lan", "The delivery driver is calling from the number on the app.", "Tài xế giao hàng đang gọi từ số trên ứng dụng."),
        ("Mr George", "I will answer it and let him in at the gate.", "Tôi sẽ nghe máy và cho anh ấy vào cổng."),
        ("Ms Lan", "Thanks, I am still tidying up inside.", "Cảm ơn anh, tôi vẫn đang dọn dẹp trong nhà."),
        # 36 old number no longer active
        ("Mr George", "I tried calling, but this old number is not active anymore.", "Tôi thử gọi rồi, nhưng số cũ này không còn hoạt động nữa."),
        ("Ms Lan", "Right, she changed it a few months ago.", "Đúng rồi, chị ấy đổi số mấy tháng trước rồi."),
        ("Mr George", "Do you happen to have the new one?", "Chị có tình cờ có số mới không?"),
        ("Ms Lan", "I do, let me send it to you.", "Có chứ, để tôi gửi cho anh."),
        # 37 number changed after moving house
        ("Ms Lan", "I changed my landline number after moving house.", "Tôi đổi số điện thoại bàn sau khi chuyển nhà."),
        ("Mr George", "Oh, I still have your old number saved.", "Ồ, tôi vẫn còn lưu số cũ của chị."),
        ("Ms Lan", "Please update it, the new one works much better now.", "Anh cập nhật lại nhé, số mới dùng ổn hơn nhiều."),
        # 38 closing - why getting it right matters
        ("Mr George", "It really matters to get every digit of a number right.", "Việc lấy đúng từng chữ số trong một số điện thoại thực sự quan trọng."),
        ("Ms Lan", "It does, one wrong digit and the call goes nowhere.", "Đúng vậy, chỉ cần sai một chữ số là cuộc gọi không tới đâu cả."),
        ("Mr George", "That is exactly why I always read it back.", "Chính vì vậy mà tôi luôn đọc lại để kiểm tra."),
        ("Ms Lan", "A good habit, and it saves everyone time.", "Một thói quen tốt, và nó tiết kiệm thời gian cho mọi người."),
    ],
}
