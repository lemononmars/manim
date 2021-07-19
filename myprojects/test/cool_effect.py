#!/usr/bin/env python

from manimlib.imports import *
text = Text("Cool Effect").scale(3)

class EffectExamples(Scene):
    def construct(self):
        self.ellipse()
        self.bounce()
        self.stack()
        self.disperse()

    def ellipse(self):
        title = Text(r'self.ellipse()', font = "Consolas", color = YELLOW, t2c = {'self':BLUE, '()':WHITE})
        title.to_edge(DOWN)
        self.add(title)

        text_start = text.copy()
        self.add(text_start)

        # start from an ellipse that is off screen
        ellipse = Ellipse(width = 20, height = 12)
        for i in range(len(text)):
            # use a built-in function to get points that are equally spaced angle-wise
            # +4 is just an offset. play around with the offset to get different effects.
            new_pos = ellipse.point_at_angle(TAU*((i+4)%len(text))/len(text)) 
            text_start[i].move_to(new_pos)

        # animate each letter to the appropriate position
        self.play(AnimationGroup(
            *[ApplyMethod(text_start[i].move_to, text[i].get_center()) for i in range(len(text))]
        ))
        self.remove(title)
        self.play(FadeOut(text_start))

    def bounce(self):
        title = Text(r'self.bounce()', font = "Consolas", color = YELLOW, t2c = {'self':BLUE, '()':WHITE})
        title.to_edge(DOWN)
        self.add(title)
        # start from top, off screen
        text_start = text.copy().shift(6*UP)

        # set smooth paths for each letter
        points = [6*UP, ORIGIN, 0.5*UP, ORIGIN, 0.1*UP, ORIGIN]
        path = VMobject().set_points_smoothly(points)
        paths = [path.copy().next_to(t.get_center(), DOWN, buff = 0) for t in text_start]
        
        # animate each letter on their own path to the appropriate position
        self.play(AnimationGroup(
            *[MoveAlongPath(t, p, rate_func = linear) for t,p in zip(text_start, paths) ],
            lag_ratio = 0.2
        ))
        self.remove(title)
        self.play(FadeOut(text_start))

    def stack(self):
        title = Text(r'self.stack()', font = "Consolas", color = YELLOW, t2c = {'self':BLUE, '()':WHITE})
        title.to_edge(DOWN)
        self.add(title)

        # start from the right, off screen
        text_start = text.copy().move_to(RIGHT*10)
        self.add(text_start)

        # animate each letter to the appropriate position
        self.play(AnimationGroup(
            *[ApplyMethod(text_start[i].move_to, text[i].get_center()) for i in range(len(text))],
            lag_ratio = 0.2
        ))
        self.remove(title)
        self.remove(*text_start) #since text_start had been animated individually, we need to remove it the same way

    def disperse(self):
        title = Text(r'self.disperse()', font = "Consolas", color = YELLOW, t2c = {'self':BLUE, '()':WHITE})
        title.to_edge(DOWN)
        self.add(title)
        
        text_end = text.copy()
        # set endpoints on an ellipse that is off screen 
        ellipse = Ellipse(width = 20, height = 12)
        for i in range(len(text)):
            new_pos = ellipse.point_at_angle(TAU*((i+8)%len(text))/len(text))
            text_end[i].move_to(new_pos)

        # animate each letter from the center to the ellipse
        self.play(AnimationGroup(
            *[ApplyMethod(text[i].move_to, text_end[i].get_center()) for i in range(len(text))]
        ))
        self.wait(1)
        self.remove(title)
