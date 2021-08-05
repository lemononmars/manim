from sys import builtin_module_names
from manim import *
from MeepleCreature.MeepleCreature import *

NUM_PLAYERS = 4

class Movie(Scene):
    def construct(self):
        self.MC = MeepleCreature()
        self.add(self.MC)
        self.intro()
        #self.toc()
        #self.tictactoe()
        #self.game_structure()
        #self.turn_order()

    def intro(self):
        self.MC.to_edge(DOWN)
        text1 = Text("สวัสดีครับ\nผมชื่อกลครับ", font = "Anakotmai Light", line_spacing= 4)
        text1.set_color(random_bright_color()).scale(1.5)
        text2 = Text("วันนี้เรามาศึกษา\nกลไกในบอร์ดเกมกัน", font = "Anakotmai Light", line_spacing = 3)
        text2.set_color(random_bright_color()).scale(1.5)
        self.play(Create(self.MC))
        self.play(Blink(self.MC))
        
        self.play(MeepleCreatureSays(
            self.MC, text1, 
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking",
            is_looking_direction_purposeful = False,
        ))

        self.wait()
        self.play(Blink(self.MC))
        self.play(RemoveMeepleCreatureBubble(self.MC))
        self.play(MeepleCreatureSays(
            self.MC, text2, 
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking",
            is_looking_direction_purposeful = False,
        ))
        self.play(Blink(self.MC))

        book = ImageMobject("book_cover")
        book.shift(UP + 4*RIGHT).scale(2.5)
        self.play(FadeIn(book, shift = DOWN))
        self.MC.look_at(book)
        self.wait(1)

        self.play(RemoveMeepleCreatureBubble(self.MC))
        self.play(FadeOut(self.MC, shift = DOWN))

        author_image = ImageMobject("geoff").scale(2)
        author_title = Text(f'Geoffrey Engelstein', font = "Prompt")
        author = Group(author_image, author_title).arrange(DOWN)

        author.shift(UP + 3*LEFT)
        self.play(FadeIn(author_image, shift = DOWN))
        self.play(Write(author_title))

        quote = Paragraph(f'Building Blocks of Tabletop Game Design: An Encyclopedia of Mechanisms\ncompiles hundreds of different mechanisms, organized by category.\nEach has a description of how it works, discussion of its pros and cons,\nhow it can be implemented, and examples of specific games that use it.', font = "Prompt").scale(0.6).set_color(GOLD_A)
        quote.to_edge(LEFT, buff = 1).shift(2.5*DOWN)
        self.play(ShowCreation(quote), run_time = 15) #13 seconds to read

        self.play(AnimationGroup(
            FadeOut(quote, shift = DOWN),
            FadeOut(author, shift = DOWN),
            FadeOut(book, shift = DOWN)
        ))
        self.play(FadeIn(self.MC, shift = DOWN))

    def toc(self):
        
        topics = [
            "Game Structure",
            "Turn Order and Structure",
            "Actions",
            "Resolution",
            "Game End and Victory",
            "Uncertainty",
            "Economics",
            "Auctions",
            "Worker Placement",
            "Movement",
            "Area Control",
            "Set Collection",
            "Card Mechanism"
            ]
        
        topics = ["Game Structure"] # overwrite for shorter animation 

        self.play(
            MoveAlongPath(self.MC, Line(self.MC.get_center(), 5*RIGHT + 2*DOWN), rate_func = smooth)
        )

        text = []
        for i in range(0,len(topics)):
            newtitle = Text(str(i+1) + ") " + topics[i], font = "Prompt").set_color(random_bright_color())
            text.append(newtitle)
        
        t = VGroup(*text).arrange(DOWN, center = False, aligned_edge = LEFT, buff = 0.1)
        t.to_corner(UL)

        for i in t:
            self.MC.look_at(i)
            self.play(Write(i))
            self.play(Blink(self.MC))

        text = Text("ทำไมเยอะจัง?", font = "Anakotmai Light", line_spacing = 3)
        text.set_color(random_bright_color()).scale(1.5)
        
        self.play(Blink(self.MC))
        self.play(MeepleCreatureSays(
            self.MC, text, 
            bubble_class = ThoughtBubble,
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking",
            is_looking_direction_purposeful = True,
        ))
        self.play(Blink(self.MC))
        self.play(RemoveMeepleCreatureBubble(self.MC))

    def tictactoe(self):
        self.add_sound("narrate")
        self.add_sound("windrider_edited")
        self.MC2 = Meeple(color = RED, start_corner = DL)
        self.MC.to_corner(DR).look_at(ORIGIN)
        self.MC2.to_corner(DL).look_at(ORIGIN)
        
        line_endpoints = [
            [3*UP + LEFT, 3*DOWN + LEFT], 
            [3*UP + RIGHT, 3*DOWN + RIGHT], 
            [3*LEFT + UP, 3*RIGHT + UP],
            [3*LEFT + DOWN, 3*RIGHT + DOWN]
        ]

        self.play(FadeInFromDown(self.MC2))
        self.play(FadeInFromDown(self.MC))
        
        #create tictactoe grid
        lines = [Line(start = line_endpoints[i][0], end = line_endpoints[i][1]) for i in range(len(line_endpoints))]
        self.play(AnimationGroup(
            *[ShowCreation(l, run_time = 1) for l in lines],
            lag_ratio = 0.2
        ))

        title = Text("Tic Tac Toe", color = GREEN_A).scale(1.2)
        title.to_edge(DOWN)
        self.play(FadeInFromDown(title))

        self.wait(7-self.time)
        text = Text("เกมนี้ประกอบด้วย\nกลไกอะไรบ้าง?", line_spacing = 3)
        self.play(MeepleCreatureSays(
            self.MC, text, 
            bubble_kwargs = {"height" : 4, "width" : 8},
            target_mode="speaking",
            is_looking_direction_purposeful = True,
        ))
        self.play(Blink(self.MC))
        self.play(RemoveMeepleCreatureBubble(self.MC))

        #add sequence of play
        tictactoe_plays = [(1,1), (1,0), (0,0), (2,2), (0,1), (0,2), (2,1)]
        corner = 2*UP + 2*LEFT
        marks = []
        for i in range(len(tictactoe_plays)):
            x, y = tictactoe_plays[i]
            p1 = Circle(color = BLUE).scale(0.5)
            if i % 2 == 1:
                p1 = Cross(p1, color = RED).scale(0.8)
            p1.move_to(corner + 2*x*RIGHT + 2*y*DOWN)
            self.play(ShowCreation(p1), run_time = 0.5)
            marks.append(p1)

        winning = Line(3*LEFT, 3*RIGHT, color = BLUE, stroke_width = 10)
        self.play(ShowCreation(winning))
        trophy = ImageMobject("Trophy").next_to(self.MC, UP).set_color(GOLD)
        self.play(FadeInFromLarge(trophy))
        self.wait(1)
        self.remove(winning, trophy)

        # clear the board and start discussion
        board = VGroup(*marks, *lines, title)
        new_board = board.copy().scale(0.5).next_to(self.MC, UP, buff = MED_LARGE_BUFF)
        self.play(FadeOutAndShiftDown(self.MC2))
        self.play(ReplacementTransform(board, new_board))
        
        self.wait(20-self.time)
        
        types = [
            "2-player game",
            "turn by turn",
            "square grid",
            "single action",
            "pattern matching",
            "single winner"
        ]

        type_text = VGroup(*[Text(t) for t in types]).arrange(DOWN, aligned_edge=LEFT)
        type_text.scale(1.5).to_corner(UL)
        for t in type_text:
            self.play(Write(t))
            self.wait(2)

        self.wait(35-self.time)
        text = Text("ถ้าเปลี่ยนบางส่วน\nแล้วจะเป็นอย่างไร?", font = "Anakotmai Light", line_spacing = 3)
        text.set_color(random_bright_color()).scale(1.5)
        
        self.play(Blink(self.MC))
        self.play(MeepleCreatureSays(
            self.MC, text,
            bubble_class = ThoughtBubble,
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking",
            is_looking_direction_purposeful = True,
        ))
        self.play(Blink(self.MC))
        self.wait(42-self.time)
        self.play(RemoveMeepleCreatureBubble(self.MC))

        # changing first part
        text = Text("3-player game?", fill_color = GREEN)
        text.next_to(type_text[0], RIGHT)
        cross = Line(type_text[0].get_left(), type_text[0].get_right(), color = RED, stroke_width = 10)
        self.play(Indicate(type_text[0]))
        self.wait(1)
        self.play(ShowCreation(cross))
        self.play(FadeInFrom(text, LEFT))
        self.wait(47-self.time)
        self.play(Indicate(type_text[4]))
        self.play(ApplyMethod(type_text[4].set_opacity, 0.3))
        self.wait(54-self.time)
        self.remove(cross, text)
        type_text[4].set_opacity(1)
        self.wait(1)

        # changing second part
        text = Text("real time?", fill_color = GREEN)
        text.next_to(type_text[1], RIGHT)
        cross = Line(type_text[1].get_left(), type_text[1].get_right(), color = RED, stroke_width = 10)
        self.wait(55-self.time)
        self.play(Indicate(type_text[1]))
        self.wait(1)
        self.play(ShowCreation(cross))
        self.play(FadeInFrom(text, LEFT))
        self.wait(62-self.time)
        self.play(Indicate(type_text[5]))
        self.play(ApplyMethod(type_text[5].set_opacity, 0.3))
        self.wait(69-self.time)
        self.remove(cross, text)
        type_text[5].set_opacity(1)

        text = Text("เปลี่ยนอย่างไร\nได้บ้าง?", font = "Anakotmai Light", line_spacing = 3)
        self.play(Blink(self.MC))
        self.play(MeepleCreatureThinks(
            self.MC, text,
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking",
            is_looking_direction_purposeful = True,
        ))
        self.play(Blink(self.MC))
        self.wait(85-self.time)
        self.play(RemoveMeepleCreatureBubble(self.MC))

        self.play(AnimationGroup(
            *[FadeOutAndShiftDown(t) for t in type_text],
            lag_ratio = 0.1
        ))
        
        # new types
        types = [
            "STR-01 Competitive Games",
            "TRN-01 Fixed-Turn Order",
            "ACT-01 Action Points",
            "VIC-01 Victory Points from Game State"
        ]

        type_text = VGroup(*[Text(t) for t in types]).arrange(DOWN, aligned_edge=LEFT, buff = 0.8)
        type_text.scale(1).to_corner(UL)
        self.play(AnimationGroup(
            *[FadeInFromDown(t) for t in type_text],
            lag_ratio = 0.1
        ))
        
        self.wait(88-self.time)
        self.play(AnimationGroup(
            *[Indicate(t[4:6]) for t in type_text],
            lag_ratio = 0.2
        ))

        self.wait(99-self.time)
        text = Text("Worker Placement?\nArea Control?", line_spacing = 3)
        text.set_color(random_bright_color()).scale(1.5)
        
        self.play(FadeInFromDown(self.MC2))
        self.MC.make_eye_contact(self.MC2)
        self.play(Blink(self.MC))
        self.play(MeepleCreatureSays(
            self.MC2, text, 
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking",
            is_looking_direction_purposeful = True,
        ))
        self.play(Blink(self.MC2))
        
        self.wait(108-self.time)
        self.play(RemoveMeepleCreatureBubble(self.MC2))
        text = Text("อ่านคำจำกัดความ\nในหนังสือดูสิ", line_spacing = 3)
        self.play(MeepleCreatureSays(
            self.MC, text, 
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking",
            is_looking_direction_purposeful = True,
        ))
        self.play(Blink(self.MC))

        book = ImageMobject("book_cover")
        book.scale(1.5).to_edge(DOWN)
        self.play(FadeInFromDown(book))
        self.MC.look_at(book)
        self.wait(114-self.time)
        #self.remove(book)
        #self.play(RemoveMeepleCreatureBubble(self.MC))
        #self.wait()

    def game_structure(self):
        subtypes = [
            "STR-01 Competitive Games",
            "STR-02 Cooperative Games",
            "STR-03 Team-Based Games",
            "STR-04 Solo Games",
            "STR-05 Semi-Cooperative Games",
            "STR-06 Single Loser Games",
            "STR-07 Traitor Games",
            "STR-08 Scenario/Mission/Campaign Games",
            "STR-09 Score-and-Reset Games",
            "STR-10 Legacy Games"
        ]

        creature = Meeple()
        bot = SVGMobject("Robot")
        creature.scale(0.7)
        bot.scale(1.2).set_color(WHITE)

        creatures = []
        creature_positions = []
        for i in range (0,4):
            newcreature = creature.copy()
            newcreature.set_color(random_bright_color())
            creatures.append(newcreature)
        
        
        # subtype 1
        title = Text(subtypes[0], font = "Prompt").set_color(random_bright_color()).to_edge(UP).scale(1.2)

        creature_positions = [UL*2, UR*2, DR*2, DL*2]
        for c,p in zip(creatures, creature_positions):
            c.move_to(p)
            c.look_at(ORIGIN)

        self.play(AnimationGroup(
            Write(title),
            *[FadeInFromDown(c) for c in creatures],
            lag_ratio = 0.2
        ))
        self.wait(0.5)
        self.remove(title)
        #'''
        # STR-02 Cooperative Games
        title = Text(subtypes[1], font = "Prompt").set_color(random_bright_color()).to_edge(UP).scale(1.2)
        self.wait(1)

        creature_positions = [UP + 4*LEFT, UP + 2*LEFT, DOWN + 2*LEFT, DOWN + 4*LEFT]
        bot.move_to(3*RIGHT)
        for c in creatures:
            c.look_at(bot)

        self.play(AnimationGroup(
            Write(title),
            FadeInFromDown(bot),
            *[MoveAlongPath(c, Line(c.get_center(), p), rate_func = smooth) for c,p in zip(creatures, creature_positions)],
            lag_ratio = 0
        ))
        self.wait(0.5)
        self.remove(title)

        # STR-03 Team-Based Games
        title = Text(subtypes[2], font = "Prompt").set_color(random_bright_color()).to_edge(UP).scale(1.2)
        self.wait(1)

        creature_positions = [UP + 3*LEFT, UP + 3*RIGHT, DOWN + 3*RIGHT, DOWN + 3*LEFT]
        creatures[0].look_at(creatures[1])
        creatures[1].look_at(creatures[0])
        creatures[2].look_at(creatures[3])
        creatures[3].look_at(creatures[2])
        self.play(AnimationGroup(
            Write(title),
            FadeOutAndShiftDown(bot),
            *[MoveAlongPath(c, Line(c.get_center(), p), rate_func = smooth) for c,p in zip(creatures, creature_positions)],
            lag_ratio = 0
        ))
        self.wait(0.5)
        self.remove(title)

        # STR-04 Solo Games
        title = Text(subtypes[3], font = "Prompt").set_color(random_bright_color()).to_edge(UP).scale(1.2)
        self.wait(1)
        creatures[0].look_at(bot)
        
        self.play(AnimationGroup(
            Write(title),
            FadeOut(creatures[1]),
            FadeOut(creatures[2]),
            FadeOut(creatures[3]),
            FadeInFromDown(bot),
            MoveAlongPath(creatures[0], Line(creatures[0].get_center(), 3*LEFT), rate_func = smooth),
            lag_ratio = 0
        ))
        self.wait(0.5)
        self.remove(title)

        # subtype 5
        title = Text(subtypes[4], font = "Prompt").set_color(random_bright_color()).to_edge(UP).scale(1.2)
        self.wait(1)

        creature_positions = [2*UP + 5*LEFT, 2*UP + LEFT, 2*DOWN + LEFT, 2*DOWN + 5*LEFT]
        bot.move_to(3*RIGHT)
        for c in creatures:
            self.add(c)
            c.move_to(creatures[0].get_center())
            c.look_at(bot)

        self.play(AnimationGroup(
            Write(title),
            FadeInFromDown(bot),
            *[MoveAlongPath(c, Line(c.get_center(), p), rate_func = smooth) for c,p in zip(creatures, creature_positions)],
            lag_ratio = 0
        ))

        self.wait(0.5)
        self.remove(title)

        # STR-06 Single Loser Games
        title = Text(subtypes[5], font = "Prompt").set_color(random_bright_color()).to_edge(UP).scale(1.2)
        self.wait(1)

        creature_positions = [UL*2, UR*2, DR*2, DL*2]
        for c in creatures:
            c.look_at(ORIGIN)

        self.play(AnimationGroup(
            Write(title),
            FadeOutAndShiftDown(bot),
            *[MoveAlongPath(c, Line(c.get_center(), p), rate_func = smooth) for c,p in zip(creatures, creature_positions)],
            lag_ratio = 0
        ))
        
        for c in creatures:
            c.look_at(creatures[1])
        cross = Cross(creatures[1])
        self.play(ShowCreation(cross))
        #self.play(ApplyMethod(creatures[1].set_fill, creatures[1].get_color(), 0.2))
        self.remove(title, cross)
        #'''

        # "STR-07 Traitor Games"
        title = Text(subtypes[6], font = "Prompt").set_color(random_bright_color()).to_edge(UP).scale(1.2)
        role_unknown = [Text("?", color = WHITE).next_to(c, DOWN) for c in creatures]
        roles = ["Good", "Good", "Traitor", "Good"] # to be replaced by image ?
        role_text = [Text(r, color = GREEN).next_to(c, DOWN) for r,c in zip(roles, creatures)]
        role_text[2].set_color(RED)

        for c in creatures:
            c.look_at(ORIGIN)

        self.play(AnimationGroup(
            Write(title),
            *[FadeInFromDown(unknown) for unknown in role_unknown]
        ))
        self.wait(0.5)
        self.play(AnimationGroup(
            *[ReplacementTransform(unknown, rt) for unknown, rt in zip(role_unknown, role_text)]
        ))

        self.wait(0.5)
        self.remove(title, *[rt for rt in role_text])
        
        # STR-08 Scenario/Mission/Campaign Games
        # ????

        # STR-09 Score-and-Reset Games
        title = Text(subtypes[8], font = "Prompt").set_color(random_bright_color()).to_edge(UP).scale(1.2)
        self.wait(1)

        creature_positions = [2*UP + 4.5*LEFT, 2*UP + 1.5*LEFT, 2*UP + 1.5*RIGHT, 2*UP + 4.5*RIGHT]
        self.play(AnimationGroup(
            Write(title),
            *[MoveAlongPath(c, Line(c.get_center(), p), rate_func = smooth) for c,p in zip(creatures, creature_positions)],
            lag_ratio = 0
        ))
        for c in creatures:
            c.look_at(ORIGIN)

        scores = [[3,4,2,5], [2,3,4,1], [3,4,5,6], [8, 11, 11, 12]]
        score_text = []
        for i in range(0, 4):
            st = [Text(str(s)).move_to(p + (i+2)*DOWN) for s,p in zip(scores[i], creature_positions)]
            if i == 3:
                [s.set_color(BLUE) for s in st]
            score_text.append(st)

        for st in score_text:
            self.play(AnimationGroup(
                *[FadeIn(s) for s in st]
            ))
        self.wait(0.5)
        self.remove(title)

        # STR-10 Legacy Games

    def turn_order(self):
        subtypes = [
            "TRN-01 Fixed Turn Order",
            "TRN-02 Stat Turn Order",
            "TRN-03 Bid Turn Order",
            "TRN-04 Progressive Turn Order",
            "TRN-05 Claim Turn Order",
            "TRN-06 Pass Order",
            "TRN-07 Real-Time",
            "TRN-08 Punctuated Real-Time",
            "TRN-09 Simultaneous Action Selection",
            "TRN-10 Role Order",
            "TRN-11 Random Turn Order",
            "TRN-12 Action Timer",
            "TRN-13 Time Track",
            "TRN-14 Passed Action Token",
            "TRN-15 Interleaved vs. Sequential Phases",
            "TRN-16 Lose a Turn",
            "TRN-17 Interrupts"
        ]

        creature = Meeple()
        creature.scale(1.2)

        creatures = []
        creature_positions = []
        for i in range (0,NUM_PLAYERS):
            newcreature = creature.copy()
            newcreature.set_color(random_bright_color())
            creatures.append(newcreature)
        
        # TRN-01 Fixed Turn Order
        title = Text(subtypes[0], font = "Prompt").set_color(random_bright_color()).to_edge(UP).scale(1.2)

        creature_positions = [4.5*LEFT, 1.5*LEFT, 1.5*RIGHT, 4.5*RIGHT]
        for c,p in zip(creatures, creature_positions):
            c.move_to(p)

        self.play(AnimationGroup(
            Write(title),
            *[FadeInFromDown(c) for c in creatures],
            lag_ratio = 0.2
        ))
        self.wait(0.5)
        #self.add_sound("Ding")
        border = SurroundingRectangle(creatures[0], buff = MED_SMALL_BUFF)
        self.play(FadeIn(border))
        

        for i in range(0,NUM_PLAYERS*2):
            self.play(
                MoveAlongPath(border,
                    Line(
                        creatures[i%NUM_PLAYERS].get_center(), 
                        creatures[(i+1)%NUM_PLAYERS].get_center()
                    ),
                    rate_func = smooth
                )
            )
            #self.add_sound("Ding")
        self.remove(title)
