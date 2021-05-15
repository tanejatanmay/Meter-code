m = input("ENTER YOUR METER TYPE: ")
u = float(input("ENTER NUMBER OF UNITS CONSUMED: "))

try:
    m == "commercial"
    m == "Commercial"
    m == "domestic"
    m == "Domestic"
    if m == "domestic" or m == "Domestic" and u < 200:
        fc = 200
        tt = (u * 2.85) + fc
    elif m == "domestic" or m == "Domestic" and 200 <= u < 400:
        fc = 200
        tt = (u * 4) + fc
    elif m == "domestic" or m == "Domestic" and 400 <= u < 600:
        fc = 200
        tt = (u * 6) + fc
    elif m == "domestic" or m == "Domestic" and 600 <= u:
        fc = 200
        tt = (u * 8) + fc
    elif m == "commercial" or m == "Commercial" and u < 200:
        fc = 400
        tt = (u * 3.5) + fc
    elif m == "commercial" or m == "Commercial" and 200 <= u < 400:
        fc = 400
        tt = (u * 6) + fc
    elif m == "commercial" or m == "Commercial" and 400 <= u < 600:
        fc = 400
        tt = (u * 8) + fc
    elif m == "commercial" or m == "Commercial" and 600 <= u:
        fc = 400
        tt = (u * 10) + fc
    gst = 0.18 * (tt)
    total = tt + gst
    print("Type of meter used:", m)
    print("Number of units consumed:", u)
    print("Fixed charges:", fc)
    print("Amount:", tt)
    print("GST charged:", gst)
    print("Total amount charged:", total)

except:
    print("Invalid meter type")
