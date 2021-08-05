#!/usr/bin/env python
from manim import *

class TwoD(GraphScene):
    CONFIG = {
            "x_min": -2,
            "x_max": 2,
            "y_min": -2,
            "y_max": 2,
            "graph_origin": ORIGIN,
            "function_color": WHITE,
            "axes_color": BLUE
        }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph,self.function_color)
        graph_lab = self.get_graph_label(func_graph, label = "x^{2} + y^{2} = 1")

        vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x,y, color=YELLOW)

        point = Dot(self.coords_to_point(1,self.func_to_graph(1)))

        self.area = self.get_area(func_graph, 0, 2)
        #Display graph
        self.play(Create(func_graph), Write(graph_lab))
        self.wait(1)
        self.play(Create(vert_line))
        self.play(Create(horz_line))
        self.add(point)
        self.play(Create(self.area))
        self.wait(2)

    def func_to_graph(self, x):
        return (x**2)

class para(GraphScene):
    CONFIG = {
            "x_min": -2,
            "x_max": 2,
            "y_min": -1.5,
            "y_max": 1.5,
            "y_bottom_tick": -1,
            "x_axis_width": 8,
            "y_axis_height": 6,
            "graph_origin": ORIGIN,
            "function_color": WHITE,
            "axes_color": BLUE
        }
    def construct(self):
        def create_angle(a):
            return Sector(
                start_angle=0, 
                angle = a, 
                outer_radius = 0.5, 
                color = GREEN,
                fill_opacity = 0.8
                )
        self.setup_axes(animate=True)
        f = ParametricFunction(self.func, t_min = 0, t_max = TAU)
        theta = ValueTracker(0)
        x = DecimalNumber(
            np.cos(theta.get_value()),
            num_decimal_places=3,
            )
        y = DecimalNumber(
            np.sin(theta.get_value()),
            num_decimal_places=3,
            )
        p = Dot(f.get_point_from_function(theta.get_value()))
        p.set_color(GREEN)
        ar = Arrow(ORIGIN, p.get_center(), buff = 0)
        ar.set_color(ORANGE)
        s = create_angle(theta.get_value())

        x.add_updater(lambda v: v.set_value(np.cos(theta.get_value())))
        y.add_updater(lambda v: v.set_value(np.sin(theta.get_value())))
        p.add_updater(lambda v: v.move_to(f.get_point_from_function(theta.get_value())))
        ar.add_updater(lambda v: v.put_start_and_end_on(ORIGIN, p.get_center()))
        s.add_updater(lambda v: v.become(create_angle(theta.get_value())))

        # add value update
        tx = MathTex("x = ")
        ty = MathTex("y = ")
        group = VGroup(tx, ty).arrange(DOWN)
        #group = VGroup(tx, x, ty, y).arrange_in_grid(2,2) #<- doesn't work? idk
        group.to_corner(UL)
        x.next_to(tx, RIGHT)
        y.next_to(ty, RIGHT)

        self.play(Create(f))
        self.play(Write(group), Write(x), Write(y), Write(p))
        self.play(GrowArrow(ar), Write(s))
        self.play(
            theta.set_value,TAU,
            rate_func=there_and_back,
            run_time=5
            )
        self.wait()
        
    def func(self, t):
        return [2*np.cos(t), 2*np.sin(t), 0]

    
# See old_projects folder for many, many more
