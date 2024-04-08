from cipher import Cipher


class AtbashCipher(Cipher):
  '''
  The AtbashCipher class\n
  encrypt_letter(self, letter) -> str: returns the letter at the opposite end of the alphabet
  decrypt_letter(self, letter) -> str: returns the letter at the opposite end of the alphabet. The only reason this exists is to match the interface of Cipher
  '''

  def encrypt_letter(self, letter) -> str:
    '''Returns the letter at the opposite end of the alphabet'''
    loc = 0
    #if not in 1-25, it is already set to 0
    for i in range(1, 26):
      if (letter == self._alphabet[i]):
        loc = i
        break
    new_loc = 25 - loc
    return self._alphabet[new_loc]

  def decrypt_letter(self, letter) -> str:
    '''Returns the letter at the opposite end of the alphabet'''
    loc = 0
    for i in range(1, 26):
      if (letter == self._alphabet[i]):
        loc = i
        break
    new_loc = 25 - loc
    return self._alphabet[new_loc]
