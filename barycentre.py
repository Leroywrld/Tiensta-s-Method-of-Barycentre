import math
import pandas as pd
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
    
    def get_c(self):
        bearing_BC = self.get_bearing(self.E_B, self.N_B, self.E_C, self.N_C)
        bearing_CB = self.get_back_bearing(bearing_BC)
        bearing_AC = self.get_bearing(self.E_A, self.N_A, self.E_C, self.N_C)
        bearing_CA = self.get_back_bearing(bearing_AC)
        angle_c = (bearing_CB - bearing_CA)
        return angle_c 
    
    def get_k(self, angle_one, angle_two):
        self.angle_one = angle_one
        self.angle_two = angle_two
        cot_angle_one = 1/(math.tan(math.radians(self.angle_one)))
        cot_angle_two = 1/(math.tan(math.radians(self.angle_two)))
        k = 1/(cot_angle_one - cot_angle_two)
        return k
    
    def get_easting_p(self):
        k_1 = self.get_k(self.get_a(), self.get_y())
        k_2 = self.get_k(self.get_b(), self.get_z())
        k_3 = self.get_k(self.get_c(), self.get_x())
        numerator = (self.E_A*k_1) + (self.E_B*k_2) + (self.E_C*k_3)
        denominator = (k_1 + k_2 + k_3)
        easting = numerator/denominator
        return easting
    
    def get_northing_p(self):
        k_1 = self.get_k(self.get_a(), self.get_y())
        k_2 = self.get_k(self.get_b(), self.get_z())
        k_3 = self.get_k(self.get_c(), self.get_x())
        numerator = (self.N_A*k_1) + (self.N_B*k_2) + (self.N_C*k_3)
        denominator = (k_1 + k_2 + k_3)
        northing = numerator/denominator
        return northing
    def output_data(self):
        dict = {
            'NORTHING': [self.get_northing_p()],
            'EASTING': [self.get_easting_p()]
        }
        dataframe = pd.DataFrame(dict)
        print(dataframe)
        
        
tm = TienstasMethod(8609.71, 3613.52, 3487.16, 7444.39, 1712.06, 1693.38, 0.00, 112.5805556, 245.7225)
tm.output_data()