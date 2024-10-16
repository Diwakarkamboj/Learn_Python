def myfunc():
    try:
        a = int(input("Ente a number: "))
        print(a)
        
    except Exception as e:
      print(e)
    
    finally:
      print("I'm inside finally block")

    
myfunc()

print(__name__)

if __name__ == "__main__":
  print("this will not  run in main.py file")
