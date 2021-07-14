from manimlib.imports import *
from MeepleCreature.MeepleCreature import *

NUM_PLAYERS = 4
MC = Meeple()

class Movie(Scene):
    def construct(self):
        self.intro()
        self.toc()
        #self.game_structure()
        #self.turn_order()

    def intro(self):
        MC.to_edge(DOWN)
        text1 = Text("สวัสดีครับ\nผมชื่อกลครับ", font = "Anakotmai Light", line_spacing= 4)
        text1.set_color(random_bright_color()).scale(1.5)
        text2 = Text("วันนี้เรามาศึกษา\nกลไกในบอร์ดเกมกัน", font = "Anakotmai Light", line_spacing = 3)
        text2.set_color(random_bright_color()).scale(1.5)
        self.play(DrawBorderThenFill(MC))
        self.play(Blink(MC))
        
        self.play(MeepleCreatureSays(
            MC, text1, 
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking",
            is_looking_direction_purposeful = False,
        ))

        self.wait()
        self.play(Blink(MC))
        self.play(RemoveMeepleCreatureBubble(MC))
        self.play(MeepleCreatureSays(
            MC, text2, 
            bubble_kwargs = {"height" : 4, "width" : 6},
            target_mode="speaking",
            is_looking_direction_purposeful = False,
        ))
        self.play(Blink(MC))

        book = ImageMobject("book_cover")
        book.shift(UP + 4*RIGHT).scale(2.5)
        self.play(FadeInFromDown(book))
        MC.look_at(book)
        self.wait(1)

        self.play(RemoveMeepleCreatureBubble(MC))
        self.play(FadeOutAndShiftDown(MC))

        author_image = ImageMobject("geoff").scale(2)
        author_title = Text(f'Geoffrey Engelstein', font = "Prompt")
        author = Group(author_image, author_title).arrange(DOWN)

        author.shift(UP + 3*LEFT)
        self.play(FadeInFromDown(author_image))
        self.play(Write(author_title))

        quote = Text(f'Building Blocks of Tabletop Game Design: An Encyclopedia of Mechanisms\ncompiles hundreds of different mechanisms, organized by category.\nEach has a description of how it works, discussion of its pros and cons,\nhow it can be implemented, and examples of specific games that use it.', font = "Prompt").scale(0.6).set_color(GOLD_A)
        quote.to_edge(LEFT, buff = 1).shift(2.5*DOWN)
        self.play(Write(quote), run_time = 15) #13 seconds to read

        self.play(AnimationGroup(
            FadeOutAndShiftDown(quote),
            FadeOutAndShiftDown(author),
            FadeOutAndShiftDown(book)
        ))
        self.play(FadeInFromDown(MC))

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
        
        #topics = ["Game Structure"] # overwrite for shorter animation 

        self.play(
            MoveAlongPath(MC, Line(MC.get_center(), 5*RIGHT + 2*DOWN), rate_func = smooth)
        )

        text = []
        for i in range(0,len(topics)):
            newtitle = Text(str(i+1) + ") " + topics[i], font = "Prompt").set_color(random_bright_color())
            text.append(newtitle)
        
        t = VGroup(*text).arrange(DOWN, center = False, aligned_edge = LEFT, buff = 0.1)
        t.to_corner(UL)

        for i in t:
            MC.look_at(i)
            self.play(Write(i))
            self.play(Blink(MC))

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
