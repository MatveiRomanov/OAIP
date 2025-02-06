from sortt import sortt
from star_filling import star_filling
from nearby import nearby

def main():
    print(sortt([("Lock", 1, "Stock"), ("and", 9, "Two"), ("Smoking", 98, "Barrels")]))
    print(star_filling("Expanding the space available for living"))
    print(nearby())

if __name__ == "__main__":
    main()