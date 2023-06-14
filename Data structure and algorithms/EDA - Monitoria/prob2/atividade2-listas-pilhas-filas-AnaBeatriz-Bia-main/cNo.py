class No:

  def __init__(self, dado=0):

      self.__dado__ = dado
      self.__prox__ = None


  def __str__(self):

      outStr = ""

      if self:
          outStr +=  "+======+=================+\n"
          outStr += f'| {self.__dado__:4} | {hex(id(self.__prox__))} | {hex(id(self))} \n'
          outStr +=  "+======+=================+\n"
          outStr +=  "                 |   \n"
          outStr +=  "                 |   \n"
          outStr +=  "           +-----+   \n"
          outStr +=  "           |            \n"
          if self.__prox__:
              outStr +=  "           V            \n"
          else:
              outStr +=  "           =            \n"
      
      return outStr

  def setDado(self, dado):

      self.__dado__ = dado

  def setProx(self, prox):

      if type(prox) == No:
          self.__prox__ = prox
      else:
          self.__prox__ = None

  def getDado(self):
      return self.__dado__

  def getProx(self):
      return self.__prox__
