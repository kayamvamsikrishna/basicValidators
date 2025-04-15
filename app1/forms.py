from django import forms
from app1.models import *

#validators

'''
    1)Validators are used for validating the data
    They are 2 types:
        a)used defined /custom validators
            user defined validators are sub divided into two type
            1)normal functions
            2)form/modelform objects
                form methods are sub divided into two types
                1)clean
                2)clean_element
        b)built-in validators

'''
#example
def v1(n):#this function mandatorily take one argument
    if n[0]=='p': #by using indexing to extract the first element in the submitted data 
        pass
    else:
        raise forms.ValidationError('always first character equal to p')

def v2(n):#this function mandatorily take one argument
    if n.startswith('p') and n.endswith('j'): #string built-in method 
        pass
    else:
        raise forms.ValidationError('always first character equal to p')


def v3(n):#this function mandatorily take one argument
    if len(n)<=4: 
        pass
    else:
        raise forms.ValidationError('always length less than or  equal to 4')
    




import re
def v4(n):#this function mandatorily take one argument
    if re.findall('mo{2}n',n): #regular expressions #patern -  {} it represents size & o repeated in two times ------ findall output is list --- list with element a single element --- true
        print(re.findall('mo{2}n',n)) #['moon'] 
        pass
    else:
        raise forms.ValidationError





class SchoolInfoUI(forms.Form):
    schname=forms.CharField(max_length=100,validators=[v3])
    schlocation=forms.CharField(max_length=100,validators=[v1,v2,v3])#for one input element  we can perform multiple validtors
    schsubjects=forms.CharField(max_length=100)



#ModelForms:
class SchoolInfoUII(forms.ModelForm):
    class Meta:
        model=SchoolInfo
        fields='__all__'


class StudentInfoUI(forms.Form):
    schsubjects=forms.ModelChoiceField(queryset=SchoolInfo.objects.all())#dropdown list,...... based on the parent table primary key column i need to insert the data in the child table
    sttname=forms.CharField(max_length=100,validators=[v4])#validation happened
    sttgender=forms.CharField(max_length=100)
    sttage=forms.IntegerField()
    sttlocation=forms.CharField(max_length=100)


#ModelForms:
class StudentInfoUII(forms.ModelForm):
    class Meta:
        model=StudentInfo
        fields='__all__'


