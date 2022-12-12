from django import forms

class checkout_form(forms.Form):
    fullname=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control col-md-6"}),help_text="enter your full name",required=True)    
    City=[(1,'bhavnagar'),(2,'ahmedabad'),(3,"surat")]
    city=forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control col-md-6"}),label="Select your city ",choices=City,required=True)
    address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control col-md-12"}),label="Ente your address ")
    mobile=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control col-md-6"}),label="Enter your mobile number ",required=True)
    pincode=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control col-md-6"}),label="Enter your pincode ",required=True)
    