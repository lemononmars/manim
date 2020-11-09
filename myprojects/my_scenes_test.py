#!/usr/bin/env python

from manimlib.imports import *
import numpy as np

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()

class TestNumberLine(Scene):
    def construct(self):
        t = TextMobject(
            "This is the real line",
            tex_to_color_map={"real": YELLOW, "line": BLUE}
        )
        nl = NumberLine()
        nl2 = NumberLine()
        nl2.p2n(0)
        group = VGroup(t, nl)
        group.arrange(DOWN)
        self.play(
            Write(t),
            Write(nl)
        )
        self.wait()
        self.play(
            Transform(nl, nl2)
        )
        self.wait()

class TestPolar(Scene):
    def construct(self):
        text = TextMobject(
            "Petal plot"
        )
        p = PolarCurve(lambda theta: 1 - np.cos(theta))
        t = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        t.add_updater(lambda d: d.set_value(p.get_point_from_function(0.5)))

        group = VGroup(text, p, t)
        group.arrange(UP)
        group.set_height(FRAME_HEIGHT - 2 * LARGE_BUFF)
        self.play(
            Write(text),
            ShowCreation(p),
            Write(t),
            run_time=5
        )
        self.wait()

class TestMatrix(Scene):
    def construct(self):
        m = Matrix([[1,2],[3,5]])
        m.set_column_colors(GREEN, RED)
        self.play(
            Write(m)
        )
        self.wait()

        newm = Matrix([[2,3], [1,2]])
        self.play(
            Transform(m, newm)
        )
        self.wait()
        

class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is going to be awesome",
            tex_to_color_map={"awesome": YELLOW, "This": GREEN}
        )
        example_tex = TexMobject(
            "\\int x^n \\, dx = \\frac{x^{n+1}}{n+1} + C",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(
            Write(example_text),
            FadeInFrom(example_tex, RIGHT)
        )
        self.wait()
        example_text2 = TextMobject(
            "Try random stuff",
            tex_to_color_map={"random": RED, "stuff": BLUE}
        )
        example_text2.to_corner(UP + RIGHT)
        
        example_tex2 = TexMobject(
            "\\alpha \\qquad \\beta \\\ \\gamma \\omega \\lambda \\zeta",
        )
        group = VGroup(example_text2, example_tex2)
        group.arrange(UP)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(
            Transform(example_text, example_text2),
            LaggedStart(*map(FadeOutAndShiftDown, example_tex)),
            FadeInFrom(example_tex2, DOWN)
        )
        self.wait()

class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

# See old_projects folder for many, many more
