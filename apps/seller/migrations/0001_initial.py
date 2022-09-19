# Generated by Django 3.2.15 on 2022-09-19 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryGender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50, verbose_name='عنوان دسته')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=50, verbose_name='عنوان دسته')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')),
                ('gender', models.ManyToManyField(related_name='typestogender', to='seller.CategoryGender', verbose_name='جنسیت')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryWear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wear', models.CharField(max_length=50, verbose_name='عنوان دسته')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')),
                ('gender', models.ManyToManyField(related_name='weartogender', to='seller.CategoryGender', verbose_name='جنسیت')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='رنگ ها')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
            ],
        ),
        migrations.CreateModel(
            name='Nature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='جنس')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='تگ ها')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='موضوع تیکت')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('att_file', models.FileField(blank=True, null=True, upload_to='ticket_att/', verbose_name='فایل الصاق شده')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد تیکت')),
                ('status', models.BooleanField(default=True, verbose_name='وضعیت تیکت')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='TickToCustomUser', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
        migrations.CreateModel(
            name='TickComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.CharField(blank=True, max_length=50, null=True, verbose_name='پشتیان سایت')),
                ('reply', models.TextField(blank=True, null=True, verbose_name='پاسخ تیکت')),
                ('att_file', models.FileField(blank=True, null=True, upload_to='ticket_att/', verbose_name='فایل الصاق شده')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان پاسخگویی')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CommentToTicket', to='seller.ticket', verbose_name='تیکت')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CommentToUser', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'TikComment',
                'verbose_name_plural': 'TikComments',
            },
        ),
        migrations.CreateModel(
            name='SellerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('مرد', 'مرد'), ('زن', 'زن')], max_length=50, null=True, verbose_name='جنسیت')),
                ('birthdate', models.DateField(blank=True, max_length=50, null=True, verbose_name='تاریخ تولد')),
                ('address', models.TextField(blank=True, max_length=50, null=True, verbose_name='آدرس')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sellertocustom', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام محصول')),
                ('first_category', models.CharField(blank=True, choices=[('البسه و پوشاک', 'البسه و پوشاک'), ('تجهیزات دوخت', 'تجهیزات دوخت'), ('ماشین آلات', 'ماشین آلات')], max_length=50, null=True, verbose_name='دسته بندی')),
                ('price', models.CharField(max_length=50, verbose_name='قیمت')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pro_img/', verbose_name='تصویر کالا')),
                ('videofile', models.FileField(blank=True, null=True, upload_to='pro_video/', verbose_name='ویدئو از کالا')),
                ('cylinder_bed', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=100, verbose_name='صفحه کار استوانه ای')),
                ('flat_bed', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=100, verbose_name='صفحه کار تخت')),
                ('sale_way', models.CharField(choices=[('یک دستگاه', 'یک دستگاه')], max_length=100, verbose_name='نحوه فروش')),
                ('warranty', models.CharField(choices=[('توسط کارخانه', 'توسط کارخانه'), ('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=100, verbose_name='گارانتی')),
                ('ghab_mako', models.CharField(choices=[('کمپلت تمام دورک', 'کمپلت تمام دورک'), ('کمپلت نیم دور', 'کمپلت نیم دور')], max_length=100, verbose_name='سیستم قاب ماکو')),
                ('ghabeliat_dokht', models.CharField(choices=[('اتوماتیک', 'اتوماتیک'), ('تمام خود کار بدون کاربر', 'تمام خود کار بدون کاربر'), ('دستی', 'دستی'), ('نیمه اتومات', 'نیمه اتومات')], max_length=50, verbose_name='قابلیت دوخت')),
                ('mako', models.CharField(choices=[('کمپلت تمام دور(کمپلت صنعتی)', 'کمپلت تمام دور(کمپلت صنعتی)'), ('کمپلت نیم دور', 'کمپلت نیم دور')], max_length=100, verbose_name='ماکو')),
                ('masore', models.CharField(choices=[('پلاستیکی', 'پلاستیکی'), ('شیشه ایی', 'شیشه ایی'), ('فلزی', 'فلزی')], max_length=100, verbose_name='ماسوره')),
                ('masore_por', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=100, verbose_name='ماسوره پر کن')),
                ('nakh', models.CharField(choices=[('ابریشمی با روکش فلزی (گلابتون)', 'ابریشمی با روکش فلزی (گلابتون)'), ('پولیستری', 'پولیستری'), ('ریونی', 'ریونی'), ('عمامه ای (ابریشمی و پنبه ای)', 'عمامه ای (ابریشمی و پنبه ای)'), ('کاموایی', 'کاموایی'), ('کتانی', 'کتانی'), ('کنفی', 'کنفی'), ('کوبلن دوزی و مِز', 'کوبلن دوزی و مِز'), ('لمه', 'لمه'), ('نایلونی', 'نایلونی'), ('نخ ابریشم', 'نخ ابریشم'), ('نخ پشمی', 'نخ پشمی'), ('نخ پنبه', 'نخ پنبه'), ('نخ دکمه', 'نخ دکمه'), ('نخ دمسه', 'نخ دمسه'), ('نخ سر کیسه دوزی', 'نخ سر کیسه دوزی'), ('نخ سردوزی', 'نخ سردوزی'), ('نخ فاستونی', 'نخ فاستونی'), ('نخ فلزی', 'نخ فلزی'), ('نخ قیطان', 'نخ قیطان'), ('نخ گلدوزی', 'نخ گلدوزی'), ('نخ متالیک', 'نخ متالیک'), ('نخ همه منظوره(پولیستر)', 'نخ همه منظوره(پولیستر)'), ('غیره', 'غیره')], max_length=100, verbose_name='نخ مورد استفاده دستگاه')),
                ('pedal', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=100, verbose_name='پدال')),
                ('sozan_nakhkon', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=100, verbose_name='سوزن نخ کن')),
                ('tavan', models.CharField(choices=[('خانگی', 'خانگی'), ('صنعتی', 'صنعتی'), ('نیمه صنعتی', 'نیمه صنعتی')], max_length=100, verbose_name='توان ساعت و حجم کار دستگاه')),
                ('machin_weight', models.CharField(choices=[('کمتر از 5 کیلو گرم', 'کمتر از 5 کیلو گرم'), ('کمتر از 10 کیلوگرم', 'کمتر از 10 کیلوگرم'), ('کمتر از 15 کیلوگرم', 'کمتر از 15 کیلوگرم'), ('کمتر از 20 کیلوگرم', 'کمتر از 20 کیلوگرم'), ('کمتر از 40 کیلوگرم', 'کمتر از 40 کیلوگرم'), ('بیشتر از 40 کیلو گرم زیر 100 کیلوگرم', 'بیشتر از 40 کیلو گرم زیر 100 کیلوگرم'), ('بیشتر از 100 کیلو گرم', 'بیشتر از 100 کیلو گرم')], max_length=100, verbose_name='وزن دستگاه')),
                ('type', models.CharField(choices=[('چرخ خیاطی Post-bed', 'چرخ خیاطی Post-bed'), ('چرخ خیاطی با قابلیت گلدوزی', 'چرخ خیاطی با قابلیت گلدوزی'), ('چرخ خیاطی بدون دسته (Off-the-arm)', 'چرخ خیاطی بدون دسته (Off-the-arm)'), ('چرخ خیاطی دارای صفحه کار استوانه\u200cای (Cylinder Bed)', 'چرخ خیاطی دارای صفحه کار استوانه\u200cای (Cylinder Bed)'), ('چرخ خیاطی دارای صفحه کار تخت (Flat-bed)', 'چرخ خیاطی دارای صفحه کار تخت (Flat-bed)'), ('چرخ خیاطی دستی', 'چرخ خیاطی دستی'), ('چرخ خیاطی دو سوزنه', 'چرخ خیاطی دو سوزنه'), ('چرخ خیاطی سردوز (Overlock)', 'چرخ خیاطی سردوز (Overlock)'), ('چرخ خیاطی قابل حمل', 'چرخ خیاطی قابل حمل'), ('چرخ خیاطی کامپیوتری', 'چرخ خیاطی کامپیوتری'), ('چرخ\u200cهای خیاطی جادکمه زن', 'چرخ\u200cهای خیاطی جادکمه زن')], max_length=100, verbose_name='نوع چرخ خیاطی')),
                ('tags', models.ManyToManyField(related_name='machintotag', to='seller.Tag', verbose_name='تگ ها')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machintocustomuser', to=settings.AUTH_USER_MODEL, verbose_name='تولید کننده')),
            ],
        ),
        migrations.CreateModel(
            name='FinalCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان دسته')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')),
                ('gender', models.ManyToManyField(related_name='finaltogender', to='seller.CategoryGender', verbose_name='جنسیت')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finaltotypes', to='seller.categorytypes', verbose_name='انواع')),
                ('wear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finaltowear', to='seller.categorywear', verbose_name='پوشاک')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_category', models.CharField(blank=True, choices=[('البسه و پوشاک', 'البسه و پوشاک'), ('تجهیزات دوخت', 'تجهیزات دوخت'), ('ماشین آلات', 'ماشین آلات')], max_length=50, null=True, verbose_name='دسته بندی')),
                ('price', models.CharField(max_length=50, verbose_name='قیمت')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pro_img/', verbose_name='تصویر کالا')),
                ('videofile', models.FileField(blank=True, null=True, upload_to='pro_video/', verbose_name='ویدئو از کالا')),
                ('name', models.CharField(max_length=50, verbose_name='نوع تجهیز')),
                ('weidth', models.CharField(choices=[('بر حسب متر', 'بر حسب متر'), ('بر حسب یارد', 'بر حسب یارد')], max_length=100, verbose_name='عرض طاقه پارچه')),
                ('colors_num', models.CharField(choices=[('تک رنگ', 'تک رنگ'), ('2 رنگ', '2 رنگ'), ('3 رنگ', '3 رنگ'), ('4 رنگ', '4 رنگ'), ('5 رنگ', '5 رنگ'), ('6 رنگ', '6 رنگ'), ('7 رنگ', '7 رنگ'), ('8 رنگ', '8 رنگ'), ('9 رنگ', '9 رنگ'), ('10 رنگ', '10 رنگ'), ('11 رنگ', '11 رنگ'), ('12 رنگ', '12 رنگ'), ('13 رنگ', '13 رنگ'), ('14 رنگ', '14 رنگ'), ('15 رنگ', '15 رنگ'), ('16 رنگ', '16 رنگ'), ('17 رنگ', '17 رنگ'), ('18 رنگ', '18 رنگ'), ('19 رنگ', '19 رنگ'), ('20 رنگ', '20 رنگ'), ('21 رنگ', '21 رنگ'), ('22 رنگ', '22 رنگ'), ('23 رنگ', '23 رنگ'), ('24 رنگ', '24 رنگ'), ('24 رنگ و بیشتر', '24 رنگ و بیشتر')], max_length=100, verbose_name='تعداد رنگبندی')),
                ('sale_way', models.CharField(choices=[('به صورت طاقه تک', 'به صورت طاقه تک'), ('به صورت عدلی', 'به صورت عدلی')], max_length=100, verbose_name='نحوه فروش')),
                ('warranty', models.CharField(choices=[('توسط کارخانه', 'توسط کارخانه'), ('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=100, verbose_name='گارانتی')),
                ('using', models.CharField(choices=[('البسه', 'البسه'), ('تزیینی', 'تزیینی'), ('مبلمان', 'مبلمان')], max_length=100, verbose_name='کاربرد پارچه')),
                ('washing_point', models.CharField(choices=[('ابریشم:پارچه پیچانده یا فشرده نشود', 'ابریشم:پارچه پیچانده یا فشرده نشود'), ('پارچه پنبه:پارچه پیچانده یا فشرده نشود', 'پارچه پنبه:پارچه پیچانده یا فشرده نشود'), ('به صورت مجزا شسته شوند.', 'به صورت مجزا شسته شوند.'), ('پارچه نایلون:پارچه نباید زیر تابش مستقیم خورشید خشک گردد', 'پارچه نایلون:پارچه نباید زیر تابش مستقیم خورشید خشک گردد'), ('پارچه پیچانده یا فشرده نشود', 'پارچه پیچانده یا فشرده نشود'), ('چاندری (Chanderi), چیفون (Chiffon):خشک کردن در هوای باز نسبت به خشک کردن زیر نور خورشید برای این پارچه ترجیح داده می شود., در آب سرد با مواد شوینده ملایم باید مورد شستشو قرار گیرد., در دمای کم باید اتو شوند.', 'چاندری (Chanderi), چیفون (Chiffon):خشک کردن در هوای باز نسبت به خشک کردن زیر نور خورشید برای این پارچه ترجیح داده می شود., در آب سرد با مواد شوینده ملایم باید مورد شستشو قرار گیرد., در دمای کم باید اتو شوند.'), ('ریون (Rayon), ژرژت (Georgette), ساتن:شستشو با اب سرد, شستشو به وسیله ماشین توصیه نمی شود, شستشوی خانگی, شستشوی دستی', 'ریون (Rayon), ژرژت (Georgette), ساتن:شستشو با اب سرد, شستشو به وسیله ماشین توصیه نمی شود, شستشوی خانگی, شستشوی دستی'), ('کرپ (Crepe), کوتا دوریا (Kota Doria), لیزی بیزی (Lizzy Bizzy), لینن (Linen), مودال ساتن (Modal Satin), موسلین (Muslin):شستوشو با آب گرم, شستوشو با ماشین, فقط به صورت خشک شسته شود و حتی شستشوی معمولی هم می تواند به پارچه آسیب بزند', 'کرپ (Crepe), کوتا دوریا (Kota Doria), لیزی بیزی (Lizzy Bizzy), لینن (Linen), مودال ساتن (Modal Satin), موسلین (Muslin):شستوشو با آب گرم, شستوشو با ماشین, فقط به صورت خشک شسته شود و حتی شستشوی معمولی هم می تواند به پارچه آسیب بزند')], max_length=500, verbose_name='نکات شستشو')),
                ('height', models.CharField(choices=[('متر', 'متر'), ('یارد', 'یارد')], max_length=100, verbose_name='طول طاق پارچه')),
                ('design', models.CharField(choices=[('تارتان (پارچه اسکاتلندی)', 'تارتان (پارچه اسکاتلندی)'), ('چریکی-جنگلی', 'چریکی-جنگلی'), ('چهارخانه', 'چهارخانه'), ('خال\u200cخالی', 'خال\u200cخالی'), ('خطوط شکسته', 'خطوط شکسته'), ('خطوط مایل', 'خطوط مایل'), ('راه\u200c راه', 'راه\u200c راه'), ('ساده', 'ساده'), ('طرح ارتشی', 'طرح ارتشی'), ('طرح بته\u200c جقه', 'طرح بته\u200c جقه'), ('طرح نوشته', 'طرح نوشته'), ('کارتونی', 'کارتونی'), ('گل\u200cگلی', 'گل\u200cگلی'), ('گلدار', 'گلدار'), ('نقش و نگار\u200cدار', 'نقش و نگار\u200cدار'), ('طرحدار', 'طرحدار')], max_length=100, verbose_name='طرح')),
                ('weight', models.CharField(choices=[], max_length=100, verbose_name='وزن پارچه')),
                ('tissue_density', models.CharField(choices=[('بافت توری', 'بافت توری'), ('بافت دانه گندمی', 'بافت دانه گندمی'), ('بافت ساتن یا ساتین', 'بافت ساتن یا ساتین'), ('بافت ساده یا تافته', 'بافت ساده یا تافته'), ('بافت سرژه', 'بافت سرژه'), ('بافت کائوچو', 'بافت کائوچو'), ('بافت کرپ پوری', 'بافت کرپ پوری'), ('بافت کرپ تاری', 'بافت کرپ تاری'), ('بافت کرد', 'بافت کرد')], max_length=100, verbose_name='تراکم بافت')),
                ('colors', models.ManyToManyField(related_name='equipmenttocolor', to='seller.Color', verbose_name='رنگبندی')),
                ('nature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipmenttonature', to='seller.nature', verbose_name='جنس')),
                ('tags', models.ManyToManyField(related_name='equipmenttotag', to='seller.Tag', verbose_name='تگ ها')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipmenttocustomuser', to=settings.AUTH_USER_MODEL, verbose_name='تولید کننده')),
            ],
        ),
        migrations.CreateModel(
            name='EccoInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100, verbose_name='نام برند')),
                ('owner', models.CharField(blank=True, max_length=50, null=True, verbose_name='صاحب برند')),
                ('category', models.CharField(choices=[('پوشاک', 'البسه و پوشاک'), ('خیاطی', 'چرخ خیاطی و ملزومات آن'), ('کفش', 'کفش')], max_length=50, verbose_name='نوع کالا')),
                ('sheba_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره شبا')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('lawful_candid_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='نام و نام خانوادگی نماینده قانونی')),
                ('lawful_candid_nationalcode', models.CharField(blank=True, max_length=10, null=True, verbose_name='کد ملی نماینده قانونی')),
                ('lawful_candid_phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='شماره تماس نماینده قانونی')),
                ('lawful_candid_image', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='آپلود عکس کارت ملی')),
                ('certificate_image', models.ImageField(upload_to='comm_sign/', verbose_name='آپلود تصویر گواهینامه ثبت علامت تجاری')),
                ('logo_image', models.ImageField(upload_to='favicon/', verbose_name='آپلود تصویر لوگو')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='eccotocustom', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام محصول')),
                ('first_category', models.CharField(blank=True, choices=[('البسه و پوشاک', 'البسه و پوشاک'), ('تجهیزات دوخت', 'تجهیزات دوخت'), ('ماشین آلات', 'ماشین آلات')], max_length=50, null=True, verbose_name='دسته بندی')),
                ('price', models.CharField(max_length=50, verbose_name='قیمت')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pro_img/', verbose_name='تصویر کالا')),
                ('videofile', models.FileField(blank=True, null=True, upload_to='pro_video/', verbose_name='ویدئو از کالا')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'XLarge'), ('XXL', 'XXLarge'), ('XXXL', 'XXXLarge')], max_length=50, verbose_name='سایز')),
                ('numbers', models.IntegerField(verbose_name='تعداد')),
                ('sleeve', models.CharField(choices=[('آستین آرنج وصله\u200cدار', 'آستین آرنج وصله\u200cدار'), ('آستین آویخته', 'آستین آویخته'), ('آستین اپل\u200cدار', 'آستین اپل\u200cدار'), ('آستین بدون سرشانه', 'آستین بدون سرشانه'), ('آستین پروانه\u200cای', 'آستین پروانه\u200cای'), ('آستین خفاشی بلند', 'آستین خفاشی بلند'), ('آستین ژولیت', 'آستین ژولیت'), ('آستین سه\u200cربع یا النگویی', 'آستین سه\u200cربع یا النگویی'), ('آستین فانوسی', 'آستین فانوسی'), ('آستین گلبرگی (لاله\u200cای)', 'آستین گلبرگی (لاله\u200cای)'), ('استین بلند', 'استین بلند'), ('استین کوتاه', 'استین کوتاه'), ('بدون استین', 'بدون استین')], max_length=100, verbose_name='نوع آستین')),
                ('close_way', models.CharField(choices=[('بند', 'بند'), ('دکمه', 'دکمه'), ('زیپ', 'زیپ'), ('زیپ دکمه', 'زیپ دکمه'), ('کش', 'کش'), ('گیره', 'گیره')], max_length=100, verbose_name='نحوه بسته شدن')),
                ('colors_num', models.CharField(choices=[('تک رنگ', 'تک رنگ'), ('2 رنگ', '2 رنگ'), ('3 رنگ', '3 رنگ'), ('4 رنگ', '4 رنگ'), ('5 رنگ', '5 رنگ'), ('6 رنگ', '6 رنگ'), ('7 رنگ', '7 رنگ'), ('8 رنگ', '8 رنگ'), ('9 رنگ', '9 رنگ'), ('10 رنگ', '10 رنگ'), ('11 رنگ', '11 رنگ'), ('12 رنگ', '12 رنگ'), ('13 رنگ', '13 رنگ'), ('14 رنگ', '14 رنگ'), ('15 رنگ', '15 رنگ'), ('16 رنگ', '16 رنگ'), ('17 رنگ', '17 رنگ'), ('18 رنگ', '18 رنگ'), ('19 رنگ', '19 رنگ'), ('20 رنگ', '20 رنگ'), ('21 رنگ', '21 رنگ'), ('22 رنگ', '22 رنگ'), ('23 رنگ', '23 رنگ'), ('24 رنگ', '24 رنگ'), ('24 رنگ و بیشتر', '24 رنگ و بیشتر')], max_length=100, verbose_name='تعداد رنگبندی')),
                ('crotch', models.CharField(choices=[('فاق بلند', 'فاق بلند'), ('فاق کوتاه', 'فاق کوتاه'), ('فاق متوسط', 'فاق متوسط')], max_length=100, verbose_name='نوع فاق')),
                ('sale_way', models.CharField(choices=[('به صورت سری رنگ', 'به صورت سری رنگ'), ('به صورت سری رنگ با تعداد سایز بندی', 'به صورت سری رنگ با تعداد سایز بندی')], max_length=100, verbose_name='نحوه فروش')),
                ('warranty', models.CharField(choices=[('توسط کارخانه', 'توسط کارخانه'), ('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=100, verbose_name='گارانتی')),
                ('pocket', models.CharField(choices=[('دارد', 'دارد'), ('تک جیب', 'تک جیب'), ('دو جیب', 'دو جیب'), ('چهار جیب', 'چهار جیب'), ('چهار جیب', 'چهار جیب'), ('شش جیب', 'شش جیب'), ('هشت جیب و بیشتر', 'هشت جیب و بیشتر'), ('ندارد', 'ندارد')], max_length=100, verbose_name='جیب')),
                ('hat', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=100, verbose_name='کلاه')),
                ('washing_point', models.CharField(choices=[('ابریشم:پارچه پیچانده یا فشرده نشود', 'ابریشم:پارچه پیچانده یا فشرده نشود'), ('پارچه پنبه:پارچه پیچانده یا فشرده نشود', 'پارچه پنبه:پارچه پیچانده یا فشرده نشود'), ('به صورت مجزا شسته شوند.', 'به صورت مجزا شسته شوند.'), ('پارچه نایلون:پارچه نباید زیر تابش مستقیم خورشید خشک گردد', 'پارچه نایلون:پارچه نباید زیر تابش مستقیم خورشید خشک گردد'), ('پارچه پیچانده یا فشرده نشود', 'پارچه پیچانده یا فشرده نشود'), ('چاندری (Chanderi), چیفون (Chiffon):خشک کردن در هوای باز نسبت به خشک کردن زیر نور خورشید برای این پارچه ترجیح داده می شود., در آب سرد با مواد شوینده ملایم باید مورد شستشو قرار گیرد., در دمای کم باید اتو شوند.', 'چاندری (Chanderi), چیفون (Chiffon):خشک کردن در هوای باز نسبت به خشک کردن زیر نور خورشید برای این پارچه ترجیح داده می شود., در آب سرد با مواد شوینده ملایم باید مورد شستشو قرار گیرد., در دمای کم باید اتو شوند.'), ('ریون (Rayon), ژرژت (Georgette), ساتن:شستشو با اب سرد, شستشو به وسیله ماشین توصیه نمی شود, شستشوی خانگی, شستشوی دستی', 'ریون (Rayon), ژرژت (Georgette), ساتن:شستشو با اب سرد, شستشو به وسیله ماشین توصیه نمی شود, شستشوی خانگی, شستشوی دستی'), ('کرپ (Crepe), کوتا دوریا (Kota Doria), لیزی بیزی (Lizzy Bizzy), لینن (Linen), مودال ساتن (Modal Satin), موسلین (Muslin):شستوشو با آب گرم, شستوشو با ماشین, فقط به صورت خشک شسته شود و حتی شستشوی معمولی هم می تواند به پارچه آسیب بزند', 'کرپ (Crepe), کوتا دوریا (Kota Doria), لیزی بیزی (Lizzy Bizzy), لینن (Linen), مودال ساتن (Modal Satin), موسلین (Muslin):شستوشو با آب گرم, شستوشو با ماشین, فقط به صورت خشک شسته شود و حتی شستشوی معمولی هم می تواند به پارچه آسیب بزند')], max_length=500, verbose_name='نکات شستشو')),
                ('style', models.CharField(choices=[('اسپرت', 'اسپرت'), ('رسمی', 'رسمی'), ('روزمره', 'روزمره'), ('کلاسیک', 'کلاسیک'), ('مجلسی', 'مجلسی')], max_length=100, verbose_name='استایل')),
                ('design', models.CharField(choices=[('تارتان (پارچه اسکاتلندی)', 'تارتان (پارچه اسکاتلندی)'), ('چریکی-جنگلی', 'چریکی-جنگلی'), ('چهارخانه', 'چهارخانه'), ('خال\u200cخالی', 'خال\u200cخالی'), ('خطوط شکسته', 'خطوط شکسته'), ('خطوط مایل', 'خطوط مایل'), ('راه\u200c راه', 'راه\u200c راه'), ('ساده', 'ساده'), ('طرح ارتشی', 'طرح ارتشی'), ('طرح بته\u200c جقه', 'طرح بته\u200c جقه'), ('طرح نوشته', 'طرح نوشته'), ('کارتونی', 'کارتونی'), ('گل\u200cگلی', 'گل\u200cگلی'), ('گلدار', 'گلدار'), ('نقش و نگار\u200cدار', 'نقش و نگار\u200cدار'), ('طرحدار', 'طرحدار')], max_length=100, verbose_name='طرح')),
                ('spatial_feature', models.CharField(choices=[], max_length=100, verbose_name='ویژگی های تخصصی')),
                ('collar', models.CharField(choices=[('دیپلمات', 'دیپلمات'), ('گرد', 'گرد'), ('یقه آرشال', 'یقه آرشال'), ('یقه اسکی', 'یقه اسکی'), ('یقه انگلیسی', 'یقه انگلیسی'), ('یقه ایرانی', 'یقه ایرانی'), ('یقه ب.ب', 'یقه ب.ب'), ('یقه بلیزری', 'یقه بلیزری'), ('یقه چهارگوش (خشتی)', 'یقه چهارگوش (خشتی)'), ('یقه چینی', 'یقه چینی'), ('یقه دراپه', 'یقه دراپه'), ('یقه شکاری', 'یقه شکاری'), ('یقه شومیزی', 'یقه شومیزی'), ('یقه فانتزی', 'یقه فانتزی'), ('یقه فرنچی', 'یقه فرنچی'), ('یقه قایقی (بلمی، کشتی)', 'یقه قایقی (بلمی، کشتی)'), ('یقه لباس ایستاده', 'یقه لباس ایستاده'), ('یقه ملوانی', 'یقه ملوانی'), ('یقه هفت', 'یقه هفت'), ('یقه ساده', 'یقه ساده')], max_length=100, verbose_name='یقه')),
                ('colors', models.ManyToManyField(related_name='dresstocolor', to='seller.Color', verbose_name='رنگبندی')),
                ('genders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dresstogender', to='seller.categorygender', verbose_name='جنسیت')),
                ('nature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dresstonature', to='seller.nature', verbose_name='جنس')),
                ('tags', models.ManyToManyField(related_name='dresstotag', to='seller.Tag', verbose_name='تگ ها')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dersstotypes', to='seller.categorytypes', verbose_name='نام پوشیدنی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dresstocustomuser', to=settings.AUTH_USER_MODEL, verbose_name='تولید کننده')),
                ('wears', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dresstowear', to='seller.categorywear', verbose_name='نوع پوشیدنی')),
            ],
        ),
        migrations.AddField(
            model_name='categorytypes',
            name='wear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='typestowear', to='seller.categorywear', verbose_name='پوشاک'),
        ),
    ]
