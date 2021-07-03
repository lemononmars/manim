from manimlib.imports import *
import numpy as np

class Box(Scene):

    def construct(self):
        # create a nice box
        box_front = Polygon([0,0,0],[2,0,0],[2,2,0],[0,2,0], stroke_width = 3, stroke_color = WHITE).set_opacity(1)
        box_top = Polygon([0,0,0],[2,0,0],[3,1,0],[1,1,0], stroke_width = 3, stroke_color = WHITE).set_opacity(0.4).shift(UP*2)
        box_right = Polygon([0,0,0],[1,1,0],[1,3,0],[0,2,0], stroke_width = 3, stroke_color = WHITE).set_opacity(1).shift(RIGHT*2)
        box = VGroup(box_front, box_top, box_right)
        box.shift(DOWN*3)

        new_box1 = box.copy().scale(0.5)

        num1 = TexMobject("1", color = GREEN).scale(3)
        num2 = TexMobject("2", color = RED).scale(3)

        startp = np.array([1,-2,0])
        path1 = ArcBetweenPoints(startp, np.array([-5,3,0]))
        path2 = ArcBetweenPoints(startp, np.array([-5,1,0]))
        path3 = ArcBetweenPoints(startp, np.array([-3,3,0]))

        num1.align_to(box)
        num2.align_to(box)

        self.add_foreground_mobjects(box)
        self.wait(6)
        self.play(MoveAlongPath(num1, path1), run_time = 2)
        self.wait(2)
        self.play(MoveAlongPath(num2, path2), run_time = 2)
        self.wait(4)
        self.play(MoveAlongPath(new_box1, path3), run_time = 2)
        self.wait(0.5)
        self.play(AnimationGroup(
            FadeOut(num1),
            FadeOut(num2),
            FadeOut(box),
            ReplacementTransform(new_box1, box)
        ))
        self.wait(0.5)