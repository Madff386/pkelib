
import mpmath as mp
from mpmath import *
import math

mp.dps = 10000 

class pke:
    def __init__(self, message):
        self.message = str(message)

    def encrypt(self, e=11, pq=3233):
        self.e = e
        self.pq = pq
        enmessage = []
        emessage = []     # define lists
        encrypted = []
        for counter in range(0, len(self.message)):   # loop through all element in message
            enmessage.append(self.message[counter])
        
        for cc in enmessage:     # replace all characters with corosponding numbers
            if cc == 'a':
                emessage.append(13)
            elif cc == 'b':
                emessage.append(14)
            elif cc == 'c':
                emessage.append(15)
            elif cc == 'd':
                emessage.append(16)
            elif cc == 'e':
                emessage.append(17)
            elif cc == 'f':
                emessage.append(18)
            elif cc == 'g':
                emessage.append(19)
            elif cc == 'h':
                emessage.append(20)
            elif cc == 'i':
                emessage.append(21)
            elif cc == 'j':
                emessage.append(22)
            elif cc == 'k':
                emessage.append(23)
            elif cc == 'l':
                emessage.append(24)
            elif cc == 'm':
                emessage.append(25)
            elif cc == 'n':
                emessage.append(26)
            elif cc == 'o':
                emessage.append(27)
            elif cc == 'p':
                emessage.append(28)
            elif cc == 'q':
                emessage.append(29)
            elif cc == 'r':
                emessage.append(30)
            elif cc == 's':
                emessage.append(31)
            elif cc == 't':
                emessage.append(32)
            elif cc == 'u':
                emessage.append(33)
            elif cc == 'v':
                emessage.append(34)
            elif cc == 'w':
                emessage.append(35)
            elif cc == 'x':
                emessage.append(36)
            elif cc == 'y':
                emessage.append(37)
            elif cc == 'z':
                emessage.append(38)
            elif cc == '1':
                emessage.append(3)
            elif cc == '2':
                emessage.append(4)
            elif cc == '3':
                emessage.append(5)
            elif cc == '4':
                emessage.append(6)
            elif cc == '5':
                emessage.append(7)
            elif cc == '6':
                emessage.append(8)
            elif cc == '7':
                emessage.append(9)
            elif cc == '8':
                emessage.append(10)
            elif cc == '9':
                emessage.append(11)
            elif cc == '0':
                emessage.append(12)
            elif cc == ' ':
                emessage.append(39)
            elif cc == '.':
                emessage.append(40)
            elif cc == ',':
                emessage.append(41)
            elif cc == ':':
                emessage.append(42)
            elif cc == '!':
                emessage.append(43)
            elif cc == '?':
                emessage.append(44)
            elif cc == 'A':
                emessage.append(45)
            elif cc == 'B':
                emessage.append(46)
            elif cc == 'C':
                emessage.append(47)
            elif cc == 'D':
                emessage.append(48)
            elif cc == 'E':
                emessage.append(49)
            elif cc == 'F':
                emessage.append(50)
            elif cc == 'G':
                emessage.append(51)
            elif cc == 'H':
                emessage.append(52)
            elif cc == 'I':
                emessage.append(53)
            elif cc == 'J':
                emessage.append(54)
            elif cc == 'K':
                emessage.append(55)
            elif cc == 'L':
                emessage.append(56)
            elif cc == 'M':
                emessage.append(57)
            elif cc == 'N':
                emessage.append(58)
            elif cc == 'O':
                emessage.append(59)
            elif cc == 'P':
                emessage.append(60)
            elif cc == 'Q':
                emessage.append(61)
            elif cc == 'R':
                emessage.append(62)
            elif cc == 'S':
                emessage.append(63)
            elif cc == 'T':
                emessage.append(64)
            elif cc == 'U':
                emessage.append(65)
            elif cc == 'V':
                emessage.append(66)
            elif cc == 'W':
                emessage.append(67)
            elif cc == 'X':
                emessage.append(68)
            elif cc == 'Y':
                emessage.append(69)
            elif cc == 'Z':
                emessage.append(70)
            elif cc == '@':
                emessage.append(71)
            elif cc == '#':
                emessage.append(72)
            elif cc == '$':
                emessage.append(73)
            elif cc == '%':
                emessage.append(74)
            elif cc == '^':
                emessage.append(75)
            elif cc == '&':
                emessage.append(76)
            elif cc == '*':
                emessage.append(77)
            elif cc == '(':
                emessage.append(78)
            elif cc == ')':
                emessage.append(79)
            elif cc == '-':
                emessage.append(80)
            elif cc == '_':
                emessage.append(81)
            elif cc == '=':
                emessage.append(82)
            elif cc == '+':
                emessage.append(83)
            elif cc == '{':
                emessage.append(84)
            elif cc == '}':
                emessage.append(85)
            elif cc == '|':
                emessage.append(87)
            elif cc == ';':
                emessage.append(88)
            elif cc == '"':
                emessage.append(89)
            elif cc == '\'':
                emessage.append(90)
            elif cc == '>':
                emessage.append(91)
            elif cc == '<':
                emessage.append(92)
            elif cc == '/':
                emessage.append(93)
            

            
        for thing in emessage:  
            sep = '.'
            quotent = (thing**self.e)/(self.pq)   # compute quotent
            rquotent = str(quotent)
            r = rquotent.split(sep, 1)[1]   #[
            r = ("0." + r)
            r = mpf(r)                      
            t = float(r)*(self.pq)
            t = t*100000
            t = str(t)
            t = t.split(sep, 1)[0] 
            t = float(t)
            t = t/100000
            encrypted_char = round(t)        #] compute remainder
            encrypted.append(encrypted_char)   # combine to new list
            self.message = encrypted

    def decrypt(self, d=851, pq=3233):
        self.pq = mpf(pq)
        self.d = mpf(d)
        self.message = str(self.message)
        self.message = self.message.replace(',', '')
        self.message = self.message.replace('~', ',')
        self.message = self.message.replace(']', '')
        self.message = self.message.replace('[', '')
        demessage = []
        dmessage = []      
        decrypted = []
        data = self.message.split()
        for temp in data:
            temp = int(temp)         # splits message into list
            demessage.append(temp)
        for thing in demessage:
            sep = '.'
            quotent = mpf()
            quotent = (thing**self.d)/(self.pq)   #[
            rquotent = str(quotent)
            r = rquotent.split(sep, 1)[1]
            r = ("0." + r)
            r = mpf(r)
            t = float(r)*(self.pq)
            t = t*100000
            t = str(t)
            t = t.split(sep, 1)[0]
            t = float(t)
            t = t/100000
            decrypted_char = round(t)       #] computes remaider
            dmessage.append(decrypted_char)  # puts in list

            # replaces number with corosponding character
        for cc in dmessage:
            if cc == 3:
                decrypted.append('1')
            if cc == 4:
                decrypted.append('2')
            if cc == 5:
                decrypted.append('3')
            if cc == 6:
                decrypted.append('4')
            if cc == 7:
                decrypted.append('5')
            if cc == 8:
                decrypted.append('6')
            if cc == 9:
                decrypted.append('7')
            if cc == 10:
                decrypted.append('8')
            if cc == 11:
                decrypted.append('9')
            if cc == 12:
                decrypted.append('0')
            if cc == 13:
                decrypted.append('a')
            if cc == 14:
                decrypted.append('b')
            if cc == 15:
                decrypted.append('c')
            if cc == 16:
                decrypted.append('d')
            if cc == 17:
                decrypted.append('e')
            if cc == 18:
                decrypted.append('f')
            if cc == 19:
                decrypted.append('g')
            if cc == 20:
                decrypted.append('h')
            if cc == 21:
                decrypted.append('i')
            if cc == 22:
                decrypted.append('j')
            if cc == 23:
                decrypted.append('k')
            if cc == 24:
                decrypted.append('l')
            if cc == 25:
                decrypted.append('m')
            if cc == 26:
                decrypted.append('n')
            if cc == 27:
                decrypted.append('o')
            if cc == 28:
                decrypted.append('p')
            if cc == 29:
                decrypted.append('q')
            if cc == 30:
                decrypted.append('r')
            if cc == 31:
                decrypted.append('s')
            if cc == 32:
                decrypted.append('t')
            if cc == 33:
                decrypted.append('u')
            if cc == 34:
                decrypted.append('v')
            if cc == 35:
                decrypted.append('w')
            if cc == 36:
                decrypted.append('x')
            if cc == 37:
                decrypted.append('y')
            if cc == 38:
                decrypted.append('z')
            if cc == 39:
                decrypted.append(' ')
            if cc == 40:
                decrypted.append('.')
            if cc == 41:
                decrypted.append('~')
            if cc == 42:
                decrypted.append(':')
            if cc == 43:
                decrypted.append('!')
            if cc == 44:
                decrypted.append('?')
            if cc == 45:
                decrypted.append('A')
            if cc == 46:
                decrypted.append('B')
            if cc == 47:
                decrypted.append('C')
            if cc == 48:
                decrypted.append('D')
            if cc == 49:
                decrypted.append('E')
            if cc == 50:
                decrypted.append('F')
            if cc == 51:
                decrypted.append('G')
            if cc == 52:
                decrypted.append('H')
            if cc == 53:
                decrypted.append('I')
            if cc == 54:
                decrypted.append('J')
            if cc == 55:
                decrypted.append('K')
            if cc == 56:
                decrypted.append('L')
            if cc == 57:
                decrypted.append('M')
            if cc == 58:
                decrypted.append('N')
            if cc == 59:
                decrypted.append('O')
            if cc == 60:
                decrypted.append('P')
            if cc == 61:
                decrypted.append('Q')
            if cc == 62:
                decrypted.append('R')
            if cc == 63:
                decrypted.append('S')
            if cc == 64:
                decrypted.append('T')
            if cc == 65:
                decrypted.append('U')
            if cc == 66:
                decrypted.append('V')
            if cc == 67:
                decrypted.append('W')
            if cc == 68:
                decrypted.append('X')
            if cc == 69:
                decrypted.append('Y')
            if cc == 70:
                decrypted.append('Z')
            if cc == 71:
                decrypted.append('@')
            if cc == 72:
                decrypted.append('#')
            if cc == 73:
                decrypted.append('$')
            if cc == 74:
                decrypted.append('%')
            if cc == 75:
                decrypted.append('^')
            if cc == 76:
                decrypted.append('&')
            if cc == 77:
                decrypted.append('*')
            if cc == 78:
                decrypted.append('(')
            if cc == 79:
                decrypted.append(')')
            if cc == 80:
                decrypted.append('-')
            if cc == 81:
                decrypted.append('_')
            if cc == 82:
                decrypted.append('=')
            if cc == 83:
                decrypted.append('+')
            if cc == 84:
                decrypted.append('{')
            if cc == 85:
                decrypted.append('}')
            if cc == 87:
                decrypted.append('|')
            if cc == 88:
                decrypted.append(';')
            if cc == 89:
                decrypted.append('"')
            if cc == 90:
                decrypted.append('\'')
            if cc == 91:
                decrypted.append('>')
            if cc == 92:
                decrypted.append('<')
            if cc == 93:
                decrypted.append('/')
             
        plaintext = ''.join(decrypted)       # returns decrypted message as string
        self.message = plaintext






