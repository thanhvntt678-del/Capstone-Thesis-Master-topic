# -*- coding: utf-8 -*-
LESSON_0024 = {
    'lesson_id': '0024',
    'cefr': 'A0 / Pre-A1',
    'domain': 'Food',
    'en_title': 'Recognising and Responding to Choosing a Drink',
    'vi_title': 'Giao tiếp nền tảng: food & drink — choosing a drink',
    'intro_en': (
        "Ms Lan and Ms Claire meet often for coffee or tea and always talk through what drink to order. "
        "Across many everyday moments -- choosing between coffee and tea, deciding hot or iced, ordering "
        "a smoothie, picking a size, asking for less sugar, choosing sparkling or still water, a fruit "
        "juice option, deciding on milk or no milk, ordering a soft drink, a herbal tea choice, choosing "
        "decaf, asking what is recommended, a seasonal drink special, choosing a straw or no straw, "
        "ordering for takeaway, asking about caffeine, choosing a drink for a friend, a drink that is too "
        "sweet, asking for extra ice, a warm drink on a cold day, a cold drink on a hot day, choosing "
        "between two similar options, asking for a refill, a drink that arrived wrong, deciding on a "
        "cocktail-free option, choosing sparkling wine for a toast, a child's drink order, asking for tap "
        "water, a drink paired with dessert, choosing between two coffee shops, a rare specialty drink, "
        "asking the price of a drink, ordering the same as before, trying a new flavour, choosing a "
        "drink to share, deciding against caffeine at night, and finally why taking a moment to choose "
        "the right drink matters -- Ms Claire often asks Ms Lan what she would like, and Ms Lan responds "
        "thoughtfully every time."
    ),
    'intro_vi': (
        "Chị Lan và chị Claire thường gặp nhau uống cà phê hoặc trà, và luôn bàn bạc xem nên gọi loại "
        "nước gì. Qua nhiều khoảnh khắc đời thường -- chọn giữa cà phê và trà, quyết định nóng hay đá, "
        "gọi sinh tố, chọn cỡ ly, xin ít đường hơn, chọn nước có ga hay không ga, chọn nước ép trái cây, "
        "quyết định có sữa hay không, gọi nước ngọt, chọn trà thảo mộc, chọn cà phê không caffeine, hỏi "
        "món nào được gợi ý, một loại nước theo mùa, chọn có ống hút hay không, gọi mang đi, hỏi về hàm "
        "lượng caffeine, chọn nước cho bạn, một ly nước quá ngọt, xin thêm đá, một ly nước ấm trong ngày "
        "lạnh, một ly nước lạnh trong ngày nóng, chọn giữa hai món tương tự nhau, xin châm thêm, một ly "
        "nước bị mang nhầm, chọn món không cồn, chọn rượu vang sủi để nâng ly chúc mừng, gọi nước cho "
        "trẻ em, xin nước lọc, một loại nước dùng kèm tráng miệng, chọn giữa hai quán cà phê, một loại "
        "nước đặc biệt hiếm có, hỏi giá của một ly nước, gọi giống như lần trước, thử một hương vị mới, "
        "chọn một ly để chia nhau, quyết định tránh caffeine vào buổi tối, và cuối cùng là vì sao dành "
        "thời gian chọn đúng loại nước lại quan trọng -- chị Claire thường hỏi chị Lan muốn uống gì, và "
        "chị Lan luôn trả lời một cách chu đáo mỗi lần."
    ),
    'turns': [
        # 1 coffee vs tea
        ("Ms Claire", "Lan, would you like coffee or tea today?", "Chị Lan, hôm nay chị muốn cà phê hay trà?"),
        ("Ms Lan", "I think I will have coffee, please.", "Tôi nghĩ tôi sẽ uống cà phê nhé."),
        ("Ms Claire", "Coffee it is, good choice.", "Vậy là cà phê nhé, lựa chọn hay đấy."),
        # 2 hot or iced
        ("Ms Claire", "Would you like that hot or iced?", "Chị muốn nóng hay đá?"),
        ("Ms Lan", "Iced, please, it is quite warm outside.", "Cho đá nhé, ngoài trời nóng quá."),
        ("Ms Claire", "Iced coffee coming right up.", "Cà phê đá sắp có ngay đây."),
        # 3 smoothie
        ("Ms Lan", "Actually, could I try a smoothie instead?", "Thật ra, cho tôi thử sinh tố thay vào được không?"),
        ("Ms Claire", "Sure, they have mango and berry today.", "Được chứ, hôm nay có xoài và các loại quả mọng."),
        ("Ms Lan", "Mango sounds wonderful, I will have that.", "Xoài nghe tuyệt đấy, tôi chọn cái đó."),
        # 4 picking a size
        ("Ms Claire", "What size would you like, small or large?", "Chị muốn cỡ nào, nhỏ hay lớn?"),
        ("Ms Lan", "A small one is enough for me, thanks.", "Cỡ nhỏ là đủ cho tôi rồi, cảm ơn chị."),
        ("Ms Claire", "Small it is, noted.", "Vậy là cỡ nhỏ nhé, tôi ghi lại rồi."),
        # 5 less sugar
        ("Ms Lan", "Could I have less sugar in mine, please?", "Cho tôi ít đường hơn được không?"),
        ("Ms Claire", "Of course, I will mention that to them.", "Được chứ, tôi sẽ nói với họ."),
        ("Ms Lan", "Thank you, I appreciate that.", "Cảm ơn chị, tôi rất trân trọng điều đó."),
        # 6 sparkling or still
        ("Ms Claire", "Sparkling water or still water for you?", "Chị muốn nước có ga hay không ga?"),
        ("Ms Lan", "Still water is fine, thank you.", "Nước không ga là được rồi, cảm ơn chị."),
        ("Ms Claire", "Still water, coming right away.", "Nước không ga, sắp mang đến ngay."),
        # 7 fruit juice
        ("Ms Lan", "Do they have any fresh fruit juice here?", "Ở đây có nước ép trái cây tươi không?"),
        ("Ms Claire", "Yes, orange juice is very popular here.", "Có chứ, nước cam ở đây rất được ưa chuộng."),
        ("Ms Lan", "Orange juice sounds refreshing, I will get that.", "Nước cam nghe mát lạnh đấy, tôi chọn cái đó."),
        # 8 milk or no milk
        ("Ms Claire", "Would you like milk in your tea?", "Chị muốn thêm sữa vào trà không?"),
        ("Ms Lan", "No milk for me, just plain tea, thanks.", "Không cần sữa đâu, trà thường thôi, cảm ơn chị."),
        ("Ms Claire", "Plain tea, got it.", "Trà thường, tôi ghi lại rồi."),
        # 9 soft drink
        ("Ms Lan", "My nephew would like a soft drink, please.", "Cháu trai tôi muốn một ly nước ngọt."),
        ("Ms Claire", "Sure, they have cola and lemon soda.", "Được chứ, ở đây có cola và soda chanh."),
        ("Ms Lan", "He will pick cola, thank you.", "Cháu sẽ chọn cola, cảm ơn chị."),
        # 10 herbal tea
        ("Ms Claire", "Would you be interested in a herbal tea instead?", "Chị có muốn thử trà thảo mộc thay vào không?"),
        ("Ms Lan", "That sounds nice, what flavours do they have?", "Nghe hay đấy, họ có những hương vị nào?"),
        ("Ms Claire", "Chamomile and peppermint are both available.", "Có cả hoa cúc và bạc hà."),
        # 11 decaf
        ("Ms Lan", "Could I have a decaf coffee this time?", "Lần này cho tôi cà phê không caffeine được không?"),
        ("Ms Claire", "Of course, decaf is easy to make here.", "Được chứ, ở đây pha loại đó dễ lắm."),
        ("Ms Lan", "Great, I do not want to stay up all night.", "Tốt quá, tôi không muốn thức trắng đêm."),
        # 12 asking what is recommended
        ("Ms Claire", "What would you recommend for someone new here?", "Chị gợi ý gì cho người mới đến đây lần đầu?"),
        ("Ms Lan", "The caramel latte is always a favourite.", "Latte caramel lúc nào cũng được yêu thích."),
        ("Ms Claire", "I will try that, thank you for the tip.", "Tôi sẽ thử món đó, cảm ơn chị đã gợi ý."),
        # 13 seasonal special
        ("Ms Lan", "Is there a seasonal drink special today?", "Hôm nay có món nước đặc biệt theo mùa không?"),
        ("Ms Claire", "Yes, they have a pumpkin spice latte.", "Có chứ, họ có latte bí ngô gia vị."),
        ("Ms Lan", "I have been wanting to try that.", "Tôi vẫn muốn thử món đó lâu rồi."),
        # 14 straw or no straw
        ("Ms Claire", "Would you like a straw with your drink?", "Chị có muốn ống hút cho ly nước không?"),
        ("Ms Lan", "No straw for me, thank you.", "Không cần ống hút đâu, cảm ơn chị."),
        ("Ms Claire", "No straw, noted, that helps the environment too.", "Không ống hút, tôi ghi lại, cũng tốt cho môi trường nữa."),
        # 15 takeaway
        ("Ms Lan", "Could I get this drink to take away, please?", "Cho tôi mang ly nước này đi được không?"),
        ("Ms Claire", "Sure, I will ask for a takeaway cup.", "Được chứ, tôi sẽ xin ly mang đi."),
        ("Ms Lan", "Thanks, I am in a bit of a rush.", "Cảm ơn chị, tôi hơi vội một chút."),
        # 16 asking about caffeine
        ("Ms Claire", "Does this drink have a lot of caffeine?", "Ly nước này có nhiều caffeine không?"),
        ("Ms Lan", "It has a moderate amount, not too strong.", "Có mức vừa phải thôi, không quá mạnh."),
        ("Ms Claire", "Good, that should still let me sleep tonight.", "Tốt, vậy tối nay tôi vẫn ngủ được."),
        # 17 choosing for a friend
        ("Ms Lan", "What should I order for my friend who is joining us?", "Tôi nên gọi gì cho bạn tôi sắp đến vậy?"),
        ("Ms Claire", "Maybe wait until she arrives to ask her.", "Có lẽ đợi bạn đến rồi hỏi trực tiếp thì hơn."),
        ("Ms Lan", "Good point, I will wait for her.", "Có lý đấy, tôi sẽ đợi bạn."),
        # 18 too sweet
        ("Ms Claire", "How is your drink? Is it good?", "Ly nước của chị thế nào? Ngon không?"),
        ("Ms Lan", "It is a little too sweet for my taste.", "Hơi ngọt quá so với khẩu vị của tôi."),
        ("Ms Claire", "You can ask them to adjust it next time.", "Lần sau chị có thể nhờ họ điều chỉnh lại."),
        # 19 extra ice
        ("Ms Lan", "Could I get some extra ice in this, please?", "Cho tôi thêm đá vào ly này được không?"),
        ("Ms Claire", "Sure, I will let the server know.", "Được chứ, tôi sẽ báo với nhân viên."),
        ("Ms Lan", "Thanks, it is quite hot today.", "Cảm ơn chị, hôm nay nóng quá."),
        # 20 warm drink on a cold day
        ("Ms Claire", "It is freezing outside, shall we get something warm?", "Ngoài trời lạnh cóng, mình gọi món gì ấm nhé?"),
        ("Ms Lan", "Yes, hot chocolate sounds perfect right now.", "Vâng, sô cô la nóng nghe hợp lúc này quá."),
        ("Ms Claire", "Great idea, I will order two.", "Ý hay đấy, tôi gọi hai ly luôn."),
        # 21 cold drink on a hot day
        ("Ms Lan", "It is so hot, I need something cold.", "Nóng quá, tôi cần thứ gì mát lạnh."),
        ("Ms Claire", "Iced lemonade would be very refreshing.", "Chanh đá sẽ rất mát và dễ chịu đấy."),
        ("Ms Lan", "That sounds perfect, let us order it.", "Nghe hợp lý lắm, mình gọi món đó nhé."),
        # 22 choosing between two similar options
        ("Ms Claire", "Latte or cappuccino, which do you prefer?", "Chị thích latte hay cappuccino hơn?"),
        ("Ms Lan", "I usually lean towards cappuccino, actually.", "Thật ra tôi thường thích cappuccino hơn."),
        ("Ms Claire", "Cappuccino it is, then.", "Vậy thì cappuccino nhé."),
        # 23 asking for a refill
        ("Ms Lan", "Could I get a refill on my water, please?", "Cho tôi châm thêm nước được không?"),
        ("Ms Claire", "Of course, I will ask them to top it up.", "Được chứ, tôi sẽ nhờ họ rót thêm."),
        ("Ms Lan", "Thank you, I am quite thirsty today.", "Cảm ơn chị, hôm nay tôi khát nước quá."),
        # 24 drink arrived wrong
        ("Ms Claire", "I think this is not what I ordered.", "Tôi nghĩ đây không phải món tôi gọi."),
        ("Ms Lan", "Let us ask the server to check the order.", "Mình nhờ nhân viên kiểm tra lại đơn hàng nhé."),
        ("Ms Claire", "Good idea, thank you for noticing.", "Ý hay đấy, cảm ơn chị đã để ý."),
        # 25 non-alcoholic option
        ("Ms Lan", "Is there a non-alcoholic option on the menu?", "Trong thực đơn có món không cồn nào không?"),
        ("Ms Claire", "Yes, they have a mocktail with berries.", "Có chứ, họ có mocktail với các loại quả mọng."),
        ("Ms Lan", "That sounds lovely, I will try it.", "Nghe hay đấy, tôi sẽ thử món đó."),
        # 26 sparkling wine for a toast
        ("Ms Claire", "Shall we get sparkling wine to celebrate?", "Mình gọi rượu vang sủi để ăn mừng nhé?"),
        ("Ms Lan", "Yes, this is a perfect occasion for it.", "Vâng, dịp này quá hợp để làm vậy rồi."),
        ("Ms Claire", "Wonderful, let us raise a toast then.", "Tuyệt, vậy mình cùng nâng ly nhé."),
        # 27 child's drink order
        ("Ms Lan", "What would your daughter like to drink?", "Con gái chị muốn uống gì vậy?"),
        ("Ms Claire", "She usually asks for apple juice.", "Bé thường xin nước ép táo."),
        ("Ms Lan", "Apple juice, I will add that to the order.", "Nước ép táo, tôi sẽ thêm vào đơn hàng."),
        # 28 asking for tap water
        ("Ms Claire", "Could we also get a jug of tap water?", "Mình xin thêm một bình nước lọc được không?"),
        ("Ms Lan", "Good idea, let us ask for that too.", "Ý hay đấy, mình xin luôn nhé."),
        ("Ms Claire", "It always helps to have water on the table.", "Có nước trên bàn lúc nào cũng tiện."),
        # 29 drink with dessert
        ("Ms Lan", "What drink would go well with this cake?", "Món nước nào hợp với chiếc bánh này vậy?"),
        ("Ms Claire", "A light tea usually pairs nicely with cake.", "Trà nhẹ thường hợp với bánh ngọt lắm."),
        ("Ms Lan", "Good suggestion, I will order that.", "Gợi ý hay đấy, tôi sẽ gọi món đó."),
        # 30 choosing between two coffee shops
        ("Ms Claire", "Should we go to this cafe or the one nearby?", "Mình đến quán này hay quán gần đây kia?"),
        ("Ms Lan", "This one has better iced drinks, I think.", "Tôi nghĩ quán này có đồ uống đá ngon hơn."),
        ("Ms Claire", "Let us stay here then.", "Vậy mình ở lại đây nhé."),
        # 31 rare specialty drink
        ("Ms Lan", "I heard they have a rare specialty drink here.", "Tôi nghe nói ở đây có một món đặc biệt hiếm có."),
        ("Ms Claire", "Yes, it is a lavender honey latte.", "Đúng vậy, đó là latte mật ong hoa oải hương."),
        ("Ms Lan", "That sounds unusual, let us try it.", "Nghe lạ đấy, mình thử xem sao."),
        # 32 asking the price
        ("Ms Claire", "Do you know how much this drink costs?", "Chị có biết ly nước này giá bao nhiêu không?"),
        ("Ms Lan", "I believe it is around forty thousand dong.", "Tôi nghĩ khoảng bốn mươi nghìn đồng."),
        ("Ms Claire", "That seems reasonable for the size.", "Nghe hợp lý so với dung tích của ly."),
        # 33 ordering the same as before
        ("Ms Lan", "I will just have the same as last time.", "Tôi cứ gọi giống lần trước vậy."),
        ("Ms Claire", "The iced coffee with less sugar, right?", "Cà phê đá ít đường phải không?"),
        ("Ms Lan", "Exactly, you remembered perfectly.", "Đúng vậy, chị nhớ chính xác luôn."),
        # 34 trying a new flavour
        ("Ms Claire", "Would you like to try something new today?", "Hôm nay chị có muốn thử vị gì mới không?"),
        ("Ms Lan", "Sure, let us try the passion fruit tea.", "Được chứ, mình thử trà chanh dây xem."),
        ("Ms Claire", "That is a fun choice, I am curious too.", "Lựa chọn thú vị đấy, tôi cũng tò mò."),
        # 35 choosing a drink to share
        ("Ms Lan", "Shall we just share one large drink together?", "Mình chia nhau một ly lớn thôi nhé?"),
        ("Ms Claire", "Sounds good, that way we can both try it.", "Nghe hay đấy, vậy cả hai đều được thử."),
        ("Ms Lan", "Perfect, let us order the mango smoothie then.", "Tuyệt, vậy mình gọi sinh tố xoài nhé."),
        # 36 deciding against caffeine at night
        ("Ms Claire", "It is quite late, maybe skip the caffeine tonight?", "Cũng khá muộn rồi, tối nay bỏ caffeine nhé?"),
        ("Ms Lan", "You are right, I will have herbal tea instead.", "Chị nói đúng, tôi sẽ uống trà thảo mộc thay vào."),
        ("Ms Claire", "Good choice, you will sleep much better.", "Lựa chọn hay đấy, chị sẽ ngủ ngon hơn nhiều."),
        # 37 asking about ingredients
        ("Ms Lan", "Does this smoothie contain any nuts?", "Ly sinh tố này có chứa hạt gì không?"),
        ("Ms Claire", "Let me check the menu for you.", "Để tôi kiểm tra thực đơn giúp chị."),
        ("Ms Lan", "Thank you, I need to be careful about that.", "Cảm ơn chị, tôi cần cẩn thận với chuyện đó."),
        # 38 asking for a lid on a hot drink
        ("Ms Lan", "Could I get a lid for this hot chocolate, please?", "Cho tôi xin nắp cho ly sô cô la nóng này được không?"),
        ("Ms Claire", "Sure, that will stop it from spilling in the car.", "Được chứ, vậy sẽ khỏi đổ trong xe."),
        ("Ms Lan", "Thanks, I always worry about that on the drive home.", "Cảm ơn chị, tôi hay lo chuyện đó lúc lái xe về."),
        # 39 oat milk alternative
        ("Ms Claire", "Would you like oat milk instead of regular milk today?", "Hôm nay chị có muốn dùng sữa yến mạch thay sữa thường không?"),
        ("Ms Lan", "Yes, please, I am trying to cut down on dairy.", "Vâng, cho tôi nhé, tôi đang cố giảm sữa động vật."),
        ("Ms Claire", "Oat milk works really well in coffee too.", "Sữa yến mạch pha cà phê cũng ngon lắm."),
        # 40 bubble tea with tapioca pearls
        ("Ms Lan", "Could I add tapioca pearls to my bubble tea?", "Cho tôi thêm trân châu vào trà sữa được không?"),
        ("Ms Claire", "Sure, would you like regular or the chewier kind?", "Được chứ, chị muốn loại thường hay loại dai hơn?"),
        ("Ms Lan", "The chewier kind sounds more fun to try.", "Loại dai hơn nghe thú vị hơn để thử."),
        # 41 asking for a drink not too hot
        ("Ms Claire", "Could you ask them to make it not too hot?", "Chị nhờ họ pha đừng nóng quá được không?"),
        ("Ms Lan", "Sure, I will mention that at the counter.", "Được chứ, tôi sẽ nói ở quầy."),
        ("Ms Claire", "Thanks, my mouth is still sensitive from the dentist.", "Cảm ơn chị, miệng tôi vẫn còn nhạy cảm sau khi khám răng."),
        # 42 a drink out of stock
        ("Ms Lan", "They just told me the mango smoothie is sold out.", "Họ vừa báo hết sinh tố xoài rồi."),
        ("Ms Claire", "That is a shame, what will you order instead?", "Tiếc quá, vậy chị định gọi gì thay vào?"),
        ("Ms Lan", "I will try the strawberry one instead.", "Tôi sẽ thử vị dâu thay vào."),
        # 43 asking for a weaker coffee
        ("Ms Claire", "Could you ask them to make the coffee a bit weaker?", "Chị nhờ họ pha cà phê nhạt hơn chút được không?"),
        ("Ms Lan", "Sure, strong coffee makes my heart race a little.", "Được chứ, cà phê đậm làm tim tôi đập nhanh hơn chút."),
        ("Ms Claire", "That makes sense, I will let them know.", "Vậy hợp lý đấy, tôi sẽ nói với họ."),
        # 44 bringing a reusable cup for a discount
        ("Ms Lan", "I brought my own cup, do they still give a discount?", "Tôi mang theo ly riêng, vẫn được giảm giá chứ?"),
        ("Ms Claire", "Yes, most cafes here take off a small amount.", "Có chứ, hầu hết quán ở đây giảm một chút."),
        ("Ms Lan", "Great, it is nice to save money and reduce waste.", "Tốt quá, vừa tiết kiệm vừa giảm rác thải."),
        # 45 closing - why choosing carefully matters
        ("Ms Claire", "It is nice to take a moment choosing the right drink.", "Thật hay khi dành chút thời gian chọn đúng loại nước."),
        ("Ms Lan", "It really is, the right drink makes the whole visit better.", "Đúng vậy, chọn đúng nước làm cả buổi gặp gỡ vui hơn hẳn."),
        ("Ms Claire", "That is exactly why I always ask before ordering.", "Chính vì vậy mà tôi luôn hỏi trước khi gọi món."),
        ("Ms Lan", "And I always appreciate being asked.", "Và tôi luôn thấy vui khi được hỏi ý kiến."),
    ],
}
