#!/usr/bin/env python

from manimlib.imports import *
from myconstructs.randomizer import *
from datetime import datetime
import functools

class DiceScene(Scene):
    CONFIG = {
        "num_dice": 3,
        "show_total": True
    }
    def construct(self):
        random.seed(datetime.now())

        pip_color = [GREEN, BLUE, ORANGE]
        dice = []
        for i in range(self.num_dice):
            dice.append(D6(pip_color = pip_color[i]))

        total = Integer(
            reduce(lambda a,b: a+b, [d.get_value() for d in dice]) 
        )
        total.scale(5)
        g = VGroup()
        for d in dice:
            g.add(d)
        g.add(TexMobject("="), total)
        g.arrange(RIGHT)

        # start animation
        self.play(ShowCreation(g), run_time = 3)
        self.wait()
        text1 = TextMobject("Roll each dice").to_edge(DOWN)
        self.play(DrawBorderThenFill(text1))
        for i in range(3):
            for d in dice:
                self.play(*d.Roll())
                total.set_value(
                    reduce(lambda a,b: a+b, [d.get_value() for d in dice]) 
                )
        
        text2 = TextMobject("Roll all dice").to_edge(DOWN)
        self.play(Transform(text1, text2))
        for i in range(3):
            seq = []
            for d in dice:
                seq = seq + d.Roll()
            self.play(*seq)
            total.set_value(
                reduce(lambda a,b: a+b, [d.get_value() for d in dice]) 
            )
        self.wait()
        

class CardScene(Scene):
    def construct(self):
        random.seed(datetime.now())
        v1 = random.randint(1,13)
        v2 = random.randint(1,13)
        c1 = PlayingCard(v1, "club", face_up= True)
        c2 = PlayingCard(v2, "diamond", face_up = False)
        g = VGroup(c1, c2).arrange(RIGHT)

        self.play(FadeInFrom(g, DOWN))
        self.wait(1)
        self.play(c1.Flip())
        self.wait(0.5)
        self.play(c1.Flip())
        self.wait(0.5)
        self.play(c2.Flip())
        self.wait(0.5)
        self.play(c2.Flip())
        self.wait(1)