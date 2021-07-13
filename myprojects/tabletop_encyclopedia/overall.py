from manimlib.imports import *

class Movie(Scene):
    def construct(self):
        #self.intro()
        self.game_structure()
    
    def intro(self):
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
        creature = SVGMobject(f'.\media\designs\svg_images\MeepleCreature_plain.svg')
        creature[4].set_color(BLUE_C)
        self.play(Write(creature))
        self.wait(1)
        pos = UP + 3*LEFT

        text = []
        for i in range(0,len(topics)):
            newtitle = Text(str(i+1) + ") " + topics[i], font = "Prompt").set_color(random_bright_color())
            text.append(newtitle)
        
        t = VGroup(*text).arrange(DOWN, center = False, aligned_edge = LEFT, buff = 0.1)
        t.to_corner(LEFT + UP)

        for i in t:
            self.play(Write(i))

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

        creature = SVGMobject(f'.\media\designs\svg_images\MeepleCreature_plain.svg')
        bot = SVGMobject(f'.\media\designs\svg_images\Robot.svg')
        creature.scale(1.2)
        bot.scale(1.2).set_color(WHITE)

        creatures = []
        creature_positions = []
        for i in range (0,4):
            newcreature = creature.copy()
            newcreature[4].set_color(random_bright_color())
            creatures.append(newcreature)
        
        # subtype 1
        title = Text(subtypes[0], font = "Prompt").set_color(random_bright_color()).move_to(TOP, aligned_edge = UP)

        creature_positions = [UL*2, UR*2, DR*2, DL*2]
        for c,p in zip(creatures, creature_positions):
            c.move_to(p)

        self.play(AnimationGroup(
            Write(title),
            *[FadeInFromDown(c) for c in creatures],
            lag_ratio = 0.2
        ))
        self.wait(0.5)
        self.remove(title)

        # subtype 2
        title = Text(subtypes[1], font = "Prompt").set_color(random_bright_color()).move_to(TOP, aligned_edge = UP)
        self.wait(1)

        creature_positions = [UP + 4*LEFT, UP + 2*LEFT, DOWN + 2*LEFT, DOWN + 4*LEFT]
        bot.move_to(RIGHT*2)

        self.play(AnimationGroup(
            Write(title),
            FadeInFromDown(bot),
            *[MoveAlongPath(c, Line(c.get_center(), p), rate_func = smooth) for c,p in zip(creatures, creature_positions)],
            lag_ratio = 0
        ))
        self.wait(0.5)
        self.remove(title)

        # subtype 3
        title = Text(subtypes[2], font = "Prompt").set_color(random_bright_color()).move_to(TOP, aligned_edge = UP)
        self.wait(1)

        creature_positions = [UP + 4*LEFT, UP + 4*RIGHT, DOWN + 4*RIGHT, DOWN + 4*LEFT]

        self.play(AnimationGroup(
            Write(title),
            FadeOutAndShiftDown(bot),
            *[MoveAlongPath(c, Line(c.get_center(), p), rate_func = smooth) for c,p in zip(creatures, creature_positions)],
            lag_ratio = 0
        ))
        self.wait(0.5)
