import itertools

print("¡Bienvenido!")
print(
    "Cómo disponibilidad ofrecemos las siguientes Funciones Generadoras Ordinarias:"
)
print(
    "1. Cadenas binarias que no contengan a las subcadenas 00 y 01.\n" +
    "2. Cadenas binarias que no contengan a las subcadenas 00 y 11.\n" +
    "3. Cadenas ternarias que no contengan a la subcadena 00.\n" +
    "4. Cadenas cuaternarias que tengan sus caracteres en orden estrictamente creciente.\n"
    + "5. Cadenas ternarias que no tienen la subcadena 22.\n" +
    "6. Cadenas binarias que no contengan la subcadena 000.\n" +
    "7. Cadenas binarias que no contengan a la subcadena 000 ni a la subcadena 010.\n"
    + "8. Cadenas ternarias que no contengan a la subcadena 000.\n")

z = int(input(""))

if z == 1:
    n = int(input(" Dígite la longitud de la cadena\n"))
    #Código 2.1.1
    nums = ([
        "".join(x) for x in itertools.product("01", repeat=n)
        if "00" not in "".join(x) and "01" not in "".join(x)
    ])
    print(nums)
    print("Número total de cadenas: ", len(nums))
elif z == 2:
    n = int(input(" Dígite la longitud n\n"))
    #Código 2.1.2
    nums = ([
        "".join(x) for x in itertools.product("01", repeat=n)
        if "00" not in "".join(x) and "11" not in "".join(x)
    ])
    print(nums)
    print("Número total de cadenas: ", len(nums))

elif z == 3:
    n = int(input(" Dígite la longitud n\n"))
    #Código 2.1.3
    nums = ([
        "".join(x) for x in itertools.product("012", repeat=n)
        if "00" not in "".join(x)
    ])
    print(nums)
    print("Número total de cadenas: ", len(nums))
elif z == 4:
    n = int(input(" Dígite la longitud n\n"))
    #Código 2.1.4
    nums = ([
        "".join(x) for x in itertools.product("0123", repeat=n)
        if (n == 4 and x[0] < x[1] < x[2] < x[3] in "".join(x)) or (
            n == 3 and x[0] < x[1] < x[2] in "".join(x)) or (
                n == 2 and x[0] < x[1] in "".join(x)) or (
                    n == 1 and x[0] in "".join(x))
    ])
    print(nums)
    print("Número total de cadenas: ", len(nums))
elif z == 5:
    n = int(input(" Dígite la longitud n\n"))
    #Código 2.1.5
    nums = ([
        "".join(x) for x in itertools.product("012", repeat=n)
        if "22" not in "".join(x)
    ])
    print(nums)
    print("Número total de cadenas: ", len(nums))
elif z == 6:
    n = int(input(" Dígite la longitud n\n"))
    #Código 2.2.1
    nums = ([
        "".join(x) for x in itertools.product("01", repeat=n)
        if "000" not in "".join(x)
    ])
    print(nums)
    print("Número total de cadenas: ", len(nums))
elif z == 7:
    n = int(input(" Dígite la longitud n\n"))
    #Código 2.2.2
    nums = ([
        "".join(x) for x in itertools.product("010", repeat=n)
        if "000" not in "".join(x) and "010" not in "".join(x)
    ])
    print(nums)
    print("Número total de cadenas: ", len(nums))
elif z == 8:
    n = int(input(" Dígite la longitud n\n"))
    #Código 2.2.3
    nums = ([
        "".join(x) for x in itertools.product("012", repeat=n)
        if "000" not in "".join(x)
    ])
    print(nums)
    print("Número total de cadenas: ", len(nums))
