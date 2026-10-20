from pyscript import display, document

def add_brand(e):
    document.getElementById('output1').innerHTML = ""

    Grade7 = {"Verity Salangas", "Kalimba Salinga"}
    Grade8 = {"Suning tuming", "Arada Sarada"}
    Grade9 = {"Jimmy Saludes", "Ai Ai",  "John Chessmaster123"}
    Grade10 = {"Alexander Floro", "Kurt Abellar", "Jeremiah Velasco"}

    input_brand = document.getElementById('input1').value
    input_brand2 = document.getElementById('input2').value
    Full = (f'{input_brand} {input_brand2}')

    new_brand_set = {Full}

    All_brands = Grade9 | new_brand_set | Grade7 | Grade8 | Grade7 | Grade10

    total_brands =len(Grade9 | new_brand_set | Grade7 | Grade8 | Grade7 | Grade10)

    brand_list = "<br>".join(sorted(All_brands))

    document.getElementById('output1').innerHTML = (f"All Kalimbayan: <br>{brand_list}")
    display(f'total Kalimbayan: {total_brands}', target= "output1" )


'''References
https://www.w3schools.com/css/css_align.asp -- fo aligning the buttons and inputs

'''