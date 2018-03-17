from django import forms


class PersonSave( forms.Form ):
    nameField = forms.CharField( label="이름" )
    person_number = forms.CharField( label="주민번호" )
    mail = forms.CharField( label="이메일" )
    phone_number = forms.CharField( label="전화번호" )
    address = forms.CharField( label="주소" )
    account = forms.CharField( label="계좌" )
    account_pw = forms.CharField( label="계좌비밀번호" )
