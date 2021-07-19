#!/usr/bin/env python

from manimlib.imports import *

class main(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 1,
        "y_min": 0,
        "y_max": 1,
        "y_bottom_tick": 0,
        "x_axis_width": 8,
        "y_axis_height": 4,
        "graph_origin": ORIGIN + 2*DOWN,
        "function_color": WHITE,
        "axes_color": BLUE,
    }

    def construct(self):
        self.sin_sum()
        self.wait()
        #self.cos_sum()
        self.wait()

    def sin_sum(self):
        self.setup_axes()
        # set up triangles
        a1 = PI/6
        a2 = PI/4
        pc1 = Dot(self.coords_to_point(math.cos(a1), math.sin(a1)))
        pb1 = Dot(self.coords_to_point(math.cos(a1), 0))
        pc2 = Dot(self.coords_to_point(math.cos(a1+a2), math.sin(a1+a2)))
        pb2 = Dot(self.coords_to_point(math.cos(a1+a2), 0))
        p_special = Dot(self.coords_to_point(math.cos(a1)*math.cos(a2), math.sin(a1)*math.cos(a2)))

        arc1 = Arc(0, a1, radius = 1).set_color(GREEN).set_fill(GREEN).move_arc_center_to(self.graph_origin)
        arc2 = Arc(a1, a2, radius = 1).set_color(PINK).set_fill(PINK).move_arc_center_to(self.graph_origin)

        text_angle1 = TexMobject("\\alpha")
        text_angle1.next_to(arc1, RIGHT)
        text_angle2 = TexMobject("\\beta")
        text_angle2.next_to(arc2, UR)

        # b = base
        # c = rotated line
        # v = vertical line
        line_b1 = Line(self.graph_origin, pb1.get_center()).set_color(GREEN)
        line_c1 = Line(self.graph_origin, pc1.get_center()).set_color(GREEN)
        line_v1 = Line(pb1.get_center(), pc1.get_center()).set_color(GREEN)
        
        line_b2 = Line(self.graph_origin, pb2.get_center()).set_color(PINK)
        line_c2 = Line(self.graph_origin, pc2.get_center()).set_color(PINK)
        line_v2 = Line(pb2.get_center(), pc2.get_center()).set_color(PINK)
        line_special = Line(pc2.get_center(), p_special.get_center())
        
        # animate triangles
        self.play(FadeIn(pb1), FadeIn(pc1)) # for debugging
        self.play(ShowCreation(line_b1))
        self.play(ShowCreation(line_v1))
        self.play(ShowCreation(line_c1))
        self.play(ShowCreation(arc1))
        self.play(Write(text_angle1))

        self.play(ShowCreation(line_b2))
        self.play(ShowCreation(line_v2))
        self.play(ShowCreation(line_c2))
        self.play(ShowCreation(arc2))
        self.play(Write(text_angle2))

        self.play(ShowCreation(line_special))

        # bisect the line

        # formulas