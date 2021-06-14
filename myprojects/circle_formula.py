#!/usr/bin/env python

from manimlib.imports import *

class main(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 1,
        "y_min": 0,
        "y_max": 1,
        "y_bottom_tick": -0,
        "x_axis_width": 8,
        "y_axis_height": 4,
        "graph_origin": ORIGIN + DOWN,
        "function_color": WHITE,
        "axes_color": BLUE,
        "radius": 2
    }

    def construct(self):
        self.integral_normal()
        self.wait()
        # clear scene?
        self.integral_polar()
        self.wait()

    def integral_normal(self):
        self.setup_axes(animate = True)

        eq_original = TexMobject("y = \\sqrt{1-x^2}")
        eq_original.to_edge(UL)
        self.play(Write(eq_original))

        graph = self.get_graph(self.func, color = None, x_min = -1, x_max = 1)
        self.play(ShowCreation(graph))

        # demo with points
        for i in range(1,3):
            dots_axis = VGroup()
            dots_curve = VGroup()
            lines = VGroup()
            prev_dot = Dot(self.coords_to_point(-1, 0))
            # create points on x-axis
            for k in range(2**(i+1)+1):
                x = -1 + (k/2**i)
                da = Dot(self.coords_to_point(x, 0), radius = 0.1).set_color(PINK)
                dots_axis.add(da)
                self.play(FadeIn(da), run_time = 0.1)
            # create points on the curve
            for k in range(2**(i+1)+1):
                x = -1 + (k/2**i)
                dc = Dot(self.coords_to_point(x, self.func(x)), radius = 0.1).set_color(GREEN)
                dots_curve.add(dc)
                self.play(FadeIn(dc), run_time = 0.1)
                if k > 0:
                    new_line = Line(prev_dot, dc)
                    self.play(FadeIn(new_line), run_time = 0.1)
                    lines.add(new_line)
                    prev_dot = dc
            self.play(FadeOut(dots_axis), FadeOut(dots_curve), FadeOut(lines))

            for i in range(3,6):
                k=1

        # animation showing arc length formula
        x0 = -1 + (1/2**2)
        p1 = Dot(self.coords_to_point(-1, 0))
        p2 = Dot(self.coords_to_point(x0, 0))
        p3 = Dot(self.coords_to_point(x0, self.func(x0)))
        l1 = Line(p1.get_center(), p2.get_center()).set_color(PINK)
        l2 = Line(p2, p3).set_color(GREEN)
        l3 = Line(p3, p1).set_color(BLUE)
        x_brace = DoubleArrow(p1, p2, buff = 0).shift(DOWN*0.2)
        x_text = TexMobject("dx").next_to(x_brace, DOWN)
        y_brace = DoubleArrow(p2, p3, buff = 0).shift(RIGHT*0.2)
        y_text = TexMobject("dy").next_to(y_brace, RIGHT)
        z_brace = DoubleArrow(p3, p1, buff = 0).shift(UP*0.2 + LEFT*0.2)
        z_text = TexMobject("\\sqrt{(dx)^2 + (dy)^2}")
        z_text.next_to(z_brace.get_center(), UL).scale(0.8)
        all_texts = VGroup(x_brace, x_text, y_brace, y_text, z_brace, z_text)
        self.play(ShowCreation(l1))
        self.play(FadeIn(x_brace), FadeIn(x_text))
        self.play(ShowCreation(l2))
        self.play(FadeIn(y_brace), FadeIn(y_text))
        self.play(ShowCreation(l3))
        self.play(FadeIn(z_brace), FadeIn(z_text))
        self.wait(1)
        self.play(Uncreate(l1), Uncreate(l2), Uncreate(l3), Uncreate(all_texts))

        # animate equation
        # move camera down first?
        
        eq_diff = TexMobject("\\frac{dy}{dx} = -\\frac{x}{\\sqrt{1-x^2}}")
        eqs = []
        eqs.append(TexMobject("\\sum \\sqrt{dy^2 + dx^2}"))
        eqs.append(TexMobject("\\int_{-1}^1 \\sqrt{","(dy)^2","+","(dx)^2", "}x"))
        eqs.append(TexMobject("\\int_{-1}^1 \\sqrt{","\\frac{(dy)^2}{(dx)^2}(dx)^2","+","\\frac{(dx)^2}{(dx)^2} (dx)^{2}", "}x"))
        eqs.append(TexMobject("\\int_{-1}^1 \\sqrt{","\\left( \\frac{dy}{dx} \\right)^2","+","1", "}\\, dxx"))
        eqs.append(TexMobject("\\int_{-1}^1 \\sqrt{","\\left( -\\frac{x}{\\sqrt{1-x^2}} \\right)^2","+","1", "}\\, dxx"))
        eqs.append(TexMobject("\\int_{-1}^1 \\sqrt{","\\left( \\frac{x^2}{1-x^2} \\right)","+","1", "}\\, dxx"))
        eqs.append(TexMobject("\\int_{-1}^1 \\frac{1}{\\sqrt{1-x^2}} \\, dxx"))
        eqs.append(TexMobject("\\arcsin x \\Big|_{-1}^{1}"))
        eqs.append(TexMobject("\\arcsin 1 - \\arcsin (-1)"))
        eqs.append(TexMobject("\\frac{\\pi}{2} - \\frac{-\\pi}{2}"))
        eqs.append(TexMobject("\\pi"))
        g1 = VGroup(*eqs)
        g1.scale(1.2).to_edge(DOWN)

        # start equation animation
        g0 = VGroup(eq_original, eq_diff, buff=2).arrange(DOWN).to_edge(UL)
        self.play(ReplacementTransform(eq_original, g0))
        self.play(ReplacementTransform(lines, eqs[0]))
        for i in range(len(eqs)-1):
            self.play(ReplacementTransform(eqs[i], eqs[i+1]))
            self.wait(0.5)
        self.wait()
        

        def func(self, x):
            return (math.sqrt(1-x**2))

    
    def integral_polar(self):
        self.setup_axes(animate = True)

        eq_original = TexMobject("\\vec{r}(\\theta) = \\cos \\theta \\vec{i} + \\sin \\theta \\vec{j}")
        eq_diff_norm = TexMobject("|| \\vec{r}\\,'(\\theta) || = 1")
        g_original = VGroup(eq_original, eq_diff_norm).arrange(DOWN)
        g_original.to_edge(UL)
        self.play(Write(eq_original))

        graph = self.get_graph(self.func, color = None, x_min = -1, x_max = 1)
        self.play(ShowCreation(graph))

        # demo with points
        for i in range(1,3):
            rays = VGroup()
            dots_curve = VGroup()
            lines = VGroup()
            
            prev_dot = Dot(self.coords_to_point(1, 0), radius = 0.1).set_color(BLUE)
            for k in range(2**(i+1)+1):
                theta = (PI*k/(2**(i+1)))
                ray = Arrow(self.graph_origin, self.coords_to_point(math.cos(theta), math.sin(theta)), buff = 0).set_color(PINK)
                rays.add(ray)
                self.play(ShowCreation(ray), run_time = 0.1)
            for k in range(2**(i+1)+1):
                theta = (PI*k/(2**(i+1)))
                dc = Dot(self.coords_to_point(math.cos(theta), math.sin(theta)), radius = 0.1).set_color(GREEN)
                dots_curve.add(dc)
                self.play(FadeIn(dc), run_time = 0.2)
                if k > 0:
                    new_line = Line(prev_dot, dc)
                    self.play(FadeIn(new_line), run_time = 0.1)
                    lines.add(new_line)
                    prev_dot = dc
            self.play(FadeOut(rays), FadeOut(dots_curve), FadeOut(lines))

        # animation showing arc length formula
        theta_0 = TAU/12
        p1 = Dot(self.coords_to_point(1, 0))
        p2 = Dot(self.coords_to_point(math.cos(theta_0), math.sin(theta_0)))
        l1 = Arrow(self.graph_origin, p1.get_center(), buff = 0).set_color(PINK)
        l2 = Arrow(self.graph_origin, p2.get_center(), buff = 0).set_color(GREEN)
        l3 = Arrow(p1.get_center(), p2.get_center(), buff = 0).set_color(BLUE)
        l1_text = TexMobject("\\vec{r}(\\theta)").next_to(l1, DOWN, buff = 0.2)
        l2_text = TexMobject("\\vec{r}(\\theta + \\Delta\\theta)").next_to(l2, UP, buff = 0.2)
        dr_text = TexMobject("\\vec{r}\\,'(\\theta)").next_to(l3, RIGHT)
        g = VGroup(l1, l2, l3, l1_text, l2_text)
        self.play(ShowCreation(l1))
        self.play(Write(l1_text))
        self.play(ShowCreation(l2))
        self.play(Write(l2_text))
        self.play(ShowCreation(l3))
        self.play(FadeIn(dr_text))
        self.wait(1)
        self.play(FadeOut(g))

        # animate equations
        
        eq_diff = TexMobject("\\vec{r}\\,'(\\theta) = -\\sin \\theta \\vec{i} + \\cos\\theta\\vec{j}")
        eq_diff_norm_new = TexMobject("|| \\vec{r}\\,'(\\theta) || = \\sqrt{(-\\sin\\theta)^{2} + (\\cos\\theta)^{2}} = 1")
        eq_diff_norm_new.generate_target()
        eq_diff_norm_new.target = eq_diff_norm
        '''
        eqs.append(TexMobject("\\sum ||\\vec{r} \\,'(\\theta) ||"))
        eqs.append(TexMobject("\\int_{0}^{\\pi} ||\\vec{r} \\,' || \\, d\\theta"))
        eqs.append(TexMobject("\\pi"))
        '''
        g1 = VGroup(eq_diff, eq_diff_norm_new).arrange(DOWN)
        g1.scale(1.2).to_edge(DOWN)
        self.play(Write(g1))
        self.wait(1)
        self.play(MoveToTarget(eq_diff_norm_new), FadeOut(eq_diff))
        self.wait()
        # start equation animation
        #g0 = VGroup(eq_original, eq_diff, buff=2).arrange(DOWN).to_edge(UL)
        #self.play(ReplacementTransform(eq_original, g0))
        #self.play(ReplacementTransform(lines, eqs[0]))
        '''
        for i in range(len(eqs)-1):
            self.play(ReplacementTransform(eqs[i], eqs[i+1]))
            self.wait(0.5)
        self.wait()
        '''
        # now use parametric
        #f_para = ParametricFunction(self.func, t_min = 0, t_max = TAU)

            
    def func(self, x):
        return (math.sqrt(1-x**2))