from cipher import Cipher

class CaesarCipher(Cipher):
  '''
  The CaesarCipher class\n
  (int) shift: the shift on the cipher
  encrypt_letter(letter) -> str: shifts letter to the right by shift\n
  decrypt_letter(letter) -> strL shifts letter to the left by shift\n
  '''

  def __init__(self, shift):
    '''Constructs a cesar cipher and initializes the shift'''
    super().__init__ ()#Don't forget this!
    self.shift = shift #Raise exception if below 0 or above 25


  def encrypt_letter(self, letter) -> str:
    '''Shifts letter to the right by shift'''
    loc = 0
    for i in range(1,26):
      if(letter == self._alphabet[i]):
        loc = i
        break
    #Apply the shift
    new_loc = (loc + self.shift)%26
    return self._alphabet[new_loc]

  def decrypt_letter(self, letter) -> str:
    '''Shifts letter to the left by shift'''
    loc = 0
    for i in range(1,26):
      if self._alphabet[i] == letter.upper():
        loc = i
        break
    new_loc = (loc - self.shift)%26
    return self._alphabet[new_loc]