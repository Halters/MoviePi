##
## EPITECH PROJECT, 2018
## api_gateway
## File description:
## flag.py
##

class Flag(object):
    flag_name = ""
    flag_weight = 0.0

    def __init__(self, line):
        temp_str = line.split('=')
        self.setFlagName(temp_str[0])
        self.setFlagWeight(temp_str[1])

    def setFlagName(self, str):
        self.flag_name = str

    def setFlagWeight(self, nb):
        try:
            self.flag_weight = float(nb)
        except ValueError:
            self.flag_weight = -1.0