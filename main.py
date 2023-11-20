from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
import random
from tkinter import messagebox
import tempfile
import os
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Grocery Management Software")

        #==================variables=====================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        

        
        #product  categories list
        self.category=["Select Option","Beverages","Bathing","DairyProduct","Snacks","Kitchen","PlantProduct"]
        #Beverages
        self.SubCatBeverages=["Cold Drink","Juice","Coffee","Energy Drink"]
        self.ColdDrink=["Pepsi","MountainDew","Sprite","CocaCola","ThumbsUp","7up","Frooti","Limca"]
        self.price_Pepsi=85
        self.price_MountainDew=85
        self.price_Sprite=90
        self.price_CocaCola=90
        self.price_ThumbsUp=90
        self.price_7up=85
        self.price_Frooti=85
        self.price_Limca=90
        

        self.Juice=["Tropicana","Real","Raw","MinuteMaid","AloFruit"]
        self.price_Tropicana=90
        self.price_Real=87
        self.price_Raw=82
        self.price_MinuteMaid=90
        self.price_AloFruit=85

        self.Coffee=["BruGold","Nascafe"]
        self.price_BruGold=300
        self.price_Nascafe=350

        
        self.EnergyDrink=["RedBull","Monster","Strings","Prime"]
        self.price_RedBull=110
        self.price_Monster=130
        self.price_String=20
        self.price_Prime=300
        

        #Bathing
        self.SubCatBathing=["Soap","Shampoo","ToothPaste","FaceWash","HandWash"]
        self.Soap=["LifeBouy","Dettol","Dove","Cinthol","Lux"]
        self.price_LifeBouy=42
        self.price_Dettol=47
        self.price_Dove=49
        self.price_Cinthol=45
        self.price_Lux=40

        self.Shampoo=["Dove","Tresame","Loreal","ClinicPlus"]
        self.price_Dove=230
        self.price_Tresame=250
        self.price_Loreal=300
        self.price_ClinicPlus=200

        self.ToothPaste=["Colgate","Pepsodent"]
        self.price_Colgate=190
        self.price_Pepsodent=180

        self.FaceWash=["GarnierMens","NeviaMen","Himalaya","CleanCare"]
        self.price_Garnier_Mens=220
        self.price_NeviaMen=190
        self.price_Himalaya=150
        self.price_CleanCare=110

        self.HandWash=["Dettol_hw","Savlon","Lifeboy"]
        self.price_Dettol_hw=100
        self.price_Savlon=90
        self.price_Lifeboy=87


        #DairyProduct
        self.SubCatDairyProduct=["Milk","Chocolate","Paneer","Butter","Bread"]
        self.Milk=["Fullcream","TonedMilk","CowMilk"]
        self.price_Fullcream=58
        self.price_TonedMilk=46
        self.price_CowMilk=50

        self.Paneer=["Fresh"]
        self.price_Fresh=630
 
        self.Butter=["Amul","MotherDiary"]
        self.price_Amul=92
        self.price_MotherDiary=100

        self.Bread=["EnglishOven","Harvest","BrownBread"]
        self.price_EnglishOven=45
        self.price_Harvest=42
        self.price_BrownBread=52
        
        #snacks
        self.SubCatSnacks=["Chips","Biscuits","Namkeen"]
        self.Chips=["Lays","Kurkure","Bingo","Doritos"]
        self.price_Lays=20
        self.price_Kurkure=20
        self.price_Bingo=20
        self.price_Doritos=35
        
        self.Biscuits=["Goodday","Hideseek","MarieGold","ParleG"]
        self.price_Goodday=20
        self.price_Hideseek=30
        self.price_MarieGold=15
        self.price_ParleG=10

        self.Namkeen=["AlooBhujia","Mixed","KhataMeetha","Punjabi"]
        self.price_AlooBhujia=50
        self.price_Mixed=60
        self.price_KhataMeetha=55
        self.price_Punjabi=60

        #kitchen
        self.SubCatKitchen=["Fooditem","Masala"]
        self.Fooditem=["Atta","Rice","Oil"]
        self.price_Atta=12
        self.price_Rice=32
        self.price_Oil=120

        self.Masala=["Redchilli","Pepper","Haldi","Salt","Sugar"]
        self.price_Redchilli=39
        self.price_Pepper=50
        self.price_Haldi=34
        self.price_Salt=25
        self.price_Sugar=40


        #PlantProduct
        self.SubCatPlantProduct=["Fruits","Vegetables"]
        self.Fruits=["Mango","Guava","Banana","Strawberry","Apple","Orange","Coconut"]
        self.price_Mango=80
        self.price_Guava=50
        self.price_Banana=40
        self.price_Strawberry=80
        self.price_Apple=120
        self.price_Orange=70
        self.price_Coconut=60
        

        self.Vegetables=["Patato","Tamato","Onion","Pea","Brinjal","Greenchilli","Lemon"]
        self.price_Patato=40
        self.price_Tamato=90
        self.price_Onion=60
        self.price_Pea=80
        self.price_Brinjal=20
        self.price_Greenchilli=70
        self.price_Lemon=80

        lbl_title=Label(self.root,text="GROCERY MANAGEMENT SOFTWARE",font=("times new roman",35,"bold"),bg="black",fg="red")
        lbl_title.place(x=0,y=100,width=1530,height=45)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(lbl_title,font=('times new roman',16,'bold'),background='black',foreground='blue')
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=150,width=1530,height=620)

        #customer labelframe
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",12,"bold"),width=21)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,text="Customer Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)


        self.lblEmail=Label(Cust_Frame,text="Email",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #product labelframe
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)

        #categories
        self.lblCategory=Label(Product_Frame,text="Select Categories",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,values=self.category,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories_add)


        #subcategories
        self.lblSubCategory=Label(Product_Frame,text="Sub Categories",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        

        self.Combo_SubCategory=ttk.Combobox(Product_Frame,values=[""],font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_SubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #product name
        self.lblproduct=Label(Product_Frame,text="Product Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.Combo_product=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_product.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.Combo_product.bind("<<ComboboxSelected>>",self.price)
        

        #price
        self.lblPrice=Label(Product_Frame,text="Price",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.Combo_Price=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Price.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #qty
        self.lblQty=Label(Product_Frame,text="Qty",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=10)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        
        #Middle frame image frame

        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)

        #image1
        img12=Image.open("image1.jpg")
        img12=img12.resize((490,340))
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=490,height=340)

        #image 2
        img13=Image.open("image2.jpeg")
        img13=img13.resize((490,340))
        self.photoimg13=ImageTk.PhotoImage(img13)

        lbl_img13=Label(MiddleFrame,image=self.photoimg13)
        lbl_img13.place(x=490,y=0,width=500,height=340)


        #search bar bill number
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=15,width=500,height=40)

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("arial",12,"bold"),bg="red",fg="white",bd=4)
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)
        self.txt_Entry_search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",height=1,font=("arial",10,"bold"),bg="orangered",fg="white",width=10,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)


        #rightframe Bill area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        #Bill Counter LabelFrame
        Button_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Button_Frame.place(x=0,y=485,width=1520,height=125)

        self.lblSubTotal=Label(Button_Frame,text="Sub Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Button_Frame,textvariable=self.sub_total,font=("arial",10,"bold"),width=26)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lblTax=Label(Button_Frame,text="Gov Tax",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblTax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_Tax=ttk.Entry(Button_Frame,textvariable=self.tax_input,font=("arial",10,"bold"),width=26)
        self.txt_Tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblAmountTotal=Label(Button_Frame,text="Amount Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Button_Frame,textvariable=self.total,font=("arial",10,"bold"),width=26)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)



       #button Frame
        Btn_Frame=Frame(Button_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,text="Add To Cart",height=2,font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate=Button(Btn_Frame,text="Genrate Bill",command=self.generatebill,height=2,font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btngenerate.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,text="Save Bill",height=2,font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,text="Print Bill",height=2,font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,text="Clear",height=2,font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,text="Exit",height=2,font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()
        self.l=[]
#======================================function ========================

    def AddItem(self):
        Tax=5
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%((((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100))))))
# bill print area
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\tWelcome to A-2-Z Mini Mall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Customer Phone No:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n==================================================")
        self.textarea.insert(END,f"\n PRODUCTS\t\t\tQTY\t\tPRICE")
        self.textarea.insert(END,"\n==================================================\n")
       
#==============genertate bill=====================
    def generatebill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n =============================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:{self.total.get()}")
            self.textarea.insert(END,"\n =============================================")


#  =========================save bill=================================
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if(op>0):
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('Bills/'+str(self.bill_no.get())+".txt",'w')
            op=messagebox.showinfo("Saved",f"Bill No: {self.bill_no.get()} Saved Sucessfully")
            f1.close()

#=================================print bill================================
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


#=====================================find bill column===========================
    def find_bill(self):
        found="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'Bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No")

#===================================clear button===================================
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        z=random.randint(1000,9999)
        self.bill_no.set(str(z))
        self.c_email.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()
        



#addition of categoey sub category etc
    def Categories_add(self,event=""):
        if self.Combo_Category.get()=="Beverages":
            self.Combo_SubCategory.config(value=self.SubCatBeverages)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="Bathing":
            self.Combo_SubCategory.config(value=self.SubCatBathing)
            self.Combo_SubCategory.current(0)
        
        if self.Combo_Category.get()=="DiaryProduct":
            self.Combo_SubCategory.config(value=self.SubCatDiaryProduct)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="Snacks":
            self.Combo_SubCategory.config(value=self.SubCatSnacks)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="Kitchen":
            self.Combo_SubCategory.config(value=self.SubCatKitchen)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="PlantProduct":
            self.Combo_SubCategory.config(value=self.SubCatPlantProduct)
            self.Combo_SubCategory.current(0)
        

        

       
    def Product_add(self,event=""):
        if self.Combo_SubCategory.get()=="Cold Drink":
            self.Combo_product.config(value=self.ColdDrink)
            self.Combo_product.current(0)
        
        if self.Combo_SubCategory.get()=="Juice":
            self.Combo_product.config(value=self.Juice)
            self.Combo_product.current(0)


        if self.Combo_SubCategory.get()=="Coffee":
            self.Combo_product.config(value=self.Coffee)
            self.Combo_product.current(0)

        if self.Combo_SubCategory.get()=="Energy Drink":
            self.Combo_product.config(value=self.EnergyDrink)
            self.Combo_product.current(0)
        
        if self.Combo_SubCategory.get()=="Soap":
            self.Combo_product.config(value=self.Soap)
            self.Combo_product.current(0)
        
        if self.Combo_SubCategory.get()=="Shampoo":
            self.Combo_product.config(value=self.Shampoo)
            self.Combo_product.current(0)
        if self.Combo_SubCategory.get()=="ToothPaste":
            self.Combo_product.config(value=self.ToothPaste)
            self.Combo_product.current(0)
        if self.Combo_SubCategory.get()=="FaceWash":
            self.Combo_product.config(value=self.FaceWash)
            self.Combo_product.current(0)
        if self.Combo_SubCategory.get()=="HandWash":
            self.Combo_product.config(value=self.HandWash)
            self.Combo_product.current(0)
        if self.Combo_SubCategory.get()=="Milk":
            self.Combo_product.config(value=self.Milk)
            self.Combo_product.current(0)
        if self.Combo_SubCategory.get()=="Paneer":
            self.Combo_product.config(value=self.Paneer)
            self.Combo_product.current(0)
        if self.Combo_SubCategory.get()=="Butter":
            self.Combo_product.config(value=self.Butter)
            self.Combo_product.current(0)
        if self.Combo_SubCategory.get()=="Bread":
            self.Combo_product.config(value=self.Bread)
            self.Combo_product.current(0)
        
        if self.Combo_SubCategory.get()=="Chips":
            self.Combo_product.config(value=self.Chips)
            self.Combo_product.current(0)
        if self.Combo_SubCategory.get()=="Biscuits":
            self.Combo_product.config(value=self.Biscuits)
            self.Combo_product.current(0)
        if self.Combo_SubCategory.get()=="Namkeen":
            self.Combo_product.config(value=self.Namkeen)
            self.Combo_product.current(0)
        if self.Combo_SubCategory.get()=="Fooditem":
            self.Combo_product.config(value=self.Fooditem)
            self.Combo_product.current(0)
        
        if self.Combo_SubCategory.get()=="Masala":
            self.Combo_product.config(value=self.Masala)
            self.Combo_product.current(0)
        if self.Combo_SubCategory.get()=="Fruits":
            self.Combo_product.config(value=self.Fruits)
            self.Combo_product.current(0)
        if self.Combo_SubCategory.get()=="Vegetables":
            self.Combo_product.config(value=self.Vegetables)
            self.Combo_product.current(0)
        
        
        
        
        
            




        
        
#======================================================================
  
#------------------------set price---------------------------
    def price(self,event=""):
        if self.Combo_product.get()=="MountainDew":
            self.Combo_Price.config(value=self.price_MountainDew)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
    
        if self.Combo_product.get()=="Pepsi":
            self.Combo_Price.config(value=self.price_Pepsi)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
    
        if self.Combo_product.get()=="Sprite":
            self.Combo_Price.config(value=self.price_Sprite)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
    
        if self.Combo_product.get()=="CocaCola":
            self.Combo_Price.config(value=self.price_CocaCola)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
    
        if self.Combo_product.get()=="Limca":
            self.Combo_Price.config(value=self.price_Limca)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
    
        if self.Combo_product.get()=="ThumbsUp":
            self.Combo_Price.config(value=self.price_ThumbsUp)
            self.Combo_Price.current(0)
            self.qty.set(1)

    
        if self.Combo_product.get()=="7up":
            self.Combo_Price.config(value=self.price_7up)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
    
        if self.Combo_product.get()=="Frooti":
            self.Combo_Price.config(value=self.price_Frooti)
            self.Combo_Price.current(0)
            self.qty.set(1)

    
        if self.Combo_product.get()=="Tropicana":
            self.Combo_Price.config(value=self.price_Tropicana)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="Real":
            self.Combo_Price.config(value=self.price_Real)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="MinuteMaid":
            self.Combo_Price.config(value=self.price_MinuteMaid)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="AloFruit":
            self.Combo_Price.config(value=self.price_AloFruit)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="Raw":
            self.Combo_Price.config(value=self.price_Raw)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="BruGold":
            self.Combo_Price.config(value=self.price_BruGold)
            self.Combo_Price.current(0)
            self.qty.set(1)

    
        if self.Combo_product.get()=="Nascafe":
            self.Combo_Price.config(value=self.price_Nascafe)
            self.Combo_Price.current(0)
            self.qty.set(1)

    
        if self.Combo_product.get()=="RedBull":
            self.Combo_Price.config(value=self.price_RedBull)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="Monster":
            self.Combo_Price.config(value=self.price_Monster)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="String":
            self.Combo_Price.config(value=self.price_String)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="Prime":
            self.Combo_Price.config(value=self.price_Prime)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="LifeBouy":
            self.Combo_Price.config(value=self.price_LifeBouy)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="Dettol":
            self.Combo_Price.config(value=self.price_Dettol)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="Dove":
            self.Combo_Price.config(value=self.price_Dove)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="Cinthol":
            self.Combo_Price.config(value=self.price_Cinthol)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        if self.Combo_product.get()=="Lux":
            self.Combo_Price.config(value=self.price_Lux)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_product.get()=="DoveSh":
            self.Combo_Price.config(value=self.price_DoveSh)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Tresame":
            self.Combo_Price.config(value=self.price_Tresame)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_product.get()=="Loreal":
            self.Combo_Price.config(value=self.price_Loreal)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="ClinicPlus":
            self.Combo_Price.config(value=self.price_ClinicPlus)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Colgate":
            self.Combo_Price.config(value=self.price_Colgate)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Pepsodent":
            self.Combo_Price.config(value=self.price_Pepsodent)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="GarnierMens":
            self.Combo_Price.config(value=self.price_GarnierMens)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="NeviaMen":
            self.Combo_Price.config(value=self.price_NeviaMen)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Himalaya":
            self.Combo_Price.config(value=self.price_Himalaya)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="CleanCare":
            self.Combo_Price.config(value=self.price_CleanCare)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_product.get()=="Dettol_hw":
            self.Combo_Price.config(value=self.price_Dettol_hw)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Savlon":
            self.Combo_Price.config(value=self.price_Savlon)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Lifeboy":
            self.Combo_Price.config(value=self.price_Lifeboy)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_product.get()=="Fullcream":
            self.Combo_Price.config(value=self.price_Fullcream)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="TonedMilk":
            self.Combo_Price.config(value=self.price_TonedMilk)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Fresh":
            self.Combo_Price.config(value=self.price_Fresh)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Fresh":
            self.Combo_Price.config(value=self.price_Fresh)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Amul":
            self.Combo_Price.config(value=self.price_Amul)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="MotherDiary":
            self.Combo_Price.config(value=self.price_MotherDiary)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="EnglishOven":
            self.Combo_Price.config(value=self.price_EnglishOven)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Harvest":
            self.Combo_Price.config(value=self.price_Harvest)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="BrownBread":
            self.Combo_Price.config(value=self.price_BrownBread)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Lays":
            self.Combo_Price.config(value=self.price_Lays)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Kurkure":
            self.Combo_Price.config(value=self.price_Kurkure)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Bingo":
            self.Combo_Price.config(value=self.price_Bingo)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Doritos":
            self.Combo_Price.config(value=self.price_Doritos)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Goodday":
            self.Combo_Price.config(value=self.price_Goodday)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Hideseek":
            self.Combo_Price.config(value=self.price_Hideseek)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="MarieGold":
            self.Combo_Price.config(value=self.price_MarieGold)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="ParleG":
            self.Combo_Price.config(value=self.price_ParleG)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Punjabi":
            self.Combo_Price.config(value=self.price_Punjabi)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Mixed":
            self.Combo_Price.config(value=self.price_Mixed)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="AlooBhujia":
            self.Combo_Price.config(value=self.price_AlooBhujia)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="KhataMeetha":
            self.Combo_Price.config(value=self.price_KhataMeetha)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_product.get()=="Atta":
            self.Combo_Price.config(value=self.price_Atta)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Rice":
            self.Combo_Price.config(value=self.price_Rice)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Oil":
            self.Combo_Price.config(value=self.price_Oil)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Redchilli":
            self.Combo_Price.config(value=self.price_Redchilli)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Pepper":
            self.Combo_Price.config(value=self.price_Pepper)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Haldi":
            self.Combo_Price.config(value=self.price_Haldi)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Salt":
            self.Combo_Price.config(value=self.price_Salt)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_product.get()=="Sugar":
            self.Combo_Price.config(value=self.price_Sugar)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Mango":
            self.Combo_Price.config(value=self.price_Mango)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Guava":
            self.Combo_Price.config(value=self.price_Guava)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Strawberry":
            self.Combo_Price.config(value=self.price_Strawberry)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Banana":
            self.Combo_Price.config(value=self.price_Banana)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Apple":
            self.Combo_Price.config(value=self.price_Apple)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Orange":
            self.Combo_Price.config(value=self.price_Orange)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Coconut":
            self.Combo_Price.config(value=self.price_Coconut)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Patato":
            self.Combo_Price.config(value=self.price_Patato)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Tamato":
            self.Combo_Price.config(value=self.price_Tamato)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Onion":
            self.Combo_Price.config(value=self.price_Onion)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Pea":
            self.Combo_Price.config(value=self.price_Pea)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Brinjal":
            self.Combo_Price.config(value=self.price_)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Greenchilli":
            self.Combo_Price.config(value=self.price_Greenchilli)
            self.Combo_Price.current(0)
            self.qty.set(1)
        if self.Combo_product.get()=="Lemon":
            self.Combo_Price.config(value=self.price_Lemon)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        
        
       
#============================================================================================================


      






if __name__== '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()