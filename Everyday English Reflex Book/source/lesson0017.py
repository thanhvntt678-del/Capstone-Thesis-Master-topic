# -*- coding: utf-8 -*-
LESSON_0017 = {
    'lesson_id': '0017',
    'cefr': 'A0 / Pre-A1',
    'domain': 'Communication',
    'en_title': 'Recognising and Responding to the First Practical Exchange About Phone Calls',
    'vi_title': 'Giao tiếp nền tảng: phone calls — the first practical exchange about phone calls',
    'intro_en': (
        "Ms Lan and Mr Robert are friends who often speak on the phone. Across many everyday moments "
        "-- answering the phone, a returned call, a wrong number, a bad signal, a voicemail, a missed "
        "call, call waiting, speakerphone, hanging up, confirming plans, an appointment call, a "
        "business call, calling family, a spam call, a dying battery, an international call, a group "
        "call, a video call, a disconnected call, asking for someone, leaving a message, a call during "
        "a meeting, a silenced phone, checking voicemail, a delayed callback, texting instead, a "
        "delivery call, customer service, an unknown number, a scheduled call, a polite goodbye, a "
        "phone number correction, and finally a follow-up call -- one of them repeatedly calls or "
        "answers the other, and each one responds naturally each time."
    ),
    'intro_vi': (
        "Chị Lan và anh Robert là bạn bè, thường xuyên nói chuyện qua điện thoại. Qua nhiều khoảnh khắc "
        "đời thường -- nghe máy, một cuộc gọi lại, một số điện thoại nhầm, sóng yếu, một tin nhắn thoại, "
        "một cuộc gọi nhỡ, cuộc gọi chờ, loa ngoài, cúp máy, xác nhận kế hoạch, một cuộc gọi về lịch "
        "hẹn, một cuộc gọi công việc, gọi cho người thân, một cuộc gọi rác, pin sắp hết, một cuộc gọi "
        "quốc tế, một cuộc gọi nhóm, một cuộc gọi video, một cuộc gọi bị ngắt, hỏi gặp ai đó, để lại lời "
        "nhắn, một cuộc gọi giữa buổi họp, điện thoại để chế độ im lặng, kiểm tra hộp thư thoại, một "
        "cuộc gọi lại trễ, nhắn tin thay vì gọi, một cuộc gọi về giao hàng, dịch vụ chăm sóc khách hàng, "
        "một số lạ gọi đến, một cuộc gọi đã hẹn trước, lời chào tạm biệt lịch sự, chỉnh sửa số điện "
        "thoại, và cuối cùng là một cuộc gọi theo dõi lại -- một người liên tục gọi hoặc nghe máy người "
        "kia, và mỗi người luôn đáp lại một cách tự nhiên."
    ),
    'turns': [
        # 1 answering the phone
        ("Mr Robert", "Hello, is this Lan?", "Alo, có phải chị Lan không?"),
        ("Ms Lan", "Yes, speaking. Who is this?", "Vâng, tôi đây. Ai đấy ạ?"),
        ("Mr Robert", "It is Robert, from the club.", "Robert đây, ở câu lạc bộ."),
        # 2 calling back
        ("Ms Lan", "Robert, sorry I missed your call earlier.", "Anh Robert, xin lỗi lúc nãy tôi lỡ cuộc gọi của anh."),
        ("Mr Robert", "No problem, thanks for calling back.", "Không sao đâu, cảm ơn chị đã gọi lại."),
        ("Ms Lan", "Of course, what did you need?", "Được chứ, anh cần gì vậy?"),
        # 3 wrong number
        ("Mr Robert", "Hello? Is this the Nguyen residence?", "Alo? Đây có phải nhà ông bà Nguyễn không ạ?"),
        ("Ms Lan", "I am sorry, you have the wrong number.", "Xin lỗi, anh gọi nhầm số rồi."),
        ("Mr Robert", "Oh, my apologies for the confusion.", "Ồ, xin lỗi vì đã làm phiền."),
        # 4 bad signal
        ("Ms Lan", "Robert, I can barely hear you. The signal is bad.", "Anh Robert, tôi gần như không nghe rõ. Sóng yếu quá."),
        ("Mr Robert", "Let me move to a better spot.", "Để tôi di chuyển đến chỗ sóng tốt hơn."),
        ("Ms Lan", "Thank you, try calling again.", "Cảm ơn anh, anh gọi lại thử nhé."),
        # 5 voicemail
        ("Mr Robert", "Lan, I left you a voicemail yesterday.", "Chị Lan, hôm qua tôi có để lại tin nhắn thoại cho chị."),
        ("Ms Lan", "Oh, I have not checked it yet.", "Ồ, tôi chưa nghe được."),
        ("Mr Robert", "No rush, it was not urgent.", "Không gấp đâu, chuyện không quan trọng lắm."),
        # 6 missed call
        ("Ms Lan", "Robert, I saw I had a missed call from you.", "Anh Robert, tôi thấy có cuộc gọi nhỡ từ anh."),
        ("Mr Robert", "Yes, I called about the meeting time.", "Vâng, tôi gọi để hỏi về giờ họp."),
        ("Ms Lan", "Ah, let me call you back now.", "À, để tôi gọi lại cho anh ngay."),
        # 7 call waiting
        ("Mr Robert", "Lan, could you hold on? I have another call.", "Chị Lan, chị chờ chút được không? Tôi có cuộc gọi khác đến."),
        ("Ms Lan", "Of course, take your time.", "Được chứ, anh cứ từ từ."),
        ("Mr Robert", "Thanks, I will make it short.", "Cảm ơn chị, tôi sẽ nói ngắn gọn thôi."),
        # 8 speakerphone
        ("Ms Lan", "Robert, I am putting you on speakerphone now.", "Anh Robert, tôi bật loa ngoài nhé."),
        ("Mr Robert", "No problem, go ahead.", "Không sao đâu, chị cứ bật đi."),
        ("Ms Lan", "Thanks, my hands are full right now.", "Cảm ơn anh, tay tôi đang bận việc khác."),
        # 9 hanging up
        ("Mr Robert", "Lan, I need to go now, talk soon.", "Chị Lan, tôi phải đi đây, nói chuyện sau nhé."),
        ("Ms Lan", "Okay, take care, bye for now.", "Được rồi, giữ gìn sức khỏe, tạm biệt nhé."),
        ("Mr Robert", "Bye, Lan.", "Tạm biệt, chị Lan."),
        # 10 returning a call
        ("Ms Lan", "Robert, you asked me to call you back.", "Anh Robert, anh nhờ tôi gọi lại phải không."),
        ("Mr Robert", "Yes, thank you for calling.", "Vâng, cảm ơn chị đã gọi."),
        ("Ms Lan", "Of course, what is going on?", "Được chứ, có chuyện gì vậy?"),
        # 11 confirming plans
        ("Mr Robert", "Lan, I am calling to confirm our lunch tomorrow.", "Chị Lan, tôi gọi để xác nhận bữa trưa ngày mai của mình."),
        ("Ms Lan", "Yes, that still works for me.", "Vâng, tôi vẫn ổn với kế hoạch đó."),
        ("Mr Robert", "Great, see you then.", "Tuyệt, hẹn gặp chị lúc đó."),
        # 12 appointment call
        ("Ms Lan", "Robert, I am calling about tomorrow's appointment.", "Anh Robert, tôi gọi để hỏi về lịch hẹn ngày mai."),
        ("Mr Robert", "Yes, everything is confirmed for ten o'clock.", "Vâng, mọi thứ đã xác nhận lúc mười giờ rồi."),
        ("Ms Lan", "Perfect, thank you for checking.", "Tuyệt, cảm ơn anh đã kiểm tra."),
        # 13 business call
        ("Mr Robert", "Lan, this is Robert calling from the office.", "Chị Lan, Robert gọi từ văn phòng đây."),
        ("Ms Lan", "Hello, Robert. How can I help you?", "Chào anh Robert. Tôi giúp gì được cho anh?"),
        ("Mr Robert", "I have a quick question about the invoice.", "Tôi có một câu hỏi nhanh về hóa đơn."),
        # 14 calling family
        ("Ms Lan", "Robert, could you call my sister for me?", "Anh Robert, anh gọi giúp tôi cho em gái tôi được không?"),
        ("Mr Robert", "Sure, what is her number?", "Được chứ, số của cô ấy là gì vậy?"),
        ("Ms Lan", "I will send it to you now.", "Tôi gửi cho anh ngay đây."),
        # 15 spam call
        ("Mr Robert", "Lan, did you get that strange call earlier?", "Chị Lan, lúc nãy chị có nhận được cuộc gọi lạ không?"),
        ("Ms Lan", "Yes, I think it was a spam call.", "Có chứ, tôi nghĩ đó là cuộc gọi rác."),
        ("Mr Robert", "I got one too, I just hung up.", "Tôi cũng nhận được một cuộc, tôi cúp máy luôn."),
        # 16 phone battery dying
        ("Ms Lan", "Robert, my phone battery is almost dead.", "Anh Robert, pin điện thoại tôi sắp hết rồi."),
        ("Mr Robert", "Okay, let us talk again later then.", "Được rồi, vậy lát nữa mình nói chuyện tiếp nhé."),
        ("Ms Lan", "Sounds good, I will charge it now.", "Được đấy, tôi sạc pin ngay đây."),
        # 17 international call
        ("Mr Robert", "Lan, are you calling from abroad right now?", "Chị Lan, giờ chị đang gọi từ nước ngoài à?"),
        ("Ms Lan", "Yes, I am using an international plan.", "Vâng, tôi đang dùng gói cước quốc tế."),
        ("Mr Robert", "Ah, that explains the delay.", "À, thảo nào lại có độ trễ."),
        # 18 group call
        ("Ms Lan", "Robert, could you join our group call at five?", "Anh Robert, anh tham gia cuộc gọi nhóm lúc năm giờ được không?"),
        ("Mr Robert", "Yes, I will be there.", "Được chứ, tôi sẽ tham gia."),
        ("Ms Lan", "Great, I will send the link.", "Tuyệt, tôi gửi đường dẫn cho anh."),
        # 19 video call
        ("Mr Robert", "Lan, shall we do a video call instead?", "Chị Lan, mình gọi video thay vì gọi thoại nhé?"),
        ("Ms Lan", "Sure, that works better for me too.", "Được chứ, vậy cũng hợp với tôi hơn."),
        ("Mr Robert", "Perfect, calling you now.", "Tuyệt, tôi gọi cho chị ngay đây."),
        # 20 disconnected call
        ("Ms Lan", "Robert, I think we got disconnected earlier.", "Anh Robert, hình như lúc nãy mình bị rớt cuộc gọi rồi."),
        ("Mr Robert", "Yes, sorry about that, my signal dropped.", "Vâng, xin lỗi chị, sóng của tôi bị mất."),
        ("Ms Lan", "No problem, let us continue now.", "Không sao đâu, mình tiếp tục nhé."),
        # 21 asking to speak to someone
        ("Mr Robert", "Hello, could I speak to Lan, please?", "Alo, cho tôi gặp chị Lan được không ạ?"),
        ("Ms Lan", "Speaking, how can I help?", "Tôi đây, tôi giúp gì được ạ?"),
        ("Mr Robert", "Hi Lan, it is Robert.", "Chào chị Lan, Robert đây."),
        # 22 leaving a message
        ("Ms Lan", "Robert, could you leave a message if I do not answer?", "Anh Robert, nếu tôi không bắt máy thì anh để lại lời nhắn nhé?"),
        ("Mr Robert", "Of course, I will let you know it is urgent.", "Được chứ, tôi sẽ báo là việc gấp."),
        ("Ms Lan", "Thank you, I feel much better knowing that.", "Cảm ơn anh, biết vậy tôi thấy yên tâm hơn nhiều."),
        # 23 call during a meeting
        ("Mr Robert", "Lan, sorry, I cannot talk right now, I am in a meeting.", "Chị Lan, xin lỗi, giờ tôi không nói chuyện được, tôi đang họp."),
        ("Ms Lan", "No worries, call me back later.", "Không sao đâu, lát nữa gọi lại cho tôi nhé."),
        ("Mr Robert", "I will, thank you for understanding.", "Tôi sẽ gọi, cảm ơn chị đã thông cảm."),
        # 24 phone on silent
        ("Ms Lan", "Robert, I did not hear my phone, it was on silent.", "Anh Robert, tôi không nghe thấy điện thoại, nó để chế độ im lặng."),
        ("Mr Robert", "That is okay, I figured as much.", "Không sao đâu, tôi cũng đoán vậy."),
        ("Ms Lan", "Sorry about that, what did you need?", "Xin lỗi anh nhé, anh cần gì vậy?"),
        # 25 checking voicemail
        ("Mr Robert", "Lan, did you get a chance to check your voicemail?", "Chị Lan, chị nghe hộp thư thoại chưa vậy?"),
        ("Ms Lan", "Yes, I listened to it this morning.", "Rồi, sáng nay tôi nghe rồi."),
        ("Mr Robert", "Good, let me know your thoughts.", "Tốt, cho tôi biết ý kiến của chị nhé."),
        # 26 delayed callback
        ("Ms Lan", "Robert, sorry for the late callback.", "Anh Robert, xin lỗi vì tôi gọi lại trễ."),
        ("Mr Robert", "No problem at all, I understand you are busy.", "Không sao đâu, tôi hiểu chị bận mà."),
        ("Ms Lan", "Thank you for your patience.", "Cảm ơn anh đã kiên nhẫn."),
        # 27 texting instead
        ("Mr Robert", "Lan, would it be easier if I just texted you?", "Chị Lan, tôi nhắn tin cho chị có tiện hơn không?"),
        ("Ms Lan", "Yes, that works better for me right now.", "Có chứ, giờ vậy hợp với tôi hơn."),
        ("Mr Robert", "Sure, I will send a message instead.", "Được, tôi nhắn tin thay vì gọi vậy."),
        # 28 delivery call
        ("Ms Lan", "Robert, someone called about a delivery for you.", "Anh Robert, có người gọi hỏi về gói hàng của anh đấy."),
        ("Mr Robert", "Oh, that must be my package.", "Ồ, chắc là gói hàng của tôi rồi."),
        ("Ms Lan", "They said they will call again later.", "Họ nói sẽ gọi lại sau."),
        # 29 customer service call
        ("Mr Robert", "Lan, I am on hold with customer service right now.", "Chị Lan, tôi đang chờ máy với bộ phận chăm sóc khách hàng."),
        ("Ms Lan", "That sounds frustrating, good luck.", "Nghe bực thật đấy, chúc anh may mắn."),
        ("Mr Robert", "Thanks, hopefully it will not take too long.", "Cảm ơn chị, mong là không lâu quá."),
        # 30 unknown number
        ("Ms Lan", "Robert, an unknown number just called me.", "Anh Robert, vừa có một số lạ gọi cho tôi."),
        ("Mr Robert", "Did you answer it?", "Chị có bắt máy không?"),
        ("Ms Lan", "No, I let it go to voicemail.", "Không, tôi để nó chuyển sang hộp thư thoại."),
        # 31 scheduled call
        ("Mr Robert", "Lan, we still have our call scheduled for three, right?", "Chị Lan, mình vẫn còn hẹn gọi lúc ba giờ đúng không?"),
        ("Ms Lan", "Yes, I have it marked on my calendar.", "Vâng, tôi có ghi vào lịch rồi."),
        ("Mr Robert", "Perfect, talk to you then.", "Tuyệt, hẹn nói chuyện lúc đó."),
        # 32 polite goodbye
        ("Ms Lan", "Robert, thank you for calling, I really enjoyed our chat.", "Anh Robert, cảm ơn anh đã gọi, tôi thích cuộc trò chuyện này lắm."),
        ("Mr Robert", "Me too, let us talk again soon.", "Tôi cũng vậy, mình nói chuyện lại sớm nhé."),
        ("Ms Lan", "Definitely, take care.", "Chắc chắn rồi, anh giữ gìn sức khỏe nhé."),
        # 33 phone number correction
        ("Mr Robert", "Lan, I think I have your old phone number.", "Chị Lan, hình như tôi vẫn lưu số điện thoại cũ của chị."),
        ("Ms Lan", "Oh, let me give you my new one.", "Ồ, để tôi cho anh số mới của tôi."),
        ("Mr Robert", "Thank you, I will save it right now.", "Cảm ơn chị, tôi lưu lại ngay đây."),
        # 34 follow-up call wrap-up
        ("Ms Lan", "Robert, thanks for following up with me today.", "Anh Robert, cảm ơn anh đã gọi theo dõi lại hôm nay."),
        ("Mr Robert", "Of course, I wanted to make sure everything was clear.", "Có gì đâu, tôi muốn chắc là mọi thứ đã rõ ràng."),
        ("Ms Lan", "It really was, I appreciate the call.", "Rõ ràng thật đấy, tôi cảm kích cuộc gọi này lắm."),
        ("Mr Robert", "Glad to hear it, speak soon.", "Mừng khi nghe vậy, nói chuyện lại sớm nhé."),
        # 35 asking about a dropped call earlier in the day
        ("Ms Lan", "Robert, why did the call drop this morning?", "Anh Robert, sao sáng nay cuộc gọi lại bị rớt vậy?"),
        ("Mr Robert", "I am not sure, my network was unstable.", "Tôi không chắc, mạng của tôi không ổn định lắm."),
        ("Ms Lan", "That happens to me sometimes too.", "Thỉnh thoảng tôi cũng bị vậy."),
        # 36 confirming the right time zone
        ("Mr Robert", "Lan, what time zone are you calling from?", "Chị Lan, chị gọi từ múi giờ nào vậy?"),
        ("Ms Lan", "I am still on local time here.", "Tôi vẫn đang ở múi giờ địa phương đây."),
        ("Mr Robert", "Good, that makes scheduling easier.", "Tốt, vậy lên lịch dễ hơn."),
        # 37 asking someone to speak more slowly
        ("Ms Lan", "Robert, could you speak a little more slowly?", "Anh Robert, anh nói chậm lại một chút được không?"),
        ("Mr Robert", "Of course, is this better?", "Được chứ, vậy có ổn hơn không?"),
        ("Ms Lan", "Yes, much clearer now, thank you.", "Có chứ, rõ hơn nhiều rồi, cảm ơn anh."),
        # 38 a call reminder app notification
        ("Mr Robert", "Lan, my phone just reminded me to call you.", "Chị Lan, điện thoại tôi vừa nhắc gọi cho chị đấy."),
        ("Ms Lan", "Perfect timing, I was just thinking of you.", "Đúng lúc thật, tôi vừa mới nghĩ đến anh."),
        ("Mr Robert", "What a coincidence.", "Trùng hợp thật đấy."),
        # 39 asking someone to repeat something
        ("Ms Lan", "Robert, could you say that last part again, please?", "Anh Robert, anh nói lại phần cuối được không?"),
        ("Mr Robert", "Of course, I said the meeting moved to Monday.", "Được chứ, tôi nói là cuộc họp đổi sang thứ Hai."),
        ("Ms Lan", "Ah, thank you, now I have it.", "À, cảm ơn anh, giờ tôi rõ rồi."),
        # 40 confirming a callback number
        ("Mr Robert", "Lan, what is the best number to call you back on?", "Chị Lan, số nào gọi lại chị dễ nhất vậy?"),
        ("Ms Lan", "This same number is fine.", "Số này đây là được rồi."),
        ("Mr Robert", "Good, I will use it later.", "Tốt, lát nữa tôi dùng số này gọi."),
        # 41 phone on airplane mode
        ("Ms Lan", "Robert, sorry, my phone was on airplane mode earlier.", "Anh Robert, xin lỗi, lúc nãy điện thoại tôi để chế độ máy bay."),
        ("Mr Robert", "Ah, that explains why I could not reach you.", "À, thảo nào tôi gọi không được."),
        ("Ms Lan", "Sorry about that, I have turned it off now.", "Xin lỗi anh nhé, giờ tôi tắt chế độ đó rồi."),
        # 42 a conference call PIN
        ("Mr Robert", "Lan, do you have the PIN for the conference call?", "Chị Lan, chị có mã PIN cho cuộc gọi hội nghị không?"),
        ("Ms Lan", "Yes, it is in the invitation email.", "Có chứ, nó nằm trong email mời họp đấy."),
        ("Mr Robert", "Thank you, let me find it now.", "Cảm ơn chị, để tôi tìm ngay đây."),
    ],
}
