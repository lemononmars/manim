from manim import *

class Intro(Scene):
   def construct(self):
      #self.math_def()
      self.rotating_tick(5)

   def math_def(self):
      return

   def get_farey_fractions(self, n):
      points = [(0,1)]
      for i in range(1, n+1):
         for j in range(1, i+1):
            if np.gcd(i,j) == 1:
               points.append((j,i))
      points.sort(key=lambda x: self.c2f(x))
      return points

   def c2f(self, c):
      return c[0]/c[1]

   def rotating_tick(self, n):
      #self.axis = Axes(x_range = [0,n,1], y_range = [0,n,1], x_length = 4, y_length = 4)
      #self.play(ShowCreation(self.axis))

      ff = self.get_farey_fractions(n)

      center = Dot(ORIGIN, radius = 0.1, color = YELLOW)
      width = 4/n
      self.endpoint = Dot(RIGHT*10) # used with updater
      self.line = Line(ORIGIN, width*RIGHT, stroke_width = 3, color = BLUE) # start at (1,0)
      
      dot_counts = ValueTracker(0)
      dot_count_num = Integer(np.int(dot_counts.get_value()))
      dot_count_text = VGroup(MathTex('n ='), dot_count_num).arrange(RIGHT)
      dot_count_text.to_corner(UL)
      self.add(dot_count_text, dot_count_num)
      dot_count_num.add_updater(
         lambda x: x.set_value(
            np.int(dot_counts.get_value())
         )
      )
      
      Dark_points = []
      for i in range(1, n+1):
         for j in range(0, i+1):
            Dark_points.append(Dot(i*width*RIGHT + j*width*UP, fill_opacity = 0.3))
      Dark_point_group = VGroup(*Dark_points)
      self.add(Dark_point_group, center)

      ff_text = VGroup(*[MathTex(r"\frac{%d}{%d}"%(f[0],f[1])) for f in ff]).scale(0.8)
      ff_text.arrange_in_grid(rows = 2, buff = 0.4)
      ff_text.to_edge(DOWN)

      # start animating the line and hitting the first dot
      self.play(Create(self.line))
      self.add_sound("Ding")
      d = Dot(width*RIGHT + 0*UP, color = GREEN)
      self.add(d)
      self.add(ff_text[np.int(dot_counts.get_value())])
      dot_counts.increment_value(1)
      
      def update_func(mob, dt):
         if mob.get_y()/mob.get_x() >= 1:
            return
         mob.rotate(dt*0.1, about_point = ORIGIN)

         # check if the line is about to reach the next dot
         if np.int(dot_counts.get_value()) < len(ff) and np.abs(mob.get_y()/mob.get_x() - self.c2f(ff[np.int(dot_counts.get_value())])) <= 0.01:
            next_dot = ff[np.int(dot_counts.get_value())]
            newdot = Dot(next_dot[1]*width*RIGHT + next_dot[0]*width*UP, color = GREEN)
            self.add(newdot)
            # TODO: add melody according to distance!
            self.add_sound("Ding")
            self.add(ff_text[np.int(dot_counts.get_value())])
            dot_counts.increment_value(1)
         
         # check if the line is leaving the previous dot
         self.line.become(Line(ORIGIN, mob, stroke_width = 3, color = RED))
         if np.int(dot_counts.get_value()) > 0 and np.abs(mob.get_y()/mob.get_x() - self.c2f(ff[np.int(dot_counts.get_value())-1])) <= 0.01:
            curr_dot = ff[np.int(dot_counts.get_value())-1]
            line_len = np.sqrt(curr_dot[0]**2 + curr_dot[1]**2)
            self.line.set_color(BLUE)
            self.line.scale_about_point(width*line_len/10, ORIGIN)

      self.endpoint.add_updater(update_func)
      self.add(self.endpoint)
      self.wait(9)
      #self.endpoint.remove_updater(update_func)
      #self.wait(2)
      #self.remove(*dot_passed_texts)
      #self.remove(Points_group, self.line)
      #self.wait()