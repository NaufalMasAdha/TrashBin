from django import forms
from. import models

class BuatLaporan(forms.ModelForm):
    class Meta:
        model= models.Pelaporan
        fields =['Kecamatan', 'Alamat_Rinci', 'Gambar']
