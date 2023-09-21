from django.db import models

# Create your models here.
class Bank_Details(models.Model):
    account_no = models.IntegerField()
    bank_name = models.CharField(max_length=50)
    account_holder_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=15)

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to='profile_pic/')
    user_type = models.CharField(max_length=10)
    bank_details = models.ForeignKey(Bank_Details, on_delete=models.SET_NULL, null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
    last_login_timestamp = models.DateTimeField(auto_now_add=True)
    dob = models.DateField()

class Expert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=40)
    expert_bio = models.CharField(max_length=400)
    expert_location = models.CharField(max_length=100)
    expert_experience = models.IntegerField()
    expert_rating = models.IntegerField()

class Category(models.Model):
    category_name = models.CharField(max_length=30)

class Gig(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    show_case_image = models.ImageField(upload_to='Gig/')
    description = models.TextField()

class Review(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) ##to note
    expert = models.ForeignKey(Expert, on_delete=models.SET_NULL, null=True, blank=True)
    star_rating = models.IntegerField()
    review_text = models.CharField(max_length=2000)
    review_timestamp = models.DateField(auto_now_add=True)

class FAQ(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    question =models.CharField(max_length= 150)
    answer = models.CharField(max_length=1000)

class Replay(models.Model):
    review = models.ForeignKey(Review, on_delete=models.SET_NULL, null=True, blank=True)
    expert = models.ForeignKey(Expert, on_delete=models.SET_NULL, null=True, blank=True)
    reply = models.CharField(max_length=1000)
    reply_timestamp = models.DateField(auto_now_add=True)

class Gig_package(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE) 
    package_type = models.CharField(max_length=10)
    package_description = models.TextField()
    duration = models.TimeField()
    file_attachment = models.BooleanField()

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    expert = models.ForeignKey(Expert, on_delete=models.SET_NULL, null=True, blank=True)
    gig = models.ForeignKey(Gig, on_delete=models.SET_NULL, null=True, blank=True)
    gig_package = models.ForeignKey(Gig_package, on_delete=models.SET_NULL, null=True, blank=True)
    paymentlink = models.CharField(max_length=250)
    order_date = models.DateField(auto_now_add=True)
    order_Status = models.CharField(max_length=15)
    meeting_date_time = models.DateTimeField()
    previous_meeting_date_time= models.DateTimeField()
    meeting_update_timestamp = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(max_length=100)


class Expert_Catogery(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Wishlist(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)

class Call_Details(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)###to note
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    call_type = models.CharField(max_length=15)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    private = models.BooleanField()
    meet_image = models.ImageField(upload_to='proof/')
    meeting_text = models.TextField()
    audio = models.FileField(upload_to='proof/')

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField()
    status = models.BooleanField()