import abc


class Cipher(abc.ABC):
  '''
  The abstract class for ciphers\n
  (str) alphabet - The alphabet\n
  encrypt_message(msg) -> str: Runs msg through the encrypt_letter method\n
  decrypt_message(msg) -> str: Runs msg through the decrypt_letter method\n
  encrypt_letter(letter) and decrypt_letter(letter) are abstract methods to be overridden. Both return strings
  '''

  def __init__(self):
    '''Initializes the alphabet'''
    self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  def encrypt_message(self, msg: str) -> str:
    '''Encrypts msg one letter at a time'''
    temp = msg.upper()
    code = ""
    for char in temp:
      if (char in self._alphabet):
        #If char is a letter, encrypt it
        code += self.encrypt_letter(char)
      else:
        #else, add it on
        code += char
    return code

  def decrypt_message(self, msg: str) -> str:
    '''Decrypts msg one letter at a time'''
    temp = msg.upper()
    secret = ""
    for char in temp:
      if (char in self._alphabet):
        secret += self.decrypt_letter(char)
      else:
        secret += char
    return secret

  @abc.abstractmethod
  def encrypt_letter(self, letter) -> str:
    '''Encrypts letter'''
    pass

  @abc.abstractmethod
  def decrypt_letter(self, letter) -> str:
    '''Decrypts letter'''
    pass

  @property
  def alphabet(self):
    '''Accesses the alphabet property'''
    return self._alphabet
