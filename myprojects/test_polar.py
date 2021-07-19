#!/usr/bin/env python

from manimlib.imports import *

class TestPolar(Scene):
    def construct(self):
        text = TextMobject("Petal plot")
        p = PolarCurve(lambda theta: 1 - np.cos(theta)) #custom class, extending ParametricFunction

        theta = ValueTracker(0)
        t = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        
        t.add_updater(lambda x: x.set_value(theta.get_value()))

        d = Dot(p.get_point_from_function(0), radius = 0.1, color = RED)
        l = Line(ORIGIN, d.get_center())
        self.add(d, l)
        d.add_updater(lambda x: x.move_to(p.get_point_from_function(theta.get_value())))
        l.add_updater(lambda x: x.become(Line(ORIGIN, d.get_center())))

        text.to_edge(UP)
        theta_tex = VGroup(TexMobject(r'\theta = '), t).arrange(RIGHT, aligned_edge = DOWN)
        theta_tex.to_edge(DOWN)
        self.play(Write(text))
        self.play(Write(theta_tex))
        self.play(ShowCreation(p))
        self.play(ApplyMethod(theta.set_value, TAU), run_time = 3)
        self.wait()