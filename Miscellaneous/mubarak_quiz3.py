class Paral:

  try:
    name =open("/Users/seamlesshr/Documents/Cds/Py/ttt.txt")
  except:
    print("SEEMS FILE DOESN'T EXIST ON YOUR LAPTOP")
  finally:
    print("BYE BYE")

  name = ''
  def __init__(self):
        qateam = ["Azeez", "Nathaniel", "Mutiu", "Timilehin", "Boluwatife","Nasifudeen", "John", "Mubarak"]
        for name in qateam:
          print("*****************************************")
          if(name == "Timilehin"):
            print(name + " YOU ARE THE TEAM LEAD OF SEAMLESSHR QA TEAM")
          elif(name == "Boluwatife"):
            print(name + " IS THE TEAM L&D DIRECTOR")
          else:
            print(name + " IS MEMBER OF THE QA TEAM")
    
      
q = Paral()
