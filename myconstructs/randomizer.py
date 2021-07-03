from manimlib.imports import *

class Dice(VGroup):
    CONFIG = {
        "face": None,
        "pip_color": BLUE,
        "num_faces": 6
    }
    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        VGroup.__init__(self, **kwargs)
        if self.face == None:
            self.face = random.randint(1,self.num_faces)
        #self.face = face
        self.border = Square()
        self.face_mob = self.get_face_mob()
        self.face_mob.set_color(self.pip_color)
        self.face_mob.move_to(self.border.get_center())
        self.add(self.border, self.face_mob)

    def Roll(self, new_face = None):
        if new_face == None:
            new_face = random.randint(1,self.num_faces)

        self.set_value(new_face)
        new_face_mob = self.get_face_mob()
        new_face_mob.move_to(self.face_mob.get_center())
        new_face_mob.set_color(self.pip_color)
        anim_list = [
            Rotate(self.border, angel = TAU/2),
            FadeOut(self.face_mob),
            GrowFromCenter(new_face_mob)
        ]
        self.face_mob = new_face_mob

        return anim_list

    def get_value(self):
        return self.face

    def set_value(self, v):
        self.face = v

    def get_face_mob(self):
        return TexMobject(self.get_value())

class D6(Dice):
    def get_face_mob(self):
        '''
            Overwrite get_face_mob from the value itself to pips
        '''
        # 1 2 3
        # 4 5 6
        # 7 8 9
        pos_pips = [[], [5], [1,9], [1,5,9], [1,3,7,9], [1,3,5,7,9], [1,3,4,6,7,9]]
        pips = VGroup()
        for pos in pos_pips[self.face]:
            x = (pos-1) % 3
            y = np.floor((pos-1)/3)
            pips.add(
                Dot(x*RIGHT + y*DOWN, radius = 0.3)
            )
        # scale to fit dice face
        pips.scale(0.6) 
        return pips

class D4(Dice): 
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.num_faces = 4
        if face == None:
            face = random.randint(1,self.num_faces)
        self.face = face
        border = Triangle()
        face_mob = self.get_face_mob()
        face_mob.move_to(border.get_center())
        self.face_mob = face_mob
        self.add(border, face_mob)

class D20(Dice): 
    def __init__(self, **kwargs):
        
        VGroup.__init__(self, **kwargs)
        self.num_faces = 20
        if face == None:
            face = random.randint(1,self.num_faces)
        self.face = face
        border = RegularPolygon(7)
        face_mob = self.get_face_mob()
        face_mob.move_to(border.get_center())
        self.face_mob = face_mob
        self.add(border, face_mob)

class PlayingCard(VGroup):
    CONFIG = {
        "value": 1,
        "suit": "spade",
        "face_up": False
    }

    def __init__(self, value = 1, suit = "spade", **kwargs):
        VGroup.__init__(self, **kwargs)

        possible_suits = ["spade", "heart", "diamond", "club"]
        if possible_suits.count(suit) == 0:
            print("Illegal suit. Use spade as a default")
            self.suit = "spade"
        else:
            self.suit = suit
        self.value = value
        self.border = Rectangle(height = 3, width = 2)
        self.border.set_color(BLUE).set_stroke(None, 1).set_fill(PINK)

        # add value
        text = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        t = TexMobject(text[self.value]).scale(1.2).align_to(self.border, UL)
        t.shift(RIGHT*0.1 + DOWN*0.1)
        
        # add card suit
        suit_string = "\\" + self.suit + "suit"
        test = TexMobject(suit_string)
        self.add(test)
        s = TexMobject(suit_string).move_to(self.border.get_center())
        if self.suit == "heart" or self.suit == "diamond":
            s.set_color(RED)
        self.front = VGroup(t,s)

        # add card back
        back = self.border
        back.set_fill(GREEN).set_stroke(width = 0)
        self.back = VGroup(back)

        '''
        if self.face_up:
            self.front.set_z(0.1)
            self.back.set_z(-0.1)
        else:
            self.front.set_z(-0.1)
            self.back.set_z(0.1)
        '''

        self.add(self.border, self.front, self.back)
        
    '''
        Input: none
        Output: either card back (if face down), or the face (if face up)
    '''
    def get_value(self):
        return self.value, self.suit

    def Flip(self):
        ''' 
            Supposed to return card flipping animation
            but I can't create a good one yet, so for now let's just deal with transparency
        
        def flip_transparency(mob):
            mob.back.set_opacity(1 - mob.back.get_fill_opacity())
            mob.front.set_opacity(1 - mob.front.get_fill_opacity())
            return mob
        '''
        #return ApplyFunction(flip_transparency, self)
        return ApplyMethod(self.flip)
