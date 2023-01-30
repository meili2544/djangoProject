from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def myinfo(request):
    return render(request, 'Myinfo.html')
def education(request):
    return render(request, 'education.html')
def interest(request):
    return render(request, 'interest.html')
def career(request):
    return render(request, 'career.html')
def myidols(request):
    return render(request, 'idol.html')
def etc(request):
    return render(request, 'etc.html')
def lab10(request):
    name = "สิริยากร วรสุทธิ์"
    stdid = "65342310153-1"
    address = "ที่อยู่ 69 หมู่ 18 บ้านโคกม่วงม่วงทอง ต.นากอก อ.ศรีบุญเรือง จ.หนองบัวลำภู 39180 "
    gen = "หญิง"
    weight = "53"
    height = "159"
    color = "สีชมพู"
    food = "บาบีก้อน พลาซ่า"
    job = "นักศึกษา"
    productlist = [["ครีมทาผิว",150,"images/pd1.jpg"],
                   ["วาสลีน ลิป โรซี่ บำรุงริมฝีปาก",100,"images/pd2.jpg"],
                   ["ฟลูโอคารีล น้ำยาบ้วนปาก  ฟลูโอคารีล เกิร์ล รสสตรอเบอร์รี่  บิ๊กทีธ",150,"images/pd3.jpg"],
                   ["Johnson's จอห์นสัน เบบี้ ออยล์ เบดไทม์  ",89,"images/pd4.jpg"],
                   ["A เอ บอนเน่ เกลือสปา มิลค์ เกลือสปาขัดผิว ",30,"images/pd5.jpg"],
                   ["Sasi ศศิ แอคเน่ โซล ลูส พาวเดอร์",49,"images/pd6.jpg"],
                   ["Eversense เอเวอร์เซ้นส์ โรล ออน ",99,"images/pd7.jpg"],
                   ["Banobagi บาโนบากิ ไวต้า จีนิค เจลลี่ มาส์ก ",49,"images/pd8.jpg"],
                   ["Vaseline วาสลีน เฮลธีไบรท์ ซุปเปอร์ฟู้ด  ",200,"images/pd9.jpg"],
                   ["Choops จุ๊ปส์ ลิปแมท ",69,"images/pd10.jpg"],
                   ]
    return render(request, 'lab10.html', {'name': name, 'stdid': stdid, 'address': address, 'gen': gen,
                                              'weight': weight, 'height': height, 'color': color, 'food': food,
                                              'job': job, 'productlist': productlist})