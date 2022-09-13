from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import (SellerRegisterForm, UserRegisterForm, SellerLoginForm, PhoneRegisterForm, 
                    RegisterEccoInfoUserForm, AddDressForm, AddEquipmentForm, AddMachinForm, OpenTicket, ReplyTicketForm,
                    SelectCategory)
from .models import (CategoryGender, CategoryTypes, CategoryWear, Dress, EccoInformation, Equipment, Machines,
                    FinalCategory, Nature, Color, Tag, Ticket, TickComment)
from .utils import Send_sms
from django.contrib.auth import authenticate, login, logout
from django.views import View
import random
import logging
from azbankintro import iban_validate, IBANValidationException

class SellerRegisterView(View):
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('seller:login')
    #     return super().dispatch(request, *args, **kwargs)
        
    def get(self,request, *args, **kwargs):
        user_form = UserRegisterForm()
        seller_form = SellerRegisterForm()
        return render(request, 'seller/register.html', {'user_form': user_form, 'seller_form':seller_form})

    def post(self,request,*args, **kwargs):
        user_form = UserRegisterForm(request.POST)
        seller_form = SellerRegisterForm(request.POST)
        if user_form.is_valid() and seller_form.is_valid():
            custom_user = user_form.save()
            seller = seller_form.save(commit=False)
            seller.user = custom_user
            seller.save()
            messages.success(request,'ثبت نام با موفقیت انجام شد')
            return redirect('seller:register_ecco')
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'seller/register.html', {'user_form': user_form, 'seller_form': seller_form})



class SellerLoginView(View):
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('seller:login')
    #     return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        form = SellerLoginForm()
        return render(request,'seller/login.html', {'form':form})

    def post(self,request,*args, **kwargs):
        form = SellerLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('phone_number')
            password=form.cleaned_data.get('password')
            user = authenticate(
            username=username,
            password=password
            )
            if user is not None:
                messages.success(request, 'ورود شما با موفقیت انجام شد')
                login(request,user)
                next_url=request.GET.get('next')
                if next_url is not None:
                    return redirect(next_url)
                else:
                    return redirect('seller:dashboard')
            else:
                messages.warning(request,'کاربر با این مشخصات یافت نشد')
                return render(request, 'seller/login.html', {'form':form})
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'seller/login.html', {'form':form})



