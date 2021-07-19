from manimlib.imports import *

class TwoCircle_RightSide(Scene):
    def construct(self):
        self.show_axis()
        self.show_circle_dot()
        self.draw_cycle()

        self.wait()

    def show_axis(self):
        self.x_start = np.array([-6.5,2,0])
        x_axis = Line(self.x_start, np.array([6, 2, 0]))
        y_axis = Line(np.array([-5, 0, 0]), np.array([-5, 0, 0]))

        self.add(x_axis, y_axis)

        self.circle1_origin = np.array([-5, 2, 0])
        self.circle2_origin = np.array([-4, 2, 0])

        self.one_cycle_length = 2 * PI

    def show_circle_dot(self):
        circle1 = Circle(radius=1)
        circle2 = Circle(radius=0.3)
        circle1.move_to(self.circle1_origin)
        circle2.move_to(self.circle2_origin)

        dot1 = Dot(radius=0.04, color=YELLOW)
        dot1.move_to(circle1.point_from_proportion(0))

        dot2 = Dot(radius=0.04, color=YELLOW)
        dot2.move_to(circle2.point_from_proportion(0))

        self.dot1_freq = 1.0
        self.dot2_freq = 3.0

        self.add(circle1, circle2, dot1, dot2)
        self.circle1, self.circle2 = circle1, circle2
        self.dot1, self.dot2 = dot1, dot2
        self.curve_start = dot2.get_center()

    def draw_cycle(self):
        self.t_offset = 0
        self.t_rate = 0.5
        self.one_cycle_time = 4

        def rotate_dot1(mob, dt):
            self.t_offset += (dt * self.t_rate)
            mob.move_to(self.circle1.point_from_proportion(((self.t_offset * self.dot1_freq) / self.one_cycle_time) % 1))

        def update_circle2(mob):
            circle = Circle(radius = 0.3)
            circle.move_to(self.dot1.get_center())
            mob.become(circle)

        def update_dot2(mob):
            mob.move_to(self.circle2.point_from_proportion(((self.t_offset * self.dot2_freq) / self.one_cycle_time) % 1))

        line_to_curve = Line(self.dot2.get_center(), self.dot2.get_center())
        def update_line_to_curve(mob):
            x = self.curve_start[0] + self.t_offset
            y = self.dot2.get_center()[1]
            line = Line(self.dot2.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )
            mob.become(line)

        cosine_curve = VGroup()
        cosine_curve.add(Line(self.curve_start, self.curve_start))
        def update_curve(mob):
            curve = mob.copy()
            last_line = curve[-1]
            x = self.curve_start[0] + self.t_offset
            y = self.dot2.get_center()[1]
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            curve.add(new_line)

            mob.become(curve)

        self.dot1.add_updater(rotate_dot1)
        self.circle2.add_updater(update_circle2)
        self.dot2.add_updater(update_dot2)

        line_to_curve.add_updater(update_line_to_curve)
        cosine_curve.add_updater(update_curve)

        self.add(line_to_curve, cosine_curve)
        self.wait(self.one_cycle_time * 4.1)

        self.dot1.remove_updater(rotate_dot1)