from manimlib.imports import *

class Thai(Scene):
    def construct(self):
        title1 = Text("今日も", font="MS Gothic")
        title2 = Text("雪歩は", font="MS Gothic")
        title3 = Text("可愛いな", font="MS Gothic")
        title = VGroup(title1, title2, title3).arrange(DOWN)
        #title.scale(3).set_color_by_gradient([, WHITE])
        title.scale(3).set_color_by_gradient([BLUE, Color("#d3dde9")])
        self.play(DrawBorderThenFill(title1))
        self.play(DrawBorderThenFill(title2))
        self.play(DrawBorderThenFill(title3))
        self.wait()

        snow1 = self.get_snow(4)
        snow1.to_edge(RIGHT).set_color_by_gradient([BLUE, Color("#d3dde9")])
        snow2 = self.get_snow(4)
        snow2.to_edge(LEFT).set_color_by_gradient([BLUE, Color("#d3dde9")])
        self.play(ShowCreation(snow1), ShowCreation(snow2))
        self.play(Rotating(snow1), Rotating(snow2))

    def get_snow(self, num_gen = 3):
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

        start_lines = VGroup()
        # create starting lines
        for i in range(6):
            p1 = np.array([np.cos(TAU*i/6), np.sin(TAU*i/6), 0])
            p2 = np.array([np.cos(TAU*(i+1)/6), np.sin(TAU*(i+1)/6), 0])
            start_lines.add(
                Line(p1, p2)
            ) 

        latest_gen = start_lines
        for i in range(num_gen):
            new_gen = next_gen(latest_gen)
            latest_gen = new_gen

        return latest_gen