#!/usr/bin/env python

from manimlib.imports import *

class main(GraphScene):
    CONFIG = {
            "x_min": -1,
            "x_max": 1,
            "y_min": 0,
            "y_max": 1,
            "y_bottom_tick": -0,
            "x_axis_width": 4,
            "y_axis_height": 2,
            "graph_origin": ORIGIN,
            "function_color": WHITE,
            "axes_color": BLUE,
            "x_axis_label": None,
            "y_axis_label": None,
            "radius": 2
        }
    def construct(self):
        def create_sector(a):
            return Sector(
                start_angle=0, 
                angle = a, 
                outer_radius = self.radius, 
                color = GREEN,
                fill_opacity = 0.8
                )
        self.setup_axes(animate=True)
        f = ParametricFunction(self.func, t_min = 0, t_max = TAU/2)
        theta = ValueTracker(PI/6)
        # create points
        point_sin_top = Dot(f.get_point_from_function(theta.get_value()), radius = 0)
        # point_sin_bottom = Dot(self.coords_to_point(math.cos(theta.get_value()),0), radius = 0)
        point_tan_top = Dot(self.coords_to_point(1, math.tan(theta.get_value())), radius = 0)
        point_tan_bottom = Dot(self.coords_to_point(1,0), radius = 0)
        self.add(point_sin_top, point_tan_top, point_sin_bottom)

        # create shapes
        sect = create_sector(theta.get_value())
        tri_sin = Polygon(ORIGIN)
        tri_tan = Polygon(ORIGIN)
        line_to_circle = Line(ORIGIN, point_sin_top)

        # create text
        mid = 2*DOWN
        pos = [mid - 2*RIGHT, mid-RIGHT, mid, mid+RIGHT, mid+2*RIGHT]
        # first set
        text_sin = TexMobject("{\\sin x", "\\over 2}").set_color(PINK).move_to(pos[0])
        text_leq1 = TexMobject("\\leq").move_to(pos[1])
        text_sector = TexMobject("{x", "\\over 2}").set_color(GREEN).move_to(pos[2])
        text_leq2 = TexMobject("\\leq").move_to(pos[3])
        text_tan = TexMobject("{\\tan x","\\over 2}").set_color(ORANGE).move_to(pos[4])
        group1 = VGroup(text_sin, text_leq1, text_sector, text_leq2, text_tan)

        # second set
        text_sin2 = TexMobject("\\sin x","").move_to(pos[0])
        text_sector2 = TexMobject("x","").move_to(pos[2])
        text_tan2 = TexMobject("\\tan x","").move_to(pos[4])
        group2 = VGroup(text_sin2, text_leq1, text_sector2, text_leq2, text_tan2)

        # third set
        text_sin3 = TexMobject("{\\sin x ","\\over \\sin x}").move_to(pos[0])
        text_sector3 = TexMobject("{x","\\over \\sin x}").move_to(pos[2])
        text_tan3 = TexMobject("{ \\tan x","\\over \\sin x").move_to(pos[4])
        group3 = VGroup(text_sin3, text_leq1, text_sector3, text_leq2, text_tan3)
        text_sin35 = TexMobject("1").move_to(pos[0])
        text_tan35 = TexMobject("{1 \\over \\cos x").move_to(pos[4])

        # fourth set
        text_sin4 = TexMobject("","1").move_to(pos[0])
        text_sector4 = TexMobject("", "{\\sin x \\over x}").move_to(pos[2])
        text_tan4 = TexMobject("","\\cos x").move_to(pos[4])
        text_geq1 = TexMobject("\\geq").move_to(pos[1])
        text_geq2 = TexMobject("\\geq").move_to(pos[3])
        group4 = VGroup(text_sin4, text_geq1, text_sector4, text_geq2, text_tan4)

        # fifth
        text_limit1 = TexMobject("\\lim_{x \\rightarrow 0} 1",
            "\\geq",
            "\\lim_{x \\rightarrow 0} {\\sin x \\over x}",
            "\\geq",
            "\\lim_{x \\rightarrow 0} \\cos x"
        ).move_to(pos[2])

        text_limit2 = TexMobject("1",
            "\\geq",
            "\\lim_{x \\rightarrow 0} {\\sin x \\over x}",
            "\\geq",
            "1"
        ).move_to(pos[2])

        text_final = TexMobject("\\lim_{x \\rightarrow 0} {\\sin x \\over x} = 1").move_to(pos[2])
        text_final.scale(2)

        # add updaters on points
        point_sin_top.add_updater(lambda v: v.move_to(
            f.get_point_from_function(theta.get_value())
        ))
        #point_sin_bottom.add_updater(lambda v: v.move_to(
        #    self.coords_to_point(math.cos(theta.get_value()),0)
        #))
        point_tan_top.add_updater(lambda v: v.move_to(
            self.coords_to_point(1, math.tan(theta.get_value()))
        ))

        # add updaters on shapes
        sect.add_updater(lambda v: v.become(create_sector(theta.get_value())))
        tri_sin.add_updater(lambda v: v.become(
            Polygon(ORIGIN, point_sin_top.get_center(), point_tan_bottom.get_center())
                .set_fill(PINK, opacity=0.8)
        ))
        tri_tan.add_updater(lambda v: v.become(
            Polygon(ORIGIN, point_tan_top.get_center(), point_tan_bottom.get_center())
                .set_fill(ORANGE, opacity=0.8)
        ))

        # start animation
        self.play(ShowCreation(f))
        self.play(ShowCreation(line_to_circle), ShowCreation(tri_sin))
        self.play(ReplacementTransform(tri_sin, text_sin))
        self.play(ShowCreation(sect))
        self.play(ReplacementTransform(sect, text_sector))
        self.play(ShowCreation(tri_tan))
        self.play(ReplacementTransform(tri_tan,text_tan))
        self.play(ShowCreation(tri_tan))
        self.play(ShowCreation(sect))
        self.play(Write(text_leq2))
        self.play(ShowCreation(tri_sin))
        self.play(Write(text_leq1))
        self.remove(line_to_circle)
        fr1 = SurroundingRectangle(text_leq1, buff = .1)
        fr2 = SurroundingRectangle(text_leq2, buff = .1)

        self.play(ShowCreation(fr1), ShowCreation(fr2))
        self.play(
            theta.set_value,0,
            rate_func=there_and_back,
            run_time=3
            )
        self.play(FadeOut(fr1), FadeOut(fr2))
        
        self.play(ReplacementTransform(group1, group2))
        self.wait(1)
        self.play(ReplacementTransform(group2, group3))
        self.wait(1)
        self.play(ReplacementTransform(text_tan3, text_tan35), ReplacementTransform(text_sin3, text_sin35))
        self.wait(1)
        group3.add(text_tan35, text_sin35)
        self.play(ReplacementTransform(group3, group4))
        self.wait(1)
        self.play(ReplacementTransform(group4, text_limit1))
        self.wait(1)
        self.play(ReplacementTransform(text_limit1, text_limit2))
        self.wait(1)
        self.play(ReplacementTransform(text_limit2, text_final))
        fr3 = SurroundingRectangle(text_final, buff = .3)
        self.play(ShowCreation(fr3))
        self.wait(2)
        
    def func(self, t):
        return [self.radius*math.cos(t), self.radius*math.sin(t), 0]
