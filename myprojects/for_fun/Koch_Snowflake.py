from manim import *
from colour import Color

class Fractal(Scene):
    def construct(self, step = 3, radius = 3):
        def next_gen(lines):
            new_lines = VGroup()
            for l in lines:
                new_lines.add(*generate_from_seed(l))
            return new_lines
            
        def generate_from_seed(line):
            p1, p2 = line.get_start_and_end()
            points = [p1, 0, 0, 0, p2]
            #            m2
            #          /    \
            #  p1 - m1       m3 - p2
            points[1] = 2*p1/3 + p2/3
            points[3] = p1/3 + 2*p2/3
            theta = PI/3
            rot_sixty = np.array([
                [np.cos(theta), -np.sin(theta), 0], 
                [np.sin(theta), np.cos(theta), 0], 
                [0,0,1]
            ])
            points[2] = points[1] + np.transpose(rot_sixty @ np.transpose(points[3]-points[1]))

            new_group = VGroup()
            for i in range(4):
                new_group.add(Line(points[i], points[i+1]))
            new_group.set_color(line.get_color())

            return new_group

        #title = TexMobject("\\text{Start}")
        #title.to_edge(UP)
        #self.add(title)

        start_lines = VGroup()
        # create starting lines
        for i in range(6):
            p1 = np.array([radius * np.cos(TAU*i/6), radius * np.sin(TAU*i/6), 0])
            p2 = np.array([radius * np.cos(TAU*(i+1)/6), radius * np.sin(TAU*(i+1)/6), 0])
            color1 = Color(rgb=(i/6, i/6, 1))
            color2 = Color(rgb=((i+1)/6, (i+1)/6, 1))
            start_lines.add(
                Line(p1, p2).set_color_by_gradient([color1, color2])
            ) 

        self.add(start_lines)
        latest_gen = start_lines
        for i in range(step):
            #title_text = "n = " + str(i+1)
            #title.become(TexMobject(title_text).to_edge(UP))
            new_gen = next_gen(latest_gen)
            new_gen.rotate(angle = TAU/12)
            self.play(
                ReplacementTransform(latest_gen, new_gen),
                rate_func = smooth,
                run_time = 1
                )
            latest_gen = new_gen
        
        smaller = latest_gen.copy()
        self.play(ScaleInPlace(smaller,0.5))
        self.play(Rotating(latest_gen, radians = -TAU, run_time = 5), Rotating(smaller, radians = TAU, run_time = 5))
        
    