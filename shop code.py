#-----------def_menu------------
from pyfiglet import Figlet
f=Figlet(font="standard")
def show_menu():
    print("1-Add product")
    print("2-Edit product")
    print("3-Delete product")
    print("4-Search product")
    print("5-Show list")
    print("6-Buy")
    print("7-exit")


#---------------------------------------Add product---------------------------------------
def Addproduct ():
    while True:
        check=input("agar ghasd ezafe kardadn mahsol ra darid benevisid (y)  va agar na benevisid (n)   :")
        if check=="y":
            code=input("code mahsol ra vared konid    :")
            name=input("name mahsol ra vared konid    :")
            price=input("gheymat mahsol ra vared konid    :")
            count=input("tadade mahsol ra vared konid    :")
            deta=("\n", id, name, price, count)
            print("mahsol ezafe shod")
        else:
            break

#---------------------------------------------------------------Edit product----------------------------------------------------------------------
def Editproduct():
    while True:
        check=input("agar ghasd edit ra darid benevisid (y)  va agar na benevisid (n)    :")
        if check=="y":
            i=0
            for i in range(len(PRODUCT)):
                print(PRODUCT[i]["code"] , ["name"])
            edit=input("(name) ya (code) mahsol ra vared konid    :")
            i=0
            for i in range(len(PRODUCT)):
                if edit==PRODUCT[i]["name"] or PRODUCT[i]["code"]:
                    break
            edit=input("kodam gozine ra mikhahid edit konid benevisid ba gozashtan alamat (,) dar payan har gozine mesle  code,price   :")
            edit1=[]
            edit1=edit.split(",")

            if "code" in edit1:
                code=int(input("code mahsol ra vared konid    :"))
                PRODUCT[i]["code"]=code

            if "name" in edit1:
                PRODUCT[i]["name"]=name
                name=input("name mahsol ra vared konid    :")

            if "price" in edit1:
                price=int(input("gheymat mahsol ra vared konid    :"))
                PRODUCT[i]["price"]

            if "count" in edit1:
                count=int(input("gheymat mahsol ra vared konid    :"))
                PRODUCT[i]["count"]=count

            print("edit anjam shod")
        else:
            break

#-----------------------------------------Delete product------------------------------------------------
def Deleteproduct():
    while True:
        check=input("agar ghasd hazf ra darid benevisid (y)  va agar na benevisid (n)    :")
        if check=="y":
            i=0
            for i in range(len(PRODUCT)):
                print(PRODUCT[i]["code"] , ["name"])
            delet=input("(name) ya (code) mahsol ra vared konid    :")
            i=0
            for i in range(len(PRODUCT)):
                if delet==PRODUCT[i]["name"] or PRODUCT[i]["code"]:
                    break
            del PRODUCT[i]
            print("mahsol pak shod")
        else:
            break

#---------------------------------------------------Search product-------------------------------------------------------
def Searchproduct():
        while True:
            check=input("agar ghasd jost va jo mahsol ra darid benevisid (y)  va agar na benevisid (n)    :") 
            if check=="y":
                search=input("(name) ya (code) mahsol ra vared konid    :")
                i=0
                for i in range(len(PRODUCT)):
                    if search==PRODUCT[i]["name"] or PRODUCT[i]["code"]:
                        break
                print(PRODUCT[i])
            else:
                break

#--------------------------------------------------Show list---------------------------------------------------------------
def Showlist():
    check=input("agar ghasd tamasha list ra darid benevisid (y)  va agar na benevisid (n)    :")
    if check=="y":
        print("code", " -", "name", " -","pric", " -","count")
        for i in range(len(PRODUCT)):
            print(PRODUCT[i]["code"]," -",PRODUCT[i]["name"]," -",PRODUCT[i]["price"]," -",PRODUCT[i]["count"])
        


#------------------------------------------------Buy----------------------------------------------------
def Buy():
    while True:
        check=input("agar ghasd kharid ra darid benevisid (y)  va agar na benevisid (n)    :")
        if check=="y":
            for i in range(len(PRODUCT)):
                print(PRODUCT[i]["code"]," , ",PRODUCT[i]["name"]) 
            i=0
            buy=input("(name) ya (code) mahsol ra vared konid    :")
            for i in range(len(PRODUCT)):
                if buy==PRODUCT[i]["name"] or PRODUCT[i]["code"]:
                    break
            while True:
                count1=PRODUCT[i]["count"]
                count=int(input("tedadi ke mikhahid az in mahsil bekharid    :"))
                if int(count1)>=count:
                    PRODUCT[i]["count"]=int(count1)-count
                    print("kharidari shod")
                    break
                else:
                    print("mojodi dar anbar kafi nist")
        else:
            break

#----------------------------run--------------------------------
while True:
    #------------array_dictionuary-------------
    myfile=open("shop deta.txt","r")
    data=myfile.read()
    PRODUCT=[]
    product_list=data.split("\n")
    for i in range(len(product_list)):
        product_info=product_list[i].split(",")
        mydict={}
        mydict["code"]=product_info[0]
        mydict["name"]=product_info[1]
        mydict["price"]=product_info[2]
        mydict["count"]=product_info[3]
        PRODUCT.append(mydict)

    #-----------------menu-------------------
    print(f.renderText("Behdad Store"))
    show_menu()
    user=int(input("please chosse a number:    "))

    #---------if----------
    if user==1:
        Addproduct()
    elif user==2:
        Editproduct()
    elif user==3:
        Deleteproduct()
    elif user==4:
        Searchproduct()
    elif user==5:
        Showlist()
    elif user==6:
        Buy()
    elif user==7:
        break
