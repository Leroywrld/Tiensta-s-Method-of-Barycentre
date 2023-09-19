import math
class TienstasMethod():
    def __init__(self, N_A: float, E_A: float, N_B: float, E_B: float, 
                 N_C: float, E_C: float, dir_PA: float, dir_PB: float, dir_PC: float):
        self.N_A = N_A
        self.E_A = E_A
        self.N_B = N_B
        self.E_B = E_B
        self.N_C = N_C 
        self.E_C = E_C
        self.dir_PA = dir_PA
        self.dir_PB = dir_PB
        self.dir_PC = dir_PC
    
    def get_bearing(self, x_1, y_1, x_2, y_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        change_x = (self.x_1 - self.x_2)
        change_y = (self.y_1 - self.y_2)
        gradient = change_x / change_y
        bearing = math.degrees(math.atan(gradient))
        if bearing < 180:
            bearing = bearing + 180
        return bearing
    
    def get_back_bearing(self, f_bearing):
        if f_bearing < 180:
            b_bearing = f_bearing + 180
        elif f_bearing > 180:
            b_bearing = f_bearing - 180
        return b_bearing
    
    def get_x(self):
        angle_x = (self.dir_PB - self.dir_PA)
        return angle_x
    
    def get_y(self):
        angle_y = (self.dir_PC - self.dir_PB)
        return angle_y
    
    def get_z(self):
        angle_z = (self.dir_PA - self.dir_PC + 360)
        return angle_z
    
    def get_a(self):
        bearing_AB = self.get_bearing(self.E_A, self.N_A, self.E_B, self.N_B)
        bearing_AC = self.get_bearing(self.E_A, self.N_A, self.E_C, self.N_C)
        angle_a = (bearing_AC - bearing_AB)
        return angle_a
    
    def get_b(self):
        bearing_AB = self.get_bearing(self.E_B, self.N_B, self.E_A, self.N_A)
        bearing_BA = self.get_back_bearing(bearing_AB)
        bearing_BC = self.get_bearing(self.E_B, self.N_B, self.E_C, self.N_C)
        angle_b = (bearing_BA - bearing_BC)
        return angle_b
    
tm = TienstasMethod(8609.71, 3613.52, 3487.16, 7444.39, 1712.06, 1693.38, 0.00, 112.5805556, 245.7225)
print(f"angle x = {tm.get_x()}")
print(f"angle y = {tm.get_y()}")
print(f"angle z = {tm.get_z()}")
print(f"angle a = {tm.get_a()}")
print(f"angle b = {tm.get_b()}")