class SellerLogoutView(View):    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('seller:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        logout(request)
        messages.warning(request, 'خروج شما با موفقیت انجام شد')
        return redirect('seller:login')


class SellerProfileView(View):
    def get(self,request,*args, **kwargs):
        return render(request, 'seller/profile.html',{'form':'form'})

    def post(self,request,*args, **kwargs):
        return redirect('seller:login')

class SellerDashboardView(View):
    def get(self,request,*args, **kwargs):
        return render(request, 'seller/dashboard.html',{'form':'form'})

    def post(self,request,*args, **kwargs):
        pass


#====================================================================================
# def codeGenerate():
#     return random.randint(1000,9999)
from django_otp.oath import totp

secret_key = b'12345678901234567890'
code = totp(key=secret_key, step=30, digits=4)

def phone_register(request):
    form = PhoneRegisterForm()
    if request.method == 'POST':
        form = PhoneRegisterForm(request.POST)
        print('code',type(code))
        if form.is_valid():
            register_phone = form.cleaned_data['phone_number']
            Send_sms(register_phone,code)
        print(register_phone, ": " ,code)
        return redirect('seller:phone_verify')
    return render(request, 'seller/phone_register.html', {'form':form})



def phone_verify(request):
    print("code", code)
    # if request.method =='POST':
    verify_code = request.GET.get('phone_verify')
    if verify_code == str(code):
        print(verify_code, "You send to the next page")
        return redirect('seller:register')
    return render(request, 'seller/phone_verify.html',{'code':code})


#===================================================================================

#-----------------------------RegisterEccoInfoSeller-------------------------
class RegisterEccoInfoUserView(View):
    
    def get(self,request, *args, **kwargs):
        form = RegisterEccoInfoUserForm()
        return render(request, 'seller/register_ecco.html', {'form': form})
    
    def post(self,request,*args, **kwargs):
        form = RegisterEccoInfoUserForm()
        if request.method == 'POST':
            form = RegisterEccoInfoUserForm(request.POST, request.FILES)
            if form.is_valid():
                brand_name = form.cleaned_data.get("brand_name")
                owner = form.cleaned_data.get("owner")
                category = form.cleaned_data.get("category")
                sheba_number = form.cleaned_data.get("sheba_number")
                try:
                    valid_sheba = iban_validate(sheba_number)
                    logging.debug('IBAN is valid')
                except IBANValidationException:
                    logging.debug('IBAN is not valid')
                description = form.cleaned_data.get("description")
                lawful_candid_name = form.cleaned_data.get("lawful_candid_name")
                lawful_candid_nationalcode = form.cleaned_data.get("lawful_candid_nationalcode")
                lawful_candid_phone = form.cleaned_data.get("lawful_candid_phone")
                lawful_candid_image = form.cleaned_data.get("lawful_candid_image")
                certificate_image = form.cleaned_data.get("certificate_image")
                logo_image = form.cleaned_data.get("logo_image")
                obj = EccoInformation.objects.create(
                    brand_name = brand_name,
                    owner = owner,
                    category = category,
                    sheba_number = valid_sheba,
                    description = description,
                    lawful_candid_name = lawful_candid_name,
                    lawful_candid_nationalcode = lawful_candid_nationalcode,
                    lawful_candid_phone = lawful_candid_phone,
                    lawful_candid_image = lawful_candid_image,
                    certificate_image = certificate_image,
                    logo_image = logo_image,
                )
                obj.save()
                messages.success(request,'ثبت نام با موفقیت انجام شد.')
                return redirect('seller:profile')
            else:
                messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
                return render(request, 'seller/add_production.html', {'form': form})
        else:
            form = RegisterEccoInfoUserForm()  
            
#----------------------------------------------------------------GenderCategory------------------------------------------------------------

class CategoryGenderView(View):
    def get(self, request, *args, **kwargs):
        genders = CategoryGender.objects.all()
        context = {
            'genders' : genders,
        }
        print(context)
        #context_object_name = 'genders'
        return render(request, 'seller/add_production.html', context)
    
#------------------------------------------------------------SelectCategoryProduction--------------------------------------------------------

class SelectCategoryView(View):
    def get(self, request, *args, **kwargs):
        form = SelectCategory()
        context = {
            'form': form,
        }
        return render(request, 'seller/select_category.html', context)
    def post(self, request, *args, **kwargs):
        form = SelectCategory()
        if request.method == 'POST':
            form = SelectCategory(request.POST)
            if form.is_valid():
                first_category = form.cleaned_data.get("first_category")
                user = request.user
                obj = Dress.objects.create(
                    first_category = first_category,
                    user = user
                )
                obj.save()
                if first_category == 'البسه و پوشاک':
                    return redirect('seller:add_dress')
                elif first_category == 'تجهیزات دوخت':
                    return redirect('seller:add_equipment')
                else:
                    return redirect('seller:add_machins')
            return render(request, 'seller/select_category.html', {'form':form})
        form = SelectCategory()
        
            
#----------------------------------------------------------------AddProduction----------------------------------------------------------------

class AddDressView(View):
    
    def get(self,request, *args, **kwargs):
        #production_form = AddProductionForm()
        dress_form = AddDressForm()
        context = {
            #'production_form' : production_form,
            'dress_form': dress_form,
        
        }
        return render(request, 'seller/add_dress.html', context)
    
    def post(self,request,*args, **kwargs):
        #production_form = AddProductionForm()
        dress_form = AddDressForm()
        if request.method == 'POST':
            #production_form = AddProductionForm(request.POST, request.FILES or None)
            dress_form = AddDressForm(request.POST)
            if dress_form.is_valid():
                user = request.user
                genders = dress_form.cleaned_data.get("genders")
                wears = dress_form.cleaned_data.get("wears")
                types = dress_form.cleaned_data.get("types")
                size = dress_form.cleaned_data.get("size")
                numbers = dress_form.cleaned_data.get("numbers")
                nature = dress_form.cleaned_data.get("nature")
                colors = dress_form.cleaned_data.get("colors")
                sleeve = dress_form.cleaned_data.get("sleeve")
                close_way = dress_form.cleaned_data.get("close_way")
                colors_num = dress_form.cleaned_data.get("colors_num")
                crotch = dress_form.cleaned_data.get("crotch")
                sale_way = dress_form.cleaned_data.get("sale_way")
                warranty = dress_form.cleaned_data.get("warranty")
                pocket = dress_form.cleaned_data.get("pocket")
                hat = dress_form.cleaned_data.get("hat")
                washing_point = dress_form.cleaned_data.get("washing_point")
                style = dress_form.cleaned_data.get("style")
                design = dress_form.cleaned_data.get("design")
                spatial_feature = dress_form.cleaned_data.get("spatial_feature")
                collar = dress_form.cleaned_data.get("collar")
                name = dress_form.cleaned_data.get("name")
                first_category = dress_form.cleaned_data.get("first_category")  
                price = dress_form.cleaned_data.get("price")
                tags = dress_form.cleaned_data.get("tags")
                description = dress_form.cleaned_data.get("description")
                image = dress_form.cleaned_data.get("image")
                videofile = dress_form.cleaned_data.get("videofile")
                dress_obj = Dress.objects.create(
                    genders = genders,
                    wears = wears,
                    types = types,
                    size = size,
                    numbers = numbers,
                    nature = nature,
                    # colors = colors,
                    sleeve = sleeve,
                    close_way = close_way,
                    colors_num = colors_num,
                    crotch = crotch,
                    sale_way = sale_way,
                    warranty = warranty,
                    pocket = pocket,
                    hat = hat,
                    washing_point = washing_point,
                    style = style,
                    design = design,
                    spatial_feature = spatial_feature,
                    collar = collar,
                    name = name,
                    user = user,
                    first_category = first_category,  
                    price = price,
                    # tags = tags,
                    description = description,
                    image = image,
                    videofile = videofile
                )
                dress_obj.save()
                dress_obj.colors.add(*colors)
                
                # pro_obj = Production.objects.create(
                #     name = name,
                #     user = user,
                #     first_category = first_category,  
                #     price = price,
                #     # tags = tags,
                #     description = description,
                #     image = image,
                #     videofile = videofile
                # )
                
                # pro_obj.save()
                dress_obj.tags.add(*tags)
                
                messages.success(request,'کالا با موفقیت اضافه گردید.')
                return redirect('seller:list_production')
            else:
                messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
                return render(request, 'seller/add_dress.html', {'dress_form': dress_form})
        else:
            form = AddDressForm()  

#----------------------------------------------------------AddEquipmentView----------------------------------------------------------------
class AddEquipmentView(View):
    
    def get(self,request, *args, **kwargs):
        equipment_form = AddEquipmentForm()
        context = {
            'equipment_form': equipment_form,
        }
        return render(request, 'seller/add_equ.html', context)
    
    def post(self,request,*args, **kwargs):
        equipment_form = AddEquipmentForm()
        if request.method == 'POST':
            equipment_form = AddEquipmentForm(request.POST)
            if equipment_form.is_valid():
                user = request.user
                weidth = equipment_form.cleaned_data.get("weidth")
                height = equipment_form.cleaned_data.get("height")
                weight = equipment_form.cleaned_data.get("weight")
                using = equipment_form.cleaned_data.get("using")
                nature = equipment_form.cleaned_data.get("nature")
                colors = equipment_form.cleaned_data.get("colors")
                colors_num = equipment_form.cleaned_data.get("colors_num")
                sale_way = equipment_form.cleaned_data.get("sale_way")
                warranty = equipment_form.cleaned_data.get("warranty")
                washing_point = equipment_form.cleaned_data.get("washing_point")
                design = equipment_form.cleaned_data.get("design")
                tissue_density = equipment_form.cleaned_data.get("tissue_density")
                name = equipment_form.cleaned_data.get("name")
                first_category = equipment_form.cleaned_data.get("first_category")  
                price = equipment_form.cleaned_data.get("price")
                tags = equipment_form.cleaned_data.get("tags")
                description = equipment_form.cleaned_data.get("description")
                image = equipment_form.cleaned_data.get("image")
                videofile = equipment_form.cleaned_data.get("videofile")
                equ_obj = Equipment.objects.create(
                    weidth = weidth,
                    height = height,
                    weight = weight,
                    using = using,
                    nature = nature,
                    colors_num = colors_num,
                    sale_way = sale_way,
                    warranty = warranty,
                    tissue_density = tissue_density,
                    name = name,
                    user = user,
                    first_category = first_category,  
                    price = price,
                    description = description,
                    image = image,
                    videofile = videofile
                )
                equ_obj.save()
                equ_obj.colors.add(*colors)
                equ_obj.tags.add(*tags)
                
                messages.success(request,'کالا با موفقیت اضافه گردید.')
                return redirect('seller:list_production')
            else:
                messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
                return render(request, 'seller/add_equ.html', {'equipment_form': equipment_form})
        else:
            form = AddEquipmentForm()  
            
#--------------------------------------------------------------AddMachinView--------------------------------------------------------------

class AddMachinView(View):
    
    def get(self,request, *args, **kwargs):
        machin_form = AddMachinForm()
        context = {
            'machin_form': machin_form,
        }
        return render(request, 'seller/add_equ.html', context)
    
    def post(self,request,*args, **kwargs):
        machin_form = AddMachinForm()
        if request.method == 'POST':
            machin_form = AddMachinForm(request.POST)
            if machin_form.is_valid():
                user = request.user
                cylinder_bed = machin_form.cleaned_data.get("cylinder_bed")
                flat_bed = machin_form.cleaned_data.get("flat_bed")
                ghab_mako = machin_form.cleaned_data.get("ghab_mako")
                ghabeliat_dokht = machin_form.cleaned_data.get("ghabeliat_dokht")
                mako = machin_form.cleaned_data.get("mako")
                masore = machin_form.cleaned_data.get("masore")
                masore_por = machin_form.cleaned_data.get("masore_por")
                sale_way = machin_form.cleaned_data.get("sale_way")
                warranty = machin_form.cleaned_data.get("warranty")
                nakh = machin_form.cleaned_data.get("nakh")
                pedal = machin_form.cleaned_data.get("pedal")
                sozan_nakhkon = machin_form.cleaned_data.get("sozan_nakhkon")
                tavan = machin_form.cleaned_data.get("tavan")
                machin_weight = machin_form.cleaned_data.get("machin_weight")
                type = machin_form.cleaned_data.get("type")
                name = machin_form.cleaned_data.get("name")
                first_category = machin_form.cleaned_data.get("first_category")  
                price = machin_form.cleaned_data.get("price")
                tags = machin_form.cleaned_data.get("tags")
                description = machin_form.cleaned_data.get("description")
                image = machin_form.cleaned_data.get("image")
                videofile = machin_form.cleaned_data.get("videofile")
                machin_obj = Machines.objects.create(
                    cylinder_bed = cylinder_bed,
                    flat_bed = flat_bed,
                    ghab_mako = ghab_mako,
                    ghabeliat_dokht = ghabeliat_dokht,
                    mako = mako,
                    masore = masore,
                    sale_way = sale_way,
                    warranty = warranty,
                    masore_por = masore_por,
                    nakh = nakh,
                    pedal = pedal,
                    sozan_nakhkon = sozan_nakhkon,
                    tavan = tavan,
                    machin_weight = machin_weight,
                    type = type,
                    name = name,
                    user = user,
                    first_category = first_category,  
                    price = price,
                    description = description,
                    image = image,
                    videofile = videofile
                )
                machin_obj.save()
                
                messages.success(request,'کالا با موفقیت اضافه گردید.')
                return redirect('seller:list_production')
            else:
                messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
                return render(request, 'seller/add_machin.html', {'machin_form': machin_form})
        else:
            form = AddMachinForm()  
            
#------------------------------------------------------------ListProductionView------------------------------------------------------------

class ListProductionView(View):
    
    def get(self, request, *args, **kwargs):
        dresses = Dress.objects.all()
        context = {
            'dresses' : dresses
        }
        
        return render(request, 'seller/list_productions.html', context)
    
#-----------------------------------------------------------DetailProductionView------------------------------------------------------------

class DetailProductionView(View):
    
    def get(self, request, id, *args, **kwargs):
        dress = get_object_or_404(Dress,id=id)
        context = {
            'dress' : dress
        }
        
        return render(request, 'seller/detail_production.html', context)

#----------------------------------------------------------------AddTicket---------------------------------------------------------------
#----------------------------------------------------------------OpenTicket--------------------------------------------------------------

class OpenTicketView(View):
    
    def get(self, request, *args, **kwargs):
        form = OpenTicket()
        context = {
            'form': form
        }
        return render(request, 'seller/open_ticket.html', context)
    
    def post(self, request, *args, **kwargs):
        form = OpenTicket()
        if request.method == 'POST':
            form = OpenTicket(request.POST , request.FILES or None)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                description = form.cleaned_data.get('description')
                att_file = form.cleaned_data.get('att_file')
                user = request.user
                obj = Ticket.objects.create(
                    title = title,
                    description = description,
                    att_file = att_file,
                    user = user
                )
                obj.save()
                
                messages.success(request,'تیکت شما با موفقیت ثبت شد.')
                return redirect('seller:show_tickets')
            messages.error(request, 'با عرض پوزش، تیکت شما ثبت نشد.')
            return render(request, 'seller/open_ticket.html', {'form':form})
        else:
            form = OpenTicket()
            
#--------------------------------------------------------------ReplyTicket----------------------------------------------------------

class ReplyTicketView(View):
    
    def get(self, request, id, *args, **kwargs):
        user = request.user
        form = ReplyTicketForm()
        reply = get_object_or_404(TickComment, id=(2*id-1))
        context = {
            'reply' : reply,
            'form' : form 
        }
        return render(request, 'seller/reply_ticket.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ReplyTicketForm()
        if request.method == 'POST':
            form = ReplyTicketForm(request.POST, request.FILES or None)
            if form.is_valid():
                reply = form.cleaned_data.get('reply')
                att_file = form.cleaned_data.get('att_file')
                user = request.user
                ticket = get_object_or_404(Ticket,user = user)
                obj = TickComment.objects.create(
                    user = user,
                    reply = reply,
                    att_file = att_file,
                    ticket = ticket
                    
                )
                obj.save()
                
                messages.success(request,'تیکت شما با موفقیت ثبت شد.')
                return redirect('seller:show_tickets')
            messages.error(request,'با عرض پوزش تیکت شما ثبت نشد.')
            return render(request,'seller/reply_tickets.html')
        else:
            form = ReplyTicketForm()
        
            
#---------------------------------------------------------------ListTickets----------------------------------------------------------

class ShowTicket(View):
    
    def get(self, request, *args, **kwargs):
        #tickets = Ticket.objects.filter(seller=request.user)
        tickets = Ticket.objects.filter(user=request.user)
        context = {
            'tickets': tickets
        }
        return render(request, 'seller/show_tickets.html', context)
    
#---------------------------------------------------------------DetailTicket----------------------------------------------------------
    
class DetailTicket(View):
    
    def get(self, request, id, *args, **kwargs):
        ticket  = get_object_or_404(Ticket, id=id)
        context = {
            'ticket': ticket
        }
        return render(request, 'seller/detail_ticket.html', context)
